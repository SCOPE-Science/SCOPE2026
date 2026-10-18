---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: With a<b<c the Legendre parameter λ=b(c−a)/[c(b−a)] is >1. Exact polynomial identity 256(1−λ+λ²)^3−1728λ²(1−λ)²=64(λ+1)²(λ−2)²(2λ−1)² forces λ=2, equivalent to 2/b=1/a+1/c and ab+bc=2ac. Adding 2n gives an arithmetic progression of the three integral squares. λ²−λ+1 has no rational roots, ruling out j=0 over Q. The family (6s,8s,12s), n=−47s², gives shifted squares s²,25s²,49s². At p≥5 of good reduction, j=1728 nonsquare quadratic twist is isomorphic precisely when p≡3 mod4 since nonsquare d has d² a fourth power exactly then. The quadratic character pairing x↔−x gives trace zero for y²=x³−x at p≡3 mod4 and thus group order p+1. Exact new checker verified factorization and small-prime trace, not infinity.

## originality

PASS

PASS (best of knowledge, limited structural novelty): The closest split-cubic paper gives the λ normalization and explicitly warns about exceptional j and twist equality but leaves its ordered positive locus and arithmetic interpretation unclassified. Standard Legendre j and quartic twist facts are prior; their specific simultaneous application gives an exact exceptional-fiber criterion and an infinite integral D(n) family, thereby interpreting the source finite-field census correctly. The full criterion is near-elementary and could already follow as a routine corollary from literature; no priority certification.

## value

PASS

PASS: The exceptional case is a natural ambiguity in the primary finite-field classification: its exact locus and arithmetic progression characterization explain where nonsquare twists cease distinguishing curves, with explicit nonempty integral witnesses and prime-by-prime consequence. The scientific content is the complete exception handling, not merely a numeric identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
