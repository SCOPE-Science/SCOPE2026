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
# Computational and analytic verification

Analytic proof: equations (1) and (2) follow from a single conditional expectation of an explicitly stated coordinate update; sharpness follows from eigenvector witnesses for the two diagonal forms. Equations (4) and (5) are obtained by summing row-sign cross terms and are exact for all iterations. An induction gives the strict two-sided residual bound and a joint contrast/horizon limit proves its sharpness. No finite enumeration is used as an infinite or unique-priority certificate.

Supplementary `verify.py` was executed from its actual package bytes using the standard Python interpreter. It returned: `PASS 370 exact-rational enumerations, plus the near-doubling asymptotic check; example error ratio 9/10, residual ratio 57/50`. The checks include direct average over every row/column choice on flat orthogonal-column designs (orders 2, 4 and 8), an exact all-path comparison through 3 steps in three two-mode cases, and a large finite contrast asymptotic sanity check. It does not establish all-dimensional or all-contrast assertions by itself.

Scientific limits: exact arithmetic; consistent real finite-dimensional data; uniform independent row and coordinate choices; flat orthogonal-column frame; constant timestep. Complete later sections of the motivating 2026 preprint were not accessible, and novelty may require further historical verification. Independent mathematical validation has not been performed.
