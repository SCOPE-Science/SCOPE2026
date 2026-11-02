# Complete domination polynomials of two-subset Kneser graphs

## Finding

Let \(K(n,2)\) have as vertices the unordered two-element subsets of \([n]\), with adjacency when the two subsets are disjoint. Put \(N=\binom n2\), and let
\[
D_n(z)=\sum_{k=0}^{N}d_{n,k}z^k
\]
count the dominating vertex sets by cardinality. For \(n\ge5\), define
\[
U_{n,k}=\binom n2\binom{2n-4}{k}
+n\left[\binom{n-1}{k}-\binom n2\binom{n-2}{k}
+\binom{n-1}{2}\binom{n-3}{k}-\mathbf1_{\{k=n-1\}}\right].
\]
Then, for every \(n\ge5\) and \(0\le k\le N\),
\[
\boxed{
d_{n,k}=\begin{cases}
0,&0\le k\le2,\\
\binom n3+15\binom n6,&k=3,\\
\binom Nk-U_{n,k}+3\binom n4\mathbf1_{\{k=4\}},&4\le k\le N.
\end{cases}}
\]
The exceptional boundary graph is \(K(4,2)=3K_2\), for which \(D_4(z)=(2z+z^2)^3\).

The coefficient \(d_{n,3}\) enumerates minimum dominating sets, whose two forms (three pairwise disjoint edges or three edges of a triangle) and minimum cardinality \(3\) are not claimed as novel. The complete higher-degree distribution and its four-edge overlap correction are the principal finding.

For \(n\ge5\), every vertex subset of cardinality at least \(2n-3\) dominates, whereas exactly \(\binom n2\) vertex subsets of cardinality \(2n-4\) do not dominate. Thus \(2n-3\) is the sharp universal cardinality threshold.

## Assumptions and scope

All graphs are finite and simple. A dominating set \(S\) contains or has a neighbor of every vertex. Binomial coefficients \(\binom ab\) are zero for \(b<0\) or \(b>a\), and \(\mathbf1_{\{P\}}\) is one when condition \(P\) holds and zero otherwise. The theorem treats every order \(n\ge4\), and all cardinalities. The graph \(K(5,2)\) is the Petersen graph, whose full domination polynomial was previously published and is recovered rather than first established here.

## Proof

### Failure witnesses

Identify a vertex of \(K(n,2)\) with an edge of the complete graph on \([n]\). For each pair \(e\), define
\[
F_e=\{f\in\tbinom{[n]}2:f\cap e\ne\varnothing,\ f\ne e\}.
\]
The set \(F_e\) has exactly \(2n-4\) members. A selected vertex set \(S\) fails to dominate \(K(n,2)\) precisely when \(S\subseteq F_e\) for at least one pair \(e\). Indeed, this says that \(e\notin S\) and no selected pair is disjoint from \(e\), exactly the failure of domination at \(e\).

### Intersections of witness families

If two distinct witnesses \(e,f\) have a common endpoint, then \(|F_e\cap F_f|=n-2\): there are \(n-3\) other spokes at the common endpoint and one cross-edge between the remaining endpoints. If \(e,f\) are disjoint, then \(F_e\cap F_f\) consists of the four cross-edges of a \(K_{2,2}\). No other witness \(g\) has all four cross-edges in \(F_g\), since the only two-vertex covers of this \(K_{2,2}\) are its two bipartition classes \(e,f\).

Consider three or more witnesses whose intersection contains at least four edges. They must be pairwise intersecting; otherwise a disjoint pair forces at most four common edges, and no third witness contains those four. Every pairwise-intersecting family of at least three distinct edges of a simple graph either has one common endpoint or is exactly a triangle. The triangle case gives an empty common \(F\)-intersection: a two-element set meeting all three triangle edges must itself be a triangle edge, and that edge is excluded from its corresponding \(F_e\). Thus the only possible higher witness intersections come from stars.

For a star of \(j\ge3\) witnesses about one endpoint, the common \(F\)-intersection consists exactly of the \(n-1-j\) remaining edges at that endpoint. There are \(n\binom{n-1}{j}\) such star families. The corresponding two-witness stars are counted separately because their intersection has size \(n-2\), not \(n-3\). The number of unordered disjoint witness pairs is \(3\binom n4\).

### Inclusion-exclusion for cardinality at least four

For \(k\ge4\), inclusion-exclusion gives the number \(b_{n,k}\) of non-dominating \(k\)-sets as
\[
\begin{aligned}
b_{n,k}={}&\binom n2\binom{2n-4}{k}
-n\binom{n-1}{2}\binom{n-2}{k}
-3\binom n4\mathbf1_{\{k=4\}}\\
&+n\sum_{j=3}^{n-1}(-1)^{j+1}\binom{n-1}{j}
\binom{n-1-j}{k}.
\end{aligned}
\]
The sum is simplified by extracting the coefficient of \(z^k\) in
\[
\sum_{j=0}^{n-1}(-1)^j\binom{n-1}{j}(1+z)^{n-1-j}=z^{n-1}.
\]
Separating the terms with \(j=0,1,2\) yields exactly
\[
b_{n,k}=U_{n,k}-3\binom n4\mathbf1_{\{k=4\}}.
\]
There are \(\binom Nk\) possible selected \(k\)-sets, so \(d_{n,k}=\binom Nk-b_{n,k}\), proving the higher-degree formula. The isolated \(3\binom n4\) correction accounts for four selected cross-edges simultaneously witnessing the failure of domination at two disjoint pairs. It is not covered by the intersecting-witness star calculation.

