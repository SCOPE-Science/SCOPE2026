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

# Verification evidence and scope

Run `python3 check_duality.py` from the directory containing this document and the checker; it requires only the Python standard library. The program (i) enumerates all sampled nonempty neighbourhood families and their generated upward closures on one to four worlds, (ii) separately enumerates every upward-closed family and evaluates the exact fiber-square sum, (iii) for one to three worlds checks the two zero-instance semantic clauses at every complementary pair of scopes for every ordered pair of families, and (iv) evaluates the optional-empty-neighbourhood identity in exact rational arithmetic.

Expected final output: `FINITE_ZERO_INSTANCE_COUPLING_OK`.

The ordered-pair collision counts are `2, 14, 1438, 35572286` for sizes one through four. The direct semantic comparisons cover all family pairs for sizes at most three; the size-four comparison uses the two distinct exact counting routes rather than all approximately one billion ordered family pairs. The all-size probability bounds and their limiting exponent, and the empty-neighbourhood limit, are established by the proof in `RESULT.md`, not finite experimental extrapolation.

This material documents finite computational corroboration and the mathematical argument only. No independent audit or external certification is asserted.
