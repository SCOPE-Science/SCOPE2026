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

# Exact reproducibility

Run `python3 verify_tietze.py` with Python 3. No third-party package, network connection, or external dataset is needed.

The script constructs the labeled Tietze graph by replacing a vertex of the standard Petersen graph with a triangle. It checks all cubical boundary compositions, the 108-dimensional second-boundary image over \(\mathbb F_{101}\), all 27 disjoint simple-cycle product tori, a signed nine-by-nine determinant of \(-1\), the rational rank-four cutoff for total length at most ten, and the index-two obstruction via the gcd of all ten maximal integer minors. It also checks an explicit mod-two detecting functional and the rank increase for each triangle–pentagon torus.

The resulting proof is integral: the unimodular minor shows a rank-nine primitive cycle sublattice, and the boundary-rank bound identifies it with the entire second-homology lattice. Modular ranks by themselves are not treated as proof of integral generation or of the index.

# Limits

The claims are restricted to the ordinary two-point unordered configuration of the specified twelve-vertex graph and to product tori of vertex-disjoint simple cycles. The verifier proves neither a general triangle-expansion theorem nor absence of equivalent statements in unavailable literature. Independent audit is not performed.
