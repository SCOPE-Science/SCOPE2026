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

For the stated Fourier sign, the divided-difference multiplier is (-i)^(-3)=-i; the constant-weight sum vanishes identically wherever the four phases are distinct. At the given reciprocal node, subtracting the constant exponential term leaves first real jet -sum w_j delta_j and quadratic imaginary jet (1/2)sum w_j delta_j^2. Denominator variation cannot contribute an imaginary quadratic term because the first exponential term becomes real. The real zero equation has nonzero gradient. On its tangent plane, elimination of v_3 gives determinant -w_0 w_1 w_2 w_3/w_3^2 for the quadratic matrix before the factor 1/2. The product of the four weights is positive because the six unordered pairs give six signs in the Vandermonde product. The restricted Hessian is therefore a saddle. The analytic Morse coordinates make its zero set precisely two axes on the real-zero surface: distinct tangent lines, and rank two off the crossing. At (1,2,3) the restricted quadratic factors as (v_2-v_1)(v_2-2v_1) after the common scale, giving the stated directions. The affine transport is invertible and multiplication by the nonzero translation factor preserves both zeros and the equation rank there.

## originality

PASS

The transform formula and the lattice-zero cancellation are covered. The strongest retrieved polytopal zero-set theorems constrain specific hypersurfaces or globally parameterized curves rather than determining the local real analytic germ at these lattice nodes. The nearby lattice catalogues classify discrete zeros only. No inspected source establishes the universal crossing or its two tangent lines.

## value

PASS

Complete reciprocal lattice nodes are naturally selected by exact phase cancellation, and their first Jacobian has insufficient rank to classify the zero set. The result distinguishes two crossing real branches from an isolated or higher-order singularity, gives their directions at every such node, and transfers to any affine tetrahedron. This is useful local geometry that a lattice census or transform evaluation does not recover.

The dated certificate retains the supplied scientific assessment, sources and limitations.
