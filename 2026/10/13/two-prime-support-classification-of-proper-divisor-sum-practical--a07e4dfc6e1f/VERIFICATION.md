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

# Verification instructions and scope

Execute `python3 verify_s_practical.py` with Python 3 and no third-party packages. The deterministic checker recomputes \(s(d)\) by independent divisor enumeration on small inputs, checks all five complete base certificates and their two margins, verifies nine exclusion witnesses, tests the theorem on \(720\) finite parameter triples, and directly rechecks \(400\) algebraic difference identities. `verify-output.txt` contains the observed replay output.

The finite tests validate the formulas and the base cases only. All unbounded exponent ranges are established by the greedy interval lemma and the exact monotonicity inequalities in `RESULT.md`, not by extrapolation. Full text of the relevant Reuijl thesis was not available for an originality comparison. Independent assessment has not been conducted.
