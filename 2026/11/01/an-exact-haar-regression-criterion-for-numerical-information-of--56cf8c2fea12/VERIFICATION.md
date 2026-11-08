---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For complex Haar x on the n-sphere, E|<Rx,x>|²=(tr RR*+|tr R|²)/(n(n+1)). Hilbert–Schmidt orthogonality to span_C{I,A,A*} makes the stated distance bound the exact best affine L² error. With normal A=Σλ_j P_j, block-Haar symmetry yields E[<Bx,x>|T]=Σ T_j tr(BP_j)/rank P_j with Dirichlet positive block masses; affine-independent distinct λ_j (at most three noncollinear planar vertices) uniquely recover all T_j from Z=Σλ_jT_j, hence this predictor is affine in Z and Zbar and is the nonlinear conditional expectation. Conversely, if every spectral projector has affine conditional mean, at extreme spectral vertices it tends to Kronecker boundary values; for ≥3 collinear distinct λ, a nonextreme spectral value gives an affine function zero at both segment ends but positive mean, and for non-simplex polygons a nonextreme λ or ≥4 extreme vertices forces an affine function zero at three noncollinear vertices but positive mean. Thus an actual spectral projection strictly beats affine regression. The exact n=3 symmetric Dirichlet joint density gives predictor (1-|t|)/2, conditional variance E=1/24, affine residual 1/18. No claim for nonnormal/infinite-dimensional operators.

## originality

PASS

Qualified PASS for complete normal-matrix classification of equality of the best nonlinear Haar mean-square prediction and the best affine prediction, including strict failure and exact three-level error. Johnson 2026 Thm 4.2 and Thm 5.2 give pointwise zero-error/factorization and sigma-algebra inclusion B∈span{I,A,A*}, not conditional expectation for arbitrary B or its L² residual. Numerical shadow/Dirichlet spline literature motivates marginal laws but no dominating conditional regression classification was identified in bounded primary comparison.

## value

PASS

A natural, nontrivial quantitative analogue of pointwise numerical information: determines exactly when observing one normal numerical shadow leaves no nonlinear regression advantage for any quadratic observable and exhibits the first 3-level obstruction with exact 25% loss reduction. The spectral-simplex boundary is structural, not a contrived matrix calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
