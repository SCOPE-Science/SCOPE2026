---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For maximal-rank square-zero X,Y in dimension 2m, im=ker for each; transversality yields intrinsic complementary U and W. Restriction maps X|W and Y|U are invertible, giving canonical blocks X0=[[0,I],[0,0]], Y_C=[[0,0],[C,0]]. A simultaneous similarity preserving both images and X0 is diag(P,P), so C similarity exactly captures pair orbits. Products XY and YX give opposite diagonal C blocks; alternating products and polynomial invertibility of C generate four block positions over k[C], yielding algebra M2(k[C]) and dimension 4deg(mu_C). Since C in GL_m, every minimal-polynomial degree 1..m occurs through unipotent Jordan blocks. Choosing U in Gaussian binomial [2m,m]_q ways, X-isomorphism in |GL_m| ways, W complement in q^(m²) ways, and Y-isomorphism correspondingly C, proves T=[2m,m]_q q^(m²) |GL_m| c_m,d. Rational-canonical centralizer formula counts c_m,d exactly. Independent complete GL2(F2) enumeration gave five degree-two and one degree-one matrices, matching (16800,3360) transverse pairs of total 20160; finite test corroborates full proof.

## originality

PASS

Classical work bounds algebra dimension for pairs of quadratic-minimal-polynomial matrices and gives invertible-cyclic-matrix enumerations. Neither inspected result gives the geometric transverse square-zero normalization linking *all* pair-conjugacy orbits to invertible similarity classes, nor the complete finite-field distribution by generated dimension. The exact orbit/frequency classification survives those prior implications; priority uncertainty remains for old unread article and quiver aliases.

## value

PASS

The transverse maximal-square-zero stratum is geometrically intrinsic and maximal dimension, not an arbitrary finite slice. It has a natural classification of two-generator associative algebra types and a complete frequency spectrum over every finite field. An exact cyclicity criterion identifies all and only pairs achieving largest possible generated algebra dimension. The computations refine a classical global bound and support quantitative finite-field structure calculations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
