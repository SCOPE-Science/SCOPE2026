# Maximal outer-mutual-visibility sets of rectangular rook graphs: complete enumerator

## Finding

Let \(m,n\ge 2\) be integers, \(R_{m,n}=K_m\square K_n\), and define \(M_{m,n}(z)=\sum_X z^{|X|}\), with the sum over all **inclusion-maximal outer-mutual-visibility** vertex sets \(X\subseteq V(R_{m,n})\). The following classification and complete enumerator hold.

Associate a rook-cell set \(X\) with the bipartite selected-edge graph \(F_X\subseteq K_{m,n}\), on all \(m\) labeled row vertices and \(n\) labeled column vertices. Then \(X\) is inclusion-maximal outer-mutual-visible if and only if \(F_X\) is a star forest of exactly one of these three disjoint kinds:

1. Every row and every column is nonisolated.
2. At least one row is isolated, no column is isolated, every nonisolated row has degree at least two, and every column has degree one.
3. At least one column is isolated, no row is isolated, every nonisolated column has degree at least two, and every row has degree one.

Let \(S_{\ge 2}(p,k)\) count partitions of a \(p\)-element labeled set into \(k\) unlabeled blocks each of size at least two; let \((r)_k=r!/(r-k)!\) and interpret empty sums as zero. Define \(A_{m,n}(z)\) by
\[
\sum_{m,n\ge0}A_{m,n}(z)\frac{u^mv^n}{m!n!}
=\exp\left(uvz+u(e^{vz}-1-vz)+v(e^{uz}-1-uz)\right).
\]
Then for all \(m,n\ge2\),
\[
\boxed{M_{m,n}(z)=A_{m,n}(z)
+z^n\sum_{s=1}^{\min\{m-1,\lfloor n/2\rfloor\}}(m)_s S_{\ge2}(n,s)
+z^m\sum_{t=1}^{\min\{n-1,\lfloor m/2\rfloor\}}(n)_t S_{\ge2}(m,t).}
\]
In particular, the smallest cardinality of a maximal set is \(\min\{m,n\}\), and its **number** \(N_{m,n}=[z^{\min\{m,n\}}]M_{m,n}(z)\) is, with \(p=\min\{m,n\}\) and \(q=\max\{m,n\}\),
\[
\boxed{N_{m,n}=\begin{cases}
\displaystyle\sum_{k=1}^{\lfloor p/2\rfloor}(q)_k S_{\ge2}(p,k),&p<q,\\[3pt]
\displaystyle p!+2\sum_{k=1}^{\lfloor p/2\rfloor}(p)_k S_{\ge2}(p,k),&p=q.
\end{cases}}
\]
For every \(n\ge2\), \(M_{2,n}(z)=nz^2+2^nz^n\), giving maximal-set coefficient gaps of arbitrarily large length.

## Assumptions and scope

All graphs are simple, undirected and finite. The rook cells are \((i,j)\) with \(1\le i\le m\), \(1\le j\le n\), adjacent when their row or column indices agree. Two vertices \(x,y\) are \(X\)-visible when they admit a shortest path whose internal vertices avoid \(X\). An outer-mutual-visibility set \(X\) makes every pair \(x,y\) with at least one endpoint in \(X\) visible. Inclusion-maximal means no proper superset of \(X\) satisfies this property; it does **not** mean largest cardinality. A star forest has connected components that are stars (including single edges) or isolated vertices. The coefficient \(A_{m,n}(z)\) is the enumerator of star forests in \(K_{m,n}\) having no isolated vertices, with each selected edge weighted by \(z\); it is *not* the all-star-forest enumerator.

## Proof

**Visibility translation.** Nonadjacent rook cells \((i,j)\) and \((k,\ell)\), with \(i\ne k\), \(j\ne\ell\), have exactly two length-two geodesics, with internal cells \((i,\ell)\) and \((k,j)\). Thus \((i,j)\in X\) fails to see \((k,\ell)\) precisely when both cross cells belong to \(X\). The selected edges \((i,j),(i,\ell),(k,j)\) then form a three-edge path on four distinct vertices in \(F_X\). Conversely, every selected three-edge path supplies such a witness. So \(X\) is outer-mutual-visible exactly when \(F_X\) has no (not necessarily induced) three-edge path. A bipartite graph has no three-edge path if and only if each nontrivial component is a star: any connected nonstar contains such a path (a cycle does too). Hence the admissible sets are exactly star forests.

**Maximality translation.** Adding an edge between distinct nontrivial star components creates a three-edge path: take an existing edge incident to each endpoint and place the new edge in the middle. A star component contains every possible cross-part edge between its own vertices. Consequently any star forest with no isolated vertex is maximal, giving family 1. If both parts have an isolated vertex, the edge joining those two isolates can be added, so the forest is not maximal.

Suppose some row is isolated and no column is isolated. For any column of degree at least two, its component is a column-centered star and it can absorb an isolated row without forming a path of three edges; for any column of degree one attached to a row of degree one, its isolated-edge component can likewise absorb an isolated row. Therefore maximality forces each column to have degree exactly one and its unique row neighbor to have degree at least two. Conversely, if these degree constraints hold, adding an edge from an isolated row to any column creates a three-edge path using the other selected column at the latter column's existing row; any other absent edge joins nontrivial components, so also creates a path. This proves family 2. The argument with rows and columns exchanged proves family 3. The families are disjoint because family 1 has no isolates, family 2 has row isolates, and family 3 has column isolates.

