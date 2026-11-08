---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For a compact antilinearly self-adjoint A, Takagi diagonalization yields nonnegative singular sigma_j. With rho=|q|<1, express each unit constrained pair as x=sqrt(b+)u+sqrt(b-)v and y=sqrt(b+)u-sqrt(b-)v with orthonormal u,v and b±=(1±rho)/2; antilinear symmetry cancels mixed bilinear terms. Weighted Ky Fan yields upper b+sigma1+b-sigma2, and explicit vectors sqrt(b+)e1+i sqrt(b-)e2 and sqrt(b+)e1-i sqrt(b-)e2 attain it; the rho=1 endpoint follows by continuity. A two-dimensional isotropic-vector path yields value zero, connectedness of constrained two-frames fills all radial moduli, and phase invariance fills every angle. The strict sigma2>sigma3 gap forces equality frames into top-two Takagi subspace. Independently checked the extremizer and inner-product conjugations symbolically; finite randomized verifier is supplemental.

## originality

PASS

Majumdar–Müller 2026 discusses qualitative disk/annulus shapes for antilinear q-numerical ranges; its accessible abstract/secondary descriptions do not provide a sharp two-singular-value radius, but full Section 6 was inaccessible and might hide the same quantitative formula. Kołaczek–Müller 2024 treats ordinary antilinear numerical range, corresponding only to q=1; complex-linear q-radius results concern different pairing. Classic Takagi+Ky Fan tools make the proof short, yet they are not themselves a previously stated constrained formula. Best-of-knowledge PASS retains a meaningful priority risk, not a whole-document noncoverage assertion.

## value

PASS

The inner-product constraint is intrinsic to current q-numerical range theory, and the exact affine dependence on q with only two singular values supplies a dimension-free quantitative law and gap rigidity beyond qualitative disk geometry. An exact natural operator invariant, not a cosmetic specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
