# Scientific review

## Correctness — PASS

The exact BDF2–Maruyama update with its reused neighboring Gaussian increment is confirmed against Andersson–Kruse's displayed scheme. For every \(z>0\), both characteristic roots have modulus below one, ensuring a unique stationary Gaussian law. An explicitly specified three-state Lyapunov equation gives the stationary variance and lag-one covariance. The recurrence and a discriminant/phase analysis prove the sharp sign transition at \(z=1/2\), with a separate double-root boundary check. Exact symbolic algebra and 3335 rational recurrence checks confirm the identities; finite calculations are not substitutes for the infinite-lag proof.

## Originality — PASS, qualified

The source papers establish BDF2–Maruyama and finite-time stability/convergence rather than the stated stationary OU autocovariance profile. A published deterministic BDF2 sign-loss result already contains the familiar \(z=1/2\) characteristic-root transition; the new claim is not that root calculation alone. The stationary stochastic covariance, exact bias relative to OU/BEM, all-lag classification, and sharp lag-one threshold have not been identified together in inspected primary materials or targeted published-result searches. The 2006 general stochastic multistep paper was only accessible as an abstract/metadata; a specialized exact stationary calculation therein or elsewhere cannot be ruled out independently.

## Value — PASS

For simulation of equilibrium time-series data, a one-time invariant variance can look accurate while physically important lag correlations are qualitatively wrong. The theorem supplies a sharp step-size criterion for preserving positive correlations at all stationary sampling lags and an exact example showing that even positive lag-one correlation does not safeguard later lags. This is a meaningful long-time statistical diagnostic, distinct from the established mean-square stability of BDF2.

## Closest literature and limitations

Kruse–Weiske (2021) and Andersson–Kruse (2015/2017) define the scheme and prove convergence properties. Buckwar–Winkler (2006) is a related, partially accessible precursor. Liu–Mao–Wu (2022/2023) studies BEM invariant measures, not BDF2's OU covariance profile. A published deterministic BDF2 result covers step-root sign loss under deterministic initialization, not the stochastic invariant covariance computations. The claim is limited to scalar additive OU forcing at stationary equilibrium and does not establish universality over SDEs.

Self-review: passed. Independent audit: not yet performed.
