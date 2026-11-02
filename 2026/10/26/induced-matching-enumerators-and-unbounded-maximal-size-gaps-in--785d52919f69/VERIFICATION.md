---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For 2<=p<=q, the assignment-to-incidence bijection requires distinct original tails and heads not among tails. For a tails-on-both-sides configuration, inclusion maximality is exactly surjectivity onto both unused original-side vertex sets, contributing (p-a)!S(b,p-a)(q-b)!S(a,q-b). All-one-side boundary configurations contribute q^p z^p and p^q z^q. The a+b spectrum from the surjection existence inequalities is {p} union {q,...,p+q-2}; largest induced size same upper bound. Independently brute-force adjacency subset enumeration agrees for six cases, including p=q=2 and p=2,q=5; arbitrary p,q follow the bijection and inequalities, not enumeration.

## originality

PASS

A prior same-graph paper (Pippenger 2001) was actively found and inspected; it counts ordinary matchings, not induced matchings. Broad earlier extremal graph bounds do not imply the exact maximal-induced polynomial. No exact coefficientwise equivalent was located in primary/main corpus searches; best-of-knowledge PASS, not certified novelty.

## value

PASS

An exact cardinality distribution of maximal induced matchings and unbounded forbidden cardinality intervals in connected bipartite graphs of girth eight provide a natural extremal/structural phenomenon; the two independent surjection constraints explain it. This is not merely reparameterizing a prior total matching count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
