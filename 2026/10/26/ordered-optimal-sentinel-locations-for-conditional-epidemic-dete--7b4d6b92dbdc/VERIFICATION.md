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

# Verification record

The analytic result uses the path-distance infection law, a derivative-of-log-generating-polynomial identity, the monotone location of each adjacent switch, and the inequality that orders consecutive switches for every path length. These steps are detailed in `RESULT.md`.

The included `verify.py` uses only Python 3's standard library and separately enumerates every bond configuration for paths with two through nine vertices at four exact rational probabilities. Every monitor/parameter pair matches the closed-form detection probability numerator and conditional arrival-time numerator. Further exact-rational tests bracket the consecutive switching thresholds through 24 vertices and check 110 global optimality comparisons. Its exact output is `certificate.json`.

These tests cannot by themselves establish an all-vertex theorem. No simulation was used as a substitute for a proof. Independent expert or formal validation has not been performed. Different epidemic processes can give different optimal sentinels; conditioning excludes non-detections from the latency objective.
