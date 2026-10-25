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

# Verification and scope

The analytical reconstruction starts from the exact stationary empty-interval recurrence with the boundary values \(E_0=1\) and \(E_n\to0\). The two characteristic roots are \(\lambda\) and its reciprocal; the decaying solution and Bernoulli forcing give the explicit formula, including the coincident-root limit. The pair \((u,v)\) determines the unordered roots of a quadratic with nonnegative discriminant exactly in the stated sharp feasibility wedge. The generator applied to the occupied-site indicator gives the initial correlation slope, and monotonicity at fixed density proves global uniqueness of \((p,r)\).

Reproduce numerical checks with `python check.py`. All tests can be run with the Python standard library. They test symbolic formula consequences at randomly generated positive parameters, exact root inversion, independent finite-truncation recurrence solutions, and the endpoint collision. They do not constitute a proof of the infinite-dimensional stationary process; that part follows from Poisson-reset coupling and the empty-interval equation. No independent audit has been performed.
