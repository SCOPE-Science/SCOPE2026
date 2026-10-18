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

# Verification

Run `python3 verify_heawood.py` in the directory containing the seven delivered files. The code uses standard Python 3 only and contains no nonstandard libraries, external files or network dependencies. It generates the Fano point-line incidence graph from three-bit dot products and checks that there are 14 vertices, 21 edges and degree three at every vertex.

Two **structurally independent** finite enumeration methods are checked for equality as complete sets: point-height envelopes with independently chosen monochromatic line heights, and spanning-tree incremental assignments of integer Lipschitz potentials with saturated-edge connectivity. Each produces exactly 660 normalized dual extreme potentials. The program checks the point-height level distribution 2,252,406, the closed subset count, all 336 graph automorphisms and their preservation of the incidence edges, the action under sign reversal, and the ten disjoint symmetry orbits and their explicit representatives.

A separate analytic proof in RESULT.md derives the 660 count from the Fano incidences. The ten-orbit classification additionally uses certified finite exhaustive loops; the loops are finite because each point family has at most 64 patterns and each monochromatic line has exactly two heights, and the spanning-tree check considers only three integer increments per tree edge. The output `ALL EXACT CHECKS PASSED` means that the stored assertions were satisfied, **not** that an independent scientific audit occurred or that the result is certified by an external authority.

Limitations: the computation addresses only this fourteen-vertex metric graph and the specified graph-automorphism-plus-sign action. It does not establish priority relative to unindexed research or test higher-order projective planes.
