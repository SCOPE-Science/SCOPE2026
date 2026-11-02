# Scientific review

## Correctness

**PASS.** Under the explicitly stationary fair binary Markov law, killed transition matrix \(M(q)\) computes the no-run probability exactly. The Cayley--Hamilton recurrence proves the four-day optimizer, and the identity \(f_q(4/5)=-(q-3/5)^2\) proves the unique long-window spectral optimum. A uniform Perron-eigenvector lower bound forces every global finite-window minimizer toward that optimum; a local two-eigenvalue expansion proves eventual global uniqueness and the positive \(4/(15n)\) shift. The standalone checker uses exact rational enumeration and polynomial identities; it does not substitute numerical evidence for the global argument.

## Originality

**PASS under inspected evidence, with meaningful residual historical risk.** The 1964 and 1977 meteorological sources motivate the precipitation Markov model rather than its optimization. Schwager (1982/1983), Wang and Ji (1995), and Oh--Park--Kim (2022) treat substantially more general run probabilities. In particular, the inspected 2022 preprint explicitly contains the relevant two-state spectral roots (Theorem 2.14); these roots and the recurrence are **prior work**, not claimed discoveries. The distinct question proved here is global optimization of paired-wet occurrence over persistence with wet frequency fixed, including finite-window correction. Search and statement comparisons found no explicit optimization of this family. Because Schwager's Cornell report and some earlier runs articles were not materially accessible, prior coverage of an equivalent optimization remains possible. This is not an independent historical-priority certification.

## Value

**PASS.** At unchanged wet-day frequency, serial persistence can make the occurrence of a paired wet spell more likely at an interior value than at either maximal alternation or maximal persistence. The four-day optimum differs from the unique asymptotic optimum, whose exact finite-horizon displacement and exponential avoidance rate quantify the distinction. This is a useful mathematical benchmark for diagnosing finite-window wet-spell risk in Markov weather generators; no unmeasured flooding or climatic consequences are asserted.

## Boundaries

The result is confined to a fair stationary two-state first-order chain and at least one adjacent wet pair. It does not resolve arbitrary marginal wet frequency, wet-spell lengths above two, higher-order memory, rainfall amounts, or real flood probabilities. Existing general run-distribution papers can reproduce the underlying avoidance probability; the assessed new content is the constrained extremal analysis.

Self-review: passed. Independent audit: not yet performed.
