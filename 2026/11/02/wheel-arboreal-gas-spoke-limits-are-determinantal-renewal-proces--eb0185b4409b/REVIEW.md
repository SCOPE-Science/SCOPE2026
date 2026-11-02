# Scientific review: wheel arboreal-gas spoke laws

## Correctness (C): PASS

The gap decomposition gives the forced spoke weights as products of the coefficients of \(A/(1-A)\); the cyclic logarithmic sum supplies the partition function. The fixed-gap limit yields explicit inclusion moments, whose determinants identify a positive contraction Toeplitz kernel; a separate renewal law has the same moments. The all-size strict negative pair correlation follows from a positive AM-GM certificate. Exact rational enumeration and determinant checks in `check_wheel.py` passed 822 and 1143 assertions respectively. The analytic proof, not bounded tests, supports the infinite conclusions.

## Originality (O): PASS, qualified

The 2019 arboreal-gas model paper, the 2010 series-parallel Rayleigh result and the 2026 general high-fugacity study do not provide this all-order spoke-process characterization. The directly related wheel paper by Bado already proves \(x=1\) pairwise negativity for every edge type and the \(x=1\) forest count, and those are credited. Its accessible abstract does not claim the all-positive-fugacity renewal/DPP law, but its full text could not be inspected. This creates a material residual historical-priority risk, especially for the finite generating identity. The primary claimed contribution is the explicit local stationary process identification and all-order inclusion law, not known unit-fugacity pairs.

## Value (V): PASS

This is an all-size, all-positive-fugacity distributional description of a natural marginal of the arboreal gas on a 3-connected non-series-parallel graph family. The joint identities identify renewal gaps, the entire limiting determinantal correlation kernel and the geometric covariance scale. The fact is structural rather than a small numerical gain or repackaging of a two-point inequality.

## Scope and outstanding limitations

Only rim-to-hub spokes are characterized; there is no mixed-edge Rayleigh, all-edge negative-association or general-graph theorem. The finite process is not claimed to be determinantal. No independent mathematical audit has been carried out and full-text access to the Bado article remains an originality risk.

Self-review: passed. Independent audit: not yet performed.
