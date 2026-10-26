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

Run `python CHECK.py` with Python 3 and SymPy installed. The checker performs exact symbolic simplification of the logarithmic derivative used in the proof and the cubic Taylor coefficient, then numerically reconstructs both nonlinear scalar eigenvalue equations for 100 reproducibly seeded, varied parameter/detuning samples. It also tests the strict mode-count transition at zero detuning and the near-threshold fold-width coefficient for several different \(J,\Gamma\).

Observed output from direct execution of the embedded checker before packaging:

```
PASS: exact derivative monotonicity identity and cubic normal form.
PASS: 100 random parameter/detuning samples; nonlinear eigensystem reconstructed.
PASS: fold uniqueness, cusp 3/2 law, and threshold mode counts.
```

Finite numerical evaluations do not establish a global theorem; the proof in `RESULT.md` supplies the necessary and sufficient argument and all boundary cases. The computed fold is obtained from a strictly monotone scalar function, not an assumed optimizer. No independent scientific audit was performed. The model's fixed-norm complex-eigenvalue equation should not be conflated with physical norm-preserving dynamics.
