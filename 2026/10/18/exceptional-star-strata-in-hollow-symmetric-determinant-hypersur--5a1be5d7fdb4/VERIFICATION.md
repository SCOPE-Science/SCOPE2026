---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In characteristic zero, only the off-diagonal adjugate entries enter the hollow Jacobian. At corank one the adjugate is a nonzero multiple of vvᵗ; vanishing off the diagonal means the kernel is a coordinate line. This gives exactly the n zero stars in addition to the corank-two locus. The isotropic Gram parametrization and its orthogonal fibers give an irreducible corank-two cone of dimension N−3, and the cited degree formula specializes to binom(n+1,3). A full-rank complementary block gives a point of each star outside the corank-two locus. Killing the star variables leaves exactly the complementary determinant among all (n−1)-minors. Its primeness follows from the cited hollow rank theorem at size n−1 and rank n−2; in particular it is not merely set-theoretically irreducible. Two stars leave a free hollow block of size n−2. Schur complements give the exact star quadratic and the 2×2 symmetric residual determinant; at the specified kernel W, the three indicated hollow perturbations map onto Sym²(W*), which proves the generic surface-double-point description. Singular codimension excludes repeated factors and intersections of distinct factors and gives normality by R1 and S2. Independent finite replay over F₃ at n=5 gave 2,421 corank-at-least-two and 2,340 rank-four star matrices in the Jacobian support, out of 59,049 total matrices. Exact rational checks of the witness ranks and transverse directions for 5≤n≤12 agree, but the uniform conclusions follow from the symbolic argument. The supplied script was read, not run. This validates reduced support only, except for the explicitly determinantal scheme intersections.

## originality

PASS

The irreducibility, codimension, primeness and degree of Y_n are exact prior coverage. The distinct contribution supported by this review is the complete hollow Jacobian support and incidence with its excess rank-(n−1) strata, including the two uniform and different generic normal forms.

## value

PASS

Removing diagonals from a natural determinantal hypersurface creates lower-dimensional singular components at corank one that are invisible to the usual corank criterion. The incidence and contrasting generic quadratic forms give a usable description of the non-equidimensional singular set, beyond recomputing known Gram rank invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
