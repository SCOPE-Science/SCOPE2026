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

Every counted exchange changes the lumped shore occupancy by one; there are no hidden within-shore jumps. An independent derivation uses the martingale for the count plus the martingale for h solving -Qh=λ-μ. Up to a bounded endpoint term their sum equals C_T-μT, with jump increments 1+Δh. The stationary cross term is 2πQh=0, giving variance rate μ+2⟨h,-Qh⟩. Reversibility and the triangular action on polynomials give the centered degree-one and orthogonal degree-two modes at N and 2(N-1). For an independent norm check, the upward-edge weights π_j u_j have total μ/2 and, normalized, are hypergeometric with parameters N-2, a-1, k-1. Orthogonality to the linear mode forces ΔH₂ to be twice j minus twice the edge mean; its Dirichlet energy is 2μ times the edge variance. Thus ||H₂||²=μ Var_edge(J)/(N-1), exactly the displayed fourth-moment formula, also when the edge variance is zero. Substitution gives both nonnegative corrections. Their simultaneous zeros give precisely the stated cases, where a constant exit rate gives a Poisson clock. Multiplying the two contributions by N in the joint window yields 16u²v² and 1/4. The supplied script was inspected, not run: it compares exact full-state Poisson solves and a symbolic norm identity; the window portion independently asserts only positivity and prints comparisons, not a convergence certificate.

## originality

PASS

The supported distinction is the explicit all-inventory, all-actual-exchange cumulant ratio and its joint scaling law. The exact generator and spectral structure are prior, and the Poisson equality cases and a fixed-inventory slice overlap materially with separate catalogue findings. None of the inspected exact statements supplies the general evaluated ratio or the joint scaling. The decision is limited to the evidence checked, not universal priority.

## value

PASS

The exact noise of the successful exchange clock is a natural dynamical observable not determined by the relaxation spectrum alone. The positive quadratic-mode contribution distinguishes exactly balanced dense chains from truly Poisson chains despite F→1, and gives the residual 1/(4N) noise floor and the joint N^(-1/4) crossover. This is useful beyond re-deriving the known eigenvalues or the k=2 slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