### Cardinalities below four and the boundary graph

No set of size at most two dominates when \(n\ge5\): for two selected edges that meet, choose an unselected edge through their common endpoint; for two disjoint selected edges, choose a cross-edge meeting both. A singleton is a subset of a non-dominating two-set.

For three selected edges, interpret them as a three-edge simple graph on \([n]\). Up to isolated vertices, its possible shapes are a triangle, a three-edge matching, a three-edge star, a four-vertex path, and a two-edge path together with an isolated edge. Three pairwise disjoint edges dominate, since no two-element witness can meet all three. A triangle dominates, since its only two-element vertex covers are its three already selected edges. The other shapes do not dominate: the star has an unused incident edge when \(n\ge5\); a path has an unselected two-vertex cover; and a two-edge path plus a detached edge has a cover pairing the shared vertex with one endpoint of the detached edge. Therefore the successful triples are exactly \(\binom n3\) triangles and \(15\binom n6\) three-edge matchings. Finally, \(K(4,2)\) is three disjoint ordinary edges, each of which must contribute at least one selected endpoint, giving \((2z+z^2)^3\).

### Universal threshold

Every non-dominating set is contained in some \(F_e\) of size \(2n-4\). For \(n\ge5\), these \(\binom n2\) sets are distinct: choose a pair meeting \(e\) but not \(f\) when the witnesses differ, or use the explicit intersection sizes above, both strictly smaller than \(2n-4\). Thus the largest non-dominating sets have size \(2n-4\), and there are exactly \(\binom n2\) of them. This proves the sharp threshold.

## Verification

The self-contained standard-library program `verification/verify.py` reconstructs the graph from pairwise disjointness. It counts all dominating selected sets via closed-neighborhood bitmasks without employing the failure-witness formula. It exhaustively examines \(2^{\binom n2}\) subsets for \(n=4,5,6,7\), then separately checks the coefficients of sizes \(3,4,5\) for \(n=8,9,10\), and checks the threshold identities for \(5\le n<50\). The actual executed program reported `VERIFY_OK`, covering 2,131,008 exhaustive masks and 1,950,012 restricted-cardinality candidates. These are corroborating finite calculations, not the proof of the infinite theorem.

For illustration, the calculated coefficients from degree three upward are:

- \(D_5(z)=10z^3+75z^4+192z^5+200z^6+120z^7+45z^8+10z^9+z^{10}\), the known Petersen polynomial.
- \(D_6(z)\) begins \(35z^3+420z^4+2163z^5+4585z^6+6315z^7\).
- \(D_7(z)\) begins \(140z^3+2205z^4+15162z^5+49854z^6\).

## Relationship to prior work

Cornet and Torres (arXiv:2308.15603, first public version 2023-08-29) prove structural incidence criteria for \(k\)-tuple dominating sets of two-subset Kneser graphs and study minimum cardinalities. Their Lemma 18 implies a test for ordinary domination on specializing \(k=1\), but their results do not present a complete cardinality polynomial or the explicit intersections and four-edge correction above. Brešar, Cornet, Dravec, and Henning (arXiv:2312.15464, 2023-12-24) study scalar \(k\)-domination, total domination, and packing parameters, not this distribution. Akbari, Alikhani, and Peng (arXiv:0905.3281, 2009-05-20) explicitly calculate the Petersen graph domination polynomial; our \(n=5\) case is a known special case, not a new result. Scalar domination number three for all \(n\ge4\) is also known. This result claims the uniform all-order polynomial enumeration for \(n\ge6\) and its structural correction, not those preexisting special cases.

## Limitations

The theorem is specific to two-element Kneser graphs; no corresponding formula is proved for general \(K(n,r)\) with \(r\ge3\). The brute-force computations cover only stated finite orders. A search of indexed literature and accessible research records cannot certify worldwide publication priority; unindexed or differently formulated enumerations remain a residual originality risk. No independent mathematical audit has been performed.

## References

1. M. G. Cornet and P. Torres, *k-tuple domination on Kneser graphs*, arXiv:2308.15603 (first posted 2023-08-29), https://arxiv.org/abs/2308.15603.
2. B. Brešar, M. G. Cornet, T. Dravec and M. A. Henning, *k-Domination invariants on Kneser graphs*, arXiv:2312.15464 (first posted 2023-12-24), https://arxiv.org/abs/2312.15464.
3. S. Akbari, S. Alikhani and Y.-H. Peng, *The Domination Polynomials of Cubic Graphs of Order 10*, arXiv:0905.3281 (first posted 2009-05-20), https://arxiv.org/abs/0905.3281.
