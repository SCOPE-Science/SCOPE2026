# Edge conditioning creates rank-one negative degree dependence in uniform bipartite spanning trees

## Finding

Let \(T\) be a uniformly random spanning tree of the complete bipartite graph \(K_{a,b}\), with \(a,b\ge 2\), and mark one left vertex \(u\), one right vertex \(v\), and their joining edge \(e=uv\). Write \(D_u,D_v\) for their degrees in \(T\), and \(E=\{e\in T\}\). Put
\[
 A(s)=\frac{a-1+s}{a},\qquad B(t)=\frac{b-1+t}{b}.
\]
The **complete edge-conditioned bivariate probability generating functions** are
\[
\mathbb E[s^{D_u-1}t^{D_v-1}\mid E^c]
=A(s)^{b-2}B(t)^{a-2},
\]
\[
\mathbb E[s^{D_u-1}t^{D_v-1}\mid E]
=A(s)^{b-2}B(t)^{a-2}
\frac{(b-1)s+(a-1)t+st}{a+b-1}.
\]
There is therefore a common coupling. Let \(B_u\sim\operatorname{Bin}(b-2,1/a)\), \(B_v\sim\operatorname{Bin}(a-2,1/b)\) be independent. Conditional on \(E^c\), the degrees have the law \((1+B_u,1+B_v)\). Conditional on \(E\), they have the law
\[
 (D_u,D_v)\overset{d}{=}(1+B_u+U,\ 1+B_v+V),
\]
where \((U,V)\) is independent of the binomials and has exactly three atoms:
\[
\Pr((U,V)=(1,0))=\frac{b-1}{a+b-1},\quad
\Pr((U,V)=(0,1))=\frac{a-1}{a+b-1},\quad
\Pr((U,V)=(1,1))=\frac1{a+b-1}.
\]
The exceptional edge thus creates a **rank-one negative dependence law**. For any real-valued functions \(f\) and \(g\) on the corresponding finite degree supports, define \(\Delta f(k)=f(k+1)-f(k)\) and similarly \(\Delta g\). Then
\[
\operatorname{Cov}(f(D_u),g(D_v)\mid E)
=-\frac{(a-1)(b-1)}{(a+b-1)^2}
\mathbb E[\Delta f(1+B_u)]\mathbb E[\Delta g(1+B_v)].
\]
For all nondecreasing \(f,g\) this is nonpositive, and it is strictly negative whenever each function is nonconstant on its respective full degree support. Given \(E^c\) the degrees are independent; without conditioning they are independent as well. In particular,
\[
\operatorname{Cov}(D_u,D_v\mid E)
=-\frac{(a-1)(b-1)}{(a+b-1)^2}<0,
\qquad
\operatorname{Cov}(D_u,D_v\mid E^c)=
\operatorname{Cov}(D_u,D_v)=0.
\]
If \(a=b=r\to\infty\), the covariance given \(E\) tends to \(-1/4\) and the corresponding degree correlation tends to \(-1/5\): conditioning on a rare edge retains nonvanishing endpoint disassortativity.

## Assumptions and scope

All vertices and edges are labeled, \(a,b\ge2\) are arbitrary integers, and the tree is uniform over the \(a^{b-1}b^{a-1}\) spanning trees of \(K_{a,b}\). Each degree includes the marked edge when present. The graph is simple and unweighted in the claimed law. For the generating-function proof, positive auxiliary conductances are introduced; they are removed by setting their parameters to one. The conditional laws are meaningful because
\[
\Pr(E)=\frac{a+b-1}{ab},\qquad
\Pr(E^c)=\frac{(a-1)(b-1)}{ab}>0.
\]
The binomial parameters \((b-2,1/a)\) and \((a-2,1/b)\) permit zero trials. Tests \(f,g\) are arbitrary real functions on integer degree sets; no moment assumptions are needed beyond finiteness.

## Proof

