# Zero-forcing sets of triangular graphs are complements of forests with an isolated vertex

## Finding

For every integer \(n\ge 2\), let \(T_n=L(K_n)=J(n,2)\), the triangular graph with one vertex for each edge of the complete graph \(K_n\). Two vertices of \(T_n\) are adjacent precisely when their corresponding complete-graph edges share an endpoint. The ordinary zero-forcing rule allows a blue vertex having exactly one white neighbor to recolor that neighbor blue.

**Theorem.** A set \(B\subseteq V(T_n)\) is an ordinary zero-forcing set if and only if the spanning graph \(H_B=([n],E(K_n)\setminus B)\), whose edges are the initially white vertices of \(T_n\), is a forest possessing at least one isolated vertex. Here the identification of \(B\) with a subset of \(E(K_n)\) is understood.

Let \(m=\binom n2\), and let \(f_j(t)\) be the labeled-forest polynomial on \([j]\) by number of edges, with \(f_0(t)=1\). Define \(a_1=1\) and \(a_k=k^{k-2}\) for every \(k\ge2\). Then, for all \(j\ge1\),
\[
f_j(t)=\sum_{k=1}^j\binom{j-1}{k-1}a_k t^{k-1}f_{j-k}(t).
\]
For each integer \(n\ge2\), the complete ordinary zero-forcing polynomial is
\[
\boxed{\mathcal Z(T_n;x)=x^{m}\sum_{j=1}^n(-1)^{j-1}\binom nj f_{n-j}(x^{-1}).}
\]
The displayed expression is an ordinary polynomial in \(x\), not merely a Laurent expression, because only forests with at least one isolated vertex survive the alternating sum.

Equivalently, let \(g_n(t)\) count labeled forests on \([n]\) with at least one isolated vertex by number of edges, and put \(g_0(t)=0\). Then their formal exponential generating function is
\[
\boxed{\sum_{n\ge0}g_n(t)\frac{u^n}{n!}
=(1-e^{-u})\exp\!\left(\sum_{k\ge1}a_k t^{k-1}\frac{u^k}{k!}\right).}
\]
In particular, \(\mathcal Z(T_n;x)=x^m g_n(x^{-1})\).

For \(n\ge3\), every minimum zero-forcing set is the complement of a spanning tree on precisely \(n-1\) of the \(n\) labels, with the remaining label isolated. There are exactly
\[
\boxed{n(n-1)^{n-3}}
\]
such minimum sets, all of cardinality \(\binom n2-n+2\). For \(n=2\), the one-vertex graph \(T_2\) has the sole zero-forcing set \(V(T_2)\), so \(\mathcal Z(T_2;x)=x\) and there is one minimum set.

## Assumptions and scope

Graphs are finite, simple, and undirected; tree and forest mean undirected acyclic graphs, with isolated vertices retained in spanning graphs. The zero-forcing polynomial sums \(x^{|B|}\) over all successful initial blue sets \(B\). A vertex of degree zero in the white-edge graph \(H_B\) means that no edge of \(K_n\) incident to that vertex is initially white. The rule is ordinary zero forcing, not positive-semidefinite or skew zero forcing. The theorem covers every integer \(n\ge2\) with labeled complete-graph vertices. The formal generating-function coefficient at \(n=0\) is set to zero because the empty graph on zero labels has no isolated vertex; no assertion is made about a zero-vertex triangular graph.

## Proof

First suppose the white-edge graph \(H_B\) contains a cycle \(C\). An initially white edge on \(C\), regarded as a vertex of \(T_n\), has two distinct initially white neighbors given by the two cycle edges adjacent to it. No cycle edge can ever be the first edge of \(C\) recolored blue, since before such a first recoloring all cycle edges remain white and any blue vertex adjacent to a cycle edge encounters either zero or at least two white cycle edges. More directly, any blue edge of \(K_n\) cannot have exactly one adjacent edge from the cycle: if both its endpoints lie on \(C\), it meets at least four cycle edges (or two in the triangular case with a chord absent from the cycle); if exactly one endpoint lies on \(C\), it meets the two cycle edges at that endpoint; otherwise it meets none. Thus the edges of \(C\) cannot be forced, and \(B\) is not zero forcing.

