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
# Reproducibility and scope

Execute `python verify.py` with Python 3 and `mpmath`. The test uses 65-digit precision to compare the closed Bessel coefficient against the integral of the solved first angular harmonic, reconstruct the harmonic radial ODE, check the exact zero-rotation polynomial and sample strict order, and numerically evaluate the large-rotation boundary layer. Successful checks are numerical and finite; no machine formalization of the global theorem or independent scientific audit has been performed.

The analytical proof is in `RESULT.md`: a backward Dirichlet equation, a Bessel boundary problem, a radial divergence integration, positive resolvent comparison, and uniform Bessel asymptotics. The claim concerns the coefficient of weak propulsion at fixed rotational diffusivity followed by a large-diffusivity analysis; it does not verify simultaneous two-parameter uniformity, different geometries or interactions.
