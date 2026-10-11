# Exact diameter of the geodesic Zare monotiles

## Finding

Liao and Wang construct, for every integer \(q\ge2\), a compact simple geodesic monotile
\[
T_q\subset\mathbb H^2
\]
with \(2q+3\) sides. In the upper half-plane model put
\[
r=\frac{q+1}{q},
\qquad
\delta=\frac1{q^2},
\qquad
L=(q+1)\delta.
\]
Its lower vertices are
\[
V_k=(k\delta,1),
\qquad
0\le k\le q+1,
\]
and its upper vertices are
\[
W_j=(rj\delta,r),
\qquad
0\le j\le q.
\]

The exact diameter is
\[
\boxed{
\operatorname{diam}(T_q)
=
\begin{cases}
\operatorname{arcosh}(41/32),&q=2,\\[2mm]
\operatorname{arcosh}\!\left(
1+\dfrac{2q^2+2q+1}{2q^3(q+1)}
\right),&q\ge3.
\end{cases}
}
\]

For \(q=2\), the farthest pair is the pair of lower endpoints
\[
V_0,\ V_{q+1},
\]
up to reversing the pair.

For every \(q\ge3\), the farthest pairs are exactly
\[
V_0,\ W_q
\qquad\text{and}\qquad
V_{q+1},\ W_0,
\]
again up to reversing the pair.

Consequently,
\[
\boxed{
q\,\operatorname{diam}(T_q)\longrightarrow\sqrt2.
}
\]
Using the source's exact area formula
\[
\operatorname{Area}(T_q)
=
2\arctan\frac1{2q^2},
\]
one also obtains the intrinsic area-diameter asymptotic
\[
\boxed{
\frac{\operatorname{diam}(T_q)}
{\sqrt{\operatorname{Area}(T_q)}}
\longrightarrow\sqrt2.
}
\]

Thus the source's estimate
\[
\operatorname{diam}(T_q)<\frac3q
\]
for this construction can be replaced by a closed exact formula, and its asymptotically sharp constant is \(\sqrt2\).

## Assumptions and scope

The tile \(T_q\) is exactly the geodesic realization in Section 7.2 of Liao--Wang, with curvature normalized to \(-1\).

The statement concerns the diameter of this explicit counterexample family. It does not assert that \(\sqrt2\) is optimal among all hyperbolic monotiles with \(2q+3\) sides, nor does it improve the source's general lower bounds for fixed side count or vertex-proper tiles.

The source proves that these \(T_q\) tile the full hyperbolic plane, are nonconvex, and satisfy the stated exact area formula. Those facts are used as premises. The new part is the exact ambient diameter and its extremizing vertex pairs.

## Proof

We first record a diameter lemma that also applies to nonconvex simple geodesic polygons.

Every compact simple geodesic polygon in \(\mathbb H^2\) admits a triangulation by geodesic diagonals using only its original vertices. One way to see this is to pass to the Klein model, where hyperbolic geodesics are Euclidean line segments, triangulate the resulting simple Euclidean polygon, and return to \(\mathbb H^2\).

Fix a point \(y\) in the polygon. On each geodesic triangle of such a triangulation, the function
\[
x\longmapsto d_{\mathbb H^2}(x,y)
\]
is convex along geodesics, so its maximum on the triangle occurs at a vertex. Hence its maximum on the whole polygon occurs at an original polygon vertex. Applying the same argument to the second variable shows that the diameter of any compact simple geodesic polygon is attained by a pair of its vertices.

