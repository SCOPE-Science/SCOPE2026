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

The packaged `VERIFY.py` is a standalone Python program using the standard library and NumPy. Execute it with `python VERIFY.py`. Its successful run prints `VERIFIED 148 independent checks: Gram spectra, rational traces, asymptotic refinements`.

It builds finite Dirichlet-weighted Bernstein Gram matrices from gamma integrals, computes the eigenvalues numerically, and compares them to the closed-form polynomial-degree spectrum for dimensions two through four and several unequal Dirichlet shape vectors. It independently computes the power-one and power-two triangle traces with exact rational arithmetic and tests the asymptotic formulas for multiple real powers and triangle and higher-dimensional weights.

The checker is not an exhaustive certificate for arbitrary dimension, power, or shape. In particular, testing finitely many degrees cannot establish the asymptotic expansion. The proof in `RESULT.md` supplies the analytic Gaussian tail control, local product expansion, and boundary-correct Euler–Maclaurin calculation needed for the infinite statement. The novelty assessment is based on compared published statements and remains subject to historical full-text access limitations. No independent audit has been performed.
