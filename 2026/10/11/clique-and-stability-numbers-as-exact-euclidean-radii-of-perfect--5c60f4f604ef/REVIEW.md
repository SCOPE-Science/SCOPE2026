# Same-model review

## Correctness
PASS. The arbitrary-dimensional proof starts from the exact irredundant Hansen facet theorem for perfect graphs and the exact signed stable-set vertex description. A clique \(C\) gives facet normal \((2\mathbf 1_C,-1)\) of norm \(\sqrt{4|C|+1}\). Central symmetry and the opposite facet pair force every inscribed ball to have radius at most the reciprocal of this norm, while the origin-centered ball at the maximum-clique value satisfies every facet. Vertex norms are exactly \(\sqrt{|S|+1}\), and a maximum stable set supplies an antipodal diameter witness for the circumradius. The uniqueness proof for the circumcenter is exact. No finite enumeration substitutes for these arguments.

## Originality
PASS. The closest middle-period source is Aprile–Cevallos–Faenza, *On 2-level polytopes arising in combinatorial settings* (arXiv:1702.03187; DOI 10.1137/17M1116684), whose Hansen section was inspected in full. The strongest same-object source inspected was Freij–Henze–Schmitt–Ziegler, *Face Numbers of Centrally Symmetric Polytopes Produced from Split Graphs* (DOI 10.37236/3315), where Lemma 5 gives the exact vertices and facets. Neither full text contains “inradius,” “circumradius,” “Euclidean,” or “radius” for this metric problem. Direct and alias searches did not locate either formula or the contact classification. The original 1977 Hansen article could not be fully read because the encountered publisher PDF endpoint required authentication, so it remains an explicit residual risk.

## Value
PASS. The canonical Euclidean Hansen polytope encodes \(\omega(G)\) and \(\alpha(G)\) in its two most basic radius invariants:
\[
\omega(G)=\frac{r^{-2}-1}{4},
\qquad
\alpha(G)=R^2-1.
\]
Maximum cliques are exactly the centered inball-contact facets, and maximum stable sets are exactly the outer-sphere vertices. This supplies a metric interpretation of two core graph invariants across the complete perfect-graph Hansen family.

## Closest literature and limitations
The structural literature gives the twisted-prism construction, signed stable-set vertices, clique-indexed facets, polarity properties, and face counts. The new step is the Euclidean optimization and exact contact classification. The inradius formula is not claimed for nonperfect graphs, where additional stable-set facets may intervene, and the metric formulas are tied to the canonical realization rather than arbitrary affine images.

Same-model review: passed. Independent audit: not yet performed.
