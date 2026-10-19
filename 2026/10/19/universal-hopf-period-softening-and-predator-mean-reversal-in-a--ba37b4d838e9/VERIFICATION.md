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

# Reproducibility and scope

Run `python verify_hopf.py` with SymPy, NumPy and SciPy. The program reconstructs the nonresonant second-order Fourier coefficients, resonant cubic radial and tangential averages, Hopf coefficient, frequency-correction identity and exact moment-slope identity using symbolic algebra; finite ODE integrations check the predicted period near onset in representative cases. These integrations are finite corroboration, not an infinite-parameter proof; the proof is in `RESULT.md`. All displayed frequencies refer to dimensionless slow time, and the asymptotics hold for fixed positive time-scale ratio. An independent audit has not been performed.
