---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

PASS: For unit rows and consistent equations E||z+||²=||z||²-z^T F(p)z, F=sum p a a^T, so sharp worst-direction decrement equals lambda_min F. The permutation average of any p cannot reduce lambda_min, by concavity; this handles all asymmetrical distributions for global optimality without asserting their uniqueness. With symmetric u,t,v, the leaf-difference eigenvalue is r t (multiplicity m-1) and the orthogonal hub/pooled 2x2 block has trace 1-(m-1)rt and offdiagonal sqrt(m)tcs. Its smaller eigenvalue is at most trace/2 -sqrt(m)tcs, with equality at equal block diagonals. The maximum of the minimum of rising rt and falling affine bound occurs at t=1/Delta; direct substitution of stated u,v equalizes diagonals and attains r/Delta simultaneously in both invariant subspaces. The endpoint c_m arises from the unique physically allowed root of the hub nonnegativity constraint. Independent calculations verified normalization, 2x2 equality and target eigenvalue at m=2,3,5,8 with c=0.3; finite tests do not prove all m. No extrapolation past c_m, where this design becomes infeasible.

## originality

PASS

PASS: Optimal i.i.d. Kaczmarz row selection as an eigenvalue semidefinite program is classical and explicitly attributed to Dai et al. The assessed new part is an exact analytic optimizer and its positive pooled-weight/zero hub-weight activation threshold for the overcomplete star-plus-pooled frame. Prior inverse-positive square-coordinate-design results do not imply this rectangular rank-one-augmented geometry.

## value

PASS

PASS: The pooled extra measurement has a distinct algorithmic purpose in redundant projection systems, and its optimal weighting against the hub and leaf directions is a meaningful explicit E-optimal design question. The exact nonzero pooled allocation and sharp phase boundary where the hub measurement becomes unnecessary determine actionable behavior unavailable from a generic SDP restatement. A structural two-block proof covers all m>=2 in the natural feasible range. The result makes no inflated claim to universally optimal Kaczmarz runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
