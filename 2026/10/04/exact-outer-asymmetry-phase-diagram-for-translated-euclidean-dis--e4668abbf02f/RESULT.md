# Exact outer-asymmetry phase diagram for translated Euclidean disks

## Finding

Let
\[
K_a=B((a,0),1)\subset\mathbb R^2,\qquad 0\le a<1,
\]
and let \(\gamma_a\) be the Minkowski gauge having \(K_a\) as its unit disk. Let \(c_{\mathrm{out}}(\gamma_a)\) be the constant of outer asymmetry introduced by Balestro, Martini, and Teixeira.

Define \(a_0\in(0,1)\) as the unique positive root of
\[
4a_0^6+7a_0^4-2a_0^2-1=0.
\]
Numerically,
\[
a_0\approx0.6833726274004417.
\]
For \(a>a_0\), define
\[
y_*(a)=
\frac{
3a^4+18a^2-5-(1-a^2)\sqrt{9a^4-2a^2+57}
}{16a^2}.
\]
Then
\[
c_{\mathrm{out}}(\gamma_a)
=
\frac{8a(1-a^2)^{3/2}}{\pi}
\begin{cases}
1+a^2,
&
0\le a\le a_0,
\\[2mm]
\displaystyle
\sqrt{
\frac{
(1-y_*)((1+a^2)^2-4a^2y_*)
}{
(1-a^2y_*)^4
}
},
&
a_0<a<1.
\end{cases}
\]

The location of the maximizing boundary point changes at \(a_0\). If
\[
x(t)=(a+\cos t,\sin t),
\qquad
z=\frac{\cos t+a}{1+a\cos t},
\]
then a maximum has \(z=0\) for \(0\le a\le a_0\), whereas for \(a>a_0\) the maximizing pair is characterized by
\[
z^2=y_*(a).
\]
Thus this canonical one-parameter gauge family has a genuine extremizer bifurcation.

Across the whole translated-disk family,
\[
\max_{0\le a<1} c_{\mathrm{out}}(\gamma_a)
=
\frac{64\sqrt2}{27\pi}
\approx1.067041559889904,
\]
and the maximum is attained uniquely at
\[
a=\frac1{\sqrt3}.
\]

## Assumptions and scope

The Euclidean disk has radius \(1\); changing its radius does not create a new gauge up to linear scaling, so \(a\) is the normalized displacement of the Euclidean center from the gauge origin. The condition \(a<1\) is exactly what makes the origin an interior point of \(K_a\).

The constant \(c_{\mathrm{out}}\) is the original, non-normalized outer asymmetry constant of Balestro–Martini–Teixeira. For a smooth planar gauge with unit disk \(K\), choose the standard determinant as symplectic form. If \(b^\pm(x)\) are the two unit vectors in the tangent direction at \(x\), ordered by determinant sign, let
\[
b(x)=b^+(x)-b^-(x),
\]
and let \(p(x)\) be the intersection of \(\partial K\) with the ray from the origin in direction \(-x\). Then
\[
f_{\mathrm{out}}(x)
=
\frac{\det(b(x),b(p(x)))}{\operatorname{area}(K)},
\qquad
c_{\mathrm{out}}(\gamma)
=
\max_{x\in\partial K}|f_{\mathrm{out}}(x)|.
\]

## Proof

Write
\[
x(t)=(a+\cos t,\sin t),
\qquad
u=\cos t,
\qquad
v=(-\sin t,\cos t).
\]
The vector \(v\) is the positively oriented tangent direction at \(x(t)\), since
\[
\det(x(t),v)=1+au>0.
\]

The line through the gauge origin in direction \(v\) meets the translated unit circle at parameters
\[
\lambda_\pm
=
-a\sin t
\pm
\sqrt{1-a^2u^2}.
\]
Therefore
\[
b(x(t))
=
2\sqrt{1-a^2u^2}\,v.
\]