Next suppose that \(H_B\) has **no isolated vertex** and contains at least one white edge. Every blue edge \(uv\) of \(K_n\) has at least one white edge incident to \(u\) and at least one white edge incident to \(v\). These are distinct, because the edge \(uv\) itself is blue. Hence no initially blue vertex of \(T_n\) has a unique white neighbor. The coloring cannot advance and \(B\) is not zero forcing.

Conversely, assume \(H_B\) is a forest with isolated vertex \(s\). If the forest contains any edge, it has a component containing an edge and therefore a leaf \(u\) of positive degree one; denote the unique white edge at \(u\) by \(uv\). The complete-graph edge \(su\) is blue because \(s\) is isolated in \(H_B\). In the triangular graph, the vertex corresponding to \(su\) has exactly one white neighbor: \(uv\), since there are no white edges incident to \(s\) and only \(uv\) is white at \(u\). Thus \(su\) forces \(uv\). Removing that edge from \(H_B\) leaves a forest and preserves the isolated vertex \(s\). Repeating recolors every white edge blue. If \(H_B\) initially has no edges, all vertices of \(T_n\) are already blue. This proves the if-and-only-if statement, including \(n=2\).

To enumerate labeled forests, look at the component of the vertex labeled \(1\) in a forest on \([j]\). If it contains \(k\) vertices, choose its other \(k-1\) labels in \(\binom{j-1}{k-1}\) ways, select a labeled tree in \(a_k\) ways by Cayley's formula (including the singleton convention), and select an arbitrary forest on the remaining \(j-k\) labels. Its tree has \(k-1\) edges. This yields the displayed recurrence for \(f_j(t)\).

Apply inclusion-exclusion to the events that each specified vertex is isolated in a forest on \([n]\). For a prescribed set of \(j\) isolated vertices the remaining forest is arbitrary, of enumerator \(f_{n-j}(t)\), and there are \(\binom nj\) choices for the prescribed set. Consequently the forest-with-isolate polynomial is
\[
g_n(t)=\sum_{j=1}^n(-1)^{j-1}\binom nj f_{n-j}(t).
\]
By the structural characterization, every such forest contributes a zero-forcing set with \(m-|E(H_B)|\) blue vertices, establishing the polynomial formula. Standard labeled-component enumeration gives the generating function for all forests as \(\exp(\sum_{k\ge1}a_k t^{k-1}u^k/k!)\). Forbidding all singleton components multiplies this by \(e^{-u}\), so requiring at least one isolated vertex multiplies by \(1-e^{-u}\). All identities hold as formal power series and require no analytic convergence.

A forest on \(n\ge3\) labels having an isolated vertex has at most \(n-2\) edges. Equality requires exactly two components, one a single isolated label and the other a tree on the remaining \(n-1\) labels. Thus minimum zero-forcing sets are precisely their edge complements. There are \(n\) choices for the isolate and, by Cayley's formula, \((n-1)^{n-3}\) labeled trees on the other labels. The known minimum cardinality follows, and the multiplicity formula is proved. For \(n=2\), the unique forest with an isolate and no edges produces the unique successful set.

## Verification

The standalone file `verify.py` tests the equivalence using two independently implemented predicates: (i) a direct step-by-step ordinary zero-forcing simulation on \(T_n\); and (ii) disjoint-set-cycle detection and degree-zero testing on the white-edge graph. It exhaustively compares all \(2^{\binom n2}\) initial sets for \(2\le n\le6\), totaling 33,866 initial sets. It also compares 4,096 reproducibly sampled initial sets for each \(7\le n\le11\), totaling 20,480 additional checks. Every coefficient for \(2\le n\le6\) is independently compared against the labeled-forest recurrence; small and larger minimum-set formulas and selected boundary coefficients are checked through \(n=16\). In all, 54,346 forcing simulations agree with the structural predicate; the captured output appears in `verify_output.txt`.

