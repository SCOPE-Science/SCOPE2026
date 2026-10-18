# Self-review

## Correctness — PASS

The claim fixes all five positive model parameters and specifies an independent finite-mean Lomax renewal clock. The zero-started chain's generating function satisfies its exact Kolmogorov equation and admits a Gamma–Poisson representation. The stationary renewal age has the exact survival \((1+t/b)^{-\alpha}\), which is the correct length-biased sampling law rather than the reset-interval survival. In the subcritical regime an explicit negative-binomial mass ratio is bounded in three age windows, yielding the logarithmic penalty with its constant. At criticality a Gamma product-tail calculation gives the exact Pareto coefficient, and in the supercritical regime exponential growth converts the age tail into a logarithmic occupation tail. Conditional Poisson concentration preserves both survival-tail equivalents. The moment conclusions follow by comparison/integration; they are not inferred from finite simulations.

The executable `verify.py` checks the generating-function equation and three numerical asymptotic predictions against independent quadratures. Numerical evidence is supplementary, not a substitute for the stated proof.

## Originality — PASS, with residual priority risks

The focal source is Grange, arXiv:2311.12414, especially its single-site master equation, Poisson local-reset term, generating-function solution, and discussion. That paper calculates local-reset stationary means and fitness condensation in a coupled zero-range model; it does not analyze iid Lomax renewal times or prove the three asymptotic equivalents for a fixed immigration intensity. Grange, arXiv:1910.05991, studies global memoryless resets. Masó-Puigdellosas, Campos, and Méndez, arXiv:2205.01613, supply general renewal-age propagator identities, so renewal mixing alone is not claimed as new. Foss, Korshunov, and Palmowski, arXiv:2007.13507, find related logarithmic tails for a branching process in a heavy-tailed random offspring environment, which is structurally distinct from complete demographic restarts. No inspected theorem implies all three exact claims for the specified model. Prior work on non-Poisson catastrophic birth–death–immigration processes could provide an equivalent or stronger special case; independent priority examination remains necessary.

## Scientific value — PASS

Heavy-tailed catastrophes change the qualitative stationary population statistics at the natural branching threshold \(\lambda=\mu\). The subcritical answer contains a non-obvious logarithmic multiplicative correction to the ordinary negative-binomial mass, while the critical and supercritical regimes have explicit, incompatible tail scales and sharp moment cutoffs. The fact that a proper stationary law exists above criticality despite all moments diverging is relevant to the design and interpretation of population and local-occupation reset models. The theorem does not claim a full interacting-system condensation theory, and the value assessment rests on the exact three-regime phase diagram rather than on numerical correctness alone.

## Limitations and literature comparison

The theorem holds only for one autonomous fixed-immigration process, not the coupled mean-field lattice. It assumes strictly positive rates and exactly Lomax-distributed renewal durations. The model's source paper treats Poisson local resetting, whereas the renewal-age paper's explicit diffusive propagators do not characterize branching occupations. A related heavy-tailed random-environment branching result shows that the logarithmic motif is not by itself new. These boundaries and a remaining older catastrophe-literature coverage risk require independent assessment.

Self-review: passed. Independent audit: not yet performed.
