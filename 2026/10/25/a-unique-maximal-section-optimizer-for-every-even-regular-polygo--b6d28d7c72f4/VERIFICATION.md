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

# Reproduction checks and limits

Run `python3 VERIFY.py` with any standard Python 3 interpreter; no third-party packages are required. The script verifies the angular-threshold characterization of maximum-side-count central sections against 210,000 independently generated prism/plane edge sign counts; compares the analytic arcsine formula with direct azimuth quadrature; checks that its unique stationary height improves nearby heights and the edge-uniform height; verifies the exact six-sided-base case and the previously known cube specialization; and tests the high-order limits numerically for increasing even base counts. Its completed output ends with `ALL_EVEN_PRISM_CENTRAL_SECTION_CHECKS_OK`.

The actual universal proof is the face-count argument, exact event reduction, Haar integral, derivative sign analysis, and Taylor expansion in `RESULT.md`. Finite random checks cannot certify an all-parameter theorem. Exceptional normals meeting a prism vertex are omitted as a Haar-null set; no statements about their degeneracies are made. Independent mathematical audit has not been performed.
