---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Reconstructed the divisor convolution series S(n)=sum_{k>=1}2^{-k}prod binom(a_i+k-1,a_i); its recursion agrees with kappa_0, including S(1)=1. For a>=b+2, termwise transfer ratio is 1+(k-1)(a-b-1)/((a+k-1)(b+1)), >1 at every k>=2; strict splitting follows from elementary product inequality. Integer majorization paths give strict lower spike and upper balanced signatures, including coincident endpoints m=r and r=1. Newton finite differences evaluate the series exactly. Independent recursion vs closed form and 63 transfer comparisons through m<=8 support but are not the unrestricted proof.

## originality

PASS

Known Fink series and Newton-difference finite evaluation are not claimed; comparison targets the distinct strict majorization and all fixed-support sharp exponent signatures. Direct full-text primary checks and Resultary semantic retrieval found no implication-equivalent fixed-(m,r) extremal theorem. Priority remains best-of-knowledge.

## value

PASS

Gives a natural complete sharp classification for every prime-factor multiplicity m and distinct-prime support r, with equality cases, not merely a table or an inherited endpoint; strict transfer explains the mechanism. A researcher optimizing recursive divisor counts within support layers needs these exact signatures. Previous formula simplicity limits novelty depth but does not erase this structural order result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
