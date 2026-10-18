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
# Verification and reproducibility

Execute `python verify_rook_general_position.py` using Python 3.9 or later; no third-party packages are required. Direct graph-geodesic tests enumerate 104306 literal vertex subsets in ten small board sizes. An independently coded root-component recurrence and the claimed finite formula are compared for each, and for seven larger boards where full subset enumeration would be expensive. Exact-integer checks compare polynomial coefficients, degrees and leading coefficients, yielding 17 passed parameter-size comparisons.

The infinite theorem depends on the explicit forbidden-path bijection, star-forest decomposition, exponential formula and equality-case classification given in the result, not on finite enumeration. No externally independent validation was performed.
