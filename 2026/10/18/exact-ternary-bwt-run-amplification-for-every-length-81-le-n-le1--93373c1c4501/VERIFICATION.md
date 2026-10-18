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

Run `python3 check_bwt_witnesses.py` beside `BWT_WITNESSES.tsv`. Its assertions check all 80 consecutive lengths, the one-cycle LF criterion, inverse-necklace primitivity, input cyclic run count, and directly computed no-sentinel BWT. The data table contains the actual witnessing last columns, so no probabilistic generation is required during verification.

The lower bound comes from the published factor-two theorem; the 80 upper bounds are checkable by finite arithmetic and lexicographic sorting. The finite computations cannot establish any unlisted length or an infinite induction. Independent external audit has not been performed.
