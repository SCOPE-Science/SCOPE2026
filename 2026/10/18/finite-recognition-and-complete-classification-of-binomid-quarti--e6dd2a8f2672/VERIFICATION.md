---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

The precise universe is nondecreasing (a,b,c,d) of nonnegative integers and monic positive f_n=product(n+a_i). Necessity of the three proposed tests follows at (n,k)=(2,1),(3,1),(4,2). For a sorted prefix j<4, R_j=product_{i<=j}(a_i+2)/(a_i+1)<R_4 and a prospective next t bounds every remaining factor by (t+2)/(t+1); integrality forces R_j((t+2)/(t+1))^(4-j)>=floor(R_j)+1. Strict decrease in t yields rigorous termination of the exact exhaustive rational sieve. Independent exact Fraction enumeration reproduced prefix counts 1,5,21,143,1867; 83 f2/f1-integer cases; eight also satisfying f1|f3; final five after the third test, with three exclusions 1440/7,500/3,98/3. Sufficiency is not merely 80 finite checks: each surviving f_n is a termwise product of powers of n and rising factorial columns, whose generalized coefficients are integral by Shapiro’s Pascal-column theorem and product closure. Nonnegative shifts, positivity and monic normalization are essential; no arbitrary quartic claim.

## originality

PASS

Best-of-knowledge scientific originality after checking statement-level equivalence, stronger coverage, exact-table aliases, prior implications and accessible primary text. Direct mathematical priority risks remain documented.

## value

PASS

Binomid integrality is a natural established arithmetic property. Classifying all nonnegative integer root-shifted quartics across an unbounded four-parameter family settles a concrete gap after degree-two results, and a three-index recognition criterion is a meaningful finite certificate for an otherwise infinite collection of divisibility conditions. The five positive cases alone would be known examples, but the proved global exclusion supplies the mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
