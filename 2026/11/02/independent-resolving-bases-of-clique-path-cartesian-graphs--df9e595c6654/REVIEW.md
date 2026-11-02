# Scientific review: independent resolving bases of clique-path Cartesian graphs

## Correctness

PASS. The distance identity for the Cartesian product reduces every potential collision to an integer-valued monotone function whose parity is independent of the landmark position. Distinct fibers and colors enforce the lower bounds; for at least four colors the parity argument proves every candidate injection resolves, while the three-color family has a genuine monotonicity obstruction separating alternating and nonalternating repeated colors. The two-color case is forced to endpoint landmarks. This supplies necessary and sufficient conditions, not an extrapolation from computer experiments. An independently implemented BFS enumeration agrees across 28 small instances, including all no-solution boundaries.

## Originality

PASS, with residual priority uncertainty. Chartrand, Saenpholphat and Zhang (2003), DOI:10.21136/MB.2003.134003, introduce independent resolving numbers but do not classify clique–path Cartesian products. Cáceres et al. (2007), arXiv:math/0507527, establish the ordinary metric dimension and graph-product projection bounds, which do not imply that a minimum basis can be independent. Suganya and Arumugam (2021), DOI:10.1080/09728600.2021.1963643, study independent resolving sets of grids and cylindrical products, without the exact clique-path existence criterion, complete minimum-basis classification, or multiplicities in the inspected text. Searches for independent metric bases of \(P_L\square K_q\) and for the explicit exceptional \(K_3\) count produced no dominating equivalent result in accessible sources. Relevant nonindexed or differently named results remain a priority risk.

## Mathematical value

PASS. The article introduces independent resolving sets for Cartesian products and tests whether graph-product bases can be made independent. This exact family gives a complete feasibility threshold when the clique factor grows with the path, an exceptional strict gap between independent and ordinary metric dimensions at three colors, and a closed formula for every minimum independent basis. The full counting classification provides materially more information than a single extremal number and is not implied by the known Cartesian projection lemma.

## Evidence and limits

The proof and exact test program are in the accompanying files. The source comparisons are limited to accessible published text and recorded literature searches; no claim of worldwide uniqueness or independent validation is made. The code verifies only finite cases. The theorem covers only independent *minimum* resolving sets, not all larger resolving sets.

Self-review: passed. Independent audit: not yet performed.
