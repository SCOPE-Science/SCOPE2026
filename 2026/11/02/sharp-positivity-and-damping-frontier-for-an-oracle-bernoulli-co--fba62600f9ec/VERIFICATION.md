---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-08.md",
      "INDEPENDENT_AUDIT_2026-11-08.json"
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

The four actual rank-one products sum to I_2, all scalar covariance denominators are positive for 0<eta<1, and Bernoulli independence gives oracle coefficients B_diag=(K+5)/6 and B_off=(K+1)/2. Substitution yields tildeY=I+(K-1)C, with C bounded below in Loewner order by (1/6-1/(4eta))I; the two positive-semidefinite summands of the scaled difference are explicit and the sample (1,1,0,1) attains equality. Thus the exact all-outcome positive-definiteness/semidefiniteness boundaries are K< / <=1+12eta/(3-2eta), and the optimal common semidefinite shift is max(0,(K-1)(1/(4eta)-1/6)-1). The raw sketch is positive definite on this counterevent. Exact Bernoulli covariance sums give raw Frobenius MSE ((1-eta)/eta)(K^2+3)/4 versus corrected MSE ((1-eta)/eta)(K-1)^2/6. The independently constructed audit_checks.py enumerated each of 16 outcomes at several rational eta,K values; finite enumerations corroborate, while the Loewner decomposition proves every real admissible parameter.

## originality

PASS

The underlying Bernoulli estimator, oracle entrywise control variates, and qualitative warning of loss of SPD are known from Polydorides et al.; the final claim is limited to an explicit balanced Parseval-frame all-outcome spectral boundary, attained negative event, minimal damping and MSE formula. Resultary analogous Gram-controller and Bernoulli-moment records address different operators. No examined statement directly implies the exact two-parameter frontier, but restricted access to the 2026 original leaves a specific priority risk.

## value

PASS

A complete attained all-sample spectral reliability frontier, minimal scalar damping, and an exact MSE/positivity tradeoff are genuinely motivated by the entrywise control-variate Gram sketch introduced in finite-element computation. This is a narrow but nontrivial exact structural obstruction: lowering MSE can destroy SPD even where the raw sampled Gram is SPD. A researcher implementing that specific method can use these exact cutoffs as test/worst-case models. It does not pretend to solve arbitrary frames or fitted coefficients.

The dated certificate retains the supplied scientific assessment, sources and limitations.
