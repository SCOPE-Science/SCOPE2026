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

# Reproducible scientific checks

Execute `python3 check_negative.py` from the directory containing this file. The execution writes standard output, which is supplied as `check_output.txt`. The code uses exact `fractions.Fraction` arithmetic; it compares direct enumeration of every word through bounded lengths with Bellman extremal recurrences, counts of extremal ties, and parity-run necessary conditions. It also tests run-counting over small alphabets and exactly enumerates the ternary witness's 27 length-three words.

The reported checked counts come from the actual execution, not a projected estimate. In particular, the finite tests do **not** prove stabilization at arbitrary lengths, regularity of the infinite winning language, or the asymptotic polynomial upper bound. Those follow from the symbolic proof in `RESULT.md`. The sign hypothesis, tie cases, arbitrary initial distribution, and the possible determinant \(-1\) are handled analytically by the proof without relying on numeric convergence.

No independent audit or external validation has been performed.
