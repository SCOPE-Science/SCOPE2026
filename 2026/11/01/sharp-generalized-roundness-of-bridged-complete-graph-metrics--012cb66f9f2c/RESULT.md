# Sharp generalized roundness of bridged complete-graph metrics

## Finding
Let \(q,r\ge1\) be integers. Join one distinguished vertex of \(K_{q+1}\) to one distinguished vertex of \(K_{r+1}\) by exactly one unit-length bridge, and equip all \(q+r+2\) vertices with shortest-path distance \(d\). For \(p>0\), write \(D_p=(d(x,y)^p)_{x,y}\). Define
\[
\beta(p)=\frac{(2^p-2)^2}{2},\qquad z(p)=\frac{4^p+2}{2}-3^p,
\]
\[
\delta_{q,r}=\frac1{2q}-\frac1{2r},\qquad
\gamma_{q,r}=1+\frac1{2q}+\frac1{2r}.
\]
There is a unique \(\wp_{q,r}\in(1,2]\) solving
\[
\boxed{\beta(\wp_{q,r})+
\sqrt{\delta_{q,r}^{\,2}+z(\wp_{q,r})^2}=\gamma_{q,r}.}
\]
It equals \(2\) precisely for \(q=r=1\); otherwise it lies strictly between \(1\) and \(2\). The metric has strict \(p\)-negative type for every \(0<p<\wp_{q,r}\), non-strict \(\wp_{q,r}\)-negative type, and no \(p\)-negative type for \(p>\wp_{q,r}\). Thus \(\wp_{q,r}\) is its exact supremal negative-type exponent, equivalently maximal generalized roundness.

If \((q,r)\ne(1,1)\), the equality space within \(\mathbf1^\perp\) at the endpoint is one-dimensional. The minimum Euclidean dimension of the snowflaked metric \(d^{p/2}\) is \(q+r+1\) for \(0<p<\wp_{q,r}\) and \(q+r\) at the endpoint. For \(q=r=1\) (the four-vertex path), the endpoint equality space is two-dimensional and the minimum dimension is \(1\).

The exponent decreases strictly when either \(q\) or \(r\) increases. When both grow without restriction on their ratio,
\[
\wp_{q,r}=p_\infty+
\frac{q^{-1}+r^{-1}}{2\,3^{p_\infty}\log(3/2)}
+O\bigl((q^{-1}+r^{-1})^2\bigr),
\qquad p_\infty=\frac{\log2}{\log(3/2)}=1.709511291351\ldots.
\]
For balanced cliques, \(q=r\), the endpoint equation simplifies to
\[
3^{\wp_{q,q}}-2\,2^{\wp_{q,q}}=\frac1q.
\]
For example, \(\wp_{2,2}=1.872408640681\ldots\) and \(\wp_{1,2}=1.895409801952\ldots\).

## Assumptions and scope
Every graph edge has length one, including the unique bridge; distances are shortest-path distances on **all** vertices, not electrical resistances. Positive integer parameters \(q,r\) count non-bridge vertices in the two cliques, so both clique sizes are at least two. Negative type means that for every real zero-sum vector \(\alpha\), \(\alpha^\top D_p\alpha\le0\); strict negative type means strict inequality whenever \(\alpha\ne0\). The theorem concerns all such integers and all real exponents in the stated ranges. No graph with a longer bridge path, nonuniform edges, or additional cross-edges is included.

