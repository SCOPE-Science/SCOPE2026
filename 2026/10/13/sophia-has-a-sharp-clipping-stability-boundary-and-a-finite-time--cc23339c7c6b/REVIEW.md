# Review

## Correctness

PASS. Under the stated exact-Hessian and zero-memory assumptions, the practical Sophia update reduces coordinatewise to
\[
T(x)=x-\eta\,\operatorname{clip}(x/\gamma,1).
\]
The three branches of this map give an exact complete classification: global convergence for every start occurs precisely for \(0<\eta<2\gamma\); the post-entry multiplier is \(1-\eta/\gamma\); every \(\eta\ge2\gamma\) has the explicit two-cycle \(\pm\eta/2\); and \(\eta=\gamma\) is exact soft-thresholding.

Risk: stochastic Hessian estimates, momentum memory, and an active denominator floor change the map.

## Originality

PASS. The defining Sophia source gives the practical clipped diagonal-Hessian recurrence and proves condition-number-independent convergence for a simplified full-Hessian variant. The inspected full text does not state the sharp practical diagonal boundary, the explicit failure cycle, or the finite-time resonance. Focused published-record and owned-ledger searches found no implication-equivalent Sophia result.

Residual risk: an equivalent elementary clipped-Newton calculation may exist under different terminology.

## Value

PASS. The theorem directly resolves how Sophia's two defining scalar controls interact in the exact-curvature regime. It sharpens condition-number independence into a complete dynamical law and identifies a finite-time setting where every diagonal quadratic is solved exactly regardless of its curvature spectrum.

Self-review: passed. Independent audit: not yet performed.
