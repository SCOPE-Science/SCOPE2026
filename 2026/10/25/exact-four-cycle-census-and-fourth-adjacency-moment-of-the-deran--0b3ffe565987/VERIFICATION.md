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

# Reproducible checks and limits

Run `python3 verify_formula.py` and `python3 verify_exhaustive.py` with Python 3; both use only the standard library. Compare stdout byte-for-byte with `formula_output.txt` and `exhaustive_output.txt`. The formula checker evaluates 4 through 10, and the exhaustive checker independently enumerates and classifies all graph four-cycles and fourth closed-walk traces for 4 through 7. The latter uses unordered quadruples of vertices and counts each simple four-cycle once, and it derives the fourth moment separately by summing squared two-step-walk multiplicities. The full infinite proof is combinatorial, not computation-dependent. No independent audit has been performed.