For points \(z=x+\mathrm i y\) and \(z'=x'+\mathrm i y'\) in the upper half-plane,
\[
\cosh d(z,z')
=
1+
\frac{(x-x')^2+(y-y')^2}{2yy'}.
\]

There are only three vertex-pair types to optimize.

For two lower vertices, the height is \(1\), so the largest separation occurs at the two lower endpoints:
\[
C_{\mathrm{low}}
:=
\max_{k,\ell}\cosh d(V_k,V_\ell)
=
1+\frac{L^2}{2}
=
1+\frac{(q+1)^2}{2q^4}.
\]

For two upper vertices, the height is \(r\), and the horizontal span is again \(L\). Thus
\[
C_{\mathrm{up}}
=
1+\frac{L^2}{2r^2}
=
1+\frac1{2q^2}
<
C_{\mathrm{low}}.
\]

For a lower and an upper vertex, the vertical difference is
\[
r-1=\frac1q.
\]
The hyperbolic cosine is increasing in the absolute horizontal separation, so the maximum occurs at opposite endpoints. Therefore
\[
C_{\mathrm{cross}}
=
1+
\frac{L^2+(r-1)^2}{2r}
=
1+
\frac{2q^2+2q+1}{2q^3(q+1)}.
\]

It remains only to compare the lower-endpoint and cross-endpoint values:
\[
C_{\mathrm{cross}}-C_{\mathrm{low}}
=
\frac{q^3-q^2-2q-1}{2q^4(q+1)}.
\]
At \(q=2\), the numerator is \(-1\), so the lower endpoints are uniquely farthest. At \(q=3\), the numerator is \(11\), and
\[
p(q)=q^3-q^2-2q-1
\]
is strictly increasing for all \(q\ge2\), because
\[
p(q+1)-p(q)=3q^2+q-2>0.
\]
Hence the cross-endpoint pairs are uniquely farthest for every \(q\ge3\). Substitution gives the exact diameter formula.

For \(q\ge3\), write
\[
x_q
=
\frac{2q^2+2q+1}{2q^3(q+1)}
=
\frac1{q^2}
+
\frac1{2q^3(q+1)}.
\]
Then
\[
q^2x_q\longrightarrow1.
\]
Since
\[
\operatorname{arcosh}(1+x)\sim\sqrt{2x}
\qquad(x\downarrow0),
\]
we obtain
\[
q\,\operatorname{diam}(T_q)\longrightarrow\sqrt2.
\]

Finally,
\[
2\arctan\frac1{2q^2}
\sim\frac1{q^2},
\]
so
\[
\frac{\operatorname{diam}(T_q)}
{\sqrt{\operatorname{Area}(T_q)}}
\longrightarrow\sqrt2.
\]

## Verification

The bundled checker reconstructs all lower and upper vertices for every
\[
2\le q\le100,
\]
evaluates every vertex-pair hyperbolic cosine exactly with rational arithmetic, and confirms the two-branch closed formula and the complete farthest-pair classification.

It also checks algebraically that
\[
C_{\mathrm{cross}}-C_{\mathrm{low}}
=
\frac{q^3-q^2-2q-1}{2q^4(q+1)}
\]
and numerically confirms convergence of
\[
q\,\operatorname{diam}(T_q)
\]
and
\[
\operatorname{diam}(T_q)/
\sqrt{\operatorname{Area}(T_q)}
\]
to \(\sqrt2\).

The finite sweep is supplementary. The all-\(q\) proof is the triangulation reduction, the three exact pair-type formulas, and the sign analysis above.

## Relationship to prior work

Liao--Wang construct \(T_q\), prove that it tiles \(\mathbb H^2\), compute its exact area
\[
2\arctan\frac1{2q^2},
\]
and prove the sufficient diameter estimate
\[
\operatorname{diam}(T_q)<\frac3q
\]
by containing the tile in a rectangle and joining arbitrary points by a vertical-plus-horizontal path. They do not identify the diameter pair or give an exact diameter formula in version 1.

The exact result here uses the same explicit vertices but replaces the path estimate with a global diameter reduction to vertex pairs. It reveals a genuine branch change: the lower endpoints control the illustrated \(q=2\) heptagon, whereas opposite lower--upper endpoints control every \(q\ge3\).

Targeted searches using the source identifier, the \(T_q\) notation, the \(2q+3\)-gon description, exact-diameter language, and the asymptotic constant \(\sqrt2\) found no prior statement of this formula. The closest indexed hyperbolic-geometry findings concern different objects such as regular hyperbolic Reuleaux polygons, regular hyperbolic simplex thickness, and Basmajian seam mass.

## Limitations

The theorem is an exact analysis of one canonical small-diameter construction, not a universal extremal theorem.

The first public version of the source is the full text inspected here. An October 6 revision was indexed during the comparison search but its revised full text was not retrievable through the available full-text interface; the indexed abstract still advertises only the bound
\[
\operatorname{diam}(T_q)<3/q.
\]
A same-day revision or another unindexed source could therefore remain a bibliographic risk.

No claim is made about the smallest possible diameter at a fixed number of sides, or about whether another non-vertex-proper construction has a smaller asymptotic constant.

## References

1. Yixi Liao and Erxiao Wang, *Area and diameter gaps for hyperbolic monotiles*, arXiv:2610.05438v1, 4 October 2026.
2. A. Zare, *Tilings by a single tile*, cited by Liao--Wang as motivation for the small-diameter construction.
