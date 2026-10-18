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

The proof uses the generator of the three-site birth--death process and the moment equations \(Au=\mathbf{1}\), \(Av=2u\). An independently written exact-rational Gaussian elimination program, `verify.py`, solves these moment equations for eleven nonnegative rational colonization-to-extinction ratios. It compares three mean and three squared coefficient-of-variation values at each ratio to the symbolic closed forms and verifies all three factorizations for the deviations from one. The symbolic derivative factorizations and Descartes sign count establish the infinite parameter-range assertions analytically. No simulation, approximation or finite test is used as a substitute for the derivative proof. Independent verification has not been performed.
