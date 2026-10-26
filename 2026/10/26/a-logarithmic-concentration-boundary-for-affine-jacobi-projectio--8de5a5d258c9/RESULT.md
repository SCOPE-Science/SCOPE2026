# A logarithmic concentration boundary for affine Jacobi projection norms
## Finding
Let \(n\ge2\) be an integer, \(\alpha>0\), and let \(\mu_{n,\alpha}\) be the symmetric Dirichlet probability measure of concentration \(\alpha\) on the barycentric simplex
\[
\Delta_{n-1}=\{x\in[0,1]^n:\ \sum_{i=1}^n x_i=1\}.
\]
Let \(P_{n,\alpha}\) be the \(L^2(\mu_{n,\alpha})\)-orthogonal projector onto the affine functions, regarded also as a bounded integral operator on \(L^1\) and \(L^\infty\). Define
\[
c=\frac{\alpha}{n\alpha+1},\qquad b=(n-1)\alpha,\qquad
C_{n,\alpha}=\frac{n\alpha+1}{\alpha}\frac{c^\alpha(1-c)^b}{B(\alpha,b)}-I_c(\alpha,b),
\]
where \(B\) is the beta function and \(I_c\) the regularized incomplete beta integral. Then the **exact** two endpoint operator norms and sharp loss of positivity are
\[
\boxed{\|P_{n,\alpha}\|_{1\to1}=\|P_{n,\alpha}\|_{\infty\to\infty}=1+2C_{n,\alpha},}\qquad
\boxed{\min_{0\le f\le1}\min_{x\in\Delta_{n-1}}P_{n,\alpha}f(x)=-C_{n,\alpha}.}
\]
Every output vertex is an extremizing evaluation point; no nonvertex is. An extremizing input is the indicator of the corresponding coordinate being smaller than \(c\).

The nontrivial concentration boundary occurs when the *total* Dirichlet mass is kept fixed: for every fixed \(\lambda>0\), as \(n\to\infty\),
\[
\boxed{
\|P_{n,\lambda/n}\|_{\infty\to\infty}
=1+2\lambda-\frac{2\lambda^2}{n}
\left[\log n+1+\log\frac{1+\lambda}{\lambda}-\psi(\lambda)-\gamma\right]
+o_\lambda(n^{-1}).}
\]
Here \(\psi\) is the digamma function and \(\gamma\) is Euler's constant. Thus the finite fixed-total-mass limiting norm \(1+2\lambda\) has a universal \((\log n)/n\) deficit and an explicit parameter-dependent next coefficient. By contrast, for every fixed \(\alpha>0\),
\[
\boxed{\lim_{n\to\infty}\frac1n\|P_{n,\alpha}\|_{\infty\to\infty}
=\frac{2\alpha^\alpha e^{-\alpha}}{\Gamma(\alpha)}.}
\]
For fixed \(n\), \(\lim_{\alpha\downarrow0}\|P_{n,\alpha}\|=1\), whereas \(\lim_{\alpha\to\infty}\|P_{n,\alpha}\|/\sqrt\alpha=\sqrt{2n(n-1)/\pi}\).

## Assumptions and scope
The measure is the normalized Dirichlet law with density proportional to \(\prod_i x_i^{\alpha-1}\) on the interior of the simplex. The affine projection is the unconstrained orthogonal projector, not projection onto nonnegative affine functions. The operator norm is the essential-supremum norm for \(\mu_{n,\alpha}\); the output affine function has a continuous version on the closed simplex, making vertices legitimate extremal evaluations. The endpoint \(L^1\)-norm is measured using the same Dirichlet measure. All parameters and limit orderings are explicit in the statements.

## Proof
**1. Exact kernel.** Write \(Y\sim\mu_{n,\alpha}\) and \(T=n\alpha\). The Dirichlet moments are
\[
\mathbb EY_i=1/n,\qquad
\operatorname{Cov}(Y_i,Y_j)=\frac{\delta_{ij}-1/n}{n(T+1)}.
\]
The affine functions are spanned by the constant and the centered coordinates \(Y_i-1/n\), whose covariance operator on the sum-zero hyperplane is \(1/[n(T+1)]\) times the identity. Therefore the reproducing kernel is
\[
K_{n,\alpha}(x,y)
=1+n(T+1)\sum_i(x_i-1/n)(y_i-1/n)
=-n\alpha+n(T+1)\sum_i x_i y_i.
\]
In particular, \(\int K(x,y)\,d\mu(y)=1\). Integrating the reproducing kernel in \(y\) gives the orthogonal projector, while direct substitution of the moments verifies that it fixes every affine function.

