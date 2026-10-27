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

Python 3, standard library only. In the directory holding the packaged files run `python3 verify_edge_search.py` and `python3 verify_outer_transfer.py`. Compare their output to `verify_edge_search.out` and `verify_outer_transfer.out`, respectively. Each program raises on mismatch with the known Jacobsthal count or the claimed perfect/non-perfect parity and ends in a named PASS sentinel.

The first program performs vertex-incidence backtracking, canonicalizes colour names at a fixed initial vertex, and checks each bicoloured cycle through \(k=8\). The second builds legal triple-colour transfers along the outer cycle with a twisted seam, then reconstructs independent bicoloured component counts through \(k=10\). The algorithms enumerate all normalized colourings within these stated finite ranges; no extrapolation from a finite search is presented as an all-parameter proof.

The infinite proof resides in RESULT.md: type invariance, odd monodromy, and an even-parity obstruction after triangle contraction. The computational results are reproducibility checks and do not constitute an independent scientific audit.
