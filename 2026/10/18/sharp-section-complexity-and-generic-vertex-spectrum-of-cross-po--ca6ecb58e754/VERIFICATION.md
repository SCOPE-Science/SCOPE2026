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

The general proof is contained in `RESULT.md`. It includes the edge-graph reconstruction, antipodal split count, vertical monotonicity, four-case realization, completed-square optimization, the standard nongeneric perturbation argument, and graph-cut comparison.

Reproduce finite checks by running `python3 check_cross_prism.py` with Python 3 and its standard library; no external downloads or numerical libraries are needed. It checks reconstructed edge graphs, exact integer functional signs, all \(518\) prescribed layer-count pairs through dimension \(8\), and additional samples through dimension \(10\). The observed summary was: `CROSS_PRISM_CHECK_OK exhaustive_integer_hyperplanes= 18962 all_realizable_count_pairs= 518 sharp_maxima= [(2, 6), (3, 14), (4, 26), (5, 42), (6, 62), (7, 86), (8, 114)] maxcut_verified= [(2, 12), (3, 22), (4, 40)]`. These are finite tests; the infinitely quantified claim is justified by the symbolic argument rather than extrapolation.

The newest prism-to-slab theorem (arXiv:2609.16195, Proposition 3.6) was compared on its actual mathematical statement. It is acknowledged and does not explicitly give the specialized all-dimensional formula or integer spectrum. The earliest motivating printed source was cataloged as first released 1994-11-29. Independent audit and external historical-priority verification have not been performed.
