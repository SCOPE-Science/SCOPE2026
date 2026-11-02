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

Exact replay: `python3 checker.py` with Python 3. Test coverage: all set partitions on labelled sets of size 1 through 5 and all idempotent candidate functions, independently evaluating forth and back rather than assuming the block formula. Separately, a rational formal-series exp/multiply implementation checks coefficients through degree 7 against independent partition sums. The last outputs are `ALL_CHECKS_OK` and `ALL_SERIES_CHECKS_OK`. This finite verification is not the general proof. The general proof uses a reversible rooted-class decomposition; historical originality is subject to the cited 2015 nonuniform-partition antecedent. Independent validation has not been performed.
