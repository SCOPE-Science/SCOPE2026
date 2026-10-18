# Sharp concentration crossover for affine Dirichlet polynomial projection

## Finding

Let \(n\ge 2\) and \(a>0\). Let \(\mu_{n,a}\) be the symmetric Dirichlet probability measure with \(n\) parameters all equal to \(a\), on the probability simplex \(\Delta_{n-1}\). Let \(P_{n,a}\) be orthogonal projection in \(L^2(\mu_{n,a})\) onto the affine functions. Put \(\lambda=na\), \(b=(n-1)a\), and \(t=a/(\lambda+1)\). Write \(I_t(u,v)\) for the regularized incomplete beta function.

The exact sharp endpoint operator norms coincide and are
\[
\boxed{\|P_{n,a}\|_{L^1\to L^1}=\|P_{n,a}\|_{L^\infty\to L^\infty}=1+2\left[\lambda I_t(a,b)-(\lambda+1)I_t(a+1,b)\right].}
\]
In particular, \(1<\|P_{n,a}\|<1+2\lambda\). Every simplex vertex maximizes the Lebesgue function (uniqueness of maximizers is not asserted).

Let \(G_a\) have the unit-scale Gamma distribution of shape \(a\), and write \(g(a)=\mathbb E|G_a-a|=2a^ae^{-a}/\Gamma(a)\). For every \(n\ge2\) and \(a>0\), the dimension-uniform coupling estimate is
\[
\boxed{\left|\frac{\|P_{n,a}\|}{n}-g(a)\right|\le\frac{\sqrt{na+1}}{n}.}
\]
For any positive sequence \(a_n\), the two concentration regimes are:

* If \(na_n\to c\in[0,\infty)\), then \(\|P_{n,a_n}\|\to1+2c\).
* If \(na_n\to\infty\), then \(\|P_{n,a_n}\|\sim n g(a_n)\to\infty\).

Consequently \(\sup_{n\ge2}\|P_{n,a_n}\|<\infty\) if and only if \(\sup_{n\ge2}na_n<\infty\). In the divergent-total-concentration regime, fixed \(a_n\to a_0>0\) gives \(\|P_{n,a_n}\|/n\to g(a_0)\), while \(a_n\to0\) gives \(\|P_{n,a_n}\|\sim2na_n\), and \(a_n\to\infty\) gives \(\|P_{n,a_n}\|\sim n\sqrt{2a_n/\pi}\).

## Assumptions and scope

The simplex is \(\Delta_{n-1}=\{x\in[0,1]^n:\sum_i x_i=1\}\), with the normalized probability measure \(\mu_{n,a}=\operatorname{Dirichlet}(a,\ldots,a)\). All projector norms use this probability measure on both domain and codomain. The measure has strictly positive density on the relative interior, so continuous kernel evaluations at boundary vertices determine the essential-supremum norm. The dimension variable \(n\) counts barycentric coordinates, not intrinsic dimension (which is \(n-1\)). The parameter \(a\) can depend arbitrarily on \(n\); the asymptotic statements require only the stated regimes.

## Proof

**1. Reproducing kernel and sharp norm.** For \(X\sim\mu_{n,a}\), the Dirichlet covariance matrix is
\[
\operatorname{Cov}(X)=\frac{1}{n(\lambda+1)}\left(I-\frac{\boldsymbol{1}\boldsymbol{1}^{\mathsf T}}n\right).
\]
Inverting this covariance on the mean-zero coordinate hyperplane, and including the normalized constant function, yields the affine projection kernel
\[
K(x,y)=1+n(\lambda+1)\sum_{i=1}^n\left(x_i-\frac1n\right)\left(y_i-\frac1n\right).
\]
The Lebesgue function \(\Lambda(x)=\int|K(x,y)|\,d\mu_{n,a}(y)\) is convex in \(x\), being an average of absolute values of affine functions. Every point in the simplex is a convex combination of vertices; consequently \(\max_x\Lambda(x)\) is the common vertex value. At the first vertex \(e_1\),
\[
K(e_1,y)=n(\lambda+1)y_1-\lambda.
\]
The marginal \(Y=X_1\) is \(\operatorname{Beta}(a,b)\), with \(\mathbb EY=1/n\), and \(\mathbb EK(e_1,X)=1\). Thus
\[
\|P_{n,a}\|_{\infty\to\infty}=\mathbb E|n(\lambda+1)Y-\lambda|=1+2\mathbb E(\lambda-n(\lambda+1)Y)_+.
\]
The sign changes exactly at \(t=a/(\lambda+1)\). Integrating the beta density on \([0,t]\), and using \(\mathbb E[Y\mathbf1_{Y<t}]=(a/\lambda)I_t(a+1,b)\), proves the displayed exact formula. The kernel is symmetric, hence the \(L^1\) and \(L^\infty\) operator norms coincide. Since the beta density is positive on both sides of \(t\), and \(0<(\lambda-n(\lambda+1)Y)_+<\lambda\) on the negative region, the strict bounds follow.

