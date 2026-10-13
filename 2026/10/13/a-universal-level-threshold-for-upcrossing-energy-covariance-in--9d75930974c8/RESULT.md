# A universal level threshold for upcrossing–energy covariance in a Gaussian autoregression

## Finding
For a stationary centered Gaussian autoregression, the covariance between the number of upward crossings of a fixed level and the empirical quadratic energy admits an exact expression. It changes sign at a unique nonzero standardized level when successive observations are positively correlated, whereas it is always positive when successive observations are negatively correlated.

Let \(n\ge 2\), \(\sigma>0\), \(-1<\rho<1\), and let \((X_j)\) be a centered stationary Gaussian process with \(\operatorname{Cov}(X_i,X_j)=\sigma^2\rho^{|i-j|}\). Write
\[
U_n(a)=\sum_{i=1}^{n-1}\mathbf1\{X_i\le\sigma a<X_{i+1}\},\qquad Q_n=\sum_{j=1}^{n}X_j^2.
\]
Here \(a\in\mathbb R\) is a standardized level. Denote the standard normal density and distribution by \(\phi\) and \(\Phi\). Put \(s=\sqrt{1-\rho^2}\) and \(h=a(1-\rho)/s\). Then
\[
\boxed{\operatorname{Cov}(U_n(a),Q_n)=\frac{\sigma^2\phi(a)}{1-\rho^2}\left(\sum_{r=1}^{n-1}(1-\rho^{2r})\right)\left[a(1+\rho^2)(2\Phi(h)-1)-2\rho s\phi(h)\right].}
\]
For \(\rho<0\), this covariance is positive for all real \(a\). For \(\rho=0\), it is zero exactly at \(a=0\), and positive otherwise. For \(0<\rho<1\), there is exactly one \(a_*(\rho)>0\) such that the covariance is negative for \(|a|<a_*(\rho)\), zero at \(|a|=a_*(\rho)\), and positive for \(|a|>a_*(\rho)\). The critical standardized level is independent of \(n\) and \(\sigma\), is bounded by
\[
0<a_*(\rho)^2\le\frac{\rho(1+\rho)}{1+\rho^2}<1,
\]
and has endpoint limits
\[
\lim_{\rho\downarrow0}\frac{a_*(\rho)}{\sqrt\rho}=1,\qquad \lim_{\rho\uparrow1}a_*(\rho)=1.
\]

## Assumptions and scope
All parameters range over the domains stated above. The autoregression may equivalently be realized by \(X_1\sim N(0,\sigma^2)\) and independent Gaussian innovations in \(X_{j+1}=\rho X_j+\sigma\sqrt{1-\rho^2}\,Z_{j+1}\). Equality at the crossing level has probability zero. This is a statement about discrete-time upcrossings and **uncentered** empirical quadratic energy \(Q_n\); it is not a claim about differentiable continuous-time crossings, or a sample variance with a fitted sample mean.

