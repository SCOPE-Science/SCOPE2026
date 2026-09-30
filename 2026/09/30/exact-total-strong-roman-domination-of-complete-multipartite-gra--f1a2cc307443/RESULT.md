# Exact total strong Roman domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\), \(n_i\ge 1\), order \(N=\sum_{i=1}^r n_i\), and \(m=\min_i n_i\). A total strong Roman dominating function is a map
\[
f:V(G)\to\left\{0,1,\ldots,\left\lceil\frac{\Delta(G)}2\right\rceil+1\right\}
\]
such that every zero-labelled vertex has a neighbor \(u\) satisfying
\[
f(u)\ge 1+\left\lceil\frac{|N(u)\cap V_0|}{2}\right\rceil,
\]
where \(V_0=\{v:f(v)=0\}\), and the subgraph induced by the positive-labelled vertices has minimum degree at least one. Write \(\gamma_{\mathrm{StR}}^t(G)\) for the minimum weight.

For distinct indices \(i,j\) with \(n_i,n_j\ge 2\), put
\[
a_i=N-n_i-1,\qquad a_j=N-n_j-1,
\]
and define \(\varepsilon_{ij}=1\) exactly when \(a_i\) and \(a_j\) are both odd and there exists \(h\notin\{i,j\}\) with \(n_h\ge 2\); otherwise put \(\varepsilon_{ij}=0\). Then
\[
\gamma_{\mathrm{StR}}^t(G)=\min\{A,B\},
\]
where
\[
A=m+1+\left\lceil\frac{N-m-1}{2}\right\rceil
\]
and
\[
B=\min_{\substack{1\le i<j\le r\\ n_i,n_j\ge 2}}
\left(2+\left\lceil\frac{a_i}{2}\right\rceil+\left\lceil\frac{a_j}{2}\right\rceil-\varepsilon_{ij}\right).
\]
The minimum over an empty index set is interpreted as \(+\infty\).

Thus the optimum is governed by two explicit modes: making an entire smallest part positive and using one strong defender there, or using two defender parts. In the two-defender mode, a third non-singleton part can save exactly one unit, and only in the indicated parity case.
## Assumptions and scope
The graph is finite, simple, connected, and complete multipartite, with at least two partite sets. The definition above is the total strong Roman domination parameter introduced in the cited source. The formula concerns the minimum weight only; it does not enumerate all minimum functions.
## Proof
Let the partite sets be \(A_1,\ldots,A_r\). For a total strong Roman dominating function \(f\), let \(P=V(G)\setminus V_0\) be the positive support, and write
\[
p_i=|P\cap A_i|,\qquad z_i=n_i-p_i,\qquad k=|P|,\qquad Z=|V_0|=N-k.
\]
Because \(G[P]\) has no isolated vertex, \(P\) meets at least two partite sets.

A positive vertex in \(A_i\) has exactly \(Z-z_i\) zero-labelled neighbors. Therefore a vertex in \(A_i\) that defends zeros must carry at least
\[
1+\left\lceil\frac{Z-z_i}{2}\right\rceil.
\]
If all zeros are defended from one part \(A_i\), then necessarily \(z_i=0\). Otherwise at least two distinct defender parts are required, because zeros lying in a defender's own part are nonadjacent to that defender. Consequently the total amount above the baseline value \(1\) on positive vertices is always at least \(\lceil Z/2\rceil\): this is immediate in the one-defender case, while for two defender parts \(A_i,A_j\),
\[
\left\lceil\frac{Z-z_i}{2}\right\rceil+
\left\lceil\frac{Z-z_j}{2}\right\rceil
\ge
\left\lceil\frac Z2\right\rceil,
\]
because \((Z-z_i)+(Z-z_j)\ge Z\).

Suppose first that some part \(A_h\) is entirely positive. Then \(k\ge n_h+1\ge m+1\). The function
\[
g(k)=k+\left\lceil\frac{N-k}{2}\right\rceil
\]
is nondecreasing in \(k\), so every such labeling has weight at least
\[
g(k)\ge g(m+1)=A.
\]

