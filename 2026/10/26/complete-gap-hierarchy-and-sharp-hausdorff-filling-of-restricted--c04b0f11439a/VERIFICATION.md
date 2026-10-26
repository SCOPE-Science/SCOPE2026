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

# Reproduction and limits
Run `python3 verify.py` with the standard-library Python interpreter. It uses `fractions.Fraction` and `itertools.product` only, and its expected result is `VERIFY_OK exact_rational_gap_checks= 2975`.

The checks compare explicit branch compositions to the closed continuant formula at 2,975 finite combinations, verify the analytically derived largest-gap constant for seven reciprocal thresholds, and check gap ordering at finite levels. They do not exhaust all digits or depths and do not independently certify the infinite theorem. The general theorem instead follows from the compact inverse-branch decomposition, a geometric contraction estimate, and the maximum first-level gap calculation in `RESULT.md`.

The 1999 restricted-digit continued-fraction study was located, but its full text was inaccessible through the available sources; prior-result comparison on that item remains incomplete. No independent validation has been performed.
