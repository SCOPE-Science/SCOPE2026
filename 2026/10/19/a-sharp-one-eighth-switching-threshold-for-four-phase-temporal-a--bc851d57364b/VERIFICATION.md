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

# Reproducibility of the exact moment and phase calculation

Run `python verify.py` using Python 3's standard library. The script enumerates every environmental state word and every inverse-branch cylinder, computes exact affine preimages of the complete random map, and integrates both cubic directional moments using rational arithmetic. It independently checks 40 combinations of switching parameters and lags against the claimed expression, including lags through eight and the exact critical switching line \(\delta=1/2,p=15/128\). It separately checks six phase-boundary and alternating-sign identities.

Actual command (from the package directory): `python verify.py`.

Actual stdout: `VERIFY_OK 40 exact independent cylinder comparisons; 6 boundary and sign identities`.

The finite computation is corroborative. The identities for arbitrary real \(0<\delta,p<1\), all integer lags, and the sharp threshold are proved analytically through the polynomial transfer operator, elementary Markov-sign moments, and a finite geometric-series sign argument in `RESULT.md`.
