---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

An invertible common affine change sends A to I and B to a determinant-one ellipse whose eigenvalues are lambda^2 and lambda^-2, so tr(A^-1 B)-2=(lambda-lambda^-1)^2 independent of orientation. The convex hull support h(phi)=max(1,sqrt(lambda²cos²phi+lambda^-2sin²phi)) changes branch precisely at beta=arctan lambda modulo pi. The support-area identity (1/2) integral(h²-h′²) over a full turn applies almost everywhere to this Lipschitz support and accounts for straight bitangent sides. The two explicit integrals yield 2(lambda-lambda^-1)+4 arctan(lambda^-1)=pi+2D-2 arctan(D/2); restoring common affine Jacobian contributes s. Derivatives G′=1+D²/(4+D²), G″=8D/(4+D²)² establish strict monotonicity/convexity, and arctan bounds and limiting lambda establish sharp 1,2 constants. Independent 12000-point hull area approximations on six disk/reciprocal-ellipse pairs agreed to <2.4e-7, separate from the continuum proof.

## originality

PASS

The Horváth--Lángi primary paper arXiv:1302.6164 establishes extremal hull volumes for isometric copies of one body under translation/reflection, with emphasis on congruent pairs. Its §§2-4 do not give a scalar trace-invariant area formula for two centered ellipses with equal determinant but differing eccentricities/orientations. Hughes--Chraibi arXiv:1106.3787 calculates ellipse overlap/intersection areas by numerical/quartic algorithms; that is a different operator than the convex hull and no exact simple spectral hull law follows from its stated method. The known question about a larger ellipse inside such a hull is a containment assertion, not the requested hull area. Best-of-knowledge novelty is specifically the exact affine spectral mismatch law with global sharp constants.

## value

PASS

The convex hull of two arbitrary centered equal-area ellipses is a natural geometric object. An affine-invariant single-scalar exact area classification (including unaligned/sheared semiaxes), the four-bitangent boundary decomposition, and globally sharp linear/convex stability profile quantify how mismatch enlarges a hull. The area law is an unknown self-contained exact fact with uses as a benchmark for ellipse geometry, not an arbitrary parameter substitution or numerically tabulated anecdote.

The dated certificate retains the supplied scientific assessment, sources and limitations.
