---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Stationary covariance S solves (γI+mL)S+S(γI+mL)=Q, so S(0)=Q/(2γ), S′(0)=−(LQ+QL)/(4γ²). Differentiating Pearson r gives the stated general path expression. In Qδ, q11=2+δ,q33=17+δ,q12=q23=1,q13=5; the slope numerator 2δ²+28δ−27 has exactly one positive root. Laplacian modal decomposition leaves only consensus variance at m→∞, giving r→1; continuity gives finite positive minimizer for δ below threshold. The δ=1/4 closed-form correlation K/sqrt(AC) has strictly positive A,C,K; derivative numerator polynomial has coefficients −,−,+,…,+, hence exactly one positive root by Descartes and endpoint signs, bracketed by exact rationals. Two-patch derivative = (a+b)(ab−c²)/(2γ(ab)^(3/2))>0. Independently verified symbolic derivative, degree-13 polynomial and bracket.

## originality

PASS

Best-of-knowledge independent statement/implication comparison supports a specific quantitative or structural contribution beyond inspected prior results; this is not an exhaustive novelty certificate. OU stationary Lyapunov covariance and Moran effects are established by Wang–Haegeman–Loreau, Kendall, Ripa, Abbott. The claim does not rename a generic synchrony paradox: its exact Q entry slope, SPD two-patch obstruction and Qδ algebraic threshold are additional specifics. Generic Lyapunov theory implies the implicit covariance, but does not by itself assert that strictly positive qij permits negative endpoint initial slope, the sharp δc in this constructed family, or unique global minimum certified by Descartes. Earlier generic nonmonotonicity results also do not imply this special positive-covariance minimality.

## value

PASS

This identifies the smallest equal-damping connected habitat graph where positive pairwise environmental correlations do not guarantee monotone dispersal synchrony, and supplies a sharp noise boundary plus an exactly certified finite optimum. The environmental-driver loadings are explicitly motivated; the small numerical dip is not overstated as a major field effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
