# Clique and stability numbers as exact Euclidean radii of perfect-graph Hansen polytopes
## Finding
Let \(G=(V,E)\) be a finite perfect graph, let \(n=|V|\), let \(\omega(G)\) be its clique number, and let \(\alpha(G)\) be its stability number. In the canonical Hansen realization
\[
\mathrm H(G)
=
\operatorname{conv}
\{(\chi_S,1),(-\chi_S,-1):S\subseteq V\text{ stable}\}
\subset\mathbb R^{n+1},
\]
with the standard Euclidean metric,
\[
\boxed{
r(\mathrm H(G))=\frac{1}{\sqrt{4\omega(G)+1}}
}
\]
and
\[
\boxed{
R(\mathrm H(G))=\sqrt{\alpha(G)+1}.
}
\]

The origin is an incenter and the unique circumcenter. The facets tangent to the centered largest inscribed ball are exactly the two signed facets indexed by maximum cliques. The vertices on the minimum enclosing sphere are exactly the two signed vertices indexed by maximum stable sets.

Equivalently, the two graph invariants can be recovered metrically from this canonical realization:
\[
\omega(G)=\frac{r(\mathrm H(G))^{-2}-1}{4},
\qquad
\alpha(G)=R(\mathrm H(G))^2-1.
\]

## Assumptions and scope
The realization is the standard twisted-prism realization used for Hansen polytopes: the last coordinate is \(1\) on the top copy of the stable set polytope and \(-1\) on its reflected copy. The theorem is metric and therefore depends on this canonical Euclidean realization; it is not invariant under arbitrary affine equivalence.

Perfectness is needed for the stated inradius formula because it supplies the complete clique-indexed facet description. The circumradius calculation itself uses only the vertex description and therefore remains valid for arbitrary graphs, but the single claim here is restricted to perfect graphs.

The empty graph on \(n\) vertices gives the canonical parallelepiped realization of a cube, with \(\omega(G)=1\), while the complete graph gives the canonical affine realization of a cross-polytope.

## Proof
Write points of \(\mathbb R^{n+1}\) as \((x,t)\), where \(x\in\mathbb R^V\). For every clique \(C\subseteq V\), define
\[
\ell_C(x,t)=2x(C)-t.
\]
A full-text Hansen-polytope facet theorem for perfect graphs gives the irredundant description
\[
-1\le \ell_C(x,t)\le 1
\qquad
\text{for every clique }C\subseteq V,
\tag{1}
\]
including the empty clique.

For completeness, validity is visible directly on the vertices. At a top vertex \((\chi_S,1)\),
\[
\ell_C(\chi_S,1)=2|S\cap C|-1\in\{-1,1\},
\]
because a stable set meets a clique in at most one vertex. At the opposite vertex the sign is reversed.

The normal vector of either facet in (1) is
\[
a_C=(2\mathbf 1_C,-1),
\]
so
\[
\|a_C\|_2=\sqrt{4|C|+1}.
\tag{2}
\]
Because \(\mathrm H(G)\) is centrally symmetric, the origin is an incenter. More explicitly, if a Euclidean ball \(B(c,r)\) lies in \(\mathrm H(G)\), the two opposite inequalities indexed by \(C\) imply
\[
|\langle a_C,c\rangle|+r\|a_C\|_2\le1.
\]
Hence
\[
r\le\frac1{\|a_C\|_2}
\]
for every clique \(C\). Taking a maximum clique gives
\[
r\le\frac1{\sqrt{4\omega(G)+1}}.
\]
Conversely, the ball centered at \(0\) with that radius satisfies every inequality (1), since \(|C|\le\omega(G)\). This proves the inradius formula.

Equality in the centered facet distance occurs precisely when
\[
\sqrt{4|C|+1}=\sqrt{4\omega(G)+1},
\]
so the centered maximal ball is tangent exactly to the two signed facets belonging to maximum cliques.

