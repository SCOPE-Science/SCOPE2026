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

# Verification and scope

The exact symbolic part of `verify.py` tests the \(d=2\) Gauss–Bonnet reduction and simplifies the \(d=4\) first correction to \(13\sqrt{15}/15\). For positive \(t\), the numerical section evaluates the Klein-model exact volume integral by independent Gauss–Legendre quadrature over barycentric simplex coordinates, rather than integrating the asymptotic itself. Observed relative residuals after truncating the two-term \(d=4\) model at \(t=0.04,0.02,0.01,0.005\) divided by \(t^2\) are approximately \(17.35,15.95,15.46,15.26\); they remain bounded as predicted by the analytical remainder. The exact two-dimensional area agreement is checked separately.

Install the dependencies specified in `requirements.txt` and run `python verify.py`. Quadrature is finite corroboration, not proof for all dimensions or angles. The analytic demonstration and normalization are in `RESULT.md`. The externally cited classification theorem has not been independently reproduced. No independent audit has been performed.
