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

# Reproducibility

The standalone source `verify_bivalued_online.cpp` was compiled and executed with:

```sh
g++ -std=c++17 -O3 -Wall -Wextra verify_bivalued_online.cpp -o verify
./verify
```

Observed output:

```text
VERIFY_OK cases=3908208 prefix_checks=21778368
```

The checker directly simulates the high-first/first-low allocation. It independently recomputes the complete EF1 inequality at every allocation prefix, and also verifies the unenvied-anchor inequality. It exhaustively enumerates all high/low binary valuation masks with \(n=2,3,4\), \(m=n+1\) under three positive integer tier palettes. It additionally tests 150,000 pseudorandom cases for each \(n=5,\ldots,9\) with heterogeneous positive integer tiers using a fixed PRNG seed. Integer arithmetic is exact, but the experiments establish only their finite domains. The mathematical proof in `RESULT.md` establishes the theorem for all integer numbers of agents and all positive real two-tier values. No independent scientific audit has been performed.
