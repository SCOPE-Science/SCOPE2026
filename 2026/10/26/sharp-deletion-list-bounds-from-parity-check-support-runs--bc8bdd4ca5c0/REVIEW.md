# Review of the support-run deletion-list theorem

**Correctness: PASS.** The insertion-tree edges correspond bijectively to deleted positions; their labels are recovered as the interval symmetric difference of odd-syndrome vertices, proving the run upper bound. A concrete compatible construction attains the bound whenever the run parity condition is solvable, and the unique even-run exception is proved by an odd-syndrome contradiction and matched by a two-odd-parent witness. The Fibonacci exceptional count follows from unique tilings. Exact finite computations from the standalone source reproduce the stated lists.

**Originality: PASS with residual risk.** Remark 9 of Verma--Hollanti--Tajeddine (arXiv:2610.23270v1) covers the alternating singleton-run mask; it does not imply the run-count inequality, equality for arbitrary parity-check supports, or the exponential prevalence statement. Earlier half-Singleton and insdel-construction papers focus on edit distances and rates rather than exact output parent-list sizes. Semantic prior-result searches found no stronger or equivalent formula. An implicit older combinatorial treatment remains a priority risk.

**Value: PASS.** Exact worst-case deletion-list size is a fundamental receiver ambiguity invariant in high-rate binary linear codes. The theorem translates coordinate geometry of the lone parity-check row into an actionable exact formula for all but an exponentially small subset of masks, and sharply delineates a parity-dependent boundary without relying on a finite code census.

**Limitations.** No equality claim for all odd-count, all-even-length multi-run masks, and no general claim for one-insertion received words or multiple edits. Independent priority and validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
