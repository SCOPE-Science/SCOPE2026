# Exact non-CIS-pair count for matching-deleted complete bipartite graphs
## Finding
Let \(a,b\ge 1\), let \(0\le t\le \min\{a,b\}\), and let \(G_{a,b,t}=K_{a,b}-M_t\), where \(M_t\) is a matching of size \(t\). A non-CIS pair is a pair \((C,S)\) in which \(C\) is a maximal clique, \(S\) is a maximal stable set, and \(C\cap S=\varnothing\). If \(\eta(G)\) counts non-CIS pairs, then
\[
\eta(G_{a,b,t})=t\bigl((a-1)(b-1)-t+1\bigr).
\]
Therefore \(G_{a,b,t}\) is CIS if and only if \(t=0\), or \(\min\{a,b\}=1\), or \((a,b,t)=(2,2,2)\). It is almost CIS if and only if \((a,b,t)=(2,2,1)\), which is the path on four vertices. For the crown graph \(\operatorname{Cr}_n=K_{n,n}-M_n\), \(n\ge2\),
\[
\eta(\operatorname{Cr}_n)=n(n-1)(n-2).
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. Write the bipartition as \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\), with deleted matching edges \(a_i b_i\) for \(1\le i\le t\). Maximal means inclusion-maximal, not maximum. The count treats a maximal clique and a maximal stable set as a pair of sets; there is no quotient by automorphisms.

## Proof
Because \(G_{a,b,t}\) is bipartite, every maximal clique is either a surviving edge or, when present, a singleton isolated vertex. For each deleted edge \(a_i b_i\), the two-set
\[
S_i=\{a_i,b_i\}
\]
is stable. It is maximal: any other vertex of \(A\) is adjacent to \(b_i\), and any other vertex of \(B\) is adjacent to \(a_i\). Apart from the two bipartition sides when they are maximal, these \(S_i\) are all maximal stable sets that use vertices from both sides. Indeed, a stable set meeting both sides can contain only a nonadjacent cross-part pair, and the only such pairs are the deleted matching pairs.

A bipartition side, when maximal, meets every surviving edge. A singleton isolated maximal clique meets every maximal stable set, because every maximal stable set contains every isolated vertex. Hence every non-CIS pair consists of a surviving edge and one of the sets \(S_i\).

Fix \(i\). A surviving edge is disjoint from \(S_i\) exactly when its endpoints lie in \(A\setminus\{a_i\}\) and \(B\setminus\{b_i\}\). There are \((a-1)(b-1)\) possible cross-pairs there, and exactly \(t-1\) of them are the other deleted matching edges. Thus precisely
\[
(a-1)(b-1)-(t-1)=(a-1)(b-1)-t+1
\]
maximal cliques are disjoint from \(S_i\). Summing over the \(t\) deleted pairs proves the formula.

The graph is CIS exactly when this nonnegative count is zero. If \(t=0\), this is immediate. If \(t>0\) and \(\min\{a,b\}=1\), then necessarily \(t=1\) and the factor in parentheses is zero. Otherwise assume \(2\le a\le b\). The zero condition is \((a-1)(b-1)=t-1\). Since \(t\le a\), the right side is at most \(a-1\), whereas the left side is at least \(a-1\); equality forces \(b=2\), hence \(a=2\) and \(t=2\). This gives the CIS classification.

Almost CIS means \(\eta=1\). Since the displayed formula is a product of nonnegative integers and \(t\ge1\), this forces \(t=1\) and \((a-1)(b-1)=1\), hence \(a=b=2\). Finally, putting \(a=b=t=n\) yields \(n((n-1)^2-n+1)=n(n-1)(n-2)\).

## Verification
The accompanying `verify.py` constructs \(G_{a,b,t}\) directly, enumerates every nonempty vertex subset, independently tests whether it is an inclusion-maximal clique or inclusion-maximal stable set, counts all disjoint maximal-clique/maximal-stable-set pairs, and compares that count with the theorem. It checks every \(1\le a,b\le5\) and every \(0\le t\le\min\{a,b\}\), and separately checks the crown specialization for \(2\le n\le6\). The final replay reports:

`ALL CHECKS PASSED; parameter_cases=80; subset_candidates_per_family_sum=17672; a,b_range=1..5; crown_n_range=2..6`

This finite enumeration is a stress test only. The theorem for arbitrary parameters follows from the analytic classification of maximal cliques and maximal stable sets above.

## Relationship to prior work
Tao, Yang, and Zang define CIS graphs by the intersection of every maximal clique with every maximal stable set and prove that recognizing CIS graphs is coNP-complete. Their preprint was first public on 2026-08-11 and lists primary MSC 05C69. This makes exact certificate structure on natural graph families a pertinent tractable complement to the general recognition result.

Wu, Zang, and Zhang define a non-CIS pair and prove that a graph is almost CIS exactly when it is a split graph with a unique split partition. The present theorem is consistent with that global characterization: among matching-deleted complete bipartite graphs, the unique almost-CIS case is \(K_{2,2}\) with one matching edge deleted, namely the four-vertex path. This consequence is not claimed as independent of their theorem; the new content is the exact defect count throughout the three-parameter family and its resulting CIS boundary.

Andrade, Boros, and Gurvich develop foundational necessary and sufficient conditions for CIS graphs. The inspected full text does not contain the phrase “complete bipartite,” and targeted searches did not locate an exact non-CIS-pair enumeration for \(K_{a,b}-M_t\). A general known fact that a connected triangle-free CIS graph is complete bipartite can recover part of the zero-versus-nonzero boundary in connected cases, but it neither counts non-CIS pairs nor handles the full disconnected boundary by itself.

## Limitations
The result concerns only deletion of a matching from a complete bipartite graph; arbitrary deleted edge sets are not classified. The recent 2026 recognition preprint's official abstract and metadata were available, but its full text could not be retrieved through the accessible arXiv or open-access routes during this check; no whole-document noncoverage claim is based on that inaccessible text. The originality assessment therefore retains a residual risk that an uninspected passage of that preprint, or an unindexed source, contains the same family formula. The finite verifier does not prove the infinite theorem.

## References
1. R. Tao, M. Yang, and W. Zang, “How Difficult Is It to Recognize CIS Graphs?”, arXiv:2608.11289, first public 2026-08-11.
2. Y. Wu, W. Zang, and C.-Q. Zhang, “A Characterization of Almost CIS Graphs”, SIAM Journal on Discrete Mathematics 23 (2009), 749–753, DOI: 10.1137/080723739.
3. D. V. Andrade, E. Boros, and V. Gurvich, “On graphs whose maximal cliques and stable sets intersect”, RUTCOR Research Report RRR 17-2006; expanded chapter version in Optimization Problems in Graph Theory (2018).
