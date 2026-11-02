# A Hilbert–Schmidt cusp trichotomy for power-diagonal commutators of generalized Cesàro operators

## Finding
For the generalized discrete Cesàro operators \(C_t\) on \(\ell^2(\mathbb N_0)\), \(0\le t\le1\), and the compact power diagonal \(D_\alpha=\operatorname{diag}((n+1)^{-\alpha})_{n\ge0}\), \(\alpha>0\), the commutator \(K_{\alpha,t}=D_\alpha C_t-C_tD_\alpha\) is Hilbert–Schmidt even at \(t=1\). Its squared Hilbert–Schmidt norm \(F_\alpha(t)\) is strictly increasing in \(t\), and, writing \(\varepsilon=1-t^2\), its endpoint deficit has exactly three distinct regimes:
\[
F_\alpha(1)-F_\alpha(t)\sim
\begin{cases}
\displaystyle I_\alpha\frac{\Gamma(1-2\alpha)}{2\alpha}\varepsilon^{2\alpha}, &0<\alpha<\tfrac12,\\
\displaystyle \tfrac12\varepsilon\log^2(1/\varepsilon),&\alpha=\tfrac12,\\
\displaystyle\zeta(2\alpha)\varepsilon\log(1/\varepsilon),&\alpha>\tfrac12,
\end{cases}
\]
where
\[
I_\alpha=\int_0^\infty \frac{(u^{-\alpha}-(1+u)^{-\alpha})^2}{(1+u)^2}\,du
=B(1-2\alpha,1+2\alpha)-2B(1-\alpha,1+2\alpha)+\frac1{1+2\alpha}
\]
when \(0<\alpha<1/2\). In particular, at the natural diagonal \(D_1=C_0\),
\[
F_1(1)=\zeta(3)-\tfrac34\zeta(4).
\]
All asymptotic equivalents mean ratio tending to one through \(0\le t<1\). The logarithms are natural.

## Assumptions and scope
Use complex \(\ell^2(\mathbb N_0)\), with standard orthonormal basis and indices beginning at zero. Define
\[
(C_t x)_n=\frac1{n+1}\sum_{j=0}^nt^{n-j}x_j,\qquad
(D_\alpha x)_n=(n+1)^{-\alpha}x_n,
\]
where \(0^0=1\) in the diagonal term at \(t=0\). The classical discrete Hardy inequality ensures \(C_1\) is bounded on \(\ell^2\); positivity of the matrix entries and \(C_t\le C_1\) entrywise imply \(\|C_t\|\le\|C_1\|\le2\). The diagonal \(D_\alpha\) is bounded and compact, so the commutator is a bounded operator.

## Proof
### Exact coefficient decomposition
For \(n>j\), the \((n,j)\)-entry of \(K_{\alpha,t}\) equals
\[
\frac{t^{n-j}}{n+1}\big[(n+1)^{-\alpha}-(j+1)^{-\alpha}\big],
\]
and its entries vanish for \(n\le j\). Put \(d=n-j\) and \(m=j+1\). Squaring and summing yields a positive power series
\[
F_\alpha(t)=\sum_{d=1}^\infty a_d(\alpha)t^{2d},\quad
 a_d(\alpha)=\sum_{m=1}^\infty
\frac{[m^{-\alpha}-(m+d)^{-\alpha}]^2}{(m+d)^2}>0.
\]
The following coefficient estimates imply \(\sum_d a_d(\alpha)<\infty\), proving the Hilbert–Schmidt claim at every \(t\in[0,1]\) and strict increase.

### Coefficients below the half-order threshold
For \(0<\alpha<1/2\), introduce
\(g_\alpha(u)=[u^{-\alpha}-(1+u)^{-\alpha}]^2/(1+u)^2\). Exactly
\[
d^{1+2\alpha}a_d(\alpha)=\frac1d\sum_{m\ge1}g_\alpha(m/d).
\]
For \(0<u\le1\), \(g_\alpha(u)\le u^{-2\alpha}\). For \(u\ge1\), the mean-value theorem gives \(g_\alpha(u)\le\alpha^2u^{-2\alpha-4}\). Both envelopes are integrable. On a compact interval away from zero, ordinary Riemann sums converge; the two envelopes control the small-\(u\) and large-\(u\) tails uniformly in \(d\) in the limit. Thus \(d^{1+2\alpha}a_d\to I_\alpha\). The substitution \(y=u/(1+u)\) produces the displayed beta-function expression; each beta parameter is positive on the indicated domain.

### The threshold coefficient
At \(\alpha=1/2\), split the coefficient sum at \(m=d\). For \(m\le d\), expansion of the square gives
\[
a_d=\sum_{m\le d}\frac1{m(m+d)^2}+O(d^{-2})
=\frac{\log d+O(1)}{d^2}.
\]
Indeed, the two omitted square-expansion terms have total absolute value at most \(O(d^{-2})\) by comparison with their Riemann integrals. For \(m>d\), the mean-value theorem bounds the complete summand by \(Cd^2m^{-5}\), so that entire tail is \(O(d^{-2})\). Finally
\(\sum_{m\le d}(m(m+d)^2)^{-1}=d^{-2}\sum_{m\le d}m^{-1}+O(d^{-2})\).

