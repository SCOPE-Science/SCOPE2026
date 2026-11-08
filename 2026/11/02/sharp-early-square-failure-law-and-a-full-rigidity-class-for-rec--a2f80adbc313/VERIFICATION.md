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

Use reduced u/v recurrence u_{n+1}=u_n²+v_n², v_{n+1}=u_nv_n; published exact square criterion makes E_j=1 iff gcd(h,u_{j−1})>1. For p^a‖h, relevant starts v_p(x0)=a map bijectively to nonzero t mod p. Local E2: t²+1=0; E3: t⁴+3t²+1=0; disjoint, factor second using i²=−1 and discr −5, giving κ1,κ2. CRT yields A,B,C and four joint probabilities. If p≡13,17 mod20, −5 nonsquare forbids any later preimage reaching ±i; p≡3 mod4 and p=2 are settled directly. Conversely p=5 or 1,9 mod20 gives immediate E3 root with x0=h t0. Independent local roots at primes <400 and CRT sample periods checked; infinite statements rest on number-theoretic argument, not finite tests.

## originality

PASS

Matijasevick–Rodríguez–Salazar 2026 supply recurrence, exact square criterion, and Theorem B bound ≤ω1(h), and explicitly ask failure-count proportions in Section 7; these premises are credited. Their bounds do not imply local κ1/κ2 CRT distribution nor the all-index exact mod-20 forbidden-prime classification, which can force at most one failure even when ω1(h) grows.

## value

PASS

Gives explicit natural densities addressing a concrete question of the primary paper, and a complete infinite arithmetic rigidity classification with arbitrarily many allowable prime divisors but at most one exceptional index.

The dated certificate retains the supplied scientific assessment, sources and limitations.
