# A width-four transition in minimum super domination of rook graphs

## Finding

Let \(2\le p\le q\) be integers and let \(R_{p,q}=K_p\square K_q\), with labeled vertex set \([p]\times[q]\). Two distinct cells are adjacent when they share a row or a column. A super dominating set is a subset \(D\) such that, for each \(t\notin D\), some \(d\in D\) has \(N(d)\cap(V\setminus D)=\{t\}\). Write \(N_{\mathrm{sp}}(R_{p,q})\) for the number of super dominating sets of minimum size.

Then
\[
N_{\mathrm{sp}}(R_{p,q})=\begin{cases}
4,&p=q=2,\\
2,&p=2<q,\\
42,&p=q=3,\\
3\cdot2^q-3,&p=3<q,\\
608,&p=q=4,\\
4\cdot3^q-6\cdot2^q+4+12q(q-1),&p=4<q,\\
pq(p-1)(q-1),&5\le p\le q.
\end{cases}
\]

Every minimum super dominating set is the complement of exactly one of the following explicitly classified selected-cell configurations, with the listed regimes determining which types occur. Let \(h=\max\{q,p+q-4\}\), the largest possible size of the complement.

1. **Column transversal:** exactly one cell in each column, with at least one empty row; this is optimal whenever \(h=q\).
2. **Row transversal:** exactly one cell in each row, with at least one empty column; this is optimal precisely when \(p=q\le4\).
3. **Crossed stars:** for \(p,q\ge4\), choose distinct rows \(r,r_0\) and distinct columns \(c,c_0\), and take
\[
T=\bigl(\{r\}\times([q]\setminus\{c,c_0\})\bigr)
\cup\bigl(([p]\setminus\{r,r_0\})\times\{c\}\bigr).
\]
This is optimal whenever \(h=p+q-4\), namely for \(p\ge4\).

The known minimum cardinality is \(\gamma_{\mathrm{sp}}(R_{p,q})=pq-h\); that numerical formula is not asserted to be new. The new results here are the full optimizer classification and its exact enumeration.

For fixed width \(p=3\) or \(p=4\), the count grows exponentially in \(q\), with respective leading terms \(3\cdot2^q\) and \(4\cdot3^q\). For every fixed \(p\ge5\), it is instead the quadratic polynomial \(p(p-1)q(q-1)\). Thus the transition between widths four and five is an exact change in optimizer growth type.

## Assumptions and scope

All graphs are finite, simple and undirected. Cells, rows and columns are labeled; no quotient by graph automorphisms is taken. Both dimensions satisfy \(2\le p\le q\). The complement of a super dominating set is denoted \(T\). In the incidence bipartite graph with row vertices and column vertices, \(T\) is regarded as its set of edges. The degree of row \(i\) in this incidence graph is \(r_i\), and that of column \(j\) is \(c_j\). Put \(z_r=|\{i:r_i=0\}|\) and \(z_c=|\{j:c_j=0\}|\).

## Proof

**Private-neighbor criterion.** For any \((i,j)\in T\), a witnessing vertex \(d\in V\setminus T\) is in row \(i\) or column \(j\). If \(d=(i,k)\), the number of its neighbors in \(T\) is \(r_i+c_k\) (because \(d\notin T\)). This equals one exactly when \(r_i=1\) and \(c_k=0\). If \(d=(\ell,j)\), the corresponding count is \(r_\ell+c_j\), and it equals one exactly when \(r_\ell=0\) and \(c_j=1\). Therefore
\[
V\setminus T\text{ is super dominating}\quad\Longleftrightarrow\quad
\forall (i,j)\in T:\quad
(r_i=1\ \land\ z_c>0)\ \lor\ (c_j=1\ \land\ z_r>0).\tag{1}
\]
This is necessary and sufficient, including the empty \(T\) case.

**Maximum complement size.** If \(z_c=0\), criterion (1) forces every occupied column to have degree one; indeed every column is occupied, so \(|T|=q\) and a row must be empty. If \(z_r=0\), symmetrically \(|T|=p\) and a column must be empty. If both are positive, every edge of the incidence graph touches an endpoint of degree one. Thus every nontrivial connected component is a star; components of single edges are allowed. If no row or no column has degree greater than one, \(T\) is a matching, and \(|T|\le p\le q\). If only row centers of degree at least two exist, \(|T|\le q\), since all columns have degree at most one; with only column centers, \(|T|\le p\).

