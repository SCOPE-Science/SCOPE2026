# A sharp Greenwood–exceedance covariance crossover for Dirichlet compositions

## Finding

Let \(m\ge 2\), let \((X_1,\ldots,X_m)\) have a Dirichlet distribution with strictly positive parameter vector \((\alpha_1,\ldots,\alpha_m)\), and put \(G=\sum_{j=1}^m X_j^2\). For an index \(i\), define \(s=\sum_j\alpha_j\), \(a_i=\alpha_i\), \(b_i=s-a_i\),
\[
 c_i=\frac{\sum_{j\ne i}\alpha_j(\alpha_j+1)}{b_i(b_i+1)},\qquad
 \tau_i=\frac{2c_i(s+1)-(1+c_i)(a_i+1)}{s(1+c_i)}.
\]
Write \(f_{a,b}(t)=t^{a-1}(1-t)^{b-1}/B(a,b)\) for the beta density. **The exact labeled covariance law** is, for every \(0<t<1\),
\[
 \operatorname{Cov}\bigl(\mathbf 1_{\{X_i>t\}},G\bigr)
 =\frac{1+c_i}{s+1}\,t(1-t) f_{a_i,b_i}(t)\,(t-\tau_i).
 \tag{1}
\]
In every admissible parameter vector, \(\tau_i<1\). If \(\tau_i>0\), this covariance is strictly negative for \(0<t<\tau_i\), vanishes only at \(t=\tau_i\), and is strictly positive for \(\tau_i<t<1\). If \(\tau_i\le 0\), it is strictly positive throughout \((0,1)\). Thus the labeled threshold statistic has either one sign reversal or none, with a complete exact criterion.

