---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The quadratic trace identity 2Q_n=(1+√2)^n+(1−√2)^n gives Frobenius Q_{ℓm}≡Q_m mod ℓ for odd ℓ. If ℓ divides Q_m, binomial expansion with units and ℓ-adic valuations yields exact lifting v_ℓ(Q_{ℓm})=v_ℓ(Q_m)+1. The smaller odd prime p cannot divide Q_{q^b}: u=α/β in F_{p²} has order dividing p−1 or p+1, hence <q, whereas u^{q^b}=−1 would force u=−1, contradicting α+β=2 mod p; p=2 is excluded by odd parity. Thus only q can divide index gcd, and lifts to full q^b or is absent. Q4=17 and doubling imply G(3*2^a)=1 for a≥2 though entry point 2 divides the index. An independent ordinary exact recurrence/gcd scan confirmed the formula on 1,000+ two-prime-support indices through 1999; universal claim rests on Frobenius/order/lifting proof.

## originality

PASS

Mbirika–Schrader–Spilker (JIS 2023) Section 6.2 Question31 explicitly seeks an index gcd formula and Conjecture32 posits an incorrect rank criterion. Their Theorem28 leaves the gcd unevaluated. The exact two-prime-support dichotomy and infinite counterfamily are not theorems there. Fiebig–Mbirika–Spilker give Lucas period/entry-point results, not the index gcd by support. Classical Lucas identities are ingredients; no identified stronger formula forces the exact all-or-nothing q^b phenomenon without additional argument.

## value

PASS

This is a complete first nontrivial support-level answer to a published Pell index-gcd question and supplies infinitely many concrete counterexamples to its proposed rank-of-apparition equivalence. The smaller-prime exclusion and full larger-prime valuation are genuine structural laws on infinite classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
