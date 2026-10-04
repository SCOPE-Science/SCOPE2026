# Same-model review

## Correctness

PASS. The QP correction is derived explicitly from the active linearized disk constraint. Exact identities prove that every corrected full iterate is strictly feasible, every following half-step is strictly infeasible, and the half-step error to \((0,-1)\) contracts geometrically. The Cesàro \(O(T^{-1})\) estimate follows from summability of that geometric tail. The rational replay is supporting evidence only.

## Originality

PASS. The primary paper was inspected at Algorithm 2, Theorem 4.5, Remarks 4.6--4.7, and its conclusion. It proves the first-half-step obstruction but explicitly leaves averaged feasibility open, reporting only numerical evidence. The immediate 2025 predecessor is a single-step CGM method, and targeted database searches returned no equivalent trajectory theorem.

Residual risk remains that a very recent unindexed note could independently contain the same derivation.

## Value

PASS. This closes a concrete question on the source's canonical hard instance. Perpetual pointwise infeasibility and averaged feasibility coexist exactly, so this witness cannot prove a positive asymptotic averaged-feasibility lower bound. The result is deliberately limited to this witness rather than presented as a universal theorem.

Same-model review: passed. Independent audit: not yet performed.
