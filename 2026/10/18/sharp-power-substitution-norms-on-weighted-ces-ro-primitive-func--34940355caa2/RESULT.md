# Sharp power-substitution norms on weighted Cesàro-primitive function spaces

## Finding
For real \(1\le p<\infty\) and \(0\le\sigma\le1\), let \(X_{p,\sigma}\) consist of equivalence classes of complex-valued, locally integrable functions on \((0,1)\) with finite norm
\[
 \|f\|_{p,\sigma}=\left(\int_0^1\left[x^{-\sigma}\int_0^x|f(t)|\,dt\right]^p dx\right)^{1/p}.
\]
For each \(\alpha>0\), define the power-substitution operator \((C_\alpha f)(x)=f(x^\alpha)\). The exact boundedness and norm profile is
\[
\boxed{\quad C_\alpha\in\mathcal B(X_{p,\sigma})\ \Longleftrightarrow\ 0<\alpha\le1;\qquad
\|C_\alpha\|=\alpha^{-1-1/p}\quad(0<\alpha\le1).\quad}
\]
The constant is independent of \(\sigma\), despite the change in the underlying norms. For \(0<\alpha<1\), no nonzero function attains this norm. At \(\alpha=1\) the operator is the identity and every nonzero function attains it. In particular the theorem applies simultaneously to the standard normalized Cesàro function space \(X_{p,1}\) and its primitive-integral counterpart \(X_{p,0}\).

## Assumptions and scope
Lebesgue measure on \((0,1)\) is used, functions may be real or complex, \(1\le p<\infty\), \(0\le\sigma\le1\), and \(\alpha>0\). Every function in \(X_{p,\sigma}\) is locally integrable on \([0,a]\) for every \(a<1\), as follows from positivity of the integral norm on any interval \([a,b]\subset(0,1)\). The composition is defined almost everywhere because the power map is nonsingular. Boundedness means it maps the whole space into itself and has finite operator norm. Values at the endpoints are irrelevant.

## Proof
Write \(F(u)=\int_0^u|f(t)|dt\), \(H_\sigma f(u)=u^{-\sigma}F(u)\), and \(G(x)=\int_0^x|f(t^\alpha)|dt\). When \(0<\alpha\le1\), the substitution \(u=t^\alpha\) gives
\[
 G(x)=\frac1\alpha\int_0^{x^\alpha}|f(u)|u^{1/\alpha-1}du
 \le\frac1\alpha x^{1-\alpha}F(x^\alpha).
\]
The inequality follows from \(u^{1/\alpha-1}\le x^{1-\alpha}\) for \(0<u<x^\alpha\). Dividing by \(x^\sigma\), raising to the \(p\)-th power and changing variables \(u=x^\alpha\) yields the precise intermediate bound
\[
 \|C_\alpha f\|_{p,\sigma}^p\le
 \alpha^{-(p+1)}\int_0^1 u^{\frac{(1-\alpha)[1+p(1-\sigma)]}{\alpha}}
 [H_\sigma f(u)]^pdu\le\alpha^{-(p+1)}\|f\|_{p,\sigma}^p.
\]
This proves the proposed upper bound. For \(0<\alpha<1\), the exponent of \(u\) in the intermediate integral is strictly positive; \(H_\sigma f\) is nonzero on a subset of positive measure whenever \(f\ne0\). Consequently the operator-norm inequality is strict for every nonzero function, proving nonattainment.

To establish sharpness, take \(f_\varepsilon=\mathbf1_{(1-\varepsilon,1)}\), \(0<\varepsilon<1\). Directly
\[
 \|f_\varepsilon\|_{p,\sigma}^p=
 \int_{1-\varepsilon}^1x^{-p\sigma}(x-1+\varepsilon)^pdx
 =\frac{\varepsilon^{p+1}}{p+1}(1+O(\varepsilon)),
\]
where the asymptotic holds for every fixed \(p,\sigma\). Its image is the interval indicator \(C_\alpha f_\varepsilon=\mathbf1_{((1-\varepsilon)^{1/\alpha},1)}\); its support width is \(\varepsilon/\alpha+O(\varepsilon^2)\). Therefore
\[
\lim_{\varepsilon\downarrow0}
\frac{\|C_\alpha f_\varepsilon\|_{p,\sigma}}{\|f_\varepsilon\|_{p,\sigma}}
=\alpha^{-1-1/p},
\]
showing the upper bound is sharp for \(0<\alpha\le1\).

