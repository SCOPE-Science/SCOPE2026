# Self-review

## Correctness
PASS. Definition 4.2 adds a grade-independent correction to all coordinates of a fixed factor, so the within-factor differences are exact invariants. Combining that identity with the source's top-grade contraction gives the full-coordinate limit formula without any additional analytic assumption. The explicit \((2,1)\)-grade witness satisfies every PCOMR equation, has EAIE \((0,0,0)\), and is an exact non-EAIE fixed point. The checker verifies these statements with rational arithmetic.

## Originality
PASS. Targeted semantic searches in the published finding corpus, exact source-title/DOI searches, and searches for Theorem 4.5, PCOMR, EAIE dynamic convergence, fixed points, and correction maps found no equivalent statement. An earlier same-source finding concerns a different covariant-transformation defect and explicitly did not assess the dynamic theorem. The closest full-text predecessor, Hwang–Liao–Chen–Wang (2021), uses grade-dependent corrections and proves coordinatewise contraction, so it does not imply the source-specific invariant obstruction.

## Value
PASS. Theorem 4.5 is the source's bridge from convergence of top-grade payoffs to convergence of the full multigrade allocation and underlies the advertised iterative implementation. The obstruction is structural rather than numerical: lower-grade offsets cannot change at all. The exact compatibility condition gives a sharp repair boundary, and the counterexample shows the published stopping test can terminate immediately at a non-EAIE state.

Closest literature and limitations: Liao (2025), DOI 10.3934/math.2025671, is the primary source. Hwang, Liao, Chen, and Wang (2021), DOI 10.3390/sym13081474, is the closest inspected dynamic predecessor. The 2012 duplicate-EANSC paper was located only at abstract/bibliographic level, so an older formulation could contain related dynamic ideas, but it cannot itself be a correction of the 2025 theorem.

Self-review: passed. Independent audit: not yet performed.
