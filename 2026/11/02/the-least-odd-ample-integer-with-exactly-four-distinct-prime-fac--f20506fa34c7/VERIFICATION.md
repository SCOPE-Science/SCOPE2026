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

The divisor lattice of a product of four ordered prime powers is indexed by coordinatewise subvectors, including zeros. Induction on exponent sum gives the same recursive-divisor value under replacement by 3,5,7,11, which can only lower the product and so preserves the strict ample inequality. Thus it is enough to exhaust positive exponents on that support through the attained boundary. Setting the other three coordinates to one and comparing exact powers gives upper bounds (22,15,13,10). Proper subvectors form the union of the nonempty coordinate faces f_i<=e_i-1. Inclusion–exclusion on these faces computes their sum T from earlier prefix sums, including T=0 at the origin. Then A=1+T and its inclusive prefix sum is 1+2T. All predecessor tuples precede the current tuple in lexicographic order. An independently written exact implementation computed all 56672 table vectors, filtered 2757 candidates and returned only (11,5,3,2), product 22975412315625, A=24786437787648. Direct proper-divisor recursion on each of the 864 boundary subvectors agreed. This finite computation is exhaustive after the analytic support and exponent reductions; it does not impose a cutoff on the original odd primes.

## originality

PASS

The function, prime-independence and finite recursion are known or routine and are not credited as new. The distinct assertion is the exact least odd ample integer at support size four. The closest primary result minimizes without that constraint and has a five-prime witness; the closest catalog statements fix three primes. None of these comparisons supplies the four-support answer or bounds that force the reported tuple.

## value

PASS

The number of available odd primes is a natural constraint in the recursive-abundance extremum. Four is immediately below the support size of the known unrestricted odd optimizer and immediately above the studied minimal-support case. Its exact optimum quantifies the cost of removing a support degree of freedom; it is a full unbounded-in-primes extremal statement, not an arbitrary box result. The methods are routine, but the exact threshold does not follow mechanically from the adjacent published optima or an existing table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
