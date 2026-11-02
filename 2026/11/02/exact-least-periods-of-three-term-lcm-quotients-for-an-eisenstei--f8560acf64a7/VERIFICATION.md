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

# Reproducible checks
Run `python3 verify.py` in a directory containing the embedded standalone program. It uses only Python's standard library. The checker compares the original product/lcm definition to the closed formula for all 9,000 pairs (odd \(m\) from 1 to 99 and \(0\le n<180\)). For five parameter values it factors the proposed least period and verifies the valuation pattern is not invariant under translation by one or by the immediate prime-power subperiod. The proof in `RESULT.md` separately establishes the sharp period for every admissible parameter and every index. Finite verification does not certify the infinite theorem or establish mathematical priority. Independent audit status: not performed.
