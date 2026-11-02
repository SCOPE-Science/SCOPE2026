---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Write u=ax+by+cx²+dxy+ey²+fx²y+gxy²+hx²y² and stratify lowest degree. If ab!=0, dim A/(u)=3 and u^4=6a²b² x²y²!=0; degree rank lower bound of L_(u²)>=4 forces (5,3,1). If exactly one linear coefficient nonzero, opposite-square coefficient selects (4,3,2) vs a unit multiple of x or y (3,3,3). For nonzero quadratic Q, rank L_u=2+rank[[d,c],[e,d]], and rank L_(u²)=1_{d²+2ce!=0}. The projective conics d²−ce=0 and d²+2ce=0 are split with q+1 rational points each, intersect at 2(q−1) nonzero affine triples in characteristic>=5; their four strata give exact counts q³ times each conic intersection class. Cubic-only rank2 and quartic-only rank1 complete all cases; counts sum q^8. Independent multiplication-matrix ranks and conic counts checked over F5,F7,F11; finite tests do not extend field quantifier.

## originality

PASS

Best-of-knowledge originality PASS for the exact final theorem, not for foundational known ingredients; source and implication comparisons are below, with named residual risks. Known type support and one representative type do not determine finite-field frequencies of arbitrary nonlinear multipliers. The claimed novelty is not the already-known (3,2,2,1,1) instance, nor generic Lefschetz behavior. A researcher could derive the table from elementary algebra and general theories, but the inspected theorems do not state it as an immediate specialization. The result supplies a reproducible complete frequency law, not a claim that Jordan ranks themselves were previously unknown.

## value

PASS

The exact all-element frequency of Jordan forms in a canonical nine-dimensional Artinian monomial complete intersection is a natural structural census beyond generic strong Lefschetz and an isolated known Jordan partition. It characterizes both generic and exceptional quadratic-discriminant strata over arbitrary finite extension fields and gives exact arithmetic frequencies; the fixed small algebra is motivated by existing Jordan-stratification research.

The dated certificate retains the supplied scientific assessment, sources and limitations.
