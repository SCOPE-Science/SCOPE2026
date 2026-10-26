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

The analytical proof uses isolation indicator expectations and exact pairwise intersections in a tree. Run `python verify.py` with versions in `requirements.txt` and compare its JSON output byte-for-byte with `certificate.json` after stripping the final line terminator. This checks all unlabelled trees through nine nodes, all degree-matched pair comparisons, exact Sturm real-root counts and direct survival-state enumeration for the exhibited pair. Exact coefficients certify the sign across the entire open parameter interval, not merely at sampled probabilities. Exhaustion stops at nine vertices; no larger census or independent validation is claimed.
