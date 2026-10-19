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

# Reproducibility and verification

Run \`python verify.py\` in an environment with Python 3, NumPy, SciPy and SymPy installed. The script requires no network access or external data files.

The script checks the algebraic derivative identity for the one-petal shape function, verifies its optimal radical at representative exact parameters, reconstructs an independently weighted friendship-graph Laplacian and compares the matrix-inverse Kirchhoff index to the articulation decomposition, and checks exact rational matrix inverses. It then compares the proposed allocation and exact objective to a direct weighted-Laplacian calculation for several heterogeneous prices on each side of the deletion boundary, and checks numerical constrained optimizers and randomly drawn nonsymmetric feasible competitors. All 549 assertions passed in the reported run.

The proof establishing the result for every \(m\ge2\), price vector and positive budget is the argument in \`RESULT.md\`. Finite numerical tests cannot certify those universal quantifiers. Floating-point constrained optimization is used only as a sanity check and may depend on its software environment. Bibliographic novelty is not an outcome of the verification program. Independent audit has not been performed.
