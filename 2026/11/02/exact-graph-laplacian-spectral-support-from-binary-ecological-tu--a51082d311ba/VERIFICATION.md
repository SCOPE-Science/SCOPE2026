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

The exact finite certificates are reproducible with Python 3 standard library:

```
python3 verify.py
```

Expected final output is `VERIFIED exact kinetics, graph spectra, both directional instability witnesses`. The program checks exact stationarity, four exact partial derivatives, the determinant and trace of the kinetic Jacobian, each of the two graph characteristic polynomials by power-sum Newton identities, every rational modal determinant at \(q\in\{0,2,3,5,6\}\), and the signs required to reverse the two stability verdicts.

The arbitrary-graph theorem uses a complete analytical spectral decomposition, an explicit diffusion-ratio formula, and a finite-spectrum separation argument in `RESULT.md`. Finite computations are not a proof of that universal statement and do not test experimental robustness or nonlinear pattern selection.

No independent scientific audit or validation has been performed.
