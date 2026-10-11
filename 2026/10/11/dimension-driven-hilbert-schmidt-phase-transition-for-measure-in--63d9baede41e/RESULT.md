# Dimension-driven Hilbert–Schmidt phase transition for measure-induced Cesàro operators on Bergman balls

## Finding

Fix an integer \(n\ge 2\), \(\alpha>-1\), \(\beta>0\), a unit vector \(\xi\in\mathbb C^n\), and a finite positive Borel measure \(\mu\) on \([0,1)\). Write \(\mathbb B_n=\{z\in\mathbb C^n:\|z\|<1\}\), and equip the analytic weighted Bergman space \(A_\alpha^2(\mathbb B_n)\) with normalized measure proportional to \((1-\|z\|^2)^\alpha\,dV(z)\). Define the measure-induced Cesàro operator initially on polynomials by
\[
(C_{\mu,\beta}^{\xi}f)(z)=\int_{[0,1)}\frac{f(tz)}{(1-t\langle z,\xi\rangle)^\beta}\,d\mu(t).
\]
Put \(\nu=n+\alpha+1\), \(\mu_m=\int_{[0,1)}t^m\,d\mu(t)\), and \(b_j=(\beta)_j/j!\), with the rising factorial \((a)_j\). For every integer \(m\ge0\), set
\[
S_m=\sum_{j=0}^{m} b_j^2\,
\frac{\Gamma(m+n)\Gamma(m-j+\nu)\Gamma(j+1)}{\Gamma(m+\nu)\Gamma(m-j+1)\Gamma(j+n)}.
\]
Then the operator has a Hilbert–Schmidt extension if and only if \(\sum_{m=0}^\infty \mu_m^2 S_m<\infty\); in that case its **exact squared Hilbert–Schmidt norm** is
\[
\|C_{\mu,\beta}^{\xi}\|_{S_2}^2=\sum_{m=0}^\infty \mu_m^2 S_m.
\]
The positive weights satisfy the exact asymptotic trichotomy
\[
S_m\sim
\begin{cases}
A_{n,\beta}\,m^{n-1},&0<\beta<n/2,\\
\Gamma(n/2)^{-2}m^{n-1}\log m,&\beta=n/2,\\
\Gamma(\beta)^{-2}\mathrm B(2\beta-n,n+\alpha+1)\,m^{2\beta-1},&\beta>n/2,
\end{cases}
\]
where \(A_{n,\beta}=\sum_{j=0}^\infty (\beta)_j^2\Gamma(j+1)/((j!)^2\Gamma(j+n))\in(0,\infty)\) in the first regime and \(\mathrm B\) denotes Euler's beta function. Accordingly, the Hilbert–Schmidt condition is **exactly**
\[
\begin{cases}
\displaystyle\sum_{m=0}^\infty (m+1)^{n-1}\mu_m^2<\infty,&\beta<n/2,\\
\displaystyle\sum_{m=0}^\infty (m+1)^{n-1}\log(m+2)\mu_m^2<\infty,&\beta=n/2,\\
\displaystyle\sum_{m=0}^\infty (m+1)^{2\beta-1}\mu_m^2<\infty,&\beta>n/2.
\end{cases}
\]
The membership criterion, unlike the leading constant above the transition, is independent of the Bergman parameter \(\alpha\).

For the natural power-logarithmic family
\[
d\mu_{s,r}(t)=(1-t)^{s-1}\big[\log(e/(1-t))\big]^{-r}\,dt,
\qquad s>0,\quad r\in\mathbb R,
\]
put \(s_*=\max\{n/2,\beta\}\). Its induced operator is Hilbert–Schmidt for \(s>s_*\), not Hilbert–Schmidt for \(s<s_*\), and, on the exact boundary \(s=s_*\), is Hilbert–Schmidt precisely for \(r>1/2\) if \(\beta\ne n/2\), or precisely for \(r>1\) if \(\beta=n/2\). This exhibits a double-critical logarithmic penalty.

## Assumptions and scope

The complex dimension is an integer \(n\ge2\). The weight exponent \(\alpha\) is any real number greater than \(-1\). The kernel exponent \(\beta\) is real and positive. The measure \(\mu\) is finite, positive, and Borel on \([0,1)\); in particular all moments exist and are nonnegative. The operator is defined by the displayed integral on polynomials and is considered on the Hilbert space \(A_\alpha^2(\mathbb B_n)\). The Hilbert–Schmidt assertion means that this polynomial operator extends as an \(S_2\) operator; it makes no assertion that a general non-Hilbert–Schmidt operator is unbounded. Rotating \(\xi\) to the first coordinate is unitary and preserves the norm.

## Proof

