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

The analytical classification follows by elementary elimination of the predator-positive equilibrium constraints and spectral analysis of three exact Jacobian factorizations. The parameter inequalities require only positivity and \(A>b\). The computations in the standalone `check.py` use SymPy; install `sympy>=1.12` (see `requirements.txt`), then run `python check.py` in the same directory. The expected successful output is `CHECK_OK: line, all three Jacobian factorizations, thresholds, sample and crossing`.

The checker constructs the full polynomial vector field with rational coefficients, symbolically checks the critical equilibrium segment, recomputes the characteristic polynomials of the interior symmetric branch and the exclusion branch, validates the threshold-ordering identity, and tests the fully rational example. Each factorization is an exact algebraic identity; the infinite-family stability conclusion requires the mathematical argument that the relevant quadratic coefficients are positive for *all* admissible parameters and segment coordinates. Those inequalities are proved in `RESULT.md` and are not inferred from the finite example.

The example \(A=2\), \(b=k=h=p=c=\delta=1\) yields a critical segment \(u+v=1\), \(y=1\) and normal characteristic polynomial \(\lambda^2+\lambda+2+z-z^2\), \(0\le z\le1\). The result makes no global attraction, oscillation-exclusion, basin-volume or robustness assertion. It has not undergone independent audit.
