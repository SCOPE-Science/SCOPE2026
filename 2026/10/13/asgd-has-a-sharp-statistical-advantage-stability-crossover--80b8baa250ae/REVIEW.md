# Review

## Correctness

PASS. The practical ASGD source equations reduce exactly to a two-state scalar matrix. Its trace and determinant give three second-order Jury inequalities; two are automatically positive on the stated source domain, while the third gives the exact stability ceiling. Direct algebra proves the SGD crossover and the sharp global lower envelope.

Risk: this is deterministic modal stability rather than stochastic mean-square stability.

## Originality

PASS. The 2017 ASGD paper gives stochastic least-squares acceleration and the 2018 paper gives the practical short-step/long-step form and its deterministic Nesterov equivalence. The deterministic endpoint is treated as prior context. The inspected sources and focused published-record searches do not state the full statistical-advantage-dependent Schur frontier, the \(\xi=10/7\) crossover, or the \(400/249\) lower envelope.

Residual risk: an equivalent two-state calculation may exist in control literature without ASGD terminology.

## Value

PASS. The result directly characterizes the three central practical ASGD tuning quantities. It separates stability of the coupled mechanism from stability of its constituent short and long steps and gives a sharp criterion for when the statistical-advantage setting enlarges or narrows the ordinary SGD large-step margin.

Self-review: passed. Independent audit: not yet performed.
