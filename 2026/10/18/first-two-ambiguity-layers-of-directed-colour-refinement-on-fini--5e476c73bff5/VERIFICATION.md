---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For each order n<=7 the degree-sorted lexicographically minimal upper-triangle code is a complete isomorphism invariant: any tournament isomorphism preserves outdegree blocks, and all within-block permutations are examined. The n->n+1 vertex-extension process with all 2^n incidence masks is inductively exhaustive for isomorphism classes. Directed 1-WL with a shared palette and in/out-neighbour colour counts, including old colour in the key, yields exactly the C^2-equivalence test for the single binary arc language. Since colours never merge, equality of palette size certifies stability. Independently implemented exact enumeration (not executing opaque repository code) produced isomorphism counts 1,1,2,4,12,56,456 and C^2 class counts 1,1,2,4,12,55,451; the only n=6 collision is [9378,9381], and n=7 has [9378,9381], [232512,232706,238754], [559362,559365], [594448,594468]. Distinct transitive-four counts within each group prove nonisomorphism. The explicit n=6 equitable two-triple orientation agrees with the table. No n>=8 or alternative colours/languages are claimed.

## originality

PASS

Best-of-knowledge qualified novelty attaches only to the complete first two ambiguous C^2 quotient layers of uncoloured tournaments: 56 isomorphism types / 55 classes at n=6 and 456 / 451 at n=7, including the exact four n=7 nonsingleton canonical-code groups. Kiefer-Schweitzer-Selman 2015 and Kiefer 2020 already characterize individual C^2-identification and imply important regular/cyclic nonidentification mechanisms, so existence of ambiguity by itself is not new. McKay already tabulates 56/456 tournaments. Searches across original papers, aliases and published Resultary records did not locate the exact pairwise class table. This is a bounded qualified original finite classification, not a priority guarantee.

## value

PASS

The precise first failure threshold for directed 1-WL on uncoloured finite tournaments and its complete immediately following layer are natural finite-model-theoretic invariants. A full class-partition with 55/451 quotients and witnesses gives reusable exact test cases for colour-refinement implementations, common-equitable-partition algorithms and C^2 expressivity, not merely a textbook illustration that regular tournaments collide. The classification is complete for orders<=7, non-implied as a tabulation by the inspected prior identification theorem, and its exact group sizes distinguish the first nonregular two-cell phenomenon from regularity-only ambiguity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
