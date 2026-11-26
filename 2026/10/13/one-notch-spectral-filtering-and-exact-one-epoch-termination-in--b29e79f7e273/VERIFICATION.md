---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The publisher PDF, Algorithm 1 lines 2, 4, 6–8 and 10, confirms x_0 is the snapshot, the single-component estimator equals H y_t, the proximal map is the identity for h=0, and the new snapshot is x_m. With the snapshot fixed, y_0=x_0 and y_{t+1}=y_t+theta(x_{t+1}-x_t)=(I-theta*eta*H)y_t. Recovering x_t from y_t gives exactly the stated epoch polynomial. On the admitted modes 1-theta*q>0 and P_m is strictly decreasing in q. Its only possible zero there is q_star=(1-u)/(1-u^m), u=(1-theta)^(1/m). For m>=2 this increases strictly from 1/m to 1 as theta increases; for m=1 it is identically 1 (the strict-increase sentence at RESULT.md line 88 should be read for m>=2; the conclusion and separately treated constant m=1 filter are correct). Thus an admissible theta exists uniquely iff mq>1. When mq<=1, strict convexity for m>=2 makes the secant slope of (1-theta*q)^m increase from -mq, so the filter is positive and has the claimed sharp infimum; at mq=1 with q<1/2 this is a boundary limit, not attainment. For m=1 the filter and its infimum are both 1-q. Independently replayed 63 exact rational recurrence cases and verified the admissible example theta=(15-5*sqrt(7))/4 exactly in Q(sqrt(7)). Crucial scope: termination at the epoch snapshot, not necessarily at Algorithm 1's reported iterate x_a, which it samples from the pre-update inner iterates and which can include the initial point. The frozen Finding states the snapshot conclusion, not a guarantee for x_a. Its step-size range is Algorithm 1's, not a claim that Theorem 4.1's general sufficient bound is met.

## originality

PASS

The interpolation and recurrence are prior algorithm inputs. The distinct contribution is the exact epoch-snapshot filter and the complete notch/tuning and no-zero boundary classification in the stated range; it is not a new optimizer or a generalized stationarity theorem. The closest accessible exact-termination analogues have different state updates. The convex NMSVRG full text could not be inspected and remains a material residual risk, not proof of novelty or of overlap.

## value

PASS

The published method has a free coefficient and distinct deterministic dynamics for the interpolation point and snapshot. The useful fact is the complete limit of that coefficient as a design parameter: an admissible exact notch can target only one curvature, with an explicit threshold for when exact annihilation is possible and an optimal residual factor below threshold. This answers a natural calibration question on the canonical quadratic model that a stationarity rate does not answer. The affine recurrence itself is routine; the value rests on the sharp classification and its limits, not on the elementary derivation or on applications outside the model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
