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

The environmental interior equations force x=x_* and y=y_* and exactly the stated resonance; the two strategy equations then force n_1+n_12=n_2+n_12=kappa, with 0<kappa<2 and the stated endpoints. Direct differentiation gives the displayed Jacobian. Independently of the quartic Hurwitz test, eliminate the environmental coordinates at a nonzero eigenvalue and scale the strategy perturbations by diag(p,q)^(-1/2). The resulting pencil is lambda^2 I+lambda D+K, with e=(sqrt(p),sqrt(q)), D=alpha e e^T and K=beta diag(pu,qr)+beta t e e^T. K is positive definite. Taking the Hermitian product with a pencil eigenvector yields a scalar quadratic with positive mass and stiffness and nonnegative damping, hence Re lambda<=0; zero-real-part roots require Dv=0 and Kv=omega^2 v. The line orthogonal to e has both coordinates nonzero and is an eigenspace of K exactly when pu=qr, equivalently x_*=y_* because pu=w(1-x_*) and qr=w(1-y_*). In that case the two eigendirections give precisely the imaginary pair and the damped quadratic. The five-variable characteristic determinant is lambda times the pencil determinant by the block determinant formula, extending the equality to zero; det K>0 proves the tangent zero is simple. Expanding the pencil gives the stated quartic and its squared Hurwitz difference. Differentiating each environmental logit cancels all terms in H dot; on the equilibrium curve H is strictly increasing and ranges from minus to plus infinity. Locally H is a regular coordinate since its n_12 derivative is positive, and each level has a unique equilibrium obtained by inverting H(E_s). In coordinates subtracting this equilibrium on the level, the other four variables have a strictly Hurwitz linearization, yielding local exponential convergence by the stable-equilibrium estimate, uniformly near compact portions using an extension along the open curve. This does not require trapping the limit in any prechosen closed subsegment if the initial H lies outside its image.

## originality

PASS

The source model, equilibrium continuum, logit resonance and stability of some symmetric reduced directions are credited as background. The strongest inspected same-model results do not recover the omitted community-asymmetric modes in the full five-dimensional resonant linearization or establish the exact condition for strict transverse damping. The supported distinction is that all four transverse modes decay precisely away from equal responses, together with local limit selection in that regime.

## value

PASS

The symmetry-reduced attractor can obscure a full-system undamped pair. The resonance family and balanced mixing are meaningful precisely because the equilibria form a curve and strategy damping has rank one. Classifying when environmental response asymmetry transfers that damping to all transverse modes closes a specific stability gap in the full model, with an exact conserved quantity predicting the local limiting point rather than merely convergence to a set.

The dated certificate retains the supplied scientific assessment, sources and limitations.
