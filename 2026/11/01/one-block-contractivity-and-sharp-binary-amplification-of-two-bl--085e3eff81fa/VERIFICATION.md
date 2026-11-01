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

# Reproducibility and verification

The only executable artifact is `CHECK.py`, a standalone Python 3 standard-library script. Run `python3 CHECK.py` in a directory containing the extracted file. Its deterministic seed is embedded in the code. The recorded execution returned `PASS finite checks: 42704` and an explicit strictly expanding two-block binary witness for \(p=2\), \(q=1/2\), \(n=2\).

The finite tests cross-check the exact telescoping binary formula over several parameters and counts, random finite-dimensional instances of the one-block norm bound, strict interior maxima and critical points, and selected near-endpoint scales. They do not certify arbitrarily large vectors or all real parameters.

The all-parameter proof is supplied in `RESULT.md`: fixed-sum concavity, exact rearrangement weights, scalar derivative analysis, grid convergence, and near-convex asymptotic expansion. The code checks numerical consistency only. No independent mathematical audit, verification authority, or publication priority determination is claimed.
