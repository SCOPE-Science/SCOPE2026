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

Finite checks were reproduced by running `python verify.py` with NumPy and SciPy. The program generated independent chi-square streams across candidate residual ranks and compared stopping frequencies against the finite product law, checked orthogonality and the Frobenius projector invariant on small matrices by QR, evaluated the finite chi-square survival products, and compared those products with Gumbel predictions at growing dimensions. **784 assertions/comparisons passed** in the recorded run.

The proof, not simulation, establishes the conditional independence, moderate deviations, first-success hazard asymptotic, and limiting distribution. The finite CDF can converge slowly to the asymptotic Gumbel law; the program prints differences rather than imposing unsupported small finite-size tolerances. No independent audit or infinite formal certification has been performed.
