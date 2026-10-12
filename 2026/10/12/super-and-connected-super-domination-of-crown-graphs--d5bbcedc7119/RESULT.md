# Super and connected-super domination of crown graphs
## Finding
For every integer \(n\ge4\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where
\[
M=\{a_i b_i:1\le i\le n\}
\]
is the deleted perfect matching.

Then
\[
\gamma_{\mathrm{sp}}(\operatorname{Cr}_n)=\gamma_{\mathrm{csp}}(\operatorname{Cr}_n)=2n-4.
\]

More strongly, the minimum super dominating sets and the minimum connected super dominating sets are the same family. They are precisely
\[
S=V(\operatorname{Cr}_n)\setminus\{a_i,a_j,b_k,b_\ell\},
\]
where \(\{i,j\}\) and \(\{k,\ell\}\) are disjoint two-element subsets of \(\{1,\ldots,n\}\). Hence the exact number of minimum sets is
\[
\binom n2\binom{n-2}{2}.
\]

In particular, deleting one perfect matching from \(K_{n,n}\) lowers the known super domination number from \(2n-2\) to \(2n-4\), while every new minimum set is automatically connected.

## Assumptions and scope
A set \(S\subseteq V(G)\) is super dominating if for every \(u\in V(G)\setminus S\) there exists \(v\in S\) such that
\[
N(v)\cap(V(G)\setminus S)=\{u\}.
\]
The minimum size of such a set is \(\gamma_{\mathrm{sp}}(G)\).

A connected super dominating set is a super dominating set whose induced subgraph \(G[S]\) is connected, and \(\gamma_{\mathrm{csp}}(G)\) is the corresponding minimum cardinality.

The complete classification is stated for \(n\ge4\). The boundary \(\operatorname{Cr}_3\cong C_6\) has \(\gamma_{\mathrm{sp}}=\gamma_{\mathrm{csp}}=4\), but it has fifteen minimum super dominating sets and only six connected ones, so the rigidity statement genuinely starts at \(n=4\).

## Proof
Let \(S\) be a super dominating set and put
\[
U=V(\operatorname{Cr}_n)\setminus S,
\qquad
U_A=U\cap A,
\qquad
U_B=U\cap B.
\]

We first show
\[
|U_A|\le2,
\qquad
|U_B|\le2.
\tag{1}
\]
Suppose \(a_i\in U_A\). A witness for \(a_i\) must lie in \(B\), say \(b_j\in S\), and must satisfy
\[
N(b_j)\cap U=\{a_i\}.
\]
In the crown graph, \(b_j\) is adjacent to every vertex of \(A\) except \(a_j\), and has no neighbors in \(B\). Therefore every vertex of \(U_A\setminus\{a_i\}\) must equal \(a_j\). Hence \(|U_A|\le2\). The argument for \(U_B\) is symmetric. Thus
\[
|U|\le4,
\]
and every super dominating set satisfies
\[
|S|\ge2n-4.
\tag{2}
\]

Now choose disjoint index pairs
\[
I=\{i,j\},\qquad J=\{k,\ell\},\qquad I\cap J=\varnothing,
\]
and let
\[
U=\{a_i,a_j,b_k,b_\ell\},
\qquad
S=V\setminus U.
\]
Then \(b_j\) witnesses \(a_i\), \(b_i\) witnesses \(a_j\), \(a_\ell\) witnesses \(b_k\), and \(a_k\) witnesses \(b_\ell\). The disjointness of \(I\) and \(J\) ensures that all four witnesses lie in \(S\). Hence \(S\) is super dominating and has size \(2n-4\). Together with (2),
\[
\gamma_{\mathrm{sp}}(\operatorname{Cr}_n)=2n-4.
\]

Equality in (2) forces
\[
|U_A|=|U_B|=2.
\]
Write
\[
U_A=\{a_i,a_j\},
\qquad
U_B=\{b_k,b_\ell\}.
\]
For \(a_i\), a witness \(b_r\) must avoid adjacency to the other omitted vertex \(a_j\). The only such vertex in \(B\) is \(b_j\), so \(b_j\in S\). Thus \(j\notin\{k,\ell\}\). Repeating this for \(a_j\) gives \(i\notin\{k,\ell\}\). Hence
\[
\{i,j\}\cap\{k,\ell\}=\varnothing.
\]
The same condition is sufficient by the construction above, so this classifies every minimum super dominating set.

It remains to prove connectedness. For \(n=4\), the two omitted index pairs partition \(\{1,2,3,4\}\). The selected \(A\)-indices equal the omitted \(B\)-indices and vice versa, so every selected cross-pair has distinct indices. Therefore
\[
\operatorname{Cr}_4[S]\cong K_{2,2},
\]
which is connected.

For \(n\ge5\), each side of \(S\) contains \(n-2\ge3\) vertices. Any selected \(a_p\) is adjacent to every selected \(b_q\) except possibly \(b_p\). If that exceptional nonedge occurs, choose a selected \(b_r\) with \(r\ne p\) and then a selected \(a_s\) with \(s\notin\{p,r\}\). This gives a path
\[
a_p-b_r-a_s-b_p.
\]
Thus all selected vertices lie in one connected component. Every minimum super dominating set is connected, so
\[
\gamma_{\mathrm{csp}}(\operatorname{Cr}_n)=\gamma_{\mathrm{sp}}(\operatorname{Cr}_n)=2n-4.
\]

Finally, choose the omitted two-set in \(A\) and then a disjoint omitted two-set in \(B\). This gives exactly
\[
\binom n2\binom{n-2}{2}
\]
minimum sets.

## Verification
The included checker evaluates the definitions directly. It exhaustively tests every nonempty vertex subset for \(3\le n\le7\), a total of \(21{,}819\) subsets. For every \(n\ge4\) in this range, both the ordinary and connected-super minimum layers agree exactly with the disjoint omitted-pair classification. The checker also directly tests \(7{,}798\) predicted minimum constructions across the range \(4\le n\le50\), with exhaustive construction coverage through \(n=12\) and representative boundary patterns thereafter.

The finite checks are corroborative only. The arbitrary-order lower bound and the equality classification follow from the witness-neighborhood proof above.

## Relationship to prior work
The 2017 primary study of super domination records the known complete-bipartite value
\[
\gamma_{\mathrm{sp}}(K_{r,t})=r+t-2
\]
when both parts have size at least two, and develops general bounds together with corona and Cartesian-product results. Its inspected full text contains no crown-graph treatment.

Connected super domination was introduced as the super-domination condition plus connectivity of the induced selected subgraph. The 2018 connected-super paper treats common graphs and join, corona, lexicographic-product, and Cartesian-product constructions. Targeted full-text inspection found no occurrence of “crown” or “complete bipartite”.

A 2022 preprint, later published in 2024, revisits super domination, graph classes, products, and enumeration. Its full text explicitly lists the complete bipartite value among previous results and then focuses on neighborhood coronas, clique gluings, Hajós sums, and enumeration for selected families. Targeted inspection found no crown or perfect-matching-deletion treatment.

The crown graph is not complete multipartite for \(n\ge3\), because cross-part nonedges depend on the matched index. Therefore complete-multipartite super-domination formulas do not subsume the theorem. Likewise, the known value for \(K_{n,n}\) does not imply the behavior after deleting a perfect matching, since super domination is not monotone under edge deletion.

## Limitations
The minimum-set classification starts at \(n=4\). At \(n=3\), ordinary and connected-super domination still have value \(4\), but their minimum families differ.

The theorem treats exactly one deleted perfect matching from \(K_{n,n}\); it does not classify arbitrary matching deletions or arbitrary bipartite graphs.

Only the minimum layer is classified. The complete polynomial enumerating all super dominating sets is not determined here.

Search coverage cannot exclude a differently phrased or non-indexed treatment of the same crown family.

## References
1. D. J. Klein, J. A. Rodríguez-Velázquez, E. Yi, “On the super domination number of graphs,” arXiv:1705.00928v1, first public version 2 May 2017; later published in Discrete Applied Mathematics 263 (2019), 201–216.
2. R. F. Liguarda, S. R. Canoy Jr., “Connected Super Domination in Graphs,” Advances and Applications in Discrete Mathematics 19(3) (2018), 273–288, DOI 10.17654/DM019030273.
3. N. Ghanbari, G. Jäger, T. Lehtilä, “Super Domination: Graph Classes, Products and Enumeration,” arXiv:2209.01795v1, first public version 5 September 2022; later published in Discrete Applied Mathematics 349 (2024), 8–24, DOI 10.1016/j.dam.2024.01.039.
