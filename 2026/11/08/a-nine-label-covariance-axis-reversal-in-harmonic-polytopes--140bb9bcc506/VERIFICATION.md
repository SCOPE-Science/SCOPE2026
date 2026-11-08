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

Run `python3 artifacts/verify.py` from the package root. No third-party dependencies or network access are required.

The executed checker returned:

`HARMONIC_COVARIANCE_CHECKS_PASSED vertices=34152 profiles=299`

It enumerates full, distinct vertex lists of orders \(n=2,3,4,5\), with counts \(6,66,1200,32880\). For every order it reconstructs each \(2n\)-coordinate vertex from the two permutation rank orders and one marked right-to-left record, then compares all entries of the empirical covariance to the exact analytical formulas, with rational arithmetic. It additionally checks the exact signs and positive eigenvalues for every integer \(n\in[2,300]\) and the transition fractions at orders eight and nine.

Finite enumeration is not an infinite proof. The infinite range is proven in `RESULT.md` by conditional permutation moments and the monotonicity of \((n+11)/h_n\) from \(n=6\) onward. The independent-audit channel is unperformed.
