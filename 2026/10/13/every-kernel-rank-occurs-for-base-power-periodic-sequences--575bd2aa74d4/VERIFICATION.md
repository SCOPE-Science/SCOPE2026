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

# Computational verification

Run `python3 verify.py` with a standard Python 3 interpreter. No external libraries or source data are needed.

The checker's `least_period` function tests divisors of a period word, and `kernel_rank` enumerates every decimation at depths through the base exponent. Every resulting finite word is reduced to its least period, making equality of the corresponding infinite periodic sequences decidable exactly. The generator `build_witnesses` realizes the recursive interleaving construction and its final color-unsharing step; the separate `restricted_partitions` enumeration exhausts output-symbol equality patterns independently of numerical names.

Executed result:

```
VERIFY_OK constructed_witnesses=168 primitive_partition_census=25285
```

Witnesses span parameter pairs \((2,t)\) for \(1\le t\le5\), \((3,t)\) for \(1\le t\le3\), and \((4,t)\) for \(1\le t\le2\). Canonical equality-pattern censuses cover \((2,1),(2,2),(2,3),(3,1),(3,2)\). The tests check exact ranks and least periods, but do not establish the theorem for arbitrary parameters. That infinite conclusion relies on the bound and induction proved in `RESULT.md`. No independent audit has been performed.