Suppose there are \(a\ge1\) row centers and \(b\ge1\) column centers, together with \(s\ge0\) isolated-edge components. All row centers connect only to degree-one columns, and all column centers connect only to degree-one rows. At least one row and one column are empty. Consequently the numbers of edges incident to row centers and column centers are at most \(q-b-1-s\) and \(p-a-1-s\), respectively. Including the \(s\) isolated edges gives
\[
|T|\le (q-b-1-s)+(p-a-1-s)+s
=p+q-a-b-2-s\le p+q-4.\tag{2}
\]
Equality in (2) requires \(a=b=1\), \(s=0\), precisely one empty row and precisely one empty column, and every remaining available row or column incident to its designated center. It is therefore exactly the crossed-star configuration given above. Conversely such configurations satisfy (1) whenever \(p,q\ge4\).

A full row contains \(q\) cells and satisfies (1) because all columns then have degree one and another row is empty. This realizes \(|T|=q\). Crossed stars realize \(|T|=p+q-4\). Hence the maximum possible size is exactly \(h=\max\{q,p+q-4\}\).

**Equality classification.** The maximum \(h\) equals \(q\) when \(p\le4\), and equals \(p+q-4\) when \(p\ge4\). If a maximizer has no column of degree greater than one, then its \(h=q\) cells must occupy all columns exactly once, with an empty row; this is a column transversal. If instead it has no row of degree greater than one, the symmetric possibility has \(p\) cells and can be optimal only if \(p=q\le4\); it is a row transversal with an empty column. In every remaining case there are both types of nontrivial star center, so equality in (2) forces crossed stars. Conversely, each listed form has cardinality \(h\) and satisfies (1). The three forms are disjoint: any common row-and-column transversal would be a perfect matching with no empty row or column, violating (1), whereas a crossed-star configuration has both a row and a column of degree at least two.

**Counting.** A column transversal of size \(q\) is a map from the \(q\) columns into the \(p\) rows. It has an empty row exactly when that map is not surjective. Its number is
\[
B_{p,q}=p^q-p!\left\{\begin{matrix}q\\p\end{matrix}\right\},\tag{3}
\]
where the braces denote a Stirling number of the second kind. A row transversal contributes a second, disjoint \(B_{p,p}\) when \(p=q\le4\). A crossed-star configuration uniquely determines its center row, empty row, center column and empty column, giving \(pq(p-1)(q-1)\) distinct configurations. Summing precisely the types permitted by the equality classification and using
\[
B_{2,q}=2,\qquad B_{3,q}=3\cdot2^q-3,\qquad B_{4,q}=4\cdot3^q-6\cdot2^q+4
\]
proves the displayed seven-case enumeration, including the small square cases. The growth comparison follows directly.

## Verification

Run `python3 check_rook_super.py` using only the Python standard library. The checker implements the graph-theoretic private-neighbor definition independently of equation (1) and compares both predicates for every one of the \(1{,}152{,}848\) subsets on nine boards ranging from \(2\times2\) to \(4\times5\). It also compares the full optimum-complement family with a separately generated classified family. For the \(5\times5\) board it checks all \(657{,}800\) subsets having six or seven cells in the complement. The combined \(1{,}810{,}648\) checks passed. These finite tests are corroboration; the universal assertion follows from the proof above.

## Relationship to prior work

Klein, Rodríguez-Velázquez and Yi established the minimum super domination number of the Cartesian product of two complete graphs, especially their Theorem 30. Their numerical result is explicitly treated here as known. The present theorem distinguishes and enumerates all attaining sets by their row–column incidence structure; their published bound does not state these counts or the width-four growth transition.

Ghanbari, Jäger and Lehtilä introduced systematic enumeration of minimum super dominating sets and computed the number for complete graphs, complete bipartite graphs, stars, friendship graphs, paths and cycles. Their full-text treatment motivates optimizer counting but does not provide the rook-graph classification. The underlying graph can equivalently be viewed as the line graph of a complete bipartite graph; this equivalence is included in the overlap comparison.

## Limitations

No formula is asserted for arbitrary nonminimum super dominating sets, higher-factor Hamming graphs or noncomplete bipartite line graphs. The known numerical minimum is not claimed as novel. The bibliographic comparison does not exclude all unindexed equivalent statements; priority remains subject to further verification. The computational checks are finite and do not replace the universal proof.

## References

1. D. J. Klein, J. A. Rodríguez-Velázquez, E. Yi, *On the super domination number of graphs*, arXiv:1705.00928 (first submitted 2 May 2017), Theorem 30 and proof, https://arxiv.org/pdf/1705.00928.
2. N. Ghanbari, G. Jäger, T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795 (first submitted 5 September 2022), Section 6, https://arxiv.org/pdf/2209.01795.
