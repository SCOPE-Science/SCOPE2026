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

Run `python3 verify_2x3x3.py` with Python 3 standard library. The finite certificate generates every nonempty matching, checks all cover relations and a complete acyclic edge-toggle matching, constructs the exact signed integral Morse boundary, and computes an explicit 35-by-35 determinant of -1 by integer arithmetic. A second matching uses a different toggle order and independently tests an exact full-rank mod-two boundary. Expected final line: `VERIFY_OK`. The code validates a *finite* combinatorial certificate; the full homotopy assertion additionally uses standard discrete-Morse and Hurewicz theorems as shown in RESULT.md. There is no external, independent scientific audit.
