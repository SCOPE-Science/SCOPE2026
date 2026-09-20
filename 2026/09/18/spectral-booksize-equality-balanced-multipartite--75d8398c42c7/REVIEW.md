# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof follows all equality constraints in the elementary chain behind
\[
\operatorname{bk}(G)\ge2\lambda(G)-n.
\]
For a spectral-radius component, equality in the edge degree-product bound forces regular or semiregular bipartite structure. The additional edge degree-sum equality rules out unequal semiregularity, hence the component is regular. Equality then forces every edge to satisfy both
\[
|N(u)\cup N(v)|=n
\quad\text{and}\quad
|N(u)\cap N(v)|=\operatorname{bk}(G),
\]
which makes the spectral component spanning and every edge dominating. The complement therefore has no induced \(P_3\), so it is a disjoint union of cliques. Regularity makes those clique components equal in size, giving a balanced complete multipartite graph. The converse is verified directly.

The disconnected case is not silently excluded: the equality argument first chooses a component attaining the spectral radius and then the neighborhood-union equality proves that this component contains every vertex.

The corollary for \(r\mid n\) follows by sandwiching the universal inequality between the assumed booksize and
\[
\lambda(T_{n,r})=(r-1)n/r.
\]

## Originality

**PASS, to the best of our knowledge.** The full accessible HTML of Liu--Ning, arXiv:2609.20225, was checked at the statement and proof of Theorem 4.1 and at Theorem 4.2/Remark 4.1. It states the universal inequality and gives \(T_{n,r}\) as a sharpness example when \(r\mid n\), but does not state an equality classification for Theorem 4.1 or uniqueness in that divisible Turán case.

Searches were made for the exact inequality and equivalent formulations using “booksize/book number”, “spectral radius”, “\(2\lambda-n\)”, “\((n+\operatorname{bk})/2\)”, “balanced complete multipartite”, “Turán graph equality”, and “dominating edge”. Nearby spectral-booksize papers by Zhai--Li--Lou, Li--Liu--Zhang, and the classical booksize literature did not reveal the classification.

Two older sources were not inspected in full and are the main residual coverage risks:
- Bollobás--Nikiforov, *Books in graphs* (European J. Combin. 26, 2005), because it is a foundational booksize paper; the accessible abstract describes edge-density extremal and stability results, not a spectral equality theorem.
- Berman--Zhang, *On the spectral radius of graphs with cut vertices* (JCTB 83, 2001), because Liu--Ning cite it for the degree-product spectral bound used in Theorem 4.1. The present record supplies the needed equality argument directly, but an unindexed remark in that paper was not ruled out by full-text inspection.

Because the source theorem is recent, unindexed parallel work remains a residual risk.

## Value

**PASS.** The result upgrades a sharp universal spectral inequality from examples of equality to a complete structural classification. It identifies a rigid extremal family across all possible booksize levels and gives uniqueness of the divisible Turán equality case highlighted in the source paper. The characterization is exact for every order and uses no asymptotic hypothesis.

## Limitations

- No quantitative stability estimate is proved for near equality.
- The result concerns adjacency spectral radius and ordinary triangle books only.
- Originality is to the best of our knowledge; the two older papers listed above were not inspected in full.
- Independent audit has not been performed.
