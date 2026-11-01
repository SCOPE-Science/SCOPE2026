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

# Verification record

The result is supported by an analytical proof in `RESULT.md`, not by enumeration. Run the portable Python standard-library script `verify_median_bv.py`; it enumerates all distinct input-order chambers on paths of 2 through 7 vertices and computes exact rational weighted edge-step column norms. It checks three positive rational edge-weight profiles at each path length, validates an attained exact four-site output-amplification witness and verifies the tridiagonal Perron eigenrelation numerically for path sizes 3 through 30.

A successful run must emit `ALL TESTS PASS` and count 103,218 exact chamber-column comparisons. These finite checks do not verify the infinite family directly. Stronger originality claims would require further literature access and independent review.

