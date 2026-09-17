# same-model review

## Run identity

- Source run ID: `SCOPE-20260917T100054Z-R02`
- Research start: `2026-09-17T10:00:54Z`
- Research end: `2026-09-17T10:15:37Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Result type: valuable unexpected finding

## Correctness

**PASS (same-model assessment).**

The new step sharpens only the probabilistic estimate inside Wilhelm's structural framework. The source certificate checks every new numerical inequality with exact integer/rational arithmetic, including primality of `571`, the exact hypergeometric bound, derivative and term-ratio bounds, the first-term estimate, and the final expectation. The source run also checked the subtle use of a real lower bound `S(t)` for an integer number of traces.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

The closest public source states only the `p>=10^5` theorem and the `p=100003` example. Searches for `571`, `186821495`, and improved quantitative versions did not locate the present certificate. The source report flags extremely recent or unpublished work as the main threat, including private work mentioned by Wilhelm whose details were inaccessible.

## Value

**PASS (same-model assessment).**

The method is conceptually moderate because it remains the same first-moment construction, but the quantitative compression is large: the displayed lattice-size upper bound falls from about `1.0e15` to `186,821,495`, directly addressing a size question raised in the source paper.

## Independence

The accessible previous run concerned generalized strong-majority edge colouring. This run deliberately moved to affine incidence geometry and NCI lattices, without using the previous theorem or method as a starting point.

## Review disclaimer

This is not independent validation, peer review, or a guarantee of scholarly priority.
