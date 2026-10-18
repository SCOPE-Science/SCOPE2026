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

Run `python3 verify.py` with Python 3.9 or later; no third-party packages, network access, or external data files are required. The program enumerates all nine-edge subsets of the three-by-three bipartite graph, removes those containing one of six perfect matchings, reconstructs the cross-polytope cycle and the six-supported cochain, and checks their signed integral incidence equations. It verifies both row/column transposition Lefschetz numbers and all 36 small-symmetry degrees. Independent projection checks cover 5,329 combinations through five rows/columns. Signed fixed-face counts for the four-by-four complex verify all 25 conjugacy-character pairs.

The expected final marker is `VERIFY_OK_INTEGRAL_BIPARTITE_NONMATCHING_K3_HOOK_TENSOR`. Success is not a proof of arbitrary-size behavior: that comes from the exact homological detection argument and the published Linusson--Shareshian--Welker homotopy/rank theorem. The code does not attempt to verify the published theorem in all sizes or to establish any case with a forbidden matching larger than three. Independent audit: not performed.
