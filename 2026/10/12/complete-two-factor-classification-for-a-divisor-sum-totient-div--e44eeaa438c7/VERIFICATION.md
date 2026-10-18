---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Prime-square exclusion follows from gcd(p,p²+p+1)=1 and p²+p+1>p−1. For p<q, p=2 forces q+1|4, hence q=3. For odd p,q, set m=(q+1)/2|p(p−1). If p∤m then m=p−1 and integrality forces p+1|15, impossible as even≥4. If p|m, put m=pa and p−1=ab: exact rearrangement gives ab+2 | b−4a−6. The positive and zero cases fail (zero gives composite q), and with 4a+6−b=t(ab+2), cases t≥3,1 give even p or composite q; t=2 forces b=2 and q=p²−p−1. Substituting that prime q gives integer ratio q(p−2). Independently generated prime factorizations and checked 210035 Ω=2 integers up to 10^6; exactly 13 hits 6,15,95,287,1199,4607,23519,28799,101567,223199,296207,352799,903167 obey the formula. Infinite proof does not depend on finite sieve.

## originality

PASS

OEIS A066995 is the exact divisibility sequence, but is a list/program rather than a structural two-prime layer classification. A011775 reverses the divisibility and cannot imply this restriction. De Koninck–Luca study composition σ(φ(n))/φ(σ(n)), not σ(n)|nφ(n). No accessible stronger published classification was found through actual semantic and arithmetic searches; unindexed elementary number theory remains a residual risk.

## value

PASS

The Ω=2 layer is the first nontrivial prime-factor-complexity slice of a long-indexed arithmetic divisibility sequence. Its exact prime-polynomial characterization and square exclusion are reusable natural arithmetic facts, separating effective membership classification from unresolved primality infinitude.

The dated certificate retains the supplied scientific assessment, sources and limitations.
