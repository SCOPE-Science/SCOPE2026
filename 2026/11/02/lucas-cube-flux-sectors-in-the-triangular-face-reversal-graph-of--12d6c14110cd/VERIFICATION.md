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

The Eulerian balance equations t_i+v_i=t_{i-1}+d_{i-1}, b_i+d_i=b_{i-1}+v_i imply a constant flux j=t_i+b_i+d_i in {0,1,2,3}. The extreme fluxes force all-zero/all-one orientations, both isolated. In j=1, each triple is X=001,Y=010,Z=100 and the 0/1 vertical reconstruction excludes precisely adjacent YZ. Coding X->00,Y->01,Z->10 turns cyclic words into independent sets of C_{2n}; upper/lower belt triangular flips correspond to allowed first/second site toggles; bit complement gives j=2. Removing I\J then adding J\I yields exact Hamming distance; coordinatewise majority of three independent sets remains independent, proving median; the only diameter 2n pair is the two alternating maximum independent sets. Classical Lucas/Fibonacci independent-set counts then give edges. Independently enumerated all raw balanced edge orientations for n=3 and 4, obtaining respectively 38 and 96 states, component sizes [1,1,18,18] and [1,1,47,47], and 60 and 208 edges, in agreement with the formulas. The local encoding argument proves all n.

## originality

PASS

Felsner establishes lattice structure for planar prescribed-outdegree orientations under general face flips; Creed treats Eulerian face-flip chains on triangular lattice graphs. Neither cited source directly states a four-component graph for antiprisms with the cap moves forbidden. Lucas cubes and their metric/vertex/edge formulas are prior work; originality is exclusively the exact flux-sector realization and restricted reconfiguration identification. Best-of-knowledge PASS with possible earlier ice/height-function alias risk.

## value

PASS

A full reconfiguration-graph decomposition of a canonical planar 4-regular polyhedron distinguishes conserved flux sectors, frozen orientations and isometric median components. It is a natural structural theorem with exact shortest-move distances, not simply an isolated Lucas-number recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
