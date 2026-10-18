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

# Exact reproducibility and limits

Use Python 3 with SymPy. Run \(\texttt{python verify.py}\) from the directory containing the script. The script uses exact rational polynomial identities (not floating-point root sampling) for the collision formula, all nontrivial \(n\)-th root classes when \(n=9,13,17\), and the arithmetic genus/delta identity.

The all-parameter proof is in RESULT.md. In particular, the strict complex modulus argument excludes multiple roots for every admissible \(n\); the no-triple argument is an exact subtraction identity; analytic coordinate normal forms handle the cusp, and coefficient extraction forces projective-group rigidity. Finite symbolic instances alone would not justify the quantified theorem. No external independent mathematical audit was performed.
