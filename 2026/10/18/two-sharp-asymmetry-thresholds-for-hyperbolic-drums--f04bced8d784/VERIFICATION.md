---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Reconstructed the geometry in hyperboloid coordinates: at a ridge the spatial transverse radius is s sin α, hence its circumference is 2πs sin α and its face has intrinsic radius ρ with sinh ρ=s sin α. The plane is X₃=(s/c)cos α X₀. The outward unit sphere and plane normals have dot product cos α/√(1+s²sin²α), giving exterior angle arctan(c tan α). The spherical belt has smooth mean curvature 2c/s, the disks zero, so the area and curvature split into the two claimed one-side contributions. A′<0 parameterizes the entire nearby fixed-total-area slice by x±h, with quadratic coefficient m″(x). In the shallow expansion the α² terms cancel and the numerator of the inverse second derivative first has coefficient 48(b₆a₄−b₄a₆)α⁷ in units of 2π; the α⁹ in the denominator yields the stated α⁻² law with its correct 2π factor. In u=cos α at the deep endpoint, A′=2πs² is nonzero; B″=−π²s and A″=−2πs²/c give the second stated limit. Independent representative coefficient-sign comparisons agree, but the endpoint expansions prove the sign intervals. The two critical radii are strictly ordered, the vanishing leading coefficients there are not assigned strict signs, and no unrestricted variation or global minimum is inferred.

## originality

PASS

The common-angle geometry and functionals come directly from Hong. The supported distinction is the exact pair of endpoint coefficients and opposite strict fixed-parent-radius, fixed-area antisymmetric local signs in the intermediate band. The strongest matched two-cut result analyzes an adjustable radius near a specified area, not these two endpoints at fixed radius; the other sharp onset result imposes symmetry. No inspected statement covers the pair of frozen endpoint laws, and the bounded search does not certify priority.

## value

PASS

For a natural restricted family used in a geometric extremal problem, balance switches from locally minimizing to locally maximizing under precisely the same area constraint as the cuts deepen. The two exact and unequal endpoint radii explain that failure of a single universal symmetry heuristic without overclaiming global minimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
