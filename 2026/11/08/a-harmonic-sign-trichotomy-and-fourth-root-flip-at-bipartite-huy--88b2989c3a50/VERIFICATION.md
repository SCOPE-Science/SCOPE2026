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

The analytic reduction is in `RESULT.md`. Numerical spot tests were run with the accompanying `verify_two_harmonic.py` (NumPy/SciPy) and reported `VERIFY_OK graphs=3 regimes=3 checks=72`. The tests reconstruct each graph Laplacian, solve the symmetric half-return equation, check the two-cycle relation and perturbative amplitude, and inspect all non-neutral one-step eigenvalues for an edge, a weighted path, and a weighted star at subcritical, tricritical, and supercritical parameters. The tests are illustrative and finite; the arbitrary-graph proof uses Perron–Frobenius simplicity, analyticity, a Lyapunov–Schmidt decomposition, and full quotient spectral stability. The residual historical-priority assessment is not an independent audit.
