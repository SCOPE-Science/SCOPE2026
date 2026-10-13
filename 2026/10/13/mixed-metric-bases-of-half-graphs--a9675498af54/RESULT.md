# Mixed metric bases of half graphs
## Finding
For every integer \(n\ge2\), let \(H_n\) be the half graph with bipartition
\[
A=\{a_1,\ldots,a_n\},
\qquad
B=\{b_1,\ldots,b_n\},
\]
and edge set
\[
E(H_n)=\{a_i b_j:1\le i\le j\le n\}.
\]
Then
\[
\operatorname{mdim}(H_n)=n.
\]

More strongly, the mixed metric bases are exactly
\[
S=\{a_n,b_1\}\cup\{s_i:2\le i\le n-1,\ s_i\in\{a_i,b_i\}\}.
\]
Thus every basis contains the two opposite leaves \(a_n\) and \(b_1\), contains exactly one vertex from every internal diagonal pair \(\{a_i,b_i\}\), and contains neither \(a_1\) nor \(b_n\). Consequently the number of mixed metric bases is
\[
2^{n-2}.
\]

## Assumptions and scope
Graphs are finite, simple, connected, and undirected. For a vertex \(s\) and an edge \(uv\), put
\[
d(s,uv)=\min\{d(s,u),d(s,v)\}.
\]
A set \(S\subseteq V(G)\) is a mixed metric generator when every two distinct elements of \(V(G)\cup E(G)\) have different distance vectors to \(S\). The mixed metric dimension is the minimum cardinality of such a set.

The half graph convention used here is \(a_i b_j\in E(H_n)\) exactly when \(i\le j\).

## Proof
First, two landmarks are forced in every mixed metric generator. Compare the vertex \(b_n\) with the incident edge \(a_n b_n\). Every vertex except \(a_n\) has the same distance to these two elements, while \(a_n\) distinguishes them. Hence
\[
a_n\in S.
\]
Symmetrically, comparison of \(a_1\) with \(a_1b_1\) forces
\[
b_1\in S.
\tag{1}
\]

For \(2\le i\le n-1\), define
\[
U_i=\{a_2,\ldots,a_i,b_2,\ldots,b_i\}.
\]
Consider the \(i\) elements
\[
x_1=a_1,
\qquad
x_k=a_1b_k\quad(2\le k\le i).
\]
Every landmark outside \(U_i\) has one common distance to all of \(x_1,\ldots,x_i\). For \(a_t\in U_i\), its distances along the ordered list are \(2\) before index \(t\) and \(1\) from index \(t\) onward. Thus any selected \(a_t\) is a threshold coordinate. For \(b_t\in U_i\), the distance is \(0\) only on \(x_t\) and \(1\) on all other listed elements, so it is a singleton coordinate.

If \(p\) selected vertices of \(U_i\) lie in the \(A\)-side and \(q\) lie in the \(B\)-side, the \(p\) threshold coordinates partition the ordered list into at most \(p+1\) common-code classes. Each singleton coordinate can split at most one existing class, increasing the number of classes by at most one. Since all \(i\) elements must have distinct mixed codes,
\[
|S\cap U_i|=p+q\ge i-1.
\tag{2}
\]

There is a symmetric suffix inequality. For \(2\le i\le n-1\), put
\[
V_i=\{a_i,\ldots,a_{n-1},b_i,\ldots,b_{n-1}\}
\]
and consider
\[
y_k=a_kb_n\quad(i\le k\le n-1),
\qquad
y_n=b_n.
\]
Landmarks outside \(V_i\) have a common distance to this entire list. Inside \(V_i\), selected \(b_t\)'s give threshold coordinates and selected \(a_t\)'s give singleton coordinates. The same class-counting argument yields
\[
|S\cap V_i|\ge n-i.
\tag{3}
\]

Taking \(i=n-1\) in (2), and using the two forced vertices from (1), gives
\[
|S|\ge n.
\tag{4}
\]

Now suppose \(|S|=n\). Then exactly \(n-2\) selected vertices lie among the internal diagonal pairs. Write
\[
z_t=|S\cap\{a_t,b_t\}|
\qquad(2\le t\le n-1).
\]
From (2) and (3),
\[
\sum_{j=2}^{t}z_j\ge t-1,
\qquad
\sum_{j=t}^{n-1}z_j\ge n-t.
\]
Adding these inequalities and using \(\sum_{j=2}^{n-1}z_j=n-2\) gives
\[
n-2+z_t\ge n-1,
\]
so \(z_t\ge1\) for every internal index. There are exactly \(n-2\) such indices and exactly \(n-2\) selected internal vertices, hence
\[
z_t=1
\qquad(2\le t\le n-1).
\tag{5}
\]
No room remains for \(a_1\) or \(b_n\). This proves necessity of the displayed basis form.

