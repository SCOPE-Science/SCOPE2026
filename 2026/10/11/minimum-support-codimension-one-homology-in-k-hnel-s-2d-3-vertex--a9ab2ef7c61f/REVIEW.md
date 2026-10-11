# Review of Minimum-support codimension-one homology in Kühnel’s \(2d+3\)-vertex sphere-bundle family

## Correctness
**PASS.** The proof separates the topological and combinatorial parts. The published cyclic construction identifies the complex with an \(S^{d-1}\)-bundle over \(S^1\), so the Wang sequence over \(\mathbf F_2\) gives one-dimensional codimension-one homology and shows that a consecutive fiber sphere is nonzero. The support lower bound is elementary. The gap argument then proves that every \(d+1\)-vertex cycle must come from one of the consecutive interior \(d\)-faces. Exact replay for \(3\le d\le7\) independently reconstructs the complexes and verifies the missing-face and boundary-rank assertions. Risk: the finite replay does not cover all dimensions, but the infinite proof does not depend on it.

## Originality
**PASS.** Full text was inspected for the exact cyclic construction and uniqueness theorem in arXiv:math/0610829, for the family’s extremal description in arXiv:math/0506372, and for its tightness framework in arXiv:1207.5599. Focused semantic and web searches used the object name, the parameter \(2d+3\), “missing \(d\)-simplex,” “minimum vertex support,” “induced sphere,” and “codimension-one homology.” No inspected source states the conjunction proved here: exactly \(2d+3\) missing \(d\)-simplices, all consecutive, and exactly those supports realizing the minimum nonzero codimension-one class. Risk: the full 1986 Kühnel article and some older unindexed computations were not directly accessible, so an unindexed prior observation remains possible.

## Value
**PASS.** This is a uniform structural theorem for the canonical vertex-minimal non-simply-connected triangulation in every dimension \(d\ge3\), not a dimension-by-dimension census. It identifies the sharp vertex-support systole of the fiber class and all minimizers. The exact minimizer classification links the cyclic handle construction to a natural local-to-global homology invariant and can be reused when comparing extremal sphere-bundle triangulations.

## Closest literature and limitations
The closest exact-object source is Bagchi–Datta’s construction and uniqueness theorem; the closest broader framework is the tightness work, which guarantees strong induced-homology behavior but does not enumerate the missing \(d\)-faces or derive the support systole. The result is mod-two only and does not address larger supports or the \(2d+4\)-vertex families.

Same-model review: passed. Independent audit: not yet performed.
