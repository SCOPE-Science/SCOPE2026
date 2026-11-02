# Sharp Gaussian quadratic transport and skewness cancellation for a stationary binary Markov chain

## Finding

Let \(X_1,X_2,\ldots\in\{0,1\}\) be the stationary irreducible two-state Markov chain described below, and let \(S_n=\sum_{j=1}^nX_j\). For every fixed admissible \(p\in(0,1)\) and nonzero correlation \(\rho\), its variance-normalized occupation sum \(Y_n=(S_n-np)/\sqrt{\operatorname{Var}(S_n)}\) has the exact sharp Gaussian transport limit

\[
\lim_{n\to\infty}n\,W_2^2\bigl(\mathcal L(Y_n),\mathcal N(0,1)\bigr)
=\frac{1-\rho}{12p(1-p)(1+\rho)}
+\frac{(1-2p)^2(1+4\rho+\rho^2)^2}
{18p(1-p)(1-\rho)(1+\rho)^3}.
\]

The first summand is a strictly positive lattice-quantization floor; the second is the squared third-cumulant correction. The latter vanishes for asymmetric stationary marginals \(p\ne1/2\) at the admissible anticorrelation \(\rho_0=-2+\sqrt3\), provided \((3-\sqrt3)/6<p<(3+\sqrt3)/6\). At this point a dependent, nonsymmetric binary chain has no first-order skewness contribution to quadratic normal transport. The formula applies to a fixed chain, not uniformly as parameters approach reducibility or periodicity.

## Assumptions and scope

Put \(q=1-p\). Let \(p\in(0,1)\) and
\[
-\frac{\min(p,q)}{\max(p,q)}<\rho<1,\qquad \rho\ne0.
\]
The chain starts in its stationary law \(\Pr(X_1=1)=p\), with transition matrix, in state order \(0,1\),
\[
P=\begin{pmatrix}
1-p(1-\rho)&p(1-\rho)\\
q(1-\rho)&1-q(1-\rho)
\end{pmatrix}.
\]
All entries are strictly positive. For probability distributions with finite second moments, \(W_2^2(\mu,\nu)=\inf_{\pi\in\Pi(\mu,\nu)}\int|u-v|^2\,d\pi(u,v)\). Define
\[
\sigma_\infty^2=pq\frac{1+\rho}{1-\rho},\qquad
\kappa_{3,\infty}=pq(q-p)\frac{1+4\rho+\rho^2}{(1-\rho)^2}.
\]
The asserted coefficient is equivalently
\[
C(p,\rho)=\frac1{12\sigma_\infty^2}
+\frac{\kappa_{3,\infty}^2}{18\sigma_\infty^6}.
\]
The independent case \(\rho=0\) is a previously tractable lattice benchmark and is excluded from the claimed dependent-chain contribution, although its limit is recovered by continuity.

## Proof

**1. Stationary two- and three-point correlations.** Let \(Z_j=X_j-p\), so \(\mathbb EZ_j=0\). The conditional expectation identity \(\mathbb E[Z_{j+h}\mid X_j]=\rho^hZ_j\) yields, for \(i\le j\le k\),
\[
\mathbb E[Z_iZ_j]=pq\rho^{j-i},\qquad
\mathbb E[Z_iZ_jZ_k]=pq(q-p)\rho^{k-i}.
\]
For the triple identity, use \(Z_j^2=pq+(q-p)Z_j\) and condition successively at the intermediate and final times; repeated indices satisfy the same formula. Therefore
\[
 v_n:=\operatorname{Var}(S_n)=pq\left(n+2\sum_{h=1}^{n-1}(n-h)\rho^h\right)
 =n\sigma_\infty^2+O_{p,\rho}(1)
\]
and, because the centered third moment is the third cumulant,
\[
\begin{split}
\mathbb E(S_n-np)^3=pq(q-p)\biggl[n
&+6\sum_{h=1}^{n-1}(n-h)\rho^h\\
&+6\sum_{h=2}^{n-1}(n-h)(h-1)\rho^h\biggr]
=n\kappa_{3,\infty}+O_{p,\rho}(1).
\end{split}
\]
Here \(|\rho|<1\), making all sums convergent after division by \(n\). Summing the two geometric series gives exactly the displayed \(\kappa_{3,\infty}\).

