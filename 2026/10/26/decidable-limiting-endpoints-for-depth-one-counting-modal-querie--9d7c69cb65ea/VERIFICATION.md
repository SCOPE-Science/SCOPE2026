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

# Verification protocol and boundaries

The result is self-contained subject to the standard multivariate central limit theorem, the Portmanteau theorem, rational linear-programming feasibility, the Gaussian orthant identity and the elementary algebraic-integer property of roots of unity. The key premises are: all nonroot outgoing-row cells are independent categorical observations; the root self-loop contributes a bounded integer term; depth-one formulas can be reduced by finite indicator case splits; and \(\Sigma\) has full rank under strictly positive nonedge probability and positive type masses.

Run `python checker.py` with a standard Python 3.10+ installation. Its expected final line is `ALL_CHECKS_OK`. It enumerates all root-row/label assignments for one through five worlds and checks three independent depth-one formulas against a multinomial sum; for the main formula it also enumerates all directed graph matrices and valuations for one through three worlds. It checks the exact covariance \(\bigl(\begin{smallmatrix}1/2&1/2\\1/2&3/2\end{smallmatrix}\bigr)\) and evaluates the claimed Gaussian-orthant limit numerically. All tests completed successfully in the delivered package.

These exhaustive finite tests cannot establish the infinite limit or demonstrate novelty. The asymptotic assertion depends on a joint central limit theorem and the zero-probability Gaussian boundary. The exact endpoint decision depends on a proof that strictly feasible homogeneous sign constraints can be rescaled to rational non-strict inequalities with unit margin; the multinomial covariance must be positive definite. The irrationality proof is independent of finite enumeration. The procedure does **not** decide convergence for formulas of modal depth two or greater, and it does not address degenerate probabilities or arbitrary dependence between graph edges.
