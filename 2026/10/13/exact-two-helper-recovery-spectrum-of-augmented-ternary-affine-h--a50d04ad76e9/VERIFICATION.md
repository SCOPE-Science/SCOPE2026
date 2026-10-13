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

# Reproduction

Extract `verify.py` from the same package as `RESULT.md` and run `python3 verify.py` using a standard Python 3 interpreter. Expected last line: `VERIFY_OK`.

The script reconstructs the generator matrix from the explicit columns in the theorem; it does not depend on an external code table or reference implementation. It enumerates **all** unordered helper pairs and all projective points they span in \(\mathbb F_3\). The output includes the per-position mismatches and incident totals for \(n=3,4,5\); expected total incidences are \(234,1329,8814\), giving \(78,443,2938\) weight-three dual supports. The independent reasoning in `RESULT.md` proves the formula for every integer \(n\ge3\). No finite run certifies the infinite parameter range, and no disjoint-availability count has been tested or claimed.
