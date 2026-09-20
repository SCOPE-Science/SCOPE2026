# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The finite bound is obtained by an exact Hamming-slice decomposition. The zero slice differs from the signed total-intensity discrepancy by at most the two-success Bonferroni remainder; the singleton slice differs from the coordinatewise L1 discrepancy by at most a factorial-moment remainder; all higher slices are bounded by the probability of at least two successes. These three estimates give the displayed constant in the additive bound.

For the proxy expansion, the one-disagreement events contribute exactly \(|p_i-q_i|\) times the probability that all other disagreement indicators vanish. The event of two or more disagreements has probability at most the second factorial moment. The elementary identity \(\lambda_i-|p_i-q_i|\ge0\) verifies \(a_i\in[0,1]\) and closes both bounds.

The sign-pattern construction was checked algebraically: swapping \((\varepsilon\alpha,\varepsilon\beta)\) to \((\varepsilon\beta,\varepsilon\alpha)\) leaves both \(\lambda_i\) and \(a_i\) exactly unchanged, while it reverses the signed intensity contribution. Aligned and balanced patterns therefore have the same proxy data but first-order TV ratio two. The \(\sqrt2\) multiplicative and \(1/3\) relative-error impossibility constants follow directly from the overlap condition for a single estimator value applied to those two indistinguishable inputs.

Adversarial boundary checks include \(n=1\), \(\mathbf p=\mathbf q\), coordinates with \(\lambda_i=0\), and arbitrary non-small aggregate intensity. The inequalities remain valid in these cases, though the rare-event interpretation can become vacuous outside the small-intensity regime.

## Originality

**PASS, to the best of our knowledge.** Smirnov (arXiv:2609.19222) introduces the sign-blind quantities \(\lambda_i,a_i\), the random proxy variable \(G\), and the universal comparison, including the exact upper inequality used here. The paper does not state the signed first-order rare-event correction or the factor-two indistinguishability construction.

Avital--Kontorovich--Salafatinos (arXiv:2602.21828) analyze tiny and small Bernoulli parameters. Their main results give multiplicative comparability to the L1 parameter difference in the tiny regime and to the singleton slice in the small regime. The reviewed statements do not give the additive expansion
\[
\frac12\left(\sum_i|p_i-q_i|+\left|\sum_i(p_i-q_i)\right|\right)
\]
with a quadratic remainder, nor the obstruction for Smirnov's newer proxy.

Kontorovich (ECP 2025, DOI 10.1214/25-ECP680) already proves a conceptually related information-loss phenomenon: the vector of marginal TV distances cannot determine product TV to arbitrarily good universal factors. The present originality claim is therefore deliberately narrower. It concerns the stronger sign-blind data \((\lambda_i,a_i)_i\), exact equality of the induced proxy law, the explicit sparse Bernoulli factor-two pair, and the resulting \(\sqrt2\) / \(1/3\) estimator barriers.

Targeted searches using the exact first-order expression, signed-intensity terminology, rare Bernoulli-product TV, and the \((\lambda_i,a_i)\) representation did not locate a prior statement of these claims. Older rare-event, Poisson-binomial, and signed-measure asymptotic literature was not exhaustively inspected and is the main residual risk of equivalent prior coverage. The originality judgment is therefore not a claim of exhaustive literature coverage.

## Value

**PASS.** The result explains precisely what information is discarded by a newly proposed efficiently computable Bernoulli-product TV proxy in the rare-event regime. It gives a finite-sample additive theorem rather than only an asymptotic heuristic, produces a sharp factor-two separation at fixed proxy data, and converts that separation into explicit lower bounds for any estimator restricted to the same representation. It also refines the existing small-parameter picture by distinguishing unsigned coordinatewise discrepancy from net signed mass balance.

## Scientific limitations

The result does not determine the optimal universal two-sided constant in Smirnov's comparison, does not prove that \(d_{\rm TV}\ge\mathcal T/2\) holds in general, and does not constrain algorithms that use the full vectors \(\mathbf p,\mathbf q\). Higher-order rare-event corrections and a classification of what additional low-dimensional statistics suffice for sharper approximation remain open.