**1. Weighted bipartite tree enumerator.** Assign positive conductance \(w_{ij}=x_i y_j\) to each cross-edge, where \(i\) ranges over the \(a\) left vertices and \(j\) over the \(b\) right vertices. Write \(X=\sum_i x_i\), \(Y=\sum_j y_j\). The weighted tree sum is
\[
\tau(x,y)=\Bigl(\prod_i x_i\Bigr)\Bigl(\prod_j y_j\Bigr)X^{b-1}Y^{a-1}.
\]
To verify it, delete any right-hand vertex \(j_0\) from the weighted Laplacian. The resulting block matrix has diagonal blocks \(Y\operatorname{diag}(x)\) and \(X\operatorname{diag}(y_j:j\ne j_0)\), with off-diagonal blocks \(-x(y_j:j\ne j_0)^\top\) and its transpose. The Schur complement is
\[
X\left[\operatorname{diag}(y_j:j\ne j_0)-Y^{-1}(y_j:j\ne j_0)(y_j:j\ne j_0)^\top\right].
\]
The matrix-determinant lemma gives its determinant as \(X^{b-1}(\prod_{j\ne j_0}y_j)y_{j_0}/Y\). Multiplying by the upper diagonal-block determinant \(Y^a\prod_i x_i\) establishes the stated tree sum by the matrix-tree theorem.

**2. Probability of the marked edge under vertex-product weights.** The electrical-network identity for tree-edge inclusion is \(\Pr(uv\in T)=w_{uv}R_{uv}\), where \(R_{uv}\) is effective resistance. Here one can verify directly that
\[
R_{uv}=\frac1{x_uY}+\frac1{y_vX}-\frac1{XY}.
\]
Indeed, send unit current from \(u\) to \(v\); writing vertex potentials \(h_i\) on the left and \(k_j\) on the right, let \(S_h=\sum_i x_i h_i\) and \(S_k=\sum_j y_jk_j\). Kirchhoff's laws are \(x_i(Yh_i-S_k)={\bf1}_{i=u}\) and \(y_j(Xk_j-S_h)=-{\bf1}_{j=v}\). Solving gives \(S_h/X-S_k/Y=1/(XY)\), hence \(h_u-k_v=R_{uv}\). Multiplication by \(w_{uv}=x_uy_v\) yields
\[
\Pr(uv\in T)=\frac{x_u}{X}+\frac{y_v}{Y}-\frac{x_uy_v}{XY}.
\]
For completeness, the electrical identity itself follows by differentiating \(\det L^{(j_0)}\) in the conductance of the marked edge: the determinant lemma gives the logarithmic derivative \(R_{uv}\), whereas directly differentiating the tree sum gives the probability divided by edge weight.

**3. Two conditioned generating functions.** Set \(x_u=s\), \(y_v=t\), with every other vertex weight one, initially for \(s,t>0\). By step 1, the normalized excess-degree pgf without edge conditioning is
\[
F(s,t)=A(s)^{b-1}B(t)^{a-1}.
\]
By step 2, the marked-edge probability under this tilt is
\[
 p(s,t)=\frac{s}{a-1+s}+\frac{t}{b-1+t}
-\frac{st}{(a-1+s)(b-1+t)}.
\]
Therefore, the unnormalized edge-present excess-degree pgf is \(F(s,t)p(s,t)\), and the edge-absent counterpart is \(F(s,t)(1-p(s,t))\). Direct cancellation yields
\[
 F(s,t)p(s,t)=A(s)^{b-2}B(t)^{a-2}
\frac{(b-1)s+(a-1)t+st}{ab},
\]
\[
 F(s,t)(1-p(s,t))=A(s)^{b-2}B(t)^{a-2}
\frac{(a-1)(b-1)}{ab}.
\]
At \(s=t=1\), these prefactors give the two stated edge probabilities. Dividing by them proves the two exact conditional pgfs, first for positive \(s,t\), then as polynomial identities for all formal arguments. The product of two binomial pgfs and the displayed three-atom polynomial yields the asserted couplings. The unconditioned pgf \(F(s,t)\) is a product, proving unconditional independence.

