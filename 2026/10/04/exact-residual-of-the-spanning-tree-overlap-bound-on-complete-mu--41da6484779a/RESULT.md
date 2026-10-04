# Exact residual of the spanning-tree overlap bound on complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge2\), partite sets \(V_1,\ldots,V_r\), part sizes \(n_i=|V_i|\), and \(N=\sum_i n_i\). For \(1\le k\le N\), let
\[
r_k(G)=\frac{d_k(G)}{\binom Nk},
\]
where \(d_k(G)\) is the number of dominating \(k\)-subsets. Following Omar, define
\[
\sigma_k(G)=\sum_{v\in V(G)}\frac{\binom{N-|N[v]|}{k}}{\binom Nk}
\]
and
\[
\tau_k(G)=\max_T\sum_{uv\in E(T)}
\frac{\binom{N-|N[u]\cup N[v]|}{k}}{\binom Nk},
\]
where the maximum is over spanning trees on the vertex set of \(G\), not necessarily subgraphs of \(G\).

Then
\[
\sigma_k(G)=\frac{\sum_{i=1}^r n_i\binom{n_i-1}{k}}{\binom Nk},
\]
\[
\tau_k(G)=\frac{\sum_{i:n_i\ge2}(n_i-1)\binom{n_i-2}{k}}{\binom Nk},
\]
and
\[
r_k(G)=1-\frac{\sum_{i:n_i>k}\binom{n_i}{k}}{\binom Nk}.
\]
More sharply, the error in the spanning-tree overlap bound is exactly
\[
r_k(G)-\bigl(1-\sigma_k(G)+\tau_k(G)\bigr)
=\frac{1}{\binom Nk}
\sum_{i:n_i\ge k+2}(n_i-k-1)\binom{n_i-1}{k-1}.
\]
Hence
\[
r_k(G)=1-\sigma_k(G)+\tau_k(G)
\quad\Longleftrightarrow\quad
\max_i n_i\le k+1.
\]
Thus a newly introduced pairwise-overlap correction has a complete sharpness criterion on a standard dense graph family, and its entire remaining higher-order deficit has a closed form.

## Assumptions and scope
Graphs are finite, simple, and undirected. There are at least two nonempty partite sets. The parameter range is \(1\le k\le N\); the case \(k=0\) is excluded because then cross-part event intersections have weight one rather than zero and require a separate trivial treatment. Binomial coefficients have their usual finite-set meaning. The result concerns Omar's 2026 overlap-corrected domination bound; it does not claim a new proof of the already known unimodality of domination polynomials of complete multipartite graphs.

## Proof
Fix a part \(V_i\) and a vertex \(v\in V_i\). Since \(v\) is adjacent to every vertex outside \(V_i\) and to no other vertex of \(V_i\),
\[
V(G)\setminus N[v]=V_i\setminus\{v\},
\]
so \(N-|N[v]|=n_i-1\). Summing the defining terms over the \(n_i\) vertices of each part gives the formula for \(\sigma_k(G)\).

For two distinct vertices \(u,v\), there are two cases. If they lie in the same part \(V_i\), then
\[
V(G)\setminus\bigl(N[u]\cup N[v]\bigr)=V_i\setminus\{u,v\},
\]
so their pair weight is \(\binom{n_i-2}{k}/\binom Nk\). If they lie in different parts, then \(N[u]\cup N[v]=V(G)\), and because \(k\ge1\) their pair weight is zero.

Any spanning tree on the whole vertex set contains at most \(n_i-1\) edges whose endpoints both lie in \(V_i\). Therefore its total weight is at most
\[
\frac{1}{\binom Nk}\sum_{i:n_i\ge2}(n_i-1)\binom{n_i-2}{k}.
\]
This upper bound is attained: choose a spanning tree inside each non-singleton part and connect the resulting part-components by \(r-1\) cross-part edges, all of weight zero. This proves the formula for \(\tau_k(G)\).

