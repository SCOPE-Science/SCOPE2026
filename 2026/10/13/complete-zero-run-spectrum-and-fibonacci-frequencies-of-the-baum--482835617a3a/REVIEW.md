# Scientific review

**Correctness — PASS.** The definition of the Baum–Sweet word is fixed at \(b(0)=1\), avoiding the alternative zero-index convention. An exact decomposition of its accepted binary strings into the tokens \(1\) and \(00\) proves the central gap sizes. Counting recursion-tree interfaces yields the stated Fibonacci formulas, and the complete limiting probability law follows by Binet asymptotics. A standalone direct-definition/recurrence verifier passed 262144 positions and all dyadic cutoff counts through eighteen; the proof does not extrapolate from the checks.

**Originality — PASS, with residual risk.** Merta (arXiv:1803.00292v1), §2, studies the same accepted one-position set but proves parity/regularity statements and a coarse zero-run result, not its complete zero-run spectrum with exact frequencies. Merta's Theorem 4.6 on first differences refers instead to a formal inverse. OEIS A060142 enumerates the accepted indices and gives a generator, not the full length-and-frequency theorem. Shallit–Xu (arXiv:2311.14961v1) studies a different factorization invariant. Historical-claim and targeted semantic comparison did not show a stronger covering theorem. Unindexed equivalent work remains a genuine risk.

**Value — PASS.** This is a natural complete classification of zero-run lengths for a classical automatic word: unlike an unspecified assertion of arbitrarily long zero runs, it excludes all other lengths and gives exact finite-prefix multiplicities together with a probability law. Dyadic cutoffs are intrinsic to the binary automaton and yield exact uncensored runs. The unproved arbitrary-cutoff distribution is expressly excluded.

Self-review: passed. Independent audit: not yet performed.