## Proof
Standardize \(Y_j=X_j/\sigma\), fix an adjacent pair \((Y_i,Y_{i+1})=(Y,V)\) with correlation \(\rho\), and put \(A=\{Y\le a<V\}\). Let
\[
L=\mathbb E[(Y^2-1)\mathbf1_A],\qquad R=\mathbb E[(V^2-1)\mathbf1_A].
\]
Because \((x^2-1)\phi(x)=-(x\phi(x))'\), integrating the conditional Gaussian formulas over \((\!-\infty,a]\) and \((a,\infty)\) gives
\[
L=\phi(a)\left[-a\Phi(-h)+\rho^2a\Phi(h)-\rho s\phi(h)\right],
\]
\[
R=\phi(a)\left[a\Phi(h)-\rho^2a\Phi(-h)-\rho s\phi(h)\right].
\]
For completeness, the derivative of \(\Phi((\rho x-a)/s)\) is \((\rho/s)\phi((\rho x-a)/s)\), and the Gaussian density identity
\[
\frac{\phi(x)\phi((a-\rho x)/s)}s=\frac{\phi(a)\phi((x-\rho a)/s)}s
\]
reduces the remaining boundary integrals to first moments of a truncated normal. Hence
\[
L+R=\phi(a)\left[a(1+\rho^2)(2\Phi(h)-1)-2\rho s\phi(h)\right].
\]
The autoregressive Markov property and Gaussian conditional second moments imply, for \(j\le i\),
\[
\mathbb E[Y_j^2-1\mid Y_i,Y_{i+1}]=\rho^{2(i-j)}(Y_i^2-1),
\]
and, for \(j\ge i+1\), the analogous identity conditioned on \(Y_{i+1}\), with factor \(\rho^{2(j-i-1)}\). Thus
\[
\operatorname{Cov}(\mathbf1_{A_i},Q_n)/\sigma^2=L\sum_{j=1}^{i}\rho^{2(i-j)}+R\sum_{j=i+1}^{n}\rho^{2(j-i-1)}.
\]
Summing in \(i=1,\ldots,n-1\), the two geometric-weight sums have the same total \(\sum_{r=1}^{n-1}(1-\rho^{2r})/(1-\rho^2)\), proving the boxed covariance identity.

The geometric factor and \(\phi(a)\) are positive. For real \(a\), \(a[2\Phi(ca)-1]\ge0\) with \(c=\sqrt{(1-\rho)/(1+\rho)}>0\). Consequently the sign is positive whenever \(\rho<0\); the \(\rho=0\) assertion follows immediately. For \(\rho>0\), the bracket is even in \(a\), negative at zero, and positive for sufficiently large \(|a|\). For \(a>0\), its zero equation can be written
\[
a(1+\rho^2)J(ca)=\rho s,\qquad J(z)=\frac{2\Phi(z)-1}{2\phi(z)}=\int_0^z\exp\!\left(\frac{z^2-u^2}{2}\right)\,du.
\]
Both \(a\mapsto a\) and \(J(z)\) increase strictly on the positive axis, so there is exactly one solution. Further, \(J(h)\ge h\) implies
\[
a_*^2=\frac{\rho(1+\rho)}{1+\rho^2}\frac{h}{J(h)}\le\frac{\rho(1+\rho)}{1+\rho^2}.
\]
The upper bound forces \(a_*\to0\) as \(\rho\downarrow0\), and the equality above with \(J(h)/h\to1\) proves \(a_*/\sqrt\rho\to1\). As \(\rho\uparrow1\), the upper bound keeps \(a_*<1\), so \(h=a_*\sqrt{(1-\rho)/(1+\rho)}\to0\) and the same identity gives \(a_*\to1\).

## Verification
The standalone `check_crossing.py` independently numerically integrates the two truncated-Gaussian second moments, checks sign transitions and the algebraic upper bound at many parameter values, and compares analytic covariances with six independently simulated stationary autoregressions. Run `python check_crossing.py` with NumPy and SciPy installed; the expected final line is `PASS: 349 deterministic and randomized checks.` These checks corroborate the displayed identities, while the proof above supplies the all-parameter result.

## Relationship to prior work
Kratz's survey (2006, arXiv:math/0612577) documents Rice formulas, Gaussian level-crossing moments, chaos expansions and approximations. Sinn and Keller (2011) investigate zero-crossing *count–count* covariances rather than an upcrossing count coupled to quadratic energy. Di Bernardino, León and Tchumatchenko (2014) treat correlations between continuous-time level-crossing processes in multiple Gaussian signals. These are not the finite discrete autoregressive mixed covariance and level-dependent sign classification proved here. The **zero-level** sign-change versus energy result is a special case and is **not** presented as novel; the contribution is the full level profile, exact all-sample-size formula and sharp transition.

## Limitations
Historical completeness cannot be guaranteed: older general Gaussian-chaos or crossing generating formulas could encode the second-chaos projection of an indicator and imply part of this result indirectly. The complete Sinn–Keller paper was not accessible for direct comparison and remains a named residual risk. No claim is made for non-Gaussian innovations, nonstationary series, continuous-time crossings, or a sample-centered variance. Numerical checks are not certificates of infinitely many parameter values. No independent scientific audit has been performed.

## References
1. M. F. Kratz (2006), *Level crossings and other level functionals of stationary Gaussian processes*, Probability Surveys 3, 230–288; arXiv:math/0612577, doi:10.1214/154957806000000087.
2. M. Sinn and K. Keller (2011), *Covariances of Zero Crossings in Gaussian Processes*, Theory of Probability and Its Applications 55(3), doi:10.1137/S0040585X97984991.
3. E. Di Bernardino, J. León and T. Tchumatchenko (2014), *Cross-Correlations and Joint Gaussianity in Multivariate Level Crossing Models*, Journal of Mathematical Neuroscience 4:22, doi:10.1186/2190-8567-4-22.
