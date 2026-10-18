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

# Reproducible finite checks

Compile `unbordered_necklaces.cpp` and `unbordered_allwords.cpp` as C++17 executables. Run the first through \(n=28\) and the second through \(n=25\), saving stdout; pass the CSV and both outputs into `verify_histogram.py` as described in `RESULT.md`. The scripts were independently replayed on the actual prepared files with successful exact comparison.

The checker tests every finite histogram coefficient against the orbit computation, every coefficient through length \(25\) against the direct computation, and total-cardinality, nonprimitive, and first-moment identities through length \(28\). It also checks exact rational mean/variance at \(n=28\).

The C++ enumeration for \(n=26,27,28\) has not been independently duplicated by a complete labeled-word traversal. A finite exhaustive computation does not prove any infinite-length formula. Independent external validation has not been performed.
