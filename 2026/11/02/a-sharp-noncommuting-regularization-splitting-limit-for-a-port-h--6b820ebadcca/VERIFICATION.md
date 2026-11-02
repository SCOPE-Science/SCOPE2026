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

# Verification of the exact regularized splitting theorem

Run `python verify.py` using a standard Python 3 installation; no third-party packages are needed. The program forms the conservative and dissipative matrices separately and checks their product against the claimed closed form. It evaluates the exact regularized flow by its two stable scalar eigenvalues and tests phase-selected sequences of positive regularization parameters. Four pairs of positive step sizes and damping coefficients, each with four scales and five phases, give 80 checks, including the transition \(h=r\log2\).

Observed execution result: `VERIFY_OK exact split matrix; regularized-flow eigenvalues; 80 phase tests; sharp energy-norm envelope`.

The verifier is a numerical cross-check. The proof's key non-finite steps are the uniform-in-phase small-parameter expansion, the exhaustiveness of the trigonometric circle parametrization, the continuous unbounded phase as the regularization vanishes, and the exact minimization of an affine expression on the interval \([0,1]\). These are established algebraically in RESULT.md. Neither the verifier nor the review is an independent scientific audit.
