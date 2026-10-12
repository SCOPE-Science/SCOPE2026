# Review: exact mean-square stability of geometric-momentum Kaczmarz

**Correctness — PASS.** The update and row-norm selection are reconstructed from Alderman–Luikart–Marshall's equations (9)–(10), not approximated. Two Bernoulli branch matrices yield an exact three-dimensional covariance recurrence. The determinant identity and endpoint are algebraic; the positive-semidefinite eigenmatrix argument gives necessity and rules out spurious first-moment stability. The provided standard-library verifier performs 64 rational determinant checks and 320 exhaustive finite-horizon recurrence checks. Finite checks alone do not establish the infinite-horizon result.

**Originality — PASS, with residual priority risk.** The closest defining article proves a two-dimensional signed *first*-moment recursion and explicitly poses mean-norm convergence and critical-momentum behavior as open directions (Sections 2.7 and 4.2). That recursion does not contain the three-dimensional covariance operator; indeed the supplied two-row rational example disproves any implication of its signed stability to mean-square stability. The separately inspected minibatch-heavy-ball source has a different state update and batch rule. Targeted literature searches and a mathematical research index yielded no stronger direct formula, but an unindexed specialized proof remains possible.

**Value — PASS.** The theorem exactly answers an explicit published algorithmic question on the natural diagonal baseline, for arbitrary row probabilities and all allowed smoothing and mass parameters. It identifies a nontrivial phase transition separating signed-mean decay from exponential mean-square blowup, with an exact smoothing safeguard and rational example. The result is neither a mere rescaling nor an unmotivated parameter slice.

**Limitations.** No claim about general nonorthogonal matrices, adaptive parameters, noisy systems, almost-sure convergence, or independent certification is made. The primary publication's analysis does not supply a complete literature census.

Self-review: passed. Independent audit: not yet performed.