**1. Exact monomial expansion and norm identity.** Let \(u=(u_1,\ldots,u_n)\in\mathbb N_0^n\), \(|u|=\sum_i u_i\), \(u!=\prod_i u_i!\), and \(e_1=(1,0,\ldots,0)\). The normalized monomials
\[
E_u(z)=\sqrt{\frac{(\nu)_{|u|}}{u!}}\,z^u
\]
form an orthonormal basis. After rotating \(\xi\) to \(e_1\), the binomial series and moment integration give, for \(k=|u|\),
\[
C_{\mu,\beta}^{e_1}E_u=
\sum_{j=0}^\infty \mu_{k+j}b_j
\sqrt{\frac{(\nu)_k}{(\nu)_{k+j}}\frac{(u_1+j)!}{u_1!}}\,E_{u+je_1}.
\]
The series is locally normally convergent because \(\mu\) is finite; orthogonality gives the squared norm as a nonnegative sum. For fixed \(k,j\), a direct generating-function calculation yields
\[
\sum_{|u|=k}\frac{(u_1+j)!}{u_1!}
=j!\,[x^k](1-x)^{-n-j}
=\frac{\Gamma(j+1)\Gamma(k+j+n)}{\Gamma(j+n)\Gamma(k+1)}.
\]
Indeed \(\sum_{q\ge0}(q+1)_j x^q=j!(1-x)^{-j-1}\), and summing over the other \(n-1\) coordinates contributes \((1-x)^{-(n-1)}\). Substitute \(m=k+j\), use \((\nu)_k/(\nu)_m=\Gamma(k+\nu)/\Gamma(m+\nu)\), and apply Tonelli's theorem to obtain
\[
\sum_{u}\|C_{\mu,\beta}^{e_1}E_u\|^2
=\sum_{m=0}^\infty \mu_m^2S_m.
\]
When finite, this sum constructs the Hilbert–Schmidt extension uniquely by density of polynomials; conversely every Hilbert–Schmidt extension has this basis norm sum.

**2. Three asymptotic regimes.** Factor \(S_m\) as
\[
S_m=\frac{\Gamma(m+n)}{\Gamma(m+\nu)}
\sum_{j=0}^{m}d_jg_{m-j},\quad
 d_j=\frac{(\beta)_j^2}{(j!)^2}\frac{\Gamma(j+1)}{\Gamma(j+n)},\quad
 g_k=\frac{\Gamma(k+\nu)}{\Gamma(k+1)}.
\]
By the gamma-ratio asymptotic,
\[
d_j\sim \Gamma(\beta)^{-2}j^{2\beta-n-1},\qquad
g_k\sim k^{n+\alpha},\qquad
\frac{\Gamma(m+n)}{\Gamma(m+\nu)}\sim m^{-\alpha-1}.
\]
If \(2\beta<n\), the series \(\sum d_j\) converges; because \(g_k\) increases with \(k\) (here \(\nu>1\)), \(g_{m-j}/g_m\le1\). Dominated convergence gives \(\sum_{j\le m}d_jg_{m-j}\sim g_m\sum_jd_j\). This yields the first branch.

If \(2\beta=n\), then \(d_j\sim\Gamma(n/2)^{-2}/j\). Separate \(j\le\varepsilon m\) from the remaining range. On the former, \(g_{m-j}/g_m\) converges uniformly to \((1-j/m)^{n+\alpha}\) away from the boundary; summing the harmonic singularity gives the full leading \(\Gamma(n/2)^{-2}\log m\). The range \(j>\varepsilon m\) contributes only \(O_\varepsilon(g_m)\), and then \(\varepsilon\downarrow0\) confirms the stated coefficient. This proves the middle branch.

If \(2\beta>n\), a Riemann-sum limit gives
\[
\sum_{j=0}^{m}d_jg_{m-j}\sim
\Gamma(\beta)^{-2}m^{2\beta+\alpha}
\int_0^1 x^{2\beta-n-1}(1-x)^{n+\alpha}\,dx.
\]
Both exponents at the endpoints exceed \(-1\), so the endpoint portions are uniformly negligible after the indicated rescaling. Multiplication by \(m^{-\alpha-1}\) yields the third branch. These positive asymptotics prove the three moment-summability equivalences, including their endpoints.

**3. Critical logarithmic densities.** Let \(s>0\) and \(r\in\mathbb R\). Substituting \(y=m(1-t)\) into the defining moment integral and using dominated convergence after truncating the exponentially small tails yields
\[
\mu_m=\int_0^1t^m(1-t)^{s-1}
[\log(e/(1-t))]^{-r}\,dt
\sim\Gamma(s)m^{-s}(\log m)^{-r}.
\]
Thus the relevant series has terms comparable to \(m^{2s_*-1-2s}(\log m)^{-2r}\) when \(\beta\ne n/2\), and to \(m^{n-1-2s}(\log m)^{1-2r}\) when \(\beta=n/2\). The integral test gives the asserted strict regimes and the boundary conditions \(r>1/2\) and \(r>1\), respectively.

