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

The Pires–Rosales logistic response becomes exactly tanh(t/2) after centering the first-urn proportions, so α=−2a gives the stated drift. Taking artanh reduces the fixed equations to artanh(z_i)−az_i=−aΣz_j for all i. For 0<a≤1 this scalar left side is strictly increasing, including at a=1 where its derivative vanishes only at 0. Equal coordinates then force zero. For a>1, artanh(r)/r is strictly increasing from 1 to infinity; its root gives the six polarized permutations. The repeated-coordinate branch function H_a has positive slope at zero, strictly negative second derivative on (0,1) and limit −∞ at 1, giving a unique positive root b and v>b. The three placements for each sign are distinct from each other and from the polarized points. At zero the eigenvalues are −1−2a and a−1 twice. The frozen Jacobian formula with row factor 1−z_i² is the Jacobian evaluated at an equilibrium; at arbitrary z the corresponding factor is sech²(aΣ_{j≠i}z_j). At (r,0,−r), the antisymmetric eigenvalue is as−1 for s=1−r²; the other block has trace −2−as and determinant 1+as−2a²s. With u=artanh(r), as=2u/sinh(2u)<1 and the determinant times sinh²u is sinh²u+u tanh u−2u²>0 by the strict bound sinh²u>u²+u⁴/3 and tanh u≥u−u³/3. Thus all six polarized points are strictly linearly stable for the ODE. Independent branch residuals and equivalent symmetric Jacobian principal-minor signs were checked at five u values; no finite run exhausts equilibria or interaction strengths.

## originality

PASS

The underlying urn model, its conditional stochastic convergence theorem, a sufficient small-interaction uniqueness condition and its Hopfield interpretation are prior art. The supported distinct claim is the sharp antagonistic threshold for the specified logistic model, with explicit thirteen-point lower bound and six strictly stable polarized equilibria of its ODE for all a>1. An exact thirteen/six pattern in an earlier cubic K₃ model is a serious comparison but the response laws differ and the stable branches in the two inspected claims have different symmetry types.

## value

PASS

The transition resolves where a prior sufficient uniqueness range gives way to multistability in a specific urn drift. Explicit branches exhibit two different symmetry types, and the analytic strict stability certificate identifies six robust ODE attractors without a coupling cutoff. The result is useful for the fixed-point structure even without a full equilibrium census or stochastic selection theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
