---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The Heawood graph is the Fano incidence graph on 14 vertices with locating domination defined only for 8 unselected vertices. Exact signature checks exclude every subset of size <6 and identify 448 passing six-subsets out of 3003. One-for-one token-jumping swaps on this complete list give 3192 edges and degree histogram 28·z^6+168·z^12+168·z^14+84·z^22. Independently reconstructed all 448 breadth-first search distance maps: every state eccentricity 6, distance histogram (3192,15204,32508,32298,14868,2058), exactly 2940 pairs need the one-exchange detour beyond 6−|S∩T| (1008 with j2,1428 j3,504 j4). Inspected two distinct frozen scripts: one Hamiltonian-cycle/chords complete BFS, and one Fano GL(3,2) plus duality computation of 336 automorphisms with four orbit sizes (28,84,168,168). All finite domains and predicates specified and complete; no extrapolation to other graphs.

## originality

PASS

The six-vertex Heawood locating-dominating optimum was previously known (Balbuena–Foucaud–Hansberg Proposition 24). The contribution is the full 448-state minimum-code exchange graph, its four automorphism orbits and exact distance/one-detour histogram. Published generic domination reconfiguration uses a weaker feasibility predicate and does not imply locating-dominating exchange distances. Same-graph exact historical table remains a priority risk, and finite object is motivated by canonical Fano-plane symmetry.

## value

PASS

The Heawood/Fano incidence graph is a canonical symmetric graph and its minimum locating-dominating codes have a natural reconfiguration geometry. The exact 448-state census, orbit classification, full metric distribution and sharp +1 exchange stretch give a meaningful complete finite classification beyond the previously known optimum six, without requiring an asymptotic theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
