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

# Verification notes

Proof checks: normalized Hardy kernels give the reciprocal circle formula exactly; differentiation gives positive \(R''\) and the strict binomial-tail inequality; minimization of circle intersections determines every horizontal slice and attainment; local and large-radius asymptotics establish precise boundary laws. Both the \(0<|a|<1\) and \(|a|=1\) regimes are covered. For the latter, the limiting minimum at large circle radius is excluded rather than attained.

Run `python3 checker.py` beside the extracted proof file to reproduce finite diagnostics. Expected output: `PASS 10358 finite checks`. These finitely sampled checks do not prove the universal assertions or literature priority; the written analytical proof must be evaluated on its own merits.

Independent audit has not been performed.
