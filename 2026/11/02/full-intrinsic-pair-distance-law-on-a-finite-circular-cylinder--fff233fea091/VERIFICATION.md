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

PASS: On the flat quotient (R/2aZ)x[0,h] with a=pi R, the shortest geodesic between two sampled points has length sqrt(X^2+Y^2), where X is uniform on [0,a] by wrapped angular difference and Y=|H_1-H_2| is independent with density 2(h-y)/h^2. Integrating the triangular conditional probability over X and splitting at B=min(a,sqrt((r^2-h^2)_+)) proves the displayed elementary CDF. The angular cutoff at r=a removes an integral of sqrt(delta-s), producing -4sqrt(2)/(3h sqrt(a)) delta^(3/2); the height cutoff at r=h adds a squared-overrun integral with coefficient +8sqrt(2)/(15 a h^(3/2)) delta^(5/2). At L=sqrt(a^2+h^2), small deficits a-X and h-Y produce triangular tail L^3 eps^3/(3a^2 h^4). Independence gives E[D^2]=a^2/3+h^2/6, E[D^4]=a^4/5+a^2 h^2/9+h^4/15; (L,E[D^2]) reconstruct a,h. The coefficient formulas are local and account for coincident cutoffs a=h. Fresh independent numerical integration for five aspect ratios checked CDF and moments; finite numerical checks do not certify the real-parameter singular expansions.

## originality

PASS

PASS best-of-knowledge: nearby geodesic work provides shortest-path algorithms on periodic surfaces, and random-distance papers treat planar Euclidean domains, spherical bodies or chord distances. No inspected source provides the same exact intrinsically wrapped lateral-cylinder law with its two differing internal singular orders, cubic endpoint tail and inverse recovery; a general formula for flat quotient strips or preexisting geometric-probability tables remains possible priority risk.

## value

PASS

PASS: The complete random intrinsic-distance distribution is a natural observable of a compact, boundary-bearing Riemannian quotient, with distinct C^1/not-C^2 and C^2/not-C^3 threshold behavior, sharp cubic extremal tail and exact recovery of radius/height from the law. Those geometric invariants go beyond a routine shortest-path formula and can support sampling/identification problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
