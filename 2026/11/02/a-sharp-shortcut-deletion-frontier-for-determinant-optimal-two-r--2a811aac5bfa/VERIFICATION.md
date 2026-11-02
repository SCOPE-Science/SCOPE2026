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
# Reproducible verification

Use the bundled Python 3 program \(\texttt{verify.py}\), requiring NumPy, SciPy, and SymPy. Run \(\texttt{python verify.py}\) from the directory containing the program. The program independently constructs the reduced weighted Laplacian, computes determinants, checks matrix-tree polynomial identities symbolically, and compares the claimed optimum to unconstrained individual-edge alternatives.

Completed output:

`VERIFIED {'exact': 6, 'determinant': 80, 'feasible': 1200, 'optimized': 27, 'threshold': 80}`

The six exact cases consist of four nonuniform rational symbolic determinant identities, one exact boundary allocation with determinant \(1/125\), and one exact interior allocation with determinant \(9/1024\). The 80 determinant checks compare the analytical polynomial with direct reduced-Laplacian matrix determinants at lengths two through five in each route and five shortcut price regimes. The 1,200 feasible tests vary each original edge independently, and the 27 SLSQP tests optimize the full individual-edge weight vector rather than the class-reduced variables.

All checks completed without assertion failures. The Python script and its specified library versions are not a formal proof of the infinite family, and stochastic comparisons cannot establish exact uniqueness. Those claims are proved symbolically in \(\texttt{RESULT.md}\). No independent audit was performed.
