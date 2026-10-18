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

# Finite verification and logical boundary

Run `python3 verify.py` with a standard Python 3 interpreter in the directory containing this file and `verify.py`. The program uses only the Python standard library and prints `VERIFY_OK` on success. It recomputes the nine-divisor signed-sum distribution from scratch, checks the complete set of zero-block solutions and the total \(12\), checks the fourteen subset-sum inequalities, constructs the two-level interval, and verifies full odd-imbalance coverage by exact subset-sum bitsets for \(a=1,2\).

Only the nine-weight finite enumeration and the finite initial inequalities enter the proof as computer-checkable certificates; they are also spelled out in the proof. Full finite searches for \(a=1,2\) provide corroboration but cannot establish the theorem for all \(a\). The unbounded multiplicity factor is proved by a disjoint-level injection, not inferred from numerical output. Exact overall counts and the optimal growth constant remain unknown here.
