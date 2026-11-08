---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Same-side swaps have unchanged utilities and same-type cross-part swaps cannot strictly benefit both. For i on the a-side and j on the b-side of different types, strict cross-multiplied utility gains are exactly d_i=b r_i-a s_i>b and d_j<-a, and force r_i>=2,s_j>=2 so the swap is legal. After the swap d_i decreases by h=a+b and d_j increases by h. Since d_i-h>-a and d_j+h<b, sign classes cannot reverse. The surplus-ticket ceilings P=sum max(0,ceil((d_c-b)/h)) and deficit tickets Q=sum max(0,ceil((-a-d_c)/h)) therefore both decrement by exactly one; a legal swap exists iff both are positive. All maximal trajectories have T=min(P,Q), an equilibrium iff max d<=b or min d>=-a. Each surplus ticket bounded by r_c-1 and deficit by s_c-1, giving T<=min(a-1,b-1), including a=1/b=1.

## originality

PASS

Best-of-knowledge originality of the precise final claim, not a certification of historical priority: inspected stronger-formulation searches and primary sources do not establish prior coverage of the extra mathematical assertion. Claim-specific comparisons, actual material read and residual risks follow.

## value

PASS

Exact policy-independent improvement duration for a nontrivial strategic dynamics is a natural dynamical invariant: even though terminal equilibria differ, every maximal strict-improvement schedule has the same length, computable in closed form from the initial type profile. The linear bound works on unbalanced bicliques where the usual regular-graph monochromatic-edge potential is not monotone; K_{2,7} gives an explicit decreasing-potential witness. This materially strengthens mere termination or equilibrium existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
