# same-model review

## Run identity

- Source run ID: `scope-20260917T083426Z-7f4c9a2e`
- Research start: `2026-09-17T08:34:26Z`
- Research end: `2026-09-17T08:39:06Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`
- Model / source mode: `GPT-5.6 Sol / UNKNOWN`

## Correctness

**PASS (same-model assessment).**

The source run checked shell capacities, the global shell totals, and the exact number `d*2^(d-1)` of hypercube edges. It explicitly avoided assuming monotonicity under adding landmarks: every `m<=d+1` was checked separately. The admissible-histogram set is a relaxation of geometric realizability, so using it can only weaken the obstruction. Two independent exact algorithms reportedly recomputed all finite counts and score minima.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

Targeted searches for the exact `Q_7`–`Q_10` lower bounds, a general `d+2` phrase, weighted-histogram methods, and Allikvere's certificate sequence did not locate these bounds or a stronger theorem implying them. The closest arXiv record remained v1 from August 2026. Unpublished or very recent unindexed work remains a residual threat.

## Value

**PASS (same-model assessment).**

The source run characterizes the result as substantive short-note/lemma-level progress: it advances exact-minimum questions for four dimensions and introduces a reusable linear obstruction on distinct histogram packings, while leaving large gaps to the known upper bounds.

## Independence / candidate history

The run acknowledges that the same framework independently reproduces the preceding SCOPE `Q_6>=8` result but does not count that as fresh. Its fresh target is `Q_7`–`Q_10`. It first considered opaque integer-feasibility certificates, then revised the approach to explicit small symmetric linear weight vectors. A tentative extension to `d=11` failed with the simple tail weights, so no broader theorem was asserted.

## Availability limitation

The supplied package did not include the verifier and report files. They are not invented in this archive.

## Review disclaimer

This is not independent validation, peer review, or a guarantee of scholarly priority.
