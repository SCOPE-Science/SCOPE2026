# All super dominating sets of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge 2\), nonempty parts \(V_1,\ldots,V_r\), and order \(N=\sum_{i=1}^r n_i\). A set \(D\subseteq V(G)\) is super dominating if every vertex \(u\in V(G)\setminus D\) has a witness \(v\in D\) satisfying
\[
N_G(v)\cap (V(G)\setminus D)=\{u\}.
\]
Write \(C=V(G)\setminus D\). Then \(D\) is super dominating if and only if exactly one of the following holds:

1. \(C=\varnothing\);
2. \(|C|=1\);
3. \(C=\{u,w\}\), where \(u\) and \(w\) lie in two distinct partite classes, and both of those partite classes have order at least \(2\).

Consequently, if
\[
E_2=\sum_{\substack{1\le i<j\le r\\ n_i\ge2,\ n_j\ge2}} n_i n_j,
\]
then the complete cardinality enumerator of super dominating sets is
\[
\mathcal S_G(x)=x^N+N x^{N-1}+E_2 x^{N-2}.
\]
In particular, if \(p=|\{i:n_i\ge2\}|\), then
\[
\gamma_{sp}(G)=
\begin{cases}
N-2,&p\ge2,\\
N-1,&p\le1,
\end{cases}
\]
and the number of minimum super dominating sets is \(E_2\) when \(p\ge2\), and \(N\) when \(p\le1\).

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. Complete multipartite means that vertices in different partite classes are adjacent and vertices in the same partite class are nonadjacent. The theorem concerns every super dominating set, not only minimum ones. The empty complement case is included because the defining condition is then vacuous.

## Proof
For a vertex \(v\in V_i\), adjacency in a complete multipartite graph gives
\[
N_G(v)\cap C=C\setminus V_i.
\]
Thus a vertex \(u\in C\) is witnessed by some selected vertex \(v\in V_i\cap D\) exactly when
\[
C\setminus V_i=\{u\}.
\]

If \(C=\varnothing\), the condition is vacuous. If \(|C|=1\), say \(C=\{u\}\), choose any vertex from a different partite class; such a vertex exists because \(r\ge2\), lies in \(D\), and has exactly \(u\) as its neighbor in \(C\).

Now suppose \(|C|=2\). If both omitted vertices lie in the same part, then every selected vertex outside that part is adjacent to both omitted vertices, while vertices inside the part are adjacent to neither. Hence no omitted vertex has a witness. If the two omitted vertices \(u\in V_i\) and \(w\in V_j\) lie in distinct parts, then a witness for \(u\) must lie in \(V_j\cap D\), and a witness for \(w\) must lie in \(V_i\cap D\). Such witnesses exist exactly when \(n_i\ge2\) and \(n_j\ge2\).

Finally suppose \(|C|\ge3\) and that some \(u\in C\) has a witness in \(V_i\). Then \(C\setminus\{u\}\subseteq V_i\), while \(u\notin V_i\). Choose \(w\in C\setminus\{u\}\) and then choose \(t\in C\setminus\{u,w\}\). Any witness for \(w\) would require all of \(C\setminus\{w\}\), including both \(u\) and \(t\), to lie in one partite class. But \(u\) and \(t\) lie in distinct parts, a contradiction. Therefore no super dominating set can omit three or more vertices.

The structural classification is proved. Complements of size \(0\) and \(1\) contribute \(x^N\) and \(N x^{N-1}\), respectively. A valid complement of size \(2\) is obtained by choosing one vertex from each of two distinct non-singleton parts, giving exactly \(E_2\) choices and the term \(E_2x^{N-2}\). The formulas for \(\gamma_{sp}(G)\) and for the number of minimum sets follow by taking the least exponent with nonzero coefficient and its coefficient.

## Verification
The standalone program `verify.py` independently implements the literal witness definition and the structural criterion. It exhaustively checks every nondecreasing complete-multipartite part profile of order from \(2\) through \(10\), every vertex subset for every such profile, every coefficient of the claimed enumerator, the minimum-size formula, the minimum-set count, and the known clique, star, and complete-bipartite boundary cases.

Its replay output is:

`VERIFY_OK profiles=128 subset_checks=64916 criterion_checks=64916 valid_sets=2505 coefficient_checks=339 gamma_checks=128 special_checks=34 max_order=10`

The finite census is a check of the theorem, not a substitute for the symbolic proof above.

## Relationship to prior work
Lemańska, Swaminathan, Venkatakrishnan, and Zuazua introduced super domination and already gave the scalar values for complete graphs, stars, and complete bipartite graphs. Klein, Rodríguez-Velázquez, and Yi later stated the scalar complete-multipartite formula: the super domination number is one less than the order when at most one part has size greater than one, and two less than the order otherwise. That scalar result is fully treated as prior work here.

Ghanbari, Jäger, and Lehtilä later initiated explicit enumeration of minimum super dominating sets and gave the counts for complete graphs, stars, and complete bipartite graphs. Their complete-bipartite count \(mn\) for \(K_{m,n}\) with \(m,n\ge2\) is the two-part special case of the coefficient \(E_2\) above. Their inspected full text contains no complete-multipartite treatment.

The retained contribution is therefore the all-set structural classification for arbitrary complete multipartite graphs, together with the full three-term cardinality enumerator and the arbitrary-part minimum-set count. It does not claim novelty for the scalar domination number or for the previously enumerated clique, star, or biclique special cases.

## Limitations
The result is restricted to connected complete multipartite graphs. The verifier covers orders only through \(10\), while arbitrary order is established by the symbolic argument. The literature comparison cannot rule out every poorly indexed source or equivalent statement under unusual terminology; the closest directly relevant full texts inspected were the 2013 founding work, the later complete-multipartite scalar treatment, and the 2022 enumeration paper.

## References
1. M. Lemańska, V. Swaminathan, Y. B. Venkatakrishnan, and R. Zuazua, *Super dominating sets in graphs*, arXiv:1309.1315, first public 2013-09-05; later published in *Proceedings of the National Academy of Sciences, India Section A*.
2. D. J. Klein, J. A. Rodríguez-Velázquez, and E. Yi, *On the super domination number of graphs*, DOI 10.22049/cco.2019.26587.1122. The inspected full text states the complete-multipartite scalar formula and lists AMS classification 05C69.
3. N. Ghanbari, G. Jäger, and T. Lehtilä, *Super Domination: Graph Classes, Products and Enumeration*, arXiv:2209.01795; later DOI 10.1016/j.dam.2024.01.039.
