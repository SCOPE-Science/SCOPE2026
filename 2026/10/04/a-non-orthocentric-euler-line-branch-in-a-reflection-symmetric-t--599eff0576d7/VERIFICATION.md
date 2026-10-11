---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

Facet areas give the claimed incenter, and direct equidistance gives the circumcenter. The two-dimensional collinearity determinant factors as \((p-h)Q\). Fresh symbolic reconstruction verified the squared identity reducing \(Q=0\) to \((p+h)^2=4ph(ph+2)^2/(5ph+6)\); the discriminant is nonnegative exactly from \(ph\ge2\), while the unsquared left side is then positive, so no extraneous solutions survive. For \(ph=3\), the exact branch has discriminant \(16/7\) and the sign term \(110/7>0\); the displayed \((\sqrt7,3/\sqrt7)\) center relation and nonorthogonality test are exact. The edge-length pattern excludes both biregular partition types.

## originality

PASS

Best-of-knowledge originality passes. Hajja--Martini explicitly say the nonorthocentric analogue of the incenter-on-Euler-line theorem is open, while the classical Edmonds--Hajja--Martini theorem covers only orthocentric simplices. The audited family contains a certified nonorthocentric example, so that theorem cannot imply it. Resultary found no older equivalent family classification.

## value

PASS

The family is a simple symmetry-reduced but genuinely two-parameter test bed for a published center-characterization problem. Its complete algebraic classification and continuous nonorthocentric branch show that the known orthocentric/biregular picture is not exhaustive, providing a meaningful structural boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
