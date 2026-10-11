---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

For a depth-u additive-tree pair (a,b), the torus parameters are P=a+b and Q=dP+b, so c=P(dP+b-1). Since P>=u+2 and b>=1, the lower bound is d(u+2)^2, uniquely at (a,b)=(u+1,1). The additive tree has P<=F_{u+3} and a,b<=F_{u+2}; equality in P occurs only in the two consecutive-Fibonacci orientations, and the orientation with maximal b uniquely gives the stated upper knot. Substituting d=n-2u into this pairwise maximum and comparing M_{u+1}-M_u proves balance is optimal, with the sole n=3 tie. Exact enumeration through u<=12,v<=14 and n<=24 agrees but is only corroborative.

## originality

PASS

Originality passes. Lin--Spreer prove the unique positive split and show linear/Fibonacci examples, while the prior SCOPE census counts each component-size fiber exactly. Neither gives crossing-number extrema. The audited theorem optimizes crossing on every binary-tree fiber and then over fixed total canonical size.

## value

PASS

Crossing number is the standard diagram complexity explicitly contrasted with Lin--Spreer's canonical triangulation size. Exact extrema on every canonical fiber and the global fixed-size maximizer give a natural quantitative bridge between the two notions and explain the Fibonacci endpoint sharply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
