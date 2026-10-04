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
The standalone verifier uses exact rational arithmetic for the concrete witness. It checks the source threshold functional, the true and printed closed-season cutoffs, the true and printed fixed-season growth-rate cutoffs, and the source's auxiliary parameter inequalities. It also checks the exact per-cycle logarithmic upper bound \(-1/2\).

The general correction is symbolic: setting the source's displayed \(\digamma\) equal to zero gives \(\int_{\overline T^*}^{T}q=crT\), while subtracting the root equation from the value at \(\overline T>\overline T^*\) gives \((1/c)\int_{\overline T^*}^{\overline T}q\). No finite experiment is used as evidence for an infinite-time claim; global extinction in the witness follows from the analytic cycle contraction.

No independent audit has been performed.
