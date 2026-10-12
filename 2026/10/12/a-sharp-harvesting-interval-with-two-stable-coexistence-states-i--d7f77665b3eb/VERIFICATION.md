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

The exact-symbolic script `verify.py` is standalone apart from the publicly available SymPy Python package and checks all algebraic identities and rational sign certificates directly from the equations. Reproduce with Python 3 and SymPy: `python verify.py`. The successful current replay printed three root-bracket sign pairs and the final line `VERIFY_OK`.

The script independently reconstructs the two-dimensional reaction Jacobian, substitutes the equilibrium relations, and proves the determinant identity by zero symbolic difference. It verifies the exact coexistence cubic, six rational sign evaluations, the equilibrium trace polynomial and its positive global minimum. General necessity and sufficiency of the harvesting window are proved analytically by monotonicity of the second derivative, not by finite tests. Source full text and relevant previously published multiple-equilibrium results were compared for scientific coverage.

Limits: the proof is specific to the diffusion-free model under the given equal-mortality subfamily, except for local hyperbolic persistence. The experiment-free signs prove local types, not global basins. Independent audit has not been performed.
