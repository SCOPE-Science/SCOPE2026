# Tree-independent Euclidean facet shells of standard Loday operahedra
## Finding
Let
\[
n\ge3,
\]
let
\[
t\in\mathrm{PT}_n
\]
be a reduced planar rooted tree with \(n\) internal vertices, and let
\[
P_t\subset\mathbb R^{n-1}
\]
be the standard-weight Loday realization of the associated operahedron introduced by Laplante-Anfossi.

Put
\[
c=\frac n2\mathbf1.
\tag{1}
\]
If a facet is indexed by a nontrivial nest
\[
N\subset E(t)
\]
with
\[
s=|N|,
\]
then the exact intrinsic Euclidean distance from \(c\) to that facet is
\[
\boxed{
\delta_s
=
\frac12\sqrt{(n-1)s(n-1-s)}.
}
\tag{2}
\]

Thus the full center-to-facet distance profile depends only on the number of internal edges in the nest. It is independent of the shape of the planar tree and of the location of the connected edge set inside that tree.

Consequently,
\[
\boxed{
r_{\mathrm{in}}(P_t)
=
\frac12\sqrt{(n-1)(n-2)}.
}
\tag{3}
\]
The incenter is unique and equals \(c\).

The centered maximal ball is tangent exactly to the facets indexed by nests satisfying
\[
\boxed{
|N|=1
\quad\text{or}\quad
|N|=n-2.
}
\tag{4}
\]
For \(n=3\), these two conditions coincide.

Since every tree contains connected edge sets of every cardinality between \(1\) and \(n-2\), the distinct centered facet-shell radii are exactly
\[
\frac12\sqrt{(n-1)s(n-1-s)},
\qquad
1\le s\le\left\lfloor\frac{n-1}{2}\right\rfloor.
\tag{5}
\]

## Assumptions and scope
The polytope \(P_t\) is the standard-weight realization from *The diagonal of the operahedra*. The weight vector is
\[
(1,\ldots,1).
\]

The ambient affine hull is equipped with the Euclidean metric inherited from \(\mathbb R^{n-1}\). The theorem is metric and realization-specific; it is not invariant under arbitrary affine transformations.

The result concerns all reduced planar rooted trees with \(n\) internal vertices. It therefore ranges across the full operahedral family described in the source, from the associahedral to the permutahedral extremes.

## Proof
The source proves that
\[
|E(t)|=n-1
\]
and that the standard-weight realization is contained in the affine hyperplane
\[
\sum_{e\in E(t)}x_e
=
\binom n2.
\tag{6}
\]

It also proves that every nontrivial nest
\[
N\subset E(t)
\]
defines a facet with inequality
\[
\sum_{e\in N}x_e
\ge
\binom{|V(t(N))|}{2}.
\tag{7}
\]
Because \(N\) is a connected set of \(s\) edges in a tree, its closure is a tree with
\[
s+1
\]
vertices. Hence (7) becomes
\[
\sum_{e\in N}x_e
\ge
\binom{s+1}{2}.
\tag{8}
\]

The affine hyperplane (6) has
\[
d=n-1
\]
coordinates. At the uniform point (1),
\[
\sum_{e\in N}c_e
=
\frac{sn}{2}.
\]
The slack in (8) is therefore
\[
\frac{sn}{2}-\binom{s+1}{2}
=
\frac{s(n-1-s)}2.
\tag{9}
\]

Inside the tangent space
\[
\mathbf1^\perp\subset\mathbb R^{n-1},
\]
the normal \(\mathbf1_N\) projects to
\[
\mathbf1_N-\frac{s}{n-1}\mathbf1.
\]
Its squared norm is
\[
s-\frac{s^2}{n-1}
=
\frac{s(n-1-s)}{n-1}.
\tag{10}
\]
Dividing the slack (9) by the normal norm in (10) gives
\[
\delta_s
=
\frac{
s(n-1-s)/2
}{
\sqrt{s(n-1-s)/(n-1)}
}
=
\frac12\sqrt{(n-1)s(n-1-s)},
\]
which proves (2).

For
\[
1\le s\le n-2,
\]
the product
\[
s(n-1-s)
\]
is minimized exactly at
\[
s=1
\quad\text{or}\quad
s=n-2,
\]
where its value is \(n-2\). This proves that the centered ball of radius (3) lies inside every facet halfspace and gives the contact classification (4).

