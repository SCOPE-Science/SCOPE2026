---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The Hermitian Kraus operators satisfy completeness and make the averaged channel unital. Equal operators for opposite jumps give conditional mean zero, so the signed increments are pairwise uncorrelated for any initial state. On sigma_x+sigma_z the channel eigenvalue is 3/4; on sigma_x-sigma_z it is theta=1/4+1/(2sqrt(2)). The second-moment operator is M=(5/4)I+sigma_x+sigma_z/4, so the weighted first step from I/2 produces M/2; its two Pauli coefficients in the displayed eigenbasis are 5/16 and 3/16. Evaluating Tr[M Phi^(ell-1)(M/2)] and subtracting (5/4)^2 verifies both positive covariance coefficients, including ell=1. Var(S_1)=17/4-(5/4)^2=43/16, and the exact lag convolution gives G_n including n=1 and the stated limiting inflation. For arbitrary Bloch initialization the signed variance sums Tr[M Phi^j(rho_0)] and its linear Bloch correction has the stated Euclidean norm, attained at opposite pure states. Stationary initialization is needed for the squared-step covariance, not for the signed martingale or finite-time displacement result. An independent matrix/history calculation through n=4 (617 nonzero paths at n=4) gave stationary E Q_4=5 and Var(Q_4)=21.2315594555, and Var(X_4)=5.1504334921 for Bloch coordinates (.2,.3,-.4). The supplied script was inspected, not executed; no inference of all-time validity rests on those finite checks.

## originality

PASS

The fixed instrument, I/2 stationarity, nonindependence and the displacement diffusion coefficient are prior. The supported distinct claims are the exact squared-step two-mode profile with its finite and limiting variance consequences, and the sharp finite-time arbitrary-state displacement interval.

## value

PASS

An established noncommuting instrument has an exact observable-dependent memory profile: uncorrelated signed displacements coexist with two positive persistent modes of squared steps and approximately 3.85 times the independent-reference variance per step. The coefficients and finite-time envelope provide a quantitative benchmark for trajectory fluctuation calculations, beyond a dependence witness or the signed diffusion coefficient.

The dated certificate retains the supplied scientific assessment, sources and limitations.
