# Exact Estermann measure of regular Reuleaux polygons
## Finding
Let \(R_n\subset\mathbb R^2\) be a regular Reuleaux polygon of odd order \(n\ge3\) and constant width \(w>0\). Let \(o\) be its dihedral center and let \(v_0,\ldots,v_{n-1}\) be the vertices of the underlying regular \(n\)-gon.

For a planar convex body \(K\), define its Estermann outer symmetry measure by
\[
E(K)=\frac{\operatorname{area}(K)}
{\inf\{\operatorname{area}(S):K\subset S,\ S\text{ is centrally symmetric}\}}.
\]
Then a minimum-area centrally symmetric superset of \(R_n\) is
\[
H_n=\operatorname{conv}\bigl(\{v_0,\ldots,v_{n-1},-v_0,\ldots,-v_{n-1}\}\bigr).
\]
This \(H_n\) is a regular \(2n\)-gon with inradius \(w/2\). Therefore
\[
E(R_n)=\frac{\pi}{n\tan(\pi/(2n))}-1.
\]
Equivalently, if \(x=\pi/(2n)\),
\[
E(R_n)=2x\cot x-1.
\]

The values are strictly increasing along odd \(n\), beginning with
\[
E(R_3)=\frac{\pi}{\sqrt3}-1,
\]
and they satisfy
\[
E(R_n)
=
1-\frac{\pi^2}{6n^2}
-\frac{\pi^4}{360n^4}
+O(n^{-6}).
\]

## Assumptions and scope
A regular Reuleaux \(n\)-gon has odd \(n\), constant width \(w\), \(n\)-fold rotational symmetry, and \(n\) reflection axes. It may be constructed from a regular \(n\)-gon by replacing each side by the appropriate circular arc of radius \(w\).

The Estermann measure used here is the area of the body divided by the least area of a centrally symmetric convex body containing it. The result identifies one actual minimum-area container. No claim is made that regular Reuleaux polygons are extremal for this measure among all Reuleaux polygons of the same order.

The formula is scale invariant. The proof below keeps \(w\) explicit.

## Proof
First we show that the center of a minimum-area centrally symmetric container may be taken to be \(o\).

Let \(K\) be a convex body invariant under reflection in a line \(L\), and let \(S\supset K\) be centrally symmetric with center \(c\). Steiner symmetrization of \(S\) about \(L\) preserves area and contains \(K\): on every line perpendicular to \(L\), the chord of \(K\) is already centered on \(L\), and its length is at most the length of the corresponding chord of \(S\). Moreover, the Steiner symmetral of \(S\) is centrally symmetric about the orthogonal projection of \(c\) onto \(L\). Indeed, central symmetry of \(S\) makes the chord-length function symmetric about that projected coordinate.

Choose two distinct reflection axes \(L_1,L_2\) of \(R_n\), meeting at \(o\). Starting with any centrally symmetric container, alternately Steiner-symmetrize about \(L_1\) and \(L_2\). Areas remain unchanged, all bodies still contain \(R_n\), and their centers follow alternating orthogonal projections onto \(L_1,L_2\), hence converge to \(o\). A fixed-area family of convex containers of the fixed body \(R_n\) is bounded after the centers enter a bounded neighborhood of \(o\); by compactness for planar convex bodies, a convergent subsequence has a centrally symmetric limit containing \(R_n\), with the same area and center \(o\). Thus the infimum over all centrally symmetric containers equals the infimum over containers centered at \(o\).

For a fixed center \(o\), the smallest centrally symmetric convex set containing \(R_n\) is
\[
\operatorname{conv}(R_n\cup(2o-R_n)).
\]
Translate so that \(o=0\).

Put
\[
\beta=\frac{\pi}{2n}.
\]
Because the diameter of the underlying regular \(n\)-gon is \(w\), its circumradius is
\[
R=\frac{w}{2\cos\beta}.
\]

Let \(L_j\) be a reflection axis through \(v_j\), and let \(u_j\) be a unit vector perpendicular to \(L_j\). Reflection in \(L_j\) sends \(u_j\) to \(-u_j\), so the support function of \(R_n\) satisfies
\[
h_{R_n}(u_j)=h_{R_n}(-u_j).
\]
Since \(R_n\) has constant width \(w\),
\[
h_{R_n}(u_j)+h_{R_n}(-u_j)=w.
\]
Hence
\[
h_{R_n}(u_j)=h_{R_n}(-u_j)=\frac w2.
\]
Therefore \(R_n\) lies in each strip
\[
|\langle x,u_j\rangle|\le\frac w2.
\]
The intersection of these \(n\) strips is the regular \(2n\)-gon \(P_n\) with inradius \(w/2\). Its vertices are precisely
\[
v_0,\ldots,v_{n-1},-v_0,\ldots,-v_{n-1}.
\]
Thus
\[
R_n\cup(-R_n)\subset P_n.
\]
Conversely all \(v_j\) belong to \(R_n\), and all \(-v_j\) belong to \(-R_n\), so
\[
P_n=\operatorname{conv}(\{\pm v_j\})\subset
\operatorname{conv}(R_n\cup(-R_n)).
\]
The reverse inclusion was just proved, and therefore
\[
H_n=\operatorname{conv}(R_n\cup(-R_n))=P_n.
\]

