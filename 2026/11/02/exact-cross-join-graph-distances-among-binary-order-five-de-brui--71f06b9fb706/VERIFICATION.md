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

# Reproducibility and evidence limits

The accompanying `crossjoin_verify.py` is standalone Python standard-library code. Run `python3 crossjoin_verify.py` in the same folder. The script constructs every 16-bit feedback table and walks the resulting permutation on all 32 states. Exactly 2048 tables encode single cycles. It then tests every potential two-bit switch both by the cyclic alternation criterion and by direct validity of the switched feedback table, checks the resulting undirected graph, reproduces the literature's degree histogram, and performs a complete breadth-first search from every graph vertex.

Expected terminal marker: `VERIFY_OK`. The verified run printed exactly 2048 vertices, 38704 edges, diameter 7, radius 5, unordered distance counts `[38704,305376,758800,710976,254800,27104,368]` and eccentricity counts `{5:48,6:1264,7:736}`. It also checks that all 2096128 unordered pairs and all 2048 vertices are counted, and reports the distance-seven witness masks 32943 and 65361.

This is exhaustive finite verification for the defined order-five graph, not a proof for all orders. It does not test any cryptographic security or other types of nonlinear feedback transformations. The previous degree table is independently published; the distance histogram and diameter have not undergone independent expert review.
