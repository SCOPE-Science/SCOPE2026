# Scientific review

## Correctness

**PASS.** For each divisor \(d\mid k\), reduction of the delayed quadratic recurrence to a cyclic four-row, \(d\)-column array is exact. When the reduced delay is even, a nonzero word is impossible. At odd reduced delays the modular indicator sums force one zero per column, the two possible zero-row transitions produce the stated binomial sums, and the boundary shift gives the critical congruences \(j\equiv3-d\pmod4\) and \(j\equiv3-2d\pmod4\). The zero count in a \(4k\)-period forces every nontrivial divisor period to be a multiple of four; Möbius inversion then gives the exact primitive-cycle counts. An independent direct-state verifier checked all 34 divisor configurations with \(2\le k\le12\). Computation is corroboration, not the infinite proof.

## Originality

**PASS with residual priority uncertainty.** Finch's arXiv:2610.34300v1, Theorem 8, counts fixed states of \(T_k^{4k}\), rather than giving the complete primitive-period decomposition or the count of \(T_k^{4d}\)-fixed states for all proper divisors \(d\mid k\). Merely applying the original theorem at delay \(d\) does not resolve the reduced-delay cases \(k/d\equiv0,2,3\pmod4\); the \(3\)-case contributes a distinct binomial congruence. Actual searches of the published mathematical records and indexed literature found no equivalent statement. Cassaigne–Finch (1995) was identified as earlier related recurrence literature, but its archived PostScript full text was not accessible for comparison; possible implicit historical coverage remains an acknowledged risk.

## Mathematical value

**PASS.** The source identifies a structured population of short-period states within a nonlinear permutation but gives only their aggregate count. The new theorem resolves the natural inverse classification: every primitive cycle with period dividing \(4k\) is counted at its exact length, uniformly over all delays, with explicit nontrivial proper-period examples at delays \(9,10,12\). It also proves complete least-period rigidity at powers-of-two delays. The distinction between short-period orbits and longer, poorly understood orbits remains important; this does not classify the full permutation.

## Closest literature and limitations

S. Finch, *Three Quadratic Recurrences Modulo 3: What We Can Prove and What We Can Guess*, arXiv:2610.34300v1 (first public 2026-10-25), Section 3 and the summary, https://arxiv.org/html/2610.34300v1 . For historical background, J. Cassaigne and S. Finch, *A Class of 1-Additive Sequences and Quadratic Recurrences*, Experimental Mathematics 4 (1995), 49–60, https://www.maths.tcd.ie/EMIS/journals/EM/expmath/volumes/4/4.html . Originality is assessed to best available knowledge, not certified uniqueness. Full 1995 PostScript was not read. Computations were finite. Independent mathematical review is outstanding.

Self-review: passed. Independent audit: not yet performed.
