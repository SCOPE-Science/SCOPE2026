# Secure-total-domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge 2\), partite sets \(V_1,\ldots,V_r\), and \(N=\sum_{i=1}^r n_i\). For \(S\subseteq V(G)\), put \(s_i=|S\cap V_i|\) and \(\operatorname{supp}(S)=\{i:s_i>0\}\). Then \(S\) is a secure total dominating set exactly in the following cases:

1. \(|\operatorname{supp}(S)|\ge 3\); or
2. \(\operatorname{supp}(S)=\{i,j\}\) and
\[
(s_i=n_i\text{ or }s_j\ge 2)\quad\text{and}\quad(s_j=n_j\text{ or }s_i\ge 2).
\]

Define the secure-total-domination enumerator
\[
\operatorname{ST}_G(x)=\sum_{S\text{ secure total dominating}}x^{|S|},
\]
and put
\[
P_i(x)=(1+x)^{n_i}-1,
\qquad
U_i(x)=P_i(x)-x^{n_i}.
\]
Then
\[
\operatorname{ST}_G(x)
=(1+x)^N-1-\sum_{i=1}^r P_i(x)
-x\sum_{i=1}^r (N-n_i)U_i(x)
+x^2\sum_{\substack{1\le i<j\le r\\ n_i,n_j\ge2}} n_i n_j.
\]
Thus every cardinality count is explicit from the part sizes.

