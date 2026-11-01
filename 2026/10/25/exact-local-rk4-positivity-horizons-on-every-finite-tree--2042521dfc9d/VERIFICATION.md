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

Let T be any finite simple unweighted tree with >=2 vertices. Exact expansion of R4(-hL) by graph distance gives h p_uv(h) on edges, h^3/6(1-h q(P)/4) for distance-three paths, strictly positive entries for distance two and four when h>0, zero past four, and positive diagonal by a sum-of-squares spectral identity. Edge p_uv=1-(a+b)h/2+[a²+ab+b²+a+b-1]h²/6-C_uv h³/24 with C_uv=(a+b)(a²+b²)+2(a²+ab+b²)-2(a+b)+s_u+s_v. Bound B<=(a+b)² and C>=(a+b)^3/2 force p' negative by negative derivative discriminant and unique positive root. Therefore entire entrywise positivity set is [0,min_uv root(p_uv),min_{length3 path} 4/sum degrees], with no reentry. Independent integer matrix powers on P5, subdivided star, P6, K2 checked all coefficient classes and the distinct first-failure mechanisms.

## originality

PASS

General SSP Runge–Kutta literature gives stability/positivity frameworks, not this exact graph-dependent horizon for arbitrary unweighted trees. The result distinguishes endpoint positivity from stagewise SSP, and identifies precisely edge and three-step path failures, which generic method coefficients do not determine.

## value

PASS

Graph-heat positivity preservation is a standard numerical criterion; a linear-time local exact sharp timestep rule for ALL finite unweighted trees and an exhaustive pair of failure mechanisms is nontrivial and operationally useful beyond a generic graph-independent step bound. It does not claim nonlinear or weighted-tree results.

The dated certificate retains the supplied scientific assessment, sources and limitations.
