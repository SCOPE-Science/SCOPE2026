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

# Reproducibility and proof boundary

The file `verify.py` integrates the exact beta-weighted moment on a contour joining \(0\), \(e^{-i\pi/4}\), and \(1\). It compares against the theorem's analytic prefactor and phase at \(\alpha=-1/2,0,1,2\) and \(n=50,200,800\), then checks decrease of the relative errors across degrees. Execute `python verify.py` with `mpmath` available; the run gave `VERIFY_OK 16 deformed-contour/asymptotic comparisons and decay checks; four weights; n=50,200,800`.

The contour is valid because \(e^{i/s}\) decays in the lower angular sector and \(\alpha>-1\) controls the endpoint arc. The leading-order saddle proof requires the unique real saddle \(u=1\), the Gaussian integral for \(\operatorname{Re}\zeta>0\), an exponentially bounded closing contour, and the beta normalization. These are addressed in `RESULT.md`; finite quadrature does not prove the all-degree asymptotic or all-Schatten inclusion.

No independent audit has been performed. The literature comparison leaves unresolved whether a much earlier special-function source independently tabulated precisely this weighted spectral asymptotic.
