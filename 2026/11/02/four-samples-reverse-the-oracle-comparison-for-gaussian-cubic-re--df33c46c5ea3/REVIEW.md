# Independent mathematical audit

## correctness

PASS

For n≥2 iid N(0,1) and cubic f(x)=μ+bx+cx³, c≠0, OLS with intercept and h(x)=x is well-defined almost surely (residual sum squares Q>0). Exact decomposition into independent Gaussian sample mean M and centered residuals yields fitted-intercept error H=−2M³+M(3Q/n−U/Q)+T/n−3M²T/Q, and sign symmetry gives unbiasedness. Wick contractions and radial-angular χ²/sphere factorization yield exact E(H²)=6(n⁵+4n⁴−13n³+176n²−168n+480)/[n³(n+1)(n+3)(n+5)]. Independently reconstructed and symbolically checked rational moment identities in source and their combination; all n≥2 have finite needed ratios, including T=0 at n=2. Best fixed coefficient b+3c leaves variance 6c²/n; exact difference has negative polynomial P(n)=5n⁴+36n³−161n²+168n−480, negative P at 2 and 3 and positive for every integer n≥4; n=4 intercept 8c²/7 versus oracle 3c²/2. No claim against arbitrary integration rules or other integrands.

## originality

PASS

Best-of-knowledge original exact finite-n Gaussian cubic OLS-intercept risk and strict n=4 reversal relative to the best *fixed coefficient* control variate. Portier–Segers 2018 derive OLS control-variate integration and asymptotic behavior, Leluc et al 2022 analyze adaptive quadrature, and Blanchet et al 2023 use other regression-adjusted estimators; these generic theories do not explicitly provide this cubic residual Wick moment or sharp n=4 inequality. Resultary Gaussian regression findings address different estimators/objectives.

## value

PASS

A data-fitted intercept outperforming the population-fixed-coefficient variance optimum in a concrete minimal odd cubic Gaussian family illustrates a real finite-sample risk distinction. The exact all-n formula and unique switch at four observations clarify what is and is not meant by oracle within a restricted estimator class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