Finally, if \(\alpha>1\), let \(g_r=\mathbf1_{(0,r)}\) with \(r\downarrow0\); then \(C_\alpha g_r=g_{r^{1/\alpha}}\). A direct calculation gives
\[
 \|g_r\|_{p,\sigma}^p=
 \frac{r^{1+p(1-\sigma)}}{1+p(1-\sigma)}+
 r^p\int_r^1x^{-p\sigma}\,dx.
\]
As \(r\downarrow0\), this expression is asymptotic to \(r^p/(1-p\sigma)\) if \(p\sigma<1\), to \(r^p\log(1/r)\) if \(p\sigma=1\), and to
\[
 r^{1+p(1-\sigma)}\left[\frac1{1+p(1-\sigma)}+\frac1{p\sigma-1}\right]
\]
if \(p\sigma>1\). In every case the leading power of \(r\) is positive and the ratio \(\|g_{r^{1/\alpha}}\|_{p,\sigma}/\|g_r\|_{p,\sigma}\) tends to infinity. Hence \(C_\alpha\) is unbounded for all \(\alpha>1\). The three cases include every boundary \(p\sigma=1\), as well as \(p=1\), \(\sigma=0\), and \(\sigma=1\).

## Verification
The stand-alone standard-library script `verify.py` checks exact integral identities for interval indicators, the sharp lower-bound behavior for multiple exponents and weights, and divergence of the lower-support test ratio on the unbounded side. Run `python3 verify.py` after extracting the included files. These finite checks are supplementary; the proof above establishes all continuous-parameter assertions.

## Relationship to prior work
Raj, Pandoh and Jamwal (2014) studied composition operators on Cesàro-type function spaces and asserted a general norm formula expressed by measure distortion. Jafari and Kamali (2020, Section 2) gave a counterexample to that purported general norm identity; their restricted boundedness theorem requires interval invariance and does not determine the sharp norm of the power maps treated here. The current exact family is not an assertion that the 2014 error was first discovered here. The paper of Curbera and Ricker (2016) studies abstract Cesàro spaces and their integral representations, not exact norms of these power substitutions. For the power maps with \(0<\alpha<1\), the measure-distortion supremum alone is \(1/\alpha\), strictly smaller than the norm \(\alpha^{-1-1/p}\); this illustrates why measure distortion does not determine the Cesàro operator norm.

## Limitations
No claim is made for \(p=\infty\), for weights \(\sigma>1\), or for general nonlinear composition symbols. The result does not determine the spectrum or essential norm of \(C_\alpha\). The formula is an analytic theorem, not a bibliographic guarantee of global priority; possible unindexed exact power-substitution results remain a literature risk. The 2014 general norm formula should not be used as a premise for this theorem; its inapplicability is independently visible from the exact interval-indicator calculations.

## References
- K. Raj, S. Pandoh, S. Jamwal, *Composition Operators on Cesàro Function Spaces*, Journal of Function Spaces (2014), article 501057, doi:10.1155/2014/501057; published online 2014-01-30.
- F. Jafari, Z. Kamali, *Some Properties of Composition Operators on Cesáro Function Spaces*, Journal of Mathematical Extension 14 (2020), 85–95, https://ijmex.com/index.php/ijmex/article/download/1093/450/6324.
- G. P. Curbera, W. J. Ricker, *Abstract Cesàro spaces: Integral representations*, Journal of Mathematical Analysis and Applications 441 (2016), 25–44, doi:10.1016/j.jmaa.2016.03.074.
