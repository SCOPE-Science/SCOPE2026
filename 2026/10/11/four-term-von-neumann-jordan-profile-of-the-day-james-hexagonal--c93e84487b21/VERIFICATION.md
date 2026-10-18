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

The exact C''' four-term objective is a positive linear combination of squares of norms of linear transforms in (x,y), hence jointly convex on product of the two closed polyhedral unit balls. Its global maximum can be realized at one of 36 ordered vertex pairs, which all lie on the sphere; the upper bound extends to sphere. Explicit 60-degree rotation, reflection and y-sign invariance split pairs into 12 equal/opposite and 24 distinct orbit pairs. Parallel pairs evaluate 1. Taking x=(1,1), y=(1,0), and 0<=m<=1/2 yields N(mx+(1−m)y)=1, N(mx−(1−m)y)=1−m, N(x−y)=1, N(x+y)=2, so F=1+3m/2−2m², always >=1 on interval. Polynomial derivative 3/2−4m gives unique maximum m=3/8 => 41/32, exactly lambda=3/8,5/8. Independently evaluated 36 pairs at exact rational checkpoints, including both symmetric maximizers, and checked analytic active branches. No statement about other normed planes or complex scalars.

## originality

PASS

Best-of-knowledge statement/implication assessment: The new exact parameter dependence does not follow from the original definition, generic bounds, or another invariant for this same polygon. There is no same-formula independent prior statement observed. Relevant primary exact-object sources and indexed findings were checked by object, invariant and quantifiers; inaccessible plausible material is retained explicitly as risk, not treated as automatic scientific rejection.

## value

PASS

A sharp parameter profile of a newly defined natural four-term Banach-space smoothness/Jordan invariant on the canonical Day–James hexagonal norm gives a geometrically meaningful benchmark: the off-center maximum 41/32 is strictly above the balanced value 5/4. Its exact vertex-orbit reduction and λ-dependence are not routine substitutions of the classical constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
