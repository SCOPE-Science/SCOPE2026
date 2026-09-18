# A one-parameter maximal-rank family with a rank-two middle summand

## Result

For every rational parameter \(u\in\mathbb Q\setminus\{\pm1\}\), consider
\[
E_u:\qquad y^2=x^3+16t^6+8u(9-u^2)t^3-27(u^2-1)^2.
\]
Then
\[
\operatorname{rank}E_u(\mathbb Q(t))=3.
\]
Moreover, under the three-summand decomposition in Bao's rank formula for
\(y^2=x^3+At^6+Bt^3+C\), the ranks are exactly
\[
(\operatorname{rank}E_1,\operatorname{rank}E_2,\operatorname{rank}E_3)=(1,2,0).
\]
Bao proves that rank \(3\) is the largest possible rank in this class. Thus the curves above form a rational one-parameter family of maximal-rank surfaces whose rank-two contribution is the non-degenerate middle summand.

Bao's Section 6 gives parametric rank-three examples of type \((1,1,1)\), but its Example 6.4 gives only one numerical example of type \((1,2,0)\), namely \((A,B,C)=(16,280,-972)\). The family above supplies an infinite rational family for that second mechanism.

## Proof

Write
\[
d=u^2-1,\qquad D=\sqrt{-3},
\]
and set
\[
A=16,\qquad B=8u(9-u^2),\qquad C=-27d^2.
\]
For \(u\ne\pm1\), both \(A\) and \(C\) are nonzero. Choose
\[
\sqrt A=4,\qquad \sqrt C=3dD\in\mathbb Q(D)=\mathbb Q(\omega).
\]
A direct calculation gives
\[
\Delta:=B^2-4AC=64(u^2+3)^3,
\]
so \(\Delta\ne0\).

### The first summand has rank one

Bao's Theorem 1.3(b) gives rank one precisely when \(\sqrt A\in\mathbb Q(\omega)\setminus\{0\}\) and \(\Delta/(4A)\) is a nonzero cube in \(\mathbb Q(\omega)\). Here
\[
\frac{\Delta}{4A}=(u^2+3)^3,
\]
so
\[
\operatorname{rank}E_1(\mathbb Q(t))=1.
\]

### The middle summand has rank two

Bao's non-degenerate rank-two criterion asks, in addition to \(\sqrt A,\sqrt C\in\mathbb Q(\omega)\), that
\[
2\sqrt A\sqrt C-B,
\qquad
-2\sqrt A\sqrt C-B
\]
be cubes in \(\mathbb Q(\omega)\). In the present family the two required identities are
\[
2\sqrt A\sqrt C-B=[2(u+D)]^3,
\]
\[
-2\sqrt A\sqrt C-B=[2(u-D)]^3.
\]
Therefore
\[
\operatorname{rank}E_2(\mathbb Q(t))=2.
\]

One of the corresponding rational sections on \(E_u\) can be written explicitly as
\[
P_2(t)=\left(
\frac{9d^2}{4t^2}-4ut,
-4t^3+9ud-\frac{27d^3}{8t^3}
\right).
\]
It is obtained from the \(P+Q\) generator in Bao's Theorem 1.4 and the decomposition map. The first summand similarly gives
\[
P_1(t)=\bigl(u^2+3,\ 4t^3+u(9-u^2)\bigr).
\]
Both displayed points satisfy the equation of \(E_u\) identically.

### The third summand has rank zero

Bao's Theorem 1.3(d) says that the third summand has rank one exactly when \(\sqrt C\ne0\) lies in \(\mathbb Q(\omega)\) and
\[
\frac{\Delta}{4C}
\]
is a cube in \(\mathbb Q(\omega)\). The source proves that a rational number is a cube in \(\mathbb Q(\omega)\) if and only if it is already a cube in \(\mathbb Q\). Here
\[
\frac{\Delta}{4C}
=-\frac{16(u^2+3)^3}{27(u^2-1)^2}
=\left(-\frac{u^2+3}{3}\right)^3\frac{16}{d^2}.
\]
Hence the third summand would have rank one exactly when \(16/d^2\) is a rational cube.

