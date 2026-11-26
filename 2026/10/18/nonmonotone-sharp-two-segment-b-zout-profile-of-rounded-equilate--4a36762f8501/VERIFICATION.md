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

Under standard mixed area (the coefficient of st is 2V₂, as used throughout the proof), extrusion by a segment gives V₂(K,L)=length(L) times the normal width divided by two. RESULT.md line 12 contains a notational slip: 'coefficient of 2st' should read 'coefficient of st'; the declared standard convention, explicit identities at lines 31–38 and the rest of the result consistently use the latter. The polar of the difference body of the equilateral triangle is the width-unit hexagon. Maximizing the absolute determinant at its vertices verifies w(u)w(v) ≥ ab|det(u,v)|. The three angular sectors in lines 46–57 give w(u)+w(v) ≥ (a+b)|det(u,v)|, and adding the offset terms proves the sharp product inequality for the rounded body. For positive r equality forces perpendicularity; on the symmetry sector the width product for such a pair is b²[cos(π/6)+cos(2x−π/6)]/2, which is minimized exactly at the two endpoints. At r=0 only attainment, not uniqueness, is needed. Steiner's formula yields the numerator after doubling the area. Differentiation yields Q divided by the squared denominator; the coefficient signs are +,+,−, so exactly one positive turning point exists, followed by strict decrease to π/2. Bounded independent corroboration sampled a 360-direction grid (normals at jπ/360; widths by max minus min vertex projections) for r=0.1, r=r*, and r=100 and found the predicted pairs. Solving Q independently gave r*=13.242673468446 and overshoot 0.002121940607. The grid does not certify global sharpness; the directional proof does. The uploaded script was inspected and not executed.

## originality

PASS

The positive-offset exact area profile, all positive-radius equality directions and consequent overshoot were not established or implied by the strongest inspected statements. The unrounded value, Steiner area law and width/parallelogram reduction are prior ingredients, not new claims. This is a best-of-knowledge judgment, not priority certification.

## value

PASS

Outer rounding tends to a disk after scaling, but the sharp width-normalized segment coefficient takes values strictly greater than its disk limit and then decreases. The explicit family shows that rounding need not give monotonic approach and the uniform equality classification supplies a geometric explanation and an exact optimizer for a natural enclosing problem. The result does not address unrestricted convex tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
