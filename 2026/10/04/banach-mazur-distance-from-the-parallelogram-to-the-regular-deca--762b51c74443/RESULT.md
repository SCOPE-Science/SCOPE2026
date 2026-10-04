# Banach–Mazur distance from the parallelogram to the regular decagon

## Finding

Let \(P_4\) denote any parallelogram and let \(P_{10}\) be any affine-regular decagon. Then
\[
\delta_{BM}(P_4,P_{10})
=
\cos\!\left(\frac{\pi}{5}\right)
+
\frac12\sec\!\left(\frac{\pi}{5}\right)
=
\frac{3\sqrt5-1}{4}.
\]

This is the first case \(j=1\) of the equality conjectured by Lassak for the family \(P_{8j+2}\). The published paper proves the displayed quantity as an upper bound for every member of that family and explicitly conjectures equality; the argument below supplies the missing lower bound for the decagon.

## Assumptions and scope

The Banach–Mazur distance is taken in the affine category of centrally symmetric planar convex bodies. Because the quantity is affine invariant, it is enough to use the Euclidean regular decagon
\[
P_{10}=\operatorname{conv}\{v_i:0\le i\le9\},
\qquad
v_i=\left(\cos\frac{i\pi}{5},\sin\frac{i\pi}{5}\right).
\]

A structural proposition in Lassak's paper says that if a parallelogram gives a homothetic sandwich for a centrally symmetric planar convex body, then one may replace it by an inscribed parallelogram without increasing the homothety factor. Hence the lower-bound problem reduces to inscribed centrally symmetric parallelograms
\[
P=\operatorname{conv}\{\pm a,\pm b\}\subset P_{10}.
\]

For such \(P\), write \(\|x\|_{a,b,1}=|\alpha|+|\beta|\) when \(x=\alpha a+\beta b\). The least dilation factor containing the decagon is
\[
\lambda(a,b)=\max_{0\le i\le9}\|v_i\|_{a,b,1}.
\]

## Proof

Put
\[
\varphi=\frac{1+\sqrt5}{2},
\qquad
q=\varphi-1=\frac{\sqrt5-1}{2}.
\]
Use \(e_0=v_0\) and \(e_1=v_1\) as a basis. The regular-decagon recurrence
\[
v_{i+1}=\varphi v_i-v_{i-1}
\]
gives
\[
v_0=(1,0),\quad
v_1=(0,1),\quad
v_2=(-1,\varphi),\quad
v_3=(-\varphi,\varphi),\quad
v_4=(-\varphi,1),\quad
v_5=(-1,0).
\]

By dihedral symmetry, central symmetry, and exchange of \(a,b\), the side-pair containing \(a,b\) has separation zero, one, or two modulo the five opposite side-pairs. Thus three cases suffice; endpoints shared by adjacent sides may be assigned to either case.

For two points on the same side, write
\[
a=(1-u)e_0+ue_1,
\qquad
b=(1-v)e_0+ve_1,
\qquad
0\le u<v\le1.
\]
The coordinates of \(v_3\) in the basis \((a,b)\) have absolute values \(\varphi/(v-u)\) and \(\varphi/(v-u)\). Therefore
\[
\lambda(a,b)\ge\frac{2\varphi}{v-u}\ge2\varphi,
\]
which is stronger than the claimed bound.

For adjacent sides, write
\[
a=(1-u)e_0+ue_1,
\qquad
b=(1-v)e_1+vv_2,
\qquad
0\le u,v\le1.
\]
Let
\[
\Delta=(1-u)(1+qv)+uv.
\]
A direct coordinate calculation for \(v_3\) gives
\[
\|v_3\|_{a,b,1}
=
\frac{\varphi(2-q^2v)}{\Delta}.
\]
Since
\[
(2-q^2v)-\Delta
=1-v+u(1-q^2v)\ge0,
\]
we obtain
\[
\lambda(a,b)\ge\varphi,
\]
again stronger than needed.

It remains to consider sides separated by one intervening side. Write
\[
a=(1-u)e_0+ue_1,
\qquad
b=(1-v)v_2+vv_3,
\qquad
0\le u,v\le1.
\]
Set
\[
E=\varphi-qu(1-v)>0,
\]
and define
\[
A=2-u+qv,
\qquad
B=\varphi+v-qu,
\qquad
C=2+q(u+1-v).
\]
Direct inversion of the \((a,b)\)-matrix yields
\[
\|v_1\|_{a,b,1}=\frac{A}{E},
\qquad
\|v_2\|_{a,b,1}=\frac{B}{E},
\qquad
\|v_4\|_{a,b,1}=\frac{C}{E}.
\]
Hence
\[
\lambda(a,b)\ge\frac{\max\{A,B,C\}}{E}.
\]
Put
\[
\mu=\frac{3\sqrt5-1}{4}
=\frac{\varphi}{2}+q,
\qquad
u_* = \frac{1}{4+q}.
\]
We prove \(\max\{A,B,C\}\ge\mu E\).

