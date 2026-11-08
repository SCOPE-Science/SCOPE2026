---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For K_n square P_L with n,L>=3, power domination first observes closed neighborhoods then unique-neighbor forces. If seeds meet an endpoint clique, propagation successively fills layers; if seeds meet consecutive cliques, propagation works outward on both fronts. Conversely if <=n-2 seeds meet no endpoint and no consecutive layers, at least two entire column indices contain no seeds. In each seedless layer, unseeded-column vertices remain permanently unobserved: a currently observed vertex in a seedless clique has at least two white clique neighbors, while an occupied interior clique vertex from an unseeded column has two white matching neighbors; any other force stays within seeded columns. Thus failure. The n-1 second-layer construction fills first clique then propagates, proving sharp budget. Failed low-budget sets correspond bijectively to independent occupied-layer sets on the interior path; substitute u=(1+z)^n-1 into I_{P_{L-2}} and subtract from all subsets, modulo z^(n-1), including the multivariate version. Independent direct unique-neighbor simulation checked ALL qualifying subsets for n=3,4,5 and L=3,4,5; finite coverage only corroborates. Bernoulli p=c/n with fixed L follows from probability bound by Bin(nL,p)>=n-1, whose tail vanishes; a=(1-c/n)^n->e^-c. No higher-degree or growing-L claim is inferred.

## originality

PASS

Best-of-knowledge PASS: known singleton power-domination minimum, general power-domination polynomials and Cartesian product bounds do not imply the all-low-budget iff or coefficient formulas in the inspected statements. The precise graph-family novelty remains subject to uninspected specialist sections.

## value

PASS

For a natural Cartesian clique-path sensor topology, knowing that one endpoint seed suffices does not describe all successful sparse placements. This sharp structural iff, first failing cardinality, exact entire low-degree coefficient window, layer-marked census, and sparse-sensor reliability law are natural combinatorial and applied graph parameters with distinct use beyond the domination number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
