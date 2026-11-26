---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Conditional on the entire reset schedule, different particle labels have independent Gaussian noises, even at two different times. Their squared-position means are 2D times their respective ages, giving 4D² times the age autocovariance. Rescaling from rate λ to one supplies λ⁻². At unit rate the stage events are Poisson with a uniform phase; conditioning on stage j leaves a Gamma(j+1,1) backward age. This gives the frozen initial G,F moments, and the age reset eliminates the incoming F term at j=0, including k=1. Summing the conditional second moments gives Var(A)=(k+1)(k+5)/12. Independently resolving the phase system yields the exact expression C_k(t)=k exp(−t)−∑_{z^k=1,z≠1} exp((z−1)t)/(z−1)². Indeed the G-mode with eigenvector (z^(−j)) has coefficient 1/[k(z−1)] and yields the F particular vector with entries (j+1) z^(−j−1)/[k(z−1)]. At t=0 the sum of these particular vectors is (j+1)G_{j+1 mod k}(0), which agrees with F_j(0) except at j=k−1, where the excess is k. That residual evolves solely as k exp(−t) in the last coordinate. Summing the mode entries gives the displayed root-of-unity expression. Substituting the roots for k=1,…,4 recovers the four frozen formulas and their strictly positive lower bounds for every finite lag, including the borderline pair of oscillatory modes with real part −1 at k=4. For k≥5 the unique leading conjugate pair has real part cos(2π/k)−1>−1 and a nonzero coefficient. The other terms are exponentially smaller, and at successively positive and negative extrema of the leading sinusoid the sign persists on disjoint open intervals by continuity. As a bounded corroboration this expression gives C_5(4.75)≈−0.0105949462353. The frozen verify.py and its reported generator and Monte Carlo evidence were inspected, not executed; those finite tests alone cannot certify a sign threshold at all lags.

## originality

PASS

The supported contribution is the sharp integer Erlang lag-sign threshold with its explicit leading mode for the stationary age autocovariance and hence for two distinct particles' squared positions. Collective renewal resetting, age mixtures and equal-time squared-position covariance are established; no originality is assigned to them here. The closest inspected temporal same-gas result uses a linear same-particle observable, while exact age/residual covariance concerns a different pair of variables. The targeted retrieval of related recurrence-time covariance papers left specific access risks, not contrary coverage evidence.

## value

PASS

This distinguishes two physically different consequences of a common clock: shared ages force positive equal-time covariance, while sufficient clock regularity makes lagged energies anticorrelate. The exact boundary at five stages, including exclusion at all finite lags for four stages despite its oscillatory modes, is stronger than observing a negative value or computing a decay rate. The residue and decay ordering explain the mechanism and provide an exact benchmark for renewal reset models.

The dated certificate retains the supplied scientific assessment, sources and limitations.