**2. Gamma coupling.** Let \(S\sim\operatorname{Gamma}(\lambda,1)\) be independent of \(Y\sim\operatorname{Beta}(a,\lambda-a)\). Beta–gamma algebra gives \(YS\stackrel{d}{=}G_a\sim\operatorname{Gamma}(a,1)\). Divide the vertex-kernel identity by \(n\), to obtain
\[
\frac{\|P_{n,a}\|}{n}=\mathbb E\left|(\lambda+1)Y-a\right|.
\]
By the elementary reverse triangle inequality and independence,
\[
\left|\mathbb E| (\lambda+1)Y-a|-\mathbb E|YS-a|\right|
\le\mathbb E[Y|S-(\lambda+1)|]=\frac1n\mathbb E|S-(\lambda+1)|.
\]
Since \(\mathbb ES=\lambda\) and \(\operatorname{Var}S=\lambda\), Cauchy–Schwarz gives the bound \(\mathbb E|S-(\lambda+1)|\le\sqrt{\lambda+1}\). The gamma absolute-deviation identity follows by splitting at \(a\) and using \(\Gamma(a+1)=a\Gamma(a)\): \(\mathbb E|G_a-a|=2a^ae^{-a}/\Gamma(a)\).

**3. Finite-total-concentration regime.** Suppose \(\lambda_n=na_n\to c\ge0\). Since \(K(e_1,Y)\ge-\lambda_n\), the preceding formula gives \(1\le L_{n,a_n}\le1+2\lambda_n\). This proves the \(c=0\) case. If \(c>0\), then \(a_n\to0\), \(t_n=a_n/(\lambda_n+1)\asymp n^{-1}\). Fix any \(r\in(0,1)\). The beta-moment formula gives
\[
\mathbb E[Y^r]=\frac{\Gamma(a_n+r)\Gamma(\lambda_n)}{\Gamma(a_n)\Gamma(\lambda_n+r)}=O(n^{-1}).
\]
Markov's inequality implies \(\mathbb P(Y>\varepsilon t_n)=O(n^{r-1})\to0\) for each fixed \(\varepsilon>0\). Hence \(n(\lambda_n+1)Y\to0\) in probability. The bounded random variables \((\lambda_n-n(\lambda_n+1)Y)_+\) therefore converge in expectation to \(c\), proving \(L_{n,a_n}\to1+2c\).

**4. Divergent-total-concentration regime.** Stirling's formula and the gamma function's limit at the origin yield positive constants \(c_1,c_2\) such that
\[
c_1\min\{a,\sqrt a\}\le g(a)\le c_2\min\{a,\sqrt a\},\qquad a>0,
\]
with \(g(a)\sim2a\) as \(a\downarrow0\) and \(g(a)\sim\sqrt{2a/\pi}\) as \(a\to\infty\). Dividing the coupling bound by \(g(a)\), for \(a\le1\) the relative error is \(O((na)^{-1/2}+(na)^{-1})\), while for \(a\ge1\) it is \(O(n^{-1/2})\). Both vanish when \(n\to\infty\) and \(na\to\infty\). This proves \(L_{n,a}\sim n g(a)\) and all asserted subregime asymptotics. Moreover \(n g(a)\) diverges along any sequence \(na\to\infty\), by the same positive lower bounds. If the total concentration sequence is merely unbounded, it possesses such a divergent subsequence, yielding the boundedness equivalence.

## Verification

The supplementary reproducibility script `CHECK.py` evaluates the incomplete-beta formula and its integration-by-parts equivalent, compares both with independently computed beta-density quadrature, verifies the gamma coupling bound, tests the uniform-weight specialization, and evaluates representative concentration regimes. Its finite numerical checks support the exact identities only; the universal inequalities and infinite-dimensional conclusions follow from the proof above. Run using Python with SciPy and NumPy installed: `python CHECK.py`.

## Relationship to prior work

Griffiths and Spanò [1] develop orthogonal polynomial kernels for Dirichlet measures and their infinite-dimensional distributional limits; the affine projector kernel is a degree-at-most-one special case of that framework. Aktaş and Xu [2] examine orthogonal polynomial systems with simplex weights, including singular boundary constructions. The prior exact unweighted simplex projector norm [4] is recovered at \(a=1\):
\[
\|P_{n,1}\|=2n\left(\frac n{n+1}\right)^{n-1}-1.
\]
The claims here concern the sharp concentration-dependent endpoint norms, a dimension-uniform gamma coupling, and the distinction between bounded and divergent total Dirichlet concentration. Neither the cited general kernel framework nor the published unweighted special case alone determines those statements. Chernov's related trace-estimate article [3] does not supply a verified complete comparison because only its abstract was accessible. The present claims are not asserted to have independently established historical priority.

## Limitations

The weight parameters must be equal and positive. No assertion is made for unequal Dirichlet parameters, higher-degree polynomial spaces, or discrete sampling operators. The exact formula itself is elementary once the affine kernel is known; the broader asserted contribution is the sharp all-scale high-dimensional dichotomy with a uniform quantitative coupling. Historical equivalence under different terminology remains a residual bibliographic risk. The checks are same-model only, not independent mathematical certification.

## References

[1] R. C. Griffiths and D. Spanò, “Orthogonal polynomial kernels and canonical correlations for Dirichlet measures,” arXiv:1003.5131 (first public 2010-03-26), https://arxiv.org/abs/1003.5131.

[2] R. Aktaş and Y. Xu, “Sobolev orthogonal polynomials on a simplex,” arXiv:1111.2994 (first public 2011-11-13), https://arxiv.org/abs/1111.2994.

[3] A. Chernov, “Optimal convergence estimates for the trace of the polynomial \(L^2\)-projection operator on a simplex,” *Mathematics of Computation* 81 (2012); https://doi.org/10.1090/S0025-5718-2011-02513-5 (only abstract inspected).

[4] “Exact positivity defect and max norm of the affine least-squares projector on a simplex,” public mathematical result, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 (public summary inspected).
