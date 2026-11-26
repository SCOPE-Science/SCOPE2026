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

Evaluation of every degree-four monomial depends only on its nonempty variable support. The 15 distinct support columns form the subset-zeta matrix indexed by nonempty supports and nonzero binary points; triangularity gives rank 15. In each support class, pair one fixed monomial with every other monomial to obtain an independent parity-zero basis of the evaluation kernel, of dimension 20. An independent exhaustive enumeration in four disjoint Gray-code intervals classified all 1,048,576 forms and reproduced exactly 24,192/80,640/20,160 rationally nonsingular forms at image sizes 10/11/12 with no other bins. The gradient encodes a unique plane over F2. For the three-variable plane-filling family the same support argument gives 256 forms. The 24 rationally nonsingular ones all have full homogeneous Jacobian ideal rank 36 in degree 7; hence each seventh coordinate power belongs to the ideal and there are no geometric projective singularities. For smooth S, a section through a rational point of S is singular there exactly when its plane is tangent. No plane is a component of a smooth quartic surface, and the auxiliary lemma precludes singular sections without a rational singularity. Therefore the planes outside the rational Gauss image are exactly the smooth sections. The quartic witness independently has ideal rank 220 in degree 9, vanishes at all 15 rational points, and its only smooth sections have masks 2, 4 and 10. The other 12 sections each have a rational singular point. This verifies both the sharp bound and the broader census under their separate nonsingularity hypotheses.

## originality

PASS

Credit the binary auxiliary plane-filling lemma and its 24-form count to earlier curve classification, and the connection between rational tangency and plane-section singularities to prior work. An already published smooth binary example can also be checked to have exactly three smooth sections. The supported distinct result is the universal sharp lower bound for smooth space-filling binary quartic surfaces together with the exact coordinate-fixed distribution for the larger rationally nonsingular family. No inspected comparable statement or table supplies that bound and census.

## value

PASS

This is the smallest even field omitted by the odd-characteristic space-filling transversality result. The computation is on the natural entire linear system, and its Gauss-image invariant directly measures smooth section scarcity through the plane-filling lemma. The exact histograms and sharp universal guarantee are useful for the binary case regardless of whether the extremizing surface itself was previously described.

The dated certificate retains the supplied scientific assessment, sources and limitations.
