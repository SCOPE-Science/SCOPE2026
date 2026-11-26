---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independently generated graph orbits directly from all edge masks through order six; the connected counts match, and the submitted Atlas table has exactly one mask in each independent orbit at orders 2–6. For each unordered endpoint pair, enumerated simple paths of the known shortest length and accumulated the exact fractional internal-vertex counts. For Perron comparisons, with p the adjacency characteristic polynomial and lambda its simple top root, q(z)=p(z)/(z−lambda) gives q(A) times the all-ones vector as a positive multiple of the Perron vector: it annihilates other eigenspaces and acts by p'(lambda)>0 on the top eigenspace. Built this vector polynomial by synthetic division and matrix Horner evaluation, isolated lambda over the rationals and used reduction modulo its irreducible factor for ties, with interval sign refinement for nonzero differences. This avoids both the supplied principal-cofactor certificate and floating-point tie decisions. There are no conflicts through five; the seven six-vertex representatives match in both leaders, give disjoint orbits of sizes 720,720,720,720,180,360,360, and exhaust the 3780 conflicts among 26704 connected labeled graphs. The fifth betweenness vector is (7,0,0,6,0,0), and six of seven classes have tied maximum degree. Replay: python /workspace/replay_frozen_graphs.py 5 (SymPy 1.14.0), output /workspace/replay_5.log.

## originality

PASS

The supported contribution is the direct betweenness versus adjacency eigenvector unique-leader boundary and complete seven-class first layer. Prior work compares the measures, and two exact catalogue results already give substantial witness-level information on particular graphs. Those overlaps do not cover the tied-degree domain or supply the complete direct classification. No novelty is attributed to the known PageRank witness graph or its known eigenvector leader.

## value

PASS

A shortest-path broker and a recursively prestigious vertex are two natural but different uses of the phrase most central. The exact smallest-order guarantee under two unique choices and the seven onset types provide precise benchmarks for both concepts and for tie handling. In six of the seven types, a unique-degree-mediated heuristic cannot even be used, so the new complete layer is substantively more informative than reusing a known PageRank/eigenvector witness or one degree comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
