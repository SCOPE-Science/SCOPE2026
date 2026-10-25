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

# Reproducibility and actual checks

Invoke `python3 verify.py` in a directory containing the supplied file. Python 3.8+ is sufficient, with no dependencies beyond the standard library. The actual exact-integer execution printed:

```
PASS first-route factors: 231
PASS pairs with product below bound: 3672
PASS second-route products: 231
PASS both independent routes agree on 6 unordered pairs
   7    7 ->    49 : 110001
   7   19 ->   133 : 10000101
   7   37 ->   259 : 100000011
  11   35 ->   385 : 110000001
  13   21 ->   273 : 100010001
  21   49 ->  1029 : 10000000101
```

The first route uniquely enumerates all \(1+2^i+2^j\) with \(1\le i<j\le22\), checks the strict product bound, then the product popcount. The second route uniquely enumerates candidate products, checks each odd possible smaller divisor through the exact integer square root, and retains factor pairs of weight three. Thus the two searches are exhaustive *conditionally on* the published bound \(ab<2^{23}\), which follows from Kaneko--Stoll Theorem 2.2 at the stated factor weights.

The verifier tests two related finite implementations, not a formal proof of the published bound and not an external or independent mathematical audit. The correctness of the mathematical reduction and the exhaustive loop ranges must be checked from the manuscript and code as well as the printed output. No unrelated range, higher digit weights or infinite experimental extrapolation is asserted.
