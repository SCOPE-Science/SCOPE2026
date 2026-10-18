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

The accompanying `verify.py` checks transfer-operator identities as functions on partition cells, not merely along a numerical orbit. It uses `fractions.Fraction` to subdivide the exact inverse-branch partitions and integrate all nine signed-digit pair cylinders for 32 rational values of \(\alpha\), including both endpoints. Expected terminal output is `CHECK_OK parameters 32 exact_or_derived_checks 1343`.

The complete proof for all real \(4/3\le\alpha\le3/2\) is the branch image calculation, integration, and elementary entropy inequality in `RESULT.md`. A finite rational grid is a diagnostic rather than a substitute for that proof. The strict non-Markov conclusion uses a forbidden three-digit word and a positive two-digit cylinder; endpoint Markovity follows from full-image branches and cellwise uniform conditional densities. No whole-space spectral gap, multi-step entropy formula, or assertion outside the stated parameter interval is claimed.
