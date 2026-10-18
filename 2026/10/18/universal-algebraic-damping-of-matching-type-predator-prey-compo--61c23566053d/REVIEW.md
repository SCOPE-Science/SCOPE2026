# Scientific review: Matching-type predator–prey algebraic damping

## Correctness

**PASS.** The source's four-population differential equations admit the exact total-abundance and type-composition coordinates stated in the result. The relative-entropy derivative is nonpositive and has no nontrivial invariant zero-dissipation orbit, yielding global convergence. At the positive equilibrium the two total directions are strictly stable while the two type-composition directions form a linear rotation. The quadratic center-manifold invariance equations have a uniquely solvable Hurwitz-matrix expression, and explicit angular averaging gives a strictly positive rational cubic damping coefficient. The same coefficient is independently recovered from averaged squared total-abundance deviations in the exact Lyapunov identity. A corrected energy removes oscillatory order-four terms and proves the asserted universal infinite-time constant. Exponential stable-fiber tracking cannot account for an initially nonzero composition because its logarithmic derivative tends to zero. The attached program verifies the nonstandard algebra and illustrates, but does not prove, the asymptotic limits.

## Originality

**PASS, subject to historical-priority risk.** Costa, Czuppon and Forien (arXiv:2609.04834, September 4, 2026), Section 2.2, Proposition 2.4 and Appendix A.2, introduce these matching-type equations and prove global convergence to positive coexistence. That stronger *qualitative global stability* does not give a quantitative algebraic decay exponent or explicit coefficient. The present finding does not reclaim global convergence. The 2016 PLOS ONE predecessor (PMCID:PMC5042472) studies different asymmetric coevolutionary models; its results do not yield the model-specific asymptotic. Standard center-manifold and averaging theory supplies the method but not the required model-dependent coefficient. Similar damped oscillations in other Lotka–Volterra systems do not imply the stated all-positive-parameter amplitude law. The possibility of an unpublished or differently indexed equivalent calculation remains a residual risk; independent priority assessment is unperformed.

## Mathematical value

**PASS.** The recent model features matching-specialist predator and prey types and long-lived transient composition cycling even while total populations equilibrate. The published global attractor theorem alone cannot distinguish exponential relaxation from arbitrarily slow critical decay. The theorem identifies a natural observed energy, its universal inverse-time asymptotic, the sharp inverse-square-root composition envelope, an explicit dependence on four ecological interaction strengths and the equilibrium abundances, and a principled balanced/unbalanced dichotomy. These quantities clarify the deterministic transient relevant to biological timescales prior to mutation or demographic noise. Nothing is asserted about stochastic fixation, spatial networks, or near-extinction boundary limits.

## Sources and limitations

Closest primary result: Costa, Czuppon and Forien, *Eco-evolutionary cycles in a matching type predator-prey interaction*, arXiv:2609.04834 (2026), particularly Proposition 2.4 and Appendix A.2. Relevant model comparison: *Evolutionary Diversification of Prey and Predator Species Facilitated by Asymmetric Interactions* (2016), PMCID:PMC5042472. Mathematical background: Carr (1981), *Applications of Centre Manifold Theory*, and Sanders, Verhulst and Murdock (2007), *Averaging Methods in Nonlinear Dynamical Systems*. These are not claimed as independently exhaustive priority coverage. Independent scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
