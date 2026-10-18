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

# Verification

The included `check_retracts.py` uses the standard Python library and can be executed with `python3 check_retracts.py` from the extracted file directory. It directly verifies symmetric-bilinear brackets, total isotropy, rank-generating polynomials, and composition-idempotence. It enumerates all maps and all idempotent endomorphisms for two-dimensional forms over \(\mathbb F_3\) and \(\mathbb F_5\), including split and anisotropic types, and one three-dimensional form over \(\mathbb F_3\). Further tests enumerate totally isotropic subspaces for ten prime-field form configurations, and directly construct finite orthogonal similitude groups and their projection-conjugacy orbits in three configurations. Observed completion messages include `ALL_QUADRATIC_LEIBNIZ_RETRACTION_CHECKS_PASSED` and `ALL_RANK_ONE_ORBIT_CHECKS_PASSED`.

These computations check finite instances only. The proof in RESULT.md is the evidence for the quantified statements over all odd prime powers and dimensions. The standard classification of nondegenerate symmetric forms over odd finite fields and Witt extension are cited mathematical inputs. No independent audit has been performed.
