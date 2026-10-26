# Scientific review — complete multipartite endpoint projections

## Correctness (PASS)
The Laplacian eigenspaces and the explicit five-valued potential are reconstructed in `RESULT.md`. The five edge-difference families exhaust the graph, and their exact sums yield the two stated part scores. The cut-score comparison is nonnegative for all actual part sizes when there are at least three parts; the cycle-score comparison gives the strict reversal in every \(K_{k,2,1}\), \(k\ge3\). A standard-library exact rational checker independently rebuilds all 1,572 columns of 86 small multipartite graphs; it also verifies the family identities at 38 parameter values. These tests are finite and are not used as a proof of the universal quantifiers.

## Originality (PASS with residual bibliographic risk)
The closest inspected primary work is Dilworth–Kutzarova–Ostrovskii, arXiv:2305.12582 (cycle-space invariant/minimal projections, discrete tori and Hamming graphs), together with arXiv:1807.03814 (finite Lipschitz-free spaces, diamonds and Laakso graphs). The exact orthogonal endpoint norms for **arbitrary complete multipartite graphs** and the strict opposed maximizing-edge pattern on \(K_{k,2,1}\) are not implied by their inspected theorems. A published calculation of coordinate suppression norms for cactus transportation bases acts on the quotient, not on the edge cut/cycle subspaces. Existing complete-multipartite graphical zonotope/inradius results treat different geometric invariants. The accessible historical graph-projection findings concern bicliques, edge perturbations, Cartesian products, and other graph families; they do not imply this full multipartite classification. The coverage assessment is limited to searchable records and inspected materials: overlooked electrical-network formulas are a residual risk, not a proven absence.

## Mathematical value (PASS)
This is an exact classification of two natural operator invariants for every unweighted multipartite graph with at least three parts, not a single numerical sample. The cut projection obeys a universal largest-two-parts rule, yet the complementary cycle projection can exclude the largest part. The infinite strict reversal family has explicit sharp rational norms and an exactly matching orbit-exchange margin, distinguishing these coupled projection problems in a structurally natural graph class.

## Limits
No minimum-over-all-projections assertion, weighted analogue, or independent validation is made. The proof applies to all parameters in the stated domain; the checker covers only the documented finite configurations.

Self-review: passed. Independent audit: not yet performed.
