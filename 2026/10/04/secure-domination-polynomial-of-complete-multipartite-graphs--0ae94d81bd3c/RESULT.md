# Secure domination polynomial of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge2\), with partite sets \(A_1,\ldots,A_r\), where \(|A_i|=n_i\), and put \(N=\sum_i n_i\). For a set \(S\subseteq V(G)\), write \(s_i=|S\cap A_i|\), \(t_i=n_i-s_i\), and \(\operatorname{supp}(S)=\{i:s_i>0\}\).

A set \(S\) is secure dominating if and only if exactly one of the following support conditions holds:

1. \(|\operatorname{supp}(S)|\ge3\).
2. \(\operatorname{supp}(S)=\{i,j\}\) and
   \[
   (t_i\le1\text{ or }s_j\ge2)\quad\text{and}\quad(t_j\le1\text{ or }s_i\ge2).
   \]
3. \(\operatorname{supp}(S)=\{i\}\), \(S=A_i\), and either \(n_i\ge2\) or every part of \(G\) is a singleton.

Define
\[
F_i(x)=(1+x)^{n_i}-1,
\qquad
H_i(x)=\sum_{a=1}^{n_i-2}\binom{n_i}{a}x^a,
\]
where \(H_i(x)=0\) when \(n_i\le2\). Let \(\epsilon_{ij}=1\) when \(n_i,n_j\ge3\), and \(\epsilon_{ij}=0\) otherwise. Finally, set
\[
U(x)=\sum_{i:n_i\ge2}x^{n_i},
\]
except that when every part is a singleton set \(U(x)=rx\).

Then the secure domination polynomial \(D_s(G;x)=\sum_{S\text{ secure dominating}}x^{|S|}\) is
\[
\begin{aligned}
D_s(G;x)=\;&U(x)
+\left((1+x)^N-1-\sum_iF_i(x)-\sum_{i<j}F_i(x)F_j(x)\right)\\
&+\sum_{i<j}\left(F_i(x)F_j(x)-n_jxH_i(x)-n_ixH_j(x)+\epsilon_{ij}n_in_jx^2\right).
\end{aligned}
\]
The first line after \(U(x)\) counts secure sets meeting at least three parts, and each summand in the last line counts secure sets meeting exactly two specified parts. Thus the formula is coefficientwise combinatorial rather than a recurrence.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. Complete multipartite means vertices in distinct partite sets are adjacent and vertices within one part are nonadjacent. A dominating set \(S\) is secure if for every \(u\notin S\) there exists a neighbor \(v\in S\) such that \((S\setminus\{v\})\cup\{u\}\) is again dominating.

The theorem concerns the full family of secure dominating sets, not only minimum ones. The previously known secure domination number of complete multipartite graphs is treated as prior work and is not the originality-bearing claim. The displayed polynomial uses the later standard terminology “secure domination polynomial”; the structural classification itself is independent of that terminology.

## Proof
First note the elementary domination criterion. If \(S\) meets at least two parts, then every vertex outside \(S\) has a neighbor in \(S\), so \(S\) dominates. If \(S\) meets exactly one part \(A_i\), then an omitted vertex of \(A_i\) has no neighbor in \(S\); hence such a set dominates exactly when \(S=A_i\).

Assume first that \(S\) meets at least three parts. Let \(u\notin S\) lie in \(A_i\). Any selected vertex outside \(A_i\) is adjacent to \(u\). Choose one such defender \(v\). After replacing \(v\) by \(u\), at least two parts remain represented: if the part of \(v\) loses its last selected vertex, there is still another represented part distinct from \(A_i\); otherwise the support obviously remains of size at least two. By the domination criterion, the exchanged set dominates. Hence every set meeting at least three parts is secure.

Now suppose \(S\) meets exactly two parts \(A_i\) and \(A_j\). Consider an omitted vertex \(u\in A_i\). Its defenders must lie in \(A_j\). If \(s_j\ge2\), removing one defender leaves both \(A_i\) and \(A_j\) represented, so the exchanged set dominates. If \(s_j=1\), then after the exchange the set lies entirely in \(A_i\); by the domination criterion it dominates exactly when the exchange fills \(A_i\), equivalently when \(t_i=1\). If \(t_i=0\) there is no omitted vertex in \(A_i\), so the condition is vacuous. Therefore every omitted vertex of \(A_i\) is defendable exactly when \(t_i\le1\) or \(s_j\ge2\). Interchanging \(i\) and \(j\) gives the second condition. Vertices in every third part are adjacent to all selected vertices, and replacing a selected vertex from either represented part by such a vertex leaves at least two parts represented. This proves the two-part criterion.