**Counting.** A star-forest component without isolates in a bipartite labeled graph is one edge (weight \(uvz\)), one row-center with \(b\ge2\) column leaves (weight \(uv^bz^b/b!\)), or one column-center with \(a\ge2\) row leaves (weight \(vu^az^a/a!\)). The labeled exponential formula gives the stated generating function for \(A_{m,n}\). In family 2, choose \(s\) active labeled rows and partition the \(n\) labeled columns into \(s\) blocks, of at least two leaves each, assigning one block to each row. There are \((m)_s S_{\ge2}(n,s)\) choices, with exactly \(n\) edges, and \(1\le s\le m-1\). The corresponding bound \(s\le\lfloor n/2\rfloor\) is automatic. Interchanging the parts counts family 3. The disjoint union establishes the complete polynomial formula.

For explicit coefficient computation one may instead use \(A_{0,0}=1\), \(A_{m,0}=A_{0,n}=0\) for \(m+n>0\), and, for \(m,n\ge1\),
\[
A_{m,n}(z)=\sum_{b=1}^{n}\binom nb z^b A_{m-1,n-b}(z)
+n\sum_{a=2}^{m}\binom{m-1}{a-1}z^a A_{m-a,n-1}(z).
\]
Indeed the component containing the distinguished first row is either row-centered with \(b\ge1\) columns (including a single edge) or a leaf of a column-centered star with \(a\ge2\) rows. This recurrence is finite and exact.

**Minimum-set multiplicities.** Every forest in family 1 meets all rows and all columns, so it has at least \(\max\{m,n\}\) edges. Family 2 always has exactly \(n\) edges; family 3 always has exactly \(m\). For \(m<n\), the \(m\)-edge minimum sets occur precisely in family 3, giving the first expression. For \(m=n=p\), the \(p\)-edge members of family 1 are exactly perfect matchings, numbering \(p!\), and families 2 and 3 contribute equal Stirling sums. This proves the second expression. For \(m=2\), the no-isolate configurations plus the row-isolate configurations give \(2^n\) maximal sets of size \(n\); the column-isolate configurations give \(n\) maximal sets of size two. The formulas include \(n=2\), where these coefficients combine.

## Verification

The accompanying standalone Python verifier uses an independent pairwise geodesic predicate, component-based star-forest recognition, direct single-cell maximality testing, and the exact Stirling/forest recurrences. It exhaustively compared all \(108688\) initial vertex subsets of the boards \((2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,3),(4,4),(2,5),(3,5)\). Each check agreed across the predicates, structural classification, exact coefficient counts, and minimum-set counts. An additional \(121\) parameter pairs through \(12\times12\) checked polynomial symmetry and the minimum-set formula. Run `python3 verify.py` with Python 3 standard library from the extracted artifact directory. These finite checks do not replace the all-parameter proof.

## Relationship to prior work

Cicerone, Di Stefano, Klavžar and Yero (arXiv:2401.02373, first posted January 4, 2024), Theorem 2.1(ii), obtained the **largest** outer mutual-visibility cardinality \(m+n-2\) for rook graphs with both factors of order at least three. Welton, Khudairi and Tuite, *Lower general position in Cartesian products*, Theorem 2, obtained the **smallest maximal** general-position cardinality \(\min\{m,n\}\), but did not count these sets. Since general-position and outer-mutual-visibility sets coincide for rook graphs, their scalar theorem also gives the scalar minimum here; it is not claimed as new. Carraher and coauthors' treatment of \(P_4\)-saturation games on complete bipartite graphs also provides older structural and extremal context, without the present complete size-profile enumeration. A previously obtained complete **all-admissible-set** polynomial for rook-graph general position uses the same star-forest equivalence; that result is not a maximal-set polynomial and does not imply this maximal-set profile simply by comparing its coefficients. Bujtás, Klavžar and Tian (2025), Proposition 3.5, motivated studying maximal visibility sets as generators of visibility polynomials by inclusion-exclusion. The contribution here is restricted to the exhaustive classification and enumeration of inclusion-maximal sets, their exact minimum-size multiplicities, and their arbitrarily large coefficient gaps.

## Limitations

This is an all-integers proof for \(m,n\ge2\), not a claim about higher-dimensional Hamming graphs or arbitrary Cartesian products. Neither the prior maximum cardinality \(m+n-2\) nor the prior lower cardinality \(\min\{m,n\}\) is asserted original. The formula counts inclusion-wise maximal sets, not all outer-mutual-visibility sets. External literature searching cannot rule out an unindexed or differently named saturation-profile enumeration; older structural saturation work leaves some overlap risk. No independent scientific audit has been performed.

## References

1. S. Cicerone, G. Di Stefano, S. Klavžar, I. G. Yero, *Mutual-visibility problems on graphs of diameter two*, arXiv:2401.02373 (version 1, 2024-01-04), Section 2, Theorem 2.1. https://arxiv.org/html/2401.02373v1
2. E. Kruft Welton, S. Khudairi, J. Tuite, *Lower general position in Cartesian products*, Communications in Combinatorics and Optimization 10 (2025), 110–125, Theorem 2; first public preprint in December 2023. https://oro.open.ac.uk/98050/9/98050final.pdf
3. J. Carraher et al., *The Game Saturation Number of a Graph*, Section 3, \(P_4\)-saturation on complete bipartite graphs. https://dwest.web.illinois.edu/pubs/gamesat.pdf
4. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, Aequationes Mathematicae (2025), Proposition 3.5. https://doi.org/10.1007/s00010-025-01197-y
