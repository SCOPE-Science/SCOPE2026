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

Use Python 3, with no nonstandard dependencies:

`python3 verify.py`

The exact-integer program must terminate with:

`VERIFY_OK triple_tuples=17550 quadruple_tuples=80730 integer_triples=3 integer_quadruples=8 prime_quads=3 first_four_pair=630194176 no_smaller_three_pairs=PASS direct_divisor_sums=PASS`

The code separately enumerates every admissible three- and four-subset of the complementary divisor-pair indices for exponents at most \(27\); uses the necessary-and-sufficient rational quotient to find odd integer prime cofactors; checks the complete unsieved and prime-sieved candidate tables; and computes all divisors and their remaining sums directly for each positive four-pair result. Prime testing is deterministic trial division up to the integer square root. The code explicitly checks no one-/two-/three-pair representation of the smallest four-pair example. The proof explains why this enumeration exhausts all cases within the mathematical bounds; the output is not a certificate about larger exponents. Bibliographic precedence was checked with available sources but has not been independently audited.
