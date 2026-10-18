# Scientific assessment: normalization-dependent sharp heat smoothing

## Correctness
**PASS (self-review).** On a complete bipartite graph the two aggregate part masses form a two-state Markov chain, while fluctuations within each part decay at its common exit rate. The exact adjacent-row difference follows by decomposing these invariant subspaces. Its signs are fixed for every positive time, so the total-variation formula gives the true supremum over bounded real or complex inputs, with an explicit attaining sign input. The strict unnormalized comparison follows from an integral representation with positive second derivative; the normalized comparison follows from the strict ordering of reciprocal part sizes. The intermediate-exponent statements follow from independently proved small- and large-time asymptotics. An analytic implicit-function argument supplies the positive short-time crossing and its first-order expansion. No numerical extrapolation is used to establish an infinite-family statement.

## Originality
**PASS within examined evidence (self-review).** Bauer et al. (arXiv:1306.2561, §§2, 4, 7) and Münch (arXiv:1412.3340, §§2, 4) give general graph heat-gradient and curvature estimates; they do not state the exact sharp edge-gradient constants and strict complete-bipartite ordering. Kubo–Namba (arXiv:2103.08149, Theorem 1.2) studies the time monotonicity of a heat-kernel *ratio* for regular bipartite graphs with four eigenvalues, not the bounded-input to graph-Lipschitz norm or its dependence on part imbalance. Public mathematical-record comparisons on complete bipartite structures and graph heat operators did not identify a stronger statement implying the combined trichotomy or the small-exponent crossing law. The spectral reduction and endpoint total-variation duality themselves are standard and are not claimed as novel.

A residual priority risk is that an earlier source could encode these conclusions using Dobrushin coefficients, neighboring-row total variation, or coupling distances without graph-gradient terminology. This search cannot establish absolute novelty.

## Value
**PASS (self-review).** The two conventional graph heat generators produce precisely reversed worst-case partition geometries, *at every positive time*, although they act on the same family of graphs and the same sharp endpoint norm. The intermediate degree exponents cannot preserve either fixed partition ordering and force a genuine time-dependent change. The explicit first-crossing scale quantifies the singular transition away from the combinatorial generator. This is a structural boundary and stability result for network diffusion rather than an isolated matrix entry or parameter substitution.

## Scientific limitations
The theorem is restricted to unit-edge complete bipartite graphs and the unweighted bounded-input/edge-Lipschitz endpoint norm. It proves existence but not global uniqueness of the intermediate time crossings. A separate historical-priority check remains useful, especially for total-variation or Markov-coupling formulations. All computational checks are finite.

Self-review: passed. Independent audit: not yet performed.
