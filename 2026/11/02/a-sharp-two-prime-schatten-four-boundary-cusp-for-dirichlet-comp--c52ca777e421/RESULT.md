# A sharp two-prime Schatten-four boundary cusp for Dirichlet composition operators

## Finding

Let \(d\ge1\), let \(p_1,\ldots,p_d\) be distinct primes, and fix \(a_1,\ldots,a_d>0\) with \(A=\sum_{j=1}^d a_j\). On the Hilbert space \(\mathcal H^2\) of square-summable Dirichlet coefficients, set
\[
\varphi_\delta(s)=\tfrac12+A+\delta+\sum_{j=1}^d a_j p_j^{-s},\qquad \delta\ge0,
\]
and \(G_d(\delta)=\|C_{\varphi_\delta}\|_{\mathcal S_4}^4\), with \(G_d(\delta)=+\infty\) when this operator does not belong to \(\mathcal S_4\). Put
\[
K_d=\frac{1}{(4\pi)^d\prod_{j=1}^d a_j}\sqrt{\frac{2\pi}{A}}.
\]
Then \(C_{\varphi_\delta}\in\mathcal S_4\) for all \(\delta>0\), and at \(\delta=0\) precisely when \(d\ge2\). More precisely, as \(\delta\downarrow0\),
\[
\begin{array}{ll}
d=1:&G_1(\delta)\sim\dfrac{1}{4\sqrt2\,a_1^{3/2}}\,\delta^{-1/2},\\[5pt]
d=2:&G_2(0)-G_2(\delta)\sim4\sqrt\pi K_2\,\sqrt\delta,\\[5pt]
d\ge3:&G_d(0)-G_d(\delta)\sim2\delta\,L_d,
\end{array}
\]
where the last coefficient is finite and positive:
\[
L_d=\sum_{m,n\ge1}(\log m+\log n)(mn)^{-1-2A}
\prod_{j=1}^d I_0(2a_j\sqrt{\log m\log n})^2.
\]
In particular, for two equal amplitudes \(a_1=a_2=1\), the exact square-root cusp coefficient is \(1/(4\pi)\). Here \(I_0\) is the standard modified Bessel function. These are asymptotics of the *fourth power* of the Schatten-four norm, not of the norm itself.

## Assumptions and scope

The Hardy–Hilbert space of Dirichlet series is
\[
\mathcal H^2=\left\{f(s)=\sum_{n\ge1}b_n n^{-s}:\sum_{n\ge1}|b_n|^2<\infty\right\}.
\]
The distinct-prime assumption supplies independent orthogonal coefficients; the prime values do not enter the constants. All amplitudes are fixed and strictly positive. The symbols are analytic and map the open right half-plane to the half-plane \(\operatorname{Re}w>1/2\), including when \(\delta=0\). Their composition operators are bounded by the Gordon–Hedenmalm criterion. The asymptotic parameter is the *real translation* \(\delta\), not the amplitudes or number of primes. There is no uniformity assertion when a positive amplitude tends to zero or when \(d\) varies.

## Proof

**1. Exact coupled Gram trace.** For the orthonormal basis \(e_n(s)=n^{-s}\), the coefficient expansion is
\[
C_{\varphi_\delta}e_n(s)=n^{-1/2-A-\delta}
\prod_{j=1}^d\sum_{k\ge0}\frac{(-a_j\log n)^k}{k!}p_j^{-ks}.
\]
Orthogonality of distinct prime monomials, followed by the defining series of \(I_0\), gives
\[
\langle C_{\varphi_\delta}e_m,C_{\varphi_\delta}e_n\rangle
=(mn)^{-1/2-A-\delta}\prod_{j=1}^d I_0(2a_j\sqrt{\log m\log n}).
\]
The identity \(\operatorname{Tr}((C^*C)^2)=\sum_{m,n\ge1}|\langle Ce_m,Ce_n\rangle|^2\), interpreted as a nonnegative extended sum, therefore gives
\[
G_d(\delta)=\sum_{m,n\ge1}(mn)^{-1-2A-2\delta}
\prod_{j=1}^d I_0(2a_j\sqrt{\log m\log n})^2.\tag{1}
\]
For positive \(\delta\), \(I_0(y)\le e^y\) and \(2\sqrt{tu}\le t+u\) make the summand at most \((mn)^{-1-2\delta}\), so the sum is finite. Equation (1) is used as a starting identity, not claimed as an independent novelty.

