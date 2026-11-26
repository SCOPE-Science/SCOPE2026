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

Independently reconstructed RESULT.md:18–54. In the homogeneous model, positive A forces S=u/B and I=αA/v. After eliminating R with the population constraint, the S equation yields the displayed positive A exactly when R₀>1; the R balance gives positive R. This proves uniqueness only within the homogeneous endemic class. The disease-free susceptible fraction is (μ+γ)/d; the infected next-generation factor for the constant mode is S_DFE B/u and the row-stochastic contact matrix has spectral radius one, consistent with the stated R₀. Linearizing in S,A,I gives the stated mode block J(q) with g+h=u. For X=z+v and P=(z+u−gq)X−hvq, direct determinant expansion and cancellation give det(zI−J)=(z+d)P+λ[(z+u+γ)X+γα]. Writing t=1−q, P=z²+(h+v+gt)z+vut; this recovers all three coefficients. They are positive for t≥0 including the homogeneous mode t=0 and the bipartite extremal mode t=2. At t=0, c₂>λ(u+γ) and c₁(u+γ)−[vu+γ(α+v)]=(d+λ+h)(u+γ)−γα>0 by d≥γ and u>α. The derivative of c₁c₂−c₃ is the sum of dg c₁(0), g c₂(0), vu(c₁(0)−d) and 2g(dg+vu)t, hence positive. The cubic Hurwitz test is strict in every mode, with no vaccination-versus-recovery restriction. Symmetry gives a complete eigenbasis. If community totals N_i are included as coordinates, their autonomous equations have eigenvalue −μ and make the enlarged Jacobian block triangular, so there are no missing population modes. Hyperbolicity gives local exponential stability for the smooth finite-dimensional model. The supplied VERIFY.py was inspected, not executed: the symbolic check starts from the reduced cubic and the three numerical examples use a single 3-community topology. These checks are ancillary to the exact universal calculation.

## originality

PASS

The distinct contribution is strict local stability in every spatial mode under the shared symmetric regular contact matrix, with common community rates but potentially unequal stage rates, including positive waning and vaccination above both recoveries. The homogeneous mode is prior, and the no-waning multigroup stability case is substantially covered under the prior paper's contact assumptions. The retrieved antecedents do not imply the whole unrestricted-within-family assertion.

## value

PASS

Separates an exact structural network-stability question from earlier sufficient rate inequalities. An endemic equilibrium stable on the synchronized subspace need not in general be stable to network-heterogeneous modes. Showing strict damping in every allowable mode even with waning and unrestricted vaccination closes that gap for a natural regular homogeneous network class. The result is local and provides no claim about global attraction, intervention choice, or arbitrary heterogeneous or directed networks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
