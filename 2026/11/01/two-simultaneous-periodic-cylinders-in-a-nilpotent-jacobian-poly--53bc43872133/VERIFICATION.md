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

The attached `verify.py` (with dependencies in `requirements.txt`) runs symbolic checks of nilpotence in the **original** coordinates, the exact shear conjugacy, the Hamiltonian first integral and the critical-energy formulas. It then evaluates the two planar one-cycle drift integrals, brackets opposite-sign drifts and finds a numerical zero in each annulus for each of three sample parameter pairs. To replay: `python -m pip install -r requirements.txt` and then `python verify.py`. A successful replay ends with `CHECK_OK`.

The analytical proof covers every real \(r>0\), \(K\ge3r/2\), including equality. Finite symbolic identities cover all values of the symbolic variables; finite numerical root checks are illustrative and not a proof of the infinite family. Numerical quadrature near the separatrix may report roundoff warnings because the period diverges. The sign-change proof does not rely on the numerical integrations. No external or independent audit has been performed.
