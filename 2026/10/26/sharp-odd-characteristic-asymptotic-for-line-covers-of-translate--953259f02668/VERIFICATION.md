---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The affine components are disjoint, there is one common point at infinity, and a line meets each conic in at most two points. For a nonvertical line of slope u through (a,a²+c_i), completing the square gives discriminant (u−2a)²+4(c_i−c_j). The i-th discriminant is a nonzero square exactly when t=u−2a is nonzero. Every nonempty product of the other discriminants has simple roots over the algebraic closure: the offsets are nonzero and distinct and the characteristic is odd. Expanding the square-indicator product, the Weil bound gives the coefficient m−1+2^(−m) in front of √q, with m=ell−1; excluding all zeros and t=0 changes the sum by at most 2m+1. In the 2ell-uniform full-line hypergraph all degrees are therefore D+O_ell(√q) for D=q/2^m, and any pair has codegree at most one. For the covering theorem's fixed gamma and d0, all degrees are positive, within gamma D of D, and <2D, all codegrees are <gamma D, and D≥d0 for large q uniformly in the translates. With accuracy alpha=epsilon this covers the affine points with at most (1+epsilon)q/2 lines; a single vertical line covers infinity and q≥2/epsilon absorbs it. Independent bounded replay `python3 /workspace/review-evidence/independent_finite_checks.py 4` compared the discriminant condition with directly enumerated lines for all two- and three-translate sets in F_9, including triples with zero full degree. That computation is only a check of the local algebra, not an asymptotic cover or an effective threshold.

## originality

PASS

The lower bound and conic family are known; a distinct Resultary record even proves a stronger finite lower bound. The supported contribution is the matching first-order upper bound along all odd prime powers, uniform over fixed-size distinct translate sets, via simultaneous quadratic splitting. No inspected statement supplies that upper bound.

## value

PASS

This resolves the missing asymptotic upper bound for an explicit natural reducible obstruction family. Uniformity over translating constants and odd extension fields is substantive: the argument shows that all components simultaneously support the nearly maximal incidence needed for an asymptotically optimal cover. The result does not claim exact finite covers, a numerical threshold, or an improvement to known lower bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
