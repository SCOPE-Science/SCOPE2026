# Mathematical review

## Correctness — PASS

The proof normalizes the circle Fourier coefficients, proves the component threshold through endpoint power sums, classifies the equal-component solutions through self-inversive endpoint polynomials, and fully computes the real Jacobian spectrum on the area-fixed rotation quotient by pairing Fourier frequencies. The Nyquist sector is treated separately when the number of arcs is even. All singular values are positive for occupancies strictly between zero and one; the inverse-function and local sharpness claims follow. The standalone checker passed 144 deterministic singular-spectrum and finite-difference tests. Numerical checks are not the basis for the universal proof.

## Originality — PASS, with historical-priority limitation

Courtney's full 2010 article gives a recovery theorem for at most \(k\) arcs using the Fourier moments through order \(k\), and a Blaschke-product endpoint algorithm. The geometric minimal-component assertion is close in spirit and its simplest cases should not be treated as the decisive novelty. Huang's 2024 paper recovers arc measures through infinite Fourier-series limits; Batenkov and Yomdin's 2011/2013 Prony work provides general inverse-local-stability theory without the specific fixed-occupancy, real-conjugate-pair spectrum. Neither inspected text reports the exact, multiplicity-resolved real singular spectrum of the first \(k-1\) moments on the fixed-area rotation-quotient at the equal-arc design. Targeted literature and claim-level comparisons found no dominating statement. An uninspected Prony or harmonic-analysis source could still establish the same formula.

## Mathematical value — PASS

Balanced restriction of consecutive Fourier modes and stable reconstruction of a binary arc mask are natural coupled sampling-design problems. The exact threshold at \(k\) components, rigidity of the optimizer, and dimension-free inverse condition number together identify an interpretable design: half occupancy is uniquely isotropic in endpoint coordinates. This is an all-rank sharp local stability theorem, not an isolated computed instance.

## Limits

Only smooth small deformations with fixed area and an orthogonal rotation gauge are covered by the quantitative inverse result. No global noise amplification, large-arc-count optimizer classification, or independent review is asserted.

Self-review: passed. Independent audit: not yet performed.
