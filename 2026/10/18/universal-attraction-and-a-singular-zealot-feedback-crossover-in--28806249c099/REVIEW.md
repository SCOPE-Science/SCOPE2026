# Scientific review

## Correctness — PASS

The flux ratio at equilibrium reduces exactly to a strictly monotone function of the total opinion fraction. The integral representation proves its derivative has a fixed sign for the full admissible interval, so there is one hyperbolic attractor and no hidden second branch. Uniform convergence of this ratio on compact opinion intervals establishes the reciprocal scaling limit; a separate boundary argument yields the fixed-bias power law. No numerical root search or finite-grid enumeration substitutes for these analytic arguments. A standalone standard-library checker corroborates representative identities and parameter limits.

## Originality — PASS, with residual risks

Huang and Prokopenko (arXiv:2609.18684v1, equilibrium equations (26)–(27), Figure 2) supply the model and a numerically traced equilibrium for one fixed committed fraction; they do not establish the all-parameter uniqueness/global-stability theorem or the singular small-commitment scaling law. Vasconcelos, Levin, and Pinheiro (arXiv:1811.08525) analyze the zealot-free competing-contagion dynamics, which lacks the positive-commitment limiting selection proved here. Mobilia (arXiv:1506.04911) analyzes a distinct symmetric superlinear \(q\)-voter equation whose bistability does not imply a theorem for reciprocal exponents straddling one. Searches of mathematical findings and relevant literature found no equivalent claim. The remaining risk is a generalized monotone-flow or zealot-regularization theorem under different terminology that might subsume the precise singular crossover.

## Value — PASS

The scaling limit isolates a motivated nonuniformity in a recent model for crisis-related opinion adoption: as committed fractions vanish, an arbitrarily small reciprocal feedback asymmetry can still cause a macroscopic change, provided the feedback and commitment vanish at comparable rates. The no-bistability result distinguishes this mechanism from superlinear \(q\)-voter tipping, and the explicit crossover predicts the amplitude and direction of equilibrium opinion shifts. This is a structural and model-specific conclusion rather than an arbitrary parameter evaluation.

## Scientific limitations

The theorem applies to a frozen-feedback, deterministic, well-mixed system with equal committed fractions; no statement is made for time-dependent feedback, finite stochastic populations, heterogeneous networks or the coupled epidemic dynamics. The mathematical verification is analytic with supplementary finite numerical checks. Historical-priority comparison is not independent certification.

Self-review: passed. Independent audit: not yet performed.
