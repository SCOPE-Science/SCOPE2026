# Parity-dependent multiplicities of maximum odd induced subgraphs in rook graphs

## Finding

Let \(R_{m,n}=K_m\square K_n\) be the simple rook graph on an \(m\)-by-\(n\) labelled board. A vertex subset \(S\) is *odd* when every vertex has odd degree in the induced graph \(R_{m,n}[S]\); the empty subset is allowed. Write \(\mathcal M_{m,n}\) for the family of odd subsets of maximum cardinality and \(M_{m,n}=|\mathcal M_{m,n}|\).

For all integers \(1\le m\le n\), define the even-fibre count, for even \(m\), by
\[
E_m(n)=m![x^m](\cosh x)^n
=\sum_{\substack{e_1+\cdots+e_n=m\\e_j\ge0\text{ even}}}
\frac{m!}{e_1!\cdots e_n!}.
\]
Then the **complete multiplicity formula** is
\[
M_{m,n}=\begin{cases}
1,&m+n\text{ odd},\\
1,&m=n=1,\\
n,&m<n,\ m,n\text{ odd},\\
E_m(n),&m<n,\ m,n\text{ even},\\
2m,&m=n\ge3\text{ odd},\\
2E_m(m),&m=n\ge2\text{ even}.
\end{cases}
\]
Here the formula for the maximum cardinality itself,
\[
\max_{S\text{ odd}}|S|=\begin{cases}mn,&m+n\text{ odd},\\mn-m,&m+n\text{ even}\end{cases},
\]
**is previously public and is not asserted to be new** [1]. The new assertion is the exhaustive classification of every maximizer and its exact multiplicity.

If \(m+n\) is odd, the unique maximizer is the full board. Suppose \(m,n\) have the same parity, and let \(D=V(R_{m,n})\setminus S\). If \(m<n\) and \(m\) is odd, the maximizing deletion sets are exactly the \(n\) complete columns. If \(m<n\) and \(m\) is even, the maximizing deletion sets are exactly the graphs of maps \(f:[m]\to[n]\) with **every fibre even**: \(D=\{(i,f(i)):1\le i\le m\}\). On a square board \(m=n\ge2\), take the union of that row-transversal family and its transpose (column-transversal family); these two families are disjoint. For \(m=n=1\), the only maximizing odd set is empty. For \(m>n\), interchange coordinates.

A quantitative consequence distinguishes the two parity regimes. For each fixed even \(m=2r\ge2\), along even \(n>m\),
\[
M_{m,n}=(2r-1)!!\,n^r+O_r(n^{r-1}),\quad
(2r-1)!!=\frac{(2r)!}{2^r r!},
\]
whereas for each fixed odd \(m\ge1\), along odd \(n>m\), the exact multiplicity is only \(n\).

## Assumptions and scope

The board rows and columns are individually labelled; two different vertex subsets are counted separately even if they are related by an automorphism. All graphs are finite, simple and undirected. Degrees refer to the *induced* subgraph on \(S\). The theorem includes one-vertex graphs and excludes no values of \(m,n\) beyond positivity. The coefficient notation is formal: \([x^m]\) selects the indicated coefficient in the power series, so the displayed integer is exact.

## Proof

It suffices by symmetry to assume \(1\le m\le n\). Write \(D\) for the deleted cells and let \(r_i\) and \(c_j\) denote the number of deletions in row \(i\) and column \(j\), respectively. For a *retained* cell \((i,j)\), no deleted cell is counted twice, and therefore
\[
\deg_{R_{m,n}[S]}(i,j)=m+n-2-r_i-c_j.
\]
When \(m+n\) is odd the full board has odd degree everywhere, proving its uniqueness at full cardinality.

Now let \(m+n\) be even. If \(|D|<m\), then there is an untouched row and an untouched column. Their intersection is retained and has original even degree \(m+n-2\), a contradiction. Thus \(|D|\ge m\). Deleting any entire column (\(m\) cells) leaves \(K_m\square K_{n-1}\), whose degrees \(m+n-3\) are odd. This proves the **already-known** maximum cardinality formula [1]. Hence every maximizer has \(|D|=m\).

If \(m<n\), then at least one column is untouched. Accordingly every row must meet \(D\), else an untouched row and untouched column would contradict oddness. As there are precisely \(m\) deletions, there is *exactly one per row*. If \(m=n\), the same empty-row/empty-column argument shows that every deletion set of size \(m\) meets **all rows or all columns**. We analyze the all-rows case; transpose handles the other.

Write \(f(i)\) for the column of the unique deletion in row \(i\), so \(r_i=1\), and let \(c_j=|f^{-1}(j)|\). Every column with \(c_j<m\) contains a retained cell, whose induced degree is odd precisely when \(1+c_j\) is odd. Thus every *nonfull* column has an even fibre size. A full column has fibre size \(m\) and no retained cell to test.

