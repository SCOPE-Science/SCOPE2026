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

# Verification record

The analytic proof is in `RESULT.md`. Execute `python verify.py` with NumPy installed. The standalone checker directly solves the finite-diffusivity fourth-degree characteristic equation, retains the two positive decaying modes, matches the two target orientation boundary conditions, and divides by the exact finite-diffusivity hit probability. It tests three loading offsets (−1.5, 0, 1.5), three marking/temporal arguments, and thermal diffusivities 0.01, 0.001 and 0.0001 at unit spatial length, rate and propulsion.

All nine sequences showed decreasing errors and a final absolute error smaller than 0.005. The maximum observed final error was approximately 0.00260493. This tests the claimed joint transform, including the exact no-reversal case, but **numerical evidence cannot establish a continuum limit by itself**. The proof relies on controlled algebraic root expansions and bounded Dirichlet uniqueness. No independent audit has been performed.
