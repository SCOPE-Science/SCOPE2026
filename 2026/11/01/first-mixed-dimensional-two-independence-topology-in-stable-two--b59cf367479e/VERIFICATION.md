---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The graph has the stable nonconsecutive two-subsets of an (k+4)-cycle as vertices, with disjointness adjacency. A legal Ind_2 face has induced maximum degree at most one; an exhaustive increasing-maximum subset recursion builds each face once, not a sampled list. I independently rebuilt all seven graphs for k=0..6, with augmented face counts 4,21,93,316,851,1948,4006, and checked the actual vertex-order matchings from verify_stable_kneser_two_independence.py against every Hasse cover. The reversed-incidence DAGs are acyclic. Independently recomputed the integer Morse projections and exact Smith normal forms: the critical d2 ranks are 1 at k=3..6, d3 ranks for k=3,4,5,6 are 0,0,9,21, and all nonzero Smith factors are units. For k=6, critical dimensions (c1,c2,c3)=(1,48,23) give Betti (0,26,2), no torsion; earlier cases give the stated circle, two-sphere and wedge ranks. In these CW Morse models a degree-one 2-cell kills the one-cell; Hurewicz for the simply connected remaining 2-skeleton identifies 3-cell attaching degrees and unit cancellation supplies the asserted wedges. No result beyond k=6 follows.

## originality

PASS

Direct comparison of distinct graph/complex or fixed-locus objects and their known implications: First mixed-dimensional two-independence topology in stable two-subset Kneser graphs. Inspected sources and Resultary searches below support a best-of-knowledge novelty finding, not a worldwide priority guarantee.

## value

PASS

The first appearance of degree-three integral homology in the natural higher independence complexes of stable Kneser graphs is a motivated finite topological threshold. Determining the exact k<=6 homotopy types, rather than just rational Betti numbers, informs future classifications and distinguishes Ind_2 from ordinary Ind. A seven-term initial segment is finite, but the k=6 mixed-dimensional transition is not an arbitrary input or a known table restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
