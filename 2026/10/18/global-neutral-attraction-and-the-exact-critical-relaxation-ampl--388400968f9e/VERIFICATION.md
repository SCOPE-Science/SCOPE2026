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

Run `python -m pip install -r requirements.txt` and then `python verify.py` from the directory containing the files. The script uses Python standard-library `fractions`, `random` and `math` plus SymPy and SciPy; no external data files are needed. It checks exact critical parameter equalities and the symbolic cubic cancellation, 2,400 sampled inward-envelope inequalities, long-time ODE trajectories at criticality for both update laws, and antisymmetric-axis preservation. The executed script produced a `PASS` message for all checks. Its finite tests and numerical integration do not certify uniqueness, global attraction or infinite-time asymptotics; those follow from the proof in `RESULT.md`. The theorem uses a strictly positive cross-group structural coupling and a zero-bias two-community system. No independent review has been performed.
