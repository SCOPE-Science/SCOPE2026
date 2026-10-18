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

# Reproduction and limits

Run `python check_spindle_john.py` with Python 3; no packages beyond the standard library are required. The script verifies (a) exact rational discriminant and isotropic-contact identities, (b) roots and meridian inclusion over 49 independent parameter/dimension cases, (c) strict numerical volume maximization over the two-axis ellipsoid family, and (d) agreement of the numerical volume ratios with the three asymptotic coefficients for fixed separations.

The precise algebraic certificate is the quadratic stationarity relation
\[
m(D-z)(1-z)=(m-1)(1-D)z
\]
together with the contact-parameter identity \(t_*^2=z/m\). Under the ellipsoid normalization, symmetric pairs of contact points with normalized axial coordinate \(\pm1/\sqrt m\), uniformly averaged in their transverse spherical direction, have covariance \(I_m/m\). After multiplying the contact probability measure by \(m\), this is John's necessary-and-sufficient contact identity.

All-dimensional conclusions are proved using the meridian ratio's derivative, uniqueness of the John ellipsoid, and Gaussian asymptotic integration. Numerical tests do not constitute an exhaustive search over the continuum of ellipsoids or a proof of the asymptotic errors. The tests were executed against the supplied code during preparation. There has been no independent external audit.
