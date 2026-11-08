---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

In Kneser K(3r-3,r), closed neighborhoods of distinct r-subsets are disjoint exactly when intersection size is 1 or 2: intersection 0 means adjacency; intersection >=3 creates a common disjoint neighbor. Four such r-sets require union size >=4r-12>3r-3 for r>=10, so maximum 3. Three-block intersections are 1 or 2, and enumerating the eight feasible Venn signatures (number k of pairwise 2-intersections, triple intersection t) gives multinomial counts divided by 6 for unordered families; all atom coordinates identify one S_n orbit for each (k,t). Recomputed exhaustive K(9,4) all 126 vertices: 6300 pairs, 163800 triples with orbit signatures (0,0):7560, (1,0):45360, (1,1):7560, (2,0):22680, (2,1):45360, (3,0):1260, (3,1):30240, (3,2):3780. This finite experiment is cross-check, not all-r proof.

## originality

PASS

Kneser packing size 3 and 1<=pairwise intersection<=2 were previously proved by Brešar et al. The evaluated full cubic enumerator, exact labeled triple multiplicities and eight orbit classification for all r>=11 were not present in inspected primary results; coding tables for maximum size or upper intersection alone do not logically imply these counts.

## value

PASS

Complete counting polynomial and exact orbit representatives of optimizers are natural enumeration and symmetry invariants of the Kneser diagonal; the formulas answer questions not decided by the already-known maximum value, with potentially useful exact distributions for covering/coding correspondences.

The dated certificate retains the supplied scientific assessment, sources and limitations.
