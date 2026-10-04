# Coefficientwise extremals for visibility polynomials of complete multipartite graphs
## Finding
Fix \(N\ge3\), and order the visibility polynomials of connected noncomplete complete multipartite graphs on \(N\) vertices coefficientwise. The coefficientwise maximum exists and equals \((1+x)^N-x^N\); it is attained exactly by the complete multipartite graphs whose part sizes are all at most \(2\). A coefficientwise minimum exists exactly for \(3\le N\le5\), where it is uniquely attained by the star \(K_{1,N-1}\), whose visibility polynomial is \((1+x)^{N-1}+x+(N-1)x^2\). For every \(N\ge6\) there is no coefficientwise minimum. More precisely, the star uniquely minimizes the cubic coefficient, with \(r_3(K_{1,N-1})=\binom{N-1}{3}\), whereas every other graph in the class has \(r_3=\binom N3\); but \(r_{N-1}(K_{1,N-1})=1\) while \(r_{N-1}(K_{3,N-3})=0\).

## Assumptions and scope
Let \(G=K_{n_1,\ldots,n_r}\) be a connected noncomplete complete multipartite graph on
\(N=\sum_i n_i\ge3\) vertices, with partite classes \(X_1,\ldots,X_r\).
A set \(S\subseteq V(G)\) is a mutual-visibility set when every pair of vertices in \(S\)
admits a shortest path whose internal vertices avoid \(S\). Write
\[
\mathcal V(G;x)=\sum_{k=0}^N r_k(G)x^k
\]
for the visibility polynomial. For two graphs of the same order, write \(G\preceq H\) when
\(r_k(G)\le r_k(H)\) for every \(k\).

The graph class considered in the extremal statement excludes the complete graph. Complete graphs trivially have
\(\mathcal V(K_N;x)=(1+x)^N\).

## Proof
Vertices in distinct parts are adjacent. Two vertices in the same part \(X_i\) have distance two, and their internal
geodesic vertex may be chosen arbitrarily outside \(X_i\). Hence a set \(S\) is mutual-visible exactly when, for every
part containing at least two selected vertices, at least one vertex outside that part is unselected.

This gives a convenient complement count. Let \(T=V(G)\setminus S\) have size \(t\ge1\). Then \(S\) fails to be
mutual-visible exactly when \(T\) is contained in one part \(X_i\) and at least two vertices of \(X_i\) remain selected.
Because \(T\ne\varnothing\), it can be contained in at most one part. Therefore
\[
r_{N-t}(G)=\binom Nt-\sum_{i:\,n_i\ge t+2}\binom{n_i}t,
\qquad 1\le t\le N-1,
\]
while \(r_N(G)=0\) because \(G\) is noncomplete. Equivalently,
\[
\mathcal V(G;x)
=(1+x)^N-
\sum_{i:\,n_i\ge2}x^{N-n_i}
\big((1+x)^{n_i}-1-n_i x\big)
+(p-1)x^N,
\]
where \(p\) is the number of non-singleton parts.

For the maximum, if every part has size at most two, a proper vertex subset can never contain all vertices outside a
part together with two selected vertices inside that part. Hence every proper subset is mutual-visible and
\[
\mathcal V(G;x)=(1+x)^N-x^N.
\]
Conversely, if some part has size at least three, selecting all vertices outside it together with any two vertices inside it
gives a proper non-visible set. Thus the coefficientwise maximum is exactly as stated, and its maximizers are precisely
the multipartite graphs with all part sizes at most two.

For the lower extremum, consider \(r_3\). A non-visible three-set must contain every vertex outside one part and at
least two vertices in that part. Since the graph is connected, there is at least one outside vertex. Thus this can happen
only when one part has size \(N-1\), that is, only for the star \(K_{1,N-1}\). The number of bad three-sets is then
\(\binom{N-1}2\), so
\[
r_3(K_{1,N-1})
=\binom N3-\binom{N-1}2
=\binom{N-1}3.
\]
Every other graph in the class has \(r_3=\binom N3\). Hence any coefficientwise minimum, if one exists, must be the star.

