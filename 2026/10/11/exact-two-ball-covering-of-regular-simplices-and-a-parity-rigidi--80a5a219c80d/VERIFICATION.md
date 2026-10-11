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
# Reproducibility and verification

Execute `python3 verify.py` in a standard Python 3 environment; no nonstandard packages or downloaded assets are required. The checker uses the exact identity \(\|\sum_i(\lambda_i-\mu_i)v_i\|^2=(s^2/2)\sum_i(\lambda_i-\mu_i)^2\) with \(s=1\). It verifies the two midpoint-to-centroid distances, all vertices of the barycentric halfspace sections, strictly positive room for center perturbation in even dimensions, and small odd-dimensional counting identities. The deterministic output starts with `VERIFY_OK`.

Actual completed test output:

`VERIFY_OK regular simplices: rational cut-vertex tests = 16571 barycentric samples = 4650 dimensions = 3..40`

The cut-vertex verifications and all optimality deductions for arbitrary \(d\) are proved in `RESULT.md`; finite code checks and interior sampling are not proofs of infinite statements. The program does not certify uniqueness beyond the proof and does not establish literature novelty. No independent audit has been performed.
