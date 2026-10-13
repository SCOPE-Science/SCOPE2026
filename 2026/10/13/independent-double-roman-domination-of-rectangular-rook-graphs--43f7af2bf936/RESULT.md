# Independent double Roman domination of rectangular rook graphs
## Finding
For integers \(2\le m\le n\), let
\[
R_{m,n}=K_m\square K_n,
\]
the rectangular rook graph on an \(m\)-by-\(n\) board. Equivalently,
\[
R_{m,n}=L(K_{m,n}).
\]
Then
\[
i_{dR}(R_{m,n})=
\begin{cases}
2m,&m=n,\\
3m,&m<n.
\end{cases}
\]

The equality cases are completely rigid.

If \(m=n\), every minimum independent double Roman dominating function is obtained by choosing a permutation \(\pi\in S_n\), assigning label \(2\) to
\[
(1,\pi(1)),\ldots,(n,\pi(n)),
\]
and assigning label \(0\) elsewhere. Hence there are exactly
\[
n!
\]
minimum functions.

If \(m<n\), every minimum function is obtained by choosing an injection
\[
\phi:\{1,\ldots,m\}\hookrightarrow\{1,\ldots,n\},
\]
assigning label \(3\) to
\[
(1,\phi(1)),\ldots,(m,\phi(m)),
\]
and label \(0\) elsewhere. Hence there are exactly
\[
\frac{n!}{(n-m)!}
\]
minimum functions.

## Assumptions and scope
An independent double Roman dominating function is a map
\[
f:V(G)\to\{0,1,2,3\}
\]
such that every vertex labeled \(0\) is adjacent either to a vertex labeled \(3\) or to at least two vertices labeled \(2\), every vertex labeled \(1\) has a neighbor labeled at least \(2\), and the positive support
\[
\{v:f(v)>0\}
\]
is independent. Its weight is
\[
\omega(f)=\sum_{v\in V(G)}f(v),
\]
and \(i_{dR}(G)\) is the minimum weight.

The theorem is stated for \(2\le m\le n\). The case \(m>n\) follows by symmetry.

## Proof
Let \(f\) be an independent double Roman dominating function on \(R_{m,n}\), and let
\[
S=\{v:f(v)>0\}.
\]
No vertex of \(S\) can have label \(1\): such a vertex would need a neighbor with label at least \(2\), contradicting the independence of \(S\). Thus every vertex of \(S\) has label \(2\) or \(3\).

View vertices of \(R_{m,n}\) as cells of an \(m\)-by-\(n\) board, with adjacency when two cells share a row or a column. Since \(S\) is independent, it contains at most one cell in each row and at most one cell in each column. Thus \(S\) is a partial matching between rows and columns.

Every zero-labeled cell must have a positive neighbor, so \(S\) is also a dominating set. If some row and some column were both unoccupied by \(S\), their intersection cell would have no neighbor in \(S\), a contradiction. Hence every row is occupied or every column is occupied. Because \(m\le n\) and an independent set has size at most \(m\), it follows that
\[
|S|=m,
\]
and every row contains exactly one support vertex. The \(m\) support vertices lie in distinct columns.

Suppose first that \(m=n\). Then the support occupies every row and every column, so it is a permutation matrix. Every zero cell has exactly two neighbors in \(S\): the support cell in its row and the support cell in its column. Since every support label is at least \(2\),
\[
\omega(f)\ge2n.
\]
Assigning label \(2\) to every cell of any permutation matrix makes each zero cell adjacent to two label-\(2\) vertices, so weight \(2n\) is attainable. Equality forces every support label to be exactly \(2\). Therefore the minimum functions are precisely the \(n!\) permutation-matrix labelings.

Now suppose \(m<n\). The support occupies exactly \(m\) columns, so at least one column \(j\) is unoccupied. In every row \(i\), the cell \((i,j)\) is zero and has exactly one positive neighbor, namely the unique support vertex in row \(i\). Consequently that support vertex must carry label \(3\). This holds in every row, so
\[
\omega(f)\ge3m.
\]
Conversely, choose any injection from the row set into the column set and label the corresponding \(m\) cells by \(3\). Every other cell shares a row with one of these label-\(3\) cells, so the labeling is feasible and has weight \(3m\). Equality therefore forces precisely this form. The number of row-to-column injections is
\[
n(n-1)\cdots(n-m+1)=\frac{n!}{(n-m)!}.
\]

## Verification
The included checker evaluates the definition directly. It exhausts every labeling on \(R_{2,2}\), \(R_{2,3}\), and \(R_{3,3}\), totaling
\[
4^4+4^6+4^9=266{,}496
\]
labelings. The exact minima and complete minimum-function sets agree with the theorem: \(2\), \(6\), and \(6\) minimum functions respectively.

The checker also constructs every theorem-predicted minimum function for all
\[
2\le m\le n\le8
\]
and checks independence, every double Roman defense condition, weight, and the exact injection count.

## Relationship to prior work
The 2019 preprint by Mojdeh and Mansouri studies the same independent double Roman parameter and develops general bounds and relationships with independent domination and independent Roman \(\{2\}\)-domination. A 2020 same-parameter article gives further sharp bounds and, in particular, relates equality in the lower bound \(2i(G)\le i_{dR}(G)\) to independent \(2\)-domination.

For the square rook graph, the scalar value \(2n\) is compatible with that general equality criterion because a permutation matrix is an independent \(2\)-dominating set. The present result goes further by classifying every minimum function and by determining the rectangular phase \(m<n\), where the value jumps from \(2m\) to the upper-bound value \(3m\). The jump is caused by the unoccupied columns: each row then contains zeros having only one support neighbor, forcing every support label from \(2\) to \(3\).

Targeted searches under rook-graph, Hamming-graph, line-graph, Cartesian-product, and \(L(K_{m,n})\) formulations did not locate an exact independent double Roman theorem for this family. The 2023 survey of double Roman domination summarizes independent double Roman results primarily as general bounds and tree results, with no rook-graph specialization identified in the inspected material.

## Limitations
The theorem concerns independent double Roman domination, not ordinary double Roman domination or independent Roman domination.

The square scalar value can also be reached through a general lower-bound equality criterion once the independent \(2\)-domination structure of the rook graph is supplied; the new content includes the complete optimizer classification and the unequal-side formula and classification.

Finite exhaustive computation is corroborative only. The arbitrary-parameter theorem follows from the partial-matching and unoccupied-column proof.

A differently phrased or non-indexed treatment of the same rook-graph family may exist.

## References
1. D. A. Mojdeh and Z. Mansouri, “On the Independent Double Roman Domination in Graphs,” preprint arXiv:1904.04788, first public 9 April 2019; later Bulletin of the Iranian Mathematical Society 46 (2020), DOI 10.1007/s41980-019-00300-9.
2. H. R. Maimani, M. Momeni, F. Rahimi Mahid, S. M. Sheikholeslami, “Independent double Roman domination in graphs,” AKCE International Journal of Graphs and Combinatorics 17(3) (2020), 905–910, DOI 10.1016/j.akcej.2020.02.001; published online 9 July 2020.
3. D. Rupnik Poklukar and J. Žerovnik, “Double Roman Domination: A Survey,” Mathematics 11 (2023), 351, DOI 10.3390/math11020351.
