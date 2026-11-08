# Review of the reversible-wave period census

## Correctness

**PASS.** The result treats a precisely defined labelled cone over the Boolean cube, all dimensions \(d\ge3\), and every finite field of characteristic two. It proves the cubical square-zero rank lemma by an invertible substitution in the truncated group algebra. It then derives the apex adjacency's exact kernel and nilpotent/idempotent identities, the associated wave fixed-space dimensions, and the exact primitive-period counts by divisibility subtraction. The exceptional smaller dimension is explicitly outside the claim. Exact matrix-rank tests and independent direct state enumeration were executed successfully from the supplied standalone scripts; these tests support the general algebraic argument but do not replace it.

## Originality

**PASS, with residual priority risk.** Macfarlane (2004) treats reversible linear automata on one-dimensional arrays, primarily state-weight sequences, while Steeb and Hardy (2007) give the general reversible second-order wave construction and one-dimensional examples. Vlasov (2014) studies evolving support sizes for two-dimensional reversible automata, not the apex-cube periodic-state census. Comparisons with first-order parity dynamics of Hamming graphs, finite-field waves on products of cliques, and wheel-graph waves show different underlying operators or graphs. The cone-over-four-cycle boundary is excluded because that instance is also a wheel. Targeted database and literature queries did not identify the same all-dimensional formula or a stronger theorem implying it. No search proves absolute novelty; unindexed equivalent work remains possible.

## Mathematical value

**PASS.** The complete primitive-period distribution on a natural infinite graph family is a dynamical invariant, not a single chosen-state computation. The proof explains a structural sensitivity to a minimal graph operation: appending just one universal vertex adds a nonzero rank-one square to the adjacency operator for even dimension, introducing period eight, while leaving the odd-dimensional maximal period six unchanged. The full finite-field formulas quantify the sizes of all temporal orbit classes. This provides an exact, reusable benchmark for reversible graph-wave models and distinguishes periodic-state census from the previously studied propagation of individual seed patterns.

## Closest literature and limitations

The closest inspected studies are A. J. Macfarlane (2004), DOI 10.1088/0305-4470/37/45/006; W.-H. Steeb and Y. Hardy (2007), DOI 10.1515/zna-2007-10-1103; and A. Yu. Vlasov (2014), arXiv:1407.6553. The setting is finite, characteristic two, and restricted to open-neighbor linear waves. Absolute priority and independent verification remain outstanding. The published 2004 manuscript's text was inspected in its introduction, principal results and concluding remarks; page images were not available from the accessible host.

Self-review: passed. Independent audit: not yet performed.
