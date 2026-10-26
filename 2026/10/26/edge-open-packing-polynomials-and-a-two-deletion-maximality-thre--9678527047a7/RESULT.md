# Edge-open-packing polynomials and a two-deletion maximality threshold in bicliques

## Finding

Let \(p,q\ge3\), \(0\le t\le\min\{p,q\}\), and let \(G_{p,q,t}\) be obtained from the labeled complete bipartite graph \(K_{p,q}\) by deleting \(t\) mutually disjoint edges. For a finite graph, an *edge-open-packing* is an edge subset in which no two distinct chosen edges admit a third graph edge joining one endpoint of the first to one endpoint of the second. The empty set is included by convention in the counting polynomial.

Put \(S_d(z)=(1+z)^d-1-dz\). The polynomial of **all** edge-open-packings, counted by cardinality, is

\[
\begin{aligned}
P_{p,q,t}(z)={}&1+(pq-t)z
 +(p-t)S_q(z)+tS_{q-1}(z)\\
 &+(q-t)S_p(z)+tS_{p-1}(z)+\binom{t}{2}z^2.
\end{aligned}
\]

The polynomial of **inclusion-maximal** edge-open-packings is

\[
M_{p,q,t}(z)=(p-t)z^q+t z^{q-1}+(q-t)z^p+t z^{p-1}+\binom{t}{2}z^2.
\]

More precisely, every nonempty inclusion-maximal packing is either (i) the complete star of one vertex or (ii) a pair of *reciprocal* edges \(a_i b_j\), \(a_j b_i\) indexed by distinct deleted matching edges \(a_i b_i\), \(a_j b_j\). No reciprocal pair can be extended by another edge. In particular, there are exactly \(p+q+\binom t2\) maximal packings.

For balanced bicliques \(G_{n,n,t}\) with \(n\ge4\), the smallest possible cardinality among maximal packings is \(n\) for \(t=0\), \(n-1\) for \(t=1\), and \(2\) for every \(2\le t\le n\). Their largest cardinality is \(n\) for \(t<n\) and \(n-1\) for \(t=n\). Thus deleting just **two disjoint edges** can reduce the smallest maximal packing from \(n\) to \(2\) while leaving the maximum packing size equal to \(n\), producing an unbounded maximum-minus-minimum gap of \(n-2\) for every \(n\ge4\).

## Assumptions and scope

The graphs are finite and simple. Label the two sides \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_q\}\); after relabeling, the missing edges are exactly \(a_i b_i\) for \(1\le i\le t\). An edge-open-packing is tested against the **original graph's** edge set, not the edge set of the chosen packing. A third connecting edge must differ from the two chosen edges. A star is the set of all edges incident with one vertex. A *maximal* packing is inclusion-wise maximal; this is distinct from maximum cardinality. The bounds \(p,q\ge3\) ensure every star has at least two edges, including in the full-matching-deletion cases.

The coefficients of \(P_{p,q,t}\) and \(M_{p,q,t}\) count distinct labeled edge subsets, not isomorphism classes. Replacing the particular deleted matching by any matching of the same size gives an isomorphic graph and preserves all counts.

## Proof

**Step 1: compatible pairs.** Write existing graph edges as ordered pairs \((i,j)\) denoting \(a_i b_j\). If distinct chosen edges \((i,j)\) and \((k,\ell)\) share an endpoint, they are compatible: the graph is bipartite, so any potential connector between their endpoints is one of the chosen edges itself. Suppose the chosen edges are disjoint, so \(i\ne k\) and \(j\ne\ell\). Their only possible third connecting edges are the two *cross edges* \((i,\ell)\) and \((k,j)\). Both must be missing. Since the missing edges form a matching, this happens if and only if \(i=\ell\le t\), \(k=j\le t\), and \(i\ne k\). Therefore the only compatible disjoint pairs are the reciprocal pairs \(\{(i,k),(k,i)\}\) with distinct \(i,k\le t\).

**Step 2: reciprocal pairs cannot be extended.** Fix a compatible disjoint pair \(e=(i,k)\), \(f=(k,i)\). An additional edge \(g\) compatible with \(e\) must either intersect \(e\) or be its unique compatible disjoint partner \(f\), by Step 1. As \(g\ne f\), it must intersect \(e\). Similarly, \(g\) must intersect \(f\). But the only possible bipartite edges joining one endpoint of \(e\) to one endpoint of \(f\) are the missing diagonals \((i,i)\) and \((k,k)\). Hence no third edge exists.

