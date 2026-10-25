---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For b=0, Q0=r² gives Lie derivative -2r^4; for b=1, Q1=r²-xy is positive definite and L_Q1/(2r^4)=-1+(cos2θ+sin2θ-cos2θ sin2θ)/2<=-1/2 by (1-cos2θ)(1-sin2θ)>=0. For b=2, an independent symbolic differentiation of F2 and the explicit quartic V confirmed V=u2^T A u2, -L_F2 V=u3^T B u3 and leading principal minors A=(33,1833,22352), B=(18,1748,258632,5083552), all positive. Thus the quartic is strict/coercive and proves global asymptotic stability. Any local C² Morse candidate would have positive quadratic leading term Q=r²+d(x²-y²)+2exy. Homogeneity forces D=L_F2 Q<=0 on every direction. D(1,0)=2(1+d+e), D(1,1)=-8(1+d+e) imply d+e=-1; the tangent derivative at (1,0) forces e=d; hence d=e=-1/2, yielding D=8y³(x-y)>0 at (2,1). This contradiction applies to ALL such local C² candidates. All algebraic certificates were independently checked exactly using symbolic polynomials.

## originality

PASS

Best-of-knowledge distinct exact theorem after statement-level comparison: Parameter-specific calculations in a not fully inspected appendix of the original cubic-family paper may cover the b=2 regime; bibliography does not certify priority. Previously known ingredients are credited; no unsuccessful search is treated as novelty proof.

## value

PASS

The result sharply distinguishes the geometry of a Morse nondegenerate Lyapunov minimum from existence of a global strict polynomial Lyapunov certificate in an already motivated planar cubic family. The three-integer boundary b=0,1,2 is structurally minimal under its integral forcing normalization, while the exact rational quartic Gram and local Hessian contradiction show both sides independently. This is a meaningful exact boundary result, not a cheap numerical no-certificate search.

The dated certificate retains the supplied scientific assessment, sources and limitations.
