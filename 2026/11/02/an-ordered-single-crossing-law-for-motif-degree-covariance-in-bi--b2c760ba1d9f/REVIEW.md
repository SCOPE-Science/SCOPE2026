# Scientific review — motif–degree covariance

## Correctness: PASS

The proposition fixes finite simple non-induced motifs with no isolated vertices, \(n\ge h\ge2\), \(n\ge3\), and \(0<p<1\). Given a prescribed copy, exactly its \(d_v\) forced incident edges change a marked motif vertex's degree law from \(\operatorname{Binomial}(n-1,p)\) to \(d_v+\operatorname{Binomial}(n-1-d_v,p)\); other vertices retain the unconditioned distribution. This gives the stated normalized covariance by exact binomial identities and linearity. Strictly decreasing positive Laurent terms establish unique roots and, using the strict increase of falling factorials with \(k\), their order. Endpoint classes are checked separately. The expansion of \((n-1)_{\underline d}\) and a nonvanishing derivative give the second-order root term for fixed \(H,k\). The finite verifier passed 3,299 exact-rational or threshold-order tests; exhaustive checks stop at six ambient vertices and are not infinite proofs.

## Originality: PASS (qualified)

Goldstein–Rinott (arXiv:math/0510586, full preprint inspected, especially the graph example) state covariances *between two degree-frequency counts*; their explicit degree–degree formula cannot be substituted to obtain the covariance with an arbitrary non-induced motif count. Döring–Eichelsbacher (arXiv:0901.3246v1, original full text inspected) treat subgraph-count moderate deviations, not the motif–degree cross-statistic. Goldstein (arXiv:1005.4390, full preprint inspected) treats the distribution of an individual degree-count statistic. Queried published research records for aliases, exact formulas and stronger implications, and accessible previous claims: the nearby triangle–component covariance, parity–motif covariance and isolated-vertex cases do not cover the family of positive-degree frequency sign thresholds, nor the degree-multiset collapse. The 1991 generalized-U-statistic article and 2010 subgraph variance article were not inspected in complete full text; unknown stronger formulae remain a genuine historical-priority risk. The established \(k=0\) special case is expressly not presented as new.

## Mathematical value: PASS

Degree frequencies and motif counts are both canonical observables in \(G(n,p)\), but their dependence is not determined by marginal variance and concentration theory. A single formula controls the full mixed matrix, collapses normalized dependence from motif topology to degree multiset, and yields exactly one monotone threshold for each admissible degree class. The strict ordering between thresholds, regular-motif exact roots and second-order sparse-window correction reveal a natural dependence phase structure, rather than an arbitrary finite computation.

## Limitations and relevant sources

Historical priority is not certified; general generalized-U-statistic covariance expansions and older overlap tables may subsume parts of the proof. The finite checker does not validate the asymptotic proof independently. The theorem applies to non-induced copies only and its expansion keeps \(H,k\) fixed. Primary sources: Goldstein–Rinott, arXiv:math/0510586; Döring–Eichelsbacher, arXiv:0901.3246; Goldstein, arXiv:1005.4390; Janson–Nowicki, DOI:10.1007/BF01193750 (incomplete inspection); Ellis–Ferry, DOI:10.1016/j.dam.2009.11.012 (incomplete inspection).

Self-review: passed. Independent audit: not yet performed.
