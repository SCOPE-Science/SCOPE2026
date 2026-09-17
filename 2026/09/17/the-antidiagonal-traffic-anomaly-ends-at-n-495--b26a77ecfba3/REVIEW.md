# same-model review

## Review status

- Research/report finalized: `2026-09-17T11:04:11.514014Z`
- Reported status: `SAME_MODEL_REVIEW_PASS`

## Correctness

**PASS (same-model assessment), with an explicit analytic-tail risk.**

The source report re-derived the exact `R_n(k)` formula and consecutive ratio, symbolically checked the sign polynomial, used exact integers for the finite bridge, recomputed the `n=495` witness, checked the even/odd off-centre estimates and central-binomial inequalities, and checked monotonicity of its envelope.

It explicitly identifies the main remaining risk as a subtle algebraic or inequality-direction mistake in the analytic tail.

## Originality

**PASS, qualified to the best of our knowledge (same-model assessment).**

The primary September 2026 preprint states the all-`n>=496` assertion as Conjecture 7.4 and reports finite verification only through 2000. Targeted searches found no later proof. Realistic threats are an unindexed author revision, a simultaneous preprint, or older sharp binomial inequalities that make part of the proof routine.

## Value

**PASS (same-model assessment).**

If correct, the result changes a finite experimental observation into a sharp infinite theorem and identifies `n=495` as the last anomalous grid size. The asymptotic envelope below one gives a structural reason for eventual disappearance.

## Review disclaimer

This is not independent validation, peer review, or a guarantee of scholarly priority.
