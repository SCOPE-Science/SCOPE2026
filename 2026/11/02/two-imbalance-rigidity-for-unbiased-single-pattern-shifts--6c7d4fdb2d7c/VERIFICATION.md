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

The theorem is proved from the weighted border generating function by differentiation at the simple positive growth root, together with the monic constant-unit entropy polynomial. The exact two-monomial contradiction is algebraic and applies at arbitrary word lengths. The sign formula and examples have been cross-checked by an independently constructed prefix automaton.

Reproduction: run `python3 verify.py` from the extracted artifact directory; this script uses only the Python standard library. It enumerates all length-four to length-eight binary forbidden patterns having at least two copies of each letter, compares two numerical formulas, and prints three longer examples. `verification_output.txt` contains the actual recorded output. Small numerical differences are floating-point tolerances, not formal certificates.

Limits: testing \(426\) patterns does not prove a theorem for all lengths; the proof is in `RESULT.md`. The full conjecture involving three or more unbalanced borders and the separate stopping-time expectation are not established. No independently conducted mathematical audit has been performed.
