# A single-edge deletion creates lacunary maximal edge-general-position spectra in bicliques

## Finding
Let \(p,q\geq2\) be integers. Fix an edge \(ab\) in \(K_{p,q}\), and let \(G_{p,q}=K_{p,q}-ab\). A set \(F\subseteq E(G_{p,q})\) is in **edge general position** if each shortest path of \(G_{p,q}\) contains at most two edges of \(F\). Write \(E_{p,q}(z)=\sum_{F\text{ edge general position}}z^{|F|}\), and let \(M_{p,q}(z)\) be the analogous polynomial restricted to inclusion-wise maximal such sets. Put \(s=p-1\) and \(t=q-1\). Then
\[
E_{p,q}(z)=\sum_{i=0}^{t}\sum_{j=0}^{s}\binom ti\binom sj z^{i+j}(1+z)^{st-ij},
\]
and
\[
M_{p,q}(z)=z^{st+t}+z^{st+s}+\sum_{i=1}^{t}\sum_{j=1}^{s}\binom ti\binom sj z^{st+i+j-ij}.
\]
In particular, exactly \((2^s-1)(2^t-1)+2\) inclusion-wise maximal sets exist, their smallest cardinality is \(s+t\), and their largest cardinality is \(st+\max\{s,t\}\). For every integer \(m\ge3\), the balanced defective biclique \(G_{m+1,m+1}\) has maximal edge-general-position sets of sizes \(m^2+1\) and \(m^2+m\), but none of sizes \(m^2+2,m^2+3,\ldots,m^2+m-1\). Thus the maximal-set cardinality spectrum has arbitrarily long gaps after removal of one edge from a complete bipartite graph.

## Assumptions and scope
Graphs are finite, undirected, simple, and labeled. Both bipartition classes have at least two vertices, so deleting the edge \(ab\) does not disconnect the graph. Maximal always means inclusion-wise maximal, not maximum cardinality. The generating functions count distinct edge subsets of the fixed labeled graph, not graph-isomorphism orbits.

Write the two vertex classes as \(A=\{a\}\cup A'\) and \(B=\{b\}\cup B'\), with \(|A'|=s\), \(|B'|=t\). Thus the edges of \(G_{p,q}\) are precisely the left spokes \(\{ax:x\in B'\}\), the right spokes \(\{yb:y\in A'\}\), and the middle edges \(\{xy:x\in B',y\in A'\}\).

## Proof
**Geodesic reduction.** All pairs of distinct vertices except \(a,b\) have distance at most two: pairs in one part have a common neighbor because both residual parts are nonempty; an opposite-part pair other than \(a,b\) is adjacent. The missing pair has distance three, and its shortest paths are exactly \(a-x-y-b\) with \(x\in B'\), \(y\in A'\). Accordingly, a set \(F\) is in edge general position precisely if it does not contain all three edges \(ax,xy,yb\) for any such pair \((x,y)\).

**All-set enumerator.** Let \(L=\{x\in B':ax\in F\}\) and \(R=\{y\in A':yb\in F\}\), with \(|L|=i\), \(|R|=j\). The geodesic reduction says that no edge of the rectangle \(L\times R\) may belong to \(F\), whereas any of the other \(st-ij\) middle edges may be independently selected. Choosing \(L,R\) in \(\binom ti\binom sj\) ways gives precisely \(\binom ti\binom sj z^{i+j}(1+z)^{st-ij}\), proving the first polynomial.

