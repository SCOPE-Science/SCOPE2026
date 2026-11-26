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

Rampersad's p(n) convention is the same suffix-comparability definition, including p(0)=1. The digit order and six-dimensional representation match the published formula, and vM₀=v handles zero and leading zeros. Independently recovered the seven exact columns starting from (M₀+M₁−2I)w and checking M₀/M₁ closure with constant −1; state output is first coordinate minus one. The even transition in state 1 switches to state 3, whose sequence is complementary to state 1 on positive n (opposite at odd n, swap the roles and halve at positive even n). State 5 is complementary to state 2 including zero (even outputs are opposite, odd branches swap). Thus a(0)=b(0)=0 and the parity recurrences, including the a(2n) exception at n=0, are valid. Summing them gives the stated discrepancy recurrences; the magnitude increments for e_A and e_B are at most 4 and 1 per digit, respectively, with base n=1. At 2m, 3Q(2m)−2m=e_A(m)+e_B(m); at 2m+1 add 3a(m)−1, of magnitude at most 2, within the one extra digit's allowance. The n=1 case is direct. This proves the 5L/3 scale bound via P(2n)−2P(n)=n+Q(n). At 2^km the errors sum as Σ(L(m)+j)/(2^jm), giving O(log(m+1)/m) uniformly in k. Bracket large n between 2^km and 2^k(m+1) with m comparable to log n; Rampersad's O(log m) upper bound yields the O(log log n) term at both endpoints. Monotonicity of P interpolates, and replacing either endpoint denominator by n costs O(log n/m)=O(1). Replay /workspace/branches/period-doubling-increments-check.py independently recovered the closure, checked 257 direct local periods using the 2-adic word formula, and checked 4096 scale discrepancies. The frozen certificate and code were read but not run; the proof is infinite conditional on the published representation, not a finite verification of that premise for all n.

## originality

PASS

The dyadic coefficient and the matrix representation are already in Rampersad. The supported distinct contribution is the quantitative one-scale discrepancy for every integer and the resulting all-integer coefficient with the stated error. A subsequence formula and logarithmic bounds do not substitute for this; the general regular-sequence theorem checked here has its spectral boundary at exactly the required eigenvalue, leaving this term uncontrolled by its explicit expansion.

## value

PASS

This determines the missing global leading coefficient of an established complexity function on a canonical automatic word. The prior dyadic coefficient and coarse logarithmic bounds leave open the behavior at general lengths; a useful all-integer discrepancy estimate and an explicit error resolve that gap. No claim is made about the sharp second-order remainder.

The dated certificate retains the supplied scientific assessment, sources and limitations.
