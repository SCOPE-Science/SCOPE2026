---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Direct inversion of 2x2 Gram gives R_B=q_B(Xbar)/S+b11/m, with S=sum_i(Xi-Xbar)^2, q_B(t)=(-t,1)B(-t,1)^T>0. Orthogonal decomp X=t*1+u in mean direction and H={sum u=0} has Lebesgue Jacobian sqrt(m). The event R_B>z is exactly a shrinking (m-1)-ball of squared radius q_B(t)/(z-b11/m). Rescale u by sqrt(z-b11/m), apply pointwise continuity of p and dominated convergence (bounded compact p, fixed B) for a finite positive coefficient; endpoint t is null set. Layer cake gives moment iff s<(m-1)/2. Holder with q_B^rho and int p=1 yields integral >= (int q_B^-1/2)^(1-m); equality requires unique positive continuous p*_B. Independent exact-rational inverse Gram checks, small-scatter volume and m=2 integral tail computations independently corroborate finite cases. Infinite asymptotics rest on dominated convergence and Holder.

## originality

PASS

Randomized least-squares conditioning and inverse-covariance lower tails are established, as are finite-pool joint volume-sampling experimental designs. The candidate identifies an exact collision-tube coefficient for iid continuous affine designs and its uniquely optimal density across all m. Those statements were not found in inspected modern primary theorems, and different sampling models/criteria prevent immediate implication.

## value

PASS

Near-coincident iid sample locations create a natural catastrophic inverse-Gram risk. The theorem gives the exact tail exponent, coefficient and sample-size-independent optimal continuous sampling law while identifying the moment existence threshold. It answers a well-motivated numerical design problem with a precise optimizable extreme-risk metric; not merely known mean-risk optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
