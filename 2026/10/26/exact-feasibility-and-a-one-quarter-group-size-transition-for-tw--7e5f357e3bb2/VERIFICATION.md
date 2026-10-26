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

# Verification instructions and limits

Run `python3 verify_two_item.py` using Python 3.10 or later; standard library only. The program implements mixed EF1 by evaluating both groups' bundle scores and explicitly considering removal of each item from the envied or own bundle. It enumerates all four two-item bundle allocations and all membership choices of each prescribed size for all valuation profiles with two through seven agents, then checks the derived minimum-type-count condition. The expected aggregate is 123,792 checked (profile, group-size) pairs.

The program also independently sums multinomial counts for sample parameters. In particular, eight agents split seven and one have exact infeasibility probability 315/8192 under four independent uniform types. Check output should end in `All checks passed.`. Finite exhaustive checks do not establish the theorem for unbounded populations; the universal and asymptotic statements follow from the separate analytical proof in RESULT.md.

Independent audit: not performed.
