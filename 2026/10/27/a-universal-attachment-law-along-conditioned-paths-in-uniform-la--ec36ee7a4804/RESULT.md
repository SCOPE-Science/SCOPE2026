# A universal attachment law along conditioned paths in uniform labeled trees

## Finding

Let \(T\) be uniform over all labeled trees on \([n]\), where \(n\ge3\). Fix a labeled tree \(S\) on a specified set of \(q\) vertices, with \(2\le q<n\), and condition on every edge of \(S\) belonging to \(T\). Put \(m=n-q\) and enumerate the vertices of \(S\) as \(v_1,\ldots,v_q\). Define the *outside attachment count* \(X_i=\deg_T(v_i)-\deg_S(v_i)\). For arbitrary indeterminates \(z_1,\ldots,z_q\), the complete joint probability generating function is

\[
\boxed{\mathbb E\left[\prod_{i=1}^q z_i^{X_i}\mid S\subseteq T\right]
=\left(\frac{m+\sum_{i=1}^qz_i}{n}\right)^{m-1}
\frac{\sum_{i=1}^q z_i}{q}.}
\tag{1}
\]

Equivalently, in law

\[
\boxed{(X_1,\ldots,X_q)= (Y_1,\ldots,Y_q)+(\mathbf1_{\{J=1\}},\ldots,\mathbf1_{\{J=q\}}),}
\tag{2}
\]

where \(J\) is uniform on \(\{1,\ldots,q\}\) and independent of the multinomial vector whose \(m-1\) trials choose each of the \(q\) displayed categories with probability \(1/n\), and an additional unobserved category with probability \(m/n\). Thus the entire outside-degree vector, *not just its marginals*, is exchangeable and depends on the marked connected subtree only through its order \(q\), regardless of topology.

For distinct \(i,j\), in the same conditional law,

\[
\boxed{\operatorname{Cov}(X_i,X_j\mid S\subseteq T)
=-\frac{m-1}{n^2}-\frac1{q^2}<0.}
\tag{3}
\]

If \(q\ge2\) is fixed while \(n\to\infty\), the vector of attachments converges jointly to
\[
(Z_1,\ldots,Z_q)+(\mathbf1_{\{J=1\}},\ldots,\mathbf1_{\{J=q\}}),
\tag{4}
\]
where \(Z_i\) are independent Poisson variables of mean \(1\), independent of uniform \(J\). In particular its negative pairwise covariance tends to \(-1/q^2\), rather than vanishing.

For two distinct fixed labels \(u,v\), condition on their unique path having length \(k\). Then \(q=k+1\), and (1)--(4) describe all path-vertex excess degrees, with baseline degree \(1\) at the endpoints and \(2\) at interior path vertices. In particular, for \(1\le k\le n-2\),

\[
\boxed{\operatorname{Cov}(\deg_T(u),\deg_T(v)\mid d_T(u,v)=k)
=-\frac{n-k-2}{n^2}-\frac1{(k+1)^2}.}
\tag{5}
\]

At \(k=n-1\) the tree is the prescribed spanning path and both endpoint degrees are \(1\), so the conditional covariance is \(0\). Moreover the *pair* of endpoint degrees admits a coordinatewise monotone coupling as \(k\) increases from \(1\) through \(n-1\), with each marginal expectation strictly decreasing. The bivariate ordering is stronger than the previously established one-endpoint stochastic regression.

## Assumptions and scope

The underlying probability space is the **uniform labeled-tree** law, not a uniformly random unlabelled tree or a nonuniform spanning-tree model. Conditioning on a fixed connected labeled subtree is legitimate because its containment probability is positive. The notation \(S\subseteq T\) means edge containment, not an induced-subgraph restriction; for a tree containing a connected tree, the two interpretations agree on those marked vertices. Formula (1) holds for every \(2\le q<n\). For \(q=n\), every outside attachment count is deterministically zero. The distance-conditioned conclusions concern fixed labeled endpoints; after specifying the distance, all ordered choices of interior labels have the same conditional outside-degree law.

## Proof

**Extension count.** Write \(m=n-q\). Moon's classical forest-extension formula, as stated and proved in Pitman's *Coalescent Random Forests*, says that a fixed forest with \(c\) components of orders \(s_1,\ldots,s_c\) is contained in exactly \(n^{c-2}\prod_{j=1}^c s_j\) labeled trees. Applied to \(S\) and the \(m\) isolated unmarked vertices, it gives exactly \(qn^{m-1}\) completions.

**Joint factorial moments.** Choose disjoint prescribed sets \(A_i\) of unmarked vertices, with \(|A_i|=r_i\), and prescribe the edges from every vertex of \(A_i\) to \(v_i\). With \(r=\sum_i r_i\le m\), this is a forest with one component of order \(q+r\) and \(m-r\) isolated vertices. The number of completing trees is \((q+r)n^{m-r-1}\). Dividing by the former count, then summing over distinct ordered outside neighbors, yields

\[
\mathbb E\left[\prod_i(X_i)_{\underline{r_i}}\mid S\subseteq T\right]
=(m)_{\underline r}\frac{q+r}{q n^r}.
\tag{6}
\]

All factorial moments are zero when \(r>m\). There is no independence assumption in this step. These counts remain valid at \(r=m\), because the last extension count simplifies to \(1\).

