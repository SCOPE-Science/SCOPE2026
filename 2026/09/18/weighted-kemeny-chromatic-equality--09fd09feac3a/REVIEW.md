# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The statement is derived from the equality condition in the partition bound of Abiad--Carmona--Encinas--Ghorbani--Jiménez--Samperio and then proved by an explicit rigidity argument.

For a proper \(r\)-coloring, equality in the chromatic Kemeny bound forces the degree-weighted quotient eigenvalues to be
\[
1,-\frac1{r-1},\ldots,-\frac1{r-1},
\]
and forces the normalized adjacency spectrum to consist of those eigenvalues together with \(n-r\) zeros. Comparing \(\operatorname{tr}(M^2)\) with the quotient compression shows that the normalized adjacency matrix has no component outside the color-indicator subspace. The zero diagonal of the quotient then forces equal color-class volumes, after which every cross-part edge weight is forced to be
\[
w_{uv}=\frac{d_ud_v}{(r-1)A}.
\]
The converse is checked directly by computing the weighted degrees and normalized adjacency spectrum. The \(r=n\) case is handled separately by the equality case of Cauchy--Schwarz and gives the same formula.

The proof was stress-tested at the principal boundary cases \(r=2\), \(r=n\), singleton parts, unequal part sizes, and nonuniform masses inside a part. In the bipartite case the theorem reduces to a rank-one condition on the positive bipartite weight matrix; in the singleton case it reduces to a uniformly weighted complete graph. A compact numerical verifier independently checks representative constructions.

No empirical computation is used as a substitute for the general proof.

## Originality

Originality is assessed **to the best of our knowledge**.

The directly motivating source is arXiv:2609.17481, submitted 15 September 2026. Its chromatic bound is stated for connected weighted graphs, while the paper explicitly says that the equality classification is stated for the unweighted case. The accessible theorem and proof around Corollary 4.2 were inspected, including the equality condition in the preceding partition theorem.

Searches were made for combinations and synonymous formulations involving:

- Kemeny's constant, weighted graphs, chromatic number, and equality;
- weighted complete bipartite and complete multipartite graphs;
- normalized adjacency / normalized Laplacian spectra of weighted multipartite graphs;
- rank-one bipartite weight matrices;
- degree-corrected multipartite and block-matrix factorizations.

The earlier Ciardo--Dahl--Kirkland result is unweighted and bipartite. Sun--Das concerns normalized-Laplacian spectra of unweighted complete multipartite graphs. Fasino--Tudisco studies algebraically related degree-corrected block matrices, but not this Kemeny/chromatic equality problem.

No equivalent or stronger published classification was found in the inspected sources or searches. No inaccessible source was identified whose available bibliographic description strongly suggested direct coverage. The principal residual risk is that a result in weighted spectral graph theory or reversible Markov chains may encode the same factorization under substantially different terminology, or that very recent parallel work may exist because the motivating preprint is itself new.

## Value

The source bound is genuinely weighted, but its stated equality classification stops at the unweighted setting. The present theorem closes that gap exactly and shows that the weighted case is structurally richer: cardinalities of the color classes can be arbitrary, while equality is governed by equal stationary mass and a degree-factorization law.

The result also gives:

- a probabilistic description of every equality walk;
- the rank-one characterization for weighted complete bipartite graphs;
- equality weightings on every complete multipartite underlying graph;
- the dimension \(n-r+1\) of the equality cone, or \(n-r\) modulo global scaling;
- the published unweighted equality theorem as a specialization.

These are structural consequences rather than isolated numerical examples.

## Limitations

The theorem assumes finite connected undirected graphs with strictly positive weights on present edges, matching the weighted-graph setting of the source bound. It does not address directed chains, signed weights, loops, or alternative Kemeny conventions. The numerical artifact checks examples only and is supporting evidence. Originality remains to the best of our knowledge, and independent audit has not been performed.
