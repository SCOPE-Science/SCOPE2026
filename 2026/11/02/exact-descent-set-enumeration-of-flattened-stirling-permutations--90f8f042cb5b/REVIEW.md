# Mathematical review

**Correctness — PASS.** The shape sum explicitly describes every canonical type-B block partition through one zero-block size, ordered block sizes, and negative-subblock sizes. Selection factors follow from the forced least-unused positive element of each ordinary block. The known word bijection yields all and only the stated descent positions, including boundary exclusions. The resulting formula is proved for every order; the independently implemented exact enumerations through order 8, source-table checks through order 10, and prescribed-descent dynamic programming corroborate the proof. The \(O(n^3)\) claim counts integer arithmetic operations and is justified by one memoized suffix state per number of remaining labels.

**Originality — PASS, with publication-priority uncertainty.** Buck et al. (2023) supply the canonical bijection and ask for equal-length run counts. Shankar (2023) supplies total descent-number distributions, not the position-specific descent-set enumeration. Neither inspected work states the positive formula for each exact descent set or the general equal-run-length specialization. The current result does **not** claim novelty for the bijection, the ordinary run-count distribution, or maximum-run enumeration. Search and source inspection cannot rule out unindexed equivalent refinements or an unnoticed stronger multivariate formula.

**Value — PASS.** A concrete open enumerative request motivates exact equal-run-length counts; the theorem supplies them uniformly for every admissible pair of parameters and, more strongly, counts all ordered run-length compositions. Its positive binomial form and polynomial-arithmetic evaluation are useful even when only one run profile is required. This is an exact natural distribution, not a table recomputation or arbitrary parameter slice.

Limitations: no independent mathematical or priority audit; no claim for multiplicities other than two, no closed simple product, and no claim that a finite experiment is an infinite proof. References and exact proof dependencies appear in RESULT.md.

Self-review: passed. Independent audit: not yet performed.
