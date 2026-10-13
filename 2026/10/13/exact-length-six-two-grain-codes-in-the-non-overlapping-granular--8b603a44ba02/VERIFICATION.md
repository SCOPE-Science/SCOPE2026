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

The verification target is the binary non-overlapping grain channel at length \(6\) with at most two grains. `artifacts/verify.py` reconstructs every allowed nonconsecutive grain pattern in two independent ways and checks equality. It then reconstructs every error ball in two independent ways and checks equality for all \(64\) transmitted words.

The verifier builds the compatibility graph in which two words are adjacent exactly when their error balls are disjoint. It exhaustively enumerates all maximal cliques, performs a separate branch-and-bound maximum-clique computation, and independently enumerates all cliques of size \(10\) in increasing order. It then intersects the sixteen maximum codes.

The saved replay in `artifacts/verification_output.txt` reports: `patterns=12`, `vertices=64`, `edges=1432`, `maximum=10`, `labeled_maxima=16`, `independent_10cliques=16`, and `core=001100,011001,100110,110011`. The computation is exhaustive only for this finite parameter; it is not evidence for other lengths, other numbers of grains, or the overlapping-grain channel.