A nonempty set \(S\) that meets at least two parts dominates \(G\). If \(S\subseteq V_i\), then every vertex outside \(V_i\) is dominated, while a vertex of \(V_i\setminus S\) has no neighbor in \(S\). Hence such an \(S\) is dominating exactly when \(S=V_i\). It follows that the non-dominating \(k\)-sets are precisely the proper \(k\)-subsets of single parts. Since \(k\ge1\), these families are disjoint across parts, giving
\[
\binom Nk-d_k(G)=\sum_{i:n_i>k}\binom{n_i}{k},
\]
and therefore the displayed formula for \(r_k(G)\).

It remains to compare the exact value with the pairwise correction. After multiplying by \(\binom Nk\), the contribution of one part of size \(n>k\) to
\(r_k(G)-(1-\sigma_k(G)+\tau_k(G))\) is
\[
n\binom{n-1}{k}-(n-1)\binom{n-2}{k}-\binom nk.
\]
The first two terms differ by \((k+1)\binom{n-1}{k}\). Using Pascal's identity and
\[
\binom{n-1}{k-1}=\frac{k}{n-k}\binom{n-1}{k},
\]
one obtains
\[
n\binom{n-1}{k}-(n-1)\binom{n-2}{k}-\binom nk
=(n-k-1)\binom{n-1}{k-1}.
\]
This is zero when \(n=k+1\) and strictly positive when \(n\ge k+2\); parts with \(n\le k\) contribute zero throughout. Summing over the parts yields the exact residual formula and the sharpness criterion.

## Verification
The included `verify.py` is an independent finite stress test. For every complete multipartite isomorphism type through order \(11\) and every \(1\le k\le N\), it constructs the graph from the part sizes, computes closed neighborhoods, evaluates \(\sigma_k\) directly, computes \(\tau_k\) by a maximum-spanning-tree algorithm on the complete weighted vertex graph, enumerates all \(k\)-subsets to count dominating sets from the definition, and checks all four closed formulas plus the exactness criterion.

The finalized replay output is:

`ALL CHECKS PASSED; multipartite_types=183; parameter_cases=1656; subsets=177373; max_order=11`

This finite computation is a stress test only; the universal statement follows from the analytic proof above.

## Relationship to prior work
Omar's *New Perspectives on the Unimodality of Domination Polynomials* (arXiv:2601.14494v1, first public 2026-01-20) introduces \(\sigma_k(G)\), the spanning-tree overlap correction \(\tau_k(G)\), and the lower bound
\[
r_k(G)\ge1-\sigma_k(G)+\tau_k(G).
\]
The paper specifically motivates \(\tau_k\) by repeated or highly overlapping closed neighborhoods and, in its conclusion, identifies higher-order overlap corrections and the best corrections for graph families as an open direction.

Beaton and Brown's *On the Unimodality of Domination Polynomials* (arXiv:2012.11813v1) had already proved unimodality for complete multipartite graphs and used their explicit domination structure. That result supplies an important boundary comparison but predates \(\tau_k\) and does not evaluate the 2026 overlap statistic or its residual.

Targeted searches for the new parameter together with complete-multipartite, complete-bipartite, spanning-tree-overlap, closed-neighborhood-overlap, and normalized-coefficient formulations located no statement implying the formulas or the sharpness criterion above. The closest indexed complete-multipartite domination records concern different domination variants.

## Limitations
The theorem is confined to finite complete multipartite graphs and to \(k\ge1\). It evaluates the first pairwise spanning-tree correction exactly but does not construct a general higher-order correction scheme for arbitrary graphs. The residual formula identifies the total correction still needed on this family, not a unique canonical decomposition into triple and higher intersections. As with any literature search, an equivalent formulation under terminology not surfaced by the inspected sources remains a residual originality risk.

## References
1. Mohamed Omar, *New Perspectives on the Unimodality of Domination Polynomials*, arXiv:2601.14494v1, 2026. Section 4 defines \(\sigma_k\) and \(\tau_k\), proves the spanning-tree overlap bound, and Section 6 discusses higher-order overlap corrections.
2. Iain Beaton and Jason I. Brown, *On the Unimodality of Domination Polynomials*, arXiv:2012.11813v1, 2020; later published in *Graphs and Combinatorics* 38 (2022). The paper proves unimodality for complete multipartite domination polynomials.
