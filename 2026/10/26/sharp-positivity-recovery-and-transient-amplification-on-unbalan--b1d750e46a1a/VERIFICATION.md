---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Computational cross-check and proof boundary

The original reproduction program `verify_bipartite.py` is unchanged. Run it with Python 3 standard library. The original recorded execution reported `ALL CHECKS PASSED: 41930 assertions`. The program tests rational spectral projectors and compares independently computed truncated matrix exponentials on 25 small ordered pairs of part sizes from two through six. It samples the signed within-part entries, row norms, larger-part dominance and temporal peaks. Larger-contrast scale diagnostics remain in the script as context, not as claims unique to the narrowed result.

This finite computation is not a proof of all-time dominance, strictness, or uniqueness of the peak. The proof in `RESULT.md` uses the known recovery ordering and a sign-change argument for the difference of signed within-part row masses.
