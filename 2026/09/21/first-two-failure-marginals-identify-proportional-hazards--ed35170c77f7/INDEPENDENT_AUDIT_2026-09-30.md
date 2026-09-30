# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/first-two-failure-marginals-identify-proportional-hazards--ed35170c77f7`  
Assigned and audited source tree: `10d06d5ff6faffeb223af9c6313e349cba206d75`  
Repository/branch: `SCOPE-Science/SCOPE2026` / `main`  
Current RESULT.md blob: `c475e2aa7bce8828f6e97291e5287f627e0f1bb0`  
Disposition: **passed**

## Correctness

**independently_supported**. The identification argument is correct. Independence gives S1=B^Λ and S2=ΣB^{Λ-λ_i}-(n-1)B^Λ. Eliminating B through u=S1 produces a finite exponential sum with positive exponents 1-q_i strictly below 1 and the unique exponent-1 coefficient -(n-1), so uniqueness of finite exponential representations recovers n and the normalized hazard multiset. The converse characterization has the correct first-moment constraint Σα_i=n-1. When n is known, derivatives at zero give power sums and Newton identities recover repeated hazards. Each marginal alone is nonidentifying: S1 can always be absorbed into the baseline, while Φ_q is a strictly increasing [0,1] bijection for every positive normalized hazard vector, allowing any admissible S2 to be represented after changing the baseline.

## Originality

**qualified_supported**. The heterogeneous order-statistic and proportional-hazards literature contains extensive stochastic-order, dependence and parametric inference results, but the checked sources did not state the baseline-free transform S2(S1^{-1}(u)) as an exact device for recovering an unknown component count and all relative hazards from two unlabeled marginal laws, nor the sharp complete nonidentifiability of either marginal alone under an unrestricted common baseline. Older reliability inverse-problem literature remains a material attribution risk, so originality is asserted only for this exact two-marginal semiparametric identification package.

## Scientific value

**meaningful_identifiability_boundary**. The result isolates a sharp information boundary: two separately observable system-failure marginals identify the whole relative hazard spectrum and component count despite an unknown baseline, whereas either marginal by itself carries no heterogeneity identification. The model-class diagnostic and finite-jet inversion are useful structural consequences.

## Independent checks

- Re-derived S1 and S2 from the probabilities of zero or one failed component.
- Verified uniqueness of the finite exponential representation after x=-log u.
- Checked the exponent-1 separation uses n≥2 and strictly positive multipliers.
- Reconstructed the finite-derivative Newton inversion.
- Verified Φ_q'(z)>0 and the second-marginal-only baseline reparameterization.

## Literature and evidence checked

- https://doi.org/10.5402/2012/839473
- https://doi.org/10.1016/j.jmva.2008.09.010
- https://doi.org/10.1017/S0269964822000146
- https://doi.org/10.1016/j.ress.2005.12.010
- https://doi.org/10.1016/j.spl.2009.11.025
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/first-two-failure-marginals-identify-proportional-hazards--ed35170c77f7
## Limitations

- Independent continuous proportional-hazards components with one common baseline and strictly positive multipliers only.
- The result is population-level; nearly colliding exponents can make inversion ill-conditioned.
- Labels and absolute hazard scale remain unidentified.
- Censoring, dependence, ties, zero multipliers and baseline misspecification are outside scope.
- Older reliability inverse-problem literature remains the principal originality risk.
