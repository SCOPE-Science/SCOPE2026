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

# Reproducibility and limits

`checker.py` can be executed with Python 3, SymPy and NumPy installed by running `python checker.py` in the directory containing the extracted files. It verifies 1,247 exact rational/symbolic, large-\(n\), and independent finite-matrix assertions over multiple positive weight parameters and monomial exponent combinations. The script has no external-data dependency.

The actual proof of the infinite singular limits is the exact monomial diagonal formula, its rational Gamma-moment expansion, and the one-diagonal singular-value ordering argument in `RESULT.md`. A finite checker is not proof of an asymptotic theorem. In particular, the numerical comparisons do not certify all real parameters or all exponent tuples. The precise critical Schatten endpoints and Dixmier traces are proved analytically.

The finite-rank classification is not independently novel; it is included to make the trichotomy exhaustive. The priority comparison is limited to the identified material and may miss equivalent historical symbolic-calculus results. Independent auditing has not been performed.
