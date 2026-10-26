# Complete power-domination-set classification and polynomial of rectangular rook graphs

## Finding
For every pair of integers \(2\le p\le q\), let \(R_{p,q}=K_p\square K_q\) be the rook graph on the \(p\)-by-\(q\) rectangular board. For \(S\subseteq V(R_{p,q})\), write \(r(S)\) and \(c(S)\) for the numbers of rows and columns meeting \(S\). Then **the exact characterization of every power dominating set** is
\[
 S\text{ is power dominating}\quad\Longleftrightarrow\quad r(S)\ge p-1\ \text{or}\ c(S)\ge q-1.
\]
Thus every non-power-dominating set is contained in a rectangle formed from \(p-2\) rows and \(q-2\) columns (with the empty-set interpretation when \(p=2\)). When \(p,q\ge3\), the inclusion-maximal non-power-dominating sets are exactly those full rectangles, in number \(\binom p2\binom q2\).

Define \(E_{0,0}(z)=1\), \(E_{r,0}(z)=E_{0,c}(z)=0\) whenever exactly one index is positive, and for \(r,c\ge1\) define
\[
 E_{r,c}(z)=\sum_{i=0}^{r}\sum_{j=0}^{c}(-1)^{r+c-i-j}\binom ri\binom cj(1+z)^{ij}.
\]
The full power domination polynomial, enumerating **all** power dominating vertex sets by size, is
\[
 \mathcal P(R_{p,q};z)=(1+z)^{pq}
 -\sum_{r=0}^{p-2}\sum_{c=0}^{q-2}\binom pr\binom qc E_{r,c}(z).
\]
Consequently the known numerical minimum \(\gamma_P(R_{p,q})=p-1\) is refined by an **exact minimum-set multiplicity**:
\[
 [z^{p-1}]\mathcal P(R_{p,q};z)=
 \begin{cases}
 p q^{p-1}, & p<q,\\
 2p\,p^{p-1}-p^2(p-1)!, & p=q.
 \end{cases}
\]
Every coefficient above degree \((p-2)(q-2)\) agrees with the corresponding coefficient of \((1+z)^{pq}\), and this threshold is sharp: for \(p,q\ge3\) a non-power-dominating set of exactly \((p-2)(q-2)\) vertices exists. The polynomial \(E_{r,c}\), interpreted as the edge-cover enumerator of a complete bipartite graph, is an established inclusion-exclusion construction, not claimed independently new here.

## Assumptions and scope
All graphs are finite and simple. The vertices of \(R_{p,q}\) are pairs \((i,j)\), \(1\le i\le p\), \(1\le j\le q\). Distinct pairs are adjacent exactly when they share a row or a column. Standard power domination begins with a selected subset \(S\) and observes the closed neighborhood \(N[S]\). Subsequently, repeatedly, an observed vertex having exactly one as-yet-unobserved neighbor causes that neighbor to become observed. A set is power dominating if this process observes every vertex. The definition includes the empty selected set, which is never power dominating in the present family.

The polynomial is \(\sum_{S\text{ power dominating}} z^{|S|}\) (each vertex subset counted once). No randomized choices, graph isomorphism quotient, or edge-observation convention is implicit.

## Proof
**Lemma 1: The first unobserved region.** Let \(I\) be the set of empty rows of \(S\), and \(J\) the set of empty columns. A vertex \((i,j)\) is in \(N[S]\) precisely when row \(i\) or column \(j\) contains an element of \(S\). Therefore the unobserved vertices immediately after the domination step are exactly \(I\times J\).

**Lemma 2: The forcing criterion.** Suppose \(|I|\ge2\) and \(|J|\ge2\). An observed vertex \((i,j)\) has either no neighbor in \(I\times J\), at least \(|I|\ge2\) such neighbors if \(i\notin I,j\in J\), or at least \(|J|\ge2\) if \(i\in I,j\notin J\). The remaining case \(i\in I,j\in J\) is unobserved, not eligible to force. Hence no observed vertex has exactly one unobserved neighbor: no forcing step is possible and \(S\) fails.

Conversely, if \(|I|\le1\) or \(|J|\le1\), the whole graph is already observed if one of these sets is empty. Suppose \(I=\{i\}\) and \(J\ne\varnothing\). Since \(p\ge2\), some row \(k\ne i\) is occupied. For every \(j\in J\), the vertex \((k,j)\) is observed, and its only unobserved neighbor is \((i,j)\); these vertices can be forced, one for each \(j\). The case \(J\) singleton follows by swapping rows and columns. This proves the claimed equivalence.

