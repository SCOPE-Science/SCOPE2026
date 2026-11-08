---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Direct cycle-marking yields E[C_r K]=E[C_r](1+mu_{n-r}); deleting a cycle gives E C_r = theta*n!*A_{n-r}/(r*(n-r)!*A_n). The weighted derangement recurrence A_m=(m-1)(A_{m-1}+theta A_{m-2}), with B_m=theta A_m prime, gives mu_2=mu_3=1 and consecutive increments delta_m=(1-p_m)(1-delta_{m-1}); delta_m in (0,1), delta_m+delta_{m-1}<1. Thus 1+mu_{n-r}-mu_n decreases with admissible r and has positive r=2 and negative r=n endpoints for n>=4. Forbidden n-1 cycle has count zero. From F(z)=exp(-theta z)(1-z)^(-theta), log coefficient differentiation at fixed theta gives mu_m=theta log(m)-theta-theta psi(theta)+O(1/m); Riemann scale r=floor(alpha n), alpha in (0,1), yields n Cov(C_r,K)->theta/alpha*(1-alpha)^(theta-1)*(1+theta log(1-alpha)), unique zero at alpha=1-exp(-1/theta). Asymptotic coefficient use is locally uniform in theta. Verified separate direct permutation enumeration and exact rational checks for n<=7; this is corroboration, not infinite proof.

## originality

PASS

Earlier Ewens-derangement factorial moments already determine each finite covariance in principle. The independently assessed claim is not the raw covariance formula: it is the simultaneous all-r single-sign crossing, the theta-dependent macroscopic location and signed profile, which require residual mean monotonicity and coefficient asymptotics beyond simply identifying prior moment identities. Resultary published search found permutation inversion covariance, fixed-point-descent and analogous set-partition sign switch, but no covering Ewens-derangement theorem. Best knowledge; equivalent sign derivation might be implicit in prior literature.

## value

PASS

The cycle-count/cycle-length dependence structure of a natural constrained Ewens measure is mathematically motivated, and its all-size monotone sign classification plus full macroscopic phase profile are reusable structural information; not an arbitrary finite slice or re-tabulation of known moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
