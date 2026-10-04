# Exact \(k\)-tuple total restrained domination enumerator of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge 2\), nonempty parts \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). Fix an integer \(k\) with \(1\le k\le \delta(G)=N-\max_i n_i\). For \(S\subseteq V(G)\), write \(s=|S|\) and \(s_i=|S\cap V_i|\).

Then \(S\) is a \(k\)-tuple total restrained dominating set if and only if, for every \(i\),
\[
s-s_i\ge k,
\]
and, whenever \(s_i<n_i\),
\[
N-s-n_i+s_i\ge k.
\]
Thus feasibility depends only on the part-intersection profile \((s_1,\ldots,s_r)\).

For a fixed cardinality \(s\), define
\[
L_i(s)=\max\{0,\,s+n_i-N+k\},\qquad
U_i(s)=\min\{n_i-1,\,s-k\},
\]
and
\[
F_{i,s}(y)=
\mathbf 1_{\{n_i\le s-k\}}y^{n_i}
+\sum_{j=L_i(s)}^{U_i(s)}\binom{n_i}{j}y^j,
\]
where a sum with lower limit larger than its upper limit is empty. If
\[
T^r_{\times k,t}(G;x)=\sum_{S\text{ a }k\text{-tuple total restrained dominating set}}x^{|S|},
\]
then
\[
T^r_{\times k,t}(G;x)
=\sum_{s=0}^{N}
\left([y^s]\prod_{i=1}^{r}F_{i,s}(y)\right)x^s.
\]
In particular, the minimum \(k\)-tuple total restrained domination number is the least exponent with nonzero coefficient in this polynomial.

## Assumptions and scope
Graphs are finite, simple, and undirected. The parameter \(k\) is restricted to \(1\le k\le\delta(G)\), which is exactly the degree range in which a \(k\)-tuple total dominating set can exist. The restrained condition is imposed only on vertices outside \(S\); when \(S=V(G)\), it is vacuous, and the displayed criterion correctly includes \(V(G)\) because \(k\le\delta(G)\).

A \(k\)-tuple total restrained dominating set means that every vertex has at least \(k\) neighbors in \(S\), and every vertex outside \(S\) has at least \(k\) neighbors outside \(S\).

## Proof
Fix a part \(V_i\). Every vertex of \(V_i\) is adjacent to every vertex outside \(V_i\) and to no vertex inside \(V_i\). Hence every vertex of \(V_i\) has exactly \(s-s_i\) neighbors in \(S\). Therefore the \(k\)-tuple total domination requirement is equivalent to
\[
s-s_i\ge k
\]
for every \(i\).

Now suppose \(s_i<n_i\), so that at least one vertex of \(V_i\) lies outside \(S\). The complement \(V(G)\setminus S\) has \(N-s\) vertices, of which \(n_i-s_i\) lie in \(V_i\). An omitted vertex of \(V_i\) therefore has exactly
\[
(N-s)-(n_i-s_i)=N-s-n_i+s_i
\]
neighbors outside \(S\). Thus the restrained requirement is equivalent to
\[
N-s-n_i+s_i\ge k
\]
for every part that is not fully selected. If \(s_i=n_i\), there is no omitted vertex in that part and no restrained inequality is required there. This proves the profile characterization.

For the enumerator, fix \(s\). The total-domination inequality gives \(s_i\le s-k\). If \(s_i<n_i\), the restrained inequality gives \(s_i\ge s+n_i-N+k\), together with \(s_i\ge0\). Hence every non-full coordinate must lie in the integer interval
\[
L_i(s)\le s_i\le U_i(s).
\]
A full coordinate \(s_i=n_i\) is permitted exactly when it also satisfies total domination, namely \(n_i\le s-k\). For each admissible value \(j\), there are \(\binom{n_i}{j}\) ways to choose the selected vertices in \(V_i\). Multiplying the part polynomials \(F_{i,s}(y)\) records all admissible profiles and their multiplicities; extracting \([y^s]\) enforces \(\sum_i s_i=s\). Summing over \(s\) proves the formula.

## Verification
The accompanying `verify.py` exhaustively checks every nondecreasing complete-multipartite profile of orders \(2\) through \(9\), every integer \(k\) in the admissible range \(1\le k\le\delta(G)\), and every vertex subset. It compares the literal neighborhood definition with the profile criterion, compares every cardinality count with the coefficient formula, and checks that the least nonzero coefficient agrees with brute-force minimization.

The replay output is:

`VERIFY_OK profiles=87 parameter_checks=341 subset_checks=104892 valid_sets=28609 coefficient_checks=3000 minimum_checks=341 max_order=9`

This finite census is a consistency check only; the theorem for arbitrary part sizes follows from the symbolic neighborhood-count proof above.

## Relationship to prior work
Kazemi introduced \(k\)-tuple total restrained domination in the cited 2011 preprint and treated the same complete-multipartite family. The paper gives an exact complete-bipartite minimum characterization and, for complete \(p\)-partite graphs with \(p\ge3\), lower and upper bounds for the minimum parameter. In particular, summing the inequalities \(s-s_i\ge k\) over all parts gives \((r-1)s\ge rk\), recovering the source's lower-bound mechanism. Its complete-multipartite section does not state an all-set profile characterization or a cardinality generating function.

The present result is strictly finer than those scalar bounds: it decides every subset from its intersection profile and counts all feasible subsets of every size. The scalar minimum is then obtained as the first nonzero coefficient rather than being the only retained information.

The ordinary total restrained case \(k=1\) was introduced earlier by Ma, Chen, and Sun; their complete-multipartite results determine the minimum in the main boundary cases, consistent with the specialization of the profile criterion.

## Limitations
The formula is an exact coefficient expression, not a single closed form for the minimum parameter for all part-size vectors and all \(k\). The literature comparison found no all-set complete-multipartite enumerator, but obscure or poorly indexed work using equivalent terminology remains a residual bibliographic risk. The finite verifier covers orders only through \(9\) and does not substitute for the proof.

## References
1. A. P. Kazemi, *k-tuple total restrained domination and k-tuple total restrained domatic in graphs*, arXiv:1106.5591v1, first posted 2011-06-28. https://arxiv.org/abs/1106.5591
2. A. P. Kazemi, *k-Tuple Total Restrained Domination/Domatic in Graphs*, Bulletin of the Iranian Mathematical Society 40(3) (2014), 751--763.
3. D.-x. Ma, X.-G. Chen, L. Sun, *On total restrained domination in graphs*, Czechoslovak Mathematical Journal 55 (2005), 165--173. DOI: 10.1007/s10587-005-0012-2.
