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

Rayleigh minimization over fixed mean-zero unit vectors is concave in conductances, so dihedral averaging preserves feasibility and cannot lower the gap. The zero-sum rim subspace has Fourier minimum a+δ_m b. On the mean-zero complement of this subspace, take the normalized common-hub-and-leaf versus rim contrast and the normalized hub-minus-leaf vector. Their 2×2 matrix has diagonals (m+2)a/2 and ma/2+2c and off-diagonal √(m(m+2))a/2, giving the claimed characteristic polynomial. Subtract the identity: for a unit gap the first diagonal is strictly positive (if zero the off-diagonal is nonzero), and the determinant condition is c((m+2)a−2)≥(m+1)a−1. Together with b≥max(0,(1−a)/δ_m), this gives the exact scalar minimization. The rational term has derivative −m/((m+2)a−2)² and strictly positive second derivative. To the right of 1 the cost increases; to its left the derivative is m k_m−m/((m+2)a−2)². For m≥6, δ_m≤1 and it is negative including in the left limit at 1. For 3≤m≤5, δ_m is 3, 2, or (5−√5)/2, respectively, so k_m>1/m²; the unique left stationary point is the stated a_m<1, with positive b_m and c_m. Using s=(m+2)a_m−2=1/√k_m in the cost yields the displayed D_m. Scale by homogeneity to budget B. At m≥6 every optimum averages to the unique symmetric optimum with mean rim weight zero, so each original nonnegative rim weight is zero. The frozen slogan's stronger equal-star-spending phrasing is also true: after unit-gap normalization the star weights sum to m+1, and testing differences of two leaf coordinates forces each pair of star weights to sum to at least 2. If any weight is below 1 the other m exceed 1 by at least the same deficit, contradicting the budget. The least-cost spectral proof covers all m and real B, not only the numerical tests. The determinant and cost simplification replay with `python /workspace/independent_reproduction.py`; frozen verify.py was inspected, not executed.

## originality

PASS

The broad continuous-time formulation and its variance dual, symmetry reduction, and the very close unaugmented-wheel price transition are prior coverage. The distinct result is the explicit gap and weight formula with a hub-attached leaf and the strictly stronger cutoff at the hexagonal rim, including all-optimum rim deletion for that graph. The wheel result makes the comparison substantive: at equal prices and six rim vertices it instead allows positive rim conductance at optimum.

## value

PASS

A single bottleneck leaf changes the structure of optimal continuous-time mixing on a canonical symmetric graph, making all rim conductances dispensable already at six while leaving them essential to the smaller-size improvement. The exact gap and all-optimizer support provide an actionable graph-specific design rule beyond feasibility of an SDP, including a meaningful contrast with the hexagonal unaugmented wheel.

The dated certificate retains the supplied scientific assessment, sources and limitations.