Finally suppose \(S=A_i\) is a one-part dominating set. If \(n_i\ge2\), then for any \(u\notin A_i\), exchanging \(u\) with any \(v\in A_i\) leaves at least one vertex of \(A_i\) together with \(u\), so the exchanged set meets two parts and dominates. If \(n_i=1\), the exchange leaves a singleton \(\{u\}\), which dominates precisely when the part containing \(u\) is also a singleton. Thus every attack is defendable exactly when all parts are singletons.

It remains to count. The polynomial \(F_i(x)\) counts nonempty choices from \(A_i\). Hence all subsets meeting at least three parts contribute
\[
(1+x)^N-1-\sum_iF_i(x)-\sum_{i<j}F_i(x)F_j(x).
\]
The one-part secure sets contribute \(U(x)\). For a fixed pair \(i<j\), all nonempty choices contribute \(F_i(x)F_j(x)\). A choice fails the first two-part condition exactly when it selects one vertex of \(A_j\) and leaves at least two vertices of \(A_i\), contributing \(n_jxH_i(x)\). The symmetric failures contribute \(n_ixH_j(x)\). Their intersection occurs exactly when \(n_i,n_j\ge3\) and one vertex is chosen in each part, contributing \(n_in_jx^2\). Inclusion-exclusion therefore gives the displayed pair summand and completes the proof.

## Verification
The standalone verifier constructs every complete multipartite graph whose part sizes form an integer partition of orders \(2\) through \(10\), directly tests the definition of secure domination for every vertex subset, independently evaluates the support characterization, and compares the full coefficient vector with the closed polynomial. The final package replay reports `VERIFY_OK graph_types=128 subsets=64916 classification_checks=64916 coefficient_checks=1179 max_order=10`.

The finite computation is a boundary check, not the proof of the unrestricted theorem. The proof above establishes the statement for arbitrary positive part sizes and arbitrary \(r\ge2\).

## Relationship to prior work
Secure domination was introduced by Cockayne, Favaron, and Mynhardt in 2003. Public metadata for that paper states the definition and later literature records that it obtained exact secure domination numbers for complete multipartite graphs. The accessible record located during this review does not provide the full paper text.

Burger et al., *Finite Order Domination in Graphs*, develops higher-order secure domination. Its openly available full text states the standard one-move specialization, proves exact formulas for complete bipartite graphs, and explicitly records the known one-move value for \(K_{p,q}\); its conclusion lists broader complete multipartite higher-order parameter values as future scope. It does not enumerate all secure dominating sets or give the polynomial above. The complete-bipartite minimum-number specialization is therefore prior coverage, not novelty evidence for the present claim.

Gipson and Subha later study secure domination polynomials for cycles, confirming that the all-cardinality enumerator is a named object. Their article concerns cycles rather than complete multipartite graphs. Targeted searches under secure domination, guard exchange, finite-order domination, complete multipartite graphs, and polynomial/enumerator terminology found no prior statement equivalent to the support classification or the displayed all-coefficient formula. This absence is not treated by itself as proof of novelty.

## Limitations
The result is specific to ordinary secure domination on complete multipartite graphs; it does not address secure total domination, higher-order security, co-secure domination, or the distinct security notion based on simultaneous attacks. The exhaustive checker is finite, through order \(10\), while the unrestricted theorem rests on the symbolic proof. The full text of the 2003 foundational complete-multipartite source was not available from the lawful sources located during review, so a residual bibliographic risk remains that it contains an unpublished-in-indexing structural lemma stronger than the later summaries indicate. The exact-day archival anchor used in metadata is 2004-05-31, the earliest exact public date verified in the inspected sources; earlier 2003 records exposed only month or volume-level dating, and no day was invented.

## References
1. A. P. Burger, E. J. Cockayne, W. R. Gründlingh, C. M. Mynhardt, J. H. van Vuuren, and W. Winterbach, *Finite Order Domination in Graphs*, Journal of Combinatorial Mathematics and Combinatorial Computing 49 (2004), 159–175. Public article page dated 2004-05-31: https://combinatorialpress.com/jcmcc-articles/volume-049/finite-order-domination-in-graphs/
2. E. J. Cockayne, O. Favaron, and C. M. Mynhardt, *Secure domination, weak Roman domination and forbidden subgraphs*, Bulletin of the Institute of Combinatorics and its Applications 39 (2003), 87–100. Public metadata: https://www.researchgate.net/publication/268059159_Secure_domination_weak_Roman_domination_and_forbidden_subgraphs
3. K. Lal Gipson and T. Subha, *Secure Dominating Sets and Secure Domination Polynomials of Cycles*, Advances and Applications in Discrete Mathematics 29(1) (2022), 59–83. https://www.pphmj.com/abstract/14929.htm
4. *A lower bound for secure domination number of an outerplanar graph*, Discrete Applied Mathematics 357 (2024), 81–85, DOI:10.1016/j.dam.2024.05.032. Its introduction summarizes the earlier exact complete-multipartite secure-domination-number result.
