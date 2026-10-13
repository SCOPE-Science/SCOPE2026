# Review

## Correctness

PASS. For \(r\lambda>1\), the standard first step crosses the scalar optimum. The resulting iterate and stored momentum have opposite signs, so the source gate removes momentum. A direct induction proves that this sign mismatch then persists forever, reducing SPI exactly to gradient descent. The ordinary-momentum comparison follows from the complete second-order Jury conditions.

Risk: the theorem classifies the overshoot branch only and assumes zero initial momentum.

## Originality

PASS. The defining source already states the qualitative stale-momentum suppression mechanism and gives a conservative convergence theorem. It does not state that one scalar overshoot permanently disables momentum or that this creates a strict deterministic stability deficit relative to ordinary momentum. Focused published-record and owned-ledger searches found no implication-equivalent result.

Residual risk: an equivalent restart calculation may exist in older control literature under different terminology.

## Value

PASS. The sign-consistency gate is SPI-Optimizer's defining design choice, and large-learning-rate robustness is one of its reported empirical advantages. The exact scalar law shows both sides of the mechanism: stale momentum is removed maximally, but so is momentum's enlarged linear-stability interval.

Self-review: passed. Independent audit: not yet performed.