If \(m\) is even, the full columns also have even fibre size, so the necessary and sufficient condition is that **every** fibre of \(f\) be even. Conversely, this condition makes the degree of every retained cell odd by the same formula. If \(m\) is odd, the sum \(\sum_j c_j=m\) is odd, while every nonfull fibre has even size. Hence at least one full column occurs; since the total number of deleted cells is \(m\), the deletion set must be precisely one full column. The converse is immediate.

For \(m=n\ge2\), a set meeting every row and every column with exactly \(m\) cells is a permutation matrix: then each retained cell has \(r_i=c_j=1\), giving even retained degree. As there are retained cells when \(m\ge2\), such a matrix cannot be a maximizing deletion set. Therefore the all-row and all-column families above are **disjoint**; both have the same count by transposition, yielding the factor two. When \(m=n=1\), the retained set is empty and must be handled separately.

For even \(m\), to count the all-row family, assign each of the \(m\) labelled rows to a labelled column, requiring even sizes of all column fibres. Fixing fibre sizes \((e_1,\ldots,e_n)\) gives the multinomial coefficient \(m!/\prod_j e_j!\), and the exponential generating-function product is \((\cosh x)^n\). This gives \(E_m(n)\) exactly. For fixed \(m=2r\), the highest-degree contribution in \(n\) comes from choosing \(r\) distinct columns each receiving two rows: there are \((2r-1)!!\,(n)_r\) such assignments, where \((n)_r\) is the falling factorial. All remaining even-fibre types use at most \(r-1\) columns and contribute \(O_r(n^{r-1})\). This proves the asymptotic claim and completes the classification and count.

## Verification

The included standalone `verify.py` uses only the Python standard library. Run `python verify.py` to enumerate every vertex subset independently from its literal rook-graph adjacency, compute the actual maximum cardinality and the complete set of maximizing complements, then compare **both the actual subsets and their counts** with the structural formula. This was executed successfully for seventeen graph sizes, each with at most twenty vertices, testing 122 maximizing subsets in total. The script separately computes the even-fibre coefficient by dynamic programming and prints additional larger-order predictions. These finite checks are supportive, not a proof for all orders.

Selected exact counts are \(M_{2,2}=4\), \(M_{3,3}=6\), \(M_{4,4}=80\), \(M_{4,6}=96\), \(M_{5,5}=10\) and \(M_{6,6}=4512\).

## Relationship to prior work

The maximum size of an odd induced subgraph of a rectangular rook graph, including the sharp column-deletion lower bound, was explicitly stated and verified publicly in June 2026 [1]. It is not a contribution here. The present theorem classifies **all** equality cases, counts their different labelled choices and reveals the distinct growth of multiplicities at odd and even fixed widths. Neither the scalar result in [1] nor the broad lower-bound statements in [2–4] directly imply those equality-case multiplicities.

Zeng [2] develops general odd-cut methods for large odd induced subgraphs. Ai et al. [3] prove a sharp lower-bound constant for graphs of maximum degree four, and Guo et al. [4] study lower bounds for arbitrary degree-parity prescriptions. These supply current motivation but are not claimed to be the source of the new rook-graph classification.

## Limitations

Only **maximum-cardinality** odd induced subsets are classified, not all odd induced subsets of smaller size. For arbitrary dimensions, correctness relies on the displayed proof. Bibliographic priority of the new multiplicity formula remains subject to further literature checking, including inaccessible complete texts of [2] and [4]. No independent mathematical audit has been performed.

## References

[1] Keanu Dean, "Proof verification: maximum odd induced subgraph of a rook graph," Mathematics Stack Exchange, June 24, 2026; answer by Mike Earnest, same date. https://math.stackexchange.com/questions/5141680/proof-verification-maximum-odd-induced-subgraph-of-a-rook-graph

[2] Qinghou Zeng, "Large odd induced subgraphs via odd cuts," arXiv:2607.23266, first posted July 25, 2026. https://arxiv.org/abs/2607.23266

[3] Jiangdong Ai, Qiwen Guo, Gregory Gutin, Yiming Hao and Anders Yeo, "Odd Induced Subgraphs in Graphs of Maximum Degree Four," arXiv:2511.15489, first posted November 19, 2025. https://arxiv.org/abs/2511.15489

[4] Qiwen Guo, Gregory Gutin, Yiming Hao, Yongtang Shi, Yong Zhang and Yacong Zhou, "Bounds on Odd and Odd-Even Induced Subgraphs," arXiv:2608.02339, first posted August 3, 2026. https://arxiv.org/abs/2608.02339
