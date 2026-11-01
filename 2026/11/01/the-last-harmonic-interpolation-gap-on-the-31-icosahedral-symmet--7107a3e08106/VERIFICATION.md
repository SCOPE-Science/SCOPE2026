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
# Verification of the interpolation-rank classification

Run `python3 verify.py` in the package directory with Python 3; no extra libraries or network are required. The script rebuilds the 62 endpoints of 31 antipodal axes from the three icosahedral symmetry orbits, checks exact norms and separation, performs exact \(\mathbb Q(\sqrt5)\) elimination for degrees 0–74, and verifies all claimed ranks. For 75–1699 it certifies full rank with the nonzero finite-field reductions modulo 10009 under \(\sqrt5\mapsto4070\). Strict inequality for degrees at least 1700 is proved analytically from the explicit minimum angular separation and the classical Bernstein Legendre bound. The success marker is `ICOSAHEDRAL_31_AXES_ALL_DEGREE_CERTIFICATE_OK`.

The finite-field reductions certify nonvanishing in characteristic zero only at the tested finite degrees; no computation alone certifies the infinite tail. Historical bibliographic originality is subject to residual access uncertainty. Independent validation has not been performed.
