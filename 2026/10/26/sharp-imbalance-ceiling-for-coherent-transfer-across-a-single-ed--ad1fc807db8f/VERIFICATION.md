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

Degrees a−1,a and b−1,b give the four-cell invariant quotient and leave the nonbridge zero-sum spaces supported on their own sides. In the interior/bridge ordering, two eigenvalues tend to one and two to zero. For λ near one, subtracting the Schur complement at λ=1 bounds the difference by O(k^−1)|λ−1|, where k=min(a,b). At λ=1 the diagonal 1/a terms cancel to first order against −1/(a−1), and similarly on the right. Thus the estimate |λ−1|≤O(k^−2)+O(k^−1)|λ−1| supplies the bootstrap implicit in line 77. The next-order 2×2 term has diagonal (−a^−2,−b^−2) and off-diagonal (ab)^−1, and its O(k^−3) error is smaller than the spectral split on comparable sizes. Its orthogonal interior directions are (a,b) and (b,−a); the exact Perron eigenvalue is one. Upper modes have O(k^−1/2) bridge components and lower-mode leakage from an interior input is O(k^−1/2) in norm, uniformly in time by unitarity. The two surviving cross coefficients are opposite and of magnitude ab/(a²+b²)+o(1), and their phase difference on t=τab is asymptotic to τ(ρ+ρ^−1) locally uniformly. The same two-term representation bounds the all-time supremum from above without expanding a phase for unbounded t, and t=π/(λ_+−λ_−) gives the matching lower bound; the explicit time in the Finding is asymptotically equivalent. Right-bridge probability is negligible uniformly, and at t=o(ab) the relative phase vanishes. A nonbridge vertex has exactly 1/(a−1) of its squared norm in the interior-uniform component, with the rest trapped on the left, proving the localized optimum. Finite numerical diagnostics were inspected, not executed or used as proof of the limits.

## originality

PASS

The supported distinct contribution is the comparable unequal-size asymptotic with both all-time observables and the quantitative nonbridge preparation contrast. Equal-size exact spectral information and dark modes already appear in Dhamapurkar–Subrahmanyam. The normalized-Laplacian formulation is an alias for these probabilities with real preparations, but the inspected vertex-transfer theorems do not cover the collective asymptotic. The strongest indexed neighbors address different dynamics, geometry or optimization.

## value

PASS

The calculation identifies which finite size imbalances survive as a macroscopic transfer deficit. The uniform all-time bound rules out recovery of high fidelity at much later times, which the scaled-time limit alone would not exclude. The localized dark-mode identity quantifies why collective and vertex-localized preparations behave differently under the same Hamiltonian.

The dated certificate retains the supplied scientific assessment, sources and limitations.
