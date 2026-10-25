# The accurate domination polynomial of every rectangular rook graph

## Finding

Let \(2\le p\le q\) be integers and let \(R_{p,q}=K_p\square K_q\) be the graph whose vertices are the cells of a labeled \(p\)-by-\(q\) board, two distinct cells being adjacent if they share a row or a column. A vertex set \(D\) is *accurately dominating* when it dominates the graph and its complement contains no dominating set having exactly \(|D|\) vertices. Write \(N=pq\) and \(d_a(k)\) for the number of accurate dominating sets of cardinality \(k\).

**Structural classification.** A set \(D\) of size \(k\) is accurately dominating if and only if exactly one of the following disjoint conditions holds:

1. \(2k>N\) and \(D\) meets every row or meets every column;
2. \(2k\le N\) and \(D\) contains an entire row and an entire column.

This classification gives every coefficient of the accurate domination polynomial \(A_{p,q}(z)=\sum_{k=0}^N d_a(k)z^k\) by two finite inclusion–exclusion sums. Put
\[
F_{p,q}(k)=\sum_{i=1}^{p}\sum_{j=1}^{q}(-1)^{i+j}\binom pi\binom qj\binom{(p-i)(q-j)}{k-iq-jp+ij},
\]
\[
B_{p,q}(k)=\binom{pq}{k}-\sum_{i=1}^{p}\sum_{j=1}^{q}(-1)^{i+j}\binom pi\binom qj\binom{(p-i)(q-j)}k.
\]
Here \(\binom ab=0\) whenever \(b<0\) or \(b>a\). Then, for every integer \(0\le k\le N\),
\[
\boxed{d_a(k)=\begin{cases}F_{p,q}(k),&2k\le N,\\ B_{p,q}(k),&2k>N.\end{cases}}
\]

In particular, the accurate domination number and the number of minimum accurate dominating sets are
\[
\boxed{\gamma_a(R_{p,q})=p+q-1,}\qquad
\boxed{d_a(p+q-1)=\begin{cases}
\binom{2q}{q+1},&p=2,\\
126,&p=q=3,\\
pq,&p\ge3\text{ and }(p,q)\ne(3,3).
\end{cases}}
\]
For all boards outside the two-row family and the \(3\)-by-\(3\) exception, the minimum accurate dominating sets are **exactly** the \(pq\) different unions of a complete row and a complete column. In the exceptional cases every vertex subset of size \(p+q-1\) is accurately dominating.

## Assumptions and scope

All graphs are finite, simple and undirected, with distinct, labeled cells. Ordinary domination uses closed neighborhoods: each vertex belongs to its own closed neighborhood. The competing set in the definition of accuracy must lie entirely in \(V(R_{p,q})\setminus D\), have cardinality \(|D|\), and itself dominate the original graph; no connectedness or minimality is imposed. The theorem covers all integral \(2\le p\le q\) and all cardinalities \(0\le k\le pq\), including equality at the half-order boundary.

The Cartesian rook graph is also the line graph of the complete bipartite graph \(K_{p,q}\). Thus the theorem equivalently enumerates *accurate edge-dominating subsets* of \(K_{p,q}\) when edges are regarded as adjacent if incident and competition is by disjoint equal-size subsets; it does not use the definition of an edge-dominating set that allows other conventions.

## Proof

**Lemma 1 (dominating sets).** A cell set \(D\) dominates \(R_{p,q}\) if and only if every row contains a cell of \(D\) **or** every column contains a cell of \(D\). Indeed, if row \(r\) and column \(c\) are both disjoint from \(D\), their intersection \((r,c)\) is undominated. Conversely, a cell outside \(D\) has a selected neighbor in its own row whenever all rows are met; the argument for columns is identical.

It follows that every dominating set has at least \(p\) cells because \(p\le q\).

**Lemma 2 (the half-order dichotomy).** Suppose \(D\) dominates, \(k=|D|\), and \(2k\le pq\). Let \(T=V(R_{p,q})\setminus D\), so \(|T|\ge k\ge p\). If \(T\) meets every row, choose one cell of \(T\) per row. The chosen \(p\)-cell set dominates by Lemma 1; it can be extended inside \(T\) to a dominating \(k\)-cell subset. Therefore accurate domination forces \(T\) to miss some row, equivalently forces \(D\) to contain that complete row. Hence \(k\ge q\). If \(T\) meets every column, one cell from each column similarly extends to a dominating \(k\)-cell subset, because now \(k\ge q\). Accuracy thus forces \(D\) to contain an entire column as well.

Conversely, if \(D\) contains a full row and a full column, then \(T\) misses both one row and one column. Every subset of \(T\) therefore fails Lemma 1, regardless of cardinality. Such \(D\) dominates and is accurate. If \(2k>pq\), a rival of size \(k\) cannot fit in the complement; accuracy is then equivalent to ordinary domination. This proves the structural classification.

