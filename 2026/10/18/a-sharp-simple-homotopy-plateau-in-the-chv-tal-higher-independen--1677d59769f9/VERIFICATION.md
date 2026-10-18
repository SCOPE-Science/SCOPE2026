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

Run `python3 verify_chvatal_plateau.py` on Python 3.10+; only the standard library is used. Successful termination prints `CHVATAL_IND2_IND3_SHARP_SIMPLE_HOMOTOPY_PLATEAU_VERIFIED`.

The program constructs the labeled four-regular triangle-free graph from its complete 24-edge list. It exhaustively tests all \(2^{12}\) masks across thresholds one through four, with an independent maximum-degree test for threshold two. It computes the entire face vectors, the exact homology ranks over \(\mathbb F_2\) for the middle two stages, and an acyclic 211-pair Forman matching (checking every one of 1428 cover incidences). It separately constructs and checks 152 genuine elementary simplicial free-face collapses from stage three to stage two, each on the current complex rather than on a stale incidence count. Exact Euler counts exclude the neighboring threshold inclusions. The integral homotopy conclusion rests on the acyclic Morse CW cell dimensions and valid elementary collapses, not on mod-two observations. The theorem applies only to this finite graph.

Independent mathematical audit has not been performed.
