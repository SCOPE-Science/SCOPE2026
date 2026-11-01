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

# Reproducible verification

The attached `verify.py` runs with Python 3, NumPy, and the standard-library `fractions` module. Run `python3 verify.py` in the directory containing that file. No remote data, certificates, or prior-run files are required.

The performed run succeeded with the message `VERIFICATION PASSED`. Exact rational arithmetic checked the sum of squared cone-generator norms, their summed vector norm, the general relative linear coefficient, and the leading constant for every integer dimension from 2 through 16 (only dimensions at least four are claimed new). A separate polynomial Dirichlet-moment expansion checked \(\mathbb E Q=5/16\), \(\mathbb E Q^2=533/5280\), and the \(34/15\) second relative correction for dimension four. A formal Catalan-root convolution independently checked the Lagrange inversion coefficients through five correction orders. Fixed-seed quadrature of the exact small cone root confirmed approach to the predicted first relative coefficients in dimensions 4, 5, and 7 at three small deficits each.

These computations do not establish analytic localization, uniqueness of near-diameter neighborhoods, uniform convergence, or correctness in all dimensions. Those obligations are discharged by the proof in `RESULT.md` (especially Steps 1–4). The finite quadrature checks are indicative, not a proof of the infinite expansion or of mathematical priority. The result has had self-review only, with no independent audit.
