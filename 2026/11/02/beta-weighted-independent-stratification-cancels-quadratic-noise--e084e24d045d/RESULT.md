# Beta-weighted independent stratification cancels quadratic noise using only endpoint interpolation

## Finding

Let \(m\ge1\) be an integer, \(h=1/m\), \(x_i=ih\), and let independent \(U_i\sim\operatorname{Beta}(2,2)\) have density \(q(u)=6u(1-u)\) on \((0,1)\). For \(f\in C^3([0,1])\), define the endpoint interpolant \(L_i(u)=(1-u)f(x_i)+uf(x_i+h)\) and the randomized integration rule
\[
Q_m(f)=h\sum_{i=0}^{m-1}\left\{\frac{f(x_i)+f(x_i+h)}2+\frac{f(x_i+hU_i)-L_i(U_i)}{6U_i(1-U_i)}\right\}.
\]
Then \(Q_m\) is unbiased, is equal to \(\int_0^1 f(x)\,dx\) almost surely for every polynomial of degree at most two, and obeys the **sharp asymptotic law**
\[
\lim_{m\to\infty}m^7\operatorname{Var}(Q_m(f))
=\frac1{25920}\int_0^1[f'''(x)]^2\,dx.
\]
Whenever the right-hand side is positive,
\[
m^{7/2}\left(Q_m(f)-\int_0^1f\right)
\xrightarrow{\mathrm d}\mathcal N\left(0,\frac1{25920}\int_0^1[f'''(x)]^2\,dx\right).
\]
For \(M=\lVert f'''\rVert_\infty>0\), every \(t>0\) and every \(m\ge1\) satisfy
\[
\Pr\left(\left|Q_m(f)-\int_0^1 f\right|\ge t\right)
\le2\exp\left(-\frac{72m^7t^2}{M^2}\right).
\]
If \(M=0\), the error vanishes identically. In particular, for every cubic \(f(x)=ax^3+bx^2+cx+d\), the *finite-sample* variance is exactly \(a^2/(720m^7)\).

The beta density is unique among **fixed, positive-almost-everywhere importance densities** for which the same independent one-sample-per-cell, endpoint-linear-residual estimator is pathwise exact on every quadratic. It is also the unique such fixed density whose variance is \(O(m^{-7})\) **on every** \(C^3\) integrand. For comparison, with independent uniform within-cell sampling and the same linear residual control variate, each \(f\in C^2([0,1])\) has
\[
\lim_{m\to\infty}m^5\operatorname{Var}(Q_m^{\mathrm{unif}}(f))
=\frac1{720}\int_0^1[f''(x)]^2\,dx.
\]

## Assumptions and scope

The integrand is a real-valued \(C^3\) function on \([0,1]\), the mesh is uniform, arithmetic is exact, and one independent beta-distributed point is sampled per cell. Endpoints are shared, giving \(2m+1\) distinct function evaluation locations (\(m+1\) endpoints and \(m\) random interior points) with probability one. Formulae containing a division by \(q(U_i)\) are well defined almost surely since \(U_i\in(0,1)\). The uniqueness comparison concerns densities \(q\) independent of mesh size and positive almost everywhere; it does not compare arbitrary correlated designs, higher-degree interpolants, or adaptive algorithms. The normal limit is nondegenerate only if \(f'''\) is not identically zero.

## Proof

**Unbiasedness.** On cell \(i\), set \(r_i(u)=f(x_i+hu)-L_i(u)\). As \(U_i\) has density \(q\),
\[
\mathbb E\frac{r_i(U_i)}{q(U_i)}=\int_0^1r_i(u)\,du.
\]
The integral of \(L_i\) is exactly the endpoint trapezoidal term, so multiplying by \(h\) and summing establishes unbiasedness.

**Quadratic annihilation and uniqueness.** For a quadratic, the interpolation remainder is \(r_i(u)=-a h^2u(1-u)\), where \(a\) is its quadratic coefficient. Therefore \(r_i(u)/q(u)=-ah^2/6\) is constant under the stated beta law. For any competing fixed density \(w\) that is positive almost everywhere, applying the estimator to \(f(x)=x^2\) gives
\[
\operatorname{Var}(Q_m^{(w)}(x^2))
=m^{-5}\operatorname{Var}_w\left(\frac{U(1-U)}{w(U)}\right),
\]
possibly infinite. If this variance is zero, \(u(1-u)/w(u)\) must be constant almost everywhere. The normalization \(\int_0^1 w=1\) forces \(w(u)=6u(1-u)\). Equivalently, Cauchy–Schwarz gives \(\int_0^1u^2(1-u)^2/w(u)\,du\ge1/36\), with equality only for this density. Every other fixed density has positive or infinite variance on the quadratic and hence fails the universal \(O(m^{-7})\) criterion.

