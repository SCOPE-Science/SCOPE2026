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

# Reproducibility and limitations

Use Python 3 with only its standard library and execute `python3 artifacts/verify_hypercube_pade.py` from the package root. The script regenerates exact spectral-shell numerators for the seven-dimensional binary cube, verifies integer polynomial factorizations for the three possible sign-changing Hamming shells, positive coefficients in all other off-diagonal shells, the positive-root count by sign variations, rational brackets and rational spectral evaluations. It also proves the Padé seventh Taylor coefficient and checks the lower-dimensional leading kernel coefficients. An actual run of the packaged script returned `VERIFY_OK` and completed without exceptions.

The underlying proof and exact polynomial signs, rather than a finite grid of test timesteps, establish the infinite-family and all-timestep statements. The supplied script checks identities; it is not an independent audit, certified theorem prover, or floating-point implementation. No claims are made about weights, internal stages, nonlinear positivity, or universal numerical accuracy.
