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

For the directed n-cycle plus n−1->1 shortcut, Boolean path propagation gives F^n>=I OR R: a base length-(n+1) tour can be shortened by a shortcut to advance one position in n steps. Iterating fills any zero gap L by time nL. Counting shortcuts in an nk-step walk (successive shortcuts need >=n−1 edges) shows T>n(L−2) when L>=2. Frobenius semigroup H=<n,n−1> proves unique maximizer e0 with T=(n−1)^2+1 and singleton times t_*-i. The largest zero-run in a uniform n-bit word is (1+o_P(1))log2 n by union bound and disjoint-block lower estimates; tail sums give expectation, and 2n error transfers to T. Independently enumerated all configurations 3<=n<=11 and confirmed uniqueness/bounds, but infinite family is proved analytically.

## originality

PASS

The extremal exponent (n−1)^2+1 and eventual all-one state are classical; not claimed as novelty. The source adds a configuration-specific L-gap comparison with <2n error and exact leading typical n log2 n relaxation for the same maximally slow graph. Jarrah–Laubenbacher–Veliz-Cuba and Gadouleau give general height bounds/periodic structure, not this run-length distribution. Neufeld–Shen 1998 studies maximal generalized exponents by support size but its accessible abstract does not supply a configuration-sensitive zero-gap law; whole text inaccessible (Oxford VPN disconnected), so an implicit implication remains a named risk.

## value

PASS

A canonical primitive extremal graph has quadratic worst-case convergence but its uniform-random starting configurations relax on the sharply smaller n log2 n scale. The uniform two-tour comparison is a motivated structural lemma linking the extremal graph to longest zero runs; its exact coefficient matters for typical Boolean-network convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
