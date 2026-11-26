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

On connected conductance supports the trace-inverse Hessian is strictly positive for a nonzero Laplacian perturbation (diagonalize L+J and sum positive multiples of squared entries). Simplicity gives injectivity in the edge weights; the compact price simplex contains a finite star and the objective diverges at disconnected limits. Thus the unrestricted optimizer is unique and invariant on each spoke and peripheral orbit. The hub cannot be isolated. At the uniform star the spoke derivative is −N/a² and the peripheral derivative is −2(N+1)/a². Under the budget constraint any feasible infinitesimal addition of peripheral weight has derivative proportional to Nt−2(N+1); the convex supporting inequality, with strict convexity including at equality, gives exactly t≥t_c. For the symmetric optimum the hub mode has eigenvalue (N+1)a, and peripheral mean-zero modes have eigenvalues a+bλ, including extra zero modes of H. With q=td/2 and f=B𝒦/N, expand (1+qx)[1+(N+1)∑(1+λx)⁻¹]. The first three peripheral moments are Nd, Nd(d+1) and Nd³+3Nd²−6T. Consequently f_x=−pδ+hx+gδx+jx²+O(δx²+x³), with p=N²d/2, h=2(N+1)d(N−d)>0, g=(N+1)Nd², j=3(N+1)[d³+(1−2N)d²+6T]. The analytic stationary solution is positive just below threshold, with C=p/h and D=−(gC+jC²)/h, which simplifies to the displayed formula. The strictly increasing change from x to feasible b identifies this branch with the global minimizer by convexity in the original weights, without needing global convexity in x. The optimized gain is (N/B)p²δ²/(2h), exactly the stated coefficient. This includes d=N−1 and disconnected H as the formulas require only N−d>0 and the positive hub spokes.

## originality

PASS

No novelty credit is assigned to the trace-inverse design framework, star-chord screening threshold, or exact clique-bouquet specializations. The supported distinction is the degree-only slope and resistance curvature together with the triangle-sensitive second ratio coefficient for the full vertex- and edge-transitive class, including disconnected H. The strongest catalog match gives exact all-price formulas on unions of cliques, hence covers a genuine subfamily, but cannot express the same-order/same-degree triangle variation of the full result.

## value

PASS

The threshold alone says when an edge is worth using; the ratio slope and exact objective curvature quantify how much is deployed and how much resistance is saved near that threshold. The first graph discriminator is the triangle count, demonstrably separating models with equal size and degree, even when disconnected peripheries are allowed. This is a useful local design principle rather than a repetition of the binary screening test or a special-case numerical optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
