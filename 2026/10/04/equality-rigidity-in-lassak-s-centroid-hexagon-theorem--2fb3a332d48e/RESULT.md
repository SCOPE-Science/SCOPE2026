# Equality rigidity in Lassak’s centroid–hexagon theorem

## Finding

Let \(A\subset\mathbb R^2\) be a planar convex body and let
\[
H=\operatorname{conv}(a_1,\ldots,a_6)
\]
be an affine-regular hexagon inscribed in \(A\), with center \(o\). Lassak proved
\[
g(A)\in o+\frac{4}{21}(H-o),
\]
where \(g(A)\) is the centroid.

The sharpness cases are rigid. The centroid lies on the boundary of the homothetic hexagon if and only if, after cyclic relabeling,
\[
A=\operatorname{conv}(H\cup\{\bar a_i\}),
\]
where \(\bar a_i\) is the corresponding outer vertex of the star obtained by extending the side lines of \(H\). Hence there is exactly one equality body up to affine equivalence.

In Lassak’s normalization
\[
a_1=(1,1),\quad a_2=(-1,1),\quad a_3=(-2,0),\quad a_4=(-1,-1),\quad a_5=(1,-1),\quad a_6=(2,0),
\]
the equality body for the top side is
\[
P_*=\operatorname{conv}\{(0,2),(-2,0),(-1,-1),(1,-1),(2,0)\}.
\]
Its area is \(7\) and its centroid is
\[
g(P_*)=(0,4/21).
\]

## Assumptions and scope

An affine-regular hexagon means a nondegenerate affine image of a regular hexagon. “Inscribed” is used in the same sense as in Lassak’s theorem: the six vertices of \(H\) lie on the boundary of \(A\).

For the normalized hexagon, the outer star vertex above the side \(a_1a_2\) is
\[
\bar a_2=(0,2).
\]
The six extremal pentagons for a fixed labeled hexagon are obtained by cyclic symmetry; they are all affinely equivalent.

The claim classifies equality in the sharp constant \(4/21\). It does not classify convex bodies whose centroid lies strictly inside the homothetic hexagon.

## Proof

By affine invariance and cyclic relabeling, suppose the centroid lies on the top supporting side of
\[
\frac4{21}H,
\]
so the desired equality is
\[
\operatorname{cen}_y(A)=\frac4{21}.
\]
Steiner symmetrization with respect to the vertical axis preserves every horizontal slice length and therefore preserves area and the vertical first moment. Let \(A_s\) denote the symmetrized body. It contains the normalized hexagon and has the same vertical centroid.

Lassak’s proof reduces the symmetric problem to a support parameter \(w\in[1,2]\). The symmetric support lines through \(a_1\) and \(a_2\) meet at \(u=(0,w)\). The proof has a low branch \(1\le w\le w_0\) and a high branch \(w_0\le w\le2\), where \(w_0\) is the root in \([1,2]\) of
\[
w^3+w^2-2w-4=0.
\]
Since this polynomial is negative at \(w=8/7\) and strictly increasing for \(w\ge8/7\),
\[
w_0>\frac87.
\]

On the low branch Lassak’s comparison pentagon has
\[
\operatorname{cen}_y(P_w)=
\frac{w^4+w^3-2w^2-4w+8}{3w(w^2+3w+4)}.
\]
Exact subtraction gives
\[
\frac4{21}-\operatorname{cen}_y(P_w)
=-\frac{(w-2)(7w^3+17w^2+8w-28)}{21w(w^2+3w+4)}.
\]
For \(w\ge1\), the cubic factor is positive because its value at \(1\) is \(4\) and its derivative
\[
21w^2+34w+8
\]
is positive. Since \(w<2\) on this branch, the deficit is strictly positive. Equality is therefore impossible on the low branch.

On the high branch Lassak’s Part 4 reduces the bound to the sign of
\[
f(w,z)=28z^2(w^2-3w+2)+20zw(2-w)+w^2(7w^2+3w-34),
\]
with \(w\in[w_0,2]\) and the relevant \(z\) lying in \([5/7,1]\). The exact factorization is
\[
f(w,z)=(w-2)q(w,z),
\]
where
\[
q(w,z)=7w^3+17w^2+28wz^2-20wz-28z^2.
\]
Complete the square:
\[
q(w,z)=28(w-1)\left(z-\frac{5w}{14(w-1)}\right)^2
+\frac{w^2(7w-8)(7w+18)}{7(w-1)}.
\]
Because \(w\ge w_0>8/7\), every term on the right is nonnegative and the second is strictly positive. Hence
\[
q(w,z)>0.
\]
Therefore \(f(w,z)<0\) for every \(w<2\), and equality in Lassak’s high-branch comparison can occur only at
\[
w=2.
\]