As a minimum-size corollary, if \(r\ge3\) and \(q=|\{i:n_i=1\}|\), then
\[
\gamma_{st}(G)=
\begin{cases}
2,&q\ge2,\\
3,&q\le1.
\end{cases}
\]
For \(r=2\), writing the part sizes as \(a\le b\),
\[
\gamma_{st}(K_{a,b})=
\begin{cases}
2,&a=b=1,\\
a+b,&a=1<b,\\
3,&a=2,\\
4,&a\ge3.
\end{cases}
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The theorem concerns the standard secure total domination rule: \(S\) is total dominating, and for every \(u\notin S\) there is an adjacent defender \(v\in S\) such that \((S\setminus\{v\})\cup\{u\}\) is again total dominating. The result is an all-cardinality classification and enumerator; it does not claim a named polynomial was previously standard.

The stored source date is \(2008\text{-}01\text{-}01\), the earliest exact calendar day verified in the inspected bibliographic records for a primary paper defining and studying secure total domination. A foundational 2007 article by Benecke, Cockayne, and Mynhardt is known from later references, but an exact public day for that article was not verified here and is not manufactured.

## Proof
A subset \(T\subseteq V(G)\) is total dominating if and only if it meets at least two partite sets. Indeed, if \(T\) lies in one part, every vertex of \(T\) has no neighbor in \(T\). Conversely, if \(T\) meets two parts, then every vertex has a selected neighbor in a different part.

Now let \(S\) be total dominating, so \(|\operatorname{supp}(S)|\ge2\). If \(|\operatorname{supp}(S)|\ge3\), take any \(u\notin S\). Choose a selected neighbor \(v\) outside the part of \(u\). Replacing \(v\) by \(u\) can delete at most one occupied part and can add at most one part. Starting from at least three occupied parts, the replacement still occupies at least two parts, so it remains total dominating. Hence every total dominating set with support at least three is secure.

Suppose instead that \(\operatorname{supp}(S)=\{i,j\}\). If \(u\in V_i\setminus S\), every defender of \(u\) in \(S\) lies in \(V_j\). After replacing a defender, the new set still meets two parts exactly when either \(V_i\) had no omitted vertex to begin with, namely \(s_i=n_i\), or at least two vertices of \(V_j\) were selected, namely \(s_j\ge2\). Thus protection of every omitted vertex of \(V_i\) is equivalent to \(s_i=n_i\) or \(s_j\ge2\). The symmetric argument for omitted vertices of \(V_j\) gives \(s_j=n_j\) or \(s_i\ge2\). If \(u\) lies in an unoccupied third part, replacing any selected neighbor preserves two occupied parts, so there is no further condition. This proves the classification.

For the enumerator, begin with all subsets whose support has size at least two:
\[
(1+x)^N-1-\sum_i P_i(x).
\]
The only insecure sets have support exactly \(\{i,j\}\). For this pair, one obstruction chooses a nonempty proper subset of \(V_i\), counted by \(U_i(x)\), and exactly one vertex of \(V_j\), counted by \(n_jx\). The opposite obstruction contributes \(n_ixU_j(x)\). Their intersection consists exactly of choosing one vertex from each of two non-singleton parts, contributing \(n_in_jx^2\). Therefore the bad polynomial for the pair is
\[
n_jxU_i(x)+n_ixU_j(x)-\mathbf{1}_{n_i,n_j\ge2}n_in_jx^2.
\]
Summing over unordered pairs and using
\[
\sum_{j\ne i}n_j=N-n_i
\]
gives the displayed formula. The piecewise values of \(\gamma_{st}\) follow by reading the least possible support profile from the classification.

## Verification
The standalone verifier `artifacts/verify_secure_total_multipartite.py` independently implements the graph definition, total domination, secure replacement rule, structural classification, and coefficient formula. It exhaustively checks every ordered part-size profile with two through five parts, each part of size at most four, and total order at most nine. Replay produced:

`VERIFY_OK graph_types=297 subset_checks=87788 coefficient_checks=2589 max_order=9`

This finite computation is a stress test only; the proof above establishes the unrestricted theorem.

## Relationship to prior work
Benecke, Cockayne, and Mynhardt introduced secure total domination in 2007. The accessible abstract of that paper describes general properties, paths, and a forest bound; the full text was not accessible from the inspected sources, so possible additional special-class statements remain a bibliographic risk rather than being declared absent.

Klostermeyer and Mynhardt, *Secure domination and secure total domination in graphs*, Discussiones Mathematicae Graph Theory 28 (2008), DOI 10.7151/dmgt.1405, studies general bounds and equality relations between domination parameters. The accessible bibliographic record and abstract do not expose an all-cardinality complete-multipartite classification.

Cabrera Martínez, Estrada-Moreno, and Rodríguez-Velázquez, *Secure Total Domination in Rooted Product Graphs*, Mathematics 8 (2020), DOI 10.3390/math8040600, develops minimum secure-total-domination formulas for rooted products, not an all-set enumerator for complete multipartite graphs.

Surya and Mathew, *On Secure Total Domination Cover Pebbling Number*, Communications in Mathematics and Applications 13 (2022), DOI 10.26713/cma.v13i1.1690, was inspected in full. Its Theorems 4.3 and 4.4 treat a different invariant, the secure-total-domination cover pebbling number, for complete bipartite and complete multipartite graphs. The proof uses particular secure total dominating sets as witnesses; it does not enumerate all secure total dominating sets or give the polynomial above.

## Limitations
The originality comparison is limited by incomplete access to the 2007 foundational article and by the possibility of older special-class results indexed only under alternate terminology. The theorem itself does not depend on the literature search: correctness follows from the support classification proof, with exhaustive small-order replay as a separate check. No independent audit has been performed.

## References
1. S. Benecke, E. J. Cockayne, C. M. Mynhardt, *Secure total domination in graphs*, Utilitas Mathematica 74 (2007), 247–259.
2. W. F. Klostermeyer, C. M. Mynhardt, *Secure domination and secure total domination in graphs*, Discussiones Mathematicae Graph Theory 28 (2008), 267–284. DOI: 10.7151/dmgt.1405.
3. A. Cabrera Martínez, A. Estrada-Moreno, J. A. Rodríguez-Velázquez, *Secure Total Domination in Rooted Product Graphs*, Mathematics 8 (2020), 600. DOI: 10.3390/math8040600.
4. S. Sarah Surya, L. Mathew, *On Secure Total Domination Cover Pebbling Number*, Communications in Mathematics and Applications 13 (2022), 117–127. DOI: 10.26713/cma.v13i1.1690.
