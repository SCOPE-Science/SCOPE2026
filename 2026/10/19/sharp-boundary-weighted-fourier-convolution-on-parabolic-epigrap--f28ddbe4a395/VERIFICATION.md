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

# Verification and reproducibility

The attached `check.py` uses only the Python standard library. Execute it with `python check.py` in a directory containing this file; successful execution prints independent checks of the overlap-volume factor, horizontal kernel mass, Carleman-kernel integral, and finite log-box Rayleigh quotients. All these checks passed before packaging.

The analytically critical statements are the exact overlap identity, beta integral, Carleman Fourier multiplier, two-limit sharpness construction, and weakly-null horizontal translation argument; their complete derivations appear in `RESULT.md`. The numerical checks sample finitely many dimensions and parameters and do not prove those statements. No independent validation has been conducted. The full literature comparison does not certify global first occurrence.