The check is reproducible by running `python3 verify.py` with a standard Python 3 installation from the directory containing the files. Exhaustive agreement at the listed small orders is not an infinite proof; the argument under **Proof** is the infinite proof.

For example,
\[
\begin{aligned}
\mathcal Z(T_3;x)&=3x^2+x^3,\\
\mathcal Z(T_4;x)&=12x^4+6x^5+x^6,\\
\mathcal Z(T_5;x)&=80x^7+45x^8+10x^9+x^{10},\\
\mathcal Z(T_6;x)&=750x^{11}+420x^{12}+105x^{13}+15x^{14}+x^{15}.
\end{aligned}
\]

## Relationship to prior work

Boyer, Brimkov, English, Ferrero, Keller, Kirsch, Phillips, and Reinhart (2018) introduced the zero-forcing polynomial and evaluated it for several graph families. Fallat, Meagher, Soltani, and Yang (2015) studied positive zero forcing and clique coverings for \(J(n,2)\); their positive variant does not imply an enumeration of all ordinary forcing sets. Abiad, Simoens, and Zeijlemaker (2023) establish, among other cases, the **already-known** ordinary zero-forcing number of \(J(n,2)\), namely \(\binom n2-n+2\). Afzali, Ghodrati, and Maimani (2024) study the largest *failed* zero-forcing set in Johnson graphs, another extremal parameter. Neither the earlier scalar result nor the published abstract of the failed-set result determines the full cardinality polynomial or the exact structure and number of all successful sets.

The new contribution assessed here is the all-set forest-with-isolate characterization, its full labeled-forest polynomial and generating function, and the resulting exact minimum-set multiplicities. Cayley's classical tree count and the general labeled-forest exponential formula are credited as established ingredients, not claimed to be new. No claim of uniqueness across all unindexed or inaccessible literature is made.

## Limitations

This is a theorem for ordinary zero forcing of the **triangular graphs** \(J(n,2)\), not for general Johnson graphs \(J(n,k)\) with \(k>2\), other line graphs, or other zero-forcing variants. The historical minimum zero-forcing number is not a new result. The full 2024 paper on failed forcing sets of Johnson graphs was not available for inspection through authorized noninteractive access; its accessible abstract concerns a different extremal invariant, but potential unstated overlap in its proofs remains a residual literature risk. Computation checks only the explicitly listed finite orders and samples; it does not serve as a certificate for the infinite assertion.

## References

1. K. Boyer, B. Brimkov, S. English, D. Ferrero, A. Keller, R. Kirsch, M. Phillips, and C. Reinhart, *The zero forcing polynomial of a graph*, arXiv:1801.08910 (initial public version 2018-01-26). https://arxiv.org/abs/1801.08910
2. A. Abiad, R. Simoens, and S. Zeijlemaker, *On the diameter and zero forcing number of some graph classes in Johnson, Grassmann and Hamming association schemes*, arXiv:2302.07757 (initial public version 2023-02-15). https://arxiv.org/abs/2302.07757
3. S. Fallat, K. Meagher, A. Soltani, and B. Yang, *Compressed cliques graphs, clique coverings and positive zero forcing*, arXiv:1508.07357 (initial public version 2015-08-28). https://arxiv.org/abs/1508.07357
4. F. Afzali, A. H. Ghodrati, and H. R. Maimani, *Failed zero forcing numbers of Kneser graphs, Johnson graphs, and hypercubes*, *Journal of Applied Mathematics and Computing* 70 (2024), 2665–2675. DOI:10.1007/s12190-024-02064-w.
5. A. Cayley, *A theorem on trees*, *Quarterly Journal of Pure and Applied Mathematics* 23 (1889), 376–378 (classical labeled-tree enumeration).
