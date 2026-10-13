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
# Reproducibility and limitations

The analytic proof is complete in `RESULT.md`. Independently reconstructed computational-basis matrices for the lowering operator and total-spin Casimir recover the predicted Dicke dark-space multiplicities for \(1\le n\le7\), including the steady-state energy. An independent finite-dimensional passive spectral sorting algorithm checks \(1\le n<40\) and the exact \(\mathcal W_4/\omega=1/16\). The command is `python3 artifacts/verify.py` with the dependency version recorded in `artifacts/requirements.txt`. Its observed output begins with `VERIFY_OK`.

The finite-dimensional checks are corroboration, not exhaustive verification of all \(n\). The universal conclusion follows from the proved binomial moderate-deviation estimate, the explicit Casimir moment bound, and uniform integrability. Only a self-review was performed; there is no independent audit, third-party certification, or finite-time hardware validation.
