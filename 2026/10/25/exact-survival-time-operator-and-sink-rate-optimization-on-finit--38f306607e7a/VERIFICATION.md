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

The proof shows the explicit Hermitian matrix solves the Lyapunov equation entrywise for all finite path lengths, with the absorber boundary and missing-neighbor boundary handled separately. All eigenvalues lie in the open left half-plane, ensuring the integral is well-defined and unique.

Run `python verify.py` with NumPy and SciPy. The program tests dimensions 2 through 15, four independent positive hopping/loss pairs per dimension, exact residuals, Hermiticity, strict stability, independent library Lyapunov solutions, every localized diagonal, four direct quadratures of survival, and loss-rate optimality on extended paths. A clean run produced `PASS: 1309 numerical assertions`.

Numerical tests cover only listed finite dimensions. The claim for all dimensions, all positive couplings, and arbitrary initial density matrices rests on the direct algebraic proof, not extrapolation from computations. No independent audit has been performed.
