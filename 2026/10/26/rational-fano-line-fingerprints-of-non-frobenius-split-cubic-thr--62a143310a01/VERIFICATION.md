---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Fedder's characteristic-two criterion identifies the non-Frobenius-split forms F_A=Σ A_ij x_i²x_j. The gradient is A^T applied to coordinatewise squares, so smoothness over the algebraic closure is equivalent to A invertible, with Euler identity ensuring gradient singularities lie on the cubic. GL_5(F_2) acts by congruence P^TAP, with scalars trivial. Four coefficients of F_A(su+tv) vanish iff the scheme-theoretic line lies in the cubic. Reconstructed and executed an independent complete GL_5(F_2) orbit BFS with elementary transpositions/shear; it yields precisely the 13 quoted representative codes and orbit sizes summing to 9,999,360. A separate Python enumeration of all 155 F_2-lines for each representative verified all thirteen point counts, line counts and point-incidence histograms. The finite classification is exhaustive because all invertible 5x5 binary matrices are covered by the orbit count. No conclusions are drawn for F-split cubics or non-F_2 forms.

## originality

PASS

PASS (qualified): Prior finite-field congruence theory (Gow) covers the 13 bilinear-form orbits, which are not claimed as new. Cheng defines the entire q-bic Fano scheme via totally isotropic 2-planes over algebraically closed fields; his geometric results provide a criterion but not the full F_2-rational line-by-line and incidence table for all 13 arithmetic orbits. Debarre–Laface–Roulleau give individual small-field cubic threefold examples and algorithms, including smooth F_2 cubics without lines outside this special locus; neither inspected table covers these arithmetic fingerprints. Thus the new object is a complete arithmetic incidence refinement, not re-discovery of the 13-form count. Full historical equivalence remains qualified.

## value

PASS

PASS: The 13 rational congruence forms are the entire natural smooth nonsplit locus at the smallest field. Determining each rational Fano-line count and point–line incidence pattern is a natural finite classification of actual contained lines rather than a slice chosen to give a particular number. Unique 1-line and 27-line extremizers, equation-weighted distribution and complete distinguishing fingerprints give substantive geometric/arithmetic structure beyond the old orbit count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
