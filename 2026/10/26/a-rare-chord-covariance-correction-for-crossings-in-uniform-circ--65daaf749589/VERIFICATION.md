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

Run `python3 verify_chord_isolation.py` on the embedded standalone Python 3 verifier. The verifier enumerates all perfect matchings for each \(1\le n\le7\) with exact fractions, reconstructs crossing pairs and crossing-free chords directly, and compares the computed expectations and covariances with the independently derived finite sums. It checks 146,599 matchings in total and reports `ALL CHECKS PASSED` when successful. The theorem claims only \(n\ge2\); size one is a computational boundary check.

The symbolic conditional-matching argument in `RESULT.md` establishes the result for arbitrary \(n\ge2\). The ratio bound proves the asymptotics analytically. There is no verified upper bound for all higher mixed cumulants, and no independent validation has been performed.
