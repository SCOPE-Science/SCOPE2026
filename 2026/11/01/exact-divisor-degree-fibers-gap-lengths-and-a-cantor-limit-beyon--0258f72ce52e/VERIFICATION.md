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
# Computational consistency checks

The accompanying `verify.py` is a self-contained Python 3 program using only the standard library. It reconstructs the exact cyclotomic factor-degree multiset \(\{\varphi(m):m\mid 2^a p^b\}\), multiplies the individual polynomial factors \(1+z^{\varphi(m)}\) coefficientwise, and compares the resulting entire degree-counting dictionary to the predicted digit formula. Separate exact-integer assertions check the multiplicity histogram, cardinalities, all sorted gaps and their length histogram, endpoints, exact uniform-divisor digit marginals and total number of divisors.

The executed grid contains 96 triples with \(1\le a\le4\), \(1\le b\le3\), and odd primes selected from \(5,7,11,13,17,19,23,29,31,37\) subject to \(p>2^a+1\). It checked 510728 supported degree coefficients and 34336 actual complement gaps. Its concluding output is:

```text
VERIFY_OK cases=96 represented_degree_coefficients=510728 complement_gaps=34336
```

This is finite numerical corroboration. The coefficient identities, gap formulas, support/measure convergence and their limiting dimensions are proved in `RESULT.md` without relying on enumeration. No external mathematical audit or independent certification is asserted.
