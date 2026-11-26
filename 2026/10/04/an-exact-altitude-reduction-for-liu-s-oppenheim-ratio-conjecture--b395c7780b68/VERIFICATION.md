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

The prior independent proof check stands, using Liu's sideline convention. With t=h−y>0, the two equal-side lines give r2+r3=2t/sqrt(1+h²). The triangle inequality applied to (1+x,y) and (1−x,y) gives R2+R3≥2sqrt(1+y²), with equality only when x=0 because y>0. Also −2y/R1≥−2y/t, strictly unless x=0. At x=0 the defect has numerator sqrt((1+h²)(1+y²))−h−y over t. Rationalization gives the stated numerator (hy−1)² and positive denominator. Thus equality in the stronger bound is exactly on the altitude; equality in the original inequality is at y=1/h, interior iff h>1. This is the orthocenter since the altitude from B has slope 1/h. Restoring the half-base shows its height is (BC)²/(4h_a). The proof is analytic, not a conclusion from the supplied numerical stress test.

## originality

PASS

Liu's original statement explicitly leaves the equality point on the isosceles altitude unidentified. The comparison found related cyclic-sum refinements and a different optimal symmetric weight, not a covering result for the exact fixed-vertex ratio, its sharp height-dependent defect, and the interior orthocenter equality. The exact catalogue hit is the audited record itself. The pass is limited to this isosceles reduction; it does not credit the conjecture itself or a solution for all triangles.

## value

PASS

The isosceles subclass is motivated by Liu's conjectured equality, not an arbitrary slice. The sharp horizontal minimization gives the exact lower bound at each fixed height and identifies the previously unspecified altitude point as the orthocenter when it is interior. This settles the full symmetric equality regime even though it leaves the scalene case open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
