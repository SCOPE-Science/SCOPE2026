---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For every row, three-wise independence gives E(S_n)_r as sum of products of distinct marginal probabilities for r=1,2,3. With sum p_i→1 and max p_i→0 all three factorial moments tend to 1. The identity S³=(S)_3+3(S)_2+S uniformly bounds third ordinary moments; therefore S and S² are uniformly integrable and any weak limit has E Y=1 and E(Y)_2=1. The nonnegative continuous extension max(0,x(x−1)(x−2)) and Portmanteau yield E(Y)_3≤1, not equality. Sufficiency uses ε_n=(a3_n−c)/(n(n−1)(n−2)) at count n, with δ0,δ1,δ2 in the pinned proof; independent SymPy simplification gave exactly zero for mass and mean correction and for the second and third factorial target residuals. Conditional uniform k-subsets then have joint all-one probabilities n^(−r) for r=1,2,3; inclusion–exclusion gives full 3-wise independence. The reference law (5/12,1/4,1/4,1/12) has E=1, E(Y)_2=1, E(Y)_3=1/2. Mixing, truncating and restoring 0/1/2 moments, then diagonalization, covers arbitrary admissible targets without mistaking finite rows for the infinite result.

## originality

PASS

The indexed pairwise weak-limit classification has E Y=λ, Var(Y)≤λ. The k=3 statement is strictly different: variance is fixed at 1 and leakage begins at third factorial order. Ramachandra–Natarajan Corollary 4.2 (inspected in full arXiv PDF) supplies finite-n count-moment feasibility for t-wise independence, but does not state the precise unit-intensity weak closure with third-moment escape or the diagonal constructive sufficiency. A stronger theorem under classical discrete moment or exchangeability terminology remains a residual bibliographic risk.

## value

PASS

The next natural level in the hierarchy of limited-independence rare-event laws is mathematically motivated: it identifies exactly which moment can be lost under weak convergence and characterizes the complete attainable count-law class. The explicit exchangeable realization resolves a nontrivial sufficiency boundary rather than providing a finite-sample table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
