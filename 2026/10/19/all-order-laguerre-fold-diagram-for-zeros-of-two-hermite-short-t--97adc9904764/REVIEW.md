# Scientific review

## Correctness — PASS

The analytic proof determines the nonzero Hermite STFT prefactor, isolates the complex polynomial, and reduces every zero to a Laguerre-ratio level on one of finitely many rays. A degree-count argument plus Rolle's theorem gives exactly one simple radial stationary point between consecutive Laguerre zeros and none elsewhere. Its level sets give all zero counts, and the explicit real Jacobian with nonvanishing transverse angular derivative proves the fold and charge statements. The standalone checker independently evaluates defining integrals for degrees one through five and symbolic identities through degree twelve. These tests corroborate, rather than replace, the proof.

## Originality — PASS, qualified

Abreu (2009) gives Hermite-window polyanalytic transform machinery; Gröchenig–Jaming–Malinnikova (2018/2019), §6, provide the general Hermite-polynomial short-time Fourier formula and lower-degree zero examples; Sète–Zur (2024) address general polyanalytic polynomial zeros; a 2026 Hermite-window white-noise study supplies related cross-transform formulas and random zero statistics. The exact deterministic all-orders amplitude phase diagram and its thresholds were not found in these relevant inspected statements, nor in the compared mathematical-record matches. This is a best-knowledge literature comparison, not a claim of exhaustive historical priority. Unindexed or older special-function treatments remain a residual risk.

## Mathematical value — PASS

The amplitude parameter changes the number of isolated Gabor zeros from \(2n\) to \(2n^2\); all intermediate bifurcations are computed exactly for any positive Hermite order, including multiple coincident transitions and charge cancellation. This is a natural complete classification of phase-space nodal geometry for a distinguished signal/window pair, rather than a gratuitous narrow numeric case.

## Scientific limits

Only the two-Hermite real positive window family with signal \(h_n\) is covered. No assertion is made that all thresholds differ. Symbolic and high-precision finite tests are diagnostic; proof does not depend on extrapolation. An independent mathematical audit has not yet been carried out.

Self-review: passed. Independent audit: not yet performed.
