# same-model review

## Run identity

- Source run ID: `SCOPE-20260917T101839Z-001`
- Research start: `2026-09-17T10:18:39Z`
- Research/report finalized: `2026-09-17T10:29:44.685353Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Result type: valuable unexpected finding

## Correctness

**PASS (same-model assessment).**

The source run reports exact arithmetic for the probability certificate, including the full size interval `254` through `508`, exact `q`, the conservative rational bound `q<293/500`, and an expectation bound below `0.09`. It checked that `127` is prime, `w=17` satisfies the marked-pair capacity condition, and that the parent construction's stated meet realization applies in this prime range.

The structural implication from the absence of admissible sets to an NCI counterexample is imported from Wilhelm's published lemmas rather than reproved from first principles.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

The parent source publicly states a `p>=10^5` theorem and uses `p=100003` for its finite example. Searches for `p=127`, `2,080,643`, smaller NCI counterexamples, and quantitative improvements found no public match. The strongest identified threat is unpublished/private work, especially Alexander Walz's private communication described by Wilhelm, plus possible unindexed author-side optimizations.

## Value

**PASS (same-model assessment).**

The source run characterizes the improvement as a structural tightening of the incidence count plus an exact finite first-moment certificate, shrinking the displayed finite upper bound by roughly `4.8e8` while keeping the same construction architecture. It does not claim a new conceptual refutation of NCI or a minimum-size theorem.

## Independence

The source run reports no earlier execution accessible within that task and no reused prior proof or unfinished direction. The scheduler did not expose a hard non-overlap lock.

## Review disclaimer

This is not independent validation, peer review, or a guarantee of scholarly priority.