## Verification

The accompanying standalone `verify_hs_identity.py` uses Python standard-library exact rational arithmetic. It independently sums normalized monomial coefficient squares over all multiindices and compares them against the closed gamma-factor expression for dimensions \(2\), \(3\), and \(4\), several integer weight/kernel parameters, and total degrees \(0\) through \(7\). It also checks a closed harmonic-number formula in the critical model \(n=2\), \(\alpha=0\), \(\beta=1\), for degrees up to \(21\):
\[
S_m=(m+3)H_{m+1}-\frac{(m+1)(2m+5)}{m+2}+\frac{m+1}{2},
\qquad H_k=\sum_{j=1}^{k}1/j.
\]
For instance, \(S_0=1\) and \(S_1=7/3\). The program prints `BALL_CESARO_HS_IDENTITY_EXACT_OK` on success. Finite exact checks corroborate the coefficient identity; the full infinite-dimensional result follows from the proof above, not enumeration.

## Relationship to prior work

Pan, Tong, and Yang (arXiv:2609.03243v1, publicly posted 2026-09-03) introduce this exact unit-ball measure-induced family and characterize boundedness between weighted Bergman spaces and into bounded holomorphic functions. Their Theorems 1.1–1.3 and proofs do not provide a Hilbert–Schmidt criterion or the three-dimensional-parameter phase diagram derived here. Their boundedness criterion at equal source/target exponents is a \(\beta\)-Carleson tail condition, not the present squared-moment summability.

Blasco and Pennanen (arXiv:2609.21657v1) examine Cesàro operators with a Bergman-type kernel in the **unit disk**; the available full text does not state this several-variable \(S_2\) result. Galanopoulos, Girela, and Merchán (Journal of Mathematical Analysis and Applications 526 (2023), 127287, DOI below) study measure-induced Cesàro operators and Hilbert–Schmidt questions in the **unit disk**; disk results are acknowledged as prior work, not claimed as new. The multivariate monomial multiplicity and resulting threshold at \(\beta=n/2\) are absent from that one-dimensional setting. Hu and Tang (2010) classify Schatten(-Herz) membership for symbol-driven *extended Cesàro/Volterra* operators on the ball, and Stević (2010) gives Hilbert–Schmidt formulas for individual weighted radial composition operators. Their kernel mechanisms differ from the present positive-measure superposition, so these results do not directly provide the stated moment convolution. Established Schatten characterizations for **Toeplitz** operators on Bergman balls likewise concern a different operator class.

## Limitations

This result classifies Hilbert–Schmidt membership, not all Schatten classes or the numerical values of general operator norms. It assumes positive finite measures; arbitrary complex measures could cause cancellation and require different arguments. The complete 2023 unit-disk JMAA article could not be read through the attempted access routes, leaving a residual bibliographic risk for analogues or reductions; its specified domain is one complex variable and does not by itself cover the stated \(n\ge2\) classification. No independent audit has been carried out.

## References

1. J. Pan, C. Tong, and Z. Yang, *Weighted Cesàro type operators on the weighted Bergman spaces in the unit ball*, arXiv:2609.03243v1 (2026-09-03). https://arxiv.org/html/2609.03243v1
2. O. Blasco and T. Pennanen, *Cesàro operator induced by a Bergman kernel*, arXiv:2609.21657v1 (2026). https://arxiv.org/html/2609.21657v1
3. P. Galanopoulos, D. Girela, and N. Merchán, *Cesàro-type operators associated with Borel measures on the unit disc acting on some Hilbert spaces of analytic functions*, J. Math. Anal. Appl. 526 (2023), 127287. https://doi.org/10.1016/j.jmaa.2023.127287
4. Z. Hu and X. Tang, *Schatten(-Herz) class extended Cesàro operators on Bergman spaces in the unit ball of \(\mathbb C^n\)*, Proc. Amer. Math. Soc. 138 (2010), 2803–2814. https://doi.org/10.1090/S0002-9939-10-10365-7
5. S. Stević, *Weighted iterated radial composition operators between some spaces of holomorphic functions on the unit ball*, Abstr. Appl. Anal. (2010), article 801264. https://doi.org/10.1155/2010/801264
6. W. Yang and J. Liu, *Schatten classes of Toeplitz operators on Bergman–Besov Hilbert spaces in the unit ball*, J. Math. Anal. Appl. (2023), article 127257. https://doi.org/10.1016/j.jmaa.2023.127257
