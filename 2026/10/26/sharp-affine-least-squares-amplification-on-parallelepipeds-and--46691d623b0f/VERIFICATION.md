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

# Reproducibility and verification

Run `python verify.py` with Python 3 and the standard library. The program evaluates the exact rational formula and independently computes uniform-sum densities through repeated polynomial convolution, testing equality of the signed-integral row norm through dimension nine. It also checks rational threshold fractions, finite-range monotonicity and large-d numerical convergence of the second asymptotic coefficient. The source executed successfully with 111 assertions in the working environment.

The all-dimensional assertions are established in `RESULT.md`: an orthonormal affine basis supplies the kernel, vertex convexity yields the global norm, standard clipped-cube inclusion-exclusion yields the finite sum, conditional Jensen gives strict monotonicity, and a controlled Fourier-integral expansion yields the asymptotic coefficient. Finite calculations alone do not certify those universal steps.

Independent audit has not been performed. Historical priority is provisional, and a prior equivalent cube norm formula may exist under different terminology.
