---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Odd G-Lehmer numbers are squarefree: a repeated prime divides Φ(n) but not n±1. For each distinct odd prime u, the ratio (u−β(u))/u is at least 4/5; for three primes this gives Φ≥64n/125. Since n≥105, F≤n+1<128n/125≤2Φ, so a positive integer quotient is necessarily 1. Multiplying the equality by the product of the signs and putting x_i=β(p_i)p_i gives ∏(x_i−1)=∏x_i−1; expansion gives the pairwise sum equal to the single sum. With all positive x_i≥5 the pairwise sum is larger, and with all negative x_i it is positive while the single sum is negative. For the two mixed cases, completing the product gives the displayed (q−t−1)(r−t−1)=t²+t+1 and (p−s+1)(q−s+1)=s²−s+1. The right sides are positive. If both factors were negative, the lower bounds 5 on the positive-residue primes and 3 on the negative-residue primes bound the product by (t−4)² or (s−4)² respectively; in the first case such a negative-factor pair already requires t>4. These bounds are strictly less than the right sides. Ordering the positive distinct factors accounts for uniqueness; substitution back gives both converses, and the residue classes make the distinguished prime distinct. The published semiprime result covers two primes (also the same ratio bound with exponent two works for n≥15); no composite odd one-prime case survives squarefreeness. My smallest-prime-factor sieve factored odd n rather than looping over the frozen three-prime tuples. Among 635,805 integers with three distinct prime factors and no multiplicities up to 5,000,000, precisely the seven reported values passed the direct divisibility test and each had quotient 1. The proof, not the finite sweep, proves the parametrization.

## originality

PASS

The Gaussian Euler product law, the odd two-prime classification and the known equality examples are prior. On the inspected evidence the distinct contribution is the exact odd three-prime classification, including the necessary equality, exclusion of two same-sign patterns, and two reversible divisor parametrizations. The brief support bound is a corollary, not a sharp general sieve barrier.

## value

PASS

This is the first support layer beyond the published twin-prime case in the inspected classification, directly tied to the explicit proper-divisor question. Its main value is not the easy quotient bound alone (counting distinct positive-residue primes strengthens that coarse bound even at four primes). The two reversible families turn a global divisibility search in three primes into a divisor enumeration of one quadratic integer for each distinguished prime, and identify the exact admissible residue patterns. A researcher studying this equality sequence or attempting a higher-support search can use that structural description and recover every low-support member, not just a bounded list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
