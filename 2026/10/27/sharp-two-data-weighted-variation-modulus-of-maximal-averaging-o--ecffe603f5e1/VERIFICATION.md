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

# Verification

The exact graph-ball formulas reduce the problem to a continuous piecewise-affine map on weighted edge-gradient coordinates. The theorem's proof bounds every column of every full-dimensional affine selector matrix, then invokes continuity to handle selection ties. A strictly positive open-cell construction realizes the largest weighted column sum. The two-vertex exception and signed-data failure are handled separately.

Run `python verify.py` to check 127,926 exact rational formal selector-column estimates (including infeasible masks), 20 exact attaining-pair instances, 5,000 exact-rational random secants, and seven signed-domain obstruction examples. No third-party packages are required.

Finite sampling does not prove the all-dimensional, all-weight result. The analytic derivative-column argument covers those infinite quantifiers. No independent audit has been performed.
