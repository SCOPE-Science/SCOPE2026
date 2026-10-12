# All open-locating-dominating sets of crown graphs
## Finding
For every integer \(n\ge3\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\}
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). A set \(S\subseteq V(\operatorname{Cr}_n)\) is an open-neighborhood locating-dominating set (OLD-set) if every \(N(v)\cap S\) is nonempty and these sets are pairwise distinct as \(v\) ranges over all vertices.

Then \(S\) is an OLD-set if and only if
\[
|S\cap A|\ge n-1\qquad\text{and}\qquad |S\cap B|\ge n-1.
\]
Consequently, for the cardinality enumerator
\[
\mathcal O_n(z)=\sum_{S\text{ an OLD-set}} z^{|S|},
\]
one has
\[
\mathcal O_n(z)=\bigl(z^n+n z^{n-1}\bigr)^2=z^{2n-2}(n+z)^2.
\]
In particular,
\[
\operatorname{OLD}(\operatorname{Cr}_n)=2n-2,
\]
and the minimum OLD-sets are exactly
\[
V(\operatorname{Cr}_n)\setminus\{a_i,b_j\},\qquad 1\le i,j\le n.
\]
Thus there are exactly \(n^2\) minimum OLD-sets and \((n+1)^2\) OLD-sets in total.

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem is for \(n\ge3\). The case \(n=2\) is excluded: \(\operatorname{Cr}_2\) is two disjoint edges, and the sidewise criterion above is not sufficient for open domination.

For \(S\subseteq V(\operatorname{Cr}_n)\), write \(S_A=S\cap A\) and \(S_B=S\cap B\). By construction,
\[
N(a_i)=B\setminus\{b_i\},\qquad N(b_i)=A\setminus\{a_i\}.
\]
No probabilistic or asymptotic assumptions are used.

## Proof
For necessity, take distinct indices \(i\ne j\). Their open-neighborhood signatures on the \(A\)-side are
\[
N(a_i)\cap S=S_B\setminus\{b_i\},\qquad
N(a_j)\cap S=S_B\setminus\{b_j\}.
\]
If both \(b_i\) and \(b_j\) were absent from \(S\), these two signatures would be equal. Since an OLD-set must distinguish every pair of vertices, at most one vertex of \(B\) can be omitted. Hence \(|S_B|\ge n-1\). Interchanging the two sides gives \(|S_A|\ge n-1\).

Conversely, suppose \(|S_A|\ge n-1\) and \(|S_B|\ge n-1\). Since \(n\ge3\), both \(S_A\) and \(S_B\) contain at least two vertices. Thus every \(a_i\) has a neighbor in \(S_B\), and every \(b_i\) has a neighbor in \(S_A\); all signatures are nonempty.

For distinct \(a_i,a_j\), at most one of \(b_i,b_j\) is omitted. If \(b_i\in S\), then \(b_i\notin N(a_i)\cap S\) but \(b_i\in N(a_j)\cap S\); if instead only \(b_j\) is known to be selected, the symmetric argument applies. Hence all \(A\)-vertices have distinct signatures. The same argument distinguishes all \(B\)-vertices. Finally, every signature of an \(A\)-vertex is a nonempty subset of \(B\), whereas every signature of a \(B\)-vertex is a nonempty subset of \(A\). Since \(A\) and \(B\) are disjoint, no cross-side signatures can be equal. Therefore \(S\) is an OLD-set.

The enumeration now factors by sides. On either side an OLD-set may select all \(n\) vertices, contributing \(z^n\), or omit exactly one of the \(n\) vertices, contributing \(n z^{n-1}\). The two choices are independent, so
\[
\mathcal O_n(z)=\bigl(z^n+n z^{n-1}\bigr)^2.
\]
The smallest exponent is \(2n-2\), attained precisely by omitting one vertex from each side. This gives \(n^2\) minimum sets.

