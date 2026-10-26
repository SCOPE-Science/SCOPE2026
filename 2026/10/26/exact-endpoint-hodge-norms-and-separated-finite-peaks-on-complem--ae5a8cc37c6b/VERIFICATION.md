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

Run `python3 verify_2subset.py` from the directory containing this file. The test has no third-party Python dependency and works with exact rational arithmetic. It constructs both graph families directly from the intersection or disjointness relation of two-element subsets, computes grounded Laplacian inverses, reconstructs the canonical edge-current columns, and tests every column of each claimed cut and complementary cycle projection.

The recorded successful run checked the triangular graphs with \(3\le n\le8\) and Kneser graphs with \(5\le n\le8\): **ten graphs and 753 edge columns**. Separate independent edge enumeration checked the detailed electrical-current orbit multiplicities for both families and every integer \(5\le n\le20\), giving **32 exact comparisons**. No floating-point tolerances were used. The code also checks that each diagonal effective resistance lies in \([0,1]\).

The accompanying analytical proof verifies the all-parameter Laplacian solutions, the orbit multiplicities by graph-edge classification, the four closed forms and the exact discrete-difference signs. The finite checker is corroborative, not a substitute for the infinite argument. No independent audit or external certification is asserted.
