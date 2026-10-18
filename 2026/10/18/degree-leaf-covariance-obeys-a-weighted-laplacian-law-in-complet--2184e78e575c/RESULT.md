# Degree–leaf covariance obeys a weighted Laplacian law in complete multipartite spanning trees

## Finding

Let \(G=K_{n_1,\ldots,n_r}\) be a complete multipartite graph with \(r\geq3\) nonempty parts \(V_1,\ldots,V_r\), total size \(N=\sum_{p=1}^r n_p\), and let \(T\) be a uniformly chosen spanning tree of \(G\). Write \(D_u=\deg_T(u)\), \(L=\sum_{v\in V(G)}\mathbf1\{D_v=1\}\). Define the leaf probabilities and positive pair weights

\[
q_p=\left(1-\frac1N\right)^{r-2}\prod_{k\ne p}\left(1-\frac1{N-n_k}\right)^{n_k-1},
\]

\[
W_{uv}=\frac{r-2}{N(N-1)}+\sum_{k:\,u,v\notin V_k}\frac{n_k-1}{(N-n_k)(N-n_k-1)}\quad(u\ne v).
\]

Then \(\Pr(D_u=1)=q_p\) whenever \(u\in V_p\), and the exact finite-graph covariance is

\[
\boxed{\operatorname{Cov}(D_u,L)=\sum_{v\ne u}W_{uv}\bigl(q_{p(v)}-q_{p(u)}\bigr).}
\]

Moreover \(W_{uv}>0\), \(q_p\) is strictly increasing with the part size \(n_p\), and therefore, whenever the part sizes are not all equal,

\[
\boxed{\begin{array}{ll}
\operatorname{Cov}(D_u,L)>0,&u\text{ in a smallest part},\\
\operatorname{Cov}(D_u,L)<0,&u\text{ in a largest part}.
\end{array}}
\]

If all parts have the same size, every such covariance is zero. For a complete bipartite graph \(K_{a,b}\), the covariance is zero for every marked vertex, even when \(a\ne b\). The sign of an intermediate part is not predetermined: the middle-part covariance in \(K_{1,2,3}\) equals \(-11/1296\), whereas in \(K_{1,2,4}\) it equals \(32/2205\).

A stronger positional identity explains the result. For any distinct \(u,v\),

\[
\boxed{\operatorname{Cov}\bigl(D_u,\mathbf1\{D_v=1\}\bigr)=q_{p(v)}W_{uv}>0,}
\]

while \(\operatorname{Cov}(D_u,\mathbf1\{D_u=1\})=-q_{p(u)}\mathbb E(D_u-1)<0\). Positive cross-vertex terms compete with a negative same-vertex term, and a weighted graph Laplacian determines the net sign.

## Assumptions and scope

The underlying graph is simple and complete multipartite, with \(n_p\ge1\) integers and \(r\ge2\). Spanning trees are unrooted and sampled uniformly; vertex degrees count ordinary tree edges, and a leaf has tree degree one. The displayed \(q_p,W_{uv}\) formulas apply to \(r\ge3\), where all denominators are nonzero. The bipartite case is proved separately. No limit in the number of vertices is assumed for the main theorem. No claim is made about the sign in a nonextremal part beyond the exact formula.

## Proof

**1. The degree-generating polynomial.** Put positive weights \(z_v\) on vertices, \(Z_p=\sum_{v\in V_p}z_v\), \(Z=\sum_vz_v\). Give every permitted edge \(\{u,v\}\) weight \(z_uz_v\). The weighted Matrix–Tree Theorem gives

\[
F(z):=\sum_{T}\prod_vz_v^{\deg_T(v)}
=\left(\prod_vz_v\right)Z^{r-2}\prod_{p=1}^r(Z-Z_p)^{n_p-1}.
\]

For completeness, delete a root row and column at vertex \(h\in V_s\) from the edge-weighted Laplacian, and factor \(z_v\) from each remaining row. The resulting matrix has diagonal entries \(Z-Z_{p(v)}\), and off-diagonal entries \(-z_w\) when its row and column vertices lie in different parts, zero otherwise. The determinant lemma reduces its determinant to that of the \(r\)-by-\(r\) matrix \(\operatorname{diag}(1+a_p)-a\mathbf1^\top\), where \(a_p=(Z_p-\mathbf1\{p=s\}z_h)/(Z-Z_p)\). Its determinant is \(z_hZ^{r-2}/\prod_{p\ne s}(Z-Z_p)\), while the extracted diagonal factor is \(\prod_p(Z-Z_p)^{n_p-\mathbf1\{p=s\}}\). Multiplication by \(\prod_{v\ne h}z_v\) gives the claimed polynomial. The identity extends from positive weights to the polynomial identity.

After dividing by \(\prod_vz_v\), setting all variables equal to one for normalization, and writing \(X_v=D_v-1\), the probability generating polynomial becomes

\[
\mathbb E\prod_vz_v^{X_v}
=\left(\frac{\sum_vz_v}{N}\right)^{r-2}
\prod_{p=1}^r\left(\frac{\sum_{v\notin V_p}z_v}{N-n_p}\right)^{n_p-1}.
\]

Thus the entire excess-degree vector is distributed as the occupancy counts of **independent** categorical draws: \(r-2\) uniform draws over all vertices and, independently for each part \(p\), \(n_p-1\) uniform draws over vertices outside \(V_p\). Their total count is \(N-2\).

