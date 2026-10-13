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

# Verification of the six-compartment positive-equilibrium classification

The analytic proof is in `RESULT.md`. An independent exact-rational cross-check of the stated positive equilibrium and instability counterexample can be run with `python3 verify.py` using standard Python 3; expected output: `VERIFY_OK`.

The script evaluates the six model right-hand sides at the exact rational equilibrium, checks strict positivity and population totals, verifies the rational infection pressure, computes the next-generation spectral-radius formula and the reproduction expression printed in the referenced v3 article, and checks that the disease-free infectious Jacobian determinant is negative. It independently checks the scalar quadratic at the equilibrium pressure. All these arithmetic tests are exact (`fractions.Fraction`), with no floating-point tolerances.

The exhaustive parameter-wide conclusion—one strictly positive endemic equilibrium if and only if the **corrected** invasion ratio exceeds one—comes from the strict monotonicity and positive inverse-matrix argument, not from testing finitely many parameters. The computation does not verify global stability, biological fit, stochastic trajectories, later article versions or the originality of any mathematical claim. The external independent review has not been performed.
