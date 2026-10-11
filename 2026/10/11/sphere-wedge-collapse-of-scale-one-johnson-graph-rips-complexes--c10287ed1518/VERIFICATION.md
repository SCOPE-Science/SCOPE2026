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
# Verification and scope

Run `python3 verify_johnson.py` beside the scientific files. This standard-library program creates the graphs from the \(k\)-subsets, enumerates maximal cliques directly from adjacency via Bron–Kerbosch, enumerates the entire flag complex, tests each proposed free-face collapse against the current surviving complex, and calculates mod-two chain boundary ranks.

The completed execution tested all 15 pairs with \(4\le n\le8\) and \(2\le k\le n-2\) and checked 2,872 collapse pairs. The final marker was `VERIFY_OK cases=15 exact_collapse_pairs=2872`. The ranks in every test gave zero first homology and second homology of the predicted rank. The examples \((n,k)=(6,3),(7,3),(8,4)\) yielded 19, 55 and 181 independent mod-two two-cycles respectively.

This is corroboration only; it neither tests all parameters nor establishes an integral or infinite statement by enumeration. The all-parameter proof is the combinatorial collapse, the simply connected hypersimplex two-skeleton, and Hurewicz/Whitehead. No independent audit or formal certification has been performed.
