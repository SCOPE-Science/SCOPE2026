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

# Verification of the four-point stability formula

The accompanying `verify_phase.py` needs only Python 3's standard library and was executed from its actual package path. Its output was `EXACT_FOUR_POINT_ISOTONIC_SOBLEV_CERTIFICATE_OK 250`.

The script computes \(\det(E_\pi Q_\gamma E_\pi-tQ_\gamma)\) exactly, for all eight consecutive pooling partitions. The determinant and the claimed factorization are both polynomials of degree at most four separately in \(\gamma\) and \(t\). Equality on a five-by-five rational grid is therefore an **identity certificate** by univariate polynomial interpolation in each variable. Further noninteger evaluations and two exact rational attaining pairs are included as regression checks. No finite-data inference is used to replace the independent analytic arguments that all pooling cells occur or that a continuous piecewise-linear map has global modulus equal to the maximum cell modulus.

The displayed branch comparison, attainment argument and classification are proved in `RESULT.md`. The checker does not establish priority or results for five or more observations. No independent audit has been performed.
