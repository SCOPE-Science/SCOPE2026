---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For q=p^(2n+1), the rational curve has exactly q affine points P_s and one point P_infty. Every nonvertical rational line intersects affine points in a coset of the kernel of x^{p^2}-a x; for nonzero kernel the gcd(p^2-1,p^(2n+1)-1)=p-1 shows kernel is F_p u, so maximal intersections are precisely affine F_p-line cosets of cardinality p. Every line through P_infty meets at most one affine point. The established minimum is q/p+1. For p>=3, if t>=2 chosen lines pass through infinity, affine incidence cap q+p-(p-1)t<q excludes such a minimum; with exactly one infinity line and q/p other lines, any submaximal ordinary secant would lose >=p-1 incidences that the infinity line cannot repair. If maximal secants left one hole and one double, summing all F_p affine line points (zero for odd p), and comparing with the zero sum of F_q, forces hole=double, contradiction. Thus an affine one-spread plus one arbitrary infinity line is necessary/sufficient. Independent plane switching in q=p^m, m>=3 yields at least (q+1)((q-1)/(p-1)+2^(q/p^2)-2) configurations. For p=2 the q+1 rational points form an arc with no three collinear; minimum covers of (q+2)/2 rational lines are exactly one tangent plus a matching, or solely secants with a unique doubled point, whose counts add to binom(q+2,2)(q-1)!!. The source's q=27 and q=8 checks were inspected; independent combinatorial evaluation q=8 gives binomial(10,2) times 7!! = 45*105 = 4725, matching the total, and q=27 switched spreads yield 19 distinct spread choices hence >=532 covers. All generic claims use the field/geometry proof, not extrapolation from checks.

## originality

PASS

Best-of-knowledge priority after direct comparison of the precise final mathematical statement, known stronger results, equivalent formulations, special cases and searched databases. Prior common premises/corollaries are explicitly excluded from the asserted original contribution; literature completeness is not claimed.

## value

PASS

The original problem asks for fewest rational lines covering a natural nonreflexive Frobenius curve, and the published work gives only the optimum number. This theorem identifies every optimum, makes a sharp p-odd rigidity statement excluding even one affine hole, reveals many non-pencil spreads, and gives an exact binary count through the oval matching structure. The parity-dependent geometry explains minimizers of an independently motivated covering problem. Classical spreads and matching formulas are explicitly attributed; novelty/value is their precise curve-specific extremal classification, not a new spread technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
