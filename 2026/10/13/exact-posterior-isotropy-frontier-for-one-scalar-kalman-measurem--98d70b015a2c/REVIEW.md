# Self-review

## Correctness
PASS. The posterior information update
\[
S_h=P^{-1}+r^{-1}hh^{\mathsf T}
\]
has direction-independent trace. For two positive eigenvalues, condition number at fixed trace is strictly minimized by maximizing determinant. The determinant lemma reduces that problem exactly to maximizing the prior Rayleigh quotient, so the unique optimal directions are the two signs of the largest-variance eigenvector.

In that eigenbasis the posterior eigenvalues are
\[
\frac{Lr}{L+r}
\quad\text{and}\quad
\mu.
\]
The condition-number envelope, isotropy noise, and prior-worsening threshold follow algebraically. The embedded exact checker replays both the isotropy case and a strict overmeasurement reversal.

## Originality
PASS with explicit residual risks. Largest-error-direction measurement selection is prior work and is not presented by itself as the new contribution. Trace/MMSE and log-determinant Kalman sensor design are also prior work. Generic condition-number-optimal rank-one matrix updates are acknowledged as nearby algebraic prior art.

The surviving claim is the complete fixed-noise two-dimensional Kalman posterior condition law together with its unique exact isotropy noise and the sharp regime in which increasing scalar measurement accuracy makes the optimally oriented posterior more ill-conditioned than the prior. Targeted semantic and exact-form searches did not locate that combined statement.

Two risks remain material: the inaccessible full body of the 1974 paper “Optimum measurements for estimation,” and possible algebraic implication from older quasi-Newton rank-one conditioning results. These are disclosed rather than treated as proved noncoverage.

## Value
PASS. The result resolves a natural tension between two standard diagnostics: total posterior uncertainty and ellipsoid anisotropy. A stronger scalar measurement always supplies more information, yet after an exactly computable isotropy point it begins to worsen conditioning. The exact sweet spot and reversal boundary are directly interpretable for sensor design and numerical covariance handling.

## Closest literature and limitations
Oshman's rule supplies prior conceptual coverage for measuring the largest-error direction. Belabbas supplies the closest continuously variable Kalman sensor-design framework but uses a trace objective. Tzoumas–Jadbabaie–Pappas use MMSE and log determinant. Wolkowicz supplies generic rank-one conditioning theory in a quasi-Newton setting.

The theorem is restricted to one scalar measurement of a two-dimensional Gaussian prior with freely selectable unit direction. Higher dimension, discrete sensor libraries, prediction dynamics, and alternative uncertainty objectives are outside scope.

Self-review: passed. Independent audit: not yet performed.
