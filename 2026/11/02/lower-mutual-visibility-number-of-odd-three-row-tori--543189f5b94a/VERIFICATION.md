---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

In C_3 square C_n for odd n, a shortest cross-row path switches rows exactly once; its column motion is a unique shortest cycle arc. An inclusion-maximal visible set must occupy every row, otherwise a new vertex can be placed in the empty row and connect to all selected vertices without internal interference. For occupancy patterns (1,1,1) and (2,1,1), extension in a singleton/paired row yields a larger visible set: for the pair in one row, the third cycle point k+1 gives gaps d,k+1-d,k all <=k. The proposed five-set has ten pairwise witness geodesics and its six exhaustive external-vertex column cases produce blocked witness pairs. An independent BFS shortest-path obstruction computation verified the five-set is maximal for n=5 and 7 and exhaustively excluded all smaller maximal sets for those n. The all-odd-n theorem rests on the case proof, not extrapolated BFS.

## originality

PASS

Brešar–Yero introduced the lower invariant and explicitly posed lower numbers for toroidal grids as Problem 1; their grid formula concerns P_m square P_n and K_m square K_n, not C_3 square C_{odd>=5}. Maximum or total visibility studies on tori are different quantifiers. Therefore this natural open-problem subfamily appears original, with priority risk from newer unindexed torus work.

## value

PASS

The lower mutual-visibility number is a natural greedy terminal-size invariant; solving the previously explicitly asked torus subfamily with a uniform minimum 5 and a sharp construction gives a meaningful extremal graph theorem beyond textbook path-grid formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
