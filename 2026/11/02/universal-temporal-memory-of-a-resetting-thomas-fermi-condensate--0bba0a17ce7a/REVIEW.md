# Scientific assessment of the edge temporal-memory theorem

## Correctness — PASS

The theorem fixes every quantifier \(r,\omega,x_0>0\), stationary rate-\(r\) Poisson resetting, and the unique global positive ODE solution. The exact covariance is reconstructed by conditioning on whether there was any reset during the observation interval. Strictness follows from independent-copy covariance positivity for strictly increasing functions; the integrability and long-lag limit use the bounded positive derivative of the scaling function. The fast-rate coefficients follow from the ODE's fourth-order Taylor coefficient and factorial-moment identities, with exponential-tail control, and the slow-rate limit follows by dominated convergence. The standalone verifier passed exact polynomial/moment checks and numerical ODE integration. The proof excludes quantum finite-particle claims.

## Originality — PASS (qualified)

The original 2026 Thomas–Fermi resetting paper [1] calculates stationary one-time edge distributions but not a lagged edge covariance or the two correlation-time limits. General Poisson resetting autocorrelation conditioning is already present in the 2021 paper [2]; it is acknowledged, not claimed as original. The assessed claim instead gives all-rate strict physical-edge memory enhancement, \(7/5\) versus \(1\) asymptotic memory, and the first dimensionless correction \(-88/25\). A search across relevant indexed mathematical research statements and relevant mathematical statements did not identify an equivalent or dominating result. This does not establish exhaustive priority: a broader nonlinear-age covariance theorem could subsume the comparison, and a different derivation of the leading quadratic-growth memory enhancement could exist.

## Value — PASS

The two-time memory of the moving condensate support is a natural diagnostic not obtained from its one-time edge law. Reset events are independent and exponentially timed, yet the finite interval covariance is strictly above the naive Poisson survival envelope for every reset rate. The fast-reset excess is a substantial \(40\%\) in the integrated correlation time and has a parameter-dependent correction that can differentiate finite-rate behavior. The contrasting slow-reset limit supplies a useful physical crossover benchmark, while strict inequalities expose a structural role for convex expansion.

## Closest work and limits

[1] Mesquita et al., arXiv:2609.37110v1 (September 29, 2026), §§2–4 and equations (37), (61)–(62): expansion law and one-time stationary edge distribution; not the presented temporal-memory classification.

[2] Stojkoski et al., arXiv:2107.11686 (July 24, 2021), §§2–3 and equation (11): established Poisson no-reset decomposition and two-time diffusion correlations; the general method is prior art, but the nonlinear condensate support's all-rate bound and asymptotic coefficients are not given there.

Residual risks: generic resetting processes may already imply some conditional-covariance pieces; broad deterministic-renewal covariance classifications were not exhaustively inspected. Finite-particle quantum correlations and noninstantaneous-reset protocols are outside scope.

Self-review: passed. Independent audit: not yet performed.