It remains to prove sufficiency. Fix any set of that form. The two mandatory landmarks \(b_1\) and \(a_n\) already separate the element types except for four natural collision families: internal vertices on the same side, internal edges, the pairs \(a_1\) versus \(a_1b_j\) with \(2\le j\le n-1\), and the pairs \(b_n\) versus \(a_i b_n\) with \(2\le i\le n-1\).

For two \(A\)-vertices \(a_i,a_j\) with \(i<j\), the selected vertex at index \(i\) distinguishes them: choosing \(a_i\) gives distances \(0\) and \(2\), while choosing \(b_i\) gives distances \(1\) and \(3\). For two \(B\)-vertices \(b_i,b_j\) with \(i<j\), the selected vertex at index \(j\) distinguishes them symmetrically.

For two edges \(a_i b_j\) and \(a_k b_\ell\), if \(i<k\), the selected vertex at index \(i\) distinguishes them. If \(i=k\) and \(j<\ell\), the selected vertex at index \(\ell\) distinguishes them. These statements also cover the endpoint indices using the forced landmarks \(b_1\) and \(a_n\).

Finally, the selected vertex at index \(j\) distinguishes \(a_1\) from \(a_1b_j\), and the selected vertex at index \(i\) distinguishes \(b_n\) from \(a_i b_n\). Hence every pair of distinct vertices or edges is resolved. Therefore every displayed set is a mixed metric generator of size \(n\), which together with (4) proves the theorem. For \(n=2\), the internal range is empty and the forced set \(\{a_2,b_1\}\) directly resolves all seven elements.

## Verification
The included verifier constructs \(H_n\) directly for every \(2\le n\le8\), computes all vertex distances by breadth-first search, and derives the distance vector of every vertex and edge.

For each \(n\), it exhaustively checks every vertex subset of size at most \(n\). It verifies that no smaller subset is mixed resolving and that the size-\(n\) mixed resolving sets are exactly the forced-endpoint diagonal transversals in the theorem.

## Relationship to prior work
Mixed metric dimension was introduced in 2016. The foundational paper studies the structure of mixed generators and determines exact values for cycles, complete bipartite graphs, trees, and grid graphs. Targeted full-text searches of that source found no occurrence of half graphs, chain graphs, or Ferrers graphs.

A 2021 paper devoted to metric dimension and related questions for chain graphs addresses ordinary metric dimension and a restricted threshold-dimension construction. The accessible abstract does not state a mixed metric result. Its full article text was not accessible in the inspected route, so this remains a bounded residual literature risk rather than evidence of coverage.

Targeted searches under the aliases half graph, chain graph, bipartite chain graph, Ferrers graph, and difference graph did not locate a published mixed-metric formula or basis classification. Related ordinary, strong, and edge-metric results for chain or half graphs do not imply the mixed theorem because mixed resolution must additionally distinguish vertices from edges.

## Limitations
The theorem concerns the canonical half graph, not arbitrary chain graphs with repeated neighborhood classes. It gives every minimum mixed generator but does not enumerate all nonminimum mixed generators.

The finite computation through \(n=8\) is corroborative only. The arbitrary-parameter theorem follows from the forced-endpoint argument, the prefix and suffix code-count inequalities, and the explicit basis verification.

The full text of the 2021 chain-graph metric-dimension article was not available through the inspected route; only its bibliographic record and abstract were read. A differently phrased or non-indexed mixed-metric treatment therefore remains possible.

## References
1. A. Kelenc, D. Kuziak, A. Taranenko, I. G. Yero, “Mixed metric dimension of graphs,” arXiv:1611.04292v1, 14 November 2016; Applied Mathematics and Computation 314 (2017), 429–438, DOI 10.1016/j.amc.2017.07.027.
2. K. Arathi Bhat, S. Hanif, G. Sudhakara, “Metric dimension and its variations of chain graphs,” Proceedings of the Jangjeon Mathematical Society 24 (2021), 809–821, DOI 10.17777/pjms2021.24.3.309.
