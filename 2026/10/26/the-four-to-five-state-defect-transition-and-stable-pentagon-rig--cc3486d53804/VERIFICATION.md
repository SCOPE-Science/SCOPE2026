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

The frozen exact claims are mathematically sound: 1, ξ₁, ξ₂ are orthonormal and the centered quadratics are perpendicular to them. At m=3 those quadratics would vanish at all atoms, contradicting rank; at m=4 their one-dimensional span forces xxᵀ=I+hB, with two distinct roots of det(I+hB)=0. Neither associated rank-one matrix is zero and their lines span the plane by isotropy, so each line carries precisely ±x with equal masses. Normalizing the two directions gives the orthogonal pair family and defect 1/[8p(1−p)]; regular polygons attain the universal 1/4 from five atoms on. In the narrowed final RESULT, the square-matrix argument gives both rigidity at zero and quantitative stability: tr K=(1/2)E s² for s=|ξ|²/2, so E(s−1)²≤4ε and both eigenvalues of K are within ε of 1/4. Moment cancellation and the complex fourth-moment identity give angular moments bounded by 7√ε; the row and column Gram deviations of the square weighted Vandermonde are at most 28√ε. The diagonal gives w_j≥0.19 and weight error ≤5.6√ε; the off-diagonal bounds the five-term geometric sums by 150√ε and fifth-power residuals by 300√ε. Nearest-root assignments cannot collide (a collision would force geometric-sum modulus ≥4.4, instead of ≤0.015), so all five roots occur. Adding the ≤5√ε radial error in s yields position error ≤305√2√ε<440√ε for ε>0, with the non-strict estimate also valid at zero. The exact five-atom assumption is necessary for the square Gram transfer. The final proof is analytic. The frozen checker was inspected, not executed; the 200 perturbed matrices do not in general satisfy the theorem's moment constraints. The repaired result makes no assertion about attaining the same stability at higher support or about optimal constants or exponent.

## originality

PASS

PASS is for the narrower theorem in repairs/3/RESULT.md, not a novelty pass for the original dual headline. The repair removes the exact support frontier and classifications as independent findings and credits the universal bound and exact five-node angular characterization as background. The older degree-three cubature bounds apply to these low moments, and the five-node equality classification follows directly from Tanaka and classical positive trigonometric quadrature. The distinct remaining result controls both masses and the full planar positions from energy excess, with no initial circle, separation, or lower mass hypotheses. No inspected result implies those bounds for this class.

## value

PASS

The repaired theorem answers a robustness question not settled by knowing the exact minimizer: whether an actual nearly optimal five-state increment rule must use almost equal probabilities and place each atom near a different pentagon vertex, despite no imposed radial or separation condition. The defect-to-geometry estimate gives explicit atomwise control of both quantities and a usable small-error range. It is a quantitative result for genuinely planar laws, not a certificate or relabeling of the classical exact cubature rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
