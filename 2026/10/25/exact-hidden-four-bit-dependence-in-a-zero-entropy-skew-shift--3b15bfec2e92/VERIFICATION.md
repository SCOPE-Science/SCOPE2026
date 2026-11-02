---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Iterating the skew map gives y_j=y+jx+j(j−1)alpha/2, and Haar invariance. Every distinct-time pair is uniform on T² because the integer two-time character matrix has nonzero determinant, while translating y by 1/2 flips all signs; Walsh inversion implies every triple is uniform. For irrational alpha, polynomial Weyl equidistribution yields unique ergodicity; O(n) spanning numbers at fixed accuracy give topological entropy 0, hence factor entropy0. Fourier coefficients of the half-circle sign are 2/(i pi k) for odd k. The two torus-character constraints reduce the 4-point AP correlation to an absolutely convergent sum with coefficient 1/27 at zero and 6 sin(2pi r/3)/(pi³r³) for nonzero r, determining the stated continuous piecewise quadratic Theta. The transformation x↦hx+binom(h,2)alpha pushes Haar to Haar, giving Theta(h²alpha). Exceptional roots modulo half period are t=1/(4sqrt3) and 1/2-1/(4sqrt3); Theta(4alpha)=−9+16/sqrt3>0, so not 4-wise independent globally. Independently evaluated two-torus midpoint grids (1800² points per test) at five parameters; absolute discrepancies below 0.004. Finite grids do not establish Fourier identity.

## originality

PASS

Novelty is a qualified best-of-knowledge mathematical comparison, not a guarantee of priority; exact original claim was searched against equivalent formulations, general theorems and data tables.

## value

PASS

The construction separates local 3-wise independence from zero entropy and gives a completely explicit, nontrivial four-bit dependence law including a finite-lag witness valid for every irrational parameter. Exact finite-dimensional distributions for a natural nilsystem coding are mathematically useful to ergodic-theoretic counterexamples, entropy/mixing distinctions, and pseudorandomness, not just a renaming of standard Walsh inversion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
