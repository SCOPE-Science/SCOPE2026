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

For d≥2 and any convex (d−1)-base K at its Santaló point, horizontal polar sections of F_a(K)-(0,t) are min(1+ts,(1−(1−t)s)/a) K°; integrating across s*=b/(1−bt) yields vol(K°)/[d t(1−t)(1−bt)^{d−1}], including the a=0 limit. The horizontal first polar moment vanishes because centroid K°=0; derivative of log polar volume has unique zero satisfying (d+1)b t²−(2+db)t+1=0 and positive second derivative. Height density (1−bz)^{d−1} has normalized mixture of Beta(1,k+1) laws; their variance decomposition proves Q(g)=b[(d+2)Var Z−g(1−g)]>0 for 0<a<1, giving t<g and endpoints equality. Volume slicing gives factor Pi_d=Pi_(d-1)*Φ_d; envelope differentiation gives d logΦ/da=(d−1)(E[Z/(1−bZ)]−t/(1−bt))>0 by Jensen and g>t. Fresh SymPy exact independent verification of centroid identities for d=2..9; checked limits d=2, a=0/1 and non-symmetric base logic. Finite dimensions are diagnostic, general proof is the analytic beta-mixture.

## originality

PASS

Best-of-knowledge statement-level comparison of original claim, aliases and stronger coverage: The new statement requires polar integrations, a quadratic root and strict mixture variance/Jensen argument beyond prior endpoint/classical geometric characterizations.

## value

PASS

A base-shape-independent Santaló center and strictly monotone Mahler factor for every homothetic frustum is a motivated interpolation between two classical convex-geometric extremal constructions. Strict centroid separation and all-base shape independence extend beyond the known pyramid endpoint and general computational polar-volume procedures.

The dated certificate retains the supplied scientific assessment, sources and limitations.