**2. Sharp endpoint and positivity defect.** For a fixed \(y\), the map \(x\mapsto(-K(x,y))_+\) is convex. Since \(x=\sum_i x_i e_i\), Jensen's inequality gives
\[
\int(-K(x,y))_+d\mu(y)\le\sum_i x_i\int(-K(e_i,y))_+d\mu(y).
\]
Symmetry makes every vertex integral identical. Moreover, unless \(x\) is a vertex, at least two of the coefficients are positive; the Dirichlet density is positive in the interior and there is a positive-measure set of \(y\) for which their individual vertex kernels straddle zero. On such a set the convexity inequality is strict. Thus *only* vertices maximize negative kernel mass. Since the integral of \(K\) equals one, the absolute kernel mass equals one plus twice its negative mass. Hence the stated \(L^\infty\)-norm is attained by the sign of the kernel at a vertex and the extremal negative output among \(0\le f\le1\) is obtained by the indicator of the negative kernel region. The kernel is symmetric, so its \(L^1\)-norm agrees by duality.

At \(x=e_1\), \(K(e_1,Y)=n((T+1)Y_1-\alpha)\). The marginal law \(Y_1\) is \(\operatorname{Beta}(\alpha,b)\), so
\[
C_{n,\alpha}=n\int_0^{c}(\alpha-(T+1)t)
\frac{t^{\alpha-1}(1-t)^{b-1}}{B(\alpha,b)}\,dt.
\]
The recurrence
\[
I_c(\alpha+1,b)=I_c(\alpha,b)-\frac{c^\alpha(1-c)^b}{\alpha B(\alpha,b)}
\]
then yields the displayed closed formula. For \(\alpha=1\), it reduces to
\(C_{n,1}=n(n/(n+1))^{n-1}-1\), a previously established unweighted case rather than a new claim.

**3. Fixed-total-mass boundary, including the second term.** Fix \(\lambda>0\), and put \(a=\lambda/n\), \(b=\lambda-a\), \(c=\lambda/[n(1+\lambda)]\). Write \(Y\sim\operatorname{Beta}(a,b)\). The exact identity
\[
\lambda-C_{n,a}=\lambda\Pr(Y>c)+n(1+\lambda)\mathbb E[Y\mathbf1_{Y\le c}]
\]
follows by splitting the negative-part integral at \(c\). As \(a\to0\), the reciprocal beta normalizer satisfies
\[
B(a,\lambda-a)^{-1}=a+O_\lambda(a^2).
\]
Consequently, using \(c\asymp_\lambda n^{-1}\), expansion of the beta density on \([c,1]\) gives
\[
\begin{aligned}
\Pr(Y>c)
&=\frac{\lambda}{n}\left[\log(1/c)
+\int_0^1\frac{(1-t)^{\lambda-1}-1}{t}\,dt\right]
+o_\lambda(n^{-1})\\
&=\frac{\lambda}{n}
\left[\log n+\log\frac{1+\lambda}{\lambda}
-\psi(\lambda)-\gamma\right]+o_\lambda(n^{-1}).
\end{aligned}
\]
For completeness, the replacement of \(t^{a-1}\) by \(t^{-1}\) contributes \(O_\lambda(a^2\log^2n)=o(n^{-1})\) after beta normalization; replacing \((1-t)^{b-1}\) by \((1-t)^{\lambda-1}\) gives \(o(n^{-1})\) by integrable logarithmic domination near one. The integral identity in the second line is the standard digamma integral, valid for all \(\lambda>0\). On the shrinking interval \([0,c]\), the same normalized beta density gives
\[
\mathbb E[Y\mathbf1_{Y\le c}]=ac+o_\lambda(n^{-2})
=\frac{\lambda^2}{n^2(1+\lambda)}+o_\lambda(n^{-2}).
\]
Inserting both expansions into the exact identity gives
\[
\lambda-C_{n,\lambda/n}
=\frac{\lambda^2}{n}\left[\log n+1+
\log\frac{1+\lambda}{\lambda}-\psi(\lambda)-\gamma\right]
+o_\lambda(n^{-1}),
\]
and multiplying by two proves the norm expansion.