**Maximal-set classification.** Every inclusion-maximal \(F\) must contain all currently permitted middle edges, because adding a missing permitted middle edge cannot create a forbidden triple. Conversely suppose all permitted middle edges are present. If both \(L\) and \(R\) are nonempty, inserting any missing spoke \(ax\) with \(x\notin L\) is forbidden by the already selected path edges \(xy,yb\) for any \(y\in R\); likewise inserting a missing spoke \(yb\) with \(y\notin R\) is forbidden by any \(x\in L\). Thus every nonempty/nonempty pair \((L,R)\) produces a maximal set. If \(R=\varnothing\), a missing left spoke is always addable; maximality therefore forces \(L=B'\). Once \(L=B'\), every missing right spoke is blocked by any corresponding middle edge, so the resulting set is maximal. The case \(L=\varnothing\) is symmetric and yields \(R=A'\). The empty/empty case is never maximal. These three mutually exclusive types exhaust all maximal sets.

**Maximal polynomial and endpoints.** In each case, \(F\) contains exactly \(st-ij\) middle edges and \(i+j\) spokes, hence has size \(st+i+j-ij\). The two one-sided cases respectively have sizes \(st+t\) and \(st+s\). Summing over the mixed nonempty/nonempty pairs gives the second polynomial. Setting \(z=1\) proves the total maximal-set count.

For \(i,j\ge1\), \(st+i+j-ij\le st+1\) because \((i-1)(j-1)\ge0\), so no mixed configuration exceeds either one-sided size. This proves the largest-cardinality formula. To bound below, observe that increasing either \(i\) or \(j\) weakly decreases \(st+i+j-ij\) whenever the other is at least one; its minimum on \([1,t]\times[1,s]\) occurs at \((t,s)\), with value \(s+t\). Each one-sided size is at least \(s+t\), since \(st\ge s,t\). Hence the smallest maximal size is \(s+t\).

**An unbounded gap.** For \(s=t=m\ge3\), the mixed sizes are at most \(m^2+1\), achieved, for example, with \(i=1,j=1\), while both one-sided cases have size \(m^2+m\). The integers strictly between these two values never occur in \(M_{m+1,m+1}\), giving a missing interval of length \(m-2\), which grows without bound. This also proves non-purity (maximal sets need not have the same size).

## Verification
The standalone \(\texttt{verify.py}\) builds each graph directly, discovers all three-edge geodesic constraints by breadth-first search, and independently enumerates every edge subset and tests extension maximality. It compares both size distributions against the two polynomials. All nine parameter pairs \((p,q)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\) passed. For example, \(M_{4,4}(z)=z^6+6z^8+9z^9+33z^{10}+2z^{12}\), exhibiting the missing exponent eleven. These finite checks validate the implementation on small instances but do not replace the general proof.

To reproduce, run \(\texttt{python verify.py}\) using a standard Python 3 installation; no third-party dependencies are required.

## Relationship to prior work
The edge general position notion was introduced by Manuel, Prabha and Klavžar (2021). Their paper determines scalar edge-general-position numbers for hypercubes, rectangular grids and trees; the present two exact size enumerators for a one-edge-defective biclique are not a stated consequence of those results. Tian, Klavžar and Tan (2023 preprint; 2024 journal) determine extremal scalar numbers and study block graphs. In particular their diameter-two lemma explains why **every edge subset** of the undeleted complete bipartite graph is in edge general position: without deleting an edge, the all-set polynomial is \((1+z)^{pq}\), with a single maximal set. The present theorem quantifies the full change caused by deleting one edge.

The 2025 work of Cao, Ji and Wang studies edge general position numbers of certain graph families, including bipartite graphs. Only its accessible metadata and abstract were inspected; no claim of complete noncoverage of its inaccessible full text is made. Comparison against published mathematical finding summaries identified results for complete multipartite edge-geodesic covering, matching-deleted biclique geodesic subpath numbers, and spider-tree edge general position sets. Those concern different invariants or graph families; none of their recovered claims gives the two polynomials or the maximal-cardinality gap. General search and index results cannot prove absolute novelty.

## Limitations
The conclusion concerns deletion of exactly one edge with \(p,q\ge2\); deleting larger matchings can introduce additional geodesic types and is not covered. The formulas count labeled edge subsets, not symmetry classes. The claims about originality are provisional against unindexed or inaccessible prior work, especially the full 2025 paper just noted. Independent external validation has not been performed.

## References
1. P. Manuel, R. Prabha, S. Klavžar, *Edge general position problem*, arXiv:2105.04292 (first posted 2021-05-10), https://arxiv.org/abs/2105.04292.
2. J. Tian, S. Klavžar, E. Tan, *Extremal edge general position sets in some graphs*, arXiv:2302.01587 (first posted 2023-02-03), https://arxiv.org/abs/2302.01587; *Graphs and Combinatorics* 40, article 40 (2024), https://doi.org/10.1007/s00373-024-02770-z.
3. P. Manuel, R. Prabha, S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357 (2022), https://arxiv.org/abs/2207.07357.
4. Y. Cao, S. Ji, L. Wang, *The edge general position number of some graphs*, *Bulletin of the Malaysian Mathematical Sciences Society* (2025), https://doi.org/10.1007/s40840-025-01873-x (full text not inspected).
