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

For n>=3 and odd 3<=m<2^n, setting M=m2^n, h=popcount(m), and greedily writing h in b_i=2^i-1 with coin count c and least occupied index t, the statement F=M^2+(h+c-1)M+(h+c+t-2) follows from the Liu–Xin–Ye–Yin exact Apéry minimum N_{-u}=(M+1)w(u)-u and its greedy-optimality lemma. Check of high digits: greedy high b_{n+j} digits are exactly the binary digits of m; their removal leaves h< b_n. The weighted greedy function w(u) is monotone; b_i-j has constant weight 2^i for 0<=j<i and drops 2 at j=i. Thus w(M-j)=w(M) for 0<=j<t, drops 2 at j=t, and unique maximum of (M+1)w(u)-u is at u=M-t+1. Standard Apéry formula subtracts M+1. Verification is an exact Dijkstra residue-graph calculation on 56 small parameter pairs, not the proof of the infinite theorem; the original published Apéry theorem is a mathematical input.

## originality

PASS

Known all-parameter Apéry/greedy theorem gives an implicit maximum, but does not itself state this closed population-and-plateau formula; earlier Frobenius formula covers restricted m=2^r+1. The extra last-plateau argument is checked independently rather than taking novelty from a different name. Best-of-knowledge priority, not uniqueness certification.

## value

PASS

A universal explicit Frobenius formula and unique extremal Apéry class for all odd Proth parameters, including the previously unevaluated zero-initial-greedy-coefficient branch (e.g., q=63), removes a genuine parameter gap. The popcount dependence compresses a semigroup arithmetic invariant into simple binary data. It is a mathematically motivated complete family calculation, not a mere table of test values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
