---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

The derivation D_f=f(t)d/dt exists for arbitrary f when N even and requires f_0=0 when odd. Characteristic 2 makes D_f^2 a derivation with D_f^2(t)=ff' mod t^N. If the leading exponent s is odd, square-zero is equivalent to 2s-1>=N; for even s=2j with 4j<N, invertibility of the leading unit reduces to the stated vanishing of odd coefficients in a finite interval. The resulting linear-space family contains exactly all extension-field points; consecutive coordinate support differences give codimension-one intersections, while nonconsecutive ones lie within the predecessor intersection. Therefore the union is reduced support with c noncontained irreducible components and the point formula. The t coefficient of ff' is f_1^2, while the homogeneous quadratic ideal cannot contain nonzero linear f_1, proving a nonzero nilpotent; tangent at zero sees only the optional linear constraint. Independently enumerated every F2 coefficient vector for N=2..12, checked square-zero, union membership and predicted point counts.

## originality

PASS

PASS best-of-knowledge: standard restricted derivation identity is prior; the explicit linear component geometry, hyperplane attachment, nonreduced boundary and all-N finite field count are not supplied by the compared general Witt/nilpotent derivation results.

## value

PASS

The locus is a natural restricted-square fiber of the derivation algebra and its precise component arrangement, intersections, finite-field point count and scheme-theoretic nonreduced boundary are meaningful geometric invariants. Uniform N and characteristic-two counterpoint to smooth/irreducible expectations make the result useful beyond a small census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
