---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

The pinned RESULT.md specifies n>=3, t>0, equal diagonal conductance, ordinary degree and only one-vertex marginals. Root-edge marking in the weighted Matrix–Tree cofactor gives Z_n(t;z)=(n−1+t)z[d+(n−1+t)z]^(n−2)(n−2+t+tz), d=n²−3n+1+(2n−1)t. At z=1, d+n−1+t=n(n−2+2t), so the pgf factors with p=(n−1+t)/[n(n−2+2t)] and q=t/(n−2+2t). A derivative in t of the convex expectation equals −(n−2)(n−1)(t−1)EΔ²φ(1+Bin(n−3,p))/[n(n−2+2t)^3]; strict for strictly convex φ and for the leaf-test φ(j)=(2−j)+ since p<1. Its moment deficit equals (n−2)(n−1)(t−1)²/[n²(n−2+2t)²]. Binomial pgf convergence at t_n/n→c∈[0,∞], including ∞, proves the independent limit and 2u e^(−u) leaves. Independently recomputed nine rational weighted-Laplacian cofactors against factorization, at multiple n,t,z. Finite checks corroborate but do not extend the symbolic proof.

## originality

PASS

The novelty-bearing assertions are a whole-family convex-order classification and an order-n fugacity crossover, not the classical weighted determinant formula. The source's identical public Resultary mirror is not an independent earlier discovery. Inspected weighted-degree and unweighted-degree originals do not state or directly specialize to these evaluated K_n,n claims; best-of-knowledge passes with acknowledged priority risk.

## value

PASS

A one-parameter matching perturbation of an extremely symmetric graph has a sharp, nontrivial convex-order and leaf-count extremum at uniform conductance; the order-n conductance window produces a distinctive non-Poisson degree law even with fixed mean. These are natural graph-probability features, not an arbitrary tiny numerical check, and can support weighted tree asymptotic studies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
