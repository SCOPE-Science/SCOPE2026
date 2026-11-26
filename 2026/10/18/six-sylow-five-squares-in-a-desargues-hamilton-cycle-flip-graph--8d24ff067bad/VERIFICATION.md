---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The graph is bipartite cubic. In a Hamilton cycle, consecutive distinct lower vertices have a unique common upper vertex if their union is a triple, and none otherwise. Thus a Hamilton tour is recovered exactly from its cyclic lower-vertex order when the ten successive unions are distinct triples. Fixing one lower vertex and one direction per order exhausts the unoriented, unrooted states and gives 24 cycles. For the alternate Petersen representation, label upper vertices by complements of two-sets; containment becomes disjointness. On the cyclic set of ground labels, write A_i={i,i+1}, B_i={i,i+2} mod 5. The A-shell has successive indices 2j mod 5 in alternating layers, with spoke to B_(2j+2) in the opposite layer. The B-shell has successive steps j↦j±3 in this positional numbering, giving GP(10,3). In a cubic graph complementing a Hamilton edge set gives a perfect matching and does not change symmetric differences; an alternating single flip is therefore exactly a connected nonempty degree-two difference. Independent replay /workspace/branches/check_4.py checks all 276 state pairs on the direct Hamilton edge sets; connected difference lengths/counts are 10:84 and 18:60, with all other differences of split shapes (6,6), (6,10), (10,10). Neighbor sets and two-step reachability give (1,7,16) at every vertex, and the length-18 graph has two size-twelve components of degree five. Exceptional edges are exactly those with no common neighbor; their components are six squares, with one neighbor per vertex in each other square, giving all fifteen cross-square perfect matchings. The permutation action is transitive with order-five stabilizer; labelling gH by grg⁻¹ for a chosen stabilizer generator is well-defined and has 24 values, since the centralizer of a five-cycle is its cyclic subgroup. The replay verifies that the square labels are the four generators of one Sylow subgroup and within-square neighbors are the second and third powers. By the normalizer action each cross-square neighbor set is one stabilizer orbit: the order-five subgroup acts transitively on the other five Sylow subgroups. This reproduces the finite conclusions independently of the supplied matching and tour implementations.

## originality

PASS

The census of 24 Hamilton cycles is verifiably prior published work (Haugland 2025), not tentative novelty. The supported distinct contribution is the classification of restricted Hamiltonicity-preserving transitions, especially the intrinsic and equivariant six-square structure and the length-18 decomposition. A distinct later-dated catalogue entry substantially covers the length-ten threshold and local/metric classification, and the count of length-18 transitions; the overlap is real and neither catalogue date alone nor rephrasing establishes historical priority.

## value

PASS

The natural first nontrivial middle-level state space tests whether alternating swaps can transform Hamilton tours while retaining Hamiltonicity. The sharp smallest usable move length, short-path connectivity and intrinsic organization of the shortest moves into six group-labelled fibers explain the connectivity structure rather than just count states. The deceptively plentiful length-18 moves fail to connect all states, illustrating why length and admissibility matter. These exact results are useful benchmarks for reconfiguration on middle levels and cubic graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
