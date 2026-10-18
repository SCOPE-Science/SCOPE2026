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

# Computational and deductive verification

The supplied standalone `verify.py` uses only the Python standard library. It compares direct Demazure multiplication of parabolic-longest elements with the theorem’s support-component criterion in finite types A2–A6, B3–B4 and D4–D5; it also checks graph weights against the rank recurrence. It enumerates every labeled subcubic tree with 2–6 vertices (1,310 labeled trees) and selected larger branched examples and compares the four-state assignment and component-weight methods. All specified tests passed and the program printed `VERIFY_OK_COXETER_TREE`.

These finite enumerations cannot prove the infinite-rank recurrence or the all-Coxeter-type assertion. The proof rests instead on the Coxeter-element/Bruhat contradiction, idempotent absorption, exact component weights, and the branch-addition identities in RESULT.md. A direct independent mathematical audit is not included. The type-A sequence is already known and is not claimed to be new numerically.

Reproduce the checks by running `python3 verify.py` with the program and `RESULT.md` in the same directory.
