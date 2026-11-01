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

Run `python verify_d4.py` using a standard Python 3 interpreter; no third-party modules or network access are needed. The code independently solves the simple-root coordinate equations over exact rationals for all twelve positive roots, generates all pairwise-incomparable subsets, checks the entire maximal-facet list, and verifies the free-face uniqueness for each of the five collapses. It then identifies the eight triangles of the octahedral two-sphere, the eight further edges, the two isolated vertices, and a spanning tree leaving exactly five non-spherical loop edges.

The run also computes mod-two simplicial boundary ranks \((9,10,1)\) in degrees one through three, matching reduced Betti ranks \((2,5,1)\). The proof of the integral homotopy type is the elementary-collapse and spanning-tree argument in RESULT.md. A finite field calculation alone cannot establish integral torsion-freeness or an arbitrary attaching map, and is not used in place of that argument. There is no claim beyond the type-\(D_4\) root poset.
