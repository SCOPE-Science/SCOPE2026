# Isolated-domination polynomial of barbell graphs
## Finding
For every integer \(n\ge 2\), let \(B_n\) be the barbell graph formed from disjoint cliques \(U=\{u_1,\ldots,u_n\}\) and \(V=\{v_1,\ldots,v_n\}\), each inducing \(K_n\), by adding the single bridge \(u_nv_n\). A set \(S\subseteq V(B_n)\) is isolate dominating when it dominates \(B_n\) and the induced graph \(B_n[S]\) has an isolated vertex.

Write \(a=|S\cap U|\) and \(b=|S\cap V|\). Then \(S\) is isolate dominating exactly when \(a,b\ge1\) and at least one of the following holds: \(a=1\) and the unique selected vertex of \(U\) is not \(u_n\), or \(a=1\), \(S\cap U=\{u_n\}\), and \(v_n\notin S\), or the symmetric condition with \(U,V\) interchanged.

Define
\[
\mathcal I_n(x,y)=\sum_{S}x^{|S\cap U|}y^{|S\cap V|},
\]
where the sum is over all isolate dominating sets of \(B_n\). Put \(P_n(t)=(1+t)^n-1\) and \(Q_n(t)=P_n(t)-nt\). Then
\[
\mathcal I_n(x,y)=P_n(x)P_n(y)-Q_n(x)Q_n(y)-xy\big((1+x)^{n-1}+(1+y)^{n-1}-1\big).
\]
Consequently the ordinary isolated-domination polynomial is
\[
I_n(z)=\mathcal I_n(z,z)
=2nz\big((1+z)^n-1\big)-2z^2(1+z)^{n-1}-(n^2-1)z^2.
\]
In particular,
\[
I_n(1)=(2n-1)2^n-n^2-2n+1.
\]
Every minimal isolate dominating set has exactly two vertices, one in each clique, and is any such cross-clique pair except \(\{u_n,v_n\}\). Hence
\[
\gamma_0(B_n)=\Gamma_0(B_n)=2,
\]
and the number of minimal isolate dominating sets is \(n^2-1\). The polynomial has degree \(n+1\), with leading coefficient \(2(n-1)\), so the largest isolate dominating sets are much larger than the largest minimal ones.

## Assumptions and scope
Graphs are finite, simple, and undirected. The statement uses the standard barbell convention of two copies of \(K_n\) joined by exactly one bridge, and it is asserted only for \(n\ge2\). The case \(n=1\) is \(K_2\) and has different one-vertex behavior, so it is deliberately excluded.

The polynomial counts all isolate dominating sets, not only minimal ones. The symbol \(\Gamma_0\) denotes the upper isolate domination number, namely the maximum cardinality of a minimal isolate dominating set.

## Proof
Every vertex of \(U\setminus\{u_n\}\) has no neighbor in \(V\), and every vertex of \(V\setminus\{v_n\}\) has no neighbor in \(U\). Therefore a dominating set must meet both cliques. Conversely, any set meeting both cliques dominates the whole graph, because a selected vertex in a clique dominates every vertex of that clique. Thus domination is equivalent to \(a,b\ge1\).

If \(a\ge2\), then every selected vertex of \(U\) has a selected neighbor inside the clique \(U\); similarly, if \(b\ge2\), every selected vertex of \(V\) has a selected neighbor inside \(V\). Hence an isolate can exist only when \(a=1\) or \(b=1\). If \(a=1\) and the selected vertex is \(u_i\) with \(i<n\), then it has no selected neighbor outside \(U\), so it is isolated. If \(a=1\) and the selected vertex is \(u_n\), it is isolated exactly when \(v_n\notin S\). The symmetric statement holds on the other side. This proves the structural criterion.

For the enumeration, all dominating sets contribute \(P_n(x)P_n(y)\). A dominating set has no isolated selected vertex in three disjoint situations. First, both sides have size at least two, contributing \(Q_n(x)Q_n(y)\). Second, the \(U\)-side is the singleton \(\{u_n\}\), while the \(V\)-side contains \(v_n\) and at least one further vertex; this contributes \(xy((1+y)^{n-1}-1)\). Third, the symmetric situation contributes \(xy((1+x)^{n-1}-1)\). The bridge pair \(\{u_n,v_n\}\) contributes the remaining \(xy\) non-isolate case. Subtracting these disjoint non-isolate cases from all dominating sets gives the displayed bivariate formula. Setting \(x=y=z\) yields the ordinary polynomial, and setting \(z=1\) yields the total count.

