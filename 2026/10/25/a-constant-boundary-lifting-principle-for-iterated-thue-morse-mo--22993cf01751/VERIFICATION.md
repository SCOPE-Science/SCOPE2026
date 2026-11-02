---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For length-2^k Thue–Morse blocks μ^k(0), μ^k(1), every internal length≥2 factor admits an occurrence crossing the central boundary in μ^k(pq) for one of four ordered pq: induction decomposes a μ^(k+1) block into two μ^k blocks; either the factor crosses their boundary or the k-induction relocates it to some k-block pair, and all pairs occur as the central two k-blocks in μ^(k+1)(cd) because (1−c,d) ranges over {00,01,10,11}. A factor spanning >=2 inflated source letters can be copied from its minimal seed-block span to an occurrence of that seed span strictly crossing a marked cut, so it spans 2^k b. A factor inside one inflated letter is handled by the universal middle-pair property plus each marked adjacent pair type. Both singleton symbols occur among the last symbols of the left inflated marked blocks. For k=0 the internal-block case is empty. Independent exhaustive strict-cut condition and factor-attractor checks passed for seed 00110 to k=3 and for 01101001100101 B={3,6,8,11} to k=2. Finite checks alone do not establish all k.

## originality

PASS

Best-of-knowledge qualified PASS for a sufficient marked-cut lifting criterion quantified over every finite binary seed and every nonnegative iteration. Banbara et al. extended primary text and its 720-state tmfa4 automaton classify four-position attractors of prefixes of one fixed Thue–Morse infinite word, and Faro–Marino–Pavone treat canonical finite Thue–Morse words with 24/16 coverage constraints. These cover motivating fixed-point examples, but not all independent arbitrary seeds. Equivalent general morphism-block lifting lemmas or constructions may exist unindexed. No exact all-seed theorem located.

## value

PASS

A concrete structural invariant of a seed—four marked adjacent pair types and strict two-endpoint factor crossing—certifies a fixed-size attracting position set for an infinite hierarchy of iterated morphic images. It is not simply an attractor-size restatement: the strict crossing rule is essential to reuse every internal boundary, and checking the seed is finite. The theorem supplies a uniform independent-seed upper-bound mechanism, without claiming optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
