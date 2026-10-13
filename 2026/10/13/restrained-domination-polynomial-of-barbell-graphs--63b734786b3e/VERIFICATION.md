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

The symbolic proof establishes the theorem for every integer \(n\ge3\). The finite checker is only a consistency test.

`verify.py` constructs \(B_n\) directly, enumerates all vertex subsets for \(3\le n\le8\), tests restrained domination from the definition, independently tests the structural complement criterion, and compares the resulting coefficient vector with the claimed closed formula. It also checks the unclaimed boundary \(n=2\), where the barbell is \(P_4\).

Replay command:

`python verify.py`

Expected output:

`VERIFY_OK n_range=3..8 subset_checks=87360 valid_sets=79957 coefficient_checks=72 boundary_n2=P4_checked max_order=16`

Limits: the finite enumeration reaches order \(16\) only and does not constitute an infinite proof. No external solver, certificate service, or probabilistic test is used.