**2. The covariance identity.** For \(r\ge3\), every allowed draw set has at least two vertices. Let \(S_t\) be the allowed vertex set for draw \(t\), \(m_t=|S_t|\), and let \(Q_v=\Pr(X_v=0)\). If \(u\ne v\), independence of draws and conditioning on any one draw give

\[
\operatorname{Cov}\bigl(X_u,\mathbf1\{X_v=0\}\bigr)
=Q_v\sum_{t:\,u,v\in S_t}\frac1{m_t(m_t-1)}=Q_vW_{uv}.
\]

For the same vertex, \(X_u\mathbf1\{X_u=0\}=0\), hence

\[
\operatorname{Cov}\bigl(X_u,\mathbf1\{X_u=0\}\bigr)=-Q_u\mu_u,
\qquad
\mu_u=\mathbb EX_u=\sum_{t:\,u\in S_t}\frac1{m_t}.
\]

For each draw containing \(u\), there are exactly \(m_t-1\) other eligible vertices, so \(\mu_u=\sum_{v\ne u}W_{uv}\). Summing the displayed individual covariances over all leaves yields

\[
\operatorname{Cov}(D_u,L)=\operatorname{Cov}(X_u,L)=\sum_{v\ne u}W_{uv}(Q_v-Q_u).
\]

The independent-draw description evaluates \(Q_v=q_{p(v)}\) and \(W_{uv}\) as in the Finding section. Since \(r-2>0\), every \(W_{uv}\) is strictly positive.

**3. Strict order of leaf probabilities and signs.** With \(N\) held fixed, let

\[
t(s)=\left(1-\frac1{N-s}\right)^{s-1}\qquad(1\le s\le N-2).
\]

As \(s\) increases, the positive base strictly decreases and its nonnegative exponent increases. Hence \(t(s)\) strictly decreases. Put \(B=(1-1/N)^{r-2}\prod_pt(n_p)>0\); then \(q_p=B/t(n_p)\). It follows that \(q_p\) strictly increases with \(n_p\). In the weighted covariance sum, every difference is nonnegative for a smallest-part vertex and at least one is positive when sizes differ; the converse holds for a largest-part vertex. Equal part sizes give equal leaf probabilities and zero covariances.

**4. Bipartite boundary.** For \(r=2\), the generating polynomial factors into separate polynomials in the vertices of \(V_1\) and \(V_2\), hence the excess-degree vectors in the two parts are independent. Within either part the tree degrees are exchangeable and have the deterministic sum \(N-1\), so each marked degree has covariance zero with its own part's leaf count. It has covariance zero with the other part's leaf count by independence. Therefore \(\operatorname{Cov}(D_u,L)=0\) for every bipartite spanning tree, including stars.

**5. Sign variability in nonextremal parts.** For each of \(K_{1,2,3}\) and \(K_{1,2,4}\), substitute the part sizes into the explicit \(q_p\) and \(W_{uv}\) expressions and sum the vertex contributions. The respective middle-part values are \(-11/1296\) and \(32/2205\), completing the exhibited contrast.

## Verification

The standalone script `verify.py` uses independent exact rational calculations and exhaustive ordinary Prüfer-code enumeration of trees for eight complete multipartite examples of up to seven vertices. It compares the enumerated tree counts and every marked-vertex degree–leaf covariance with the values from the independent categorical-draw formula, verifies opposite middle-class signs, and checks extreme-class signs for a further finite parameter grid. Run `python verify.py`; its current version prints `PASS 165 exact assertions`. Enumeration covers only the stated finite examples; the determinant and conditional-expectation arguments above prove the universal theorem.

## Relationship to prior work

The complete multipartite tree-count formula is classical, and the vertex-weighted Matrix–Tree method is a standard technique. Aldous (1990) studies uniform spanning-tree leaves and vertex degrees, and Martin–Reiner (2003) gives weighted tree-enumerator factorization methods for a different family, Cartesian products of complete graphs. Wang–Ge (2026) provides a more general complete-multipartite fixed-forest inclusion count. Such formulas can, in principle, supply all finite moments after differentiation and inclusion–exclusion, but their inspected statements do not present the exact degree–total-leaf Laplacian identity or its extremal-part sign classification. The new assertion is the dependence identity and its all-part-size sign consequences, **not** the underlying tree enumeration or its factorization.

## Limitations

No signs are asserted for intermediate-sized parts in general; the two examples show both possibilities. No joint stochastic ordering of total leaves conditional on degree is claimed. The historical-priority comparison was not exhaustive: Onadera's original complete-multipartite enumeration article was not inspected in full, and some older weighted-enumerator literature may contain implicit equivalent formulas.

## References

1. D. J. Aldous, *The random walk construction of uniform spanning trees and uniform labelled trees*, SIAM Journal on Discrete Mathematics 3 (1990), 450–465. DOI: 10.1137/0403039.
2. J. L. Martin and V. Reiner, *Factorizations of some weighted spanning tree enumerators*, preprint first posted 2003-02-18, arXiv:math/0302213.
3. W. Wang and J. Ge, *On enumeration of spanning trees of complete multipartite graphs containing a fixed spanning forest*, first posted 2026-02-03, arXiv:2602.03602.
4. R. Onadera, *On the number of trees in a complete n-partite graph*, Matrix and Tensor Quarterly 23 (1972–1973), 142–146; bibliographic record only, original full text not inspected.
5. N. Hartsfield and J. S. Werth, *Spanning Trees of the Complete Bipartite Graph*, in *Topics in Combinatorics and Graph Theory* (1990), 339–346. DOI: 10.1007/978-3-642-46908-4_38.
