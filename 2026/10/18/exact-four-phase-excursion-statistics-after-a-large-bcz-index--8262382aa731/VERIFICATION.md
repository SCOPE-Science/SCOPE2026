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

The closed-form probabilities follow from explicit one-dimensional integrals evaluated in `RESULT.md`, with the conditional cylinder density \(8/(k+t+s)^3\). The deterministic digit-\(2\) run length is derived pointwise before integrating.

Run `python3 check.py` to replay 8,160 exact-rational starting points for all integer initial digits from \(12\) through \(79\). It checks the actual floor-map iterates against the derived ceiling formula and phase support. This finite replay is a consistency check and does not constitute an infinite proof or independent audit. No external validation was performed.