## Proof
**1. Exact quadratic-form reduction.** Label the bridge endpoints \(u,v\), the \(q\) other left vertices \(a_i\), and the \(r\) other right vertices \(b_j\). For a zero-sum \(\alpha\), put
\[
X=\sum_i\alpha_{a_i},\quad Y=\sum_j\alpha_{b_j},\quad
S=\alpha_u+X=-\alpha_v-Y,
\]
\[
e_i=\alpha_{a_i}-X/q,\qquad f_j=\alpha_{b_j}-Y/r.
\]
The only nonzero distances are \(1\) inside either clique or across the bridge, \(2\) from a non-bridge vertex to the opposite bridge endpoint, and \(3\) between non-bridge vertices in different cliques. Expanding all pair contributions, with \(h=2^p\), yields the exact identity
\[
\begin{aligned}
\alpha^\top D_p\alpha={}&-\sum_i e_i^2-\sum_j f_j^2
-2\left(S+\frac{h-2}{2}(X-Y)\right)^2\\
&-\begin{pmatrix}X&Y\end{pmatrix}
M_{q,r}(p)\binom XY,
\end{aligned}
\]
where
\[
M_{q,r}(p)=
\begin{pmatrix}
1+q^{-1}-\beta(p)&z(p)\\
z(p)&1+r^{-1}-\beta(p)
\end{pmatrix}.
\]
Every real pair \((X,Y)\) and the scalar \(S\) are realizable by zero-sum coefficients; the fluctuations \(e_i,f_j\) have zero class sums. Thus the metric has \(p\)-negative type exactly when \(M_{q,r}(p)\) is positive semidefinite, and strict negative type exactly when it is positive definite.

**2. The unique crossing.** The smaller eigenvalue of this symmetric two-by-two matrix is
\[
\lambda_{-}(p)=\gamma_{q,r}-\beta(p)
-\sqrt{\delta_{q,r}^{\,2}+z(p)^2}.
\]
At \(p=1\), \(\beta=z=0\), so \(\lambda_-(1)=\gamma_{q,r}-|\delta_{q,r}|>0\). At \(p=2\), \(\beta=2\) and \(z=0\), giving \(\lambda_-(2)=\gamma_{q,r}-2-|\delta_{q,r}|\le0\), with equality only when \(q=r=1\).

