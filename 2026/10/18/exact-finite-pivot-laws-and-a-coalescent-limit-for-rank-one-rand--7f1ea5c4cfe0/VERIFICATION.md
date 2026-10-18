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

# Verification of rank-one Jacobi stopping laws

The analytic argument in RESULT.md is the basis for the all-dimension claims. Its nonstandard steps are: exact orthogonal elimination of one active coordinate of a rank-one block; state-dependent pair-selection probability; independence of holding periods; geometric-to-exponential limit plus a uniform discarded-stage expectation; and the block hypergeometric first-step recursion. The matrix identity and finite rational recurrence were checked by the accompanying `reproduce.py`, using Python 3.10+ standard library only.

Observed finite checks: 702 structural, rational, and variance tests passed. Nine empirical means over 6,000 repetitions each agreed with exact expected block-pivot counts within stated tolerances. The program does not certify infinitely many cases and does not test floating-point eigenvalue routines; the proof covers exact arithmetic only. External independent review or certification has not been performed.
