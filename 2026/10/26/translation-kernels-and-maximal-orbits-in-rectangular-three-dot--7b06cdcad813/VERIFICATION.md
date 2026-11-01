---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Verified the finite-field intersection of roots of X^(2^a-1)+1 and (1+X)^(2^b-1)+1 and Frobenius multiplicities, yielding gcd H_g^r, H_g=(X^(2^g-1)+1)/(X+1). Confirmed individual orders L via primitive roots and nilpotent H_g-adic valuation, including r=1 and g=1. The S3 actions lambda->lambda^-1 and lambda->1+lambda constrain semisimple relations; for g>=4 even a polynomial degree bound excludes the exceptional diagonal; for g=2 an explicit H2-adic lowest-term unit argument leaves exactly three. The coefficient-of-highest-degree pairing in F2[X]/H_g^r is nondegenerate, furnishing one faithful-orbit witness rather than an unsupported genericity assumption. Reconstructed 15 bounded independent GF2 kernel/group cases; all-parameter conclusions follow from the polynomial proof.

## originality

PASS

Ledrappier periodic point counts are prior work and Miles–Ward 2015 Example 4.1 treats this same action in the general algebraic Z^d point-count setting. The audited result explicitly does not claim point-count novelty. Inspected source gives the dual system and periodic count, but the exact translation-group kernel for this special rectangular family, exceptional F4 diagonal and exhibited orbit witness were not stated in examined material. Qualified priority risk from Lind 1996 and extraction from general subgroup-count results.

## value

PASS

Provides the explicit full finite group action beyond scalar periodic point counts: exactly which translations act trivially and a maximal orbit realized in each natural Mersenne-power torus, including an exceptional degree-two case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
