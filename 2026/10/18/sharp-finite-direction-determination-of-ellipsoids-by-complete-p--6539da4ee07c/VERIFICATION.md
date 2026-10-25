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

An ellipsoid c+Q^{1/2}B_d has section support midpoint u.c and squared halfwidth u^TQu, while amplitude determines det Q, so all full profile data reduce to these measured quantities. Span{uu^T}=Sym_d gives an injective linear shape-matrix map and center recovery. For any subcritical view set a nonzero indefinite H exists in its kernel: if normals span R^d, any nonzero semidefinite H vanishing on them is zero; otherwise w orthogonal to normals gives H=wv^T+vw^T indefinite. det(I+sH) tends to zero at both ends of a bounded positive-definite pencil and attains each interior level twice; these two distinct ellipsoids have the same determinants, midpoints and halfwidths, proving strict lower bound even with known volume. Exact coordinate/bisector inversion yields Q_ij=s_ij-(s_i+s_j)/2 and |err|<=2epsilon. Inspected exact rational checker for d=2..7 and its explicit opposite offdiagonal same-determinant pair; these illustrate, not replace, general proof.

## originality

PASS

Classical determination of a symmetric matrix from enough evaluations of its quadratic form and the ellipsoid section formula are known. The specific sharp universal calibrated finite full-section-profile reconstruction, including equal-volume nonidentifiability for every subcritical view configuration, goes beyond the all-direction convex-body results inspected in Fish–Ryabogin–Sun–Yaskin, and beyond published unoriented random-section moment inversion where directions are averaged rather than calibrated. Prior quadratic measurement or tomography literature may have equivalent linear-span criteria; risk retained.

## value

PASS

A precise optimal acquisition theorem for a natural inverse geometric tomography problem, with an explicit optimal view design, exact stable reconstruction, and a determinant-aware lower bound. The complete classification of good directional frames is useful even though the linear interpolation aspect is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
