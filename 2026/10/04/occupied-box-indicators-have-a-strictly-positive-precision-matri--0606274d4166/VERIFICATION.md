---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

Inclusion-exclusion gives the stated strict negative off-diagonal covariance. For one draw, \(C=\operatorname{diag}(p)-pp^{\mathsf T}\) has kernel exactly the constants. For \(n\ge2\), a zero covariance quadratic form makes \(\sum_i a_iI_i\) constant; singleton occupancy patterns force all coefficients equal, and positive-probability two-box patterns force that common value to zero. Thus \(C\succ0\). Diagonal normalization gives a symmetric positive-definite Z-matrix \(A=I-B\) with \(B\) strictly positive off diagonal and \(\rho(B)<1\); the Neumann series makes \(C^{-1}\) strictly positive. The exact-rational verifier checks formulas, principal minors, inverses, and direct small sample-space reconstructions.

## originality

PASS

The checked occupancy literature gives strong negative dependence and the pairwise covariance cross-term; generic Stieltjes-matrix theory makes inverse nonnegativity standard once positive definiteness is known. No source located gives the occupancy-specific rank transition together with strict inverse positivity and the resulting full-order partial-correlation sign.

## value

PASS

The exact rank transition and strict precision sign refine standard pairwise negative dependence for a canonical multinomial statistic and yield a clear structural statement about all full-order linear partial correlations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
