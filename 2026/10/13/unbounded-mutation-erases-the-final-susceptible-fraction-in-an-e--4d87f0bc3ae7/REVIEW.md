# Self-review

## Correctness — PASS

The proof uses a mass-conserving no-flux mutation operator. Its compartment identity forces prevalence to decay via convolution of the integrable infection flux. For the positive-diffusion half-line model, assuming positive terminal susceptibles gives a uniformly supercritical Dirichlet interval at a sufficiently high infectivity. Heat-kernel positivity seeds this interval, its growing sine subsolution contradicts the mass bound, and therefore the terminal susceptible fraction is zero. For a finite trait cap, the integrated contact-force inequality yields a strictly positive unique final-size lower root. The bound is sharp as an infimum by concentrating nonmutating infected initial data near the cap. Finite-time semigroup continuity and the zero-diffusion compact support yield noncommuting limits. A supporting arithmetic checker confirms a sample positive eigenvalue margin and a root bracket. The proof, not finite arithmetic testing, establishes the all-parameter assertions.

## Originality — PASS

The closest direct source is Lamata-Otín et al. (2026), arXiv:2603.18801v1/v2, which gives the trait-evolution PDE but focuses on early-time epidemic acceleration, control peaks, numerical attack rates, and finite prevalence cutoffs. It does not formulate the exact half-line versus finite-cap terminal-size dichotomy. Alfaro–Carles (2014), arXiv:1405.2768, give explicit solutions and acceleration of mass-normalized linear-fitness replicator–mutator equations, without susceptible depletion and recovered mass. Almeida et al. (2020/2021), arXiv:2010.15410, analyze heterogeneous SEIR final size with diffusion but within a differently formulated trait model; full text was not available and this is an unresolved comparison risk. The local source and literature search did not reveal a dominating or equivalent full theorem; search failure is not proof of global novelty.

## Mathematical value — PASS

The exact late-time dynamics of an unbounded rate-trait approximation can be qualitatively different from bounded-probability implementations, and the difference survives arbitrarily small mutation. The positive-diffusion exhaustion theorem, finite-cap sharp susceptible floor, and singular zero-mutation limit supply a motivated structural boundary for interpreting long-horizon epidemic models. The proof explicitly excludes physical overinterpretation and claims no finite-time outbreak size forecast.

## Limitations and literature

The unbounded variable is mathematical transmission-rate fitness, not an infection probability. The asymptotic time can be very large, and stochastic extinction and finite cutoffs are outside scope. The heterogeneous SEIR comparison (Almeida et al.) is based on its abstract/publisher preview rather than complete primary text, and potential stronger coverage remains a residual risk. The supplementary code is a local finite consistency check, not an infinite-time certificate.

Self-review: passed. Independent audit: not yet performed.
