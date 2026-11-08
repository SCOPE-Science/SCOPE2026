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
# Verification and limits

The attached `check_balanced_chain_lowner.py` uses only Python 3 standard-library integers and rational fractions. Run it with `python3 check_balanced_chain_lowner.py`. It enumerates all vertices at \(m=1,2,3,4,5,6,7,8\), covering dimensions \(2,4,6,8,10,12,14,16\). For every dimension it verifies all positive rational weights sum to one, the exact mean and full covariance equal the displayed center and ellipsoid shape divided by dimension, and the exact reciprocal-shape quadratic form is one at every vertex. It also verifies the three positive squared-semiaxis values and ratio \(2m+1\).

Observed final line: `BALANCED_CHAIN_LOEWNER_EXACT_CHECKS_PASSED`.

These finitely many checks corroborate but do not prove the claim for unbounded \(m\). The proof in `RESULT.md` supplies the general hypergeometric identity and AM–GM optimality inequality. No independent mathematical audit has been conducted, and no certification beyond the displayed proof and runnable finite checker is asserted.
