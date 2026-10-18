---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For all primes p>=17, prove 1+p^-4<product_{q>p}(1-q^-4)^-1 by strict finite rational sums of at most ten next-prime reciprocal fourth powers for all 33,602 p<396738; a fresh sieve to 430000 and exact Python Fraction arithmetic reproduce worst count ten. Dusart Proposition 6.8 proves the necessary small-gap bound for every p>=396738; two successors <101p/100 then suffice. Sanna Lemma 2.3 (combined with tail prime inequalities) gives exactly the tail interval [1,T], not merely sampled values. Exact rational Machin alternating-series pi bounds certify the six exponent thresholds A=(3,2,1,1,1,1); connectivity of each high exponent grid gives 192 closed product blocks. My independent fraction-only construction obtains 140 merged components and 139 strictly positive gaps, first coefficient pair (1,1), last (1558603338253/1440270720000,11033033011/10194124800), exactly matching the real 140-line COMPONENTS.tsv. Infinite claims rest on read published theorems and stated overlap proof, not on finite enumeration.

## originality

PASS

General published finite-interval theorem and recursive algorithm do not print an exact r=4 component count or its 140 endpoint coefficients; exhaustive nontrivial computation of a natural missing exponent is the incremental original result.

## value

PASS

Provides a natural exact topological invariant and full 140-component endpoint classification for the first unreported even reciprocal exponent beyond Sanna’s r=2 example. The substantial certified finite cutoff/merge and exact pairs resolve a meaningful missing point in a studied exponent-dependent component-count family; this is not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
