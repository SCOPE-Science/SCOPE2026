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

For n>=3 and 0<δ<1, strict convexity of H=(1−δ)I+δ11^T yields a unique interior equilibrium q1 and a pathwise nonincreasing quadratic error potential. The prescribed strict ellipsoid implies ||e||_2<r and every coordinate update remains strictly interior, excluding clipping at all times. The identity e_i′=−δ(S−e_i) leads to S′=(1−δ)(S−e_i), Q′=Q−e_i²+δ²(S−e_i)² and exact averaging Σ(S−e_i)²=(n−2)S²+Q. This proves the displayed 2×2 evolution of E[S²],E[Q] for all steps. Strictly positive matrix entries and det(I−T)>0 imply 0<σ<ρ<1; from F_1≥(d/n)F_0 and σ<d/n, the Perron coefficient is strictly positive for every deterministic nonzero perturbation. Eigenvalue expansion gives both δ↑1 and n→∞ constants. Independent exact rational update-string enumeration matched each moment in four cases n=3..6 through depth four (81,256,625,1296 strings).

## originality

PASS

The same Misiak–Dziubiński 2026 complete-network random-order public-good model has convergence bounds and numerical clique slowdown; it does not state the exact Euclidean two-moment matrix or universal initial-profile mean-square Perron factor. Gower–Richtárik randomized iterative method theory gives general expected squared norm inequalities rather than this special second-moment identity and its two sharp limits. A closely related Resultary entry on delayed two-coordinate Gauss–Seidel studies a different stochastic recurrence, not this game. The contribution is an exact symmetry reduction of an established algorithm, not a new general stochastic convergence theory.

## value

PASS

The exact mean-square relaxation rate is a natural observable for a canonical symmetric best-response game, not a arbitrary slice. The finite-dimensional closure yields all-time formulas and two sharp slowdown asymptotics with guaranteed generic coefficient, sharpening formerly numerical and inequality-based understanding of complete-network stochastic convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