**Generating function.** Put \(W=\sum_i(z_i-1)\). Expanding \(\prod_i(1+(z_i-1))^{X_i}\), inserting (6), and applying the multinomial theorem gives

\[
\begin{aligned}
\mathbb E\prod_i z_i^{X_i}
&=\sum_{r=0}^m\binom mr \frac{q+r}{q}\left(\frac Wn\right)^r\\
&=\left(1+\frac Wn\right)^{m-1}\left(1+\frac Wq\right).
\end{aligned}
\]

Since \(n=q+m\), the last expression is (1). Factoring the two probability generating functions establishes the independent multinomial-plus-categorical representation (2). For distinct coordinates, multinomial covariance is \(-(m-1)/n^2\) and the one-hot categorical covariance is \(-1/q^2\); independence proves (3). For fixed \(q\), the standard multinomial rare-category limit gives independent Poisson variables of mean \(1\), proving (4).

**Conditioned geodesics.** A tree has one path between fixed labels \(u,v\). When its distance is \(k\), fixing its ordered interior labels specifies a connected labeled subtree with \(q=k+1\) vertices. Formula (1) is independent of those labels, hence averaging over them gives the same law conditional only on the distance. The two endpoint baseline degrees equal \(1\), so their covariance is (3), giving (5). The case \(k=n-1\) is deterministic.

**Joint endpoint coupling.** Fix \(n\), and write \(q=k+1\). For each \(q\le n-1\), represent the attachments to the two marked endpoints using the first \(n-q-1\) variables of one infinite sequence of independent categorical trials, each hitting endpoint one or two with probability \(1/n\) apiece. Independently take \(J_2\) uniform on \(\{1,2\}\), and construct \(J_{q+1}\) by retaining \(J_q\) with probability \(q/(q+1)\), and otherwise setting it equal to \(q+1\). Each \(J_q\) is uniform on \(\{1,\ldots,q\}\), while the indicators \(\mathbf1_{\{J_q=1\}}\) and \(\mathbf1_{\{J_q=2\}}\) can only decrease as \(q\) increases. Consequently both endpoint attachment counts decrease simultaneously under this coupling; at \(q=n\) set both counts to zero. Their means are \((n-q-1)/n+1/q\) for \(q<n\), and zero for \(q=n\), giving strict successive inequalities. This proves the asserted vector stochastic comparison without asserting independence of the endpoints.

## Verification

The accompanying Python standard-library checker reconstructs every labeled tree by its Prüfer code for \(2\le n\le8\), finds the ordered path between fixed vertices, records the *entire* excess-degree vector, and independently compares every attainable coefficient of (1) as an exact rational number, including zero-probability vectors. It also checks the exact distance counts and all pairwise conditional covariances. The checker reports **648 exact assertions**. This enumeration tests finite boundary cases; it does not replace the all-size forest-count proof or prove historical originality.

## Relationship to prior work

Pitman's 1996 report gives the needed classical forest-extension formula, which is acknowledged as a premise rather than claimed as a discovery. The published result *Exact negative regression between endpoint degree and distance in a uniform Cayley tree* gives the one-endpoint binomial-plus-Bernoulli marginal law and its stochastic ordering; those one-dimensional statements are not claimed here. The new question is the **simultaneous conditional law along the entire marked path**, its universal one-hot competition, its negative pairwise covariance, and the **two-endpoint** coupling; none follows from a one-dimensional marginal law alone. The underlying extension count is strong enough to enable this additional marked-neighbor derivation, and an older equivalent multivariate weighting remains a real priority risk.

Aldous treats uniform labeled-tree degree marginals via random-walk constructions. Berzunza Ojeda and Janson investigate distance profiles of simply generated random trees and marked-edge decompositions; their inspected open full-text sections concern distance limits and conditioned branches, not an exact finite multi-vertex attachment polynomial of the form (1).

## Limitations

The independence in (2) is between the multinomial vector and a single categorical assignment, **not** among the attachment coordinates. For \(q\ge2\) their covariances are strictly negative. The Poisson limit (4) assumes \(q\) fixed, not growing with \(n\). The bivariate comparison covers the two *marked endpoints* as distance changes; it is not a coupling of entire trees or of path degree vectors of changing dimension. The literature comparison cannot exclude an equivalent statement implicit in classical multivariate Cayley/forest generating functions.

## References

1. J. Pitman, *Coalescent Random Forests*, Berkeley Statistics Technical Report 457 (dated 1996-09-01), especially Section 2.2, Lemma 3; public PDF at https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf.
2. D. J. Aldous, *The Random Walk Construction of Uniform Spanning Trees and Uniform Labelled Trees*, SIAM Journal on Discrete Mathematics 3 (1990), 450–465, DOI 10.1137/0403039.
3. G. Berzunza Ojeda and S. Janson, *The distance profile of rooted and unrooted simply generated trees*, arXiv:2009.00572 (first posted 2020-09-01); journal DOI 10.1017/S0963548321000304.
4. *Exact negative regression between endpoint degree and distance in a uniform Cayley tree*, published mathematical record (2026-10-04), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-negative-regression-between-endpoint-degree-and-distance-i--d9ddfb06a9ae.
