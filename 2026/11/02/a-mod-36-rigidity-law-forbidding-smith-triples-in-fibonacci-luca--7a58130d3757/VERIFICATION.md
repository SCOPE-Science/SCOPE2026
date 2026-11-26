---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For the Fibonacci recurrence matrix Q, the off-diagonal entry is F_n, its trace is L_n, and the off-diagonal entry of (Q^n)^2 is their product. The congruences Q^6=I mod 4 and Q^24=I mod 9 certify complete periods without requiring minimality. Independent recurrence calculation reproduced all 6 and 24 obstruction residues: modulo 4 the entries are 2 exactly at indices 0 and 3 and 3 otherwise, while modulo 9 the table is nowhere zero and hits a multiple of 3 only at 5,13,21, where it equals 3. Hence T_n is nonzero, the displayed valuations of |T_n| are exact, and neither 4 nor 9 divides T_n at any positive n. Complete additivity of P_b, valid even for noncoprime factors, would force equality of the digit sum of F_{2n} with the sum of the other two digit sums if all three were Smith. The digit congruence modulo b-1 would force b-1 to divide T_n. Either 4 or 9 dividing b-1 contradicts the complete-period certificates. The definition excludes noncomposites, including 1, so those indices do not pose exceptional Smith cases. Independent decimal-string recurrence and multiplication confirmed both transcribed factor products, F_827 L_827=F_1654, digit sums 809,802,1592, transcribed factors' sums 809 and 802, and deficit -19.

## originality

PASS

The paper that motivates the problem already gives the doubling identity, additive prime-factor digit sums in the decimal search, and the common Smith index 827. These ingredients and standard modular Fibonacci periodicity are not original. The unsupported-by-prior-formulas remainder is the complete sharp local calculation for the nonlinear product-minus-sum obstruction, which yields a uniform triple exclusion in the stated bases. The inspected sources do not give that exact obstruction law or a stronger statement implying it.

## value

PASS

The product F_n L_n is naturally singled out by the existing even-index Smith search and its known common Smith index, not by choosing an arbitrary recurrence or sampling modulus. The exact low-prime valuations resolve a factorization-free obstruction at all indices, explaining why the common-index phenomenon cannot persist under doubling as a triple, in decimal and uniformly for two base families. That complete restriction is useful in interpreting or extending expensive Smith searches. It is stronger than testing the known example and is not a claim about the rarity or uniqueness of the underlying pair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