**4. Rank-one covariance and sign.** For any \(f\), conditional on \(U\), independent \(B_u\) gives
\[
 \mathbb E[f(1+B_u+U)\mid U]
 =\mathbb E[f(1+B_u)]+U\,\mathbb E[\Delta f(1+B_u)].
\]
The analogous formula holds for \(g\) and \(V\). By independence of the binomials and of their pair from \((U,V)\), the covariance factorizes into the two expected discrete derivatives times \(\operatorname{Cov}(U,V)\). But
\[
\mathbb E U=\frac b{a+b-1},\qquad
\mathbb E V=\frac a{a+b-1},\qquad
\mathbb E UV=\frac1{a+b-1},
\]
so \(\operatorname{Cov}(U,V)=-(a-1)(b-1)/(a+b-1)^2\). This proves the rank-one identity. A nondecreasing function which is nonconstant on the full degree support has strictly positive expected discrete difference, because each binomial has full support from zero through its number of trials; the strict negative assertion follows. Taking identity functions and using conditional independence under \(E^c\) gives the degree covariances.

**5. Balanced limit.** When \(a=b=r\to\infty\), both binomials converge to independent Poisson(1) variables, and the three-atom law converges to equal mass on \((1,0)\) and \((0,1)\). Thus conditional covariance tends to \(-1/4\). The conditional marginal variance is
\[
(r-2)\frac1r\left(1-\frac1r\right)
+\frac{r(r-1)}{(2r-1)^2}\ \longrightarrow\ \frac54.
\]
Dividing covariance by the marginal variance gives limiting correlation \(-1/5\).

## Verification

The included self-contained standard-library checker `verify_edge_degree.py` enumerates all labeled spanning trees of \(K_{a,b}\) for \(2\le a,b\le4\), independently reconstructs conditional empirical joint degree distributions as exact fractions, and compares them to the two formulas. It checks the exact tree counts, marked-edge probabilities and conditional covariances: 5,133 enumerated trees across nine parameter pairs. These finite tests cross-check definitions, normalizations and low-order boundary cases; they do not substitute for the all-parameter determinant and electrical proof above. Reproduce with `python verify_edge_degree.py`.

## Relationship to prior work

Dong and Ge (arXiv:2103.05294, first public version March 9, 2021) give a general exact count of bipartite spanning trees containing a fixed spanning forest; the present argument uses the standard weighted enumeration viewpoint but asks for a complete probability law of two marked vertex degrees under an edge-inclusion or edge-exclusion constraint. Rapoport (arXiv:2312.14992, 2023) supplies general joint-degree field formulas for spanning trees of arbitrary finite graphs and discusses neighboring vertices and edge constraints; such formulas furnish an in-principle general computational route, but the inspected work does not state these explicit bipartite three-atom and rank-one coupling identities. Sanmartín, Schnörr and Hamprecht (arXiv:2409.13472, 2024) give general Laplacian formulas for the moments and covariance of degrees in random spanning trees; consequently the mere existence or computability of second moments is not new here. The contribution assessed here is the fully factorized conditional distribution and its nonlinear negative-covariance classification, not general tree enumeration or a generic covariance algorithm.

## Limitations

This is a finite-graph statement specialized to complete bipartite host graphs, with a limit only for balanced growing sides. It is not asserted for arbitrary weighted bipartite trees or other fixed edges in general graphs. The formula is proved internally but has not undergone independent review. The possibility that earlier general joint-degree or bipartite Prüfer-code results contain an equivalent specialized factorization remains a historical-priority risk; the absence of a matching search hit is not evidence of uniqueness.

## References

1. F. Dong and J. Ge, *Counting spanning trees in a complete bipartite graph which contain a given spanning forest*, arXiv:2103.05294, first publicly submitted 2021-03-09; Journal of Graph Theory (2022).
2. A. Rapoport, *Correlations in uniform spanning trees: a fermionic approach*, arXiv:2312.14992, first publicly submitted 2023-12-22.
3. P. Sanmartín, C. Schnörr and F. A. Hamprecht, *Expectation and Variance of the Degree of a Node in Random Spanning Trees*, arXiv:2409.13472, first publicly submitted 2024-09-20.
4. Standard tools: Kirchhoff's matrix-tree theorem, the transfer-current/effective-resistance identity, and the matrix determinant lemma (used explicitly in the proof).