**Corollary: Maximal obstructions and cutoff.** Failure requires \(|I|\ge2,|J|\ge2\), so every failing \(S\) lies in a rectangle supported on some \(p-2\) rows and \(q-2\) columns. Every such full rectangle fails. For \(p,q\ge3\), adjoining a vertex outside a full rectangle occupies a previously empty row or column, leaving at most one empty row or column, so its failure is inclusion-maximal. Conversely an inclusion-maximal failing set must fill one such rectangle. Distinct choices of two omitted rows and columns give \(\binom p2\binom q2\) full rectangles. The upper cardinality bound and sharpness follow. If \(p=2\), the empty set is the only failing set.

**Counting the entire polynomial.** To have exactly \(r\) occupied rows and exactly \(c\) occupied columns, first choose those rows and columns in \(\binom pr\binom qc\) ways. The selected vertices form an edge cover of the corresponding complete bipartite incidence graph on \(r+c\) vertices: every chosen row and column must be represented. Apply inclusion-exclusion to omitted rows and columns to obtain its size generating polynomial \(E_{r,c}(z)\) as displayed, with the stipulated zero cases. Failure is equivalent to \(r\le p-2\) and \(c\le q-2\). Subtracting the generating polynomial of all failures from \((1+z)^{pq}\) proves the full expression, including the empty set.

**Minimum size and multiplicity.** A set of cardinality below \(p-1\) cannot meet \(p-1\) rows, and cannot meet \(q-1\) columns because \(q\ge p\), proving the lower bound. The set consisting of one vertex in each of \(p-1\) distinct rows meets it, proving \(\gamma_P=p-1\). If \(p<q\), every \((p-1)\)-element power dominating set uses exactly one vertex in each of \(p-1\) rows, yielding \(p q^{p-1}\) selections. If \(p=q\), also count the analogous column selections, subtracting their intersection: an intersection is a bijection between a selected \((p-1)\)-row set and \((p-1)\)-column set, giving \(p^2(p-1)!\) such sets. Inclusion-exclusion gives the displayed minimum coefficient. \(p=2\) is covered by the same formulas.

## Verification
The accompanying `verify.py` builds rook-graph adjacency lists, directly simulates the closed-neighborhood initialization and subsequent unique-neighbor forces, and checks every vertex subset on eight boards from \(2\times2\) through \(4\times5\). The total is 1,152,592 independently simulated subsets. It compares each direct outcome with the row/column criterion and the complete polynomial produced by separate exact-integer inclusion-exclusion. It also compares the minimum coefficient with the formula and checks exact polynomial arithmetic on all \(2\le p\le8\), \(p\le q\le11\). All checks passed. Run with `python3 verify.py` in the directory containing that file. The output is recorded in `verification_output.txt`. This finite computational check does not prove the infinite theorem; the proof above does.

## Relationship to prior work
Soh and Koh (2014, Theorem 3.3) already established the **minimum cardinality** \(p-1\) for Cartesian products of complete graphs. Their Lemmas 3.1--3.2 prove the numerical bound; that bound is not claimed novel here. Brimkov, Patel, Suriyanarayana and Teich (arXiv:1805.10984, first public 28 May 2018) defined and systematically developed the **power domination polynomial**, obtaining structural results and formulas for other families. Their relevant definitions, structural section and family-enumeration section do not supply this rook-graph full polynomial. Mertens (arXiv:2401.00716, first public January 2024) studies the **ordinary domination polynomial** of rook graphs and its edge-cover inclusion-exclusion; the edge-cover counting identity is shared prior methodology, not a new general identity. Ordinary domination is strictly different from the iterative forcing condition here, so that paper does not imply this full polynomial or the minimum power-domination-set count. The novelty assessed is the exact all-subsets propagation criterion and the resulting full power-domination enumerator and maximal-obstruction classification.

## Limitations
This proof treats precisely the Cartesian product of two complete graphs with both orders at least two. It gives no classification for arbitrary Cartesian products, multidimensional Hamming graphs, constrained propagation variants, or propagation-time distributions. Small-case computational checks are supplementary, not an exhaustive infinite verification. Searches did not locate a covering earlier enumeration, but unindexed or differently described equivalent publications are an unresolved bibliographic priority risk. 

## References
1. B. Brimkov, R. Patel, V. Suriyanarayana, A. Teich, *Power domination polynomials of graphs*, arXiv:1805.10984 (initial submission 2018-05-28), https://arxiv.org/abs/1805.10984.
2. K. W. Soh, K. M. Koh, *A note on Power Domination Problem in Diameter Two Graphs*, AKCE International Journal of Graphs and Combinatorics 11 (2014), 51--55, Theorem 3.3; DOI:10.1080/09728600.2014.12088762.
3. K. M. Koh, K. W. Soh, *Power domination of the Cartesian product of graphs*, AKCE International Journal of Graphs and Combinatorics 13 (2016), 22--30; DOI:10.1016/j.akcej.2016.02.004.
4. S. Mertens, *Domination Polynomial of the Rook Graph*, arXiv:2401.00716 (initial submission 2024-01-01), https://arxiv.org/abs/2401.00716.
