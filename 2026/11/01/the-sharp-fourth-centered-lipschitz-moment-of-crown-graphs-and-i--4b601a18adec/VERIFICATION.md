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

For C_n=K_n,n minus a perfect matching with unit graph distances and N=2n, objective N^-1 sum|f-mean f|^4 over Lip(f)<=1 is strictly convex after fixing a constant, so any maximizing point is a vertex of edge-Lipschitz polytope. At a vertex tight edges span a connected graph: all values integral, and A-side values can be translated to {0,1,2}. Each B_i lies in [max_{j!=i} A_j-1,min_{j!=i} A_j+1], and strictly convex one-coordinate optimization forces an endpoint. The source enumerates all cases by A-level counts and outlier endpoints, reducing to three-level signed pattern bound F_N(k,d)=k/N+(d/N)^2(-4+6k/N)-3d^4/N^4 for k<=n and exceptional four-level pattern. Exact maximizers are T_n=1/16+5/n for n3..11 (multiset {0,1^(n-1),2^(n-1),3}) and U_n=1/2-1_{odd}(1/(4n^2)+3/(16n^4)) for n>=12 (balanced 0/2 on one shore, constant1 on other). Equality patterns and threshold n12 follow strict inequalities. Independently recomputed exact rational orbit-reduced endpoint maxima for n3..18 and all branch values, including n11 vs12; finite checks corroborate the all-n case distinction.

## originality

PASS

Best-knowledge PASS: graph spread/variance is second centered moment, and earlier published crown symmetric-edge inradius is equivalent to second-Lipschitz L2 extremum at a different n8 transition; neither determines convex quartic maximum or n12 outlier-to-balanced change.

## value

PASS

The graph crown family has natural deleted matched edges and a well-defined centered Lipschitz moment; its fourth power identifies rare outliers versus balanced shores, a nontrivial optimizer-type transition at 12 pairs not predicted by existing second-moment results. This is a motivated exact entire graph-family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