### Coefficients above the threshold
For \(\alpha>1/2\), write
\[
d^2a_d(\alpha)=\sum_{m\ge1}
\frac{[m^{-\alpha}-(m+d)^{-\alpha}]^2}{(1+m/d)^2}.
\]
The summand is bounded by \(m^{-2\alpha}\) and converges pointwise to it. Dominated convergence gives
\(d^2a_d(\alpha)\to\zeta(2\alpha)\).

### Abelian passage to the endpoint
Write \(r=t^2=1-\varepsilon\), and observe
\[
F_\alpha(1)-F_\alpha(t)=\sum_{d\ge1}(1-r^d)a_d(\alpha).
\]
If \(a_d\sim I_\alpha d^{-1-\beta}\) with \(0<\beta=2\alpha<1\), splitting the sum at \(d\asymp\varepsilon^{-1}\), then rescaling \(x=\varepsilon d\), gives the convergent integral
\[
\varepsilon^{-\beta}\sum_{d\ge1}(1-(1-\varepsilon)^d)d^{-1-\beta}
\longrightarrow\int_0^\infty(1-e^{-x})x^{-1-\beta}\,dx
=\frac{\Gamma(1-\beta)}\beta.
\]
The coefficient equivalent transfers to the weighted sum because the contribution from each fixed \(d\) is \(O(\varepsilon)=o(\varepsilon^\beta)\).
At \(\alpha=1/2\), for \(d\le\varepsilon^{-1}\), use
\(1-(1-\varepsilon)^d=\varepsilon d+O(\varepsilon^2d^2)\). Therefore the principal sum is
\[
\varepsilon\sum_{d\le1/\varepsilon}\frac{\log d+O(1)}d
=\frac{\varepsilon}{2}\log^2(1/\varepsilon)
+O(\varepsilon\log(1/\varepsilon)).
\]
The quadratic-error contribution and the tail \(d>\varepsilon^{-1}\) are both \(O(\varepsilon\log(1/\varepsilon))\). When \(\alpha>1/2\), replace the coefficient equivalent by \(\zeta(2\alpha)d^{-2}\), and use
\(\sum_{d\le1/\varepsilon}(\varepsilon d)d^{-2}\sim\varepsilon\log(1/\varepsilon)\); the tail is \(O(\varepsilon)\). The finite initial coefficient terms do not affect the logarithmic leading term. This proves all three asymptotic equivalents.

### Exact classical corner
For \(\alpha=1\), at \(t=1\), expand the squared difference and sum over \(n>m\ge1\):
\[
F_1(1)=\sum_{n>m}\frac{(n-m)^2}{n^4m^2}
=\zeta(2,2)-2\zeta(3,1)+\zeta(3)-\zeta(4).
\]
Euler's standard weight-four double-zeta identities \(\zeta(2,2)=3\zeta(4)/4\) and \(\zeta(3,1)=\zeta(4)/4\) yield \(\zeta(3)-3\zeta(4)/4\). Here \(\zeta(p,q)=\sum_{n>m\ge1}n^{-p}m^{-q}\).

## Verification
The included standalone \(check.py\) computes the commutator-entry square sum two independent ways (direct matrix entries and separation coefficients) using exact rational arithmetic for multiple dimensions and rational \(t\) at \(\alpha=1\). It also calculates numerical finite-cutoff diagnostics for the coefficient regimes and the exact classical corner. Such finite comparisons cannot prove the infinite operator theorem or the asymptotic limits; the proof above supplies those arguments.

## Relationship to prior work
Albanese, Bonet and Ricker introduce the same family \(C_t\) and analyze compactness, spectra and linear dynamics across sequence spaces; their full open-access article does not discuss these power-diagonal commutators or their Hilbert–Schmidt endpoint cusp. Curbera and Ricker study generalized Cesàro operators in Banach lattices, and Gül's essentially-normal result concerns the different self-commutator \(C_1^*C_1-C_1C_1^*\). The present claim is about \([D_\alpha,C_t]\), a parameter-dependent compact perturbation of the diagonal and its precise nonanalytic approach as \(t\uparrow1\). This does not claim novelty for the classical Hardy inequality, the coefficient representation, the Euler double-zeta identities, or generic Abelian theorems.

## Limitations
Only power diagonals \(\alpha>0\), the Hilbert–Schmidt norm, and \(t\in[0,1]\) are treated. The asymptotics do not assert singular-value distribution or exact operator norms. Results for other weighted diagonals, complex \(t\), and general Schatten exponents are not claimed. Equivalent descriptions in broader operator-ideal or Hankel-matrix literature may exist; no independent audit has occurred.

## References
1. A. A. Albanese, J. Bonet, W. J. Ricker, *Spectral properties of generalized Cesàro operators in sequence spaces*, arXiv:2305.04805 (first public 2023-05-08); open-access journal version 2023, DOI 10.1007/s13398-023-01470-2.
2. G. P. Curbera and W. J. Ricker, *Fine spectra and compactness of generalized Cesàro operators in Banach lattices*, arXiv:2302.08750 (2023 preprint).
3. E. Gül, *The Cesàro operator in \(\ell^2\) is essentially normal*, arXiv:2311.15245 (2023).
4. Classical discrete Hardy inequality; Euler's weight-four double-zeta identities (standard established results, not original claims).
