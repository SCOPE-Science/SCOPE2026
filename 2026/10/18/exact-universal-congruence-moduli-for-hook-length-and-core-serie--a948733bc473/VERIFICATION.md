---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

PASS: In Z[[x]], A(x) is a unit, so the gcd of F_(t²)-C_t equals that of H=A(x)^(t²)-A(x^t)^t. Frobenius A^p≡A(x^p) mod p and binomial lifting (U≡V mod p^s => U^p≡V^p mod p^(s+1)) establish H≡0 mod p^(a+1) for t=p^a. For N=p^(2a), v_p(binomial(N,j))=2a-v_p(j); all degrees below d=p^(a-1) vanish mod p^(a+2), while [x^d]H≡-p^(a+1) mod p^(a+2), including a=1 and p=2. The degree-one H coefficient excludes primes outside t. For t=p^a m with m>1,p∤m, Frobenius gives first p-nonzero H term at n=p^(2a), coefficient -m² mod p, hence gcd 1. Independent direct finite Euler-product expansion checked t=2,3,4,5,6,8,9,10,12,16,25 through n=40; this is corroboration, not proof.

## originality

PASS

Best-of-knowledge claim-versus-prior assessment with direct source comparisons; see four named checks, source inspections and retained risks.

## value

PASS

PASS: The prime-power exact gcd and sharp first failure degree settle the maximal universal congruence modulus, a natural sharp question explicitly motivated by the new prime-power dichotomy. For a>1, the p^(a+1) strengthening and degree p^(a-1) cutoff are not mere restatements of the cited p^a theorem; nonprime-power part is credited, not claimed novel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