**2. Passage to logarithmic Lebesgue measure, with differentiable error.** Write \(t=\log m\), \(u=\log n\), and
\[
g_\delta(t,u)=e^{-(2A+2\delta)(t+u)}
\prod_j I_0(2a_j\sqrt{tu})^2,
\qquad
\mu=\sum_{n\ge1}n^{-1}\delta_{\log n}.
\]
Thus \(G_d(\delta)=\iint g_\delta\,d\mu\,d\mu\). Set \(J_d(\delta)=\iint_{[0,\infty)^2}g_\delta(t,u)\,dt\,du\). The elementary harmonic estimate
\[
\mu([0,t])-t=\sum_{n\le e^t}\frac1n-t=\gamma+O(e^{-t})\qquad(t\ge0)
\]
shows that \(\mu-dt\) is a boundary evaluation plus a distribution whose integration-by-parts primitive decays exponentially. Consequently,
\[
E_d(\delta):=G_d(\delta)-J_d(\delta)
\]
extends to a continuously differentiable function for \(0\le\delta\le\delta_0\), and in particular \(E_d(\delta)=E_d(0)+O(\delta)\). To verify the needed domination rather than assuming a formal sum-to-integral approximation, use the absolutely convergent power series of \(I_0(2a\sqrt{tu})\) to differentiate the smooth kernel, the bounds \(|I_0^{(r)}(y)|\le e^y\) for fixed \(r\), and the estimate
\[
|\partial_t^{r}\partial_u^{s}\partial_\delta^q g_\delta(t,u)|
\le C(1+t+u)^M e^{-2A(\sqrt t-\sqrt u)^2}
\quad(r,s\le1,\ q\le1).
\]
For each derivative used in integration by parts, the extra \(e^{-t}\) (or \(e^{-u}\)) in the primitive makes its integral finite; the terms with one variable at zero are exponentially decreasing in the other. Applying the one-variable summation-by-parts identity successively in the two variables therefore proves the stated \(C^1\) error estimate. This argument also handles the terms with \(m=1\) or \(n=1\). The polynomial power \(M\) depends on \(d\), the amplitudes and derivative orders; its precise value is immaterial to exponential integrability.

**3. Diagonal Gaussian concentration.** Substitute
\[
x=\frac{t+u}{2},\qquad v=\frac{t-u}{\sqrt x},\qquad
 t=x+\frac{v\sqrt x}{2},\quad u=x-\frac{v\sqrt x}{2}.
\]
The Jacobian is \(\sqrt x\), and \(|v|\le2\sqrt x\). Therefore
\[
J_d(\delta)=\int_0^\infty e^{-4\delta x}\,Q_d(x)\,dx,
\quad
Q_d(x)=\sqrt x\!\int_{-2\sqrt x}^{2\sqrt x}
 g_0\!\left(x+\tfrac12v\sqrt x,x-\tfrac12v\sqrt x\right)dv.
\]
For fixed \(v\) and \(x\to\infty\), the standard Bessel asymptotic \(I_0(y)=e^y(2\pi y)^{-1/2}(1+O(y^{-1}))\) yields
\[
g_0(t,u)\sim \frac{(tu)^{-d/2}}{(4\pi)^d\prod_j a_j}
\exp\left[-2A(\sqrt t-\sqrt u)^2\right],
\qquad
2A(\sqrt t-\sqrt u)^2\longrightarrow\frac A2v^2.
\]
When \(|v|=o(\sqrt x)\) the Gaussian provides a uniform integrable majorant. For \(|v|\) comparable to \(\sqrt x\), \(\sqrt t-\sqrt u\) has magnitude comparable to \(\sqrt x\), giving exponential suppression; the possible small argument of one Bessel factor only improves the estimate. Split at \(|v|=x^{1/8}\) and then at a fixed fraction of \(\sqrt x\) to justify dominated convergence. It follows that
\[
Q_d(x)\sim K_d x^{1/2-d},\qquad
K_d=\frac1{(4\pi)^d\prod_j a_j}
\int_{-\infty}^\infty e^{-Av^2/2}\,dv
=\frac1{(4\pi)^d\prod_j a_j}\sqrt{\frac{2\pi}{A}}.\tag{2}
\]
The same domination bounds \(Q_d(x)\le Cx^{1/2-d}\) for all sufficiently large \(x\); near zero, analyticity gives local integrability.

