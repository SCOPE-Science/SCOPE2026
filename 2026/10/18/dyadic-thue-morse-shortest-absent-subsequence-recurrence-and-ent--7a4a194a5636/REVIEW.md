# Self-review

## Correctness — PASS
The claim counts absent strings, not embeddings: any binary query of length \(k+1\) is absent precisely when no boundary pair matches the corresponding 01/10 block. This is proved by a complete greedy matching dichotomy. The matrices count such boundary-constrained strings once each; the Thue–Morse complement relation gives \(P_{r+1}=(P_rJ)^2\), and determinant \(-1\) plus Cayley–Hamilton gives the exact quadratic recurrence for all indices. The linear inhomogeneous logarithmic recurrence is solved explicitly; the perturbation series is absolutely convergent, establishing the claimed entropy and \(O(1)\) remainder. Finite direct enumeration, direct matrix multiplication, and an independent distinct-subsequence dynamic program agree through their stated ranges. A computation by itself is not being treated as an infinite proof.

## Originality — PASS, with disclosed residual risk
The general shortest-absent-subsequence framework and the precise triangular transfer matrices for concatenated binary 01/10 blocks are **known**. The closest published note optimizes all such block sequences and derives Fibonacci extrema; it neither states nor implies an explicit *evaluated* Thue–Morse-specific trace-square recurrence and entropy constant without the additional Thue–Morse self-similar analysis supplied here. Related complete-source comparisons with the 2021 absent-subsequence paper and the 2024 tight-bounds paper did not locate such a theorem, and targeted external mathematical searches and research-record searches likewise found none. General algorithms that can compute each term separately do not constitute the uniform nonlinear recurrence or its limit. Residual risk: an equivalent Thue–Morse matrix-product/trace-map result could have appeared under continued-fraction or automata terminology outside the inspected sources. Search failure is not proof of uniqueness.

## Mathematical value — PASS
The precise count for every dyadic prefix of a canonical aperiodic automatic word refines algorithmic and extremal counting results into an explicit infinite family. The two-integer renormalization reduces a matrix product of exponentially many factors to logarithmically many scalar steps, and the positive explicit entropy series quantifies exponential growth in input length. This is a motivated structural invariant, not an arbitrary isolated small-length census or a rebranding of the known transfer matrix.

## Scope and limitations
Only the prescribed binary dyadic Thue–Morse prefixes and shortest absent scattered subsequences are covered. The general 01/10 matrix-transfer representation is prior work. The indicated asymptotic constant is evaluated by a convergent series; the finite checks support but do not replace the theorem. Independent assessment has not occurred.

Self-review: passed. Independent audit: not yet performed.
