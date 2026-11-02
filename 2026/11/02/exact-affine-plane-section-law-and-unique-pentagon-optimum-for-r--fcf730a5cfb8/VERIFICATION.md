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

Extract `verify_prism.py` alongside the report and run `python verify_prism.py` with a standard Python 3 interpreter. The program implements a direct angular integral of the offset-overlap geometry separately from the evaluated closed formula; it also samples plane normals and offsets and uses directional width weights to approximate the complete face-count law. Its final output must be `ALL_CHECKS_PASSED` for the supplied numerical tolerances. The high-precision optimum and the global uniqueness statement follow from the analytic derivative proof, not exhaustive numerical search.

The mathematical proof is for all positive aspect parameters. Direct quadrature and Monte Carlo are finite checks and cannot prove identity at untested parameters. No independent mathematical audit has been performed. Historical priority comparison is bounded by accessible primary sources and the explicitly named inaccessible prism-stereology publications.
