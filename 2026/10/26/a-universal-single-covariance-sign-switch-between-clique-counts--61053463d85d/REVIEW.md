# Review of clique–induced-motif covariance sign classification

## Correctness

The exact identity follows by conditioning an induced-pattern indicator on each vertex subset and partitioning clique tests by overlap size. The treatment of intersections of size zero or one is valid because no complete-graph edge is then constrained. Normalizing by a positive expectation is legitimate for \(0<p<1\). Strict decrease of the normalized expression follows from the nonzero edge count, and its endpoint limits prove a unique sign switch. The asymptotic correction is obtained from a controlled fixed-parameter expansion, not numerical extrapolation. A standard-library checker gives 168 exact-rational finite comparisons. Boundary cases (empty graph and complete graph) have separately checked strict signs. Correctness is supported within the stated restrictions.

## Originality

Sah–Sawhney's general graph-factor theory (arXiv:2006.11369) supplies a Fourier viewpoint on induced motif counts, and Goldschmidt–Griffiths–Scott (arXiv:1902.06830) use graph-overlap methods for subgraph deviations. Bhattacharya–Das–Mukherjee (arXiv:2011.03026) concerns vertex-sampling inference. Their inspected statements and relevant sections do not explicitly prove a single covariance sign switch across *all* induced motifs and all clique orders, nor its triangle-excess location law. General Fourier expansions could facilitate other derivations; this is a residual priority risk. The overlap method itself is not presented as new. The all-parameter sign classification is the assessed contribution.

## Value

This resolves a natural covariance-calibration question for every induced network motif against every clique size in a finite binomial random graph, not merely one selected motif. It replaces potentially complicated graph-shape dependence by a strict one-switch law and identifies the first finite-size effect of triangle excess. Explicit five-vertex examples show opposite associations at equal edge density, a phenomenon relevant to interpreting jointly reported motif counts. The conclusion does not assert a downstream estimator improvement or a joint distribution theorem.

## Residual limitations

Full historical priority is not certified; the general graph-factor framework presents the most important overlap risk. Independent scientific validation remains outstanding. The proof applies only within its explicit finite-graph sampling model and size conditions.

Self-review: passed. Independent audit: not yet performed.