For the **symmetric Dirichlet family**, \(\alpha_1=\cdots=\alpha_m=\alpha>0\), define the exceedance count \(N_m(t)=\#\{j:X_j>t\}\). Then for every \(0<t<1\),
\[
 \operatorname{Cov}(N_m(t),G)
 =\frac{m(m\alpha+2)}{((m-1)\alpha+1)(m\alpha+1)}
 f_{\alpha,(m-1)\alpha}(t)\,t(1-t)
 \left(t-\frac{\alpha+1}{m\alpha+2}\right).
 \tag{2}
\]
The **unique sign switch** is exactly at \(t_m=(\alpha+1)/(m\alpha+2)\). For \(\alpha=1\), the vector is the collection of \(m\) uniform spacings and \(G\) is Greenwood's statistic; the formula becomes
\[
 \operatorname{Cov}(N_m(t),G)
 =\frac{(m-1)(m+2)}{m+1}\,t\left(t-\frac{2}{m+2}\right)(1-t)^{m-1}.
 \tag{3}
\]
In particular, the covariance of a count of gaps longer than \(t\) with their sum of squares is negative below \(2/(m+2)\), zero at that point, and positive above it. The threshold is asymptotically twice the mean gap.

There is also a joint Gaussian crossover. Fix \(\alpha>0\), \(y>0\) and let \(Z\) have gamma shape \(\alpha\), rate \(\alpha\), with density \(f_\alpha(y)=\alpha^\alpha y^{\alpha-1}e^{-\alpha y}/\Gamma(\alpha)\) and survival probability \(p_\alpha(y)=\Pr\{Z>y\}\). Under symmetric Dirichlet sampling as \(m\to\infty\),
\[
 \left(\frac{N_m(y/m)-mp_\alpha(y)}{\sqrt m},\;
 \sqrt m\left(mG-\frac{\alpha+1}{\alpha}\right)\right)
 \ \xrightarrow{d}\ \mathcal N_2(0,\Sigma_\alpha(y)),
 \tag{4}
\]
where
\[
 \Sigma_{11}=p_\alpha(y)(1-p_\alpha(y))-\frac{y^2 f_\alpha(y)^2}{\alpha},\qquad
 \Sigma_{22}=\frac{2(\alpha+1)}{\alpha^3},\qquad
 \Sigma_{12}=\frac{y f_\alpha(y)}{\alpha}\left(y-\frac{\alpha+1}{\alpha}\right).
 \tag{5}
\]
Both marginal variances are strictly positive. The two limiting Gaussian fluctuations are independent at exactly \(y=(\alpha+1)/\alpha\); their covariance is negative below and positive above that value. This limit also gives \(\lim_{m\to\infty}m\operatorname{Cov}(N_m(y/m),G)=\Sigma_{12}\).

## Assumptions and scope

All Dirichlet parameters are real and strictly positive; \(m\) is any integer at least two; all threshold statements apply only for \(0<t<1\). Equation (1) is a **labeled** coordinate result for arbitrary parameters; it does not assert a unique zero for the sum of labeled indicators under nonexchangeable parameters. Equations (2)–(5) require equal parameters, and the Gaussian statement fixes \(\alpha\) and \(y\) while \(m\) tends to infinity. Uniform spacings correspond to the symmetric case \(\alpha=1\). The statistical interpretation is dependence under the null distribution, not a claim of test optimality.

## Proof

**Conditional Dirichlet decomposition.** Fix \(i\), abbreviate \(a=a_i\), \(b=b_i\), \(c=c_i\), and \(X=X_i\). The marginal of \(X\) is beta\((a,b)\). Conditional on \(X=x\), the normalized remaining coordinates have Dirichlet parameters \((\alpha_j)_{j\ne i}\), whence
\[
 \mathbb E[G\mid X=x]=x^2+c(1-x)^2=(1+c)x^2-2cx+c.
 \tag{6}
\]
Indeed, the conditional normalized second moment of the \(j\)-th remaining coordinate is \(\alpha_j(\alpha_j+1)/(b(b+1))\).

**Exact beta tail identities.** For the beta density \(f=f_{a,b}\), its derivatives satisfy
\[
 [x(1-x)f(x)]'=(a-(a+b)x)f(x),\quad
 [x^2(1-x)f(x)]'=((a+1)x-(a+b+1)x^2)f(x).
\]
Integrating from \(t\) to one, with \(s=a+b\), yields
\[
 \operatorname{Cov}(\mathbf1_{\{X>t\}},X)
 =\frac{t(1-t)f(t)}s,
\]
\[
 \operatorname{Cov}(\mathbf1_{\{X>t\}},X^2)
 =\frac{t(1-t)f(t)}{s+1}\left(t+\frac{a+1}s\right).
\]
Substitute these identities into (6), factor the resulting affine polynomial, and obtain (1). The step is an identity for all positive real beta shapes, without an approximation.

**Sign classification.** Since \(\sum_{j\ne i}\alpha_j^2\le b^2\), one has \(0<c\le1\). Direct algebra gives
\[
 s(1+c)(\tau_i-1)=c(b+1)-(s+a+1)<0.
\]
Every other prefactor in (1) is strictly positive on \((0,1)\), so the stated classification follows. When all parameters equal \(\alpha\), one has \(c=(\alpha+1)/((m-1)\alpha+1)\) and \(\tau=(\alpha+1)/(m\alpha+2)\). Summing (1) over all \(i\) proves (2). Substituting \(\alpha=1\), including the beta density \((m-1)(1-t)^{m-2}\), yields (3). For instance, \((\alpha_1,\alpha_2,\alpha_3)=(100,1,1)\) gives \(\tau_1=-31/170\), so a zero inside \((0,1)\) is not guaranteed without symmetry.

**Joint asymptotic law.** Write \(X_j=Y_j/\sum_kY_k\) with independent gamma variables \(Y_j\) of shape \(\alpha\) and rate \(\alpha\). Let \(\overline Y=m^{-1}\sum_jY_j\), \(\mu_2=(\alpha+1)/\alpha\). Then
\[
 N_m(y/m)=\sum_j\mathbf1_{\{Y_j>y\overline Y\}},\qquad
 mG=\frac{m^{-1}\sum_jY_j^2}{\overline Y^2}.
\]
A standard empirical-cdf expansion at the random threshold \(y\overline Y\), justified by continuity of the gamma density and local empirical-process stochastic equicontinuity, together with the multivariate central limit theorem, gives influence variables
\[
 A_y(Y)=\mathbf1_{\{Y>y\}}-p_\alpha(y)-yf_\alpha(y)(Y-1),
\]
\[
 B(Y)=Y^2-\mu_2-2\mu_2(Y-1).
\]
The centered vector in (4) equals \(m^{-1/2}\sum_j(A_y(Y_j),B(Y_j))+o_p(1)\). The gamma moments give \(\operatorname{Var}(Y)=1/\alpha\), \(\operatorname{Cov}(Y,B)=0\), and \(\operatorname{Var}(B)=2(\alpha+1)/\alpha^3\). Gamma tail integration gives
\[
 \mathbb E[(Y-1)\mathbf1_{\{Y>y\}}]=yf_\alpha(y)/\alpha,
\]
\[
 \mathbb E[(Y^2-\mu_2)\mathbf1_{\{Y>y\}}]
 =yf_\alpha(y)\left(y/\alpha+(\alpha+1)/\alpha^2\right).
\]
Consequently the covariance matrix of \((A_y,B)\) is exactly (5), proving the joint normal limit. Strict positivity of \(\Sigma_{11}\) holds because a nonconstant indicator cannot coincide almost surely with an affine function of a continuously distributed gamma variable. Finally, the finite exact formula (2), after applying the gamma limit to the rescaled beta density, gives the stated limit of the (unscaled) covariances; this does not rely on unjustified moment convergence from weak convergence.

## Verification

Run `python checks/verify_dirichlet.py` after installing `requirements.txt`. The checker uses independent incomplete-beta polynomial integration (114 exact-rational cases with integer parameter profiles), high-precision incomplete-beta integration (30 cases with noninteger parameters), the symmetric finite-size-to-gamma coefficient comparison, and independent gamma-integral evaluations of the limiting covariance matrix (six cases). All reported checks passed in the supplied environment. Exact finite checks supplement rather than replace the analytic proof for arbitrary positive real parameters and all sample sizes.

## Relationship to prior work

Royen (2010, arXiv:1008.4059v1) obtains integral/orthogonal-series representations for the marginal distribution of the quadratic sum of symmetric and asymmetric Dirichlet components, including Greenwood's statistic. Its full text was examined for the proposed labeled exceedance mixed moment; no such identity or sign-phase classification was found. Ghosh and Jammalamadaka (1998) examine approximations, cumulants and quantiles of marginal spacing statistics, not their covariance with threshold counts. Pyke's 1965 survey establishes the classical spacings framework and much general asymptotic theory; its abstract and bibliographic record were available, but full-text comparison was not completed. General Gaussian empirical-process theory can imply an abstract form of the asymptotic statement; the finite exact mixed-moment identities and their all-parameter sign diagram are the distinctive claimed contribution. Absence from searched sources does not prove priority.

## Limitations

No independence is claimed at finite \(m\) when covariance vanishes; in (4) the independence at the crossover is specifically Gaussian *limiting* independence. The unsymmetric **total** exceedance count may exhibit a more complex sign pattern and is not classified here. No performance or power improvement for combined goodness-of-fit tests is established. The literature comparison is incomplete, especially for older comprehensive spacing surveys and possible equivalent formulations under Simpson concentration, squared coefficient of variation, or truncated beta moments.

## References

1. T. Royen, *The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic*, arXiv:1008.4059v1 (first posted 2010-08-24), https://arxiv.org/abs/1008.4059.
2. K. Ghosh and S. R. Jammalamadaka, *Small sample approximations for spacing statistics*, Journal of Statistical Planning and Inference 69 (1998), 245–261, DOI:10.1016/S0378-3758(97)00164-X, https://jammalam.faculty.pstat.ucsb.edu/html/Some%20Publications/1998_SmallSample%20AppoxSpacings_JSPI.pdf.
3. R. Pyke, *Spacings*, Journal of the Royal Statistical Society, Series B 27 (1965), 395–436, DOI:10.1111/j.2517-6161.1965.tb00602.x. Comparison limited to available summary.
