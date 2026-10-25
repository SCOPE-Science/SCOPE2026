# Self-review

## Correctness

**PASS.** The claimed domain is all positive real parameters, with special points \(1/3\), \(1\), and \(3\) handled explicitly. The proof derives all twelve supporting facets for \(1<\lambda<3\), rather than extrapolating facet normals from numerical hull computations, and gives necessary-and-sufficient strict illumination criteria. The no-two-negative-vertices lemma supplies a weighted lower bound of four, while an explicit continuous-parameter construction of four actual directions supplies the matching upper bound. A separate inequality argument certifies the exact single-direction vertex-capacity threshold at \(\lambda=2\); reciprocal scaling covers the smaller parameter interval. Simplex and cube endpoints are directly verified. Rational-arithmetic tests of the facet planes and witnesses were rerun from the packaged `verify.py`; finite directional grids are explicitly not used as infinite proofs.

## Originality

**PASS under inspected evidence; historical priority remains provisional.** The nearest broad bound, Gorodzha, arXiv:2609.23913 (2026), characterizes equality in the universal \(2^d\) fractional upper bound but does not determine the four-direction value or the three-versus-four vertex-capacity transition for polar tetrahedral truncations. Livshyts and Tikhomirov, arXiv:1710.05070 (2017), prove an upper bound of seven near the three-dimensional cube, which does not imply this exact four-valued limit. Published cube–octahedron-intersection and independent-corner-truncation constructions have different vertex/facet systems and cannot be substituted for this result. Searches for triakis tetrahedron, scaled opposite tetrahedra, and polar truncated-simplex illumination did not identify exact coverage; searches are not proof of novelty. The two most directly applicable scholarly papers were inspected beyond snippets; neighboring research-index records were available as summaries only.

## Mathematical value

**PASS.** The theorem completely evaluates two natural illumination invariants for a canonical three-dimensional geometric deformation connecting a tetrahedral dual, the Catalan triakis tetrahedron, and a cube. The surprising discontinuity from four to eight at rectification and the independent sharp single-direction transition at one-quarter truncation depth give motivated geometric boundary information. The invariant is standard, the parameter has a direct physical construction, and the exact all-parameter proof is not a table recomputation.

## Literature comparisons and limits

The stated novelty is not a universal improvement to Hadwiger's conjecture or an extension of the general fractional bound. It does not cover arbitrary nonsymmetric perturbations or unrelated polyhedral families. The bibliographic search may miss a differently named homothetic-tetrahedra result, and inaccessible full records in the research index were not treated as whole-document negative evidence.

Self-review: passed. Independent audit: not yet performed.
