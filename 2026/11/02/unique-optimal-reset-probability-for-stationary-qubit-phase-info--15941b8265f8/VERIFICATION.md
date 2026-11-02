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

# Mathematical verification and reproducibility

The included `verify.py` reproduces two exact symbolic identities using SymPy: the reset-probability and odds-ratio QFI expressions coincide identically, and the derivative of the odds formula is the stated polynomial divided by a positive fourth power. It also verifies the exact half-turn optimum value and the radical detuning constant.

For a numerically independent check, the program constructs the stationary two-by-two qubit density matrix, applies the reset-plus-unitary channel directly, and verifies the fixed-point equation. It obtains the SLD Fisher information by eigen-decomposing the density matrix and using centered finite differences in phase. This calculation was compared at 24 combinations of reset probability and nonresonant phase, with all comparisons within a relative or absolute tolerance of \(2\times10^{-6}\). The code checks root brackets and maximum comparisons at six representative detunings and records convergence toward the analytic near-resonance constants.

To reproduce, use Python 3 with NumPy and SymPy installed and run `python verify.py` from the extracted file directory. The exact polynomial sign proof, which establishes a statement for infinitely many parameter values, is written in `RESULT.md`; finite numerical checks are corroborating only.

No finite-time metrological cost model, external experimental comparison, or independent audit is supplied. At exact gate resonance, full-rank QFI is not asserted.
