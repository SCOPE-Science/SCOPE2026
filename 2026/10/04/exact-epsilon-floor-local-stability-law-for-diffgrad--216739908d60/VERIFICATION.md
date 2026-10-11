---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The first-order reduction was reconstructed directly. At the zero orbit, \(v_t=\beta_2v_{t-1}+O(x_t^2)\), while \(\xi_t=1/2+O(|x_t-x_{t-1}|)\); because both corrections multiply the first-order momentum in the parameter step, neither changes the Jacobian. The limiting \((x,m)\) block has determinant \(\beta_1\), trace \(1+\beta_1-(1-\beta_1)\alpha\lambda/(2\varepsilon)\), and Jury stability exactly when \(0<\alpha\lambda/\varepsilon<4(1+\beta_1)/(1-\beta_1)\). Independent symbolic/numeric replay gave the upper root \(-1\) at the boundary, the cap 76 at \(\beta_1=0.9\), and the stated complex-root plateau with modulus \(\sqrt{\beta_1}\). The exponentially decaying bias-correction perturbation is compatible with the strict limiting hyperbolicity claim; no nonlinear claim is made at the unit-root boundary.

## originality

PASS

The source paper gives the exact diffGrad recurrence and the floor value \(\xi=1/2\), while Cohen et al. give the EMA-heavy-ball quadratic threshold. Neither inspected source states the local Jacobian of source-form diffGrad with epsilon outside the square root, proves that both the gradient-difference variation and adaptive second-moment variation disappear at first order, or gives the doubled ceiling and complex-root plateau. Bock--Weiß discuss Adam local convergence and the nondifferentiability caused by epsilon outside the square root, but not diffGrad. The audited theorem is therefore not merely a numerical retabulation of a published diffGrad theorem, though it deliberately uses the prior heavy-ball threshold once the reduction is proved.

## value

PASS

The exact local frontier is a motivated method-level boundary: diffGrad was introduced specifically to change oscillatory behavior near optima, and the theorem identifies which part of that mechanism survives infinitesimally, quantifies the exact doubling relative to frozen EMA momentum, and isolates the complex-root plateau. This is more informative than a generic optimizer substitution because it resolves a nonsmooth adaptive recurrence at its stationary orbit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
