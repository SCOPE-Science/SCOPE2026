# Review of the finite-band spectral endpoint theorem

## Correctness — PASS

The stated expectation identity follows from the exact covariance \(K=(2\pi/\ell)u/(1-r^2)\) and the Gaussian zero-count formula. All endpoint contributions are controlled analytically: the complement contributes its length divided by \(1-r\) to the angular mean logarithmic derivative, and each band endpoint contributes \(-\pi^{-1}\log(1/(1-r))\) before angular normalization. The resulting count coefficient \(J/(4\pi^2)\) is exact; the quantified remainder is \(O_E(1)\). The rescaled Poisson kernel and its derivatives establish the compact-uniform local density profile. The numerical checker passed 169 assertions, which are corroborative only.

## Originality — PASS, with priority uncertainty

Noda–Shirai, arXiv:2106.02860, covers trigonometric-polynomial spectral densities, whereas the present model has open spectral gaps. Shirai, arXiv:2501.02586, **already uses the identical half-circle spectral mask** in Example 2.4 but proves a fixed-direction interior-gap limit; it does not state the endpoint-moving profile or the integrated logarithm. A strictly positive spectral-jump formula has different hypotheses and cannot be specialized through a zero-valued side. Actual literature, published-finding corpus and accessible claim-overlap searches did not identify a theorem implying both new conclusions. Undiscovered or implicit earlier work remains possible.

## Value — PASS

Finite unions of spectral arcs naturally model band-limited stationary Gaussian analytic functions. The precise positive logarithmic term detects the number of band endpoints, not simply the spectral measure or bandwidth, while the local law explains how near-boundary zeros enter a spectral band. The distinction between macroscopic zero-count density and a topology-sensitive subleading coefficient has mathematical content beyond a direct substitution or numerical example.

## Scope and limitations

Arc positions are fixed and every band and gap has positive length. The argument is not uniform under endpoint collisions and does not address nonindicator weights, zero correlations, fluctuations or almost-sure counting. The 2025 related paper is treated as a genuine overlap requiring explicit comparison, not as evidence of priority for the new statements. This is a self-review, not independent verification.

Self-review: passed. Independent audit: not yet performed.