A regular \(2n\)-gon of inradius \(w/2\) has area
\[
\operatorname{area}(H_n)
=
2n\left(\frac{w^2}{4}\right)\tan\beta
=
\frac{nw^2}{2}\tan\beta.
\]
Firey's exact area formula for a regular Reuleaux \(n\)-gon of width \(w\) simplifies to
\[
\operatorname{area}(R_n)
=
w^2\left(
\frac{\pi}{2}
-\frac n2\tan\beta
\right).
\]
Taking the ratio gives
\[
E(R_n)
=
\frac{\pi/2-(n/2)\tan\beta}{(n/2)\tan\beta}
=
\frac{\pi}{n\tan\beta}-1.
\]

With \(x=\beta\), this is \(2x\cot x-1\). Since
\[
\frac{d}{dx}(x\cot x)
=
\frac{\sin x\cos x-x}{\sin^2x}<0
\qquad(0<x<\pi/2),
\]
and \(x=\pi/(2n)\) decreases as \(n\) increases, the measure strictly increases with \(n\).

Finally,
\[
x\cot x
=
1-\frac{x^2}{3}-\frac{x^4}{45}+O(x^6),
\]
so
\[
E(R_n)
=
1-\frac{\pi^2}{6n^2}
-\frac{\pi^4}{360n^4}
+O(n^{-6}).
\]

## Verification
The supplied `verify.py` uses only the Python standard library. For every odd \(n\) from \(3\) through \(101\), it reconstructs the \(2n\) vertices \(\{\pm v_j\}\), checks the strip inequalities attached to the \(n\) reflection axes, verifies that the resulting polygon has inradius \(w/2\), checks its shoelace area against
\[
\frac{nw^2}{2}\tan\!\left(\frac{\pi}{2n}\right),
\]
and compares Firey's area formula with the simplified expression used in the proof. It also checks the Estermann ratio and monotonicity numerically to high precision.

These finite computations check indexing and algebra only. The universal containment and minimization statements are proved symbolically above.

## Relationship to prior work
Firey studied regular Reuleaux polygons of unit breadth and gave their exact area as part of his isoperimetric analysis. His formula is equivalent to
\[
\frac{\pi}{2}-\frac n2\tan\!\left(\frac{\pi}{2n}\right)
\]
in width-one normalization.

Jin and Guo studied asymmetry of constant-width domains and regular Reuleaux polygons for the Minkowski measure. Their later regular-Reuleaux paper states the exact Minkowski asymmetry
\[
\frac{1}{2\cos(\pi/(2n))-1}
\]
and proves regular Reuleaux polygons extremal within their order for that different measure. The inspected full text does not state an Estermann formula, and an exact-text search there found no occurrence of “Estermann.”

Classical sources on the Estermann measure identify the Reuleaux triangle as extremal among constant-width bodies. The present result instead gives the entire regular odd-\(n\) family and identifies its minimum-area centrally symmetric supersets explicitly.

Targeted searches for “Estermann measure regular Reuleaux polygon,” “smallest centrally symmetric superset regular Reuleaux polygon,” the exact trigonometric form, and the heptagon/pentagon special cases did not locate a prior formula.

## Limitations
This result does not prove that a regular Reuleaux \(n\)-gon is extremal among all Reuleaux \(n\)-gons for the Estermann measure. It computes the invariant only for the regular family.

The centering argument proves existence of a minimum-area container centered at the dihedral center; it does not claim uniqueness of the minimizing center.

Historical literature on symmetry measures is broad. A residual originality risk remains that the same short computation may occur in an unindexed note, book exercise, or discussion of Reuleaux polygons under another name.

## References
1. H. L. Jin and Q. Guo, *On the asymmetry for convex domains of constant width*, Communications in Mathematics Research 26, 176--182. Public bibliographic date: 2011-07-19. MSC includes \(52A38\) and \(52A10\).
2. Q. Guo and H. L. Jin, *On a measure of asymmetry for Reuleaux polygons*, Journal of Geometry 102 (2011), 73--79. DOI: 10.1007/s00022-011-0096-9. Relevant material: definition of regular Reuleaux polygons, the exact Minkowski-asymmetry formula, and the comparison program among Reuleaux polygons.
3. W. J. Firey, *Isoperimetric ratios of Reuleaux polygons*, Pacific Journal of Mathematics 10 (1960), 823--829. Relevant material: the width-one regular-Reuleaux area formula on page 824.
4. B. Grünbaum, *Measures of symmetry for convex sets*, Proceedings of Symposia in Pure Mathematics 7 (1963), 233--270.
