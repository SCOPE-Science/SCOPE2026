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

Execute `python3 verify_heawood_perfect_matching.py` in a directory containing the supplied source file. Only the Python 3 standard library is needed. The script independently computes the Fano-plane incidence pairs, all 24 perfect matchings (by recursion and subset permanent), the 2,201 nonempty simplicial faces, a 1,092-pair deterministic face-poset matching, the 8,736 directed Hasse covers and a complete topological sort. Expected result: `VERIFY_OK`, with precisely one critical vertex and sixteen critical two-cells. The script independently computes mod-two boundary ranks \((20,148,396,360,144,24)\), giving Betti numbers \((1,0,16,0,0,0,0)\).

The chain rank computation checks only field homology. The integral homotopy equivalence follows instead from the acyclic discrete-Morse matching and the absence of critical one-cells or any other higher or lower cells. All finite faces and covers are enumerated; no partial search result or timeout is used as a nonexistence proof. The finding does not classify other bipartite graphs or the homotopy map induced by inclusion into the ordinary matching complex.
