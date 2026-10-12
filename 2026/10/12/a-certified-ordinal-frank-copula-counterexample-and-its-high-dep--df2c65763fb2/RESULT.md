# A certified ordinal Frank-copula counterexample and its high-dependence mechanism

## Finding

**Theorem (correlation inflation after ordinal Frank-copula discretization).** Let \((U,V)\) be uniform on \([0,1]\) marginally, with bivariate Frank copula
\[
 C_\theta(u,v)=-\frac1\theta\log\left(1-\frac{(1-e^{-\theta u})(1-e^{-\theta v})}{1-e^{-\theta}}\right),\qquad\theta>0.
\]
There are identically distributed twenty-category ordinal variables with labels \(1,\ldots,20\), obtained by thresholding \((U,V)\) at strictly increasing rational points, for which the ordinal Pearson correlation **exceeds** the latent Spearman correlation \(\rho_S(\theta)=\operatorname{Corr}(U,V)\). Specifically, take \(\theta=15\), and let the nineteen thresholds be

\[
\begin{gathered}
0.14357,\ 0.20483,\ 0.25318,\ 0.29517,\ 0.33333,\\
0.36901,\ 0.40301,\ 0.43591,\ 0.46812,\ 0.50000,\\
0.53188,\ 0.56409,\ 0.59699,\ 0.63099,\ 0.66667,\\
0.70483,\ 0.74682,\ 0.79517,\ 0.85643.
\end{gathered}
\]
Each displayed finite decimal is an **exact rational number**. Define
\[
 X=1+\sum_{j=1}^{19}{\bf1}\{U>t_j\},\qquad
 Y=1+\sum_{j=1}^{19}{\bf1}\{V>t_j\}.
\]
The accompanying deterministic rational-arithmetic certificate establishes
\[
\boxed{\operatorname{Corr}(X,Y)>0.93092569,\quad
\rho_S(15)<0.92938730,\quad
\operatorname{Corr}(X,Y)-\rho_S(15)>0.00153839.}
\]
More accurate values, for orientation only, are
\[
\operatorname{Corr}(X,Y)=0.930925698735820068\ldots,\qquad
\rho_S(15)=0.929365805485040129\ldots.
\]

The failure is structural rather than an isolated accidental choice of cutpoints. Let \((U_\theta,V_\theta)\) follow the Frank copula with parameter \(\theta\), and set \(g(u)=(1-\cos(\pi u))/2\). Then
\[
\boxed{\lim_{\theta\to\infty}\theta^2\left[\operatorname{Corr}(g(U_\theta),g(V_\theta))-\rho_S(\theta)\right]=\frac{\pi^2}{6}(12-\pi^2)>0.}
\]
For every sufficiently large fixed positive \(\theta\), finite integer-scored ordinal quantizers of the same increasing \(g\) have correlations exceeding \(\rho_S(\theta)\).

## Assumptions and scope

Only the bivariate Frank copula with positive parameter is considered. The variables \(U,V\) have standard uniform margins, the specified thresholds lie strictly between zero and one, and every ordinal category has positive probability. Both ordinal scores are the consecutive integers \(1,\ldots,20\); no nonlinear relabelling of ordinal categories is used. The 2026 source explicitly compares the Pearson correlation after discretization with the latent Frank-copula Spearman correlation, not with the ordinal variables' tie-adjusted rank correlation. Our comparison uses exactly those two statistics. The main assertion is existential, not an optimality or smallest-number-of-categories result.

## Proof

**1. Exact finite-dimensional identity.** For uniform \((U,V)\) and any cutpoints \(t_1<\cdots<t_{m-1}\), Hoeffding's covariance identity, or direct indicator expansion, gives
\[
\begin{aligned}
 A_\theta&=\operatorname{Cov}(X,Y)
 =\sum_{i,j=1}^{m-1}\left[C_\theta(t_i,t_j)-t_it_j\right],\\
 B&=\operatorname{Var}(X)=\operatorname{Var}(Y)
 =\sum_{i,j=1}^{m-1}\left[\min(t_i,t_j)-t_it_j\right].
\end{aligned}
\]
Every \(t_i\) is rational, and \(B>0\), so \(\operatorname{Corr}(X,Y)=A_\theta/B\). For \(\theta>0\), writing \(a=\min(u,v)\), \(b=\max(u,v)\), the Frank expression has the numerically stable exact form
\[
C_\theta(u,v)=a-\frac1\theta\log R_\theta(u,v),\qquad
R_\theta(u,v)=\frac{1+e^{-\theta(b-a)}-e^{-\theta b}-e^{-\theta(1-a)}}{1-e^{-\theta}}.
\]
Its numerator is positive. At \(\theta=15\), the finite sum \(A_{15}\) therefore requires only exponentially and logarithmically transformed rational arguments. The supplied `check_frank.py` encloses every value between **exact rational endpoints**; no floating-point comparison is used to certify the sign. Its exact integer comparison yields a lower bound \(A_{15}/B>0.93092569\).

