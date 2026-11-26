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

With Haar probability and ordinary trace characters, Schur orthogonality gives N=|a|²+|b|²+|c|² exactly. I reconstructed the Gram of (χ_V²,χ_V*²,χ_W²,χ_Vχ_V*,χ_Vχ_W,χ_V*χ_W) by Weyl integration: multiply each torus Laurent polynomial by the signed Vandermonde determinant, then take their coefficient dot products in the determinant-one exponent quotient, divided by 24. The diagonal is (2,2,3,2,2,2) and the only nonzero off-diagonal pairs have value 1 between the first two squares and 2 between χ_W² and χ_Vχ_V*. With the factors 2 in mixed expansion terms, this gives precisely the frozen M, including coefficients 2 and 8 in the two phase real parts. Writing x=|a|, y=|b|, z=|c|, S=x²+y² and p=xy, phase alignment gives the upper envelope 2S²+6p²+3z⁴+8z²(S+p). Its increase to p=S/2 is accounted for exactly by (3/2)(x²−y²)²+4z²(x−y)². The final envelope is (51/11)N²−(11/2)(z²−5N/11)². Restoring the two exact phase losses recovers all deficit terms. Equality at N>0 fixes x²=y²=3N/11, z²=5N/11, b/a=±1 and c²/(ab)>0, giving exactly the four projective classes. Each class saturates all losses; the zero function is trivial.

## originality

PASS

The exact fusion inputs are standard and are not credited as new. The strongest inspected sharp theorem replaces the exterior-square character by the trivial character and has a different extremal profile and value. Neither the fundamental-character generating functions nor Haar moment algorithms give the sharp unrestricted complex packet bound, phase classes and coefficient deficit without solving this separate extremal problem.

## value

PASS

The packet consists of all fundamental characters of a natural rank-three compact simple group, not tuned coefficients or an ad hoc character list. The mixed character ratio exceeds that of any pure character and the established two-character subspace, with the sharp deficit pinpointing exactly which fusion couplings enforce a 3:3:5 energy split and four phase classes. This gives an independently useful exact central synthesis estimate, without assuming an all-rank result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
