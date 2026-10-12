# Disjunctive-total-domination polynomial of crown graphs
## Finding
For every integer \(n\ge 3\), let
\[
\operatorname{Cr}_n=K_{n,n}-\{a_i b_i:1\le i\le n\},
\]
with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\). A set \(S\subseteq V(\operatorname{Cr}_n)\) is disjunctive-total-dominating when every vertex has a neighbor in \(S\) or has at least two vertices of \(S\) at distance \(2\). Put
\[
I=\{i:a_i\in S\},\qquad J=\{i:b_i\in S\}.
\]
Then \(S\) is disjunctive-total-dominating if and only if, for every \(i\in\{1,\ldots,n\}\),
\[
J\setminus\{i\}\ne\varnothing\quad\text{or}\quad |I\setminus\{i\}|\ge2,
\]
and simultaneously
\[
I\setminus\{i\}\ne\varnothing\quad\text{or}\quad |J\setminus\{i\}|\ge2.
\]
Consequently every subset of cardinality at least \(4\) is disjunctive-total-dominating, no subset of cardinality at most \(2\) is, and a three-vertex set is disjunctive-total-dominating exactly in either of two forms: all three vertices lie in one bipartition class, or two lie in one class and the singleton on the other side has an index outside the two selected indices on the first side.

Therefore the complete cardinality enumerator is
\[
\mathcal D_n(x)=\frac{4}{3}n(n-1)(n-2)x^3+\sum_{k=4}^{2n}\binom{2n}{k}x^k.
\]
In particular,
\[
\gamma_t^d(\operatorname{Cr}_n)=3,
\]
and the number of minimum disjunctive-total-dominating sets is
\[
\frac{4}{3}n(n-1)(n-2).
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The restriction \(n\ge3\) is essential to the distance table used below: in a crown graph of this order, matched vertices \(a_i,b_i\) are at distance \(3\), distinct vertices in the same bipartition class are at distance \(2\), and unmatched opposite-side vertices are adjacent. The claim is an exact all-set classification and cardinality enumerator, not merely a minimum-value computation.

## Proof
Fix \(i\). The neighbors of \(a_i\) are precisely the vertices \(b_j\) with \(j\ne i\), while the vertices at distance \(2\) from \(a_i\) are precisely the vertices \(a_j\) with \(j\ne i\). Hence \(a_i\) is disjunctively totally dominated by \(S\) exactly when \(J\setminus\{i\}\ne\varnothing\) or \(|I\setminus\{i\}|\ge2\). Interchanging the two bipartition classes gives the second displayed condition. This proves the local criterion.

Write \(p=|I|\) and \(q=|J|\). If \(p+q\ge4\) and \(p,q\ge2\), each vertex has a selected neighbor on the opposite side except possibly at its deleted-matching index, where the second selected opposite-side index supplies a neighbor. If instead \(q\le1\), then \(p\ge3\). Every vertex on the \(B\)-side has a selected neighbor among the at least three selected \(A\)-vertices, and any \(A\)-vertex lacking a selected opposite-side neighbor has at least two other selected \(A\)-vertices at distance \(2\). The case \(p\le1\) is symmetric. Thus every set of cardinality at least \(4\) satisfies the local criterion.

For cardinality \(3\), the occupancy pairs \((p,q)=(3,0)\) and \((0,3)\) always satisfy the criterion. For \((p,q)=(2,1)\), write \(I=\{i,j\}\) and \(J=\{k\}\). If \(k\in I\), the selected vertex \(a_k\) has neither a selected neighbor nor two selected vertices at distance \(2\), so the set fails. If \(k\notin I\), every local condition holds. The case \((p,q)=(1,2)\) is symmetric. Finally, inspection of the same local criterion for \(p+q\le2\) shows that one of the two displayed alternatives fails for some vertex, so no such set is disjunctive-total-dominating.

There are \(2\binom n3\) one-sided valid triples. For mixed triples, choose the singleton side, its index, and two indices from the remaining \(n-1\) positions, giving \(2n\binom{n-1}{2}\). Their sum is
\[
2\binom n3+2n\binom{n-1}{2}=\frac{4}{3}n(n-1)(n-2).
\]
All larger subsets are valid, so the enumerator and its minimum-degree consequences follow.

## Verification
The standalone script `verify.py` independently constructs \(\operatorname{Cr}_n\), computes all-pairs graph distances by breadth-first search, evaluates the definition of disjunctive total domination directly for every vertex, and compares the result with the stated classification for every subset when \(3\le n\le9\). It also checks every coefficient of the enumerator and the minimum-set count. The replay output is:

`VERIFY_OK n_range=3..9 subset_checks=349504 dtd_sets=348419 criterion_checks=349504 distance_checks=840 coefficient_checks=91 minimum_checks=14 max_order=18`

These finite checks support boundary and implementation verification only; the proof above establishes the statement for all \(n\ge3\).

## Relationship to prior work
The earliest verified public source used for the parameter is Henning and Naicker's arXiv record from 2014-09-05, which defines disjunctive total domination and proves general upper bounds. Their later full manuscript gives the same definition, records classification \(05C69\), and develops general bounds together with exact results for cycles and other special families. Its searchable full text contains no occurrence of “crown” or “complete bipartite.” The special case \(\operatorname{Cr}_3\cong C_6\) means the scalar equality \(\gamma_t^d(\operatorname{Cr}_3)=3\) is already implied by their cycle formula; that special scalar consequence is not treated as original here.

Jamil and Malalay characterize disjunctive and disjunctive-total domination under graph join, corona, and composition operations. A crown graph is instead the direct product \(K_2\times K_n\), so their abstracted operation results do not imply the present all-set classification. Çiftçi studies disjunctive total domination of shadow-distance constructions built from several familiar graph families, including complete bipartite graphs; that construction is different from the crown graph itself. Targeted searches using the aliases “complete bipartite graph minus a perfect matching,” “direct product \(K_2\times K_n\),” and “bipartite Kneser \(H(n,1)\)” found no statement implying the all-set criterion or enumerator above.

## Limitations
The literature comparison cannot exclude a poorly indexed equivalent formulation, especially under product-graph terminology. The accessible record for the join/corona/composition paper supplied its abstract and operation scope rather than a checked full text, so a residual access risk remains, although its stated graph operations do not include direct products. The result is specific to unweighted crown graphs and counts sets only by cardinality. No claim of absolute literature uniqueness is made.

## References
1. M. A. Henning and V. Naicker, *Graphs with Large Disjunctive Total Domination Number*, arXiv:1409.1681v1, first public version 2014-09-05.
2. M. A. Henning and V. Naicker, *Disjunctive Total Domination in Graphs*, arXiv:1410.0187v1; DOI:10.1007/s10878-014-9811-4.
3. F. P. Jamil and R. P. Malalay, *On disjunctive domination in graphs*, DOI:10.2989/16073606.2018.1547797.
4. C. Çiftçi, *Disjunctive Total Domination of Some Shadow Distance Graphs*, DOI:10.33401/fujma.790046.
