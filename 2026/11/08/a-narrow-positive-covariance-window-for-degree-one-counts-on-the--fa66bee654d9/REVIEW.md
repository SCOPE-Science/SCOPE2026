# Self-review

## Correctness — PASS
Exact probability count is independently reconstructed for a marked left and right vertex. Their joint event splits into shared-edge-present and shared-edge-absent cases, producing the displayed \(P_{n,k}\) and \(J_{n,k}\); all finite boundary values have the zero-binomial convention. An explicit falling-factorial product for \(J/P^2\) and uniform Taylor expansion through order \(n^{-3}\) give the sparse and critical-window limits. The separately runnable verifier performed 1,302 exact assertions, including independent enumeration of every binary matrix of order at most four. Enumeration is not treated as an all-size proof. At \(|x|=2/\sqrt3\) the theorem makes no finite-sign assertion.

## Originality — PASS (historical-priority risk acknowledged)
McKay and Skerman (arXiv:1302.2446, especially Theorem 1(c)) address the same fixed-edge bipartite model, but their general approximation requires density larger than the sparse scaling here and their reference model has independent two-sided degree sequences. It does not imply the signed covariance at order \(n^{-1}\). Palka (1984), *On the degrees of vertices in a bichromatic random graph*, is a close historical source; its full text was not accessible. Eicker, Siddiqui and Mielke (1972), *A matrix occupancy problem*, presents a further bibliographic risk. The originality assessment concerns the exact cross-count covariance **together with the sharp critical-window sign reversal** and is qualified by these access limits.

## Mathematical value — PASS
Counts of degree-one vertices in each side of a bipartite graph are natural local structural diagnostics. The result identifies a sharp and counterintuitive dependence reversal caused by fixed-size sampling: coarse sparse asymptotics are negative away from mean degree two, but a square-root-width window has positive covariance. Both a fully exact finite expression and a quantitatively sharp limiting boundary are supplied.

## Verification limits and closest literature
The main exact enumeration and uniform asymptotics are proved in RESULT.md. The separate checker uses finite model enumeration only. The available full text of McKay and Skerman was compared by mathematical implication, not title. The inaccessible historical sources leave a specific priority risk. No claim of independent external validation or whole-distribution ordering is made.

Self-review: passed. Independent audit: not yet performed.
