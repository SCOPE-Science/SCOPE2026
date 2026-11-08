---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For all integer n>=2, each initially blue A_i has exactly a+1_{i in W_B} white neighbors and blue B_i has b+1_{i in W_A}; the exhaustive cases a=0 or b=0 or singleton white layer with a nonmatched blue forcing witness give a necessary-and-sufficient success condition. Counting the cases yields the all-coefficient zero-forcing polynomial, Z_n(1)=(n+1)2^(n+1)-n^2-6n-1 for n>=3, and minimum count 2n(n-1)+2. Fort constraints classify a,b: singleton-versus-(n-1) sets and two-plus-two sets, with n=2/3 exceptions; combinatorial proof all n. Independent direct full graph simulation/fort inclusion tests for n=2..7 exactly reproduced every reported polynomial and minimal fort histogram (including 44 degree-four forts at n=4). Poisson white-count convergence proves the independent-failure window, not correlated cases.

## originality

PASS

Boyer et al introduce zero forcing polynomials and Cameron et al minimal fort hypergraphs; products of complete graphs have known scalar zero-forcing/failed-forcing values, but inspected source sections do not supply the full polynomial and minimal forts for K_n square K_2 plus its critical failure window. General bounds/scalars cannot fix all polynomial coefficients.

## value

PASS

All-order exact polynomial and minimal-fort hypergraph for a natural graph family (two cliques joined by a perfect matching), and an explicit sharp robustness threshold, give independent combinatorial data for forcing and intervention design. More than a known Z=n deduction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