**2. Rigorous upper bound for latent Spearman correlation.** The standard Debye formula for the Frank copula is
\[
\rho_S(\theta)=1-\frac{12}{\theta}\big(D_1(\theta)-D_2(\theta)\big),\qquad
D_k(\theta)=\frac{k}{\theta^k}\int_0^\theta\frac{s^k}{e^s-1}\,ds.
\]
Using \(1/(e^s-1)=\sum_{n\ge1}e^{-ns}\) for \(s>0\) and positive-term integration yields
\[
\rho_S(\theta)=1-\frac{12\zeta(2)}{\theta^2}
+\frac{48\zeta(3)}{\theta^3}
+\frac{12 E_1(\theta)}{\theta^2}
-\frac{48 E_2(\theta)}{\theta^3},
\]
where \(E_1(\theta)=\sum_{n\ge1}e^{-n\theta}(1+n\theta)/n^2\) and \(E_2(\theta)=\sum_{n\ge1}e^{-n\theta}(1+n\theta+(n\theta)^2/2)/n^3\) are nonnegative. For positive integers \(N\), elementary integral-tail comparisons give
\[
\zeta(2)\ge \sum_{n=1}^Nn^{-2}+\frac1{N+1},\quad
\zeta(3)\le \sum_{n=1}^Nn^{-3}+\frac1{2N^2}.
\]
With \(q=e^{-\theta}\), \(E_1\le q/(1-q)+\theta q/(1-q)^2\). At \(\theta=15\), the rational bounds for \(q\) and \(N=35\) give \(\rho_S(15)<0.92938730\), proving the strict difference asserted above. This bound deliberately discards the negative \(E_2\) term and is therefore conservative.

**3. Why the certificate is a proof, not a numerical search.** For every rational \(s\in[0,15]\), compute \(S_{85}(s)=\sum_{j=0}^{85}s^j/j!\) and \(T_{86}(s)=s^{86}/86!\). All summands are rational and nonnegative. Since successive omitted terms have ratio at most \(s/87<1\),
\[
S_{85}(s)\le e^s\le S_{85}(s)+\frac{T_{86}(s)}{1-s/87}.
\]
Taking reciprocals brackets \(e^{-s}\). Likewise for \(y\in[1,3]\), with \(z=(y-1)/(y+1)\in[0,1/2]\), the identity
\[
\log y=2\sum_{j\ge0}\frac{z^{2j+1}}{2j+1}
\]
has a positive tail beyond the first twenty-two terms bounded by \(2z^{45}/(45(1-z^2))\). Rounding lower endpoints down and upper endpoints up at denominator \(10^{20}\) preserves enclosure. The checker computes all \(19^2\) terms with these enclosures and finally compares rational numbers by exact cross-multiplication. The output shows a certified strict gap larger than \(0.00153839\). Finite calculation is exhaustive for this finite, explicitly stated example; it makes no assertion about other thresholds.