**Sharp \(C^3\) variance.** Taylor's theorem, with a remainder controlled by the modulus of continuity of \(f'''\), gives uniformly in \(i\) and \(0\le u\le1\), after division by \(u(1-u)\) and continuous extension to endpoints,
\[
\frac{r_i(u)}{6u(1-u)}
=-\frac{h^2}{12}f''(x_i)-\frac{h^3}{36}(1+u)f'''(x_i)+o(h^3).
\]
For a rigorous uniform divided-remainder estimate, subtract the cubic Taylor polynomial in the local coordinate; the remainder's second derivative is bounded by \(h^3\omega_{f'''}(h)\), and the elementary interpolation inequality \(|g(u)-L_g(u)|\le\tfrac12\lVert g''\rVert_\infty u(1-u)\) applies. Since \(\operatorname{Var}(U_i)=1/20\), independence and uniformity of the remainder give
\[
\operatorname{Var}(Q_m)=\frac{h^8}{25920}\sum_{i=0}^{m-1}[f'''(x_i)]^2+o(mh^8).
\]
The Riemann sum proves the stated variance limit. For cubics, the displayed expansion is exact, so the variance is exactly \(a^2/(720m^7)\).

**Central limit.** The centered cell contributions are independent and each is bounded by a constant times \(h^4\lVert f'''\rVert_\infty\). After multiplication by \(m^{7/2}\), their largest magnitudes are \(O(m^{-1/2})\), which verifies Lindeberg. Their variances sum to the positive stated limit, and the Lindeberg–Feller triangular-array theorem gives the asserted Gaussian limit.

**Finite-sample concentration.** Subtract the quadratic Taylor polynomial on each cell. Since the second derivative of its remainder, expressed in the local unit coordinate, has absolute value at most \(Mh^3\), the interpolation inequality implies that the beta-weighted remainder differs from a deterministic quadratic contribution by at most \(Mh^3/12\). Hence each independent random cell contribution to \(Q_m\) has an interval of possible values of width at most \(Mh^4/6\). Hoeffding's inequality gives \(2\exp(-2t^2/(mM^2h^8/36))\), which is the displayed bound.

**Uniform-sampling comparator.** The ordinary uniform residual estimator has cell residual \(r_i(u)=-\frac{h^2}{2}f''(x_i)u(1-u)+o(h^2)\), uniformly. Since \(\operatorname{Var}(U(1-U))=1/180\) for uniform \(U\), summing independent cell variances gives the \(m^{-5}\) limit with coefficient \(1/720\).

## Verification

The standalone \(\texttt{verify.py}\) uses Python's standard library and exact rational arithmetic to check beta moments, polynomial exactness, unbiasedness on a cubic, the cubic variance identity, the uniform benchmark moment, and quartic asymptotic constants. Its seeded finite-input checks verify the implemented quadrature formula. Run \(\texttt{python3 verify.py}\). These finite computations supplement, rather than certify, the all-dimensional and all-integrand analytic statements.

## Relationship to prior work

Kunsch's 2023 stratified control-variate analysis provides a general high-confidence randomized-integration context and employs independent uniform residual samples, not the fixed beta-weighted linear-interpolation rule above. Wu's 2020 randomized trapezoidal method uses randomized evaluation pairs with antithetic structure and does not give this beta-residual identity. Leluc–Portier–Segers–Zhuman's 2022 adaptive importance-sampling/control-variate framework is more general in methodology but does not directly state the particular one-interior-evaluation per cell beta law, the unique quadratic annihilation in this family, its sharp \(m^{-7}\) variance constant, or its Gaussian limit. Generic zero-variance importance sampling and quadratic interpolation error formulae are established ideas and are not claimed as novel separately. The distinct contribution is their exact independent stratified endpoint-linear synthesis with its sharp distributional and concentration laws.

## Limitations

The result assumes independent sampling, a fixed beta law, exact function evaluation and exact arithmetic. Cancellation near the endpoints can affect floating-point implementations; no finite-precision guarantee is proved. The uniqueness statement is restricted to a precisely specified fixed-density family and does not imply minimax optimality across all sampling methods. Earlier specialized literature may contain a mathematically equivalent formulation, so publication priority requires independent verification. The normal limit concerns the asymptotic centered error, not finite-sample normality.

## References

- R. J. Kunsch, *Linear Monte Carlo quadrature with optimal confidence intervals*, arXiv:2309.09059 (first public 2023-09-16), https://arxiv.org/abs/2309.09059.
- Y. Wu, *A randomised trapezoidal quadrature*, arXiv:2011.15086 (first public 2020-11-30), https://arxiv.org/abs/2011.15086.
- R. Leluc, F. Portier, J. Segers, and J. Zhuman, *A Quadrature Rule combining Control Variates and Adaptive Importance Sampling*, arXiv:2205.11890 (first public 2022-05-24), https://arxiv.org/abs/2205.11890.
