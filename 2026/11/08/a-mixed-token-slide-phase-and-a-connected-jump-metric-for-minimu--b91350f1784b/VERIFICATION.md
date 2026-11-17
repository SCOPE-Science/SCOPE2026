---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Cubic edge-count inequality 2k>=8+e(S) forces minimum k>=4 and independence/equivalent induced-tree structure at k=4. Read RESULT.md and both direct_check.js and cycle_check.js Git blobs. Independent graph generation, union-find complete enumeration and all-source BFS confirmed GP(5,2): 20 optimal triples all slides frozen; GP(6,2): 120 optimal 4-sets connected slides; GP(7,2): 70 optimal 4-sets, slide 14K1+14K2+7P4 (35 edges), jump 4-regular, 140 edges, eccentricities 56 at 6 and 14 at 7. This is full finite enumeration, not a theorem for n>=8.

## originality

PASS

Bau--Beineke, Wei--Li, Gao et al. study decycling numbers; known feedback-set jump/slide notions are prior. Search found self-entry plus Heawood/Pappus/dodecahedral FVS move graphs, not GP7 exact 70-state mixed mobility formula. The claim is a natural graph-specific exact configuration classification, not invented move notion or generalized Petersen all-order theorem.

## value

PASS

Minimum feedback-set mobility is natural in graph reconfiguration; GP7 gives first mixed frozen/movable optimal slide phase among checked initial n=5,6,7, with connected jumps and sharp metric. Exact finite invariant is independently useful despite modest graph order.

The dated certificate retains the supplied scientific assessment, sources and limitations.
