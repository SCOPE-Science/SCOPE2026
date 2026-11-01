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

# Verification

The exact certificate is the included standalone `octave_certificate.py`. It requires Python 3 standard libraries only. Running `python3 octave_certificate.py` on the packaged file prints:

`CERTIFICATE_OK all=729 strict=726 exceptional=3 witness=exact`

It enumerates each of the \(3^6=729\) matrices of radius choices, scales them by 30 to integral entries, and uses exact fraction-free Bareiss determinants to verify that all six leading principal minors of \(1269I_6-B_s^{\mathsf T}B_s\) are strictly positive for every one of the 726 nonexceptional choices. It separately checks that the other three choices are exactly the radius-zero-on-one-antipodal-pair configurations, and checks the winning algebraic eigenvector equations over \(\mathbb Q(\sqrt6)\).

The logical scope is the six-vertex problem only. Exhaustiveness is mathematical because there are exactly three distinct centered balls at each vertex and every real nonnegative input has a maximizing coordinatewise radius choice. Floating-point computations are not used to establish the exhaustive bound. The analytic two-dimensional block proof and active-radius inequalities establish attainment and all extremizers. No external independent validation is asserted.
