---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The exact GF(2) argument M=I+A shows Mx=1 is solvable: for y in ker(M), y·1=yᵀMy=yᵀAy=0 in characteristic two. Selected-vertex induced degree is even, and vertex-disjoint simple cycles prohibit Eulerian degree >=4; hence selected degrees 0/2 and unselected degrees positive odd meet the stated rule. Both seven-vertex examples have explicit center-action contradictions. An independently written integer exhaustive census enumerated all 2^(n choose 2) labelled simple graphs (n<=6) and all n=7 graphs of possible cactus edge sizes 6..9, checked biconnected components, every action profile and explicit adjacency permutations. Counts were n=1..7: 1,1,4,31,362,5676,111982; failures 0 through n=6 and 3150 at n=7, exactly two isomorphism types with multiplicities 630 and 2520. The analytic existence lemma extends beyond finite n; finite enumeration alone would not prove it.

## originality

PASS

The published picky-rule general-graph NP-completeness result and classical odd-domination GF(2) solvability are explicitly prior. They neither classify the first cactus counterexamples nor restrict selected degrees to zero or two where cycles can share vertices. The separately verified seven-vertex two-type obstruction census survives the inspected theorem comparisons; unknown older graph-game censuses remain a priority risk.

## value

PASS

The first obstruction order and complete minimal cactus taxonomy answer a natural small-obstruction question for a previously studied nonmonotone public-goods game. The all-size vertex-disjoint-cycle existence lemma identifies why vertex sharing is structurally important. The 7-vertex cutoff is motivated by first failure, not arbitrary sampling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
