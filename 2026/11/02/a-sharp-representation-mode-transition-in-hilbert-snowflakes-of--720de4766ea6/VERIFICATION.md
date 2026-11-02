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
# Reproducibility and mathematical limits

The analytical proof is in `RESULT.md`. Execute `python3 check_kneser.py` using Python's standard library. The observed output was `KNESER_NEGATIVE_TYPE_CHECK_OK association_eigenvalues= 462 boundary_j2_upper= -0.525383 boundary_j3_lower= 0.041197`.

The script checks independent inclusion-sum eigenvalues for all \(3\le k\le30\) and \(1\le j\le k\), in exact integer and rational arithmetic. It also proves the strict \(k=7\) inequalities by rational bracketing of \(2^{1/100}\) and \(3^{1/100}\) using integer hundredth powers. The all-\(k\) conclusion requires the analytic mode domination proof in the theorem, not finite enumeration. Independent mathematical audit is not performed.
