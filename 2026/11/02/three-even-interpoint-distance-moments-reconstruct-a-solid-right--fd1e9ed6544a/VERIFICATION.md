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

Recomputed all three moments by expanding Cartesian coordinate differences and multiplying independent one-point mixed moments, without taking the source’s conditional distance powers as input. For powers (2m,2n,j), the one-point moment is R^(2m+2n)H^j times 3/(3+2m+2n+j) times (2m)!(2n)!/[4^(m+n)m!n!(m+n+1)!]; odd planar coordinate powers vanish. The exact expressions agree. The normalized fourth moment has derivative (32/63)(69r−236)/(r+8)^3; the interior minimum, excluded flat limit and excluded needle limit yield the specified preimage counts. In particular the first branch does not contribute at 113/63. At fixed M₁, r=1 and r=1730/227 give different cones with equal M₂. The independent rational substitution into the normalized sixth moment factors with the stated linear factor and positive quadratic, whose discriminant is −887538234128. Thus distinct candidates cannot also share M₃, and recovering R,H from r and M₁ gives global injectivity.

## originality

PASS

The closest theorem has the same three-moment inverse strategy but samples only the cone sidewall. Neither this theorem nor the relevant distance-distribution and width results give the solid-volume moment formulas, the sharp ambiguity thresholds, or the required separation of the two branches for volume sampling. The comparison is bounded, not a priority certificate.

## value

PASS

The inverse problem is natural when only distances rather than coordinates are available. The answer specifies the exact information needed globally: two moments really can give two incompatible solid cones, the ambiguous interval is sharp, and a sixth moment always resolves the choice. This addresses a structural measurement question, not just a catalogue of moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
