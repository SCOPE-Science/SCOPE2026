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

# Reproducibility and limitations

Extract `check.py` and run `python check.py` with SymPy and NumPy. It checks symbolically the factorization of the scalar second iterate, the discriminant, the two-step Jacobian characteristic polynomial, the exact Jury polynomial, its maximizing discriminant and the quartic boundary. It also verifies one irrational-coordinate but rational-parameter exact sink, compares the Schur inequalities with numerical cubic eigenvalues for 3,000 pseudorandom \((A,\Delta)\) pairs, and exercises representative boundary points. Numerical comparisons do not prove infinite parameter claims. The complete analytic deductions and hypotheses are in `RESULT.md`.

The arXiv text of Muni (2024) and the relevant period-two and stability sections of Zhou–Liu–Ren (2017) were read. Full text of the separate 2024 torus-doubling journal paper could not be examined. This access limit leaves historical-priority uncertainty without affecting the independent algebraic derivation of the stated claim. No independent mathematical audit was performed.
