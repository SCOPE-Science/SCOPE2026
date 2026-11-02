# Minimal forts, complete zero-forcing polynomial, and fractional gap of crown graphs

## Finding

**Theorem.** For each integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the crown graph with shores \(L=\{L_1,\ldots,L_n\}\) and \(R=\{R_1,\ldots,R_n\}\), where \(L_iR_j\) is an edge exactly when \(i\ne j\). Its full inclusion-minimal fort collection consists of

\[
\mathcal F_{\min}(\operatorname{Cr}_n)
=\big\{\{L_i,L_j,L_k\}:i<j<k\big\}
\cup\big\{\{R_i,R_j,R_k\}:i<j<k\big\}
\cup\big\{\{L_i,L_j,R_i,R_j\}:i<j\big\}.
\]

Thus there are exactly \(2\binom n3+\binom n2\) minimal forts, of sizes three and four. Put \(c=\binom n2\). The polynomial counting **all** standard zero-forcing sets by number of initially blue vertices is

\[
\mathcal Z_n(z)=\sum_{a=0}^2\sum_{b=0}^2\binom na\binom nb z^{2n-a-b}-c z^{2n-4}
=c(c-1)z^{2n-4}+2nc z^{2n-3}+(n^2+2c)z^{2n-2}+2nz^{2n-1}+z^{2n}.
\]

In particular,

\[
Z(\operatorname{Cr}_n)=2n-4,\quad
\#\{\text{minimum zero-forcing sets}\}=\binom n2\big(\binom n2-1\big),\quad
\operatorname{ft}(\operatorname{Cr}_n)=\left\lfloor\frac{2n}{3}\right\rfloor,
\quad Z^*(\operatorname{Cr}_n)=\frac{2n}{3}.
\]

Here \(\operatorname{ft}\) means the maximum number of pairwise vertex-disjoint nonempty forts, and \(Z^*\) is the optimum of the fractional *fort-cover* linear program (not the unrelated three-color/skew forcing game). The ratio \(Z/Z^*=3-6/n\) approaches three.

## Assumptions and scope

All graphs are finite, undirected, and simple. A **fort** is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors in \(F\). A fort is **inclusion-minimal** when it contains no proper nonempty fort. In standard zero forcing, a blue vertex with precisely one white neighbor may force that neighbor blue; a set is zero forcing when repeated legal forces can blue the graph. The fort-cover LP minimizes \(\sum_v x_v\) subject to \(x_v\ge0\) and \(\sum_{v\in F}x_v\ge1\) for all forts \(F\). The theorem holds for all and only integer parameters \(n\ge3\); its boundary \(n=2\), consisting of two independent edges, is intentionally excluded.

## Proof

**1. Exhaustive fort classification.** For \(F\subseteq V(\operatorname{Cr}_n)\), define its shore-index sets \(A=\{i:L_i\in F\}\) and \(B=\{i:R_i\in F\}\), with \(a=|A|\), \(b=|B|\). By the exact adjacency rule, any excluded left vertex \(L_i\) with \(i\notin A\) has \(b-\mathbf1_{i\in B}\) neighbors in \(F\). Every excluded right vertex \(R_j\), \(j\notin B\), has \(a-\mathbf1_{j\in A}\) such neighbors. Hence the fort condition is equivalent to

\[
\forall i\notin A:\ b-\mathbf1_{i\in B}\ne1,\qquad
\forall j\notin B:\ a-\mathbf1_{j\in A}\ne1.
\tag{1}
\]

Every three left vertices form a fort, because an outside right vertex has two or three neighbors in that triple and an outside left vertex has none. The same holds for every right triple. Thus any minimal fort with \(a\ge3\) equals exactly one left triple; likewise, any minimal fort with \(b\ge3\) equals exactly one right triple. (The asserted triples are minimal because, as verified next, no smaller nonempty fort exists.)

It remains to classify nonempty pairs of sets with \(0\le a,b\le2\). If \(b=0\) and \(1\le a\le2\), some excluded right vertex has exactly one neighbor when \(a=1\); for \(a=2\), choose an index in \(A\) (its right vertex is excluded), which sees \(a-1=1\). This uses \(n\ge3\) in the singleton case to find an excluded index. The case \(a=0\), \(1\le b\le2\) is symmetric. If \(a=b=1\), choose an index outside \(A\cup B\), which exists because \(n\ge3\); the excluded vertex on either shore then sees one neighbor. If \(a=1,b=2\), choose \(i\in B\setminus A\), which is nonempty; the excluded \(L_i\) has exactly one neighbor. If \(a=2,b=1\), the symmetric argument applies. Finally, if \(a=b=2\), the first inequality (1) forces \(B\subseteq A\), and the second forces \(A\subseteq B\); hence \(A=B=\{i,j\}\). Conversely this configuration is a fort: each excluded vertex sees two neighbors, as its index is not one of \(i,j\). Its only smaller nonempty subsets have shore sizes at most two and were just excluded. These cases prove that the displayed three types are all minimal forts, including their minimality and the claimed count.

