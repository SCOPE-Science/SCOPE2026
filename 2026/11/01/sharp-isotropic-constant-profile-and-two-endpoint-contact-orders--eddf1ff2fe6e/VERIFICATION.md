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

Slicing at S=sum X_i gives density n s^(n−1)/(1−t^n) and independent uniform barycentric proportions. Their second-moment matrix yields transverse eigenvalue E[S²]/[n(n+1)] and axial eigenvalue Var(S)/n; dividing their determinant by (a/n!)² proves the stated profile and simplex baseline. For the derivative, an independent formal chain rule in t and u=t^n recovers the sparse numerator −n(n+2)t^(n−1)(1−t)B_n. Analyticity of H at 1 follows by setting S=1−hY: the law of Y on [0,1] has a normalized polynomial weight, and the factor h² in Var(S) cancels the volume-square factor. The substitutions a(1/t)=−t^−n a(t), and likewise for b,c, give H(1/t)=H(t) and H'(1)=0. With the derivative prefactors, this forces (1−t)^6 to divide B_n. Its quotient has degree 2n−3 and is palindromic. Its coefficients through degree n−2 come from ((n−1)−(n+3)t)/(1−t)^6 and equal positive [(5(n−1)−4j)/5] binom(j+4,4); reflection covers every coefficient including n=2. Thus H'<0 on (0,1), with continuity giving strict decrease from t=0 too. Expanding E and a gives the first deficit (n−1)(n+2)t^n. The thin slice has E[S²]→1 and Var(S)/h²→1/12; using volume a/n! gives the stated finite endpoint and e²/12 dimensional limit. Independent second-order expansion using the density of Y proportional to (1−hY)^(n−1) gives zero linear term and relative quadratic term (n−1)(n+3)h²/30. Both coefficients are nonzero for all n≥2; no assertion assigns an isotropic constant to the degenerate t=1 body.

## originality

PASS

Best-of-knowledge pass for the all-dimensional ordered profile with both exact endpoint contacts. An indexed theorem exactly matches the dimension-three specialization, not the n-dependent theorem; the exact normalization, ordering and contacts there must not be counted as an additional new result. The inspected same-family mixed-volume and homothetic-frustum polar-volume theorems concern different invariants. Raw covariance moments admit a standard homothetic subtraction calculation, but that calculation alone is not ordered monotonicity in all dimensions. No inspected result supplies the all-dimensional ordering and derivative sign mechanism.

## value

PASS

The all-dimensional strict ordering is stronger than a simplex-endpoint inequality and captures how the affine-normalized covariance changes under a natural one-vertex deformation. The exact, different contact orders quantify how weakly a small removed cap changes this invariant and how the normalized thin endpoint is reached. The coefficient mechanism is uniform, not an isolated depth sample or a recasting of the known dimension-three calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
