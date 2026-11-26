---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Conditional on an open subgraph, the expected component order of a uniform root is the sum of squared component orders divided by n, equivalently one plus 2/n times the sum of unordered-pair connection probabilities. An independent bitset transitive-closure and isomorphism-orbit enumeration (python3 /workspace/branches/independent_checks.py 1) exhausted labeled connected graphs through order 5 and every open-edge state needed. Connected labeled/unlabeled counts were (1,1), (1,1), (4,2), (38,6), (728,21). Only degrees (1,2,2,2,3) and (2,2,2,3,3) have non-singleton groups, each of size two, and the n-times-mean differences up to sign factor as 2 p^3(1-p)(p+5) and 2 p^3(1-p)^2(p+5) respectively. The explicit C4 with a length-two tail and C5 with a leaf are connected, triangle-free and have the stipulated common multiset. Open-edge counts lead to coefficients (0,0,0,2,-18,14,2) for six times their difference, exactly 2 p^3(1-p)(1-8p-p^2). The last factor is strictly decreasing with the stated unique open-interval zero; the endpoints tie. This proves sharpness under homogeneous independent undirected edge percolation and a uniform single seed, not generic stochastic SIR or degree profiles fixed at named vertices.

## originality

PASS

The established observable is not novel; the distinct claim supported here is the sharp order-six threshold, with degree and triangle matching in the witness and a unique explicitly determined crossing. No inspected primary statement or mathematically dominating Resultary entry gave that claim.

## value

PASS

The mean component of a random seed is an intrinsic percolation observable and the degree multiset is a natural control for graph comparisons. The threshold says exactly when ordering can first depend on transmissibility even in equal-degree triangle-free examples, with two explicit graphs and crossing value usable as benchmarks. It does not claim epidemiological applicability outside the independent-edge model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
