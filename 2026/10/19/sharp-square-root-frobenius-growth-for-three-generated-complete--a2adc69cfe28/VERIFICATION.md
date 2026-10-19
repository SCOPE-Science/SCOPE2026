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

The constructive arithmetic proof uses the standard complete-intersection gluing theorem, the Apéry description of a gluing, the two-generator Sylvester formula, the AM–GM inequality, and elementary inclusion–exclusion. The key universal classification step is that any three-generated complete-intersection numerical semigroup glues a two-generated numerical semigroup to the one-generated nonnegative integers. This is a published theorem, not inferred from finite experiments.

`verify_ci_asympt.py` uses a shortest-path algorithm on residue classes modulo the multiplicity for independent exact Frobenius-number calculations. It tests the constructed family across the stated finite range and the lower-bound inequality across a broad grid of normalized gluings. It does not enumerate every semigroup at arbitrary multiplicity. Computations neither establish asymptotic novelty nor substitute for the mathematical proof.

Run `python3 verify_ci_asympt.py` from the directory containing this file. Python 3.9+ standard library is sufficient. Reproducible script output from current verification:

```
VERIFY_OK: 297 constructed multiplicities; 127 exact Apéry checks; 18625 normalized gluing lower-bound checks
sample 100 a 11 b 10 ratio 1.979000
sample 1000 a 33 b 31 ratio 1.981388
sample 10000 a 101 b 100 ratio 1.999799
sample 100000 a 317 b 316 ratio 1.997101
sample 1000000 a 1001 b 1000 ratio 1.999998
```

The final limit uses the mathematical estimate \(\omega(m)=o(\log m)\), not an empirical estimate of the growth rate. Independent mathematical audit has not been performed.
