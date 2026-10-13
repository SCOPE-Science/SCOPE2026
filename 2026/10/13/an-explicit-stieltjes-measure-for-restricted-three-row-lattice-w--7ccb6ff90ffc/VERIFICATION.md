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

# Verification of the explicit moment measure

The symbolic checker `artifacts/verify_moments.py` confirms the algebraic jump calculation, the substitution and Jacobian, and the critical positivity derivative and minimum using exact rational arithmetic. It checks numerical moments \(0\leq k\leq14\) by high-precision quadrature, reproducing the binomial formula to absolute error less than \(10^{-38}\), and computes positive leading and once-shifted Hankel determinants of sizes one through six. Its saved output is `artifacts/verification_output.txt`.

Run `python3 -m pip install -r artifacts/requirements.txt` followed by `python3 artifacts/verify_moments.py`. The script uses Python 3, SymPy, and mpmath; dependencies are explicitly listed in `artifacts/requirements.txt`.

The proof in `RESULT.md` is mathematical, using the exact analytic parametrization, endpoint contour bounds, and a generalized Vandermonde determinant identity. Computed moments and finite determinants do not certify the infinite claim independently. The other sequence \(Q\) in the motivating conjecture is unproved by this package.
