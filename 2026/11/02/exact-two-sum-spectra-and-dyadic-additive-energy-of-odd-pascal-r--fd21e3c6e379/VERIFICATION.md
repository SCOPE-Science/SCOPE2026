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
# Reproducibility and verification

From the extracted package root, execute `python3 verification/verify.py` with Python 3 and its standard library. The checker computes 32,896 direct binomial-parity comparisons, checks 256 complete ordered two-sum convolution profiles by explicitly enumerating support pairs, checks 256 corresponding additive-energy totals, and compares the deduced dyadic recurrence for all 12 levels \(0\le r\le11\), across 2,048 row indices. All these checks passed before packaging.

The infinite statement rests on the proved block-sum injectivity and the formal generating-function decomposition in `RESULT.md`, neither of which is certified by any finite computation. The checker requires no external downloads, data tables or third-party packages.
