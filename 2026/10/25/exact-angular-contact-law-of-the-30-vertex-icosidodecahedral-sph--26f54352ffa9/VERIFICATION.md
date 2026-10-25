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

# Verification evidence and limits

The standalone `verify_icosidodecahedral_cover.py` was run against its actual file bytes with Python 3, NumPy and SciPy. It independently reconstructed the 12 original icosahedral vertices, 30 sites and 32 faces, checked the four normal directions at every site, compared the analytic distribution against numerical spherical-area quadrature and 420,000 random directions, and checked the two asymptotic coefficients. It completed with:

```
INDEPENDENT_THIRTY_SITES_TWENTY_TRIANGLES_TWELVE_PENTAGONS_OK
FOUR_ORTHOGONAL_FACE_DIRECTIONS_GOLDEN_GNOMONIC_RHOMBUS_OK
COMPLETE_ELEMENTARY_CDF_MATCHES_INDEPENDENT_SPHERICAL_AREA_QUADRATURE_OK
DIRECT_THIRTY_SITE_UNIFORM_ORIENTATION_MONTE_CARLO_CDF_OK_420000
SHARP_FIRST_OVERLAP_AND_QUADRATIC_COVERAGE_COMPLETION_COEFFICIENTS_OK
ALL_ICOSIDODECAHEDRAL_SPHERICAL_COVERAGE_CHECKS_OK
```

Monte Carlo tests are finite checks, not a proof. The proof is the exact geometric reduction and spherical integral in RESULT.md. The cited 2011 related study was inspected only through the accessible abstract and metadata, not through full text, and historical priority cannot be guaranteed. No independent audit was performed.
