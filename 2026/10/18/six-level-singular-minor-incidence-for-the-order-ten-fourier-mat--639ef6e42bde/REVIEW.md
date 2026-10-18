# Self-review

**Correctness — PASS.** The statement is a finite, fully exhaustive classification. The exact cyclotomic implementation enumerates every one of the \(210\times210\) row/column choices, expands each determinant using all \(24\) permutations, and applies the minimal polynomial \(\Phi_{10}\), which makes exact integer-vector vanishing logically equivalent to complex singularity. The independent finite-field Gaussian-elimination checker produces exactly the same 44,100 binary decisions over three primes. The code has been run from the packaged paths and its output recorded.

**Originality — PASS (best knowledge).** Tang (2017) and the published order-ten full-spark result address whether a selected Fourier row frame is full spark, not its full bad-column incidence. The latter establishes precisely the 20 zero-degree four-row sets; it does not establish the five positive degree strata or the total 5,000 singular minors. Another published theorem computes the 10 singular minors for the fixed near-consecutive row pattern, not all 210 rows. Targeted source, alias, exact-number, broader-coverage and degree-spectrum searches revealed no complete existing table. An unindexed equivalent enumeration remains possible.

**Mathematical value — PASS.** This exact incidence spectrum refines an important small composite Fourier full-spark counterexample into a quantitative rank-failure robustness census. Different four-row designs can have 0, 10, 20, 30, 110 or 130 bad choices out of 210; the six-level distribution shows substantial variation beyond the previously established full-spark dichotomy. It is a motivated natural complete finite invariant, not an arbitrary selection of entries. The result does not assert general-order consequences.

**Limitations.** No closed-form structural classification of every singular pair is claimed beyond the exact decision certificate. Complex-field correctness relies on the cyclotomic enumeration, not on modular vanishing alone. Novelty is best knowledge and independent scientific validation has not been conducted.

Self-review: passed. Independent audit: not yet performed.
