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

# Reproduction and limits

Run `python3 verify.py` using Python 3 and only the standard library. The expected success marker is `RS_UNIFORM_UNIVERSALITY_PASS transfers=23 dyadic=16 brute=19x14 factors=22890`.

The checker constructs the weighted automaton for counting complete binary greedy arches, composes four substitution-block transfers across 23 recursion levels, tests the closed transfer formula against all three entering states, and confirms the exact dyadic-prefix index independently using the binary-digit definition. It directly enumerates target subsequences for short factors, then tests the uniform discrepancy and dyadic interval partition on 22,890 additional factors. These are finite reproducibility checks. The proof of the infinite theorem consists of the four-state substitution, the transfer-table induction, and the dyadic decomposition argument in `RESULT.md`.

No independent mathematical audit or external certification is claimed.