## Verification
The proof above is symbolic and covers every \(n\ge3\). As a finite stress test, `verify_old_crown.py` independently constructs \(\operatorname{Cr}_n\), checks the OLD definition directly for every subset for \(3\le n\le8\), compares every result with the sidewise criterion, and checks the three nonzero enumerator coefficients. Its packaged replay output is:

`VERIFY_OK n_range=3..8 subsets=87360 old_sets=271 minimum_sets=199 max_order=16`

This exhaustive computation is only a boundary and implementation check; it is not used as a proof for arbitrary \(n\).

## Relationship to prior work
Seo and Slater introduced the OLD-set problem and defined the same open-neighborhood signatures used here. Their 2010 paper treats general existence, complexity, paths, trees, and infinite grids; full-text inspection found no crown graph or complete-bipartite-minus-matching result. Chellali, Jafari Rad, Seo, and Slater later characterized several extremal OLD regimes and proved bounds under conditions including \(C_4\)-freeness; those statements do not yield the crown formula. In particular, crowns with \(n\ge4\) contain \(4\)-cycles, while \(\operatorname{Cr}_3\cong C_6\) is not one of their \(C_4\)-free equality graphs.

Kincaid, Oldham, and Yu study OLD-sets on the infinite triangular grid; their first public arXiv version on 2014-03-27 supplies an exact archive-era public anchor for this parameter and is classified under MSC 05C69. Pandey's 2015 algorithmic work treats bipartite graphs broadly and gives a polynomial-time result for chain graphs. Crowns with \(n\ge3\) are not chain graphs because the neighborhoods \(B\setminus\{b_i\}\) are pairwise incomparable under inclusion. Henning and Yeo's identifying-open-code result concerns cubic graphs, so it applies as a general bound only at the isolated crown \(\operatorname{Cr}_4\), not to the family classification or enumerator.

The terminology “identifying open code” and, more recently, “open-separating total-dominating code” is equivalent to the OLD condition used here. Targeted searches under those aliases found no statement implying the sidewise criterion or the enumerator above.

## Limitations
The theorem concerns ordinary OLD-sets only; it does not address fault-tolerant variants, weighted variants, directed graphs, or noisy detectors. The exhaustive computation stops at \(n=8\); the infinite claim rests on the proof, not on enumeration.

The scalar value at the boundary \(n=3\), where \(\operatorname{Cr}_3\cong C_6\), may be recoverable from cycle-specific results. The claimed contribution is the uniform if-and-only-if characterization for the crown family together with the complete cardinality enumerator and minimizer count.

The 2010 introductory paper predates the exact archive anchor used in metadata, but accessible evidence located during this review gave only month/year for its public appearance. No day was invented; the metadata date uses the exact first-public arXiv date of an inspected archive-era OLD-set source.

## References
1. S. J. Seo and P. J. Slater, “Open neighborhood locating-dominating sets,” *Australasian Journal of Combinatorics* 46 (2010), 109–119.
2. R. Kincaid, A. Oldham, and G. Yu, “Optimal open-locating-dominating sets in infinite triangular grids,” arXiv:1403.7061, first version 2014-03-27; later *Discrete Applied Mathematics* 193 (2015), 139–144.
3. M. Chellali, N. Jafari Rad, S. J. Seo, and P. J. Slater, “On open neighborhood locating-dominating in graphs,” *Electronic Journal of Graph Theory and Applications* 2(2) (2014), 87–98, DOI 10.5614/EJGTA.2014.2.2.1.
4. M. A. Henning and A. Yeo, “Distinguishing-Transversal in Hypergraphs and Identifying Open Codes in Cubic Graphs,” *Graphs and Combinatorics* 30 (2014), 909–932, DOI 10.1007/s00373-013-1311-2.
5. A. Pandey, “Open Neighborhood Locating-Dominating Set in Graphs: Complexity and Algorithms,” *2015 International Conference on Information Technology*, 1–6, DOI 10.1109/ICIT.2015.14.