For the circumradius, the vertices are exactly
\[
\pm(\chi_S,1)
\]
as \(S\) ranges over stable sets. Their squared Euclidean norms are
\[
\|(\chi_S,1)\|_2^2=|S|+1.
\]
Therefore every vertex lies in the centered ball of radius \(\sqrt{\alpha(G)+1}\), and equality holds exactly for maximum stable sets. Convexity of the Euclidean norm implies the whole polytope lies in that ball.

Choose a maximum stable set \(S\). Any Euclidean ball containing \(\mathrm H(G)\) must contain the antipodal pair
\[
v=(\chi_S,1),
\qquad
-v.
\]
Their distance is \(2\|v\|_2=2\sqrt{\alpha(G)+1}\), so every enclosing ball has radius at least \(\sqrt{\alpha(G)+1}\). The centered ball attains this lower bound, proving the circumradius formula.

The circumcenter is unique. If a ball of radius \(\|v\|_2\) centered at \(c\) contains both \(v\) and \(-v\), then
\[
\|v-c\|_2^2\le\|v\|_2^2,
\qquad
\|-v-c\|_2^2\le\|v\|_2^2.
\]
Adding the two inequalities yields \(2\|c\|_2^2\le0\), hence \(c=0\).

## Verification
The proof is valid in arbitrary dimension and does not infer an infinite statement from finite computation. The source-dependent premises were checked against full text: the twisted-prism vertex description and, for perfect graphs, the irredundant clique-indexed facet inequalities.

The accompanying `verify.py` independently enumerates several small perfect graphs. It reconstructs all stable sets and cliques, checks every declared facet inequality on every Hansen vertex, checks exact affine rank for both signed facets, and verifies that the largest facet-normal norm and largest vertex norm reproduce the formulas above. These calculations are corroborative only.

## Relationship to prior work
Aprile, Cevallos, and Faenza treat Hansen polytopes as a major graphical family of \(2\)-level polytopes and use their vertex and facet counts in a vertex-facet trade-off theorem. A full-text earlier paper of Freij, Henze, Schmitt, and Ziegler records the exact vertex set and the irredundant facet description
\[
-1\le -t+2x(C)\le1
\]
for every clique \(C\) of a perfect graph. Those structural results are the premises of the metric calculation here.

Neither inspected full text contains the terms “inradius,” “circumradius,” “Euclidean,” or “radius” in connection with Hansen polytopes. Targeted searches using Hansen polytope, twisted prism, clique number, stability number, inradius, circumradius, and the exact square-root forms did not locate a prior theorem giving these radii or the tangent/outer contact classification.

The original 1977 Hansen article is the historical primary source for the construction. Its journal landing page was accessible, but the PDF endpoint encountered in this run required authentication, so that article was not used to support a whole-document noncoverage assertion.

## Limitations
The inradius statement is proved only for perfect graphs, where clique inequalities give the full irredundant facet description. For a nonperfect graph, additional stable-set facets can reduce the inradius.

The formulas refer to the canonical twisted-prism coordinates and the standard Euclidean norm. Arbitrary affine images can change both radii.

The literature comparison does not exclude an equivalent formula hidden under different terminology or normalization in inaccessible or unindexed sources. The original 1977 article remains an explicit access-related residual risk.

## References
1. Manuel Aprile, Alfonso Cevallos, and Yuri Faenza, *On 2-level polytopes arising in combinatorial settings*, arXiv:1702.03187, first public version 2017-02-10; SIAM Journal on Discrete Mathematics 32 (2018), 1857–1886, DOI 10.1137/17M1116684.
2. Ragnar Freij, Matthias Henze, Moritz W. Schmitt, and Günter M. Ziegler, *Face Numbers of Centrally Symmetric Polytopes Produced from Split Graphs*, Electronic Journal of Combinatorics 20(2) (2013), #P32, DOI 10.37236/3315.
3. A. B. Hansen, *On a Certain Class of Polytopes Associated with Independence Systems*, Mathematica Scandinavica 41 (1977), 225–241, DOI 10.7146/math.scand.a-11716.