To see strict monotonicity of \(\Phi(p)=\beta(p)+\sqrt{\delta_{q,r}^{\,2}+z(p)^2}\) for \(1<p<2\), first note that \(g(p)=2\,3^p-4^p-2\) vanishes at \(p=1,2\) and is positive between them. Indeed \(g'(p)=2(\log3)3^p-(\log4)4^p\) has exactly one real zero, with a positive sign at \(1\) and a negative sign at \(2\). Hence \(z(p)=-g(p)/2<0\). Furthermore
\[
\beta'(p)-z'(p)=3^p\log3-2\,2^p\log2>0
\qquad(p\ge1),
\]
since \(3\log3>4\log2\) and the relevant power ratio grows with \(p\). If \(z'(p)\le0\), then \(\Phi'(p)>0\). If \(z'(p)>0\), then \(\Phi'(p)\ge\beta'(p)-z'(p)>0\). There is therefore exactly one crossing in \((1,2]\). Before it both eigenvalues of \(M_{q,r}(p)\) are positive. At the crossing the smaller eigenvalue is zero and the larger is positive, except that \(q=r=1\) gives \(M_{1,1}(2)=0\). After it and up to \(2\) the smaller eigenvalue is negative. For \(p>2\), \(\beta(p)>2\), so each diagonal entry of \(M_{q,r}(p)\) is negative, immediately ruling out positive semidefiniteness.

The strictness below \(1\) follows from the general strictness propagation theorem: positive \(p_0\)-negative type of a metric gives strict \(p\)-negative type for every \(0<p<p_0\). One proof applies the Laplace representation of fractional powers to the positive Gaussian kernels induced by the \(p_0\)-negative-type metric; see Li--Weston, Theorem 5.4. This establishes the complete exponent classification.

**3. Equality vectors and Euclidean dimensions.** For \((q,r)\ne(1,1)\), one has \(z(\wp_{q,r})<0\). Thus \(M_{q,r}(\wp_{q,r})\) is positive semidefinite with a one-dimensional kernel spanned by a vector \((X,Y)\) with both entries nonzero, determined by
\[
(1+q^{-1}-\beta(\wp_{q,r}))X+z(\wp_{q,r})Y=0.
\]
Equality in the complete quadratic form additionally requires \(e_i=f_j=0\) and
\[
S=-\frac{2^{\wp_{q,r}}-2}{2}(X-Y).
\]
Consequently the equality coefficients are precisely
\[
\alpha_{a_i}=X/q,\quad \alpha_{b_j}=Y/r,\quad
\alpha_u=S-X,\quad\alpha_v=-S-Y
\]
up to common scaling. For \(q=r=1\) at \(p=2\), both Schur-complement eigenvalues vanish, giving a two-dimensional equality space. Schoenberg's finite-distance criterion states that the centered Gram matrix \(-\tfrac12 JD_pJ\) is positive semidefinite precisely for \(p\)-negative type, with rank equal to the least Euclidean dimension of \(d^{p/2}\). Its kernel on the zero-sum space is exactly the equality space just found, proving the dimension statements.

**4. Size monotonicity and asymptotics.** Increasing \(q\) strictly decreases the upper-left entry of \(M_{q,r}(p)\), and increasing \(r\) similarly decreases the lower-right entry. At a nonexceptional endpoint, a kernel vector has neither coordinate zero because \(z<0\); its Rayleigh quotient becomes strictly negative after either increase. Hence the new threshold is strictly smaller. At the exceptional endpoint \((q,r,p)=(1,1,2)\), either increase makes a diagonal entry negative, with the same conclusion.

As \(q,r\to\infty\), the endpoint equation becomes \(\beta(p)+|z(p)|=1\), or equivalently \(3^p=2\,2^p\) in \((1,2)\). The unique solution is \(p_\infty\) above. Near that exponent the smaller eigenvalue is a smooth function of \(q^{-1},r^{-1},p\), with derivative in \(p\) equal to \(-3^{p_\infty}\log(3/2)\ne0\) and first-order variation \((q^{-1}+r^{-1})/2\). Taylor's theorem gives the stated uniform two-parameter asymptotic expansion. For equal sizes the Schur-complement kernel is \((1,1)\), so its scalar equation reduces to \(3^p-2\,2^p=1/q\).

## Verification
The accompanying `verify_bridge_barbells.py` constructs shortest-path matrices independently of the proof and uses exact rational arithmetic to check the quadratic-form identity for 525 coefficient/exponent/size configurations (all \(1\le q,r\le5\), exponents \(1,2,3\), seven coefficient configurations each). It also compares the root equation with directly centered Gram eigenvalues for 100 integer size pairs, tests 81 strict monotonicity comparisons, and checks the asymptotic approximation on five larger pairs. The final output is `ALL_BRIDGE_BARBELL_CHECKS_OK`. Finite computation corroborates but does not establish the infinite-family theorem; the algebra and inequalities above do.

## Relationship to prior work
Li and Weston establish strict negative-type propagation, but no evaluated barbell thresholds. Sánchez gives a general matrix criterion for finite metric spaces and an evaluated complete-bipartite example, not the two-clique bridge family. Aalipour and coauthors study *exactly the same bridge-barbell graph family* at distance exponent one; their Section 5 determines determinants and ordinary distance-matrix inertia, not the sharp exponent, powered-distance conditional definiteness, equality spaces, or asymptotic law. In particular, their ordinary inertia theorem does not determine when powers of distances cease to be conditionally negative definite. The formulas here depend nontrivially on both \(2^p\) and \(3^p\). The explicit complete two-parameter exponent classification is the contribution; the general matrix method and ordinary distance spectrum are not claimed new.

## Limitations
All edges have unit length and the two cliques meet through a single edge; no assertion is made for weighted bridges, longer connecting paths, or extra cross-edges. The theorem classifies negative type, not the full inertia of powered-distance matrices for all exponents above the threshold. The apparent absence of a previously evaluated formula is based on the cited primary texts and targeted record searches; it is not a proof of publication priority.

## References
1. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first public version 2009-01-06), especially Theorem 5.4. https://arxiv.org/abs/0901.0695
2. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first public version 2011-08-02), especially Corollary 2.4 and Theorem 3.1. https://arxiv.org/abs/1108.0451
3. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196 (first public version 2015-09-03), especially Section 5, Theorems 5.1--5.2. https://arxiv.org/abs/1509.01196