**2. Exact zero-forcing polynomial.** By the fort-transversal characterization of standard zero forcing, an initially blue set \(S\) is zero forcing exactly when it intersects every inclusion-minimal fort. Let \(A\) be the indices of white left vertices and \(B\) those of white right vertices. Avoiding an entirely white left or right triple is equivalent to \(a\le2\) and \(b\le2\). Avoiding a white matched four-set is equivalent to forbidding any two distinct indices in \(A\cap B\), i.e. \(|A\cap B|\le1\). For \(a,b\le2\), the only excluded pairs \((A,B)\) are \(a=b=2\) with \(A=B\); there are \(\binom n2\) of them. All other choices are admissible. Counting choices independently by \(a\) and \(b\), then deleting those forbidden coincidences, gives the polynomial exactly. Its smallest exponent is \(2n-4\), whose coefficient \(\binom n2(\binom n2-1)\) is positive for every \(n\ge3\), proving both minimum statements.

**3. Largest family of disjoint forts.** Every fort contains a minimal fort and therefore has size at least three. Thus at most \(\lfloor2n/3\rfloor\) pairwise disjoint forts can fit in \(2n\) vertices. Write \(n=3q+r\), where \(r\in\{0,1,2\}\). Form \(q\) disjoint triples in the left shore and \(q\) in the right shore using the first \(3q\) indices. When \(r=0\) or \(r=1\), these \(2q\) forts reach \(\lfloor2n/3\rfloor\). When \(r=2\), add the matched four-set on the remaining two indices to obtain \(2q+1=\lfloor2n/3\rfloor\) disjoint forts. Both bounds match.

**4. Exact fractional fort-cover optimum.** Assign \(x_v=1/3\) to all \(2n\) vertices. Each fort contains at least three vertices, so this assignment is feasible with objective \(2n/3\). For the opposite inequality, place dual weight \(1/\binom{n-1}{2}\) on each of the \(2\binom n3\) single-shore triple forts and zero on all other minimal forts. Each vertex occurs in exactly \(\binom{n-1}{2}\) supported triples; therefore every dual vertex-capacity sum is one. The dual objective is

\[
\frac{2\binom n3}{\binom{n-1}{2}}=\frac{2n}{3}.
\]

Weak LP duality proves equality; no numerical optimization or unproved integrality assertion is required.

## Verification

The accompanying standard-library Python program `verify.py` computes graph adjacency directly and, without using the classification formulas to identify forts or forcing sets, exhaustively enumerates all inclusion-minimal forts and all zero-forcing sets for each \(3\le n\le8\). It compares the results to the explicit formulas, checks direct disjoint-fort packings through \(n=7\), and verifies the primal/dual fractional certificates in all tested orders. It reports `VERIFY_OK`. These finite computations are corroboration, not a substitute for the proof for arbitrary \(n\). Execute using `python3 verify.py`.

## Relationship to prior work

Cameron, Hogben, Kenter, Mojallal, and Schuerger (2023, arXiv:2310.17904) introduced the fort number, the fort-cover fractional zero-forcing LP, and an exact fort-transversal interpretation of ordinary zero forcing. Their complete-bipartite example concerns the graph *before* deleting a perfect matching; its minimal forts are shore pairs, whereas the deletion destroys those twin-pair forts. Becker, Cameron, Hanely, Ong, and Previte (2024, arXiv:2404.05963), Proposition 9, explicitly enumerated minimal forts of complete bipartite graphs, but not the matching-deleted family. The later general integer-programming methods of Cameron and Pulaj (2025, arXiv:2508.07293) do not present this crown-family closed classification. Brimkov, Cameron, and Grubbs (2025, arXiv:2507.10826) analyze hypercubes and therefore have a relevant single graph \(\operatorname{Cr}_4\cong Q_3\); this isolated case does not yield the complete all-\(n\) formula. The novelty claim is confined to the combined infinite-family hypergraph and polynomial/LP consequences, not to fort definitions, covering duality, or the specific hypercube instance.

## Limitations

Publication priority is a best-knowledge comparison with the inspected primary literature and research records, not a proof that no equivalent unpublished or unindexed theorem exists. The theorem concerns standard zero forcing and the fort-cover fractional LP, not skew or positive-semidefinite zero forcing. The excluded \(n=2\) disconnected boundary has a different minimal-fort profile. The finite checker establishes only the tested sizes, while the mathematical proof establishes the unbounded family. Independent audit and independent mathematical validation have not been performed.

## References

1. T. R. Cameron, L. Hogben, F. H. J. Kenter, S. A. Mojallal, H. Schuerger, *Forts, (fractional) zero forcing, and Cartesian products of graphs* (first public arXiv posting 2023-10-27), arXiv:2310.17904, https://arxiv.org/abs/2310.17904.
2. P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the number of minimal forts of a graph* (first public arXiv posting 2024-04-09), arXiv:2404.05963, https://arxiv.org/abs/2404.05963.
3. T. R. Cameron, J. Pulaj, *IP Models for Minimum Zero Forcing Sets, Forts, and Related Graph Parameters* (2025), arXiv:2508.07293, https://arxiv.org/abs/2508.07293.
4. B. Brimkov, T. R. Cameron, O. Grubbs, *On the forts and related parameters of the hypercube graph* (2025), arXiv:2507.10826, https://arxiv.org/abs/2507.10826.
