# Scientific review

## Correctness — PASS

The operator is monotone and Lipschitz in either orientation and has unique common zero. Complexification of the real recurrence yields an explicit two-by-two transfer for each orientation, and the product over one complete cycle has real trace and determinant. The exact trace recurrence reconstructs the four short-dwell characteristic polynomials, each negative at unit multiplier for all positive stepsizes. For all fixed longer dwells, perturbation of the simple roots at zero stepsize gives the signed \(4-m\) quadratic coefficient and a vanishing second multiplier. The boundary \(m=4\) is separately resolved by a positive quartic correction. Exact polynomial checks and direct numerical state-transfer checks support, but are not substitutes for, these universal arguments.

## Originality — PASS, conditional on residual bibliographic uncertainty

The source on optimal bounded stepsizes applies to a fixed operator and does not cover switching products. Earlier periodic-game results concern an optimistic-gradient update with previous-operator dependence, and a 2026 reflected-gradient work gives qualitative divergence examples. None of the fully inspected material or accessible statement identifies the simultaneous four short-dwell instabilities, the first stable dwell \(m=5\), or the all-\(m\ge5\) perturbative law in the present current-operator model. The complete 2026 Chen–Yu manuscript was not accessible for full comparison; an equivalent pre-existing switched-period theorem cannot be excluded solely from abstract-level evidence.

## Mathematical value — PASS

This is an exact structural switching boundary, not a generic numerical counterexample or simple relabeling: every frozen operator is individually a benign monotone Lipschitz rotation with convergent small-step reflected iteration, yet four complete dwell lengths permit no positive safe stepsize at all. The fifth dwell restores small-step convergence, and the proof covers all integers beyond five. This identifies a concrete stability-design constraint on update frequencies for a one-evaluation reflected algorithm in time-varying bilinear systems. It does not purport to quantify arbitrary switching.

Self-review: passed. Independent audit: not yet performed.
