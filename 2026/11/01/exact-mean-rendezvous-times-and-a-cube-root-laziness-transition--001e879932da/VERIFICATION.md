---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Three transient symmetry states O,A_d,B_d yield the explicit 3x3 substochastic Q in RESULT.md; solving (I-Q)E=1 gives M=1/[2s(1-s)]+[4ab-3(a+b)+2+s(a+b-2)]/[(1-s^2)(a+b+s-1)]. Direct independent symbolic 3x3 inversion agrees for all 1<=a,b<=4; an independent symbolic derivative after z=s/(1-s) equals the stated degree-six P(z) / [2 z² (2z+1)²(tz+t-1)²] over the same grid. For any a,b>=1, its coefficient signs c0,c1,c2<0, c4,c5,c6>0 and free c3 force exactly one positive zero by Descartes, with P(1)>=0 and equality only a=b=1. Uniform O(1) remainder relative to 1/[2s(1-s)]+4H/(1-s²), H=ab/(a+b), gives minimizer scale (16H)^(-1/3) and Mmin=4H+3(H/4)^(1/3)+O(1) when min(a,b)->infty, including unbalanced parts; boundary a=1 yields star optimizer (sqrt3-1)/2. Treat s=0 as infinite meeting due to bipartite parity; s=1 fixed walkers. Finite symbolic tests corroborate only.

## originality

PASS

Ohwa 2015 provides general two-walker first-meeting Markov/Laplace recurrences and star/cycle/complete special cases, not optimized laziness over every K_{a,b}; Kanade et al. address coalescence orders and van Belle–Klimovsky generic spectral representations. The present exact parameter law, uniqueness and uniform cube-root-vs-star boundary are more specialized but nontrivial. The 2023 Warwick mobile-agents thesis full PDF was not read and remains an explicit risk.

## value

PASS

A natural meeting/search optimization on the entire K_{a,b} family with exact rational expectation, a nontrivial unique globally optimal laziness, sharp cube-root scaling when both parts grow and a different constant star limit. Zero holding prevents any opposite-start meeting; fixed one-half holding is first-order 25% slower on balanced bicliques. This is a meaningful exact family classification, not just a general resolvent restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
