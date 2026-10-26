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

The analytic proof uses an explicit hypergeometric likelihood-ratio comparison and a nested coupling of uniformly distributed intersection sets. See `RESULT.md` for the exact quantifiers and treatment of boundary cases.

The portable `VERIFY.py` program (Python 3 standard library only) was run from the same directory with `python3 VERIFY.py`, returning `PASS: 6707 exact assertions`. This includes independently enumerated random-set sample spaces and comparisons of rational mass functions. These finite checks do not certify the infinite family; the written proof supplies that generality.

The first publicly identified motivating source is the 2022-02-15 preprint arXiv:2202.07485v1. The packet-distribution and fixed-packet-size literatures remain possible sources of broader deductions; independent priority review is not performed.
