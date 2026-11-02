# Mathematical review

## Correctness

**PASS.** The truncated noncommutative signature records exactly scattered-subsequence counts and is multiplicative. Degree-one zero-sum differences, degree-two elementary commutators, and the inductive \((U a V,V a U)\) gadgets span all required homogeneous free Lie degrees. The bracket formula \([P,X_a+C]\) is obtained by expanding the precise signature difference and checking the degree boundary. The coefficient matrix \(I+c\mathbf1^{\mathsf T}\) has determinant \(1+|U|\), ruling out a loss of spanning rank. Uniform expansion multiplies a leading degree-\(j\) difference by \(m^j\); the telescoping product calculation makes each base-\(2^j\) digit independent at the lowest differing degree. Double counting recovers all shorter decks from the actual length-\(k\) deck. Uniform suffix padding preserves injectivity. These implications prove a lower bound at every sufficiently large length; the upper bound is sourced to Theorem 5.1 of the cited 2026 paper. Exact standalone checks confirm the selected ranks and finite cases, without being substituted for the infinite proof.

## Originality

**PASS, subject to publication-priority risk.** The closest primary source (Nilforoushan–Parvaresh, arXiv:2609.23106, Sections 5–8) states the desired general lower bound as Conjecture 8.1, proves only special lower-bound cases, and thus does not imply this theorem. Lejeune–Rigo–Rosenfeld (2020), Section 4, proves an earlier general upper bound and the \(k=2\) growth law, not the all-degree lower bound. The accessible abstract and finite table for Chrisnata et al. (2023) document weaker bounds. The full 2023 journal text was access-restricted, which is recorded as a risk rather than counted as a conclusive negative inspection. Comparison with accessible claim descriptions on related subsequence coding and word-equivalence topics did not identify a theorem with the same all-parameter conclusion. Standard free Lie theory is used as prior mathematics, not presented as novel.

## Value

**PASS.** The theorem settles a specifically formulated all-parameter asymptotic counting conjecture arising in the zero-error capacity of short-subsequence readout. It identifies the exact polynomial degree for every fixed alphabet and read length, and gives an explicit construction that explains how each Lyndon dimension is independently realizable at its full weighted order. The result substantially exceeds a finite-parameter exercise, while making no unsubstantiated exact-constant or efficiency claim.

## Limitations and closest literature

The proof establishes only fixed-parameter order of growth. The constants may be large, and the direct construction does not optimize word length or code complexity. Classical nilpotent-group growth ideas are related but do not automatically yield the fixed-length positive-word injective construction stated here. Priority remains subject to earlier unindexed or inaccessible literature, particularly the full 2023 counting paper. Independent validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
