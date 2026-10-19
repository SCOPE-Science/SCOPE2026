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

# Reproducible finite-state verification

Run `python3 verify.py` using the Python standard library; optionally run `python3 verify.py --native` to compare against NumPy binary16 evaluations. Both were executed successfully on the complete binary16 nonnegative interval grid.

The script uses integer-scaled exact binary16 significands and exponent fields, exact nearest-even rational comparisons and a full deterministic functional-graph decomposition. It asserts the count \(15{,}361\), the exact graph and basin profiles, all node-to-cycle reachability relations, the two rational ensemble means, the number of mismatched transitions and the number of starts with different zero-basin membership. It also prints immutable transition-table SHA-256 fingerprints for both maps.

The native cross-check reproduces \(30{,}722\) directed transitions independently through native 16-bit array operations; if NumPy is absent, the standard-library proof remains fully executable. The calculation covers each and every permitted discrete state; it does **not** prove anything about unrepresented real numbers, other arithmetic expressions or alternative rounding conventions.
