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

The exact transfer and dynamical checks were run from the standalone file `verify_finite.py`. It enumerates every one of the \(9^n\) labelled ternary initial states for \(n=3,4,5,6\), checks each local square and rim circulation, evolves the synchronous update and compares eventual extinction with the zero-Laurent coefficient. The respective matching counts are \(261,1485,8409,49215\). See `CHECKS.txt`.

The standalone exact-algebra script `verify_symbolic.py` recomputes the characteristic factor at unit weight and the second derivative of the weighted characteristic polynomial directly from the prescribed nine rung states; the spectral root and positive variance reproduce the reported constants. Its dependencies include SymPy. The analytic proof additionally uses the published finite-graph circulation theorem and the Perron–Frobenius/Fourier saddle argument, which these bounded computations do not replace.

The comparison of historic material has stated access limits: some early full texts were not materially inspected. No independent audit has been performed.
