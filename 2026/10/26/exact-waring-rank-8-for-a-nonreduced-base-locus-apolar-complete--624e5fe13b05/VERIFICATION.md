---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Three differential annihilator identities and complete-intersection socle degree 6 verify the apolar ideal. An explicit degree-eight reduced scheme has ideal J=(XY,Y(Y^2-Z^2),X^6+Z^4(Y^2-Z^2)); its generators lie in F^perp by the exact identity X^6+Z^4q_1=Xg+YZ^3q_2+(Z^4-XZ^3)q_1. Leading monomials XY,Y^3,X^6 give eight points, six (zeta,0,1) with zeta^6=1 and two (0,±1,1). For the lower bound, any hypothetical set of <=7 reduced apolar points extends to exactly seven. If no five collinear, cubics separate points by pairing six points into lines avoiding the seventh, degree-four relations force its vanishing ideal into (q_1,q_2), impossible because that base scheme has a doubled point. If five are collinear, the unique containing quadric is reducible q_1 or q_2. Restricting the quartic vanishing ideal to the off-line pair forces only the configuration Y=0, off-line P±, and a quintic separator then forces Z^2 to divide a squarefree binary quintic, contradiction. Direct independent symbolic differentiation and the apolar-generator inclusion identity and eight displayed zeros passed. Finite identities do not replace the universal seven-point geometry argument.

## originality

PASS

Best-of-knowledge exact rank eight not stated by the inspected abstracts or the package-cited Examples 6.1 and 4.1, which report only 4<rank<=8 and non-CI minimal apolar configurations. The closest primary papers were not obtainable in full, so residual risk of stronger later material is explicitly nonzero. Do not mistake abstract-only comparison for full-document NOT_COVERING.

## value

PASS

The exact Waring rank of a specifically cited unresolved sextic is an intrinsic and motivated invariant central to two recent papers about this complete intersection. The lower-bound obstruction for nonreduced quadratic base locus is structural and supplies the precise missing numerical endpoint; a general rank classification is unnecessary for this exact natural example to matter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
