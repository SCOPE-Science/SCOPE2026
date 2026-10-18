---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

CG residual p_k is the normalized degree-k orthogonal polynomial for the positive b_i^2 spectral measure. Ritz zeros in [mu,L] give |1-lambda/theta|<=1 when L<=2mu and hence |p_k(lambda)|<=1; x_{k,i}=b_i/lambda_i*(1-p_k(lambda_i))>=0. At convergence residual zero. Two-mode systems converge within two steps. For kappa>2, diag(1,kappa/2,kappa), b=(1,1,eps) has p2(kappa)->kappa-1>1 and negative third coordinate for small eps. Identical exact-line-search Broyden iterates follow a cited existing CG equivalence. Independent rational recurrence reproduced the kappa=4 negative second iterate.

## originality

PASS

Neither the published 3D CG Stieltjes sign-loss construction nor the steepest-descent condition-two theorem covers the all-iterate positivity theorem for diagonal CG; the CG–Broyden equivalence transfers the property but does not imply positivity. The exact orthogonal-polynomial sign certificate and universal sharp condition-number frontier survive source/implication comparison.

## value

PASS

Coordinatewise positivity is a natural feasibility invariant for iterative solvers with nonnegative solutions, not controlled by standard CG energy-norm convergence. A dimension-free all-step safe region plus the minimal dimension and iteration of failure gives a sharp structural boundary usable when selecting unsafeguarded CG/BFGS on nonnegative diagonal problems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
