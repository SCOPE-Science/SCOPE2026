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

The open-access primary article was inspected directly for the exact vector field, equilibrium line, characteristic polynomial, Equation (7), the two reported convergent line-equilibrium trajectories, and the publication date.

`artifacts/verify_line_equilibria.py` reconstructs the vector field and Jacobian symbolically, verifies the equilibrium-line substitution, factors the characteristic polynomial exactly, checks the source-parameter counterexample at \(\xi=0\), and verifies that both rounded limiting coordinates reported in the source satisfy \(\xi^2>8/3\). The recorded checker output ends in `VERIFY_OK`.

The checker verifies algebra only. The sum/product sign classification, normal-hyperbolicity interpretation, and originality/value judgments are supplied analytically in the accompanying files. No numerical integration is used as proof, and no independent audit has been performed.
