# Scientific review

## Correctness — PASS

The proof derives the exact right directional derivative of edge-weighted variation for every binary cut under the degree-normalized Markov generator on \(K_{2,q}\). It treats every class of cuts up to complement: right-only cuts reduce to column singleton inequalities, while one-left-vertex cuts reduce, for fixed right-set cardinality, to largest-score subset sums. The exact Euler identity for binary cuts and the coarea/triangle-inequality argument prove all-time contraction for arbitrary real data. A positive cut derivative gives strict small-time amplification. Exact-rational tests using `verify.py` arithmetically cross-check all 25,728 sampled binary cuts and the five-vertex witness. Proof does not rely on finite enumeration.

## Originality — PASS, with limitations

Full-text examination of arXiv:1307.0045 (graph coarea, graph MBO and curvature) and arXiv:1306.2561 (heat-gradient curvature estimates), together with the abstract and publication metadata of DOI:10.1137/120895068 (proximal graph-TV optimization), did not identify the stated anisotropic heat-semigroup criterion, its sorting reduction, or the first mixed-cut obstruction. Related prior classifications for trees, cycles, and unweighted complete multipartite graphs concern different graph classes or different heat and weight models and do not imply the result for arbitrary positive variation weights on \(K_{2,q}\), \(q\ge3\). The possibility of an equivalent result in historical work on polyhedral dissipativity or matrix logarithmic norms remains a residual risk.

## Mathematical value — PASS

The two-left-vertex complete bipartite graph is a minimal natural family connecting the three-vertex path, the four-cycle, and genuinely multicycle graphs. The full criterion is constructive and takes \(O(q^2\log q)\) rather than the exponential enumeration of all cuts. The explicit \(K_{2,3}\) example demonstrates that the local vertex tests, sufficient on the smaller family members, cease to decide semigroup contraction at five vertices. This is a structural boundary and an efficient all-weights classification, not a mere special numerical instance.

## Limits

Only strictly positive variation weights, unweighted degree-normalized heat transitions, and real signals are treated. The statement does not classify weighted jump rates, higher-dimensional complete bipartite graphs, or finite-time amplification maxima. Independent verification has not been performed.

Self-review: passed. Independent audit: not yet performed.
