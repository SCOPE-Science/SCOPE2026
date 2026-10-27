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
# Reproduction

Run `python3 verify_triangle_gp.py` with the Python standard library. It reports `PYTHON_VERIFICATION_OK` after comparing labelled block-assembly counts against direct triple-geodesic tests through \(n=6\), checking inclusion-maximality by single-edge extensions, and checking extremal multiplicities through \(n=15\).

Run `c++ -std=c++17 -O3 -o triangle_gp_check verify_triangle_gp.cpp && ./triangle_gp_check`. It reports `ALL_EXHAUSTIVE_CHECKS_OK` after an independently implemented exhaustive edge-subset and maximality enumeration through \(n=7\). Both programs use integer arithmetic and no external input. The exact coefficient comparisons cover all cardinality strata at the stated finite orders.

The proof for all orders uses the connected-clique classification of pairwise-intersecting selected edges, disjoint-support labelled enumeration, and a bidirectional maximality characterization. The finite tests alone do not prove an infinite-family result, and literature searches alone do not prove absolute priority.