**4. Abelian boundary limits.** For \(d=1\), (2) and scaling \(x\mapsto x/(4\delta)\) imply
\[
J_1(\delta)\sim K_1\Gamma(1/2)(4\delta)^{-1/2}
=\frac{\sqrt\pi}{2}K_1\delta^{-1/2}.
\]
For \(d=2\), the finite boundary value and the identity \(\int_0^\infty(1-e^{-y})y^{-3/2}dy=2\sqrt\pi\) give
\[
J_2(0)-J_2(\delta)
\sim K_2(4\delta)^{1/2}\,2\sqrt\pi
=4\sqrt\pi K_2\sqrt\delta.
\]
The \(O(\delta)\) discretization defect does not affect either leading term. If \(d\ge3\), then \(\int_0^\infty xQ_d(x)dx<\infty\) by (2). Monotone convergence in the exact nonnegative double series (1), using the matching tail bound or comparison with the continuous integral, yields
\[
G_d(0)-G_d(\delta)
\sim2\delta\!\sum_{m,n\ge1}
(\log m+\log n)(mn)^{-1-2A}
\prod_j I_0(2a_j\sqrt{\log m\log n})^2.
\]
The coefficient is positive because terms with \(m,n>1\) are positive, and finite by (2) and the differentiable-error estimate. For \(d=1\), the first asymptotic diverges; for \(d\ge2\), the integrable profile and finite correction prove the endpoint membership criterion. Substituting \(a_1=a_2=1\) into the displayed formula for \(K_2\) yields \(4\sqrt\pi K_2=1/(4\pi)\), as claimed.

## Verification

The accompanying `check_schatten4.py` and `requirements.txt` provide supplementary reproducible calculations. Run `python check_schatten4.py` after installing the stated SciPy dependency. The checker tests two independent expansions of the Gram kernel for one-, two- and three-prime cases, independent numerical quadrature of the diagonal profile at increasing large scales, and the elementary equal-amplitude cusp constant. Its finite assertions do not certify the limiting theorem, and the proof above is the basis for that theorem.

## Relationship to prior work

Bayart and Kouroupis, arXiv:2306.05733 (first public 2023-06-09), establish general Schatten membership criteria and an even-Schatten trace framework for Dirichlet-series composition operators. The exact Gram trace (1), and qualitative membership alone, are not proposed as new. Bayart and Brevig, arXiv:1505.02944, give compactness and approximation-number results for finite-prime symbols. The present claim is the *sharp boundary-translation asymptotic*, especially the exact two-prime \(\sqrt\delta\) coefficient and its explicit amplitude dependence. The Hilbert–Schmidt norm is governed by a one-index Bessel sum, rather than the coupled two-index trace here, and has different critical dimensions. Broader classical Laplace/Abelian methods supply tools but not, by themselves, the stated operator-specific normalization and coefficient. A generally applicable earlier theorem may subsume this calculation, so independent historical-priority review remains worthwhile.

## Limitations

These results concern fixed finite independent prime supports, positive fixed amplitudes, the Schatten-four norm and real boundary translation. They give no stability estimate for noisy data, no uniformity as amplitudes vanish, and no statement for arbitrary Dirichlet-series symbols or Schatten exponents. The remainder estimate in the sum-to-integral step depends on the fixed parameters. Supplementary finite numerical tests cannot replace the analytic Gaussian concentration and Abelian steps. Independent review and historical-priority confirmation have not been performed.

## References

- F. Bayart and A. Kouroupis, *Schatten class composition operators on the Hardy space of Dirichlet series and a comparison-type principle*, arXiv:2306.05733 (first posted 2023-06-09), https://arxiv.org/abs/2306.05733; sections 1 and 3.
- F. Bayart and O. F. Brevig, *Compact composition operators with non-linear symbols on the Hardy space of Dirichlet series*, arXiv:1505.02944 (first posted 2015-05-12), https://arxiv.org/abs/1505.02944; finite-prime-symbol approximation-number results.
- Y. Fang, Q. Guo, H. Mishra and J. Muthukumar, *Critical norm profiles for finite-prime composition operators*, arXiv:2608.26041, https://arxiv.org/abs/2608.26041; comparison with operator-norm boundary scaling, not a Schatten-four trace calculation.