**4. Other scales.** If \(\alpha>0\) stays fixed while \(n\to\infty\), the gamma representation of a Dirichlet vector implies \((n\alpha+1)Y_1\) converges in distribution to a \(\operatorname{Gamma}(\alpha,1)\) variable \(G\). The second moments are bounded, hence uniform integrability gives
\[
\lim_{n\to\infty}\frac{\|P_{n,\alpha}\|}{n}
=\mathbb E|G-\alpha|
=2\alpha\Pr(G\le\alpha)-2\mathbb E[G\mathbf1_{G\le\alpha}]
=\frac{2\alpha^\alpha e^{-\alpha}}{\Gamma(\alpha)}.
\]
For fixed \(n\), the inequality \(0\le C_{n,\alpha}\le n\alpha\) gives the \(\alpha\downarrow0\) limit. For fixed \(n\), the Dirichlet central limit theorem gives \(K(e_1,Y)/\sqrt\alpha\Rightarrow N(0,n(n-1))\); its second moment is \((n-1)(n\alpha+1)/\alpha\to n(n-1)\), ensuring uniform integrability and yielding the stated Gaussian absolute-mean limit. These statements concern distinct, explicitly ordered regimes.

## Verification
The standalone standard-library script `check.py` verifies the kernel reproducing identity from independently evaluated first and second Dirichlet moments, and evaluates the beta negative-part integral using exact rational polynomial expansion for integer concentrations \(1\le\alpha\le4\) and \(2\le n\le10\). It compares this calculation with the beta-recurrence formula and, separately, with the published unweighted formula. Replaying the package script yields 1,017 exact-rational assertions. Numerical stress tests of the shrinking-parameter formula at \(\lambda=0.2,1,3,10\) and \(n=1000,10000,100000\) matched the predicted vanishing scaled residual. Neither finite computations nor numerics establish the all-parameter or asymptotic claims; the arguments above supply their proofs.

## Relationship to prior work
Griffiths and Spanò (2010) develop Dirichlet multivariate Jacobi projection kernels in the study of canonical correlations, furnishing the natural spectral starting point. Xu (2013) likewise treats Jacobi and Hahn polynomial systems on simplexes. The published *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (2026) proves the uniform-volume case \(\alpha=1\); the present result explicitly does **not** claim this case as new. What is added is the **Dirichlet-weighted parameter family** together with the exact fixed-total-concentration regime, especially its \((\log n)/n\) boundary correction and the distinct fixed-coordinate-concentration linear-growth law. The 2010 source provides kernels and positivity criteria for different correlation operators, not this endpoint norm or the double scaling. The 2026 unweighted formula contains no variable concentration and cannot imply the fixed-total-mass asymptotic by a specialization or limit within its assumptions.

## Limitations
This is the degree-at-most-one orthogonal projector for symmetric strictly positive Dirichlet parameters. It does not classify arbitrary nonsymmetric Dirichlet weight vectors, higher polynomial degrees, or globally coupled finite-element projections. The asymptotic remainders are for each fixed positive parameter and are not asserted uniformly across changing parameter ranges. Orthogonal-polynomial Lebesgue-constant theory is extensive, so an equivalent weighted endpoint computation or fixed-mass correction under alternative Jacobi terminology remains a residual historical-priority risk; the bibliographic comparison is not independent certification.

## References
1. R. C. Griffiths and D. Spanò, *Orthogonal polynomial kernels and canonical correlations for Dirichlet measures*, 2010 preprint, arXiv:1003.5131, https://arxiv.org/abs/1003.5131 (first public 2010-03-26).
2. Y. Xu, *Hahn, Jacobi, and Krawtchouck polynomials of several variables*, 2013 preprint, arXiv:1309.1510, https://arxiv.org/abs/1309.1510.
3. R. Aktaş and Y. Xu, *Sobolev orthogonal polynomials on a simplex*, 2011 preprint, arXiv:1111.2994, https://arxiv.org/abs/1111.2994.
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, public research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34.
