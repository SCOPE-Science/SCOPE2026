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

Run `python3 verify_bernoulli_affine.py` using the Python standard library. The script independently constructs finite probability weights and full kernel row sums in exact rational arithmetic, compares the maximal row with the rare-corner expression, checks exact direct conditional-expectation matrix entries, verifies extremizing sign inputs and the \([0,1]\)-input positivity defect, tests bias monotonicity for selected profiles and confirms the fair-binomial parity identities for dimensions through 18. Poisson examples are checked numerically against an explicitly calculated limit.

The supplied copy ran successfully and reported `PASS checks= 54049`, `random asymmetric sharp norm= 203/75`, `positive undershoot= -64/75`. No external packages, downloads or environmental inputs are needed. The enumerations are finite and do not certify the universal convex-order or asymptotic claims; those rest on the separate analytical proof. The documented literature comparisons are research checks, not independent peer review or a proof of global novelty.
