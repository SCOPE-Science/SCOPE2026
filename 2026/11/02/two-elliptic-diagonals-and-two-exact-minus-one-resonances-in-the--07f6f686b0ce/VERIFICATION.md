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

A period-two chord must be normal at both ends. The curve is simple and centrally symmetric, and its curvature numerator ε(1−3u+6u²) is positive for u=sin²θ, so opposite normals force antipodal impacts. The radial critical-point equation gives exactly two nonaxial lines on the indicated open interval and axial merger at either end. Independently, the arclength chord-length generating function has pure second partials (1−K)/L and mixed partial +1/L at these impacts (oriented tangents are opposite). It gives an equal one-step matrix at both ends in those charts, with rows (K−1,−L) and ((1−(1−K)²)/L,K−1). Its determinant is one, the squared trace formula is tr(M²)=4(1−K)²−2, and when K=1 Cayley–Hamilton gives M²=−I. The rational curvature expression has positive numerator and denominator, with D−(1+u)Q=4u(1−u)(3u+2), giving 0<K<2. K−1 has the stated cubic numerator, whose derivative has exactly one root in (0,1); sign tests establish the two stated brackets. Independent arithmetic reproduced ε≈0.42893701026975975 and 0.83512933523582675. For the axes K=16ε² and 2/ε², both >2 in the open interval. The uploaded checker was inspected, not executed; the bounded independent calculation is in review_checks.py, billiard().

## originality

PASS

Credit the exact-family normal-diameter interval and axial traces as background. The supported distinct result is the exact diagonal spectral classification and two exceptional −I matrices. The observed related classifications and standard linearization do not mechanically supply the family-specific positivity and root count. The assessment is provisional on the inaccessible full texts, not a global priority claim.

## value

PASS

The diagonal behavior closes a natural gap in the two-bounce description of the already studied exact billiard family. The specific exceptional parameters mark where a nonresonant elliptic description fails, and identifying the full matrix as −I rather than a parabolic Jordan block is useful for subsequent local analysis. This is value of the exact spectral census, not a claim of nonlinear dynamics or KAM islands.

The dated certificate retains the supplied scientific assessment, sources and limitations.
