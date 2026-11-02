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

A first color class either consists of a deleted matching nonedge pair (allowing an exact recursive peel of one crown index), or a full bipartition side, in which case exactly two colors are used. For t pair peels, predecessor constraints a_i<b_j and b_i<a_j for all 1<=i<=t<j describe an exact poset; different ordered pair-index choices yield disjoint permutations. Direct first-two/three vertex decomposition proves L(n,1)=(2n)!/n² and L(n,t)=3L(n−1,t−1); multiplied by n!/(n−t)! ordered choices yields the asserted tail distribution for all n≥2. Independent complete enumeration of all vertex permutations for n=2,3,4 matched counts (2:24), (2:480,3:240), and (2:30240,3:7200,4:2880), respectively. The source C++ verifier was inspected and checks all n≤5 and 28 poset cases through n9; our finite test is not used to prove the recurrence at arbitrary n.

## originality

PASS

The 2016 crown-graph simulation deals with randomly ordered *unbuffered* greedy coloring but its analytic distribution section concerns a buffered algorithm; Ye–Xu–Wang–Zheng–Li 2026 prove only O(1) expected colors/weak upper expectation bound on uniform random crown graphs. Their estimates do not imply individual exact probabilities, linear-extension factor-three recursion, or 40n!3^{n−3} extremal-order counts. Li–Li 2026 address random bipartite inputs rather than an exact fixed crown law.

## value

PASS

Crown graphs are the canonical bipartite Grundy/greedy-coloring gap examples. An explicit complete random-order law and exact rare worst-order count quantitatively explain how random arrival regularizes a worst-case n-color instance; these facts are useful independent exact benchmarks in online-coloring probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
