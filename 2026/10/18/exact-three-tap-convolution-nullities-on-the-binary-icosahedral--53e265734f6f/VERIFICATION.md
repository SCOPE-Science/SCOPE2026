---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

Run `g++ -O2 -std=c++17 check.cpp -o check && ./check` with a C++17 compiler and Boost multiprecision headers. The checker enumerates the 120 determinant-one 2-by-2 matrices modulo five, builds the multiplication/inversion/conjugation tables, and exhausts all 7,021 identity-normalized unordered supports in 62 disjoint orbits. For every orbit representative it performs four-prime exact elimination on the 120-by-120 three-ones-per-row regular matrix. The four primes are trial-division primality-checked; their product is compared using arbitrary-precision integers against the universal Hadamard bound. The code asserts the 35-signature completeness, all nine nullity-count entries, 280,840 total supports, the 22-nullity signature, and the sharp 80-nullity signature.

The complete checker was compiled with GNU C++ 14.2.0 and executed successfully; stdout began with `PASS group=SL(2,5), normalized_pairs=7021, conjugation/rebasing_orbits=62, distinct_order_signatures=35`. No floating-point extrapolation is used. A finite exact proof of this group's census does not settle other groups, nonunit weights, or external priority questions.
