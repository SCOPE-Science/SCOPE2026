# Log-periodic Mellin spectra and measurable weak traces for geometric-circle Bergman Toeplitz operators

## Finding
Let \(b>1\) and \(\alpha>1\). On classical analytic Bergman space with area normalization \(dA/\pi\), let \(\sigma_r\) be normalized angular probability measure on the circle of radius \(r\), and define the positive radial measure
\[
\mu_{\alpha,b}=\sum_{j=1}^{\infty}b^{-\alpha j}\sigma_{\sqrt{1-b^{-j}}}.
\]
Its positive Toeplitz form defines a compact, positive operator \(T_{\alpha,b}\). The eigenvalue corresponding to the normalized monomial \(\sqrt{n+1}z^n\) is exactly
\[
\lambda_n=(n+1)\sum_{j=1}^{\infty}b^{-\alpha j}(1-b^{-j})^n,\qquad n\ge0.
\]
Define the positive analytic one-periodic Mellin profile
\[
G_{\alpha,b}(t)=\sum_{\ell\in\mathbb Z} b^{\alpha(t-\ell)}e^{-b^{t-\ell}}.
\]
Then, **uniformly in the fractional logarithmic phase**, as \(n\to\infty\),
\[
\boxed{n^{\alpha-1}\lambda_n=G_{\alpha,b}(\log_b n)+o(1).}
\]
Its Fourier coefficients are explicit and nonzero at every integer frequency:
\[
\boxed{\widehat G_{\alpha,b}(m)=\frac{\Gamma(\alpha-2\pi i m/\log b)}{\log b},\qquad m\in\mathbb Z.}
\]
Consequently the normalized eigenvalues have precisely the cluster interval \([\min G_{\alpha,b},\max G_{\alpha,b}]\), of strictly positive length for every allowed \(\alpha,b\); there is no unique ordinary power-law coefficient.

Put \(p_c=1/(\alpha-1)\). For each \(p>0\),
\[
\boxed{T_{\alpha,b}\in\mathcal S_p\ \Longleftrightarrow\ p>p_c.}
\]
At the critical exponent, \(T_{\alpha,b}^{p_c}\) is positive, lies in the weak trace ideal \(\mathcal L^{1,\infty}\), is not trace class, and **is Dixmier-measurable despite the nonconstant normalized eigenvalue profile**. Every Dixmier trace has the same value:
\[
\boxed{\operatorname{Tr}_{\omega}(T_{\alpha,b}^{p_c})=
\int_0^1G_{\alpha,b}(t)^{p_c}\,dt.}
\]
In particular, for \(\alpha=2\), the original operator itself lies in weak trace class and
\[
\boxed{\operatorname{Tr}_{\omega}(T_{2,b})=\frac{1}{\log b}}
\]
for every Dixmier trace, even though \(n\lambda_n\) oscillates between different positive accumulation points.

## Assumptions and scope
The Hilbert space \(A^2(\mathbb D)\) consists of holomorphic functions with norm \(\|f\|^2=\pi^{-1}\int_{|z|<1}|f(z)|^2\,dA(z)\). The normalized monomial basis is \(e_n(z)=\sqrt{n+1}\,z^n\) for \(n\ge0\). The measure \(\sigma_r\) assigns total mass one to its circle, and \(\mu_{\alpha,b}\) is a finite positive Borel measure supported on countably many circles approaching the boundary. The Toeplitz form is \(\langle T f,g\rangle=\int f\overline g\,d\mu_{\alpha,b}\), initially on polynomials and then extended by boundedness. No pointwise radial density is assumed. The singular values are arranged in nonincreasing order. The Schatten conventions cover \(0<p<1\) as quasi-norm ideals. A positive operator in weak trace class is called Dixmier-measurable here when all normalized Dixmier traces yield the same value.

## Proof
**1. Diagonalization and bounded extension.** Rotational invariance gives orthogonality of distinct monomials in the measure-induced form. Evaluating diagonal terms yields the exact displayed \(\lambda_n\). Each is positive. The following asymptotic shows \(\lambda_n\to0\), hence \(\sup_n\lambda_n<\infty\), so the quadratic form extends to a bounded, positive, compact diagonal operator. This independently confirms the Bergman–Carleson property of the measure.

