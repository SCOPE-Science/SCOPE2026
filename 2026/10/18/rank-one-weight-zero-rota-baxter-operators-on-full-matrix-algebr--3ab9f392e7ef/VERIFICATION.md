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

# Verification record

The accompanying `verify.py` runs without third-party dependencies. Execute `python verify.py`. It exhaustively ranges over all nonzero ordered pairs of matrices, tests the defining polynomial identity against all ordered matrix-unit pairs, compares with the two normal-form predicates, normalizes the resulting operators by their full action on the basis, and checks the exact counts.

Verified configurations: \(M_2(\mathbb F_2)\), \(M_2(\mathbb F_3)\), and \(M_3(\mathbb F_2)\), with counts respectively \(15\), \(56\), \(651\). The checker additionally tests that each accepted map has linear composition square zero. The input-pair search is exhaustive for these cases because the defining identity is bilinear in both arguments.

This is finite computational corroboration, not a proof for all dimensions or all prime powers. The mathematical proof handles those infinite families separately. No independent audit or external verification has been carried out.
