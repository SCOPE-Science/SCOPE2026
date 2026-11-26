---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A triple is IR exactly when none of its vertices has two hostile partners, equivalently its induced friendship graph is connected. The independent replay tested all 32,768 labeled simple graphs, testing all 20 triples and pairing each with its complement (each unordered partition is counted twice). It matched every one of the 176 CSV entries, all binomial row totals, 25,748 feasible graphs (6437/8192 at p=1/2), and the two seven-edge positive-minimum-degree obstruction classes (15 and 90). Independent-edge sampling supplies the p^j(1-p)^(15-j) weight per graph, with no further binomial factor. For the analytic dense cutoff, a universal vertex leaves a five-vertex graph with at least three edges, hence two adjacent edges; a degree-four vertex can pair its unique nonneighbor with two neighbors, or the nonneighbor and its sole neighbor with a common third vertex from the degree-four vertex's neighborhood, or use the connected remaining three neighbors if the latter is unavailable. With maximum degree three, eight edges yield degrees (1,3,3,3,3,3) or (2,2,3,3,3,3), and nine give a cubic graph. Deleting the leaf in the first case leaves K5 minus P3 and K2, with the stated spanning path through the leaf. In the second case the two deficient vertices can be joined if nonadjacent and Dirac's theorem applied to the augmented graph; if adjacent, start through them and follow a Hamiltonian path from a prescribed vertex in K4 minus one edge. A six-vertex spanning path splits into two connected triples. Isolation obviously obstructs. The two explicit seven-edge witnesses leave either a K2 component or five vertices covered only by a matching on removal of the universal vertex, so neither can work. The first moment follows by block independence and the all-ten law by counting matching hostility graphs. Scope: exactly six agents, two unordered size-three blocks, symmetric +/-1 preferences; only the probability model assumes independent equal-p edges. The finite census is exhaustive, not a proof for other sizes.

## originality

PASS

The supported distinct claim is the joint edge-layer and connected-triple-partition multiplicity census together with the sharp six-vertex obstruction layer. Neither the P3-factor existence equivalence nor the general constrained-IR model is new. The inspected statements do not supply the claimed law or its sharp obstruction classification.

## value

PASS

Two size-three blocks are the first balanced triadic instance with a choice among full partitions. The joint law answers both how frequently assignment is possible and how many alternatives remain, at every friendship density. The isolate-only threshold and exact preceding obstruction types give a structural explanation at the dense edge of the law, not merely a graph-atlas recount. This is a finite baseline for symmetric constrained allocation, not a conclusion about larger markets or strategic stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
