---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The expected range is exactly \(\sum_j[1-P_j^N-(1-P_j)^N]d_j\). The centered parent is \(\sum_jd_jH_j\), so the \(L^2\) triangle inequality gives the lower constant; with at least two positive gaps the nested centered indicators are not positive scalar multiples, making the lower inequality strict, and one dominant gap gives sharpness. The extreme-order mass identities give the exact covariance with the cellwise secant slopes of \(u^N+(1-u)^N\); strict convexity makes those slopes strictly increasing, so Cauchy--Schwarz has an admissible unique affine equality support. Connectedness gives the full interval. Fresh exact-rational replay checked 2500 independent profiles/supports and all displayed inequalities and score ordering.

## originality

PASS

A prior SCOPE record already gives the exact profile-specific upper constant and the same unique secant-score maximizer. The audited record is therefore not original on its upper half. It adds the sharp lower cumulative-cut constant, proves strict nonattainment for at least three atoms, and combines both sides into the complete attainable interval. That lower extremal problem is not stated or implied by the prior upper theorem or by the inspected classical mean-variance range literature.

## value

PASS

Expected range in standard-deviation units is a classical scale-efficiency statistic. Once category probabilities are fixed, the newly supplied lower floor identifies the worst possible support geometry and completes the previously one-sided profile theorem into an exact interval. That is a natural structural refinement with direct use as a calibration envelope for finite or rounded data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
