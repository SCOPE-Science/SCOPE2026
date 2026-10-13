# Adjacency bases of crown graphs

## Finding
For every integer \(n\ge3\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and edges \(a_i b_j\) exactly when \(i\ne j\). Write \(P_i=\{a_i,b_i\}\) for the deleted matched pair. Then
\[
\operatorname{adim}(\operatorname{Cr}_n)=n-1.
\]
Here an adjacency resolving set is a set \(S\subseteq V(G)\) whose vectors of truncated distances \(d_2(x,s)=\min\{d(x,s),2\}\), \(s\in S\), are distinct for all vertices \(x\); an adjacency basis is a minimum such set.

Every adjacency basis omits exactly one pair \(P_r\) and contains exactly one vertex from each other pair. If \(n\ge4\), every such one-hole transversal is an adjacency basis, and therefore the number of adjacency bases is
\[
n2^{n-1}.
\]
For \(n=3\), a one-hole transversal is a basis exactly when its two selected vertices are on the same bipartition side. Hence \(\operatorname{Cr}_3\) has exactly six adjacency bases.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The theorem concerns \(\operatorname{Cr}_n\) for \(n\ge3\). The parameter is the ordinary, one-fold adjacency dimension, not the more general \(k\)-adjacency dimension. The term “basis” means minimum cardinality.

For distinct vertices outside an adjacency resolving set \(S\), equality of their truncated-distance vectors is equivalent to equality of their open-neighborhood intersections with \(S\). This observation is used below only as a restatement of the definition.

## Proof
Let \(S\) be an adjacency resolving set.

First suppose two distinct matched pairs \(P_i\) and \(P_j\) are both disjoint from \(S\). For every \(s\in S\), the vertices \(a_i\) and \(a_j\) have the same truncated distance to \(s\): every selected vertex in \(A\) is at truncated distance \(2\) from both, while a selected vertex \(b_k\) has truncated distance \(1\) from both because \(k\notin\{i,j\}\). Thus \(a_i\) and \(a_j\) are not distinguished. Consequently at most one matched pair can be omitted, and
\[
|S|\ge n-1.
\]

Assume now that \(|S|=n-1\). Equality in the preceding counting bound forces exactly one pair, say \(P_r\), to be omitted and exactly one vertex to be chosen from each \(P_i\) with \(i\ne r\).

Consider two unselected vertices on the same side, say \(a_i,a_j\) with \(i\ne j\). At most one of \(P_i,P_j\) is the omitted pair. Hence at least one of \(b_i,b_j\) belongs to \(S\); that selected counterpart has truncated distances \(2\) and \(1\) to \(a_i,a_j\), in one order or the other. Thus every same-side unselected pair is distinguished. The argument for two vertices of \(B\) is symmetric.

It remains to consider an unselected cross pair \(a_i,b_j\). Necessarily \(i\ne j\), because if \(i=j\) then either \(P_i\) is the unique omitted pair, in which case every selected \(a_k\) has truncated distances \(2\) and \(1\) to \(a_i,b_i\), or \(P_i\) is represented and one of the two vertices is selected and therefore distinguished from every other vertex by its zero coordinate.

For \(i\ne j\), a selected vertex \(a_k\) distinguishes \(a_i\) and \(b_j\) unless \(k=j\): its two truncated distances are \(2\) and \(1\) when \(k\ne j\). Symmetrically, a selected \(b_\ell\) distinguishes them unless \(\ell=i\). Therefore the cross pair \(a_i,b_j\) is unresolved exactly when
\[
S\subseteq\{a_j,b_i\}.
\]
If \(n\ge4\), then \(|S|=n-1\ge3\), so this containment is impossible. Thus every one-hole transversal is an adjacency basis. There are \(n\) choices for the omitted pair and two choices in each of the remaining \(n-1\) pairs, giving \(n2^{n-1}\) bases.

When \(n=3\), a one-hole transversal has size two. Such a set fails exactly when it consists of one \(A\)-vertex and one \(B\)-vertex from different matched pairs: if it is \(\{a_j,b_i\}\) with \(i\ne j\), the unselected cross pair \(a_i,b_j\) has the same truncated-distance vector. The valid one-hole transversals are therefore precisely the three two-element subsets of \(A\) and the three two-element subsets of \(B\), for a total of six. This also attains the lower bound \(n-1=2\).

## Verification
A standalone checker in `verify.py` constructs \(\operatorname{Cr}_n\), evaluates the truncated metric \(d_2\), exhausts every subset below the claimed optimum, and compares every subset of size \(n-1\) with the structural classifier for \(3\le n\le9\). Its expected terminal line is:

`VERIFY_OK n_range=3..9 subset_checks=141658 basis_checks=59274 bases=4086 max_order=18`

This finite computation is corroborative only. The theorem for all \(n\ge3\) follows from the symbolic proof above.

## Relationship to prior work
Jannesari and Omoomi introduced adjacency metric dimension in their study of lexicographic products. Their first public arXiv version is dated 17 March 2011. The inspected arXiv text introduces the parameter but contains no occurrence of “crown” or “complete bipartite.”

Estrada-Moreno, Ramírez-Cruz, and Rodríguez-Velázquez developed the \(k\)-adjacency dimension using the same truncated metric \(d_2\), with general structural results and formulas for several families. Their searchable full text mentions complete bipartite graphs only as a basic twin-rich example and contains no occurrence of “crown”; it does not state the matching-deleted complete-bipartite basis classification above.

Later adjacency-dimension literature gives general bounds and formulas for additional classes, but focused searches under “crown graph,” “complete bipartite graph minus a perfect matching,” “one-factor deletion,” and “bipartite Kneser graph” did not locate a statement implying the theorem or its exact basis count.

## Limitations
The theorem classifies minimum adjacency resolving sets only; it does not enumerate all larger adjacency resolving sets or treat \(k\)-adjacency bases for \(k>1\). The exhaustive verifier stops at \(n=9\) and is not an infinite certificate. Literature coverage can miss an unindexed source using uncommon terminology; this remains the principal originality risk.

## References
1. M. Jannesari and B. Omoomi, *The Metric Dimension of Lexicographic Product of Graphs*, arXiv:1103.3336, first public version 17 March 2011; Discrete Mathematics 312 (2012), DOI 10.1016/j.disc.2012.07.025.
2. A. Estrada-Moreno, Y. Ramírez-Cruz, and J. A. Rodríguez-Velázquez, *On the adjacency dimension of graphs*, arXiv:1501.04647, first public version 19 January 2015; Applicable Analysis and Discrete Mathematics 10 (2016), DOI 10.2298/AADM151109022E.
3. S. Bermudo, J. M. Rodríguez, J. A. Rodríguez-Velázquez, and J. M. Sigarreta, *The adjacency dimension of graphs*, Ars Mathematica Contemporanea 22 (2022), DOI 10.26493/1855-3974.2496.07a.
