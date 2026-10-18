---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Both divisor sums are multiplicative, with σ*(p^a)=1+p^a, σ^(e)(p^a)=sum_{d|a}p^d. For a=ℓ² this becomes (1+p^a)(1+q)=q(p+p^ℓ+p^a), hence q(p+p^ℓ−1)=p^a+1. Let D=p+p^ℓ−1; if p>2, odd ℓ gives p^a+1 mod D =1−(p−1)^ℓ, a nonzero residue whose absolute value is strictly below D, impossible to divide. For p=2, x^ℓ+1 divides x^(ℓ²)+1 (x=2), and quotient Φ_(2ℓ²)(2) must be prime, with converse immediate. Independently computed small quotient values and primality for ℓ=3,5,7; uniform proof is elementary congruence, not a finite test.

## originality

PASS

The Trudgian paper and OEIS A236474 already list the exponent-49 example. A published Resultary finite theorem handles exponents 2..49, so the example itself and finite checking are not new. The genuine contribution is an unbounded prime-square exponent classification and uniform reduction to one cyclotomic prime candidate for all odd primes ℓ; no prior cited result implies these exponent layers beyond 49.

## value

PASS

The result explains why the largest highlighted known equality example has exponent 49 and isolates a natural infinite subfamily of a published infinitude problem, with precise structural obstruction for all odd p. It does not claim infinitely many cyclotomic primes or settle the full equality problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
