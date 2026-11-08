---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every h>=1,k>=1, the Fibonacci companion matrix Q satisfies Q^p=-Q^{-1} and Q^(p^2)=Q modulo odd inert primes p=2,3 mod 5; the odd-binomial coefficients of (p+h)^(2k) are even. Therefore F_((p+h)^(2k))=F_((h-1)^(2k)) mod p, while a_1=F_((h+1)^(2k)); their difference is a fixed nonzero integer Delta. Infinitely many inert primes by Dirichlet avoid M*Delta for any fixed M, contradicting the prime-index Dold condition. For h=0, the positive 5-multiplier is supplied by the explicitly credited Moss-Ward Cor.3, and n=5 Dold forces 5|M. The h=1 and index-1 boundaries are handled; 24 inert primes times 40 h,k cases were independently checked, but the infinity assertion rests on proof, not enumeration.

## originality

PASS

Qualified PASS for the positive-translation non-almost-realizability theorem; the h=0 result and multiplier five are prior work, fully credited.

## value

PASS

PASS: A natural and sharp rigidity/instability boundary for almost-realizability under positive translations, with a nontrivial all-multiplier obstruction uniform across infinitely many primes. The h=0 positive theorem is credited rather than repackaged.

The dated certificate retains the supplied scientific assessment, sources and limitations.
