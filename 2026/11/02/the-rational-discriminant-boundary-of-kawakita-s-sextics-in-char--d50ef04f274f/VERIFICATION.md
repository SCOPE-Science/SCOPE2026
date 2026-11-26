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

Writing A=a+b and B=b−a, the quotient cubic becomes Awt²+Bs³+As²t+bst²+t³. It is primitive and linear in w because A and B are nonzero, and its gradient forces its only singularity to be s=t=0. At that point the double tangent has contact three; completing the square in the formal local quadratic reduces the equation to a square equal to s³ times a unit, an ordinary cusp also in characteristic three. Squaring is étale off the axes, so this gives precisely four cusps there. The axis cubic f(v)=v³+av²+bv+1 has f′(v)=b−av and a³f(b/a)=−D. Here ab≠0, the quadratic coefficient at the root is a≠0, and the remaining root is simple and nonzero. At each double contact the quadratic part of the pullback is (a+b)³X²/a²+b(Y−Y₀)², a pair of distinct lines since both coefficients are nonzero. There are two such points per axis; at simple intersections the along-axis derivative is nonzero. The simple intersections on U=0 and V=0 give independent valuation parities for U/W and V/W. Thus the generic pullback is a degree-four field, and finite flatness of squaring (two monic square-root equations on each target chart) implies integrality of the pullback itself. On the normalized cubic only the three simple intersections ramify, with inertia two, including the common odd poles on W=0; Riemann–Hurwitz gives 2g−2=−8+6=−2. This agrees with the sextic genus defect of ten. The displayed cubic for the witness has no F₃ root and avoids the excluded values.

## originality

PASS

Credit the earlier same-family characteristic-three analysis for the cubic quotient, four cusps, the axis discriminant and the Kummer method on D≠0. The contribution supported here is the contrasting complete D=0 stratum with a+b and a−b nonzero: exact double contacts, six new nodes and rational normalization, including integrality at the degeneration. The inspected open-stratum theorem excludes the boundary, and the located literature works in characteristic at least five or on the excluded symmetric Wiman family.

## value

PASS

This is the axis-contact discriminant singled out by the earlier open-locus study of a published family, not an arbitrary parameter slice. It gives the exact geometric nature of the first excluded degeneration: six nodal identifications are added to the four cusps, integrality persists and the normalization drops from genus six to zero. These data matter for the geometry of the family and cannot be inferred just from the degree or the existence of the discriminant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
