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

Run `python3 verify_binary_cover.py` in this directory using Python 3 with its standard library. No network access or third-party dependency is required.

The script enumerates all \(25^3=15625\) normalized ordered triples after fixing two independent basis vectors, thereby covering all five-term spanning sequences, even when entries repeat. Rank-deficient five-term sequences remain in a proper subgroup of size at most \(5\). It separately enumerates all \(\binom{25}{5}=53130\) distinct five-element subsets, enumerates all \(480\) invertible linear maps, and partitions all \(1920\) maximizers into exactly six disjoint orbits of lengths \(120,120,240,480,480,480\). It checks a complete six-term covering witness and all invariant-factor isomorphism types of abelian groups with orders \(2\) through \(25\). All tests use exact integer and set operations.

Expected output begins with `VERIFY_OK` and reports `maximum_boolean_sumset 24`, `maximum_sets 1920`, `number_of_orbits 6`, and `exception [(25, (5, 5), 5, 6)]`. Loop bounds and normalization give the mathematical completeness argument. The script is not a substitute for interpreting the proof and is not external or independent certification. No behavior for groups of order above \(25\) is asserted.
