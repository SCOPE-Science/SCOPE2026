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

# Reproducibility and limits

Run `python verify.py` with Python 3 standard library. The script checks four even lengths, several exact rational perturbations, the conserved simplex-mass derivative, exact Jacobian identities, selected Hessian signs, the geometric-equilibrium polynomial signs, the entropy dissipation identity by finite differences, and the \(k=2\) extended-basin witness. Expected output starts `VERIFY_OK`. The displayed proof independently establishes the theorem for every even positive \(L=2k\), every initial simplex vector, and every finite time; finite tests do not establish an infinite quantifier. The original mean-field dynamics and equilibrium theorem can be compared with arXiv:2605.28984v1. The convergence rate is eventual and trajectory-dependent; the entire stable separatrix is not explicitly parameterized. Independent mathematical audit has not occurred.