First note that
\[
A-B=q^2(1-u-v).
\]
For fixed \(u\), both \(A/E\) and \(B/E\) are increasing in \(v\), while \(C/E\) is decreasing. Indeed their derivative numerators, after multiplying by the positive denominator \(E^2\), are respectively
\[
q(1-u)(\varphi-u),
\qquad
\varphi(1-u)+q^2u^2,
\qquad
-q(E+uC).
\]

Assume first that \(u+v\le1\), so \(A\ge B\). The crossing \(A=C\) occurs at
\[
v_A=\frac12+\frac{\varphi^2}{2}u.
\]
It lies in \([0,1-u]\) exactly when \(u\le u_*\). If \(u\le u_*\), monotonicity reduces the minimum of \(\max\{A/E,C/E\}\) to \(v=v_A\), and
\[
A-\mu E
=
\frac{u}{4}\bigl(1-(4+q)u\bigr)
\ge0.
\]
If \(u\ge u_*\), the crossing lies to the right of the allowed interval, so the minimum is at \(v=1-u\), where
\[
C-\mu E
=
\frac{3-2q}{2}(u-u_*)(u+\varphi)
\ge0.
\]

Now assume \(u+v\ge1\), so \(B\ge A\). The crossing \(B=C\) occurs at
\[
v_B=q+2q^2u.
\]
If \(u\le u_*\), this crossing lies below the interval \([1-u,1]\), and the minimum is at \(v=1-u\); there
\[
B-\mu E
=
\frac{3-2q}{2}(u_*-u)(\varphi-u)
\ge0.
\]
If \(u_*\le u\le\tfrac12\), the crossing lies inside the interval, and at \(v=v_B\)
\[
B-\mu E
=
\frac{(1-2u)(5-7q)}{2}(u-u_*)
\ge0.
\]
Finally, if \(u\ge\tfrac12\), the crossing lies above the interval and the minimum is at \(v=1\); there
\[
C-\mu E
=
\frac q2(2u-1)
\ge0.
\]
Thus every inscribed parallelogram requires dilation at least \(\mu\).

For the matching upper bound, take one vertex of the parallelogram at \(v_0=(1,0)\) and the other at the midpoint of the side \([v_2,v_3]\), namely
\[
b=\left(0,\sin\frac{2\pi}{5}\right).
\]
The corresponding gauge of \(v_1\) is
\[
\cos\frac{\pi}{5}
+
\frac{\sin(\pi/5)}{\sin(2\pi/5)}
=
\cos\frac{\pi}{5}
+
\frac{1}{2\cos(\pi/5)}
=
\mu.
\]
The remaining vertices are no farther in this gauge by the decagon symmetries and the same direct coordinate calculation. This is exactly Lassak's published coordinate-axis upper-bound construction. Hence
\[
\delta_{BM}(P_4,P_{10})=\mu=\frac{3\sqrt5-1}{4}.
\]

## Verification

The proof uses only exact algebra in the quadratic field \(\mathbb Q(\sqrt5)\), elementary monotonicity, and Lassak's inscribed-parallelogram reduction. The accompanying `verify.py` checks symbolically the golden-ratio identities, the two crossing locations, the five residual factorizations used in the case split, the derivative numerators, and the final closed form. It was replayed from the packaged path and prints `VERIFY_OK exact symbolic identities`.

The symbolic checker is supplementary: it verifies the displayed identities but does not replace the geometric reduction or the quantified case analysis.

## Relationship to prior work

Lassak's 2020 preprint, later published in *Results in Mathematics*, proves exact distances from the parallelogram to affine-regular \(8j\)-gons and \((8j+4)\)-gons. For affine-regular \((8j+2)\)-gons it proves only
\[
\delta_{BM}(P_4,P_{8j+2})
\le
\frac12\sec\!\left(\frac{2j\pi}{8j+2}\right)
+
\cos\!\left(\frac{2j\pi}{8j+2}\right),
\]
and explicitly conjectures that this upper estimate is the true distance. Substituting \(j=1\) gives precisely the constant proved here for \(P_{10}\).

Targeted searches for the decagon, the exact constant, the \(8j+2\) conjecture, affine-regular decagons, and parallelogram Banach–Mazur distance did not locate a later proof of the \(P_{10}\) case. General planar Banach–Mazur papers and later work on small-dimensional cube/crosspolytope distances do not imply this particular two-dimensional decagon value.

## Limitations

The proof settles only the decagon, equivalently \(j=1\) in Lassak's \(P_{8j+2}\) conjecture. It does not settle the remaining \(P_{8j+2}\) family, the \(P_{8j+6}\) family, or classify every optimal inscribed parallelogram. The literature search was targeted rather than logically exhaustive, so a weakly indexed later solution of this special case remains a residual originality risk.

## References

M. Lassak, “Banach-Mazur distances between parallelograms and other affinely regular even-gons,” arXiv:2008.01653, first submitted 2020-08-04; published as “Banach–Mazur Distance from the Parallelogram to the Affine-Regular Hexagon and Other Affine-Regular Even-Gons,” *Results in Mathematics* 76, 62 (2021), DOI 10.1007/s00025-021-01368-8.

T. Kobos, “Extremal Banach–Mazur distance between a symmetric convex body and an arbitrary convex body on the plane,” arXiv:1711.01787; *Mathematika* 66 (2020), 325–341.