**Lemma 3 (enumeration).** For fixed nonempty selected families of \(i\) full rows and \(j\) full columns, their union has \(iq+jp-ij\) cells, and the remaining \((p-i)(q-j)\) cells are optional. Inclusion–exclusion over the event that a row is completely selected and the event that a column is completely selected gives \(F_{p,q}(k)\). Similarly, the bad event for ordinary domination is that at least one row and at least one column are completely omitted. For fixed \(i\) omitted rows and \(j\) omitted columns, the remaining \((p-i)(q-j)\) cells are optional; inclusion–exclusion subtracts exactly the double sum in \(B_{p,q}(k)\) from all \(\binom{pq}{k}\) subsets. The coefficient formula follows from Lemma 2.

**Minimum and multiplicity.** Put \(h=p+q-1\). A full row and a full column have union size exactly \(h\), so this gives an accurate dominating set of size \(h\). The inequality
\[
2(h-1)=2(p+q-2)\le pq
\]
follows from \((p-2)(q-2)\ge0\). Therefore every smaller set has size at most half the graph order, and Lemma 2 excludes its accuracy because it cannot contain a full row and column. Thus \(\gamma_a=h\).

If \(h>pq/2\), we have \((p-2)(q-2)<2\), which under \(2\le p\le q\) is equivalent to \(p=2\) or \(p=q=3\). For these boards any \(h\)-cell set is dominating: otherwise by Lemma 1 its complement would contain the union of an empty row and empty column, which requires \(h\) complement cells, but \(pq-h<h\). All \(\binom{pq}{h}\) sets are therefore accurate. If \(h\le pq/2\), Lemma 2 says a minimum accurate set is exactly a row–column union. The \(pq\) choices give distinct sets (here \(p\ge3\), \(q\ge4\)). The asserted three cases follow.

## Verification

A standalone Python program, `verify.py`, derives adjacency from shared row/column coordinates, tests the original domination definition, explicitly searches for disjoint equally large dominating competitors on all subsets of seven small boards, and compares the resulting cardinality distributions to both inclusion–exclusion formulas. It also enumerates every subset on four larger boards to compare the structural criterion and polynomial coefficients, and checks the minimum formula on 95 parameter pairs. Its independent-definition stage covers 10,064 masks, and its larger structural stage covers 1,409,024 masks. The recorded output is `verification-output.txt`; both files are included in the same research package. The code is a finite consistency check, not an infinite proof.

To reproduce: with Python 3 and no external packages, run `python3 verify.py` and require a final line `VERIFY_OK`.

## Relationship to prior work

Cyman, Henning and Topp (2017) developed accurate domination and its comparison with ordinary domination, with results for trees and coronas rather than the row–column incidence structure here. Alikhani, Safazadeh and Ghanbari (2021) specifically studied enumeration of accurate dominating sets of paths, cycles, ladders, book graphs, and the hypercube; their general half-order observation already implies that accurate and ordinary domination coincide for all cardinalities strictly exceeding half the order. This theorem uses that known large-cardinality principle and contributes the low-half complete row–column classification, its inclusion–exclusion enumeration, and the rook-graph minimum-optimum classification. Literature on ordinary domination polynomials of graph products is not presented as the new ingredient.

A 2022 paper entitled *Accurate and Connected Accurate Domination Polynomials of Graphs* examines polynomial enumerators for some standard graph classes. Its complete text was not available for a decisive comparison; coverage of rook graphs therein remains a documented bibliographic uncertainty. A 2022 atlas covers individual connected graphs with at most six vertices, including possible small instances but not the claimed infinite two-parameter classification.

## Limitations

The result concerns precisely two-factor rook graphs, not general Hamming graphs of dimension at least three or arbitrary line graphs. The proof is mathematical, while finite checks are supporting evidence only. Bibliographic searches are not a proof of novelty; unindexed equivalent work and the unresolved 2022 full text could affect priority. No independent validation or external mathematical certification is claimed.

## References

1. Joanna Cyman, Michael A. Henning, Jerzy Topp, *On Accurate Domination in Graphs*, arXiv:1710.03308v1, first posted 2017-10-09; https://arxiv.org/html/1710.03308v1 .
2. Saeid Alikhani, Maryam Safazadeh, Nima Ghanbari, *Enumeration of accurate dominating sets*, arXiv:2101.10185v1, first posted 2021-01-22; https://arxiv.org/html/2101.10185v1 .
3. K. R. Sridhara, M. B. Kattimani, *Accurate and Connected Accurate Domination Polynomials of Graphs*, Annals of Pure and Applied Mathematics 25 (2022), 67–75, DOI:10.22457/apam.v25n2a02861 (only metadata/abstract compared).
4. K. R. Sridhara, M. B. Kattimani, *An Atlas of Accurate Domination Polynomials of Connected Graphs of Order at Most Six*, NeuroQuantology 20 (2022), 902–909, DOI:10.14704/NQ.2022.20.16.NQ88089 (individual small-graph tables).
5. Tomer Kotek, James Preen, Peter Tittmann, *Domination Polynomials of Graph Products*, arXiv:1305.1475 (background on ordinary domination polynomial, not claimed as novel here).