The condition
\[
\frac{16}{d^2}\in\mathbb Q^{\times3}
\]
is equivalent to the existence of \(r\in\mathbb Q\) such that
\[
d=4r^3.
\]
Indeed, one direction is immediate, while if \(16/d^2=s^3\), then \(r=ds/4\) satisfies \(r^3=d/4\). Thus a putative rank-one third summand yields
\[
u^2-1=4r^3.
\]
With
\[
X=4r,\qquad Y=4u,
\]
this becomes the Mordell curve
\[
Y^2=X^3+16.
\]
The LMFDB curve 27.a4 is the curve \(Y^2=X^3+16\); it has Mordell--Weil rank \(0\) and torsion group \(\mathbb Z/3\mathbb Z\). Consequently its rational points are the point at infinity and the two nontrivial torsion points \((0,\pm4)\). These give only \(u=\pm1\), which were excluded. Therefore \(\Delta/(4C)\) is not a cube and
\[
\operatorname{rank}E_3(\mathbb Q(t))=0.
\]

Bao's decomposition now gives
\[
\operatorname{rank}E_u(\mathbb Q(t))=1+2+0=3.
\]
By Bao's Proposition 6.1, rank \(3\) is maximal in the full \(At^6+Bt^3+C\) class.

## Structural remarks

The family is not merely a constant rescaling of one fixed coefficient triple. For example, the dimensionless quantity
\[
\frac{B^2}{AC}
=-\frac{4}{27}\frac{u^2(9-u^2)^2}{(u^2-1)^2}
\]
is nonconstant in \(u\). The special value \(u=0\) gives the particularly simple maximal-rank surface
\[
y^2=x^3+16t^6-27.
\]
The values \(u=\pm1\) are excluded because \(C=0\) and the non-degenerate decomposition used above changes.

## Verification

`artifacts/verify.py` uses exact symbolic arithmetic to verify the discriminant factorization, both cubic identities in \(\mathbb Q(\sqrt{-3})\), the reduction of the third-summand cube condition, the two displayed rational sections, and the substitution into \(Y^2=X^3+16\). The Mordell--Weil rank and torsion data for the final Mordell curve are taken from LMFDB 27.a4 rather than recomputed by the artifact.

## Limitations

The rank conclusion uses Bao's Theorem 1.3 and Proposition 6.1 as established inputs, and the final exclusion uses the LMFDB Mordell--Weil data for curve 27.a4. No independent reproof of those source results is claimed. The originality assessment is to the best of our knowledge. The motivating preprint is very recent, so contemporaneous work that is not yet indexed remains a residual risk. No claim is made that this parametrization exhausts all rank-three triples of decomposition type \((1,2,0)\), nor that different rational parameters always give non-isomorphic elliptic surfaces.

## References

1. Zhengheng Bao, *A formula for the rank over Q(t) of the elliptic curve y^2=x^3+At^6+Bt^3+C*, arXiv:2609.16349v1 (2026). https://arxiv.org/abs/2609.16349
2. LMFDB, elliptic curve 27.a4 (Cremona 27a3), simplified model \(y^2=x^3+16\). https://www.lmfdb.org/EllipticCurve/Q/27/a/4
3. Julie Desjardins and Bartosz Naskręcki, *Geometry of the del Pezzo surface y^2=x^3+Am^6+Bn^6*, Ann. Inst. Fourier 74 (2024), 2231--2274. https://doi.org/10.5802/aif.3635
4. Remke Kloosterman, *Determining explicitly the Mordell--Weil group of certain rational elliptic surfaces*, Indag. Math. (2026); arXiv:2506.19423. https://arxiv.org/abs/2506.19423
