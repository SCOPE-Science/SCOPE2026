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

# Verification record

The self-contained `verify.py` runs with Python 3 standard library and requires no external packages. From the directory containing the file, run `python3 verify.py`.

It checks Kummer parameter congruences and coprimality, the explicit residue permutation, the number and sum of gaps derived from candidate Apéry representatives, the closed weight polynomial, and the conductor formula. For small cases it also evaluates the Dedekind sum by exact rational arithmetic and compares it with two-step reciprocity. It includes precise sample checks for \((q,n)=(3,4),(4,4),(5,4)\).

This is a **finite** independent arithmetic replay of the displayed formulas, not a proof for arbitrary prime powers or arbitrary even exponents. The mathematical proof for all admissible parameters is given in `RESULT.md`. The genus and Kummer ramification data used in the proof come from Ma–Wang (arXiv:2609.19546); the general gap-set theory is prior work. No independent review or external certification has been performed.
