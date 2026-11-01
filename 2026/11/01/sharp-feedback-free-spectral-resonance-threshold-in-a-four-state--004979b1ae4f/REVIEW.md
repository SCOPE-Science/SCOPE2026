# Scientific review: four-state cyclic promoter spectral resonance

## Correctness — PASS

The stationary promoter has Fourier eigenvalues \(0,-2a,-a\pm ia\), yielding the stated explicit covariance and power spectrum. The exact immigration–death transfer formula includes both Poisson shot noise and promoter-rate correlations. Differentiation in \(x=(\omega/a)^2\) produces the displayed sixth-degree polynomial with strictly positive nonconstant coefficients, so it crosses zero on positive \(x\) exactly when its constant coefficient is negative. This proves both necessary and sufficient threshold conditions, including equality. The n=2 and n=3 formulas and reversible-chain positive Lorentzian decomposition prove the scope-specific minimality statement. The standalone checker passed 892 finite checks, including 48 exact rational identities and 600 independent random generator/resolvent comparisons. Such finite comparisons are not used as the infinite-parameter proof.

## Originality — PASS on examined evidence

The 2005 exact reaction-network spectrum theory and 2013 multistate-promoter noise analysis are strong methodological antecedents. In particular, the general mRNA spectral-filtering formula is already established in the 2013 work; it is not claimed as new. That work investigates up to three-state cycling and variance/noise architecture rather than the four-state feedback-free sharp frequency-peak threshold. The 2019 feedback oscillation result assumes a different two-state hybrid mechanism; the 2021 cell-lineage paper supplies general spectral machinery but not the inspected four-state phase boundary. Five targeted published-record searches found closely related biological oscillators and Markov-chain covariance results, not a statement that implies the specific if-and-only-if polynomial criterion. This is a qualified best-knowledge comparison, not a proof that no earlier or equivalent theorem exists.

## Mathematical value — PASS

The exact boundary distinguishes a non-equilibrium cyclic promoter's intrinsic temporal correlation from feedback-driven oscillations, and states a falsifiable peak criterion in terms of three kinetic rates. The result provides a sharp parameter-space classification and demonstrates why three-state models and all reversible promoter dynamics fail to reproduce this spectral signature in the specified measurement process. The issue is not just an elementary rescaling of a known variance calculation: a non-monotone frequency response and its global uniqueness require the explicit numerator sign analysis.

## Closest literature, comparisons, and limits

Warren et al. (2005), https://arxiv.org/html/q-bio/0512041v1: general power-spectrum methods, not a four-state promoter peak criterion. Rieckh and Tkačik (2013), https://arxiv.org/html/1307.8075v2: general mRNA filtering and three-state promoter cycling, not the sharp four-state spectral-shape condition. Jia et al. (2019), https://arxiv.org/html/1909.09769v3: two-state feedback-induced oscillations, not feedback-free directed four-state cycling. Jia and Grima (2021), https://doi.org/10.1103/PhysRevX.11.021032: cell-lineage spectral analysis with broader resolvent methods and a potential general-method subsumption risk. Full historical priority has not been independently established. The model excludes nonuniform cycle rates, burst synthesis, and coupled feedback.

Self-review: passed. Independent audit: not yet performed.
