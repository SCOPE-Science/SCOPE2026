---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

A fresh GF(2) polynomial/divisor implementation independently enumerated x^n+1 divisors for 3<=n<=15, giving 148 divisors including the 13 zero-dimensional generators and hence exactly 135 positive-dimensional cyclic codes. Independent codeword enumeration reproduced all three headline dimensions, Hamming distances, symbol-pair distances, spectra, and Griesmer values: (8,3,4,6,6) with spectrum A_6=4,A_8=3; (12,5,4,8,8) with A_8=9,A_9=16,A_12=6; (14,3,8,12,12) with A_12=7. The lengths 8,12,14 are not 2^t-1, so the stated non-membership in Luo's two displayed families follows.

## originality

PASS

Luo et al. prove the b-symbol Griesmer bound and construct two distance-optimal families, but the full text inspected does not list these three short cyclic codes. Targeted exact-parameter searches and Resultary produced no prior exact match other than the candidate. The codes are therefore not covered by the two known families and no broader table located in this run subsumed them.

## value

PASS

The three codes are natural extremal objects for the newly established b-symbol Griesmer bound and show explicitly that the two published cyclic/extended-cyclic optimal families are not exhaustive at short lengths. The exhaustive n<=15 cyclic census gives a motivated finite cutoff and reusable constructions rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
