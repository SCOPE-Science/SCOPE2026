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

The proof in `RESULT.md` establishes the finite comparison and sharp limiting constant for all stated alphabets and languages. The checker is optional corroboration, not an infinite proof.

Run `python3 check.py` using Python 3 with no third-party packages; compare its stdout to `CHECK_OUTPUT.txt`. The program builds useful residual automata from actual finite word sets, computes the exact layer profile, takes breadth-first balls from every residual, and tests the exact integer inequality. The binary witnesses were checked at 24 parameter pairs; the additional 1,000 finite languages are deterministic pseudorandom tests with seed 20261017. Larger languages and all untested parameter values are covered by the mathematical proof rather than by these experiments.

Independent scientific validation: not performed.
