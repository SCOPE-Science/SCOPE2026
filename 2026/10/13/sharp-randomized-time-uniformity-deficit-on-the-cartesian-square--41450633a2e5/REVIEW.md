# Scientific review

## Correctness — PASS

The graph/Hamiltonian normalization is the unweighted adjacency walk on nine vertices, and the objective uses every matrix entry. The identity \(A_3^3=2A_3\) yields the exact real mixing matrix \(B(x)\). The Cartesian Kronecker factorization is exact. Reflection-symmetrization follows from column-permutation invariance and norm convexity, not from assuming symmetry of arbitrary initial observation laws. The 81-entry moment expansion is reproduced symbolically by `verify.py`. For the admissible moment range \(s^2\le q\le s\), the objective is increasing in \(q\); the remaining quartic has a unique minimizer since its cubic derivative has strictly positive derivative. All extremizers have cosine support at the two points and reflection-invariant average forces equal weights. Numerical exponentiation independently checks an attaining two-time law. Finite checks are supplementary to the analytical proof.

## Originality — PASS, with residual risk

The closest primary source, Baptista–Coutinho–Marques (2023), explicitly gives uniform time-randomized mixing of \(P_3\) (§3.2) and explains common-clock product covariance (§5). Its tensor product formula and trace bounds do not determine the unrestricted 81-entry Frobenius optimum or uniquely characterise the optimal time-phase distribution. Coutinho–Guo (2024, §4.2) surveys the generalized averages without this optimization. Lo et al. (2005) treats big-O limiting average uniformity, not this exact arbitrary-law functional. Semantic database searches covered name, product, covariance and metric aliases but cannot exclude all different vocabulary; a stronger unknown quantitative product theorem remains a risk.

## Value — PASS

The original primary article singles out the failure of simple tensorization for a common random time. Quantifying the optimal global deviation and constructing its unique optimal cosine distribution resolves a natural nine-vertex test of that interaction. The minimizing shared-clock law is **not** the factor law known to achieve exact uniform mixing, and that factor law pays a strictly larger exact penalty \(1/9\). This is a motivated sharp boundary rather than an arbitrary numerical slice. No general product theorem or operational noise-resilience claim is asserted.

## Literature limits

Prior qualitative factor mixing and tensorization are fully credited. The source-level comparison covers the primary paper's full §§3 and 5, the survey's full §4, and the older Cartesian paper's §§2 and 5. The remaining uncertainty is unindexed or differently named quantitative optimization literature, not correctness of the elementary algebra.

Self-review: passed. Independent audit: not yet performed.