It remains to show that no larger ball, and no other center with the same radius, is possible.

Every singleton edge set
\[
\{e\}
\]
is a nontrivial nest. Its facet inequality is
\[
x_e\ge1.
\tag{11}
\]
Suppose a radius-\(r\) Euclidean ball centered at \(q\) is contained in \(P_t\). In the affine hull (6), the intrinsic normal length of the singleton hyperplane is
\[
\sqrt{\frac{n-2}{n-1}}.
\]
Thus every singleton facet gives
\[
q_e-1
\ge
r\sqrt{\frac{n-2}{n-1}}.
\tag{12}
\]
Summing (12) over the \(n-1\) internal edges and using (6),
\[
\binom n2-(n-1)
\ge
r\sqrt{(n-1)(n-2)}.
\]
Since
\[
\binom n2-(n-1)=\frac{(n-1)(n-2)}2,
\]
we obtain
\[
r\le
\frac12\sqrt{(n-1)(n-2)}.
\tag{13}
\]
This matches the centered feasible radius, proving (3).

If equality holds in (13), then equality must hold in every singleton inequality (12), so every coordinate \(q_e\) is equal. Equation (6) then forces
\[
q=c.
\]
Hence the incenter is unique.

Finally, every tree with \(n-1\) edges has a connected edge subset of each size
\[
1,2,\ldots,n-2
\]
by starting from any edge and repeatedly adjoining an adjacent unused edge. Therefore all shell radii in (5) occur.

## Verification
The proof is arbitrary-rank and symbolic.

The source-dependent ingredients were checked directly in the primary arXiv full text and its facet page: the tree has \(n-1\) internal edges; nests are connected nonempty edge subsets; Proposition 2.15 gives the affine equation, all nest halfspaces, and their completeness; and Corollary 2.16 identifies the standard realization as a removahedron.

The accompanying `verify.py` checks the exact squared-distance formula and the sharp inradius for
\[
3\le n\le200.
\]
It also enumerates every labeled tree through \(n=6\), every nonempty proper connected edge subset, and verifies that the direct source facet constant, projected-normal distance, and tangent-cardinality classification agree with the theorem. These finite checks are corroborative only.

## Relationship to prior work
Laplante-Anfossi introduces the standard-weight Loday operahedra, proves their complete facet description, and shows that they are removahedra obtained by deleting inequalities from the classical permutahedron. The paper develops cellular diagonals, operadic composition, normal fans, and generalized-permutahedral geometry; it does not state Euclidean inradii or normalized center-to-facet distances.

The same source emphasizes that operahedra range from associahedra to permutahedra. The theorem here shows that, despite the changing combinatorial type, all standard realizations retain a rigid Euclidean shell law: every facet distance from the common uniform center is determined solely by nest cardinality.

A previously known endpoint comparison for particular Loday polytopes does not imply the present theorem for intermediate operahedra, nor does it provide the exact all-facet shell formula (2). Likewise, graph-associahedron metric results for special graph families do not cover these line-graph-of-tree removahedral realizations.

Targeted published-result and literature searches under “operahedron”, “Loday operahedron”, “removahedron”, “inradius”, “Chebyshev center”, and “Euclidean facet distance” did not locate a theorem implying (2)--(5).

## Limitations
The theorem applies only to the standard weight. General positive weights translate the facet heights non-uniformly, so the shell formula need not survive.

The result is tied to the source's Euclidean coordinate realization and does not claim affine invariance.

The theorem determines all distances from the uniform incenter to facets, but not the circumradius, John ellipsoid, or pairwise vertex metric.

Because the source already identifies \(P_t\) as a removahedron, the inradius alone can be viewed as a consequence of retained singleton facets. The nontrivial added content is the exact distance of every retained facet and the complete cardinality-shell classification. A residual risk remains for an equivalent observation in generalized-permutahedron folklore.

## References
1. Guillaume Laplante-Anfossi, *The diagonal of the operahedra*, arXiv:2110.14062, first public version 2021-10-26; Advances in Mathematics 405 (2022), 108494, DOI 10.1016/j.aim.2022.108494.
