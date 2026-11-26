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

In the five-point equation the two extreme coefficients come only from Δλ² and are λ²/T² and (1−λ)²/T². Both are nonzero in the open interval; the recurrence can be solved globally in either direction and the signed companion determinant is the positive ratio (1−λ)²/λ². At λ=1/2, z_{k+1}=z_{k−1}. In the state ordering in RESULT, (E,O)=(p2,p1) and (νe,νo)=(z_k,z_{k−1}) with k even. The remaining two p coordinates are reconstructed linearly for fixed E,O from the definitions of νe,νo. In this chart one step is (E,O,νe,νo)↦(O+2T(νe−L(E)),E,νo,νe). Two steps thus fix the labels and apply two unit-determinant shears. Period two forces an alternating scalar sequence; every such sequence satisfies the equation and has prime period precisely when the values differ. The leaf Jacobian is the product of the two triangular shear derivatives, with trace 2+4T²L′(u)L′(v) and determinant 1; the full derivative has two additional unit eigenvalues. At either trace boundary the pair is called parabolic in the stated spectral sense, without a Jordan or nonlinear-stability assertion. A periodic orbit cannot attract an open set: its finite set of F²-label pairs excludes nearby points with other invariant pairs; return maps on the individual leaves additionally preserve area. This proof uses no passivity assumption beyond the illustrative example and does not depend on executing the packaged finite checks.

## originality

PASS

Credit the explicit global full-state reduction and complete period-two return spectrum for this particular fourth-order recurrence. The model, midpoint operator, implicit parity relation, and general symplectic-shear method are prior or immediate; they are not distinct contributions here. The strongest inspected primary passages do not state the full normal form and sharp Floquet classification.

## value

PASS

For a discrete circuit model intended to support nontrivial dynamics, the exact centered chart reduces a four-state return problem to a family of planar maps without losing orbits or excluding leaves. The complete Floquet criterion identifies all possible linear transverse types directly from device derivatives and rules out attracting periodic behavior at the centered parameter, while allowing both an elliptic and a hyperbolic example within one passive characteristic. This is a model-specific dynamical boundary, not a claim of nonlinear elliptic stability or a new generic integrator.

The dated certificate retains the supplied scientific assessment, sources and limitations.
