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
The result is established by the analytical mixed-moment/Fourier-uniqueness proof in `RESULT.md`. For \(m<1\), the angular parity and complex Gamma-integral calculation annihilate *all* mixed moments. For \(m\ge1\), exponential integrability and one-dimensional Fourier-analytic continuation along every real direction prove symbol uniqueness.

`verify_moments.py` independently executes finite, non-certifying numerical checks of the trigonometric phases and representative angular embedding bounds. Such checks do not constitute an infinite-dimensional proof or an independent audit. All symbols are taken modulo equality almost everywhere. The entire-kernel classification and non-bounded symbol cases remain open here.
