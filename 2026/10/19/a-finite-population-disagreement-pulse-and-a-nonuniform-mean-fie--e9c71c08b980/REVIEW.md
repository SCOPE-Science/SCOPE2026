# Scientific review

## Correctness — PASS

The proof starts with the original finite-agent ordered-pair jump generator, computes exact conditional drifts of the squared empirical mean and empirical second moment, and closes the resulting two-by-two ODE for every integer \(N\ge2\). Positivity of the determinant, negative trace and strictly positive off-diagonal entries produce two distinct negative eigenvalues. The unique disagreement maximum follows from a one-root exponential derivative equation; the explicit asymptotics follow from determinant and trace expansions. For fixed finite population, a bounded-martingale endpoint argument proves almost-sure consensus, independent of the finite enumerations. The attached standard-library program tests the moment identities exactly and checks peak/crossover formula numerically. It does not replace the all-parameter proof.

## Originality — PASS (with residual risk)

The closest published work is Cao and Cortez, *Fractal opinions among interacting agents*, arXiv:2408.01624v1 / SIAM JADS 2025. Its known contribution is mean-field relaxation to a nontrivial Bernoulli-convolution equilibrium. Finite-horizon chaos does not cover the newly stated finite-population moment spectrum or the logarithmic-to-population-time crossover. Lanchier and Mercer, arXiv:2402.02579v1, address qualitative endpoint consensus in related, mainly asymmetric kindness dynamics; their conclusions do not supply the exact moments here. Cao and Cortez, arXiv:2601.21023v2, treat a distinct sign-response variant and cannot imply uniform-in-time approximation for the original process. A fuller general-theorem implication or journal expansion might nevertheless establish equivalent statements; originality is a best-knowledge literature conclusion, not an independent priority certification.

## Value — PASS

The pulse gives a directly measurable finite-population transition from temporary opinion fragmentation to unanimous extreme consensus. Its unique peak at \(\frac{2}{\mu(2-\mu)}\log N+O(1)\), asymptotic plateau height \(\mu/(2-\mu)\), and sharp population-scale decay separate three regimes invisible in the infinite-population stationary description. The explicit one-marginal Wasserstein obstruction addresses a stated motivation in the source article.

## Scientific limitations

The theorem is for symmetric responses, all-zero initial opinions, complete-graph mixing, and the explicitly chosen total update rate \(N/2\). It proves expected empirical variance and one-marginal nonuniformity, not a distributional central limit theorem for the fluctuating histogram. Independent mathematical review and full publication-priority checking remain outstanding.

Self-review: passed. Independent audit: not yet performed.
