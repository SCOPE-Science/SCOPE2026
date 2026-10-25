# Cubic suppression of endpoint normal cones in path Laplacian simplices

## Finding
For each integer \(n\ge5\), let \(L_n\) be the ordinary graph Laplacian of the path with consecutively numbered vertices \(1,\ldots,n\). In the Euclidean zero-sum hyperplane \(H_n=\{x\in\mathbb R^n:\sum_i x_i=0\}\), form its canonical Laplacian simplex
\[
T_n=\operatorname{conv}\{L_ne_1,\ldots,L_ne_n\}\subset H_n.
\]
For each vertex, let \(\omega_{n,i}\) be the normalized spherical measure of its outward normal cone, equivalently the probability it uniquely maximizes a uniformly random linear functional on \(H_n\). As \(n\to\infty\),
\[
\boxed{\omega_{n,1}=\omega_{n,n}\sim8\sqrt3\,\pi\,\frac{\log n}{n^3}},
\qquad
\boxed{\sup_{2\le i\le n-1}|n\omega_{n,i}-1|\longrightarrow0.}
\]
Hence the two endpoints together carry normal-cone mass asymptotic to \(16\sqrt3\,\pi(\log n)/n^3\), while every interior vertex has mass asymptotic to \(1/n\), including the vertices immediately next to the endpoints. This is a sharp boundary-versus-interior angular dichotomy, not a claim about equal finite-dimensional interior angles.

For comparison, let \(S_n\) be the canonical Laplacian simplex of the \(n\)-vertex star. The normal-cone mass of its hub tends to \(1/2\), and each leaf has mass asymptotic to \(1/(2n)\). In particular, lattice-unimodular equivalence of tree Laplacian simplices does not preserve the Euclidean normal-cone distribution.

## Assumptions and scope
The graphs are simple, connected, unweighted and undirected. All cones and spherical measures use the **canonical column-Laplacian embedding** with the usual Euclidean inner product on \(H_n\); a nonorthogonal lattice coordinate change would generally alter normal-cone angles. The random direction has Haar probability measure on the unit sphere in \(H_n\). Since the Laplacian of a connected graph has rank \(n-1\), the \(n\) displayed columns are affinely independent and ties occur with probability zero. The statement is asymptotic, not an identity at finite \(n\). The star comparison concerns only the hub/leaf orbits.

Set \(\Phi\) and \(\varphi\) to be the standard normal distribution and density, respectively, and \(\varphi_s(t)=s^{-1}\varphi(t/s)\). Define \(u_n=\Phi^{-1}(1-1/n)\) and \(t_n(y)=\sqrt6(u_n+y/u_n)\).

## Proof
**Gaussian normal-cone representation.** For independent standard Gaussian variables \(g_1,\ldots,g_n\), maximize the scores \(X_i=\langle g,L_ne_i\rangle\). Since \(L_ne_i\in H_n\), replacing \(g\) by its orthogonal projection onto \(H_n\) changes no score. The projected Gaussian direction is uniformly spherical. Thus \(\omega_{n,i}=\Pr(X_i=\max_jX_j)\). Explicitly,
\[
X_1=g_1-g_2,\quad X_n=g_n-g_{n-1},\quad
X_i=2g_i-g_{i-1}-g_{i+1}\quad(2\le i\le n-1).
\]
The endpoint variance is \(2\), and each interior variance is \(6\). For interior indices, correlations at lags one and two are \(-2/3\) and \(1/6\), and scores separated by three or more indices are independent. At the left endpoint, \(\operatorname{Cov}(X_1,X_2)=-3\), \(\operatorname{Cov}(X_1,X_3)=1\), and \(X_1\) is independent of every \(X_j\) for \(j\ge4\). Reflection interchanges the two endpoints.