Now suppose no part is entirely positive. Any defender part therefore contains a zero, so there are at least two defender parts. Choose two of them, say \(A_i\) and \(A_j\), and write
\[
x=p_i-1,\qquad y=p_j-1,\qquad q=\sum_{h\notin\{i,j\}}p_h.
\]
Then
\[
Z-z_i=a_i-y-q,\qquad Z-z_j=a_j-x-q.
\]
The weight is therefore at least
\[
2+x+y+q+
\left\lceil\frac{a_i-y-q}{2}\right\rceil+
\left\lceil\frac{a_j-x-q}{2}\right\rceil.
\]
For fixed \(q\), increasing \(x\) by one changes \(x+\lceil(a_j-x-q)/2\rceil\) by either zero or one; hence this expression is nondecreasing in \(x\). The same holds for \(y\). Thus it is at least
\[
2+q+
\left\lceil\frac{a_i-q}{2}\right\rceil+
\left\lceil\frac{a_j-q}{2}\right\rceil.
\]
Define
\[
H_{a,b}(q)=q+\left\lceil\frac{a-q}{2}\right\rceil+\left\lceil\frac{b-q}{2}\right\rceil.
\]
A one-step calculation gives
\[
H_{a,b}(q+1)-H_{a,b}(q)
=1-\mathbf 1_{a-q\ \mathrm{odd}}-\mathbf 1_{b-q\ \mathrm{odd}}.
\]
If \(a\) and \(b\) have opposite parity, \(H_{a,b}\) is constant. If both are even, it alternates between its initial value and one more. If both are odd, it alternates between its initial value and one less. Hence
\[
H_{a_i,a_j}(q)\ge
\left\lceil\frac{a_i}{2}\right\rceil+
\left\lceil\frac{a_j}{2}\right\rceil-\varepsilon_{ij}.
\]
Indeed, the one-unit saving requires \(q>0\); under the present assumption that no part is entirely positive, this can happen only if a third part has size at least two. Therefore every labeling in the no-full-part case has weight at least \(B\).

It remains to attain both bounds. For \(A\), choose a part of size \(m\), label every vertex of that part positively, choose one positive vertex outside it, give one vertex in the full part label
\[
1+\left\lceil\frac{N-m-1}{2}\right\rceil,
\]
and give every other positive vertex label \(1\). All remaining vertices receive \(0\). The positive support meets two parts, and the displayed defender sees every zero vertex, so the weight is exactly \(A\).

For a pair \(i,j\) contributing to \(B\), first suppose \(\varepsilon_{ij}=0\). Choose one positive vertex in each of \(A_i,A_j\), give them labels
\[
1+\left\lceil\frac{a_i}{2}\right\rceil
\quad\text{and}\quad
1+\left\lceil\frac{a_j}{2}\right\rceil,
\]
and label every other vertex \(0\). Each zero in \(A_i\) is defended from \(A_j\), each zero in \(A_j\) from \(A_i\), and every other zero from either defender. The weight is the corresponding term of \(B\).

If \(\varepsilon_{ij}=1\), choose a third part \(A_h\) with \(n_h\ge 2\) and one additional positive vertex there, of label \(1\). Give the chosen vertices in \(A_i,A_j\) labels
\[
1+\left\lceil\frac{a_i-1}{2}\right\rceil
\quad\text{and}\quad
1+\left\lceil\frac{a_j-1}{2}\right\rceil.
\]
Since \(a_i,a_j\) are odd, the total weight is exactly
\[
2+\left\lceil\frac{a_i}{2}\right\rceil+
\left\lceil\frac{a_j}{2}\right\rceil-1.
\]
The positive support again has no isolated vertex, and the two strong vertices defend every zero. This proves the formula.
## Verification
The standalone verifier performs two exact checks. First, it enumerates every possible positive-support count vector for every complete multipartite isomorphism type of orders \(2\) through \(13\), totaling \(359\) graph types, computes the exact minimum permitted by the defining defense inequalities, and compares it with the closed formula. Second, it independently enumerates every legal label assignment from the definition for every complete multipartite isomorphism type of orders \(2\) through \(7\), totaling \(37\) graph types. Both checks return `VERIFY_OK`.
## Relationship to prior work
Nazari-Moghaddam, Soroudi, Sheikholeslami, and Yero introduced total strong Roman domination in the first public version of arXiv:1912.01093 on 2019-12-02 and developed general bounds and tree results. The source text does not give a complete-multipartite or complete-bipartite exact formula. Later work on signed total strong Roman domination changes the label set and neighborhood-sum condition, so it is a different parameter. The formula here specializes the original total strong parameter to the full class of connected complete multipartite graphs and exposes an additional parity phenomenon in the two-defender regime.
## Limitations
The result determines the minimum weight but does not classify or count all minimum total strong Roman dominating functions. It does not address signed, unique-response, or generalized \(p\)-strong variants. The proof uses the complete multipartite twin structure and therefore does not directly extend to arbitrary diameter-two graphs.
## References
1. S. Nazari-Moghaddam, M. Soroudi, S. M. Sheikholeslami, I. G. Yero, *On the total and strong version for Roman dominating functions in graphs*, arXiv:1912.01093v1, first public 2019-12-02; Aequationes Mathematicae 95 (2021), 215–236, DOI 10.1007/s00010-021-00778-x.
2. M. Hajjari, S. M. Sheikholeslami, *Signed total strong Roman domination in graphs*, Discrete Mathematics Letters 10 (2022), 41–44, DOI 10.47443/dml.2022.020.
