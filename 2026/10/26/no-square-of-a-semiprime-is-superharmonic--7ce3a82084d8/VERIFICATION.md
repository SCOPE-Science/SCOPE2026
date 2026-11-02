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

The universal cyclotomic-support argument was reconstructed. sigma(p²q²)=Phi_3(p)Phi_3(q), tau=9, Phi_3(t)=t²+t+1. Every prime ell!=3 dividing Phi_3(r) has order 3 of r modulo ell and ell=1 (mod 3), while the exact 3-adic valuation for prime r!=3 is 0 or 1. For p=2, Phi_3(p)=7 forces q=7 but Phi_3(7)=3·19; p=3 forces q=13 but Phi_3(13)=3·61. For p>=5, the q factor in Phi_3(p)=3q^a has a=1 from the size inequality, while p|Phi_3(q) and 3q≡1(mod p) imply 13≡0(mod p): so p=13,q=61, contradicted by Phi_3(61)=3·13·97. These cover all primes; bounded independent divisibility diagnostics corroborate only, not replace, universal proof.

## originality

PASS

Cohen 2008/2009 introduces superharmonicity and Theorem 5 excludes odd squarefree n, which does not cover any p²q². Pollack–Pomerance 2012 Section 5.2 establishes population asymptotics and a stricter prime-deficient analogue, not this sharp exponent pattern. Luca 2004 concerns sigma-prime support contained in rad(n), a stricter condition than support in 3pq; its full text is inaccessible and a possible stronger corollary remains a material risk. No equivalent universal (2,2) exclusion was identified in the targeted mathematical-result queries.

## value

PASS

The two-prime exponent pattern (2,2) is the first genuinely nonsquarefree symmetric core beyond the odd squarefree exclusions in the original superharmonic literature. The theorem rules out an infinite, naturally defined potential odd-superharmonic family, with a short cyclotomic-order obstruction that may be relevant to further small-prime-support classifications. It deliberately does not claim to classify all odd or all two-prime superharmonic numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
