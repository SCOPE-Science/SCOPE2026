# Same-model review

## Correctness
PASS. The bin integral is evaluated exactly, the origin average is an exact tiling identity, and the aligned-grid formula reduces to finite trigonometric sums after dividing by \(\gcd(k,N)\). The resulting zero criterion and the \(N=2k\) phase law are algebraic consequences. Finite numerical checks were used only as stress tests, not as proof.

## Originality
PASS. The closest source is the 2026 oscillatory PIT calibration example, which gives an approximate phase-free sinc attenuation and reports about \(64\%\) retention at \(N=2k\). The inspected full manuscript does not state the origin-phase dependence, the parity/gcd closed form, the exact blindness condition \(N\mid2k\), or the interpretation of the sinc curve as the randomized-origin mean. Broader ECE-binning literature checked does not imply these exact identities. The principal residual risk is an equivalent elementary aliasing calculation in older signal-processing or quadrature terminology.

## Value
PASS. The finding is mathematically small but structurally consequential for the motivating benchmark: deterministic bin alignment can change the critical-resolution population discrepancy from roughly \(64\%\) to exactly zero, while a half-bin phase shift recovers \(100\%\). The exact phase-average identity explains the prior curve and isolates a reproducible failure mode of fixed-origin binning.

## Closest literature and limitations
The closest literature is A. Kipnis, arXiv:2607.08378v1, together with the associated 2026 workshop manuscript. The result does not claim finite-sample power, minimax optimality, or a multi-frequency classification. Equivalent prior work under general aliasing terminology remains possible.

Same-model review: passed. Independent audit: not yet performed.