**Step 3: all larger packings are stars.** A packing of at least three edges cannot contain a compatible disjoint pair, by Step 2. Thus all of its edges are pairwise incident. In a simple bipartite graph, at least three pairwise incident edges must have a common endpoint, since the only alternative would be a triangle. Thus every packing with at least three edges is contained in a star. Conversely every subset of a star is an edge-open-packing, by Step 1.

**Step 4: both polynomials and maximality.** The empty packing contributes \(1\); the \(pq-t\) singleton edge sets contribute \((pq-t)z\). Every star subset of size at least two has a **unique center**, since two distinct edges cannot share two endpoints. There are \(p-t\) centers of degree \(q\), \(t\) of degree \(q-1\), \(q-t\) of degree \(p\), and \(t\) of degree \(p-1\). A center of degree \(d\) contributes \(S_d(z)=\sum_{k=2}^{d}\binom dk z^k\). In addition, there are exactly \(\binom t2\) disjoint reciprocal edge pairs. This proves the formula for \(P_{p,q,t}\).

Every reciprocal pair is maximal by Step 2. Every full star is maximal because it has at least two edges and any extension of size at least three must be in the same star by Step 3. Conversely a non-full star subset of size at least two extends inside that star; a singleton extends because every endpoint has degree at least two, and the empty set extends because the graph has edges. Hence the full stars and reciprocal pairs are precisely the maximal packings. Counting the full stars by their degrees proves \(M_{p,q,t}\).

**Step 5: sharp two-deletion transition.** For \(p=q=n\ge4\), substitute into the exact maximal polynomial:
\[
M_{n,n,t}(z)=2(n-t)z^n+2t z^{n-1}+\binom t2 z^2.
\]
For \(t=0\), only exponent \(n\) appears; for \(t=1\), the smallest exponent is \(n-1\); for \(t\ge2\), exponent \(2\) appears. If \(t<n\) the \(z^n\)-term is nonzero, and if \(t=n\) the largest exponent is \(n-1\). This proves all asserted minima, maxima, and unbounded gaps.

## Verification

A standalone pure-Python checker (`verification/verify_eop_matching.py`) rebuilds the graph from its edge list, independently tests every pair of edges for a third connecting edge, enumerates **every** compatible edge subset using a separate compatibility-search recursion, tests inclusion-maximality against all unused graph edges, and compares both resulting cardinality dictionaries with the closed formulas. The tested domain was all \(78\) triples with \(3\le p,q\le6\) and \(0\le t\le\min(p,q)\), totaling \(15{,}961\) admissible subsets (including empty sets). All polynomial coefficients and maximal-set coefficients matched. The computations are finite checks; the proof above establishes the full infinite-domain result.

## Relationship to prior work

Chelladurai, Kalimuthu and Soundararajan (2022) introduced edge-open-packing and determined the maximum size for complete multipartite graphs, which gives the \(t=0\) maximum in the present setting. Brešar and Samadi (arXiv:2403.00750, first public March 1, 2024) proved general bounds on how the maximum changes after removing one edge. Pandey and Santra (arXiv:2508.01935) gave broader scalar characterizations. These are not claimed as new. The present result identifies and counts every admissible and every inclusion-maximal packing in the entire *matching-deficient* bipartite family and locates the two-deletion maximality threshold; no cited theorem supplies those enumerators or the lower maximality behavior as a stated consequence.

## Limitations

The domain requires both bipartition sides to have at least three vertices and the deleted edges to be pairwise vertex-disjoint. The formulas are not asserted for arbitrary deleted edge sets or multipartite graphs with three or more parts. The literature comparison concerns accessible published texts and indexed records; it cannot exclude all unpublished, unindexed, or differently named equivalent results. No independent audit has been performed.

## References

1. G. Chelladurai, K. Kalimuthu, and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, DOI: 10.1051/ro/2022171.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750 (first posted 2024-03-01), subsequently Theoretical Computer Science (2024), DOI: 10.1016/j.tcs.2024.114884.
3. A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935 (2025).