**2. Uniform discrete-scale Mellin limit.** For \(n\ge1\), write \(k=\lfloor\log_b n\rfloor\) and \(t=\log_b n-k\in[0,1)\). Substituting \(j=k+\ell\) into the exact diagonal expression gives
\[
n^{\alpha-1}\lambda_n=\left(1+\frac1n\right)
\sum_{\ell\ge1-k} b^{\alpha(t-\ell)}
\left(1-\frac{b^{t-\ell}}n\right)^n.
\]
For each finite set of integers \(\ell\), the last factor converges uniformly in \(t\in[0,1]\) to \(\exp(-b^{t-\ell})\). The positive \(\ell\)-tail is uniformly dominated by the geometric series \(\sum_{\ell\ge L}b^{\alpha(1-\ell)}\). For the negative tail, \((1-u)^n\le e^{-nu}\) with \(u=b^{t-\ell}/n\) bounds each term by \(b^{\alpha(t-\ell)}e^{-b^{t-\ell}}\), uniformly summable as \(\ell\to-\infty\). The omitted terms with \(\ell<1-k\) of the limiting bilateral sum are a vanishing subset of the same negative tail. Thus the difference from the full bilateral sum tends to zero uniformly in \(t\), proving the boxed asymptotic. Uniform convergence of all derivatives of the profile follows from the same superexponential and geometric tail bounds.

**3. Gamma Fourier transform and nonconstancy.** Absolute convergence permits integration over one period and interchange of the bilateral sum. Set \(u=t-\ell\), then \(x=b^u\). For any integer \(m\),
\[
\begin{aligned}
\widehat G(m)&=\int_0^1G(t)e^{-2\pi i m t}\,dt
=\int_{-\infty}^{\infty}b^{\alpha u}e^{-b^u}e^{-2\pi i m u}\,du\\
&=\frac1{\log b}\int_0^\infty x^{\alpha-1-2\pi i m/\log b}e^{-x}\,dx
=\frac{\Gamma(\alpha-2\pi i m/\log b)}{\log b}.
\end{aligned}
\]
The Gamma function has no zeros, hence every nonzero-frequency coefficient is nonzero and \(G\) is nonconstant. It is continuous and positive, so its image is a nondegenerate closed interval. Every phase \(t\in[0,1]\) is approached by \(\{\log_b n\}\), e.g. using \(n=\lfloor b^{k+t}\rfloor\) as \(k\to\infty\), and every subsequential normalized-eigenvalue limit comes from a phase by compactness. This proves the exact cluster interval.

**4. Critical ideal threshold.** Positivity and continuity give constants \(0<c<C<\infty\) such that, for all sufficiently large \(n\), \(c n^{1-\alpha}\le\lambda_n\le Cn^{1-\alpha}\). Since the singular values of a positive compact diagonal operator are its eigenvalues with multiplicity one, in some order, the \(p\)-Schatten membership is equivalent to \(\sum_{n\ge1}n^{-p(\alpha-1)}<\infty\); this holds exactly when \(p>p_c\). Let \(A=T^{p_c}\) and \(a_n=\lambda_n^{p_c}\). Then
\[
a_n=\frac{H(\log_b n)+o(1)}{n},\qquad H(t)=G(t)^{p_c},
\]
with the error uniform in the phase; in particular \(c_0/n\le a_n\le C_0/n\) eventually.

**5. Logarithmic means in canonical and decreasing order.** Smooth periodicity of \(H\) implies that \(x\mapsto H(\log_b x)/x\) has integrable derivative on \([1,\infty)\). Thus the sum–integral difference stays bounded, and periodic averaging gives
\[
\sum_{1\le n\le N}\frac{H(\log_b n)}n
=\int_1^N\frac{H(\log_b x)}x\,dx+O(1)
=(\log N)\int_0^1H(t)\,dt+O(1).
\]
The cumulative \(o(1/n)\) error is \(o(\log N)\). Hence the same limit holds for the first \(N\) entries in canonical order, including \(a_0\), normalized by \(\log N\). To justify rearrangement, extend the two-sided bounds to all indices \(n\ge1\) by adjusting constants. Choose a fixed \(B>\max(2,C_0/c_0)\). Every entry with index greater than \(BN\) is strictly smaller than every entry among the first \(N\), for large \(N\). The \(N\) largest entries therefore come from indices at most \(BN\). Consequently the sum of the \(N\) largest entries lies between the canonical sums through \(N\) and \(BN\), whose difference is bounded by \(\sum_{N<n\le BN}C_0/n=O(1)\). This yields
\[
\lim_{N\to\infty}\frac1{\log(1+N)}\sum_{j=1}^Ns_j(A)=\int_0^1H(t)\,dt.
\]
This ordinary limit makes all Dixmier traces agree; its strictly positive finite value proves \(A\in\mathcal L^{1,\infty}\setminus\mathcal S_1\).