**The interior extreme-value law.** Let \(I_n\) be any subset of \(\{2,\ldots,n-1\}\) obtained by removing at most a fixed number of indices, and write \(M_{I_n}=\max_{i\in I_n}X_i\). Then, uniformly over those choices of removed indices, for every fixed \(y\in\mathbb R\),
\[
\Pr(M_{I_n}\le t_n(y))\longrightarrow F(y):=\exp(-e^{-y}).\tag{1}
\]
Here \(n\Pr\{N(0,6)>t_n(y)\}\to e^{-y}\). For completeness, divide the sequence into consecutive blocks of length \(b_n=\lfloor(\log n)^2\rfloor\), separated by two omitted indices. The separated blocks are independent, and the omitted indices have total exceedance probability \(O(1/b_n)\). Within a block, the total of independent-pair double-exceedance probabilities is \(O(b_n^2/n^2)\); the at-most-two-dependent neighbors per index contribute \(o(b_n/n)\) by the bivariate Gaussian bound
\[
\Pr(Y>t,Z>t)\le\Pr(Y+Z>2t)
\le \exp\!\left[-\frac{t^2}{6(1+\rho)}\right]
\]
for two variance-\(6\) Gaussians with correlation \(\rho\le1/6\) at positive distance at most two (at lag one, \(\rho=-2/3\), which makes the bound stronger). Since \(t_n(y)^2=(12+o(1))\log n\), these probabilities are at most \(n^{-12/7+o(1)}\). Bonferroni therefore makes one block's exceedance probability \(b_ne^{-y}/n(1+o(1))\). Multiplying the independent block-survival probabilities proves (1), including uniformity under finitely many deleted sites.

**Sharp endpoint mass.** Put \(R_n=\max_{4\le j\le n-1}X_j\), which is independent of \(X_1\). Changing variables \(x=t_n(y)\) gives
\[
\Pr(X_1>R_n)=\int_{\mathbb R}\Pr(R_n\le t_n(y))
\frac{\sqrt6}{u_n}\varphi_{\sqrt2}(t_n(y))\,dy.\tag{2}
\]
Mills' ratio, together with \(\varphi(u_n)\sim u_n/n\) and \(u_n^2\sim2\log n\), gives the pointwise density limit
\[
\frac{n^3}{\log n}\frac{\sqrt6}{u_n}\varphi_{\sqrt2}(t_n(y))
\longrightarrow4\sqrt3\,\pi e^{-3y}.\tag{3}
\]
To justify integrating (3), for \(y\ge0\) the normalized integrand is bounded by a constant times \(e^{-3y}\). For \(-u_n^2/2\le y\le0\), choose every third interior score; these are independent and yield, by Mills' inequalities,
\[
\Pr(R_n\le t_n(y))\le\exp[-c\exp(-3y/4)]
\]
with absolute \(c>0\) for all sufficiently large \(n\). The normalized density factor is at most \(Ce^{-3y}\), so this left side is integrably dominated. For \(y<-u_n^2/2\), the entire unnormalized contribution is at most \(\Phi(u_n/2)^{\lfloor(n-6)/3\rfloor}\), which is smaller than every power of \(n^{-1}\). Dominated convergence and \(z=e^{-y}\) give
\[
\begin{aligned}
\lim_{n\to\infty}\frac{n^3}{\log n}\Pr(X_1>R_n)
&=4\sqrt3\,\pi\int_{\mathbb R}e^{-3y-e^{-y}}\,dy\\
&=4\sqrt3\,\pi\int_0^\infty z^2e^{-z}\,dz
=8\sqrt3\,\pi.\tag{4}
\end{aligned}
\]

Restoring the three omitted competitors does not affect this scale. Indeed, conditional on \(X_1=x\), \(X_2\) is normal with mean \(-3x/2\) and variance \(3/2\), while \(X_3\) is normal with mean \(x/2\) and variance \(11/2\). For each fixed \(K>0\), conditional tail bounds show that, on \(X_1>t_n(-K)\), the probability that either defeats \(X_1\) is at most \(n^{-\delta+o(1)}\) for some \(\delta>0\). Thus their joint exceptional probability is \(o(n^{-3}\log n)\). The part of (2) with \(X_1\le t_n(-K)\), once normalized, tends to a quantity tending to zero as \(K\to\infty\) by the left-tail domination above. Finally, \(X_n\) is independent of \(X_1\), and its probability of exceeding \(X_1>t_n(-K)\) is \(O_K(n^{-3}\log n)\), negligible after multiplication by the endpoint exceedance probability. Hence \(\omega_{n,1}\sim\Pr(X_1>R_n)\), establishing the first boxed formula.

**Uniform interior mass.** For each interior \(i\), remove the at most four other interior indices within distance two and call the maximum of the remaining interior scores \(R_{n,i}\). This maximum is independent of \(X_i\), and (1) holds uniformly in \(i\). The same integral argument, now with the variance-\(6\) density, gives
\[
\frac{n\sqrt6}{u_n}\varphi_{\sqrt6}(t_n(y))\longrightarrow e^{-y},
\qquad
n\Pr(X_i>R_{n,i})\longrightarrow\int_{\mathbb R}e^{-y-e^{-y}}\,dy=1
\]
uniformly over \(2\le i\le n-1\). Uniform integrable domination follows from the identical independent-subsequence argument. Conditional on \(X_i=x\) with \(x\ge t_n(-K)\), every omitted nearby interior score has conditional mean \(\rho x\) for \(\rho\in\{-2/3,1/6\}\) and strictly smaller-than-one regression coefficient. Nearby endpoint scores have conditional regression coefficient at most \(1/6\), with bounded residual variance. Each therefore beats \(X_i\) with conditional probability \(n^{-\delta+o(1)}\), uniformly in \(i\). Distant endpoints are independent of \(X_i\) and have smaller variance. The left tail is handled as above. Consequently \(n\omega_{n,i}\to1\) uniformly, completing the path assertion.

