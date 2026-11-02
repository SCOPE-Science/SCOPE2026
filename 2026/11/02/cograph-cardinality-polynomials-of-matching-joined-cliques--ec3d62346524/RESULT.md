# Cograph cardinality polynomials of matching-joined cliques

## Finding

Let \(G_{a,b,t}\) be the graph formed from disjoint cliques of orders \(a\) and \(b\) by adding a matching of size \(t\) between them. Throughout, \(a,b,t\) are integers satisfying \(3\le t\le\min(a,b)\). Equivalently, \(G_{a,b,t}\) is the complement of the graph obtained by deleting a matching of size \(t\) from \(K_{a,b}\).

A *cograph* is a graph with no induced four-vertex path. Define \(C_{a,b,t}(z)\) to count **all** vertex subsets inducing cographs, including the empty set, by their cardinality. Define \(M_{a,b,t}(z)\) to count **inclusion-maximal** such subsets, again by cardinality. Write \(\delta_{a,t}=1\) when \(a=t\) and \(0\) otherwise, and similarly for \(\delta_{b,t}\).

**Theorem.** Both complete cardinality polynomials are
\[
\begin{aligned}
C_{a,b,t}(z)={}&(1+z)^{a+b-2t}(1+2z)^t\\
&+tz^2\big((1+z)^{a-1}+(1+z)^{b-1}-1\big)
+\binom{t}{2}z^4,
\end{aligned}
\]
\[
\boxed{
M_{a,b,t}(z)=\binom{t}{2}z^4
+t z^{a+1}+t z^{b+1}
+\bigl(2^t-(t+1)(\delta_{a,t}+\delta_{b,t})\bigr)z^{a+b-t}.
}
\]
Coefficients at equal exponents are summed. Each polynomial counts labelled vertex subsets of the specified graph, not graph isomorphism types.

In particular, \(G_{n,n,n}=K_2\square K_n\) is the two-row rook graph, for which
\[
M_{n,n,n}(z)=\binom n2 z^4+(2^n-2n-2)z^n+2nz^{n+1}.
\]
For every \(n\ge6\), the inclusion-maximal induced cographs have precisely the three sizes \(4,n,n+1\), so none of the \(n-5\) consecutive integers \(5,6,\ldots,n-1\) is attainable. The number of maximal sets is \(2^n+\binom n2-2\); the proportion of them of size \(n\) tends to one, with error \(O(n^2/2^n)\).

## Assumptions and scope

All graphs are finite, undirected and simple, and vertices are distinct and labelled. The matching joining the cliques has pairwise disjoint endpoints. Denote the first clique's vertices by \(x_1,\ldots,x_a\), the second clique's vertices by \(y_1,\ldots,y_b\), and the joining edges by \(x_i y_i\) for \(1\le i\le t\). A vertex subset is inclusion-maximal if no strict superset of it induces a cograph. Since cographs form a hereditary class, checking all single-vertex additions is sufficient. The theorem covers all \(3\le t\le\min(a,b)\), without any parity assumptions. The full-subset formula also happens to extend to smaller matching sizes, but these cases are not needed for the joint theorem.

## Proof

**Induced-path criterion.** Let \(S\) select sets \(X\subseteq\{x_1,\ldots,x_a\}\) and \(Y\subseteq\{y_1,\ldots,y_b\}\). An induced four-vertex path can use at most two vertices from either clique, since any three within one clique form a triangle. It therefore uses two from each clique, with its middle edge one of the joining matching edges. More precisely, it exists exactly when some \(i\le t\) has \(x_i,y_i\in S\) and there are \(x\in X\setminus\{x_i\}\) and \(y\in Y\setminus\{y_i\}\) that are not joined by a matching edge. The four vertices then give the induced path \(x-x_i-y_i-y\). Conversely, every induced four-vertex path has this form, possibly with its endpoints reversed.

Write \(B(S)=\{i\le t:x_i,y_i\in S\}\), the set of *selected matching bridges*. If \(B(S)\) is empty, the selected graph is the disjoint union of two cliques and is a cograph. If one selected shore has size at most one, the selected graph is also a cograph. Finally, when \(B(S)\ne\varnothing\) and \(|X|,|Y|\ge2\), fix \(i\in B(S)\). Avoiding an induced four-vertex path forces every pair from \(X\setminus\{x_i\}\) and \(Y\setminus\{y_i\}\) to be a joining matching edge. Since these two sets are nonempty and the cross edges form a matching, each must be a singleton, and those two vertices must be the endpoints of a second matching edge. Thus \(S\) consists exactly of the four endpoints of two joining matching edges. Conversely, those four vertices induce a four-cycle, which is a cograph. We have proved the following **exhaustive criterion**: \(S\) induces a cograph if and only if it has no selected matching bridge, has at most one selected vertex in one clique, or consists of precisely two whole matching pairs.

**Counting all induced cographs.** With no selected matching bridge, every matched pair contributes one of three states (neither vertex, first endpoint, second endpoint), giving the factor \((1+2z)^t\); the \(a+b-2t\) unmatched vertices are unrestricted, giving \((1+z)^{a+b-2t}\). With a selected bridge and a singleton second shore, there are \(t\) choices of its matched index \(i\), the two endpoints are forced, and any remaining vertex of the first clique can be selected: this contributes \(tz^2(1+z)^{a-1}\). The symmetric contribution is \(tz^2(1+z)^{b-1}\). Their intersection consists of the \(t\) isolated selected matching pairs, counted twice, so subtract \(tz^2\). The remaining case has exactly two complete matching pairs and contributes \(\binom t2z^4\). The cases are disjoint after inclusion-exclusion, proving the formula for \(C_{a,b,t}\).