**4. Structural high-dependence mechanism.** For any nonconstant \(h\in C^1([0,1])\), integration by parts gives the covariance-deficit identity
\[
\operatorname{Var}(h(U_\theta))-\operatorname{Cov}(h(U_\theta),h(V_\theta))
=\int_0^1\!\int_0^1h'(u)h'(v)\,[\min(u,v)-C_\theta(u,v)]\,du\,dv.
\]
By the stable Frank representation from Step 1, the integrand's bracket is \(\theta^{-1}\log R_\theta(u,v)\). For \(0\le u,v\le1\), the Fréchet upper bound ensures \(R_\theta\ge1\). From the explicit fraction,
\[
0\le\log R_\theta(u,v)
\le e^{-\theta|u-v|}+\frac{e^{-\theta}}{1-e^{-\theta}}.
\]
In the interior scaling \(v=u+w/\theta\), \(R_\theta\to1+e^{-|w|}\). Boundedness of \(h'\), the exponential majorant and \(\theta e^{-\theta}/(1-e^{-\theta})\to0\) justify dominated convergence after the change of variables, with boundary intervals converging to the real line. Thus
\[
\lim_{\theta\to\infty}\theta^2
\big(\operatorname{Var}(h(U_\theta))-\operatorname{Cov}(h(U_\theta),h(V_\theta))\big)
=\frac{\pi^2}{6}\int_0^1h'(u)^2du,
\]
using \(\int_{-\infty}^{\infty}\log(1+e^{-|w|})\,dw=\pi^2/6\), obtained by integrating its absolutely convergent alternating exponential series. Since each transformed marginal has the same positive variance, divide by \(\operatorname{Var}(h(U))\). For \(h(u)=u\), this quotient is \(12\); for \(g(u)=(1-\cos\pi u)/2\), it is \(\pi^2\), since \(\operatorname{Var}(g(U))=1/8\) and \(\int_0^1g'(u)^2du=\pi^2/8\). Subtracting the two correlation-deficit limits proves
\[
\lim_{\theta\to\infty}\theta^2\{\operatorname{Corr}(g(U_\theta),g(V_\theta))-
\rho_S(\theta)\}=\frac{\pi^2}{6}(12-\pi^2)>0.
\]
Finally, for each positive integer \(m\), define the nondecreasing integer-valued quantizer
\[
Q_m(u)=1+\sum_{j=1}^{m-1}{\bf1}\{g(u)>j/m\}.
\]
Because \(0\le g\le1\), \(|Q_m(u)/m-g(u)|\le1/m\), uniformly in \(u\). At every sufficiently large **fixed** \(\theta\), its correlations converge to the correlation of \(g(U_\theta),g(V_\theta)\) by uniform convergence and positive limiting variance; thus a finite \(m\) retains the strict inflation. This is an existence assertion for each such \(\theta\), not a uniform finite bound on \(m\).

## Verification

Run `python3 check_frank.py` with Python 3; only the standard library is required. The script reports the rationally certified output:

```
theta 15 categories 20
corr_lower 0.93092569873582
corr_upper 0.93092569873582
rho_upper 0.92938729464884
certified_gap_lower 0.00153840408698
proof: strictly positive rational gap, using Taylor enclosures and integral test
```

The printed decimals are **rounded presentations** of exact rational endpoints; the decisive `assert` uses the exact fractions. Independently, high-precision evaluation of all 361 original Frank-CDF terms and the Debye integrals yields \(\operatorname{Corr}(X,Y)\approx0.930925698735820068\) and \(\rho_S(15)\approx0.929365805485040129\). This secondary numerical check is not used for the certified inequality. No finite computation substitutes for the separate large-\(\theta\) analytical argument.

## Relationship to prior work

Barbiero (2026, Sections 2.2 and 5) explicitly proposes universal attenuation of the ordinal Pearson correlation relative to the latent Spearman correlation as a **conjecture**. The numerical study optimizes ordinal margins for \(2\le m\le11\) and latent Spearman correlations up to \(0.9\), and Theorem 2 proves **sign preservation**, not attenuation. Our example has \(m=20\) and \(\rho_S(15)\approx0.92937\), beyond both explored grid ranges, and contradicts the conjectured magnitude bound while respecting positivity. The earlier copula-calibration work of Barbiero (2021) describes constructing discrete distributions with chosen correlation and does not give the claimed universal Frank attenuation inequality. Standard covariance identities and Debye functions are pre-existing tools, not claimed as discoveries here. The research novelty asserted is the **mathematically certified Frank-ordinal counterexample together with its high-dependence explanation**, not the identity for the copula or a general Gaussian extremal theorem.

## Limitations

The quantitative witness uses positive dependence and these particular twenty categories; no minimal number of categories, optimal margin, or complete finite-parameter phase diagram is claimed. The asymptotic formula assumes each transformed variable is generated by the same nonconstant continuously differentiable function, and its finite quantization conclusion is pointwise in each sufficiently large parameter. These results do not question the earlier theorem on preservation of the **sign** of correlation. An equivalent independently published counterexample may escape the indexed literature inspected. Independent scientific audit has not been performed.

## References

1. Alessandro Barbiero, *The Frank copula as a latent model for ordinal variables: dependence structure, correlation attenuation, and statistical inference*, Advances in Data Analysis and Classification, first public 26 September 2026. DOI: 10.1007/s11634-026-00709-1. https://link.springer.com/article/10.1007/s11634-026-00709-1
2. Alessandro Barbiero, *Inducing a desired value of correlation between two point-scale variables: a two-step procedure using copulas*, AStA Advances in Statistical Analysis (2021). DOI: 10.1007/s10182-021-00405-9. https://link.springer.com/article/10.1007/s10182-021-00405-9
3. The elementary covariance identity and the Frank-copula Debye representation are reproduced in the primary source above; their earlier references are acknowledged there.
