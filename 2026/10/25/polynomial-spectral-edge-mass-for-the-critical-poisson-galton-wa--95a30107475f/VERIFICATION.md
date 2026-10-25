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

The analytic checks are: (1) the branching generating-function identity \(F(z)=z\exp(F(z)-1)\) and Lagrange inversion yield \(\Pr(N=n)=e^{-n}n^{n-1}/n!\); (2) Stirling's formula gives two-sided \(n^{-3/2}\) bounds for all sufficiently large \(n\); (3) the conditioned-tree height theorem gives a positive-probability height at least \(a\sqrt n\); (4) the explicit diameter-path test function has energy \(d\) and variance at least \(d(d+1)(d+2)/12\); (5) summing normalized spectral mass gives the \(E^{3/2}\) lower bound. The result is analytic and uses no numerical simulation. The proof does not establish a matching upper bound, an exact asymptotic, or a finite-graph zero-atom convergence result.