At \(w=2\), the support intersection is \(u=(0,2)\), while the two auxiliary side intersections become \(a_6\) and \(a_3\). The wing triangles in Lassak’s decomposition have zero area, and the comparison polygon becomes exactly
\[
P_*=ar a_2a_3a_4a_5a_6.
\]
The equality chain in Parts 2, 6, and 7 therefore forces the symmetric equality body itself to be \(P_*\). The preliminary deletion of the three lower star regions also has to be void: every deleted point has vertical coordinate at most \(0\), so deleting a set of positive area would strictly raise a positive centroid, contradicting the already sharp upper bound \(4/21\).

It remains to undo Steiner symmetrization. Assume \(A_s=P_*\). Write the horizontal slice of the original body as
\[
A\cap\{y=t\}=[c(t)-h(t),c(t)+h(t)]\times\{t\}.
\]
Steiner symmetrization preserves \(h(t)\). For \(P_*\),
\[
h(t)=t+2\quad(-1\le t\le0),
\qquad
h(t)=2-t\quad(0\le t\le2).
\]
For a convex body the left endpoint function \(c-h\) is convex and the right endpoint function \(c+h\) is concave. Since \(h\) is affine on each of the two displayed intervals, \(c\) is both convex and concave there, hence affine on each interval.

The original body contains the six hexagon vertices. Its slice at \(t=-1\) has the same length \(2\) as the corresponding slice of \(P_*\) and contains \((-1,-1)\) and \((1,-1)\), so \(c(-1)=0\). The slice at \(t=0\) has length \(4\) and contains \((-2,0)\) and \((2,0)\), so \(c(0)=0\). The slice at \(t=1\) has length \(2\) and contains \((-1,1)\) and \((1,1)\), so \(c(1)=0\). Affinity now gives
\[
c(t)=0
\]
throughout both intervals. Thus \(A=A_s=P_*\).

Conversely, direct shoelace computation gives \(\operatorname{area}(P_*)=7\) and
\[
g(P_*)=(0,4/21),
\]
so every affine image and cyclic copy of this pentagon attains equality. This proves the classification.

## Verification

The standalone `verify.py` uses exact rational arithmetic only. It checks the polynomial factorization of \(f\), the completed-square identity after clearing denominators, the low-branch deficit factorization, the threshold sign at \(8/7\), and the exact area and centroid of \(P_*\).

Polynomial identities are checked on rational interpolation grids whose sizes exceed the separate degree bounds, so these checks certify the identities rather than merely sampling them numerically. The replay output is

`VERIFY_OK centroid-hexagon equality rigidity`

The checker does not replace the geometric argument. In particular, the convex-slice argument that reverses Steiner symmetrization and the structural comparison decomposition are proved in the text and in the cited primary source.

## Relationship to prior work

Lassak proved the sharp inclusion
\[
g(A)\in o+\frac4{21}(H-o)
\]
for every planar convex body with an inscribed affine-regular hexagon. At the end of the paper he exhibited the normalized pentagon \(P_*\) to prove sharpness and explicitly stated the expectation that there are no other examples besides affine images of that pentagon.

The present finding proves exactly that expected equality classification. It sharpens Lassak’s two numerical sign checks to exact factorizations and adds the slice-center rigidity needed to recover the nonsymmetric original body after Steiner symmetrization.

Targeted searches for the constant \(4/21\), affine-regular hexagons, equality cases, uniqueness, the sharp pentagon, and affine extremizers located the primary paper and topic-adjacent centroid work but no later proof of the stated uniqueness classification.

## Limitations

The originality assessment cannot exclude an unindexed or differently phrased observation. The proof also uses the structural reductions established in Lassak’s published theorem; the new work rechecks the equality-critical algebra exactly and supplies the missing equality analysis, rather than reproving every preliminary containment construction from first principles.

The conclusion is only an equality classification for this two-dimensional centroid bound. It does not address higher-dimensional analogues or stability estimates for near-extremizers.

## References

M. Lassak, “Position of the centroid of a planar convex body,” arXiv:2202.01815, first submitted 2022-02-03; Aequationes Mathematicae 98 (2024), 687–695, DOI 10.1007/s00010-024-01058-0.

M. Lassak, “Estimation of the centroid Banach–Mazur distance between planar convex bodies,” Ukrainian Mathematical Journal 76 (2024), DOI 10.3842/umzh.v76i5.7428.
