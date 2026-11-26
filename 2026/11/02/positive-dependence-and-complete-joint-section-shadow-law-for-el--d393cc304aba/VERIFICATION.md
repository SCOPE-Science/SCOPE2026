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

Final assessment is for repairs/3/RESULT.md. The frozen raw-volume density rule tests membership after squaring s and h without requiring s,h>0; read literally as a density on R² it assigns spurious density to sign reflections and can even be negative. The repair explicitly restricts to the positive quadrant and gives zero elsewhere. It also distinguishes closed topological support from a boundary of zero mass, and scopes the repeated-axis density exclusion to the triaxial formula. The complementary-minor identity for A² and A⁻² proves both volume formulas. Independent gamma ratios Z_k=P_k/P_{k+1} have Beta(k/2,1/2) law jointly independent (each ratio is independent of its new total, iteratively), and P_k is their tail product. Summation by parts shows both raw volumes are nondecreasing in these independent coordinates; conditioning on all but one coordinate with a positive spectral gap gives strictly positive conditional covariance, while association of the remaining coordinates makes the covariance of the conditional means nonnegative. Balls are deterministic. Positivity of the Dirichlet law on the simplex gives the entire convex hull, strict convexity gives its dimension, and the two-level affine identity gives the positive comonotone curve. In dimension three with distinct λ the barycentric inverse takes the respective values 1,0,0 at the vertices; the affine determinant has magnitude Δ and the Dirichlet normalization is 1/(2π). The positive-quadrant change of variables is bijective with absolute Jacobian 4h/s³, proving the repaired density, normalization and direction recovery up to signs. The uploaded numerical checker was inspected, not executed; the analytic replay covers the final exact claim and no scientific change to support is needed.

## originality

PASS

The repaired record's distinct supported result is all-dimensional association of the same-normal central section and projection volumes, including strict positive covariance precisely off the ball. The old geometry and classical Dirichlet law are credited; their explicit triaxial affine change of variables and inverse are useful joint-law formulas, not a separate novelty credit for the underlying geometry or a routine Jacobian. The earlier same-normal tomography result does not assert association and uses the scalar product TV rather than the raw paired law to infer shape. A later catalogue finding gives an equivalent triaxial density and inverse after scaling a width–brightness pair, but does not furnish the raw-volume association theorem. This is a bounded prior-coverage assessment.

## value

PASS

Both observables are natural and measured in the same direction. Even with known marginals, the joint dependence is undetermined; full association (not just one covariance) and strict nonball positivity give concrete multivariate constraints in every dimension. The explicit positive-domain triaxial law and squared-coordinate inversion make the dependence quantitatively usable, while the known geometry and scalar inverse are credited. The result does not require a higher-dimensional elementary density or a downstream application to be substantive.

The dated certificate retains the supplied scientific assessment, sources and limitations.
