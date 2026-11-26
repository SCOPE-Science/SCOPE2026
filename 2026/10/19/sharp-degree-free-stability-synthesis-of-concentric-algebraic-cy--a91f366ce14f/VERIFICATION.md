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

For each a_i>0 the y-division remainder of xP+yQ by y^2+x^2-a_i vanishes at both branches over an open x interval, so both polynomial coefficients are identically zero. The circle factors are pairwise comaximal; H divides xP+yQ. At degree below 2n the quotient can be at most constant, and since H(0) is nonzero and xP+yQ vanishes at the origin that quotient is zero. Then s is preserved and, at a nonstationary circle, the local return map on a radial section is the identity. Degree at most 2n instead leaves a homogeneous linear quotient, including zero. The proposed interpolated field has radial polynomial yH(s) and degree exactly 2n (the radial expression has degree 2n+1). Its angular speed is positive on each prescribed circle since C exceeds the magnitude of its two harmonic coefficients. The radial linearization decouples on the circle; division by the angular velocity converts the exponent to a full angular integral. Rotating the phase, putting R0^2=A^2+B^2 and using integral 1/(C+R0 cos(theta))=2pi/sqrt(C^2-R0^2), the sine-weighted integral is -2pi A/[sqrt(C^2-R0^2)(C+sqrt(C^2-R0^2))], also by continuity if R0=0. This gives the printed log multiplier and sign -epsilon_i for any simple positive squared radii and all choices, including n=1. Multipliers are positive and nonunit, not arbitrary prescribed numerical values. The recorded 1414 finite checks in verify.py were inspected, not rerun; RESULT.md lines 17–59 supply the universal proof.

## originality

PASS

Best-of-current-evidence pass for independently prescribing all qualitative stability choices at exact prescribed concentric radii and the sharp degree, by explicit interpolation. Degree-only attainability is credited to earlier work; the classical degree obstruction is also corroborated by a published citation to Dolov–Pavlyuk. The later Resultary theorem gives strong mathematical coverage, not evidence that the result was known before this frozen record. Neither the two inaccessible older constructions nor the later record's relationship to the frozen result is resolved.

## value

PASS

The natural inverse design gap is whether choosing attraction and repulsion independently costs degree or forces changes to the radii. The interpolation and exact nonunit multiplier calculation answer this without appealing to topological equivalence or prescribing the rest of the phase portrait. The first-harmonic obstruction explains why angular modulation is the useful degree-saving mechanism. This is more than the already known count or degree-only existence, and does not claim arbitrary numerical periods or exclude additional periodic orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
