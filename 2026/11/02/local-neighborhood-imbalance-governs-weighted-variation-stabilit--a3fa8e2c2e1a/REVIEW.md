# Scientific review: local neighborhood imbalance governs graph gossip variation

## Correctness — PASS

For every third vertex, an exact two-point convexity inequality bounds the effect of exchanging endpoint values by the weighted neighbor discrepancy. The omitted edge contributes exactly the stated gap reduction; the locally sharp choices at each third vertex can be made simultaneously. Coarea reduces the quotient norm to characteristic functions of graph cuts. Exhaustive rational cut evaluations, data tests, and independent two-terminal minimum-cut comparisons support the analytic proof. The exceptional graph with only two vertices is expressly outside the main norm statement.

## Originality — PASS, with residual uncertainty

Boyd et al. (2006) define classical pairwise consensus and analyze mixing eigenvalues; their statement does not supply graph-edge variation-norm criteria. Ben-Ameur, Bianchi and Jakubowicz (2012) study a nonlinear distributed TV-regularized optimization algorithm, not the weighted BV norm of ordinary pairwise exchange; their relevant sections were read in full-text PDF. Kováč and Smith (arXiv:0911.1928) establish graph-edge variation as a regression penalty, but only an abstract was accessible, so whole-document noncoverage is not asserted. Available earlier findings address different heat diffusion and conditional averaging operators. Mathematical record searches for neighbor-profile criteria, partial swaps, graph-BV contraction and exact cut norms found no directly covering result. Hidden prior equivalence remains possible, especially because the underlying local inequality is elementary; this risk does not amount to demonstrated coverage.

## Mathematical value — PASS

The sharp phase criterion answers whether each individual averaging communication can increase measured roughness; its conjunction over edges characterizes pathwise variation monotonicity for every gossip sequence. A sharp induced norm with minimum-cut threshold permits quantitative guarantees when the local test fails. Explicit complete multipartite and tree classifications and growing star amplification show structural implications rather than merely restating a general bound.

## Limits and source comparison

The result holds for finite connected simple undirected weighted graphs, at least three vertices, symmetric endpoint exchanges in the unit interval, and real signals. It does not address arbitrary mixers, nonlinear TV flow, or mixing times. Sources inspected: Boyd et al., *Randomized Gossip Algorithms* (2006); Ben-Ameur et al., *Robust Average Consensus using Total Variation Gossip Algorithm* (2012); Kováč and Smith, *Regression on a Graph* (arXiv:0911.1928, abstract only); Boyd et al. (2004, conference paper overview only). Independent mathematical assessment is still required before treating novelty as conclusively established.

Self-review: passed. Independent audit: not yet performed.
