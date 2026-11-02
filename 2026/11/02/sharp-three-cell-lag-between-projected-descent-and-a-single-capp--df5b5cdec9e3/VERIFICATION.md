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

The standalone standard-library Python 3 script `verify.py` performs 7,007 exact-rational checks of the proposed three-cell trajectory formulas and the exact max-norm error, followed by 300 separately randomized two-cell exact-rational comparisons. It computes Euclidean projections independently by active-set enumeration. An explicit rational example additionally compares 128 repeated local projection steps to the analytic continuous flow, emphasizing the difference from one global projection of the cumulative drift.

Execute `python3 verify.py` from the extracted files. Expected output: `VERIFY_OK 7007 exact-rational comparisons` and `VERIFY_2CELL_OK 300 exact-rational comparisons`.

The proof of all real-parameter statements and the limiting family sharpness is analytical in RESULT.md; the finite script is a supplemental consistency check rather than an exhaustive or formal infinite-domain certificate. The sharp \(1/3\) envelope is confined to the stated family; no wider quantitative bound is claimed. Independent audit has not been performed.
