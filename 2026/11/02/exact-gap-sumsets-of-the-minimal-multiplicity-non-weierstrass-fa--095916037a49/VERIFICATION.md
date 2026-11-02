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

# Verification record

The provided Python 3 script `verify_gap_sums.py` is self-contained and uses integer arithmetic. Its `enumerate_gaps` constructs semigroup membership from the generators without using the closed gap formulas; its `predicted_sumset` constructs the two explicitly missing arithmetic progressions; and its `run` compares the complete enumerated sumsets with the predicted sets, as well as cardinalities and Buchweitz deficits.

Executed command: `python3 verify_gap_sums.py`.

Observed result: `VERIFY_OK` over 864 admissible integer parameter pairs, comprising the 72 integers from 13 through 120 not divisible by three and all 12 orders from 1 through 12. Sample cardinalities: genus 13 gives 35 and 57 at orders two and three; genus 14 gives 38 and 62.

These finite tests are independent computational cross-checks of the supplied algebraic proof, not a proof of the infinite statement. The previously published non-Weierstrass property of the family is cited as an external mathematical input and is not computationally certified here. No external mathematical review or independent audit is claimed.
