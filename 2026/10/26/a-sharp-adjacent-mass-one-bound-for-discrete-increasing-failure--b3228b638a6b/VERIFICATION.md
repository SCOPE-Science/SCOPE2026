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

The universal inequality was checked by a complete analytic derivation using log-concavity of the survival sequence, an exact one-variable upper envelope for the mean, a derivative sign analysis on every active-set interval, and a monotonicity proof for the endpoint thresholds. Equality forces a specified geometric survival profile and conversely that profile meets all assumptions.

Reproducible supplementary checks: `python verification/check.py` from the package root, using standard Python. This executes more than 7,000 finite checks, including rational arithmetic for a five-point witness. It independently evaluates the cubic root numerically, confirms normalization and zero mean of the limiting equality law, and checks the analytical envelope on grids. Finite grids cannot prove the inequalities on all real parameters; the proof is contained in `RESULT.md`.

The historical hazard-rate literature comparison is nonexhaustive. There is no independent audit evidence.
