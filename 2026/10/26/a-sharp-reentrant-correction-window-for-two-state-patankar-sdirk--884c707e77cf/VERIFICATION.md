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

For constant two-state conservative Q, uncorrected SDIRK predictors have first components u=pi+(x-pi)/(1+gamma*s) and v=pi+R(s)(x-pi). Direct evaluation of the cited final-stage-only Patankar column scalings L,M gives the strictly positive conservative corrected output (x+h*b*M)/(1+h*(a*L+b*M)); as epsilon tends to zero at fixed a,b,h,x this is exactly clip(v,0,1). With x=1, R has unique minimum (1-sqrt(2))/2 at s=4+3sqrt(2), giving negative predictor iff 0<pi<3-2sqrt(2) and precisely the quadratic-root open stiffness interval. At a=9,b=1,h=4/5 the limit zero disagrees with exact component >0.1; the first-order O(epsilon) boundary-layer coefficient follows by rational asymptotics. Independent fresh tests used 300 parameter sets and three cutoffs, plus threshold checks; finite experiments are not the all-parameter proof.

## originality

PASS

Primary published results were compared by their mathematical implications; the stated precisely delimited new theorem is not established by the inspected statements, with incomplete-source and implicit-folklore risks retained. Originality is a qualified best-of-knowledge assessment, not a priority certificate.

## value

PASS

The fixed-step singular-floor limiting map and a sharp window where positivity correction converges to the wrong face expose a meaningful boundary of an actively studied positivity-preserving integration method, distinct from routine timestep convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
