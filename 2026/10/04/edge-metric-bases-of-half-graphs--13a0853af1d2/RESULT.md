# Edge metric bases of half graphs
## Finding
For every integer \(p\ge 2\), let \(H_p\) be the half graph with bipartition \(A=\{a_1,\ldots,a_p\}\) and \(B=\{b_1,\ldots,b_p\}\), where \(a_i b_j\) is an edge exactly when \(j\le i\). For \(1\le r<p\), put \(P_r=\{a_r,b_{r+1}\}\). A vertex set is an edge metric basis of \(H_p\) if and only if it contains exactly one vertex from every \(P_r\). Hence
\[
\operatorname{edim}(H_p)=p-1,
\qquad
\#\{\text{edge metric bases of }H_p\}=2^{p-1}.
\]

## Assumptions and scope
All graphs are finite, simple, and connected. For a vertex \(v\) and edge \(xy\), the vertex-edge distance is \(d(v,xy)=\min\{d(v,x),d(v,y)\}\). An edge metric generator is a vertex set whose distance vectors distinguish all edges; a minimum such set is an edge metric basis. The theorem concerns the standard half graph \(H_p\) for \(p\ge2\). The one-edge graph \(H_1\) is excluded because its conventional edge metric dimension is \(1\), not \(0\).

## Proof
Write \(e_{ij}=a_i b_j\) for \(1\le j\le i\le p\). Directly from the nested neighborhoods,
\[
d(a_t,e_{ij})=
\begin{cases}
0,&t=i,\\
1,&t\ne i\text{ and }j\le t,\\
2,&t\ne i\text{ and }j>t,
\end{cases}
\]
and
\[
d(b_t,e_{ij})=
\begin{cases}
0,&t=j,\\
1,&t\ne j\text{ and }t\le i,\\
2,&t\ne j\text{ and }t>i.
\end{cases}
\]

First choose one vertex from every \(P_r\), and call the resulting set \(T\). Suppose \(e_{ij}\) and \(e_{k\ell}\) have the same \(T\)-code. If \(i<k\), inspect the chosen vertex of \(P_i\). If it is \(a_i\), its distances to the two edges are \(0\) and a positive value. If it is \(b_{i+1}\), its distance to \(e_{ij}\) is \(2\), whereas its distance to \(e_{k\ell}\) is \(0\) or \(1\). Thus \(i=k\). If now \(j<\ell\), inspect the chosen vertex of \(P_{\ell-1}\). The choice \(b_\ell\) has distances \(1\) and \(0\), while the choice \(a_{\ell-1}\) has distances \(1\) and \(2\). Thus \(j=\ell\). Therefore every transversal \(T\) is an edge metric generator, so \(\operatorname{edim}(H_p)\le p-1\).

For the lower bound, consider the \(p\) row-star edges \(E_i=a_i b_1\). A landmark \(a_t\) gives distance \(0\) only to \(E_t\) and distance \(1\) to every other \(E_i\). A landmark \(b_j\) with \(j\ge2\) gives distance \(2\) for \(i<j\) and distance \(1\) for \(i\ge j\); \(b_1\) is constant on the family. More generally, on any consecutive subfamily of these row-star edges, each selected \(a_t\) is a single-position marker and each relevant selected \(b_j\) is a one-threshold marker. If there are \(k\) effective landmarks, the threshold landmarks split the ordered edges into intervals; inside each interval, \(s\) single-position markers yield at most \(s+1\) different codes. Summing over the intervals gives at most \(k+1\) codes. Consequently, distinguishing \(m\) consecutive row-star edges requires at least \(m-1\) effective landmarks. Applying this to all \(p\) row-star edges gives \(\operatorname{edim}(H_p)\ge p-1\).

It remains to identify all minimum generators. Let \(S\) have size \(p-1\). In the full row-star family, \(b_1\) is ineffective, so \(b_1\notin S\). By the symmetric column-star family \(F_j=a_p b_j\), the common endpoint \(a_p\) is ineffective, so \(a_p\notin S\). For \(1\le r<p\), let \(z_r=|S\cap P_r|\). Then \(\sum_{r=1}^{p-1}z_r=p-1\).

For \(1\le s\le p-2\), apply the same marker-threshold bound to \(F_1,\ldots,F_{s+1}\). Among vertices of \(S\), the only effective ones are \(a_1,\ldots,a_s\) and \(b_2,\ldots,b_{s+1}\), so
\[
\sum_{r=1}^s z_r\ge s.
\]
For \(2\le s\le p-1\), apply it to \(E_s,\ldots,E_p\). The effective vertices are \(a_s,\ldots,a_{p-1}\) and \(b_{s+1},\ldots,b_p\), so
\[
\sum_{r=s}^{p-1} z_r\ge p-s.
\]
The prefix inequality before \(z_r\) and the suffix inequality after \(z_r\), together with the total sum \(p-1\), imply \(z_r\le1\) for every \(r\); since the \(z_r\) are nonnegative integers summing to \(p-1\), every \(z_r=1\). Thus every minimum generator is exactly a transversal of the pairs \(P_r\). There are \(2^{p-1}\) such transversals.

## Verification
The proof is symbolic and valid for every \(p\ge2\). The accompanying verifier independently constructs \(H_p\), computes all vertex-edge distances by breadth-first search, exhaustively rules out generators of size \(p-2\), and checks that a set of size \(p-1\) resolves the edges exactly when it is a transversal of the stated pairs, for every \(2\le p\le9\). Its replay output is:

`VERIFY_OK p_range=2..9 subset_checks=101762 basis_checks=59278 transversal_checks=510 max_order=18`

The finite computation is corroborative only; it is not used to infer the infinite theorem.

## Relationship to prior work
Kelenc, Tratnik, and Yero introduced edge metric dimension and gave the defining vertex-edge distance formulation, together with exact values for paths, cycles, complete graphs, complete bipartite graphs, and trees. Their public first version is arXiv:1602.00291v1, dated 31 January 2016, and lists AMS 05C12 among its classifications. Full-text searches of that paper for the aliases “half”, “chain”, and “Ferrers” return no occurrence. Its complete-bipartite formula does not imply the half-graph theorem because a nontrivial half graph has nested, non-complete bipartite neighborhoods.

Wei, Yue, and Zhu later characterized connected bipartite graphs of order \(n\) having edge metric dimension \(n-2\). For \(H_p\) with \(p\ge3\), the present value is \(p-1\) on \(2p\) vertices, so that extremal characterization is not applicable; their full text likewise contains no “half”, “chain”, or “Ferrers” occurrence. Focused searches under all three aliases found no published statement classifying all edge metric bases of half graphs.

## Limitations
The theorem is restricted to the canonical half graph and does not claim an edge metric formula for arbitrary chain graphs with repeated twin classes. The literature comparison cannot rule out an obscure equivalent result indexed under substantially different terminology. The exhaustive verification stops at order \(18\); correctness for larger graphs rests on the proof above.

## References
1. A. Kelenc, N. Tratnik, I. G. Yero, “Uniquely identifying the edges of a graph: the edge metric dimension,” arXiv:1602.00291v1; later Discrete Applied Mathematics 251 (2018), 204–220, DOI:10.1016/j.dam.2018.05.052.
2. M. Wei, J. Yue, X. Zhu, “On the edge metric dimension of graphs,” AIMS Mathematics 5(5) (2020), 4459–4465, DOI:10.3934/math.2020286.
