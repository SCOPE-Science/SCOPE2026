---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The Catalan constant term is the central binomial coefficient minus its neighbor; binomial transformation gives CT((1−z)(z⁻¹+1+z)^n). As a check on the recurrence normalization, its ordinary generating function from that transform is F=(1−sqrt((1−3x)/(1+x)))/(2x), which satisfies x(1−2x−3x²)F′+(1−3x²)F=1 and F(0)=1. For N=p^r, coefficientwise Frobenius yields R_N≡1 and R_(N−1)≡k_N mod p, where k_0=0 and k_m=−2 for m≡2 mod 3 and 1 otherwise for m>0. The recurrence denominator N+2 is a unit at every odd p. The bracket is 5 or −4 mod p, so only p=5 and even r require further work. Raising congruent Laurent polynomials mod 5 to the fifth power proves the mod-25 reduction to T(z^(5^(r−1)))^5. The coefficients 51,45,30,15,5,1 give bracket 15 mod 25 for even r, exactly one extra factor of five. This works for all even r≥2; p=3 and r=1 require no exceptional assumption. Independent modular counts of Motzkin paths with level-zero horizontals forbidden reproduced 21 valuations over seven odd primes, including 5²+1 and 5⁴+1. The all-exponent proof is not inferred from these counts.

## originality

PASS

The supported distinct finding is the evaluated uniform exact valuation, especially the sharp even-exponent exception at five. The recurrence and Laurent representation are known, and low-prime slices have closely related known methods. None of the inspected results evaluates the all-odd-prime family with the five-adic exception.

## value

PASS

These indices arise at the prime-power recurrence numerator, not from an arbitrary modulus sweep. Distinguishing a unit bracket from exact first-order cancellation at five provides a sharp classification, including an infinite exceptional branch invisible to mod-p testing alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