**Star comparison.** Write the hub Gaussian coordinate as \(g_0\) and the leaves as \(g_1,\ldots,g_{n-1}\). The exposed-vertex scores are \(X_0=(n-1)g_0-\sum_{j=1}^{n-1}g_j\) and \(X_j=g_j-g_0\). The hub wins exactly when
\[
g_0>\frac{\sum_{j=1}^{n-1}g_j+\max_{1\le j\le n-1}g_j}{n}.
\]
The right side tends to zero in probability (indeed almost surely under the natural infinite coupling); it is independent of \(g_0\). Thus the hub angle tends to \(\Pr(g_0>0)=1/2\). Symmetry splits the remaining mass equally among the \(n-1\) leaves, giving the stated leaf limit.

## Verification
The standalone `verify.py` checks the exact path Laplacian score covariance matrix with integer arithmetic for dimensions \(5\) through \(89\). Direct Gaussian sampling and an independent conditional importance-sampling integral agree within six combined standard errors at dimensions \(24,60,100\). Weighted rare-event diagnostics are also reported at dimensions \(100,300,1000\), and the star-hub probability is checked numerically at dimensions \(100,1000\). The finite samples do not establish the sharp asymptotic constant or uniform interior limit; these follow from the preceding analytical bounds.

To reproduce: `OPENBLAS_NUM_THREADS=1 python verify.py` with NumPy and SciPy installed. The script uses fixed pseudorandom seeds and reports diagnostics and assertions.

## Relationship to prior work
Braun and Meyer introduced Laplacian simplices and established that all tree examples of a fixed dimension are lattice-unimodularly equivalent (in particular, their Proposition 4.1). Their results concern lattice structure, reflexivity, and Ehrhart invariants, not the spherical normal-cone weights of the canonical Euclidean embedding. Meyer and Pllaha investigate reflexive Laplacian simplices through coding theory and Ehrhart theory, without deriving path endpoint exposure asymptotics. An accessible later study of Euclidean inradii of tree Laplacian simplices gives polynomially different inradius scales for paths and stars, but no statement about directionally exposed vertices or their normal-cone probabilities. Those metric phenomena neither imply nor subsume the cubic rare-angle formula here.

Classical extreme-value arguments for finite-dependent Gaussian sequences explain the Gumbel law for the interior maximum, but the stated geometric separation requires additionally the variance-mismatched endpoint density, its exact gamma-integral coefficient, control of local correlations, and comparison with the star embedding. The result is not a new general Gaussian extreme-value theorem.

## Limitations
The asymptotic is proved only for the unweighted path and star families in their canonical Euclidean embeddings; it does not classify angular distributions for arbitrary trees or weighted paths. The statement provides the sharp leading endpoint scale, not a finite-dimensional exact angle formula or a uniform relative error bound. Numeric diagnostics converge slowly and do not independently validate the infinite-dimensional limit. A bibliographically unindexed treatment of finite-dependent, unequal-variance Gaussian argmax probabilities could potentially contain a mathematically equivalent special case; the available literature search is not a proof of absolute priority.

## References
1. Benjamin Braun and Marie Meyer, *Laplacian Simplices*, arXiv:1706.07085v1, first public 2017-06-21, especially Section 4 and Proposition 4.1.
2. Marie Meyer and Tefjol Pllaha, *Laplacian Simplices II: A Coding Theoretic Approach*, arXiv:1809.02960v1, first public 2018-09-09.
3. Adam Jakubowski and N. Soja-Kukieła, *Managing local dependencies in asymptotic theory for maxima of stationary random fields*, *Extremes* 22 (2019), 293–315, DOI 10.1007/s10687-018-0336-6 (background for local-dependence extremes, not the rare endpoint formula).
4. *Tree Laplacian simplices exhibit sharp, lattice-invisible Euclidean inradius exponents*, publicly indexed mathematical research note (2026), different Euclidean invariant.