**6. The explicit trace at the original operator threshold.** When \(\alpha=2\), \(p_c=1\) and the Fourier formula at frequency zero yields
\[
\int_0^1G_{2,b}(t)\,dt=\frac{\Gamma(2)}{\log b}=\frac1{\log b}.
\]
This is the common Dixmier trace of \(T_{2,b}\), notwithstanding the proven nontrivial limit interval for \(n\lambda_n\).

## Verification
All infinite-dimensional conclusions follow from the exact diagonal identity, uniform bilateral-tail estimates, the Mellin–Gamma integral, and an explicit rearrangement bound. The accompanying standalone `verify_geometric_circles.py` performs 276 finite checks: profile periodicity, numerical positivity, approach to the scaling profile at three parameter sets, Mellin-profile means at four bases, and finite logarithmic trace averages. It passes using only the Python standard library. Finite checks are supplementary; they do not substitute for the convergence and equality proofs.

For illustration at \(\alpha=2,b=4\), the profile takes approximately \(0.71356\) at phase \(0\), \(0.72924\) at phase \(1/2\), and \(0.74606\) at phase \(\log_4 3\). These differ, while the common Dixmier trace is \(1/\log4\approx0.72135\). The normalization of the circle measures, area, and basis is fixed in the assumptions; changing any of them changes the numerical constants.

## Relationship to prior work
Maximenko and Pacheco (arXiv:2503.23649, Theorem 3.3) establish the diagonal moment formula for general radial Bergman–Carleson measures; their Sections 5–7 analyze individual circle measures, radial averages, and logarithmic continuity. That general diagonalization is the starting point here, not a novelty claim. The present result extracts from a geometrically self-similar singular radial measure the explicit nonconstant Mellin-periodic power-law coefficient, all its nonzero Gamma Fourier modes, and an exact, constant critical Dixmier trace. These conclusions are not stated by that general diagonalization theorem.

Li, Long, and Wang (arXiv:2609.22908) give general Schatten membership criteria for positive Toeplitz operators on smooth convex finite-type domains, encompassing relevant qualitative ideal questions; the elementary Schatten threshold is included here only as context, not as an independent priority claim. A previously published result on smooth radial Gaussian Fock Toeplitz symbols with \(\log\log\)-periodic profiles identifies a *nonmeasurable* critical trace range; the present singular circle-supported **disk Bergman** construction operates at the different multiplicative-log spectral scale and yields a *measurable* critical power, so neither result is a special case of the other. Classical Mellin-transform and Gamma-function identities are used as standard tools. No universal novelty claim for all discrete-scale measures is made.

## Limitations
The theorem concerns one explicit family of positive singular measures on classical analytic Bergman space; it does not classify arbitrary radial or self-similar measures, nonradial perturbations, or weighted Bergman spaces. The Fourier coefficient is indexed by normalized monomial degree, not asserted as a pointwise asymptotic for the rearranged singular-value sequence. The logarithmic average is established for the positive critical power and standard Dixmier traces, not for every possible singular trace functional. The familiar general Schatten threshold is not claimed as novel. Other specialized older literature on Mellin–Poisson summation or singular radial Toeplitz measures might contain an equivalent spectral formulation; independent priority and scientific audits have not been performed.

## References
1. E. A. Maximenko and C. G. Pacheco, *Toeplitz operators in Bergman space induced by radial measures*, arXiv:2503.23649v1 (publicly submitted 2025-03-31), https://arxiv.org/abs/2503.23649. Open-access journal full text: https://link.springer.com/article/10.1007/s40590-025-00830-9, Theorem 3.3 and Sections 5–7.
2. M. Li, J. Long, and L. Wang, *Small exponent Schatten class Toeplitz operators on convex domains of finite type*, arXiv:2609.22908v1 (publicly submitted 2026-09-19), https://arxiv.org/abs/2609.22908.
3. *The logarithmic spectral filter for smooth radial Fock Toeplitz operators*, mathematical research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-logarithmic-spectral-filter-for-smooth-radial-fock-toeplitz--0bc5b54dc8b5; used for statement-level comparison only.
4. Standard Mellin–Gamma integral and Fourier-periodization identity; proofs specialized to the present family are included above.
