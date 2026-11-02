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

# Verification and reproducibility

Run `python verify.py` using Python 3 and SymPy. The exact verifier reconstructs the endpoint coefficients, performs 234 symbolic and rational assertions, and prints the diagonal Sturm variation pairs for every dimension from two through fourteen.

The proof uses an infinite-family geometric-series identity, an exact integer-polynomial numerator with positive denominator, and a symbolic Sturm count for a finite list of univariate integer polynomials. The cases of fourteen through sixteen states at timestep six use exact rationals; all higher dimensions are covered by an explicit decreasing upper bound. No finite-precision root finder is used to certify root counts or exact set endpoints.

Additional rational matrix inversions are evaluated directly for dimensions two, three, four, five and fourteen. These tests cross-check the separately derived kernel formula, with no external files or data. Approximate isolating-root values are provided only for readability; exact intervals and defining polynomials are in `RESULT.md`.

The result is self-reviewed but has no independent mathematical audit. Alternative historical terminology for extrapolation positivity may conceal overlapping earlier results. The analysis applies only to the precise unit-rate cyclic generator and unmodified second-order Richardson combination stated in the finding.