**Counting maximal induced cographs: no bridge.** Suppose \(B(S)=\varnothing\). Maximality forces every unmatched vertex to be selected and exactly one endpoint of every matched pair to be selected; if neither endpoint is selected, one can add an endpoint without creating a bridge. Put \(u=a-t\), \(v=b-t\), and let \(k\) matched pairs contribute their first-clique endpoint. Then \(|X|=u+k\), \(|Y|=v+t-k\) and \(|S|=a+b-t\). The set is maximal precisely when both shores have at least two selected vertices, or when one shore consists of its sole unmatched vertex. In the latter situation, adding any missing matched endpoint creates a bridge and an induced four-vertex path using that unmatched vertex. If a shore is empty, one can add a first vertex. If a shore consists of a single **matched** endpoint, one can add its partner without destroying the cograph property. When both shores contain at least two vertices, adding any missing matched endpoint creates exactly one bridge and hence an induced four-vertex path by the criterion above. There are \(\binom tk\) choices for each \(k\). Among all \(2^t\) orientations, exactly \(t+1\) are excluded if \(u=0\), namely \(k=0,1\), and exactly \(t+1\) are excluded if \(v=0\), namely \(k=t,t-1\). Because \(t\ge3\), the two excluded ranges are disjoint. Thus the bridge-free maximal contribution is \(\big(2^t-(t+1)(\delta_{a,t}+\delta_{b,t})\big)z^{a+b-t}\).

**Counting maximal induced cographs: at least one bridge.** If one selected shore is a singleton, maximality first forces the opposite clique to be wholly selected, because adding another vertex on that opposite shore preserves the singleton condition. The singleton must be one of the \(t\) matched vertices, with its partner already selected. Conversely, because the opposite clique has size at least three, adding any remaining vertex on the singleton shore creates an induced four-vertex path. These cases contribute \(tz^{a+1}+tz^{b+1}\). If both shores have at least two vertices, the preceding criterion forces exactly two complete matching pairs; every further vertex destroys the cograph condition. They contribute \(\binom t2z^4\). These classes are mutually disjoint and exhaust all maximal cases, proving \(M_{a,b,t}\).

**Specialization.** Substitute \(a=b=t=n\) and simplify. For \(n\ge6\), all three displayed coefficients are positive and their exponents \(4,n,n+1\) are distinct. The gap and total count follow immediately. The size-\(n\) coefficient is \(2^n-2n-2\), whereas the total count is \(2^n+\binom n2-2\); their ratio tends to one with the stated error.

## Verification

The standalone file `verify_cograph_matching.py` constructs the graph directly and tests cograph membership by searching all induced four-vertex subgraphs for the path degree pattern \((1,1,2,2)\) with three edges. It independently checks one-vertex inclusion-maximality, both structural characterizations, and every polynomial coefficient. Run `python3 verify_cograph_matching.py`. On the recorded execution it returned:

`VERIFY_OK graph_instances=57 direct_subsets=320832 cograph_and_maximal_structural_checks=PASS both_polynomials=PASS`

The finite verification covers \(57\) triples of parameters and \(320832\) vertex subsets. It is corroborating evidence, not a substitute for the all-parameter proof above.

## Relationship to prior work

Brosse, Lagoutte, Limouzy, Mary and Pastor established polynomial-delay enumeration of maximal induced cographs in arbitrary graphs. Their proof develops an algorithm via twin construction orderings and proximity search rather than a closed cardinality polynomial for matching-joined cliques. Cao gave general algorithms for maximal induced hereditary subgraphs; those complexity statements likewise do not supply the present exact coefficients. Dąbrowski, Lozin and Stacho study the general *co-bipartite matching graph* class and describe the strictly matched subfamily; their graph-partition algorithms do not count induced cograph subsets. The two-row rook graph is the line graph of a complete bipartite graph and the complement of a crown graph, so the specialization is a natural graph family rather than an artificial parameter slice.

## Limitations

The theorem is for induced vertex subsets, not maximal spanning-edge subgraphs or arbitrary cograph modifications. The maximal-set formula is stated only for \(3\le t\le\min(a,b)\); cases with fewer joining edges require separate boundary classification. No claim is made about arbitrary co-bipartite graphs with nonmatching cross edges. The finite program does not certify infinite parameter ranges. The literature comparisons support provisional priority only; an equivalent unindexed formulation remains possible. Independent mathematical audit has not been performed.

## References

1. C. Brosse, A. Lagoutte, V. Limouzy, A. Mary, L. Pastor, *Efficient enumeration of maximal split subgraphs and induced sub-cographs and related classes*, first public arXiv preprint July 2, 2020, arXiv:2007.01031, https://arxiv.org/abs/2007.01031. Later published in *Discrete Applied Mathematics* 345 (2024), 34–51.
2. Y. Cao, *Enumerating Maximal Induced Subgraphs*, arXiv:2004.09885, first public April 21, 2020, https://arxiv.org/abs/2004.09885.
3. A. Conte, R. Grossi, A. Marino, T. Uno, L. Versari, *Proximity Search for Maximal Subgraph Enumeration*, arXiv:1912.13446, https://arxiv.org/abs/1912.13446; *SIAM Journal on Computing* 51 (2022), 1580–1625.
4. *Rook Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/RookGraph.html (standard identification of \(K_2\square K_n\) and the complement of a crown graph).
5. K. Dąbrowski, V. Lozin, J. Stacho, *Graph Partitions Below 3-colourability*, open manuscript, https://www.cs.toronto.edu/~stacho/public/partitions7.pdf, Theorem 1 (co-bipartite matching graphs) and Theorem 9 (graph-partition algorithm).
