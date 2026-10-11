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

Whitening the sampling covariance reduces the repeated-sampling ellipsoid statistic to Q equal to the sum of independent chi-square-one variables weighted by a_i=1/(1+lambda_i). Continuity gives a unique fixed-level ellipsoid scalar. Pathwise comparison with a_min times chi-square-d and a_max times chi-square-d gives strict interior bounds under anisotropy. For a contrast, the posterior-to-sampling variance ratio is a generalized Rayleigh quotient, whose worst direction yields tau_L=a_max. Finally Q dominates a_max times one chi-square-one term and is bounded above by a_max chi-square-d, while the upper quantiles of chi-square-one and chi-square-d have ratio tending to one, proving tau_E tends to tau_L. Fresh deterministic quadrature reproduced the package's two-dimensional value 0.6917708844598199.

## originality

PASS

The bMGP source supplies the conservative covariance decomposition, while Tanaka supplies generic scalar-calibration context. Neither accessible primary statement nor the fresh Resultary search gives the finite-level strict separation between the exact joint-ellipsoid scalar and the sharp all-linear-contrast non-undercoverage threshold, together with their extreme-confidence coalescence. The weighted-chi-square and generalized-Rayleigh argument is therefore a best-of-knowledge new structural consequence of the bMGP limit.

## value

PASS

The theorem identifies the exact cost of insisting on one direction-preserving scalar correction for a practically motivated conservative posterior: exact joint coverage can permit materially more contraction than simultaneous contrast protection. This is a useful calibration boundary rather than a generic restatement of covariance mismatch.

The dated certificate retains the supplied scientific assessment, sources and limitations.
