# Critical-window extreme-value crossover for the slashed inverse-Rayleigh law

## Finding

Let \(X\) have inverse-Rayleigh density \(f_X(x)=2\theta x^{-3}\exp(-\theta/x^2)\) on \((0,\infty)\), and let \(Y_q\sim\mathrm{Beta}(q,1)\) be independent of \(X\), for \(\theta,q>0\). Write \(Z_q=X/Y_q\), \(S_q(z)=\Pr(Z_q>z)\), and
\[
L(z)=\log(z^2/\theta),\qquad
\Phi(w)=\int_0^1 e^{-wt}\,dt
=\begin{cases}(1-e^{-w})/w,&w\ne0,\\1,&w=0.\end{cases}
\]
Let \(\gamma_{\mathrm E}\) denote the Euler--Mascheroni constant. **Uniform critical-window theorem:** for every finite \(K>0\), as \(z\to\infty\), uniformly for real \(|w|\le K\), set \(q(z,w)=2+2w/L(z)\). Then \(q(z,w)>0\) for all sufficiently large \(z\), and
\[
\boxed{
S_{q(z,w)}(z)=\frac{\theta}{z^2}
\left[L(z)\Phi(w)+1-\gamma_{\mathrm E}e^{-w}
+O_K\!\left(L(z)^{-1}\right)\right].}
\]
The leading factor \(\Phi(w)\) interpolates strictly and continuously across the boundary \(q=2\); fixed-parameter tail limits do not give this moving-parameter statement.

**Triangular-array extreme-value theorem:** fix any real \(\kappa\). For each sufficiently large integer \(n\), draw independent \(Z_{n,1},\ldots,Z_{n,n}\), each with the above law at
\[
q_n=2+\frac{2\kappa}{\log n},\qquad
b_n=\sqrt{\theta n\log n},\qquad M_n=\max_{1\le j\le n}Z_{n,j}.
\]
For every \(x>0\),
\[
\boxed{\lim_{n\to\infty}\Pr(M_n\le b_nx)
=\exp\!\left(-\frac{\Phi(\kappa)}{x^2}\right).}
\]
There is a quantitative finite-size correction. Uniformly for \(\kappa\) in any fixed compact interval and \(x\) in any fixed compact subinterval of \((0,\infty)\),
\[
\boxed{
 n S_{q_n}(b_nx)=\frac{1}{x^2}\left[
\Phi(\kappa)+
\frac{1+e^{-\kappa}(\log\log n+2\log x-\gamma_{\mathrm E})}{\log n}
+O\!\left(\frac{(1+\log\log n)^2}{(\log n)^2}\right)
\right].}
\]
The corresponding maximum-CDF error is of order at most \((1+\log\log n)/\log n\) on such compact ranges, and its displayed leading correction can be inserted into \(\exp(-nS_{q_n}(b_nx))\).

## Assumptions and scope

All probabilities are under independent inverse-Rayleigh and beta factors as defined above. No assumption of a finite variance is made. The first formula concerns \(z>\sqrt\theta\) tending to infinity, with bounded real \(w\); the second concerns independent observations **within each row** of a triangular array, where the shape parameter changes with row size. There is no asserted coupling or independence between different rows. All \(O\)-constants are uniform only on the explicitly stated compact parameter sets. The theorem does not describe arbitrary unbounded \(w\) or a shape parameter approaching two at a rate outside the stated window.

## Proof

**1. Exact survival formula.** The stated density integrates to \(F_X(x)=\exp(-\theta/x^2)\). For \(a=\theta/z^2\), conditioning on \(Y_q\) gives
\[
S_q(z)=\int_0^1 qy^{q-1}\bigl(1-e^{-a/y^2}\bigr)\,dy.
\]
Substitute \(t=a/y^2\) in the exponential term and integrate by parts. For every \(a,q>0\),
\[
S_q(z)=1-e^{-a}+a^{q/2}\Gamma(1-q/2,a),
\qquad\Gamma(s,a)=\int_a^\infty e^{-t}t^{s-1}\,dt.
\]
The integral definition is valid for any real \(s\) because \(a>0\).

**2. Uniform two-term expansion.** Put \(q=2+2\eta\) and \(\eta=w/L\), where \(L=\log(1/a)\). Division by \(a\) gives
\[
\frac{S_q(z)}{a}=\frac{1-e^{-a}}a+
 a^\eta\int_a^\infty e^{-t}t^{-1-\eta}\,dt.
\]
Split the integral into its singular elementary part on \((a,1)\) and a regular remainder:
\[
\begin{aligned}
R_a(\eta)&=\int_a^1(e^{-t}-1)t^{-1-\eta}\,dt
 +\int_1^\infty e^{-t}t^{-1-\eta}\,dt,\\
a^\eta\int_a^1t^{-1-\eta}\,dt
&=\frac{1-a^\eta}{\eta}=L\Phi(w).
\end{aligned}
\]
The last formula is understood by continuity at \(\eta=0\). Whenever \(|\eta|\le1/2\), the integrands defining \(R_0(\eta)\) are integrable and their \(\eta\)-derivatives are dominated by integrable functions (use \(|e^{-t}-1|\le t\) for \(t<1\) and exponential decay for \(t>1\)). Hence \(R_0(\eta)=R_0(0)+O(|\eta|)\). Furthermore, \(|R_a(\eta)-R_0(\eta)|\le C a^{1-\eta}\), which after multiplication by \(a^\eta\) is \(O(a)\). The classical exponential-integral constant identity gives
\[
R_0(0)=\int_0^1\frac{e^{-t}-1}{t}\,dt
+\int_1^\infty\frac{e^{-t}}t\,dt=-\gamma_{\mathrm E}.
\]
Because \(a^\eta=e^{-w}\), \((1-e^{-a})/a=1+O(a)\), and \(|\eta|\le K/L\), we obtain, uniformly for \(|w|\le K\),
\[
\frac{S_{2+2w/L}(z)}a
=L\Phi(w)+1-\gamma_{\mathrm E}e^{-w}+O_K(L^{-1}).
\]
This is the first assertion, including its nonzero constant term and the boundary case \(w=0\).

