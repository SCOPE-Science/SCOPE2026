---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Vertex and edge transitivity give respectively P_ii=k/n and edge leverage k mu/m for the k-dimensional base Fiedler projector P. The lifted mean-zero vectors (r phi,(1+r) phi) therefore have summed energy kB/n and summed squared norm k[r^2+(1+r)^2], proving the budget upper bound for any assignment, even one with zero rates. With b=b_* constant, a base weighted eigenvalue xi yields a 2x2 block with eigenvalues (xi+2b +/- sqrt(xi^2+4b^2))/2. The lower branch is strictly increasing, starts at zero, and stays below b; the upper branch is at least 2b. At xi=a_* mu the lifted vector has eigenvalue lambda_* on the lower branch (it is below b_*), and the candidate meets the budget since mt a_*/(n lambda_*)=2r^2+r. Every optimal assignment must saturate each individual Rayleigh inequality. Its leaf equation forces b_i=b_* because for each vertex some Fiedler basis vector has a nonzero coordinate there. Then the budget fixes total base rate, and the block formula reduces the gap criterion to exactly base gap optimality, including the disconnected cases. On the cycle the imaginary parts of the first Fourier mode equation force equality of neighboring edges; on the clique all mean-zero directions must have the same eigenvalue, determining the full matrix. The positive uniform solution and both class expenditure fractions are as stated; no general uniqueness of base weights is needed. The recorded 4209 checks were inspected as finite illustrations, not rerun or used as universal proof.

## originality

PASS

Pass is for the supported distinct contribution: the characterization of every optimizer for general vertex- and edge-transitive bases, including forced uniform leaves and exact transfer to the full base optimal set. The cycle formula and unrestricted cycle uniqueness are explicitly covered; the general value and invariant rates also have a near-identical indexed counterpart. Neither is counted as distinct content against those comparators.

## value

PASS

An exact allocation alone could conceal qualitatively different asymmetric optima. The full transfer shows where all freedom in the design resides and which rates cannot change even in a symmetry-unconstrained solution. This is a structural characterization that remains useful despite exact overlap on the cycle specialization and general scalar value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
