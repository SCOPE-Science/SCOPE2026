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

# Verification

The finite checker can be compiled and run using `c++ -O3 -std=c++17 checker.cpp -o checker && ./checker` in the directory of this package. It enumerates all unordered row and column three-point subsets of the nine- and twenty-five-point character tables. Its determinant route computes the six signed permutations as coefficients of powers of a primitive prime root, reducing exactly modulo the cyclotomic polynomial; a separate two-by-two minor route determines rank one. Separately coded proportionality and geometric predicates are cross-checked on each pair.

Expected outcomes are:

```
CHECK_PASS p=3 triples=84 collinear=12 rank1=36 rank2=1296 rank3=5724 exact_cyclotomic=true geometry=true
CHECK_PASS p=5 triples=2300 collinear=300 rank1=15000 rank2=600000 rank3=4675000 exact_cyclotomic=true geometry=true
```

These computations cover all 7,056 and 5,290,000 ordered pairs of unordered three-element supports respectively. They do not prove the universal quantifier over all primes. That follows from the unit-modulus determinant lemma, the geometric characterization of proportional Fourier rows or columns, and exact finite-plane counting in the proof. The source comparisons concern different cyclic groups, Hamming-number extremal problems, and support uncertainty bounds; an older equivalent theorem remains possible.
