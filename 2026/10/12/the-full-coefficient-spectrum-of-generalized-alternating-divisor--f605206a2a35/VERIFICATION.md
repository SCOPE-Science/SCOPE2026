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

For c_Q(n)=1 iff n has no prime factor in arbitrary fixed Q, finite Q inclusion-exclusion gives F_Q(X)=Σc_Q(n)σ(n)≈(ζ(2)/2)P_QX² with P_Q=∏(1-1/p)(1-1/p²). For Σ_{p∈Q}1/p convergent, bound σ(pm)≤(p+1)σ(m) and ∑_{m≤T}σ(m)≤T² yield uniform omitted-prime tail ≤2X²∑_{p∈Q,p>Y}1/p. For divergent reciprocal sum, squeeze F_Q between 0 and any finite truncation with product→0; obtain o(X²). Hence S_Q/X²→(π²/12)(2P_Q−1) for ALL Q. Greedy odd-prime inclusion with factors f_p→1 and product all odds→0 constructs every P_Q∈[0,1]. Finite odd-only products have odd denominators, even-containing products≤3/8, hence P_Q=1/2 only infinite. Independently checked exact finite factors and coefficient arithmetic. Finite numerical checks are not the infinite proof.

## originality

PASS

Tóth 2017 Theorem 57 establishes finite Q coefficient, and Open Problem 58 explicitly asks about arbitrary Q. Zurita 2020 Theorem 4 retains finite-prime-set hypothesis. New ordinary limits cover arbitrary sparse/dense infinite Q and a complete interval spectrum plus infinite-only cancellation.

## value

PASS

Direct answer to a published open question for an unrestricted natural family of multiplicative sieve sets; describes all attainable limit coefficients and a new zero-main-term phenomenon requiring infinitely many forbidden primes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
