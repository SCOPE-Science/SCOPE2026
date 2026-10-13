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

# Verification of terminal reshuffling classification

The self-contained `verify.py` uses only Python 3's standard library and `fractions.Fraction`. Run `python verify.py` alongside this document. The observed output is exactly `VERIFY_OK 123 exact-rational cases`.

Its `terminal_moment` routine enumerates the literal component-index sequences under each sampling scheme, propagates every exact rational iterate through one or more complete epochs, and accumulates the expectation of squared error. Separately, `exact_formula` computes the alleged answer from the second-moment and geometric-sum expressions without using enumeration. The script tests \(n=2,3,4\), integer horizons up to three, several positive curvatures, rational normalized steps on each side of \(\eta\lambda=1\) and at equality, and nonzero initialization. It additionally verifies opposite signs in a two-eigenvalue model and exact equality of the explicit squared-error values \(81/16\) and \(45/16\).

The additional symbolic cancellation test, performed with SymPy during analysis and not required by the standalone checker, verified
\[
 A_n(q)^2-B_n(q)=\frac{2q(1-q^n)(1-q^{n-1})}{(1-q)^2(1+q)}
\]
for each integer \(2\le n\le12\), by exact polynomial simplification. The published proof derives this identity algebraically for all \(n\ge2\); neither a finite enumeration nor a computer-algebra check is a substitute for it.

**Unproved limits:** no universal terminal sampling comparison is asserted outside the shared-Hessian stable-step class, and no independent audit, automated proof assistant, or external certificate has been performed. Eigenmode cross-correlations do not enter the objective comparison because the common Hessian diagonalizes the excess quadratic exactly.
