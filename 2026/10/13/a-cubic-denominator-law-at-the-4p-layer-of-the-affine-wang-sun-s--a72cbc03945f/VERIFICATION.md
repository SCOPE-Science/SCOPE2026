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

Theorem 5.1 and Remark 5.2 give S_{4p}−C_{4p} integral: only divisors 4 and 4p contribute cotangent blocks, C₄=−2, and the multiplier count for full divisor 4p is one. Splitting the alternating sum by parity gives C_{4p}=2P_{4p}(2p)−P_{4p}(4p). Independently, E_q(t)=((1+it)^q−(1−it)^q)/(2iqt) by its cotangent roots and its constant term, giving the stated e_j. For q=2p or 4p those even-index coefficients have denominators dividing p by e_j=(−1)^{j/2}binom(q−1,j)/(j+1) and the original denominator q; only degrees p−1 and (for 4p) 3p−1 can be exceptional. Factor E=B(1+R/B), where B is p-integral with constant term one and R is the sum of exceptional terms. In degree 4p the coefficients of log B have valuation at least −1: powers of B−1 have p-integral coefficients and the log divisor k is ≤4p<p². Multiplication by −4p makes this part integral. The log(1+R/B) terms of orders 1–3 give valuation at least −2 after −4p; no order ≥5 is possible, and in order four all factors must have degree p−1 in R. The fourth-order sign and −4p give p^3P_{4p}(q) ≡ u_q^4[t^4]B^{−4}=10/9−4/5=14/45 mod p, with u_q≡(−1)^{(p−1)/2}. Thus the same nonzero residue survives in C_{4p} for every prime p≥11, with no other denominator prime by Newton identities. For p=7 an independent exact log-coefficient extraction by integer partitions gives P₂₈(14)=90379872762811458892/49 and P₂₈(28)=34695770991787218624432158970/49; their prescribed combination is the stated C₂₈, with numerator 2 mod 7.

## originality

PASS

The source already gives machinery for exact values at any even modulus, and Liu–Xin also give a general evaluation of the cotangent block. The supported distinction is the uniform reduced denominator law at 4p, with the exceptional cancellation at p=7, not a new general formula for the sums or priority for one computed rational value.

## value

PASS

The next dyadic layer after the published denominator-p theorem is a natural complete family rather than an isolated computation. The p-adic mechanism explains both the generic cubic denominator and the single exceptional drop, answering a uniform arithmetic question not visible in the finite table and useful in analyzing denominator growth for affine Wang–Sun sums.

The dated certificate retains the supplied scientific assessment, sources and limitations.