The opposite-ray point is
\[
p(x)=-\lambda x,
\qquad
\lambda=\frac{1-a^2}{1+a^2+2au}.
\]
If \(u'\) denotes the first coordinate of the outward unit normal to \(K_a\) at \(p(x)\), direct substitution gives
\[
u'
=
-\frac{(1+a^2)u+2a}{1+a^2+2au}.
\]
The tangent-direction construction at \(p(x)\) therefore yields
\[
|b(p(x))|
=
2\sqrt{1-a^2(u')^2}.
\]
Because the two tangent directions are rotations of the two circle normals,
\[
|\det(v,v')|
=
a(1+\lambda)|\sin t|.
\]
Since \(\operatorname{area}(K_a)=\pi\), these identities determine \(|f_{\mathrm{out}}|\) exactly.

Now make the Möbius substitution
\[
z=\frac{u+a}{1+au}.
\]
It maps \([-1,1]\) increasingly onto itself, and the opposite-ray involution becomes simply \(z\mapsto-z\). Elementary simplification gives
\[
|f_{\mathrm{out}}(x(t))|^2
=
\frac{64a^2(1-a^2)^3}{\pi^2}
\frac{
(1-z^2)\bigl((1+a^2)^2-4a^2z^2\bigr)
}{
(1-a^2z^2)^4
}.
\]
Thus it remains to maximize, for \(y=z^2\in[0,1]\),
\[
\Phi_a(y)
=
\frac{
(1-y)\bigl((1+a^2)^2-4a^2y\bigr)
}{
(1-a^2y)^4
}.
\]

Differentiation gives
\[
\Phi_a'(y)
=
\frac{N_a(y)}{(1-a^2y)^5},
\]
where
\[
N_a(y)
=
8a^4y^2
+
(-3a^6-18a^4+5a^2)y
+
4a^6+7a^4-2a^2-1.
\]
Also,
\[
N_a(1)=-(1-a^2)^3<0.
\]

Let
\[
P(s)=4s^3+7s^2-2s-1.
\]
On \([0,1]\), \(P\) first decreases and then strictly increases, while \(P(0)<0<P(1)\); hence it has a unique zero. Its square root is \(a_0\).

If \(0\le a\le a_0\), then \(N_a(0)\le0\). Since \(N_a\) is a convex quadratic in \(y\) and both endpoint values are nonpositive, \(N_a(y)\le0\) throughout \([0,1]\). Therefore \(\Phi_a\) is decreasing and its maximum is at \(y=0\).

If \(a>a_0\), then \(N_a(0)>0>N_a(1)\). The upward-opening quadratic \(N_a\) has exactly one zero in \((0,1)\); the other zero exceeds \(1\). The zero in \((0,1)\) is precisely
\[
y_*(a)
=
\frac{
3a^4+18a^2-5-(1-a^2)\sqrt{9a^4-2a^2+57}
}{16a^2}.
\]
Thus \(\Phi_a\) increases up to \(y_*(a)\) and decreases afterward. Substitution gives the two displayed branches for \(c_{\mathrm{out}}(\gamma_a)\).

It remains to maximize over \(a\). On the first branch, apart from the positive constant \(8/\pi\), the relevant factor is
\[
g(a)=a(1+a^2)(1-a^2)^{3/2}.
\]
Its derivative factors as
\[
g'(a)
=
-\sqrt{1-a^2}\,(2a^2+1)(3a^2-1),
\]
so the first branch has its unique maximum at \(a=1/\sqrt3\). Moreover \(1/\sqrt3<a_0\), because
\[
P(1/3)=-\frac{20}{27}<0.
\]

For the second branch, set
\[
H(a,y)
=
a^2(1-a^2)^3\Phi_a(y).
\]
At the interior maximizer \(y=y_*(a)\), the envelope derivative is \(\partial_a H\). After using the relation \(N_a(y_*)=0\), its numerator reduces to
\[
\frac{a^2(1-a^2)}2
\left[
a^4y_*+4a^4-17a^2y_*+7a^2+5
\right].
\]
The bracket is positive for \(0\le y_*\le1\), since it is decreasing in \(y_*\) and its value at \(1\) is
\[
5(1-a^2)^2>0.
\]
The remaining denominator has negative sign for \(a\in(a_0,1)\) and \(0<y_*<1\), so the second branch is strictly decreasing. Hence the family maximum occurs uniquely at \(a=1/\sqrt3\). Substituting that value gives
\[
c_{\mathrm{out}}(\gamma_{1/\sqrt3})
=
\frac{64\sqrt2}{27\pi}.
\]

## Verification

The proof is algebraic and establishes the statement for the full continuum \(0\le a<1\). The accompanying `verify.py` is an independent numerical replay, not a substitute for the proof.

For nine displacement parameters on both sides of the threshold, the checker constructs \(b(x)\) and \(b(p(x))\) directly from circle-line intersections and performs a dense scan over the boundary parameter. It compares those maxima with the closed formula. It also checks the threshold, the high-branch witness obtained from \(z^2=y_*(a)\), and the exact family maximum at \(a=1/\sqrt3\).

The replay prints:

`VERIFY_OK translated-disk outer asymmetry phase diagram`

## Relationship to prior work

Balestro, Martini, and Teixeira introduced \(c_{\mathrm{out}}\), proved that it is invariant under gauge isometries, established continuity, and showed the universal sharp bound
\[
c_{\mathrm{out}}(\gamma)<2.
\]
Their defining paper does not compute \(c_{\mathrm{out}}\) for translated Euclidean disks; full-text searches found no occurrence of “translated,” “ellipse,” or “Euclidean disk” as a worked family.

Their companion work on dual gauges and symplectic forms supplies the underlying gauge and orthogonality framework but predates the outer-asymmetry construction and does not contain this translated-disk phase diagram.

Classical and later asymmetry measures for convex bodies, including Minkowski- and John-type asymmetries, are different functionals. They do not imply the value of \(c_{\mathrm{out}}\), whose definition is built from the mismatch of tangent directions at opposite rays through the chosen gauge origin.

Targeted searches for translated disks, shifted circles, Randers-type gauges, outer asymmetry, and the notation \(c_{\mathrm{out}}\) did not locate an equivalent formula, the threshold polynomial, or the sharp translated-disk family maximum.

## Limitations

The result concerns the original outer asymmetry constant, not the normalized outer asymmetry constant introduced later in the same paper. It treats Euclidean disks translated relative to the gauge origin; it does not classify translated ellipses, general centrally symmetric bodies with off-center origins, or higher-dimensional gauges.

The originality search was targeted rather than exhaustive. A weakly indexed follow-up computation could exist under different terminology, especially in Finsler or asymmetric-norm literature. No such source was located in the searches used for this result.

## References

V. Balestro, H. Martini, and R. Teixeira, “Asymmetry Measures for Convex Distance Functions,” Journal of Convex Analysis 27 (2020), no. 1, 117–138; arXiv:1901.08462, first submitted 2019-01-24.

V. Balestro, H. Martini, and R. Teixeira, “Duality of gauges and symplectic forms in vector spaces,” Collectanea Mathematica 72 (2021), 13–30; arXiv:1901.03421, first submitted 2019-01-10.

R. Brandenberg and S. König, “Sharpening geometric inequalities using computable symmetry measures,” Mathematika 61 (2015), 559–580.
