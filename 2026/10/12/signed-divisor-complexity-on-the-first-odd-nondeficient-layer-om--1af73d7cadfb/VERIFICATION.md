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

The sign-flip identity gives ν_-(n)=min{|T|: T consists of distinct nontrivial proper divisors and sum T=(σ(n)−2n)/2}. Odd Ω=5 guarantees nonsquare n, even σ(n) and integral H. Checked abundancy cutoffs: 3 distinct primes force support 3,5,7 and exponent partitions (3,1,1)/(2,2,1); 4 distinct primes with exponents (2,1,1,1) force first two primes 3,5 and top ≤103; 5 distinct primes force squarefree first three 3,5,7 and top ≤383. Fresh INDEPENDENT SymPy integer enumeration over these COMPLETE exponent/prime supports generates precisely 121 numbers, n in [945,442365], and exhaustive exact combinations of proper divisors of cardinality 1..5 yields 17,1,88,0,15, with only ν=2 at 2205 and exactly the listed fifteen ν=5 extremals. No arbitrary n cutoff; finite output is exhaustive by symbolic prime bounds.

## originality

PASS

Ross 2024 formulates the signed-perfect conjecture and gives finite positive examples; Campbell 2026 gives the H(n)-subset sum criterion and infinite counterexamples but not these minimization counts. The published certified ≤10^6 window with ≤7 negatives covers existence on this layer, so this is NOT new as an existence claim; its stated coarse seven-sign witnesses do not imply the exact minimality spectrum and fifteen sharp five-sign cases. Resultary searches did not yield a covering exact table. Subject to risk of an unindexed full minimum-cardinality table, PASS for the complete natural multiplicity-layer classification and enumerated exact extremizers.

## value

PASS

Omega=5 is a natural first possible odd nondeficient prime-factor layer, while the minimum-negative count is the quantitative complexity of signed-divisor representations. A complete finite classification with mathematically proven finite prime bounds, exact spectrum, missing cardinality 4, and all sharp extremizers answers a meaningful unknown invariant beyond a known coarse existence window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
