# Generalized power domination of chain graphs is always one or two
## Finding
Let \(G\) be a finite connected chain graph with canonical nonempty open-neighborhood twin classes \(A_1,\ldots,A_p,B_1,\ldots,B_p\), normalized so that every vertex of \(A_i\) is adjacent to every vertex of \(B_j\) exactly when \(j\le i\). Write \(\alpha_i=|A_i|\) and \(\beta_i=|B_i|\). For every integer \(k\ge1\), put
\[
L_A=\max\{\alpha_1,\ldots,\alpha_{p-1},\alpha_p-1\},\qquad
L_B=\max\{\beta_1-1,\beta_2,\ldots,\beta_p\},
\]
with the evident one-term interpretation when \(p=1\). Then
\[
\gamma_{P,k}(G)=
\begin{cases}
1,&\min\{L_A,L_B\}\le k,\\
2,&\min\{L_A,L_B\}>k.
\end{cases}
\]
More precisely, every vertex of \(A_p\) is a \(k\)-power dominating set if and only if \(L_A\le k\), and every vertex of \(B_1\) is one if and only if \(L_B\le k\). If any singleton \(k\)-power dominating set exists anywhere in \(G\), then at least one of these two extreme conditions holds.

## Assumptions and scope
All graphs are finite, simple, and connected. A chain graph is bipartite and has nested open neighborhoods on each side; the canonical classes above are the maximal open-neighborhood twin classes. Generalized \(k\)-power domination uses the standard domination step followed by the rule that a monitored vertex having at most \(k\) unmonitored neighbors monitors all of those neighbors. The theorem is for integers \(k\ge1\). It includes ordinary power domination at \(k=1\).

## Proof
Choose \(a\in A_p\). Its domination step monitors \(a\) and every vertex of \(B_1\cup\cdots\cup B_p\). If \(L_A\le k\), then \(B_p\) has exactly \(\alpha_p-1\le k\) unmonitored neighbors and therefore monitors the rest of \(A_p\). Inductively, after \(A_{i+1},\ldots,A_p\) have been monitored, any vertex of \(B_i\) has exactly \(\alpha_i\le k\) unmonitored neighbors, namely \(A_i\), so it monitors all of \(A_i\). Descending through \(i=p-1,\ldots,1\) monitors the whole graph. Hence every vertex of \(A_p\) is a \(k\)-power dominating singleton when \(L_A\le k\). The symmetric argument shows that every vertex of \(B_1\) works when \(L_B\le k\).

For necessity, suppose a singleton \(\{v\}\) with \(v\in A_i\) is \(k\)-power dominating. For any \(j\ne i\), no vertex of \(A_j\) is monitored in the domination step. If \(\alpha_j>k\), then as long as \(A_j\) remains unmonitored, every monitored vertex adjacent to \(A_j\) has more than \(k\) unmonitored neighbors in \(A_j\) alone, so no propagation step can monitor even one vertex of that twin class. Thus \(\alpha_j\le k\) for every \(j\ne i\).

If \(i<p\) and \(\alpha_i>k\), the domination step leaves at least \(k\) unmonitored vertices in \(A_i\), while the nonempty class \(A_{i+1}\) is also unmonitored. Every initially monitored vertex of \(B_1\cup\cdots\cup B_i\) therefore has at least \(k+1\) unmonitored neighbors, and \(v\) itself has no unmonitored neighbor because all of its neighbors lie in \(B_1\cup\cdots\cup B_i\), already monitored. No propagation step can start, a contradiction. Hence \(\alpha_i\le k\). Therefore when \(i<p\), every \(\alpha_j\le k\), which implies \(L_A\le k\). If \(i=p\), the same twin-class obstruction gives \(\alpha_p-1\le k\), while the preceding argument gives \(\alpha_j\le k\) for \(j<p\); again \(L_A\le k\). The case \(v\in B_i\) is symmetric and implies \(L_B\le k\).

Finally, choose \(a\in A_p\) and \(b\in B_1\). Since \(A_p\) is complete to the entire \(B\)-side and \(B_1\) is complete to the entire \(A\)-side, \(\{a,b\}\) is already a dominating set. Hence \(\gamma_{P,k}(G)\le2\). Combining this with the singleton criterion proves the formula.

## Verification
The accompanying `verify.py` independently constructs every canonical chain-graph block profile of order at most \(11\), for up to five block pairs, and checks \(k=1,2,3,4\). It executes the literal generalized power-domination process, tests every singleton against the formula, and when the formula predicts value \(2\), checks an extreme pair \(\{a,b\}\) with \(a\in A_p\) and \(b\in B_1\). The replay result is `VERIFY_OK profiles=4092 singleton_checks=19327 extreme_pair_checks=700 max_order=11 k_max=4`. This finite verification is a stress test, not the proof of the infinite theorem.

## Relationship to prior work
Dorbec, Varghese, and Vijayakumar define generalized \(k\)-power domination and emphasize that exact characterization remains difficult even for structured graph families; their full text discusses bipartite hardness and complete-bipartite examples but contains no occurrence of “chain” or “Ferrers” [1]. Brimkov, Patel, Suriyanarayana, and Teich later develop power-domination polynomials and all-set counting methods, but their searchable full text likewise contains no occurrence of “chain”, “Ferrers”, or “multipartite” [2]. The present result is different in scope: it gives a closed generalized \(k\)-power domination number for every connected chain graph, with an exact one-versus-two threshold in terms of the canonical twin-class sizes. At \(p=1\) it specializes to the complete-bipartite condition that one PMU suffices exactly when one side has size at most \(k+1\), consistent with the complete-bipartite examples in [1].

## Limitations
The theorem determines the minimum cardinality and explicit extreme singleton witnesses. It does not enumerate all minimum \(k\)-power dominating sets, classify propagation radii, or extend the formula to disconnected chain graphs. The literature search cannot exclude an older result indexed only under uncommon terminology; Ferrers graphs, difference graphs, bipartite chain graphs, generalized power domination, and \(k\)-power domination were all checked, and that residual indexing risk remains.

## References
[1] P. Dorbec, S. Varghese, and A. Vijayakumar, “Heredity for generalized power domination,” *Discrete Mathematics & Theoretical Computer Science* 18:3 (2016), article 5. arXiv:1603.07243; DOI:10.46298/dmtcs.1290.

[2] B. Brimkov, R. Patel, V. Suriyanarayana, and A. Teich, “Power domination polynomials of graphs,” arXiv:1805.10984 (2018).

[3] T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi, and M. A. Henning, “Domination in graphs applied to electric power networks,” *SIAM Journal on Discrete Mathematics* 15 (2002), 519–529. DOI:10.1137/S0895480100375831.
