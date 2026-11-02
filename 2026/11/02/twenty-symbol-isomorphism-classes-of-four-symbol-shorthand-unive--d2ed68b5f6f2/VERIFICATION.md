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

Run `python3 verify.py` with `classes.tsv` in the same directory. The standard-library-only program exhausts all directed Euler tours anchored at the unique arc `012`, then independently exhausts all 2048 last-exit assignments on the 11 nonroot vertices. Both methods yield exactly 384 identical cyclic words.

Every global symbol permutation and its composition with reversal is then applied to every word, with a unique rotation normalization at `012`. All five conjugacy-class fixed-point profiles, the exact 20 relabeling classes, the exact 11 relabeling-and-reversal classes, their orbit sizes, and the full canonical class table are rederived. Successful local output is `VERIFY_OK`.

The complete finite enumeration establishes only the stated four-symbol, length-three-window result. It does not imply a comparable formula for other sizes. Independent scientific auditing remains unperformed.
