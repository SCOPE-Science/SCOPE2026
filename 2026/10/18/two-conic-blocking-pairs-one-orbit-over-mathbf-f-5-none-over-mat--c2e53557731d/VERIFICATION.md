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

# Reproducibility and limits

Execute `python verify_conic_census.py` for exhaustive normalized-form smoothness and line-coverage tests over \(\mathbf F_5\) and \(\mathbf F_7\); run `python verify_conic_orbit.py` for the full \(\operatorname{PGL}_2(\mathbf F_5)\) action and unique-orbit check. Run `python crosscheck_numpy.py` with NumPy available for an independently coded matrix-incidence enumeration. These were executed successfully, returning respectively `(3100, 12)` and `(16758, 0)` smooth-conic/partner counts and one orbit of size 18,600. All loops cover finite canonical forms; no infinity claim is made. The symmetric-matrix determinant supplies a field-independent exact criterion for geometric smoothness in odd characteristic. Public literature priority remains subject to archival coverage limitations. No independent audit has been performed.
