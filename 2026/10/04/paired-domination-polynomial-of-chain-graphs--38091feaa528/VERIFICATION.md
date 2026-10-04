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

The proof in `RESULT.md` is the primary verification. It reduces perfect matchability to Hall's condition and uses the nested chain ordering to reduce Hall's inequalities to cumulative class counts.

The standalone checker `artifacts/verify.py` constructs canonical chain graphs, enumerates vertex subsets, tests paired domination directly from the definition, tests the structural characterization independently, and computes the polynomial again by the deficit-state recurrence. Its tested range is every profile of order at most \(10\) with at most four canonical twin-class pairs.

Expected terminal line: `VERIFY_OK graph_types=510 subset_checks=348500 polynomial_profiles=1681 max_order=10`.

The computation is finite evidence only. It does not replace the proof for arbitrary order or an arbitrary number of twin classes.
