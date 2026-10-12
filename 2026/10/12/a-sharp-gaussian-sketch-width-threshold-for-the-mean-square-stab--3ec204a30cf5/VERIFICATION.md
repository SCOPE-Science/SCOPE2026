---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility

Execute \(`python3 verify.py`\) with Python 3, standard library only. The checked script is the exact embedded file, not an external path. Its first check evaluates 101 positive-definite rational test inputs and their four rank-one LU residuals, confirming exact moments at exponents \(1,2,3,4,6\) with fractions. Its second check tests 360 deterministic Gaussian-sketch coordinate-swap identities at block widths \(1,2,3,5,9\). Its third check numerically integrates Beta conditional-selection laws for six diagonal parameter values at widths one and two, and checks their exact expected-square identities. It prints two lines beginning with \(`VERIFY_OK`\).

The analytical proof, including inverse chi-square finiteness for \(b>2\), establishes the universal bounds and impossibilities. Finite tests are not exhaustive, and the exact Gaussian law is proved by measure invariance, not by finite sampling.
