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

Functional calculus for unitary U gives ||Re(e^(−it)U)||=max_{ζ∈σ(U)}|cos(t−argζ)|=cos d(t,S), with S the compact antipodal spectrum on circle of length π. The period-π angular normalization converts the defining 1/(2π) integral to 1/π ∫cos²d. Each complement gap ℓ contributes deficit (ℓ−sinℓ)/2 and the countable sum is absolutely convergent because Σℓ≤π; no finiteness or atomic-spectrum assumption is imposed. Equality at lower 1/2 requires one gap of length π, i.e. U² scalar; upper 1 requires no gaps, i.e. full projective spectrum. For q distinct projective eigenclasses, concavity of sin and strict monotonicity q sin(π/q) give sharp n-dimensional bound and equality classes. Independent numerical midpoint integration agreed with the exact formula for q=1,2,3 nonuniform and q=8 evenly spaced within 2×10^(−10); these finite checks corroborate rather than prove the infinite spectral statement.

## originality

PASS

The defining Audeh–Moradi–Sahoo paper, read at Theorem 17 and adjacent results, proves only general normal/commuting operator upper/lower bounds and a proportional-Cartesian-parts equality, not exact arbitrary unitary spectral geometry. The novel gap-by-gap functional and finite-dimension equality characterization are not corollaries of those inequalities alone. Related convex-support-function integration could contain an equivalent classical formula, but none was identified in material searches. Originality passes best of knowledge, not historical uniqueness.

## value

PASS

The new numerical radius is a natural operator invariant. The theorem gives exact values for arbitrary continuous/infinite unitary spectra and a complete sharp n-dimensional extremal theorem with all equality spectra, replacing loose general bounds with a spectral-geometric classification. This is not a renamed operator-norm inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
