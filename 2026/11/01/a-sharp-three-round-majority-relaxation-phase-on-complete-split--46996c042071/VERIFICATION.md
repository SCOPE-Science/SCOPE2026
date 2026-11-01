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

# Reproducible checks
Run `python verify_majority_split.py` in this directory using Python 3.8 or later. It uses only the Python standard library.

The primary implementation computes each vertex's next value from its complete graph-neighborhood count, retaining the previous bit on an exact tie. For every ordered pair of positive part sizes with total at most 16 it enumerates all labelled starting states, computes their first return at displacement two, and checks both the exact time-three classification and the full two-step recurrent-state count. This covers 120 size pairs and 1,835,012 starting configurations.

A separately written word-level implementation computes each module's transition from its total counts. For all 1,024 ordered parameter pairs with part sizes from 1 through 32, it checks all 313,600 possible part-population signatures, their entry times, and the binomial-weighted time-three census. The code also checks that exactly two configurations are fixed in every small exhaustive case. Sample all-parameter checks include \(E_3(5,3)=60\), \(E_3(6,4)=120\), and \(E_3(7,5)=910\).

The recorded output in `verification_output.txt` ends with `MAJORITY_SPLIT_ALL_CHECKS_PASSED`. These checks do not prove the theorem beyond the stated finite ranges; the complete proof appears in `RESULT.md`. No independent external audit or formal proof assistant validation has been performed.
