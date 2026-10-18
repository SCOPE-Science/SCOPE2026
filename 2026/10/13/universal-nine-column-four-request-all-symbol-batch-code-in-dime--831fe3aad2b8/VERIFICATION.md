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

At the frozen nine-column rank-four integer generator, a fresh independent JavaScript verifier checked all 45 primitive disjoint signed integer recovery bundles (nine quadruple repeats and 36 two-pair requests) and explicitly all 495 four-request multisets, totaling 540 successful bundles / 2160 exact integer identities. Four-request partitions 4,3+1,2+2,2+1+1,1+1+1 reduce to those checks; for 3+1 and 2+1+1, at most one or two of four disjoint repeated-symbol recovery sets meet the singles, leaving enough disjoint sets. Integer equations hold in every characteristic, including odd fields. The identity block ensures rank 4. Boruchovsky et al. Proposition 18 gives ASP(4,3,q)=8, and Proposition 10(iii) strictly increases minimal length with requests, so lower bound 9. Theorem 23/Proposition 24 locate the previous gap. Checked complete certificates.json Git blob 2277f051f2e3c4d17c07dc75e35959fd01490079; evidence is exact, not field sampling.

## originality

PASS

Best-of-knowledge PASS specifically for universal odd-characteristic four-request recovery of the nine-column known single-parity design; matrix construction and characteristic-two optimum and 9 lower bound are explicitly prior.

## value

PASS

Closes a natural exact finite coding-theory parameter gap uniformly over finite-field characteristic. A complete all-symbol four-request recovery certificate for the optimal length nine is a motivated, reusable exact fact; the finite case is neither arbitrary nor merely a recomputation of a known bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
