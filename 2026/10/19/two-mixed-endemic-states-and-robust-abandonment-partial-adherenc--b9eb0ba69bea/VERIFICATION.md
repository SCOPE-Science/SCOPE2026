---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

# Verification

The certificate for the saddle-to-sink connections and local basin separation is analytic in `RESULT.md`: uniform rational estimates make the tube wall strictly inward pointing, then scalar speed bounds and a compact slice argument identify both unstable branches and their limits. No simulation of trajectories is used to certify a connection.

With Python 3.10+ and SymPy, the unchanged `check.py` reproduces the equilibrium reduction, the two rational root brackets, the Jacobian coefficient identities and the strict Routh bounds. The original recorded run reports `PASS: algebraic reduction, two rational root brackets, derivative signs, exact Jacobian identities, Routh bounds`. This program does not check the tube or the geometric connection argument.
