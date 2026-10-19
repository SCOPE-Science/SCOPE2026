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

The mathematical argument is in `RESULT.md`. Execute `python walker_verifier.py` in a Python environment with NumPy, SymPy and SciPy. A successful execution prints `VERIFY_OK` with numerical diagnostic values. The checker verifies by exact trigonometric and symbolic identities that the sine-wave modes cancel to cubic order at the specified shape, that the restoring drift has the stated coefficient, and that the reduced fixed-point equations have the required roots in several small-detuning cases. It independently compares finite original-map iterations with numerical solutions of the detuning-limit ODE for both signs and tests the long-time critical slope.

The recorded run produced `VERIFY_OK` with final crossover error approximately \(0.002155\), inverse-fourth slope approximately \(13.4196\) after \(200000\) iterates, and predicted slope approximately \(13.4814\) at \(C=0.05\), \(\mu=0.6\). Those checks are finite diagnostics, not a computer-assisted proof. The rigorous results require the center-manifold expansion, the complete stationary polynomial calculation, and the memory-contraction plus Grönwall convergence estimates.

All results are local. No exact symbolic certificate for every initial state, no numerical certification of an infinite-time limit, and no independent review is claimed.
