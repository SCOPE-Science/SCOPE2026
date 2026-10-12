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

The arbitrary-order verification is the proof in `RESULT.md`: every zero-protection obstruction and every positive-support isolation obstruction is localized at a deleted matching index, and the seven cases partition all possibilities for the two label-\(2\) counts.

The standalone program `artifacts/verify.py` tests the predicate directly from crown-graph adjacency, without using the structural classifier. It enumerates all \(3^{2n}\) labelings for \(3\le n\le6\), forms the brute-force weight distribution, evaluates the displayed closed formula independently, and compares the full coefficient maps and minimum layers.

Replay result:

`VERIFY_OK n_range=3..6 labelings=597780 valid_functions=410530 coefficient_checks=52 minimum_checks=4 max_order=12`

This computation is finite corroboration only. It does not prove the theorem for arbitrary \(n\), and no extrapolation from the finite range is used in the proof.
