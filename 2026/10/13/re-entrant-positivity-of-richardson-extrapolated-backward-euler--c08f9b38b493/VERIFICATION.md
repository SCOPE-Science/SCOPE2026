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

`verify.py` uses only the Python standard library and exact rational arithmetic. It reconstructs the homogeneous five-state pure-birth generator, forms the Richardson combination from exact backward-Euler inverses for rational steps, and checks row sums and signs. At \(h=1/4\), it checks the exact negative entry \(-7799/36905625\) in the first-row absorbing position; at \(h=1\), it checks entrywise nonnegativity. It also verifies the exact rational signs \(p(3959/10000)<0<p(99/250)\), which isolate the unique positive root because the proof establishes uniqueness by Descartes' rule.

The checker does not establish the universal sign theorem by enumeration. That theorem rests on the exact coefficient and tail formulas in `RESULT.md`; the replay is an independent arithmetic check of the critical witness and root bracket.
