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
# Reproducibility and evidence limits

Run `python checks.py` with Python, NumPy and SciPy. The code evaluates the original four-oscillator derivatives against the reduced system for 400 deterministic random phase configurations and numerically differentiates the conserved quantities. For phase lag \(\alpha=0.4\), it integrates one case below threshold, an approximation to the separatrix, and a periodic case, using strict IVP tolerances.

See `checker_output.txt` for the actual recorded result. The equality orbit is unstable to numerical rounding, so the equality check is deliberately made at finite time only; the exact equality convergence and all continuum parameter assertions come from the analytic proof in `RESULT.md`. The code does **not** certify the global theorem or exclude prior publications. Independent scientific audit has not been performed.
