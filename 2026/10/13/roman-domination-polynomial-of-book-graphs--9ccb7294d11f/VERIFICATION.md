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

The theorem is proved structurally by conditioning on the two spine labels and deriving necessary-and-sufficient page constraints in each case. The finite checker is a stress test of that proof, not a replacement for it.

`verify.py` constructs the square book directly from its spine and page edges. For every \(1\le n\le5\), it enumerates all \(3^{2n+2}\) labelings, tests the Roman condition from adjacency, forms the exact weight histogram, and compares that histogram with the claimed polynomial. It separately checks the least weight and its multiplicity and evaluates the closed total-count formula.

Expected replay output:

`VERIFY_OK n_range=1..5 labelings=597861 rdf_functions=180730 coefficient_checks=66 minimum_checks=5 total_checks=5 max_order=12`

The symbolic proof applies to all \(n\ge1\); the enumerated range is finite and no claim of exhaustive computation beyond that range is made.
