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

# Reproducible checks
Run `python3 verify.py` with Python 3.8 or newer. No packages beyond the Python standard library are needed. The script constructs the second-order recurrence by exact integer additions and does not use the interpolation formula to generate its values. It verifies \(48\) primitive starting pairs modulo eight across \(11\) successive divisibility levels, checks exact counts of qualifying residues and the multiplier-period identity, and tests \(2760\) further signed pairs against the low-valuation branch classifications.

Expected completed output:

```text
VERIFY_OK primitive_classes_mod8=48 unbounded_classes=24 modular_censuses=528 additional_integer_pairs=2760
```

The infinite isometry and unique-root claim are established in the mathematical proof, not by these finite checks. The two-adic root is determined modulo each \(2^m\) by checking the unique zero class at divisibility \(2^{m+3}\). An exact zero term has valuation \(+\infty\). No independent mathematical audit has been performed.
