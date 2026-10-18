---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For complex V dimension n≥2 and d≥3, τ(v_d(PV)) consists of [ℓ^(d−1)m]. A diagonal one-parameter subgroup with generator weights 1,(d+1),...,(d+1)^(n−1) has distinct weights on all degree-d monomials. A fixed monomial belongs to τ iff its exponent vector has some entry≥d−1; unique factorization leaves exactly n pure powers and n(n−1) ordered mixed x_i^(d−1)x_j, distinct for d≥3, for a total n². Torus Euler localization on the projective tangential variety proves χ_top=n². Independent exhaustive exponent vector enumeration for (n,d)=(2,3),(3,3),(4,5),(5,4) returned 4,9,16,25 fixed monomials, and quadratic d=2 has the separate binomial(n+1,2) count. A further geometric cross-check is the continuous bijective proper map P(V)×P(V)→τ(X) for d≥3, hence a homeomorphism; its χ is n·n. No smoothness is assumed.

## originality

PASS

The exact tangential Veronese projective family was previously studied in detail for defining ideals, coordinate rings, CM and Gorenstein conditions. Their stated topological invariant was not the ordinary Euler characteristic. The n² formula and explicit fixed monomial enumeration were not found as a published theorem; however the already classical bijective factorization parametrization readily implies the Euler value, an especially strong corollary/folklore risk.

## value

PASS

An explicit uniform topological Euler invariant and a sharp degree-two exception for a natural, usually singular, projective tangential family are useful geometry. The formula is simple, and the existing parameterization yields another short proof, limiting its depth; nevertheless it gives a motivated exact invariant rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