**3. Extreme-value interpolation.** For fixed \(x>0\), define \(N=\log n\), \(d=\log N+2\log x\), and \(z=b_nx\). Then \(a=1/(nNx^2)\), \(L=\log(1/a)=N+d\), and \(\eta=(q_n-2)/2=\kappa/N\). In particular \(w=\eta L\to\kappa\). The first assertion yields \(nS_{q_n}(b_nx)\to x^{-2}\Phi(\kappa)\), so
\[
\Pr(M_n\le b_nx)=\bigl(1-S_{q_n}(b_nx)\bigr)^n
\longrightarrow \exp(-x^{-2}\Phi(\kappa)).
\]
To obtain the rate and constant, expand the elementary expression directly:
\[
L\Phi(w)=\frac{1-e^{-\kappa(1+d/N)}}{\kappa/N}
=N\Phi(\kappa)+e^{-\kappa}d+O_K(d^2/N),
\]
with the identity valid by continuity at \(\kappa=0\). The constant part of the first assertion is \(1-\gamma_{\mathrm E}e^{-\kappa}+O_K(d/N)\). Multiplying the combined formula by \(na=(Nx^2)^{-1}\) gives the displayed two-term expansion, uniform on compact \(\kappa,x\)-ranges. Finally \(nS_{q_n}(b_nx)^2=O(n^{-1})\), and \(\log(1-u)=-u+O(u^2)\) gives the maximum-CDF error bound. This proves both claims.

## Verification

The accompanying `verify_sir_crossover.py` uses high-precision upper incomplete gamma evaluation and an independent conditional integral based on \(-q\log Y_q\sim\mathrm{Exp}(1)\). It passes 14 direct representation comparisons, seven fixed-parameter boundary checks (background only), five first-order critical-window tests, five second-order triangular-array tests, and three extreme-value limits. To reproduce, run `python verify_sir_crossover.py` with Python 3, `mpmath` and `scipy`. These finite checks are diagnostics; the preceding estimates provide the infinite-parameter proof.

## Relationship to prior work

Gómez, Gallardo, Bourguignon and Venegas (2026) define the slashed inverse-Rayleigh law via the ratio representation, derive its survival function, and discuss regular variation in Proposition 8 (printed page 23269). The fixed-parameter, three-regime tail classification follows from its integral survival formula and is not presented here as a new claim. The present statement instead makes \(q\) approach the critical value **at the reciprocal logarithmic rate**, proves a uniform two-term bridge, and extracts an explicit triangular-array maximum law and finite-size correction. Pointwise fixed-\(q\) regular variation does not imply these uniform moving-\(q\) assertions.

Classical product-tail literature, including Denisov and Zwart (2007), covers regular variation for products of fixed independent laws, often with moment assumptions. It supplies important context but no model-specific \(q_n=2+2\kappa/\log n\) triangular-array coefficient or the displayed two-term expansion. Almuhayfith and coauthors (2023) study a differently oriented inverse-Weibull product with a **bounded multiplicative** uniform factor; their distribution does not reproduce the reciprocal-beta tail amplification considered here.

## Limitations

This theorem treats a precise moving-parameter regime, not general triangular arrays with arbitrary varying \(q_n\). The quantile and maximum limits are asymptotic, not exact finite-\(n\) tail risk guarantees. The expansion is not uniform as \(|w|\to\infty\); at such scales it must be matched to different regimes. Independent scholarly review and assessment of possible unpublished or unindexed equivalent results remain outstanding. No assertion is made that the cited 2026 paper itself claimed an incorrect tail exponent.

## References

1. H. W. Gómez, D. I. Gallardo, M. Bourguignon and O. Venegas, “EM algorithm in the slashed inverse Rayleigh regression model with an application,” *AIMS Mathematics* **11** (2026), 23262–23281, DOI: 10.3934/math.2026938. Published 30 July 2026. Full text: https://www.aimspress.com/aimspress-data/math/2026/7/PDF/math-11-07-938.pdf.
2. D. Denisov and B. Zwart, “On a theorem of Breiman and a class of random difference equations,” *Journal of Applied Probability* **44** (2007), 1031–1046, DOI: 10.1239/jap/1197908822.
3. F. E. Almuhayfith, T. Arslan, H. S. Bakouch et al., “A versatile model for lifetime of a component under stress,” *Scientific Reports* **13** (2023), article 20202, DOI: 10.1038/s41598-023-47313-3.