**2. Continuity-corrected lattice expansion.** We state the specific finite-state spectral consequence needed for the transport calculation, together with its derivation. Let \(h_n=v_n^{-1/2}\), \(x_{n,k}=(k-np)h_n\), and \(\gamma=\kappa_{3,\infty}/\sigma_\infty^3\). For every central integer \(k\) with \(|x_{n,k}|\le R_n:=\sqrt{20\log n}\),
\[
\Phi^{-1}\!\left(\Pr(S_n\le k)\right)
=x_{n,k}+\frac{h_n}{2}
+\frac{\gamma}{6\sqrt n}(1-x_{n,k}^2)
+O_{p,\rho}\!\left(\frac{(1+\log n)^B}{n}\right), \tag{1}
\]
where \(B\) is some fixed finite integer and the remainder is uniform in \(k\).

For completeness, consider the moment generating function
\[
 \mathbb Ee^{zS_n}=\pi D(z)[PD(z)]^{n-1}{\bf1},\quad
 \pi=(q,p),\quad D(z)=\operatorname{diag}(1,e^z).
\]
The leading eigenvalue \(\lambda(z)\) of \(PD(z)\) is simple and analytic near zero, and the second eigenvalue is \(\rho\) at zero. The characteristic matrix has spectral radius strictly below one at every \(z=i\theta\), \(0<|\theta|\le\pi\): strict positivity of \(P\) makes equality in the entrywise Perron bound impossible unless the two phase factors coincide. On a neighborhood of zero, the spectral representation is \(A(z)\lambda(z)^n+O(c^n)\), \(0<c<1\), with \(A(0)=1\). Stationarity and \(\mathbb ES_n=np\) give \(A'(0)=0\). Thus the only term of normalized order \(n^{-1/2}\) in the characteristic expansion is the cubic cumulant \(\gamma(it)^3/(6\sqrt n)\), while the mean and variance are already normalized exactly.

Expand the analytic eigenvalue and prefactor to arbitrarily high fixed order on \(|\theta|\le n^{-2/5}\), bound the complementary Fourier arc using the strict spectral gap and Gaussian decay on the intermediate arc, and invert Fourier coefficients. This gives local lattice Edgeworth expansions to any prescribed polynomial order, with the first density correction \(\gamma H_3(x)\phi(x)/(6\sqrt n)\), where \(H_3(x)=x^3-3x\). Summing the local expansion by Euler--Maclaurin up to the integer cutoff \(k\) supplies the half-cell correction \(h_n\phi(x)/2\); since \(\int_{-\infty}^xH_3(t)\phi(t)\,dt=(1-x^2)\phi(x)\), the first-order CDF correction is as asserted. This is the usual continuity-corrected lattice expansion, with the finite-state spectral calculation verifying its applicability here; compare Kolassa--McCullagh [2]. Taking sufficiently high order (for example, a uniform remainder \(o(n^{-20})\)) ensures that, on \(|x|\le R_n\), dividing the residual CDF error by \(\phi(x)\ge c n^{-10}\) still leaves \(o(n^{-1})\). All remaining Edgeworth coefficients are Gaussian densities times fixed polynomials, so their contribution to the inverse CDF is \(O(n^{-1}(1+\log n)^B)\). Taylor inversion of \(\Phi\) yields (1).

**3. Quadratic quantile cells.** Let \(G\) be standard normal and couple it monotonically to \(Y_n\). If \(t_{n,k}=\Phi^{-1}(\Pr(S_n\le k))\), with \(t_{n,-1}=-\infty\) and \(t_{n,n}=+\infty\), this coupling sends the interval \((t_{n,k-1},t_{n,k}]\) to \(x_{n,k}\). Thus
\[
W_2^2(\mathcal L(Y_n),\mathcal N(0,1))
=\sum_{k=0}^n\int_{t_{n,k-1}}^{t_{n,k}}
(z-x_{n,k})^2\phi(z)\,dz.\tag{2}
\]
Writing \(s_{n,k}=\gamma(1-x_{n,k}^2)/(6\sqrt n)\), equation (1) makes the endpoints of a central cell equal to
\[
x_{n,k}-h_n/2+s_{n,k}+O(n^{-1}(1+\log n)^B),\quad
x_{n,k}+h_n/2+s_{n,k}+O(n^{-1}(1+\log n)^B).
\]
The variation of \(s_{n,k}\) between successive centers is absorbed by the same remainder. Integrating the squared displacement over this shifted interval gives
\[
\int_{t_{n,k-1}}^{t_{n,k}}(z-x_{n,k})^2\phi(z)\,dz
=h_n\phi(x_{n,k})\left(\frac{h_n^2}{12}+s_{n,k}^2\right)
+o(n^{-1}h_n), \tag{3}
\]
with summable errors over the central cells. In particular, the cross-term vanishes by symmetry of the leading cell around its shifted center; the shift and width errors add in quadrature, not linearly.

**4. Tails and the limiting integral.** The spectral moment-generating-function bound and Chernoff's inequality, with \(R_n=\sqrt{20\log n}\), give
\[
\Pr(|Y_n|>R_n)\le 2\exp\{-R_n^2/2+O_{p,\rho}(R_n^3/\sqrt n)\}=n^{-10+o(1)}.
\]
The fourth moments of \(Y_n\) are uniformly bounded by the same analytic moment generating function. Applying Cauchy--Schwarz to the integrand in (2) shows that the omitted cells contribute \(o(n^{-1})\). Consequently, summing (3), multiplying by \(n\), and applying a Gaussian Riemann-sum limit yields
\[
\begin{split}
\lim_{n\to\infty}nW_2^2
&=\int_{\mathbb R}\phi(x)\left[\frac1{12\sigma_\infty^2}
+\frac{\gamma^2}{36}(1-x^2)^2\right]dx\\
&=\frac1{12\sigma_\infty^2}+\frac{\gamma^2}{18},
\end{split}
\]
using \(\mathbb E(1-G^2)^2=2\). Substitution gives the stated rational expression. The nonzero lattice term also proves that the \(n^{-1/2}\) scale of \(W_2\) cannot be improved for these chains.

**5. An asymmetric zero-skew correlation.** For \(p\ne1/2\), the third-cumulant term vanishes precisely when \(1+4\rho+\rho^2=0\). Its sole root in \((-1,1)\) is \(\rho_0=-2+\sqrt3\). The strict transition-positivity condition at this root is equivalent to \((3-\sqrt3)/6<p<(3+\sqrt3)/6\), proving the admissible cancellation statement.

## Verification

The included `check_two_state_markov_w2.py` computes the full finite-state count distribution by dynamic programming, evaluates the exact one-dimensional monotone coupling integral using normal quantile boundaries, and tests finite-size convergence at five parameter choices. It also checks the finite-size variance and third-cumulant identities in exact rational arithmetic for the first ten lengths, together with the exceptional root. The saved output records 97 passed deterministic checks. The numerical tests cannot prove an infinite limit; the proof is the analytic calculation above.

## Relationship to prior work

Hafouta and Leppänen [1], first public on 2026-10-21, establish optimal-order \(W_2=O(n^{-1/2})\) CLT bounds for weakly dependent systems under mixing conditions, but do not give this exact occupation-count coefficient or the negative-correlation skewness-cancellation locus. Bobkov [3] develops Gaussian transport Edgeworth constants under a nonlattice smoothing condition, which is inapplicable to binary occupations; its general rate inequality is consistent with this result. Kolassa and McCullagh [2] establish arbitrary-order continuity-corrected lattice Edgeworth expansions for independent variables; the lattice correction is essential here, but their independence hypothesis excludes nonzero \(\rho\). The independent-binomial specialization is not claimed as new. The distinguishing feature here is the simultaneous dependence-sensitive long-run cumulant, lattice transport correction and explicit nontrivial cancellation locus.

## Limitations

The assertions hold for fixed, strictly positive two-state transition kernels with nonzero correlation. No uniform rate is asserted near an absorbing or period-two boundary, no higher-dimensional transport result is proved, and no full second-order correction after the stated leading coefficient is derived. Priority remains subject to independent examination of older lattice Markov transport and spectral Edgeworth literature.

## References

[1] Y. Hafouta and J. Leppänen, *Optimal CLT error bounds in the second order Wasserstein metric via Stein's method for weakly dependent sequences*, arXiv:2610.30352v1, 2026-10-21, https://arxiv.org/html/2610.30352v1.

[2] J. E. Kolassa and P. McCullagh, *Edgeworth Series for Lattice Distributions*, Annals of Statistics 18 (1990), 981--985, https://galton.uchicago.edu/~pmcc/pubs/paper16.pdf, doi:10.1214/aos/1176347637.

[3] S. G. Bobkov, *Berry--Esseen bounds and Edgeworth expansions in the central limit theorem for transport distances*, Probability Theory and Related Fields (2018), https://www-users.cse.umn.edu/~bobko001/papers/2017_PTRF_CLT.for.W.p_online.version.pdf, doi:10.1007/s00440-017-0756-2.

[4] Y. Zhang and Q. Xie, *Gaussian Approximation for Multivariate Martingale Sums from Uniformly Ergodic Markov Chains*, arXiv:2609.09480, 2026-09-08, https://arxiv.org/abs/2609.09480 (related bound; abstract inspected).
