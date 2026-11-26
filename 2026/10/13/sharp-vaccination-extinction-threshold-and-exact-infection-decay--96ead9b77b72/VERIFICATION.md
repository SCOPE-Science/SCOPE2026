---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Replayed RESULT.md lines 13–107 for the autonomous Holling-II model on the full nonnegative cone. Inward boundary derivatives and the host-population differential inequality give global bounded solutions, with bounded environmental coordinate from its stable filter equation. The S,V block is Hurwitz Metzler (trace negative, determinant D>0), and subtracting its nonnegative infection losses gives the exponentially convergent infection-free upper envelope. For the infected block, a positive test vector (H/ξ,1,φ/ω) has image (AH(R_c−1)/ξ,0,0) under B0. Multiplication by its positive left Perron vector proves the spectral sign equivalence, and the full linearization is block triangular. For R_c>1, the instability is also relative to the cone: any trajectory with a positive infected/contaminated sum that stayed in a sufficiently small disease-free neighborhood would grow by comparison with a constant lower Metzler block with positive spectral abscissa. Subcritically, the upper comparison block is strictly stable after a transient. At R_c=1 the left Perron projection W satisfies the stated upper inequality with an integrable envelope error and negative saturation term. Comparison against the linear lower bound on S gives an eventual positive S floor; integration then gives integrability of C²/(κ+C). Bounded derivatives give C→0 and C′→0, then I→0 and E→0; stable linear convolution returns the other coordinates to equilibrium. For small initial perturbations all needed coefficient bounds are uniform by the host and environment bounds, and the envelope error is proportional to the initial displacement, establishing Lyapunov stability as well as attraction. Finally B(t)→B0; the same positive left Perron projection satisfies W′/W=s(B0)+o(1) whenever the initial infected/contaminated sum is positive, since the perturbation term is bounded by o(1)W. This gives the exact normalized logarithmic rate, including zero at criticality and no positive exponential decay rate there. Independently checked the two rational witnesses using the factorized determinant (λ+2)²(λ+1)−b(λ+1)−b in that family: the displayed thresholds and characteristic coefficients agree, and (1,2,2) is the exact critical left null vector. The uploaded RK4 script was inspected, not executed; those example trajectories are not evidence of the global theorem or of the exact exponent.

## originality

PASS

The supported claim is the sharp global vaccinated Holling-II disease-free threshold through equality on the full cone, paired with the exact trajectory logarithmic extinction rate in the stated class. The same model, reproduction number, and strict local threshold are prior; the motivating global theorem has a stricter sufficient condition, and the sharp unvaccinated corollary does not cover positive vaccination. General positive-system tools and analogous critical theorems are antecedents, not new claims of this record.

## value

PASS

The result closes the gap between the local and sufficient global extinction tests for a motivated deterministic model. It proves global stability at the nonhyperbolic boundary and determines exactly what the asymptotic logarithmic decay rate does there. Two exact witnesses show genuine coverage beyond the earlier test, including at equality. The contribution is mathematical disease-free analysis, not field validation, control calibration, or an algebraic prefactor at criticality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
