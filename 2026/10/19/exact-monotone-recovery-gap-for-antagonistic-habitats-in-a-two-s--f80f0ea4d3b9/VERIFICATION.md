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

# Mathematical verification

The proof in `RESULT.md` reconstructs the equilibrium, the full Jacobian, its symmetry decomposition, all four eigenvalues, the strictly dominant eigenvalue and the sharp endpoint expansions. The crucial strict-monotonicity inequality is the exact identity

\[
 r^2\big((r^2-\delta^2)^2+4\delta^2\big)-(r^2+\delta^2)^2
 =(r^2-1)(r^2-\delta^2)^2>0
\]

for all \(r>1\) and \(0<\delta<r\).

The standalone checker `verify.py` needs only Python 3 standard library. From the extracted package directory, execute `python3 verify.py`. It uses exact rational arithmetic for 20 parameter examples, checks the nonlinear equilibrium, direct four-by-four Jacobian action on invariant subspaces, and agrees with the factorized characteristic determinant at five spectral test values in each example. It also checks the strict algebraic inequality. These finite tests are sanity checks, not substitutes for the all-parameter analytical proof.

No global nonlinear convergence theorem, stochastic extinction claim, or independent external assessment is provided.
