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

Run `python3 checker.py` with Python 3 and no nonstandard packages. It directly computes ordinary borders as literal prefix/suffix equality and Abelian borders by equality of prefix/suffix letter counts; it tests all binary words with at most three ones through length 30 and all words with exactly four ones through length 26. The latter are checked against the gap characterization. A separate arithmetic coefficient test compares the rational series against an independent sum over gap parameters through length 120.

Expected successful console output contains `PASS: sparse_r<=3_words= 36455`, `PASS: weight_four_words= 80730`, and `PASS: lengthwise_gf_and_params_to_n= 120`. The tests exercise only finite samples; the proof's gap reductions and formal generating-function identities, not computational extrapolation, establish the infinite assertions.

No independently commissioned mathematical audit has been performed. The cited 2014 paper on Abelian borders was not available in full for historical-priority comparison.
