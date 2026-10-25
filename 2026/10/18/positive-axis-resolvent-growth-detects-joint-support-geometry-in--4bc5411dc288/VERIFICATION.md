---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Schur bounds on explicit V^n kernels imply ||T_d^n|| <= (n!)^-d, so quasinilpotent T_d has norm-convergent Neumann resolvent. The positive integral kernel sums to lambda^-2 E_d(product_j(x_j-t_j)/lambda), E_d(z)=sum_n z^n/(n!)^d, with log E_d(z)=d z^(1/d)+O_d(log(z+2)) by exponential-product upper and Stirling single-term lower bounds. The constant-one input on a small output corner attains operator type d. For nonzero f>=0, product_j(x_j-t_j)≤rho_f wherever integrand nonzero, proving upper rate; choose positive measure patch f>=c with support product >rho_f-eta, and a fixed output corner x>1-delta to prove matching lower rate. Division yields rho_f^(1/d), and cross/diagonal rectangles demonstrate identical marginals with different rho. Scalar E_2 finite diagnostics checked but not needed for infinite positivity proof.

## originality

PASS

Ji-Zhang one-variable Volterra complex-plane power sets and Hu-Ji-Liang general inclusions do not calculate positive-real-axis tensor resolvent type for arbitrary nonnegative multivariate f; the present result deliberately restricts to positive inputs and fixed positive-axis approach. Classical Laplace positivity is a proof ingredient; the joint-support formula and marginal counterexample are not obtained as stated from inspected one-variable results.

## value

PASS

An explicit local resolvent growth invariant for the tensor Volterra operator identifies joint support geometry invisible to coordinate marginals. The cone-restricted support classification in every fixed d links nonnormal operator growth to a geometrically meaningful essential supremum; it is more substantial than a one-dimensional Volterra restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