The complement formula with \(t=1\) gives
\[
r_{N-1}(G)=\sum_{i:\,n_i\le2}n_i.
\]
The star has \(r_{N-1}=1\). If \(N\ge6\), the graph \(K_{3,N-3}\) has no part of size at most two, so its
\((N-1)\)-st coefficient is zero. It follows that the star does not dominate this graph coefficientwise, while no other
graph can be a coefficientwise minimum because the star uniquely minimizes \(r_3\). Therefore no coefficientwise
minimum exists for \(N\ge6\).

For \(N=3\), the star is the only noncomplete connected complete multipartite graph. For \(N=4\), the only coefficient
above degree two and below the zero top coefficient is \(r_3\), which the star uniquely minimizes. For \(N=5\), the
star uniquely minimizes \(r_3\), and its value \(r_4=1\) is smaller than that of every nonstar partition: a nonstar with
a part of size three has two vertices in parts of size at most two, while a graph with all parts of size at most two has
\(r_4=5\). Hence the star is the unique coefficientwise minimum exactly for \(3\le N\le5\).

## Verification
The included checker tests the mutual-visibility definition directly, rather than using the counting lemma. It constructs each
complete multipartite graph, computes graph distances, and for every selected pair deletes the other selected vertices and
checks whether the original shortest distance is preserved. It exhausts all complete multipartite isomorphism types through
order ten and compares every coefficient with the formula. It separately checks the coefficientwise extremal classification
over all integer part-size partitions through order thirty.

## Relationship to prior work
The foundational mutual-visibility paper determines the maximum mutual-visibility number for complete bipartite graphs and
gives broader results for cographs. Later work on visibility polynomials gives an explicit polynomial for complete bipartite
graphs and a general join formula. Those results supply prior coverage of the bipartite special case and enough machinery to
derive complete-multipartite coefficient formulas recursively; the coefficient formula above is therefore used as proof
machinery, not claimed as the originality of this finding.

A 2026 game-theoretic paper treats complete multipartite graphs directly and gives the mutual-visibility number
\(N\), \(N-1\), or \(N-2\) according to the part sizes, together with structural information about maximal sets.
That optimization information does not determine coefficientwise extrema of the entire visibility polynomial across all
multipartite partitions. A separate 2026 visibility-polynomial paper gives formulas for wheels, friendship graphs, shell
graphs, and bow graphs, not complete multipartite coefficientwise comparisons.

The new assertion here is the extremal order theorem: the exact coefficientwise maximum class, the sharp existence threshold
\(N=6\) for failure of a coefficientwise minimum, and the incompatible cubic and near-top extremizers that force that failure.

## Limitations
The coefficientwise order is taken only within connected noncomplete complete multipartite graphs of a fixed order.
The result does not claim an extremal theorem among all connected graphs. The complete-multipartite coefficient formula is
compatible with and partly derivable from published join results, so only the cross-partition extremal classification is
asserted as the new contribution. The exhaustive computation through order thirty for partition extremals and through order
ten at definition level is corroborative; the all-orders theorem follows from the proof.

## References
1. G. Di Stefano, “Mutual Visibility in Graphs,” Applied Mathematics and Computation 419 (2022), 126850,
   DOI 10.1016/j.amc.2021.126850; first public preprint arXiv:2105.02722v1, 6 May 2021.
2. K. B. Tonny, M. Shikhi, “On the Visibility Polynomial of Graphs,” arXiv:2507.01851v2.
3. V. Iršič Chenoweth, S. Klavžar, G. Rus, E. Tan, J. Tian, “Builder-Blocker Mutual-Visibility Game,”
   Bulletin of the Malaysian Mathematical Sciences Society 49 (2026), article 89, DOI 10.1007/s40840-026-02083-9.
4. K. B. Tonny, M. Shikhi, “Visibility Polynomial of Some Graph Classes,” Advances and Applications in Discrete Mathematics
   43(2) (2026), 213–225, DOI 10.17654/0974165826015.
