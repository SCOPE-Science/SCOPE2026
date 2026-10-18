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

PASS: For n=2^alpha p^beta q^gamma the exact unitary-divisor sum (2^alpha+1)(p^beta+1)(q^gamma+1) and Das's necessary sigma*(n)>=2n yield monotone rational restrictions p=3 or 5. The p=5 branch forces n=70; p=3 yields only 6q^c, 60, and 90. The converse is independently demonstrated by explicit equal-sum partitions of all unitary divisors, and of all proper unitary divisors, in every branch. Independent exact brute subset-partition checks agreed on 1,344 cases for odd p<q in {3,5,7,11,13,17,19} with exponents 1..4. The finite checks are regression tests; the symbolic bounds prove all primes/exponents. Boundary alpha=1 and c>=1 are covered.

## originality

PASS

PASS (qualified): The complete if-and-only-if three-prime-support classification and consequent exact slice of Das's conjecture are not stated in the materially inspected complete 2024 Das paper. Its existing coprime-multiplication Proposition 2.3 ALREADY implies the 6q^c sufficient family from 6, and the exceptions 60/70/90 appear as examples; these parts are NOT counted as new independently. Das Proposition 2.7 gives weaker necessary prime restrictions and does not force exact exponent classification. Novelty attaches to exhaustive necessity plus simultaneous half-Zumkeller conclusion, best-of-knowledge only.

## value

PASS

PASS: A natural complete classification for exactly three prime supports closes a question specifically left open after the two-prime work and proves the conjectured implication on this entire arithmetically motivated infinite stratum. The exclusion of every other prime-power shape is substantive, rather than a generic table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
