# Rigidity and exact enumeration of shortest burning sequences in binary projective triple systems

## Finding
For every integer \(m\ge3\), the shortest valid sequential burning sequences of the binary projective Steiner triple system \(H_m\) are **exactly** those whose first \(m\) sources are an ordered vector-space basis and whose final source is any vertex not already burned at the end of round \(m\). The final choice is always redundant (it also ignites by propagation in that round). Thus every minimum sequence has the cumulative burned-count profile
\[1,2,4,\ldots,2^{m-1},2^m-1,\]
and the exact number of shortest ordered sequences is
\[B_m=(2^{m-1}-1)\prod_{j=0}^{m-1}(2^m-2^j).\]
The known burning number is \(m+1\). The contribution is the *classification of all optimum source sequences*, including their forced temporal profile, and the resulting count for arbitrary \(m\).

## Assumptions and scope
Let \(V=\mathbb F_2^m\setminus\{0\}\), where addition is over the binary field. The hyperedges of \(H_m\) are precisely the triples \(\{x,y,x+y\}\) with distinct \(x,y\in V\). All three entries are nonzero and distinct, and every pair lies in a unique triple. In round \(r\ge1\), a source \(a_r\) must be outside the burned set \(S_{r-1}\) at the *end of the preceding round*. Simultaneously, every triple whose other two vertices lie in \(S_{r-1}\) propagates fire to its third vertex. Thus, with \(S_0=\varnothing\),
\[S_r=S_{r-1}\cup\{x+y:x,y\in S_{r-1},\ x\ne y\}\cup\{a_r\}.\]
A source is *redundant* if it was unburned at the previous round but also would ignite by propagation in its chosen round. Labelled sequences distinguish vectors and ordered source positions; final redundant choices are counted separately. No claim is made about other Steiner triple systems, affine triple systems, or nonsynchronous variants.

## Proof
**Span obstruction.** Let \(U_r=\langle a_1,\ldots,a_r\rangle\) be the binary linear span of the first \(r\) chosen sources. The displayed update rule shows inductively that \(S_r\subseteq U_r\setminus\{0\}\). More sharply, immediately before a new source in round \(r\), all propagating vertices lie in \(U_{r-1}\). Consequently
\[|S_r|\le 2^{\dim U_{r-1}}\!\!-1+1\le2^{r-1}.\]
For \(r\le m\), this is strictly smaller than \(|V|=2^m-1\) (using \(m\ge3\) at the endpoint). Hence at least \(m+1\) rounds are necessary. If an \((m+1)\)-round sequence is successful but \(a_1,\ldots,a_m\) are linearly dependent, then \(\dim U_m\le m-1\) and in the final round the entire propagated set lies in \(U_m\setminus\{0\}\). The last chosen source can add at most one further point, so \(|S_{m+1}|\le2^{m-1}<2^m-1\), a contradiction. Therefore its first \(m\) sources form a basis.

**Basis-prefix propagation.** Conversely, fix any ordered basis \(a_1,\ldots,a_m\). Induction shows, for every \(1\le r\le m\),
\[S_r=(\langle a_1,\ldots,a_{r-1}\rangle\setminus\{0\})\cup\{a_r\}.\]
It holds at \(r=1\), interpreting the span of the empty set as \(\{0\}\). For the step, write \(W=\langle a_1,\ldots,a_{r-2}\rangle\). At the end of round \(r-1\), every nonzero element of \(W\), and the point \(a_{r-1}\) outside \(W\), are burned. Propagation from pairs \(a_{r-1},w\) with \(0\ne w\in W\), together with the points already burned, fills precisely every nonzero element of \(\langle W,a_{r-1}\rangle\). The new independent source \(a_r\) adds one point outside that space; it was legal. In particular, \(|S_r|=2^{r-1}\).

At the end of round \(m\), exactly \(2^{m-1}\) vertices are burned, and the next propagation phase, *without needing an additional source*, fills all \(2^m-1\) vertices. Every one of the remaining \(2^m-1-2^{m-1}=2^{m-1}-1\) vertices is a legal final source and is redundant. These and only these source sequences achieve the lower bound \(m+1\).

**Enumeration.** The number of ordered bases of \(\mathbb F_2^m\) is
\[\prod_{j=0}^{m-1}(2^m-2^j),\]
since after choosing \(j\) independent vectors their span excludes exactly \(2^j\) vectors. Multiplication by the \(2^{m-1}-1\) valid final redundant choices proves the stated count and complete classification.

## Verification
The standalone `verify_pg.py` exhaustively enumerates **all valid source sequences**, including sequences with a redundant source, using a cached exact bitmask recurrence for \(m=3\) and \(m=4\). It gives respectively \(504\) and \(141120\), in agreement with the formula and the previously tabulated small cases. Explicit independent-basis trajectories are replayed for \(m=3,4,5,6\), with cumulative counts \(1,2,4,\ldots,2^{m-1},2^m-1\). Run `python3 verify_pg.py`; `verify_output.txt` contains the executed output. The general theorem rests on the preceding proof, **not** on finite enumeration.

## Relationship to prior work
Burgess, Danziger, Jones, Marbach and Pike, *Burning Steiner Triple Systems*, arXiv:2608.25627v1, Section 4.7, prove the burning number \(b(H_m)=m+1\) and exhibit an optimal sequence through induction; that numerical extremum and construction are not claimed as new. The indexed computational table in C. W. Jones's *Hypergraph Burning* MSc thesis reports exactly \(504\) optimal sequences on the Fano STS and \(141120\) on the 15-point projective STS, so those two numbers are also explicitly not new. What is proved here is the global forced-basis criterion for **every** minimum sequence, the unique optimum size profile, and the resulting count in all dimensions. The related published finite enumerations are compatible with, but do not themselves establish, this all-dimensional classification.

## Limitations
The result concerns only binary projective Steiner triple systems and ordered valid synchronous sources; it does not classify arbitrary designs, nor distinguish equivalence classes under projective automorphisms. Source priority beyond the inspected 2026 full-text paper remains subject to historical verification: the complete 2025 thesis PDF could not be accessed here, although relevant indexed excerpts containing the small cases were examined. Nothing here is independently audited, and searches alone do not prove priority.

## References
1. A. C. Burgess, P. H. Danziger, C. W. Jones, T. G. Marbach, D. A. Pike, *Burning Steiner Triple Systems*, arXiv:2608.25627v1, 26 August 2026, https://arxiv.org/html/2608.25627 . Sections 1 and 4, especially Theorem 4.7.
2. C. W. Jones, *Hypergraph Burning*, MSc thesis, Memorial University of Newfoundland, available indexed PDF at https://www.math.mun.ca/~dapike/publications/Theses/JonesCaleb-MSc.pdf . Computational-results table and accompanying indexed passages; complete PDF unavailable for inspection.
