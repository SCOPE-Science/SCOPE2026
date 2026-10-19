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

# Verification and boundary conditions

A reproducible algebraic and numerical verifier (`verify.py`) directly builds the \(4\times4\) amplification matrix from the published split equations, and independently implements the characteristic polynomial. It checks 224 direct-matrix polynomial identities for sweep counts \(1\) through \(8\), seven couplings and four flow parameters; four exact symbolic identities; and over two hundred strict-region root comparisons. The recorded completed run reports **469 passed assertions**. It also evaluates the exact \(K=2,\kappa=3/2\) rational example. The code requires Python 3, NumPy and SymPy, and can be executed as `python verify.py`.

The infinite-parameter results are proved by symbolic elimination, exact polynomial factorization, classical strict Schur inequalities, and continuity with a simple-root implicit-function argument. Numeric eigenvalues are cross-checks only. The limits \(\varepsilon=0\) and equality \(a_K=-1\) or \(a_K=1/3\) do **not** assert stability at zero flow or settle marginal stability at positive flow. No independent scientific audit has been performed.
