---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

On cubic physical-time interpolants with long-step nodes 0,-r,-r-1,-2r-1 and short-step nodes 0,-1,-1-r,-2-r, the exact Lagrange derivative coefficients have newest-value terms (5r^2+5r+1)/(r(r+1)(2r+1)) and (r^2+5r+5)/((r+1)(r+2)). Enforcing y'=−lambda y multiplies the first row of each zero-equation companion by d_i/(d_i+q), where q=lambda*h>0. An independent symbolic interpolation calculation reproduced every entry of both submitted 3x3 matrices for arbitrary r,q>0, and all six leading first-row limits. Hence A tends to [[2/q,-2/q,0],[1,0,0],[0,1,0]], B to [[1/(1+q),0,0],[1,0,0],[0,1,0]]. The product has exact characteristic z^2(z+2/(1+q)), yielding spectral radius 2/(1+q) by continuity of matrix spectrum, with strict eventual regimes q<1 (unstable) and q>1 (stable), while q=1 finite-r classification is deliberately excluded. At r=100,q=1/10 the independent exact determinant det(I+BA)=-4621393451/14621500436<0; the nonreal conjugate factors in det(I+P) are positive, so a negative determinant forces a real Floquet multiplier below -1. All claims are for unrestricted triples and repeated alternating periods; neither test-case checks nor zero-stability alone establish the all-r limit.

## originality

PASS

Best-of-knowledge narrow originality PASS: the inspected primary Li–Liao 2022 theorem supplies BDF3 stability under adjacent ratio <2.553, and Liao–Tang–Zhou 2022 gives energy/convergence results under ratio <1.4877; neither covers r->infinity alternating ratios. The latter paper does study periodic alternating grids experimentally at finite µ but not the fixed-q infinitely repeated scalar test-equation Floquet spectrum. Guglielmi–Zennaro (2001), Skeel–Jackson (1983), and Calvo et al. concern spectral/zero-stability or Nordsieck method bounds; for Guglielmi–Zennaro only the abstract was accessible, so historical priority remains a real explicit risk. The separate published BDF2 sign-loss result addresses positivity, not BDF3 repeated-period instability. No source that implies the exact q-dependent 2/(1+q) law or its finite certificate was identified. Search failure is not proof of priority, and the BDF interpolation/Jury/Floquet techniques are classical.

## value

PASS

Alternating long and short steps are a natural diagnostic pattern for an adaptive BDF stiff solver. The exact Floquet multiplier limit shows a qualitative loss of negative-real-axis absolute stability despite exact ODE dissipation, and identifies the sharp fixed-q damping separation between eventual growth (0<q<1) and decay (q>1) as r becomes extreme. The exact finite unstable rational example establishes that it is not only an artifact of the limiting matrix. This gives a motivated nontrivial stability boundary for a standard numerical method rather than a table recomputation. It does not claim mesh-refinement convergence or a general nonlinear/nonperiodic theorem; the result is a narrow but independently useful counterexample/structural asymptotic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
