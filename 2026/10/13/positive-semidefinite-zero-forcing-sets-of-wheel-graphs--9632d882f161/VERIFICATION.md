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

The proof is analytic and infinite; the computation below is a finite corroboration, not a substitute for the proof.

The standalone `artifacts/verify.py` independently constructs each wheel \(W_n\), simulates the positive semidefinite component color-change rule from every initial subset, and compares the result with the two-case structural criterion. It also compares the complete coefficient vector with the closed polynomial, verifies the cyclic \(111\)-avoidance transfer-matrix trace, and checks the minimum value and basis count.

Tested range: \(5\le n\le14\).

Exact replay output:

`VERIFY_OK n_range=5..14 subset_checks=32736 criterion_checks=32736 coefficient_checks=200 basis_checks=20 max_order=14`

The finite range checks all \(32736\) initial subsets across those wheels. The theorem for arbitrary \(n\ge5\) rests on the component-structure proof in `RESULT.md`.
