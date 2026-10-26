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
# Reproduction and limitations

Run `python verify.py` from the directory containing this file and `verify.py` (Python 3, NumPy, SciPy). The verifier independently computes \(s_\eta\), integrates the full two-dimensional exposed–infectious fundamental matrix through one period, extracts its positive dominant multiplier, and forms a mixed finite-difference quotient at several annual phases. The script compares it with the symbolic coefficient for three distinct rate regimes, checks strict optimal-versus-opposite-phase inequalities, and fails loudly upon discrepancies. Floating-point checks are approximate and do **not** prove all-parameter strict optimality or the existence of an exact global minimum. The analytic all-parameter proof is in `RESULT.md` and rests on the periodic Riccati perturbation and its uniform \(C^2\) remainder.

The newest claim is confined to the principal local Floquet infection growth rate near the disease-free pulse-periodic state. No independent audit or external mathematical validation has been conducted.
