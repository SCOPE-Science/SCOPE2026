---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For n=1 the proper-divisor recurrence gives 2κ(1)=1+κ(1), and for n>1 gives 2κ(n)=1+Σ_{d|n}κ(d). Thus for each fixed finite set of primes, 2F=H+HF in Z[[X1,…,Xr]], H=Π(1−Xj)^(−1), and F=(2Π(1−Xj)−1)^(−1), denominator having constant term 1. With a1=A maximal, Q=Π_{j>1}(1−Xj), coefficient extraction is [X1^A]F=2^A Q^A/(2Q−1)^(A+1). The quotient is integral and mod 2 equals [X2^{a2}…Xr^{ar}]Q^A=Π_{j>1}binom(A,aj) mod 2. Lucas/Frobenius gives oddness iff each aj is a binary submask of A. Includes r=1 and repeated maximal exponents; n=1 deliberately excluded. Independently calculated divisor recurrence on all 780 positive vectors of lengths 1..4 with exponents 1..5: 192 sharp, 588 strict, zero failures. Saved VERIFY_OUTPUT is not treated as universal proof.

## originality

PASS

Best-of-knowledge: the full arbitrary-support binary-submask sharpness locus is not stated in the inspected primary formulas or databases. The Fink lower bound is old and the low-support case is covered, but the uniform first 2-adic digit criterion for all prime supports appears to be a substantive new extraction; significant implicit-prior-formula and inaccessible-primary risks are retained.

## value

PASS

The exponent-normalized κ0(n)/2^A is singled out as a natural open topic in Fink 2023, Section 6 Question 4. The theorem gives a complete exact first-bit/sharpness locus for arbitrary numbers of prime factors, not an unmotivated finite slice or a list of computed values. The exact parity fact could be used to filter signatures before higher-valuation and ordered-factorization investigations; it neither claims new all-value formulas nor settles higher bits. This modest exact invariant survives its two-prime precedent and short formal-power-series proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
