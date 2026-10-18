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

The accompanying `check_split_type_b.py` is a standalone standard-library Python program; invoke `python3 check_split_type_b.py` in the containing directory. It performs exact rational vertex enumeration in small polar cases and exact algebraic witness and signed-root contact checks for two hundred parameter pairs. Reproducibility needs no external data files or network service. The proof in `RESULT.md` establishes every quantified claim for all integers \(p,q\ge2\); numerical or exhaustive bounded tests alone would not.

The pair \((p,q)=(3,1)\) is checked by the program as an out-of-domain boundary diagnostic and is not part of the theorem. The original source date is determined from the earliest public preprint version on 2018-10-29, not the date of its latest revision or journal appearance. An external independent audit has not been performed.
