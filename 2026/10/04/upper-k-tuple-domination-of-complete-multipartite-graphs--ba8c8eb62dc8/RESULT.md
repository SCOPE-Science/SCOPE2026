# Upper \(k\)-tuple domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\). Write \(N=\sum_i n_i\) and \(L=\max_i n_i\). For every integer \(k\) for which a \(k\)-tuple dominating set exists, equivalently
\[
1\le k\le N-L+1,
\]
the upper \(k\)-tuple domination number satisfies
\[
\Gamma_{\times k}(G)=L+k-1.
\]
Moreover, if \(V_i\) is any part of size \(L\) and \(T\subseteq V(G)\setminus V_i\) has \(|T|=k-1\), then \(V_i\cup T\) is a maximum-cardinality minimal \(k\)-tuple dominating set.

## Assumptions and scope
All graphs are finite, simple, and undirected. A set \(S\subseteq V(G)\) is \(k\)-tuple dominating when \(|N[v]\cap S|\ge k\) for every vertex \(v\). It is minimal when no proper subset is \(k\)-tuple dominating. The upper \(k\)-tuple domination number \(\Gamma_{\times k}(G)\) is the maximum cardinality of a minimal \(k\)-tuple dominating set.

For \(G=K_{n_1,\ldots,n_r}\), the minimum degree is \(N-L\), so such sets exist exactly for \(k\le N-L+1\). The theorem includes \(k=1\), where it reduces to the ordinary upper domination value \(L\), but the claim is about the entire feasible \(k\)-tuple range.

## Proof
Let the parts be \(V_1,\ldots,V_r\), and for a set \(S\) put \(s=|S|\) and \(s_i=|S\cap V_i|\). If \(v\in V_i\cap S\), then
\[
|N[v]\cap S|=s-s_i+1,
\]
whereas if \(v\in V_i\setminus S\), then
\[
|N[v]\cap S|=s-s_i.
\]

For the lower bound, choose a largest part \(V_i\) and a set \(T\subseteq V(G)\setminus V_i\) with \(|T|=k-1\), and put \(S=V_i\cup T\). Every vertex of \(V_i\) has exactly \(k\) members of \(S\) in its closed neighborhood. For any other part \(V_j\), if it is not fully selected then \(s_j\le n_j-1\le L-1\), so each of its vertices sees at least
\[
(L+k-1)-(L-1)=k
\]
selected vertices in its closed neighborhood. If \(V_j\) is fully selected, then its selected vertices see at least \(L+k-1-L+1=k\). Thus \(S\) is \(k\)-tuple dominating. Removing a vertex of \(V_i\) leaves that removed vertex with only \(k-1\) selected closed neighbors; removing a vertex of \(T\) leaves every vertex of \(V_i\) with only \(k-1\). Hence \(S\) is minimal and
\[
\Gamma_{\times k}(G)\ge L+k-1.
\]

For the upper bound, let \(S\) be any inclusion-minimal \(k\)-tuple dominating set. Minimality implies that for every \(u\in S\) there is a closed neighbor \(w\in N[u]\) with \(|N[w]\cap S|=k\): otherwise deleting \(u\) would preserve all \(k\)-tuple domination inequalities. Fix one such witness \(w\), and suppose \(w\in V_j\).

If \(w\in S\), then \(s-s_j+1=k\), so \(s_j=s-k+1\). The part \(V_j\) must be fully selected, because any unselected vertex in it would have only \(s-s_j=k-1\) selected closed neighbors. Hence \(s_j=n_j\le L\), giving \(s\le L+k-1\).

If \(w\notin S\), then \(s-s_j=k\). Since \(s_j<n_j\le L\), one has \(s_j\le L-1\), and again \(s=k+s_j\le L+k-1\). Thus every minimal \(k\)-tuple dominating set has size at most \(L+k-1\), completing the proof.

## Verification
The standalone verifier enumerates every unordered complete-multipartite part profile of order at most \(10\). For every feasible \(k\), it constructs the graph explicitly, tests every vertex subset against the literal closed-neighborhood definition, tests inclusion-minimality by one-vertex deletions, compares the largest minimal-set cardinality with \(L+k-1\), and separately checks every construction obtained from every largest part and every choice of \(k-1\) outside vertices.

The replay output is:

`VERIFY_OK profiles=128 parameter_checks=697 subset_checks=403280 minimal_sets=24686 construction_checks=19604 max_order=10`

This finite census is a regression check only; the proof above establishes the theorem for all admissible part sizes and all feasible \(k\).

## Relationship to prior work
Chang, Dorbec, Kim, Raspaud, Wang, and Zhao introduced and studied the upper \(k\)-tuple domination parameter in the cited 2012 paper. Its full text states the tight-witness characterization used above, then develops sharp bounds for regular graphs, a special bound for claw-free regular graphs, and complexity results for bipartite and chordal graphs. A full-text search of that paper found no occurrence of “multipartite,” and its stated scope does not contain an exact complete-multipartite formula.

Henning and Kazemi studied \(k\)-tuple **total** domination and explicitly determined minimum total-domination quantities for complete multipartite graphs. Kazemi later compared the minimum closed-neighborhood and total variants on complete multipartite graphs. These results concern minima, and the total variant uses open neighborhoods; neither implication determines the maximum size of an inclusion-minimal closed-neighborhood \(k\)-tuple dominating set. The case \(k=1\) is consistent with the classical fact that upper domination equals the independence number on bipartite graphs, hence equals the largest part size for a complete multipartite graph.

## Limitations
The result evaluates the upper \(k\)-tuple domination number and gives a large explicit family of maximum minimal sets, but it does not classify every maximum minimal set. The originality comparison covered the defining upper-parameter paper, the directly relevant complete-multipartite minimum/total literature, targeted web searches under upper/double/multiple-domination terminology, semantic-literature searches. Older literature with different terminology can never be excluded absolutely; that residual bibliographic risk remains.

## References
1. G. J. Chang, P. Dorbec, H. K. Kim, A. Raspaud, H. Wang, W. Zhao, “Upper k-tuple domination in graphs,” *Discrete Mathematics & Theoretical Computer Science* 14(2) (2012), 285–292, DOI 10.46298/dmtcs.593, HAL hal-00903694v1.
2. M. A. Henning, A. P. Kazemi, “k-tuple total domination in graphs,” *Discrete Applied Mathematics* 158 (2010), 1006–1011, DOI 10.1016/j.dam.2010.01.009.
3. A. P. Kazemi, “On the Total k-domination Number of Graphs,” *Discussiones Mathematicae Graph Theory* 32(3) (2012), 419–426, DOI 10.7151/dmgt.1616.
