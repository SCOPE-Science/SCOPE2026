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

The theorem is verified analytically by the structural induction in `RESULT.md`. The critical semantic fact is that in a symmetric frame every successor of a nonisolated world is nonisolated. Therefore the modal operation on the two-coordinate profile is exactly \(\pi(\Box A)=(1,a_n)\).

`verify_closed_kb.py` is a bounded independent sanity check. It generates all variable-free syntax trees of size at most seven, enumerates every symmetric relation on sets of at most four worlds, evaluates formulas directly, and checks agreement with the profile recursion at every world. It also checks that all four profiles occur. Passing this finite replay supports implementation correctness but is not used to infer the general theorem.

Scientific limit: the originality review found no covering source in targeted searches, but a bibliographically identified older article about constant formulas could not be inspected in full and remains an overlap risk.
