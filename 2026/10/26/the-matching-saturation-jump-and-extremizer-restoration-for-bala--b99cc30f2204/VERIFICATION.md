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

# Exact-rational verification

Execute `python3 check.py` with Python 3.10 or later. No third-party packages are used. The checker reconstructs the full Laplacian of each graph \(G_{s,t}\) for \(3\le s\le8\), \(0\le t\le s\), grounds one vertex, and performs exact rational Gauss–Jordan inversion.

For every edge source it checks the independently reconstructed transfer-current column against the rank-update formula, computes both absolute column sums directly, verifies all edge-orbit formulas, checks maximizing column types and compares current signs for every surviving target edge. In the saturated case it checks the complete-matching formulas. It thereby tests 39 graphs, 1,370 source columns, and 60,990 transfer-current entries. The actual successful output is:

`MATCHING_DELETION_ENDPOINT_EXACT_OK graphs=39 columns=1370 current_entries=60990 positive_disjoint_entries=1566`

All code required for this check accompanies the report. Its computations are finite consistency tests. The universal correctness argument is the symbolic derivation and sign/inequality proof in `RESULT.md`; checking the enumerated cases alone does not verify every integer parameter.
