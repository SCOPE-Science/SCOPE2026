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

The proof enumerates all extensive isotone idempotent endomaps of the diamond, computes their composition law, and derives maximal commuting families and all ordered tuples by inclusion-exclusion.

Run `python3 check.py` from the directory containing this file. The checker enumerates the original closure axioms directly for labelled diamonds of widths 2 through 8, compares every pair's actual compositions with the formula, checks maximal family structure, and independently counts selected commuting tuples of lengths 0 through 4. Expected final lines are `VERIFY_OK` and `TUPLES_VERIFY_OK`.

Finite verification cannot certify the infinite parameter statements. The published unrefined count is not claimed as new. The earliest dated scientific basis is the 2022 monotone-modal study; the full diamond counting lemma appeared in a 2023 preprint. No independent external audit has been performed.
