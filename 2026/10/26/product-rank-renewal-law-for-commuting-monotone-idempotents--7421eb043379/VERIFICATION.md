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

The all-size claim follows from the common-product interval-fiber decomposition and the anchored-retraction generating series in `RESULT.md`; the finite checker is supporting evidence only.

Run `python3 check_commuting_monotone.py` in a directory containing this file and the checker. It uses only Python's standard library. The test directly generates all monotone maps of each chain \([n]\), filters idempotents, calculates commutation by pointwise comparison of both compositions, and refines counts by \(|\operatorname{im}(ef)|\). Its independent predicted counts come from a recurrence for the number of anchored retractions and a weighted block renewal convolution.

On the included checker, the observed result was `ALL_MONOTONE_IDEMPOTENT_RANK_TESTS_PASSED 9 7817630`, covering each \(n\) from one through nine and testing 7,817,630 ordered idempotent pairs. The exhaustive range is finite; no assertion of independently certifying the infinite theorem is made. Asymptotic constants were additionally evaluated from the displayed rational functions, but no numerical approximation is used as proof.
