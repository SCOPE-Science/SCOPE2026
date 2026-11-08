---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

Radial monomial moments (alpha+1)B(p,alpha+1) yield a pair interaction with curvature u_alpha at right-angle separations and v_alpha at opposite separations. The real four-by-four Hessian is twice a four-cycle Laplacian with edge weight u plus two opposite chords with weight v, so Fourier vectors give 0,4(u+v),4(u+v),8u. Dividing the positive integrals expresses u/v as the mean of R(t)=4t(1+t)^4/(1+t^2)^3 under a measure proportional to (1-t)^{alpha+1}/(1+t)^3; R is strictly increasing, and increasing alpha strictly shifts mass toward zero. Hence u/v decreases strictly and continuously from 2 to 0. Exact endpoint integrals give positive u2-v2 and negative u3-v3 with rational pi/log2 bounds, guaranteeing a unique crossing in (2,3). Taylor’s theorem gives sharp half-minimal-eigenvalue local stability, while beta moment expansion gives u~4/alpha,v→1 and condition number alpha/8. An independent quadrature/Hessian eigensystem computation across weights and root-finding at alpha=2.727841735937447 supports these identities; only the analytic monotonicity proves uniqueness.

## originality

PASS

The complete published fixed-weight N-pole Fourier Hessian theorem was read in full: it explicitly fixes weight (1-|z|²), i.e. alpha=1, and establishes the least first mode at that exponent, not a continuous-alpha crossing. General Chui global equispaced optimality/convexity papers treat minimization, but that does not determine the ordering of the two Hessian eigenfamilies as alpha>1 varies. The new statement is a sharp one-parameter modal transition for exactly four poles; not the existence of a global minimizer.

## value

PASS

The crossover is a motivated spectral-stability phase transition: it exactly identifies when the geometrically soft deformation switches representation and when the local Hessian is isotropic. Both the unique critical weight and the large-alpha conditioning law provide useful precise local quantitative information not implied by global optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