For minimality, suppose an isolate dominating set has \(a=1\) and \(b\ge2\). By the structural criterion, the unique selected vertex on the \(U\)-side is already isolated and remains isolated after deleting any selected vertex of \(V\) while leaving at least one selected vertex there. The resulting set still meets both cliques and therefore still dominates, contradicting minimality. Hence every minimal isolate dominating set has \(a=b=1\). Every cross-clique pair dominates, and such a pair is isolate dominating exactly when it is not the bridge pair \(\{u_n,v_n\}\). This gives exactly \(n^2-1\) minimal sets, all of cardinality two, proving both \(\gamma_0(B_n)=2\) and \(\Gamma_0(B_n)=2\).

## Verification
The proof above is symbolic and applies to every \(n\ge2\). As an independent finite consistency check, `verify.py` exhaustively enumerates every vertex subset for \(2\le n\le7\), checks domination and the induced-isolate condition directly from adjacency, compares every bivariate and univariate coefficient with the formulas, and separately checks the complete classification of minimal isolate dominating sets.

The replay result on the packaged verifier is:

`VERIFY_OK n_range=2..7 subset_checks=21840 isolate_sets=2633 minimal_sets=133 bivariate_checks=48 univariate_checks=27 max_order=14`

Finite enumeration is not used as an infinite proof; it only checks the symbolic classification on all barbell graphs through order \(14\).

## Relationship to prior work
Hamid and Balamurugan introduced isolate domination and made their paper publicly available online on 2015-11-05. Their exact-value section treats paths, cycles, wheels, complete multipartite graphs, and a pendant-extension construction, but not barbell graphs. Their framework supplies the definitions of \(\gamma_0\) and \(\Gamma_0\).

Bhangale and Pawar later treated the same barbell object. Their Theorem 2.6 proves the scalar equality \(\gamma_0(B_n)=2\) and exhibits the cross-clique pairs other than the bridge pair as minimum isolate dominating sets. That scalar result is recovered here, but it does not determine the counts in every cardinality, the bivariate side profile, or the upper isolate domination number.

Puttaswamy, Prakasha, and Nayaka subsequently defined the isolated domination polynomial as the cardinality enumerator of isolate dominating sets. Their inspected full text treats complete graphs, stars, bi-stars, joins, complete multipartite graphs, and friendship graphs. A full-text search found no occurrence of “barbell”. Their bi-star \(B(m,n)\) is a tree obtained from \(P_2\) by attaching leaves to its two endpoints and is not the barbell graph considered here. Thus their general polynomial definitions and listed family formulas do not imply the present barbell formula.

## Limitations
No claim is made here about the location of the zeros, unimodality, log-concavity, or extremal behavior of \(I_n(z)\). The result does not cover \(n=1\). The literature comparison includes the foundational isolate-domination paper, the same-object scalar barbell theorem, the paper introducing the isolated-domination polynomial, and published-finding corpus searches under multiple equivalent formulations. An unindexed or inaccessible source could still contain the same all-set formula; no such source was found in the checked material.

## References
1. I. Sahul Hamid and S. Balamurugan, “Isolate domination in graphs,” *Arab Journal of Mathematical Sciences* 22 (2016), 232–241. DOI 10.1016/j.ajmsc.2015.10.001. Available online 2015-11-05.
2. S. T. Bhangale and M. M. Pawar, “Isolate and independent domination number of some classes of graphs,” *AKCE International Journal of Graphs and Combinatorics* 16 (2019), 110–115. DOI 10.1016/j.akcej.2018.08.005.
3. Puttaswamy, M. N. Prakasha, and S. R. Nayaka, “Isolated Domination Polynomial of a Graph,” *International Journal of Mathematics And its Applications* 8(4) (2020), 69–73.
4. B. H. Arriola, “Isolate Domination in the Join and Corona of Graphs,” *Applied Mathematical Sciences* 9 (2015), 1543–1549. DOI 10.12988/ams.2015.512. The paper explicitly classifies the topic under MSC 05C69.
