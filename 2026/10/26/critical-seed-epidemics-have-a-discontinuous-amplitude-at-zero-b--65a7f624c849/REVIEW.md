# Self-review of the critical-seed turnover finding

## Correctness — PASS

The statement is restricted to the normalized six-compartment MB ODE at \(\kappa=\rho\beta_1+(1-\rho)\beta_2\), with initial behavior composition at switching equilibrium. Direct summation gives the exact \((S,I,R,d)\) subsystem; positivity and conservation ensure global boundedness. The signed imbalance \(d\leq0\) makes \(I\leq\varepsilon e^{-\kappa\varepsilon t}\), yielding the finite final size and exact recovered-coordinate balance. At positive turnover, \(|d|\leq C\varepsilon/a\) makes the correction terms lower order; at zero turnover, the unique final-size root has curvature \(M_2\). The separate uniform-tail argument proves continuity at each nonzero seed and validates the noncommuting iterated limits. The exact example \(M_2=76/49\) was checked against direct integration. Numeric results are not relied upon for the theorem.

## Originality — PASS with documented residual risk

The full Allen–Heller–Pons article (arXiv:2207.08999, Sections 2–5 and appendix context) proves reproduction-number/sensitivity statements but does not give a final-size critical-seed theorem. Magal–Seydi–Webb (2018, equations (3.2)–(3.4)) treat group-conserving SIR dynamics without switching membership. El Attouga–El Khalifi (2024, Section 2.3) treat fixed heterogeneous susceptibility and imply the zero-turnover final-size equation but not the positive-turnover coefficient nor the interchange failure. Perra et al. (2011, behavior-transition sections) treat disease-induced fear spread, a different switching law. Searches for the precise two-parameter singular limit, model name, aliases, and published research records did not expose a dominating statement. A more general unindexed epidemic singular-perturbation result remains possible; no human or independent literature audit has occurred.

## Mathematical value — PASS

The result locates a real singular modeling boundary: replacing a very slow but positive behavior turnover by zero is harmless at a fixed nonzero seed yet changes the leading critical-outbreak size at vanishing seed. The coefficient jump is exact, parameter-transparent, and not a routine calibration of \(\mathcal R_0\), which remains one in both regimes. It separates timescale equilibration from permanently frozen susceptibility composition, a structural issue for critical outbreak projections.

## Scope and risks

The theorem is deterministic; no finite simulation proves the limits. The exact zero-turnover model is a boundary extension, and no uniform crossover at \(a\asymp\sqrt\varepsilon\) is claimed. Stochastic outbreaks, broader time-dependent behavior changes, and independent review remain unaddressed.

Self-review: passed. Independent audit: not yet performed.
