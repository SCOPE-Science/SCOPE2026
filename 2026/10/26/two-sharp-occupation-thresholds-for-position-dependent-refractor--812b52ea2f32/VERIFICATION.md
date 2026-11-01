---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Stopped Brownian increment at rate r has centered Laplace density (c/2)exp(−c|x|), so reset epochs satisfy an affine perpetuity and exploration-time stationary position S_a=sum_{j>=0}a^j Z_j. The reset-state stationary law is aS_a. Markov-renewal occupation rewards weight active density by 1/r and resting density by tau0 e^{lambda|x|}; the conditional duration law matters through the mean only, with residual holding time needed for a Markov realization. Convolution with the leading Laplace increment and a contracted remainder having a strictly stronger exponential moment gives sharp f_a and g_a tails with positive coefficient c/(2P_a), c/(2aP_a), respectively. Integrability iff lambda<c/a follows at equality too; posterior odds are eta e^{lambda|x|}g_a/f_a, proving all three threshold cases. Its two-sided positive Laplace pole yields M_a(lambda)~c/[aP_a(c/a−lambda)] and active-fraction coefficient. Independent 45-digit mpmath partial-fraction tests confirmed f-tail at 3 x values and posterior asymptotics at 3 lambda values; these are supplementary finite tests.

## originality

PASS

Known Laplace perpetuity and constant-delay mixture are acknowledged; new consequence requires conditioning the holding mean on the random reset position, then comparing two distinct exponential tail exponents and determining a sharp null-recurrence boundary.

## value

PASS

A physically motivated reset-location-dependent recovery time creates a genuine separation between tail-level inferred phase inversion and loss of normalizable stationarity. The result fully classifies both thresholds, the nontrivial critical posterior, and a sharp occupation-collapse coefficient for a natural regenerative process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
