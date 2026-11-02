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

Established directly from greedy subsequence matching in infinite 0101... that minimal host-prefix length c(u)=|u|+1_{u1=1}+number of equal adjacent letter pairs; this is exact for all binary u and starting-letter boundaries. Every even palindrome is uniquely b1...bh bh...b1, giving exact minimal-cost series t²z³(1+z)/(1-t²(z²+z⁴)); every odd palindrome of length >=3 adds center factor t(1+z²); the two length-one words give tz(1+z). Summing minimal costs and multiplying by (1-z)^-1 yields the stated bivariate generating function. Setting t=1 gives z(1+z)(1+z²)/((1-z)(1-z²-z⁴)); parity splitting and Fibonacci series give P_2m=2F_(m+3)-4, P_(2m+1)=F_(m+5)-4, with P0=0, and growth base sqrt(golden ratio). Independently enumerated every distinct subsequence string for all alternating prefixes N=0..22 and counted literal palindromes; obtained 0,1,2,4,6,9,12,17,22,30,38,51,64,85,106,140,174,229,284,373,462,606,750, agreeing with all Fibonacci cases. Enumeration is finite support, not proof beyond N22.

## originality

PASS

The old Mahalingam-Pandoh paper already tabulated the first ten binary maximum counts (which equal this alternating-family prefix census). These ten values are explicitly not new. Its full paper proves general bounds and exact q>=n/2 maximum, not an all-N alternating binary length-profile rational generating function. Holub-Saari 2009 studies highly palindromic words and scattered palindrome sets; full text inaccessible (including institutional VPN), so equivalent historical closed-form remains a risk. This is best knowledge only.

## value

PASS

This complete all-N and by-length rational generating function for a natural highly structured binary word answers a motivated fixed-two-letter scattered-palindrome counting question. Its parity-resolved exact Fibonacci totals and asymptotic growth differ from all subsequences; it is more than re-tabulating ten published counts and does not assert unproved binary extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
