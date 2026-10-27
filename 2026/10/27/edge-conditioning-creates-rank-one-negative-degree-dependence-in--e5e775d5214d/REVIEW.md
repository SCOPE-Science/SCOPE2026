# Review: conditional endpoint-degree dependence in uniform bipartite spanning trees

## Correctness (PASS)

A weighted matrix-tree calculation gives the complete two-vertex degree generating function, and the explicit effective-resistance calculation correctly splits it by the event that the connecting edge is present. Normalizing yields two conditional pgfs, a three-atom coupling, and the rank-one covariance for all finite-degree test functions. The proof treats every integer \(a,b\ge2\), including zero-trial binomials; exact enumeration independently checked 5,133 spanning trees over nine parameter pairs. The finite checks are not substituted for unrestricted proof.

## Originality (PASS on inspected evidence, residual risk)

Dong–Ge (arXiv:2103.05294) count spanning trees containing a given bipartite forest but do not state the edge-conditioned endpoint-degree generating functions. Rapoport (arXiv:2312.14992) derives general joint-degree distributions and neighboring-point edge treatments; this is a genuine broad computational framework and an important potential implication, but the inspected paper does not exhibit the bipartite three-atom coupling or its all-function rank-one dependence. Sanmartín–Schnörr–Hamprecht (arXiv:2409.13472) compute general degree moments and covariance; our isolated covariance is not claimed as a new general method. The novel structural package assessed is the exact two-condition pgf and coupling, the independence/negative-dependence switch, and its persistent balanced-limit correlation. Residual risk: uninspected earlier bipartite Prüfer identities or an unpublished specialization of the broad frameworks could imply the structure.

## Value (PASS)

Endpoint-degree assortativity is a natural network observable. A single edge constraint changes an *unconditionally independent* endpoint-degree pair into a strictly negatively correlated pair for every pair of increasing nonconstant transforms; the exact rank-one kernel quantifies the dependence rather than merely its sign. The nonzero limiting correlation shows this conditional effect persists for growing balanced hosts. These are finite-size structural facts, not just a routine marginal expectation or an arbitrary parameter slice.

## Scientific limitations

The result assumes uniform spanning trees of complete bipartite graphs. Generic graph extensions, historical priority outside inspected sources, and independent mathematical validation remain open.

Self-review: passed. Independent audit: not yet performed.
