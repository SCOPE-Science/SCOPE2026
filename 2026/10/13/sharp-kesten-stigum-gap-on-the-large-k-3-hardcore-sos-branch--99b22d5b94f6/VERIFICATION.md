---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For k=3 hinge admissibility and x=1, the published large positive boundary-law branch obeys theta=(y^3-y)/(y^4-2), r=y^2>sqrt(2). Multiplying by y^3 yields theta y^3 = r^2(r-1)/(r^2-2) = 2+(r-2)^2(r+1)/(r^2-2)>=2 with equality iff r=2. Published nontrivial eigenvalues satisfy lambda_2=1/(1+theta y^3) and |lambda_1|<lambda_2 for 0<theta<1: clearing positive denominators gives (lambda_2-lambda_1)D(theta t+1)=2theta(theta t+1)^2>0 and plus identity 2(theta t+1)(t(1-theta^2)+theta)>0. So second-largest absolute eigenvalue lambda<=1/3 and 3lambda^2-1<=-2/3; sharp at y=sqrt2,theta=1/sqrt2. Verified factorization and independent parameter arithmetic. KS is sufficient for non-extremality, hence failure does NOT prove extremality.

## originality

PASS

Best-of-knowledge PASS as an exact gap sharpening within the source natural branch: Jahnel–Rozikov derive branch and eigenvalue formulas and rule out Kesten–Stigum only in theta>(sqrt3-1)/8^(1/4), not all theta in (0,1). Khakimov–Makhammadaliev–Rozikov later analyze wand rather than hinge admissibility; Kulske–Rozikov a different SOS model. The submitted sharp all-theta factorization is not a corollary of the earlier coarse sufficient region.

## value

PASS

The hinge model paper devotes substantial analysis to extremality tests. Exact global suppression of its Kesten–Stigum sufficient nonextremality signal on the entire large k=3 branch and the attained sharp margin eliminates a previously unclassified theta interval for that criterion. Narrow but naturally motivated extremality-test phase diagram fact, not a theorem of actual extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
