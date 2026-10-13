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

# Reproduction and limitations

From this directory execute:

`python3 verify.py`

The verifier is standard-library-only. It implements two structurally distinct enumerations: direct vertex-level finite tree closures and color-preserving isomorphism keys, and a bounded recursive multiset construction. It independently calculates unbounded generating-function coefficients by formal series arithmetic; it checks partition coefficients using Euler's generalized-pentagonal recurrence, not a partition-sequence lookup.

Recorded output:

`VERIFY_OK 42474 exact assertions; 1444 labelled finite-node selections screened; 7 tree-plan shapes compared by direct isomorphism invariants; 4283 exhaustive small plans incl. 2107 antichain plans`

The enumeration exhaustively covers all selected-node configurations for the seven chosen actual finite colored trees with two successor copies per infinity label. In addition, it enumerates every increasing-parent plan encoding with at most six nodes, every root-respecting infinity labelling, and the corresponding rational identity for antichain-label plans. These are finite regression checks, not exhaustive checks of all plans or a computational proof of the infinite growth assertions. The latter follow from the complete structural argument in RESULT.md. Independent mathematical audit has not been performed.
