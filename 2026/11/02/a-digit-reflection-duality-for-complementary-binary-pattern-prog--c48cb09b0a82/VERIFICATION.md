---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For every mixed binary word v of length m and every L>=m+1 and n<2^(L-m), padding binary n with >=m zeros preserves overlapping occurrences of v. Bitwise complement turns its L-bit padded representation into the ordinary binary representation of y=2^L-1-n; prepending prescribed initial zeros for complement pattern adds exactly delta(complement(v)) occurrences independent of n, where delta is one only for 0^a1^(m-a), 1<=a<m. Thus exact integral count identity e_barv(y)=e_v(n)+delta(barv). For each arbitrary finite monochromatic arithmetic progression of difference d, choose L large and reverse its members under y=2^L-1-x; reflected sequence has same common difference and colors shifted by the same parity. Converse by complement proves equal suprema A_v(d)=A_barv(d) for every d>=1, including infinite suprema. Independent direct occurrence counts for mixed lengths 2..6 and several starts/steps corroborated exact identities; the arbitrary-length reflection argument proves the full claim.

## originality

PASS

The exact statement appears as an open mixed-pattern question (Problem 4) in Sobolewski 2022, where equalities were observed for short patterns only. The new universal integral reflection with constant correction and consequent equality for every difference is not provided in the inspected primary source. Other block-counting and automatic-sequence studies ask different questions.

## value

PASS

Answers an explicitly posed natural research problem for all mixed binary patterns and positive arithmetic progression differences; the exact occurrence-count reversal is a stronger structural duality than merely the maximal-run length equality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
