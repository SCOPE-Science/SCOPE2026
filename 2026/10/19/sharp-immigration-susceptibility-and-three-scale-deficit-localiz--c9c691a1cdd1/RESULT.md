# Sharp immigration susceptibility and three-scale deficit localization at a Gamma coexistence boundary

## Finding
For the stochastic logistic diffusion with environmental multiplicative noise and constant immigration defined below, the equilibrium law responds to weak immigration in three sharply distinct ways. The conventional total-variation distance between the stationary law at immigration rate \(\varepsilon>0\) and that at zero immigration has the **exact leading coefficient**
\[
 d_{\mathrm{TV}}(\pi_\varepsilon,\pi_0)\sim H_\alpha(s),\qquad s=\frac{b\varepsilon}{D^2}\downarrow0,
\]
where
\[
 H_\alpha(s)=
 \begin{cases}
 \dfrac{\Gamma(1-\alpha)}{\Gamma(1+\alpha)}s^\alpha,&0<\alpha<1,\\[5pt]
 s\log(1/s),&\alpha=1,\\[5pt]
 \dfrac{(\alpha-1)^{\alpha-2}e^{-(\alpha-1)}}{\Gamma(\alpha)}s,&\alpha>1.
 \end{cases}
\]
The **abundance scales carrying the missing equilibrium mass** also differ. Write \(Y=bX/D\), let \(f_s\) be the stationary density of \(Y\) at dimensionless immigration \(s\), and let \(f_0\) be its zero-immigration Gamma density. The normalized deficiency law
\[
 \nu_s^-(dy)=\frac{(f_0(y)-f_s(y))_+}{d_{\mathrm{TV}}(f_s,f_0)}\,dy
\]
has the following three limits as \(s\downarrow0\):

* If \(0<\alpha<1\), the image law under \(y\mapsto y/s\) converges **in total variation** to the probability density
\[
 g_\alpha(z)=\frac{\alpha}{\Gamma(1-\alpha)}z^{\alpha-1}(1-e^{-1/z})\boldsymbol 1_{\{z>0\}}.
\]
* If \(\alpha=1\), the image law under \(y\mapsto\log(y/s)/\log(1/s)\) converges **weakly** to the uniform law on \([0,1]\). Deficit mass is spread over logarithmic abundance scales, not confined to one narrow boundary layer.
* If \(\alpha>1\), \(\nu_s^-\) itself converges **in total variation** to a bulk law with density
\[
 \frac{f_0(y)}{C_\alpha}\left(\frac1y-\frac1{\alpha-1}\right)_+,
 \qquad C_\alpha=\frac{(\alpha-1)^{\alpha-2}e^{-(\alpha-1)}}{\Gamma(\alpha)}.
\]
These are exact limits, not finite-sample fitting statements.

## Assumptions and scope
Fix \(D>0\), \(b>0\), and \(\alpha>0\). The process is the one-dimensional Itô stochastic differential equation on \((0,\infty)\)
\[
 dX_t=\bigl[D(\alpha+1)X_t-bX_t^2+\varepsilon\bigr]dt+\sqrt{2D}\,X_t\,dW_t,\qquad X_0>0,
\]
with constant immigration \(\varepsilon\ge0\). Here \(D\) is the multiplicative-noise intensity, \(b\) is self-regulation, and \(\alpha\) is the shape of the stationary Gamma law at \(\varepsilon=0\). No interactions, environmental colored noise, demographic absorption, finite-number individual sampling, or perturbation of \(D,b,\alpha\) is assumed.

The unique stationary law \(\pi_\varepsilon\) has density proportional to
\[
 x^{\alpha-1}\exp\left(-\frac{bx}{D}-\frac{\varepsilon}{Dx}\right),\quad x>0.
\]
At \(\varepsilon=0\) this is the Gamma law with shape \(\alpha\) and rate \(b/D\); at positive immigration it is generalized inverse Gaussian. These density identities are prior knowledge, not claimed as discoveries. Upon setting \(Y=bX/D\) and \(s=b\varepsilon/D^2\), the normalized density is
\[
 f_s(y)=\frac{f_0(y)e^{-s/y}}{Z_\alpha(s)},\quad
 f_0(y)=\frac{y^{\alpha-1}e^{-y}}{\Gamma(\alpha)},\quad
 Z_\alpha(s)=\int_0^\infty f_0(y)e^{-s/y}dy.
\]
Total variation means \(\tfrac12\int_0^\infty |f_s-f_0|dy\). All asymptotics are for fixed \(D,b,\alpha\), with \(\varepsilon\downarrow0\); no claim is made for a joint limit in \(\alpha\).

## Proof
**1. Stationarity and uniqueness.** With \(x>0\), the stationary candidate \(p(x)=x^{\alpha-1}\exp(-bx/D-\varepsilon/(Dx))\) satisfies the zero-current identity
\[
 [D(\alpha+1)x-bx^2+\varepsilon]p(x)-\frac{d}{dx}[Dx^2p(x)]=0.
\]
The logarithmic coordinate \(R_t=\log X_t\) solves
\[
 dR_t=[D\alpha-be^{R_t}+\varepsilon e^{-R_t}]dt+\sqrt{2D}\,dW_t.
\]
Its drift points inward at both ends (at the left end the limit is \(D\alpha>0\) if \(\varepsilon=0\), and becomes more positive if \(\varepsilon>0\)); the stationary speed density above is integrable and the endpoints are not attained in finite time. One-dimensional regular diffusion theory then yields conservativity, positive recurrence, irreducibility, and uniqueness of the stationary probability. Normalization of the \(Y\)-density gives
\[
 Z_\alpha(s)=\frac{2s^{\alpha/2}K_\alpha(2\sqrt s)}{\Gamma(\alpha)},\quad s>0,
\]
although the proof of the asymptotics uses only the integral representation.

**2. Normalization loss and its three regimes.** Define \(\delta(s)=1-Z_\alpha(s)\). Then
\[
 \delta(s)=\frac1{\Gamma(\alpha)}\int_0^\infty y^{\alpha-1}e^{-y}(1-e^{-s/y})dy.
\]
For \(0<\alpha<1\), substitute \(y=sz\) and use dominated convergence, with dominating integrable function \(z^{\alpha-1}(1-e^{-1/z})\). Integration by parts gives
\[
 \int_0^\infty z^{\alpha-1}(1-e^{-1/z})dz=\frac{\Gamma(1-\alpha)}{\alpha}.
\]
Consequently \(\delta(s)\sim \Gamma(1-\alpha)s^\alpha/\Gamma(1+\alpha)\). For \(\alpha=1\), split the integral into \((0,s)\), \((s,1)\), \((1,\infty)\); the middle interval contributes \(s\log(1/s)+O(s)\) and the others contribute \(O(s)\), giving \(\delta(s)\sim s\log(1/s)\). For \(\alpha>1\), dominated convergence applied to \((1-e^{-s/y})/s\le1/y\) gives \(\delta(s)/s\to\mathbb E_0[1/Y]=1/(\alpha-1)\).

**3. Total-variation constants.** The density difference \(f_s-f_0=f_0(e^{-s/y}/Z_\alpha(s)-1)\) changes sign once, at
\[
 y_*(s)=\frac{s}{-\log Z_\alpha(s)},
\]
negative below and positive above. Hence
\[
 d_{\mathrm{TV}}(f_s,f_0)=\frac1{Z_\alpha(s)}\int_0^\infty f_0(y)\,[e^{-s/y}-Z_\alpha(s)]_+dy.
\]
For \(\alpha\le1\), \(s/\delta(s)\to0\). At every fixed \(y>0\), \([e^{-s/y}-Z_\alpha(s)]_+/\delta(s)\to1\); it is bounded above by \(1\). Dominated convergence therefore proves \(d_{\mathrm{TV}}/\delta\to1\), yielding the first two exact constants.

For \(\alpha>1\), \((f_s-f_0)/s\to f_0(y)\bigl((\alpha-1)^{-1}-y^{-1}\bigr)\) in \(L^1(dy)\): this follows from \((1-e^{-s/y})/s\le 1/y\), the integrability of \(f_0/y\), and the normalization limit. Hence the TV coefficient is the positive integral above \(\alpha-1\):
\[
 \int_{\alpha-1}^\infty f_0(y)\left(\frac1{\alpha-1}-\frac1y\right)dy
 =\frac{(\alpha-1)^{\alpha-2}e^{-(\alpha-1)}}{\Gamma(\alpha)},
\]
using the incomplete-Gamma recurrence (or integration by parts). This proves the third coefficient.

**4. Localization of the negative difference.** For \(0<\alpha<1\), change variables \(y=sz\) in \((f_0-f_s)_+/d_{\mathrm{TV}}\). Its density equals
\[
 \frac{s^\alpha}{\Gamma(\alpha)d_{\mathrm{TV}}}z^{\alpha-1}e^{-sz}\left(1-\frac{e^{-1/z}}{Z_\alpha(s)}\right)_+.
\]
Since \(Z_\alpha(s)<1\), the positive-part factor is bounded by \(1-e^{-1/z}\); dominated convergence in \(L^1(dz)\), together with the TV limit, yields \(g_\alpha\) and total-variation convergence.

For \(\alpha=1\), \(y_*(s)\sim 1/\log(1/s)\). For every fixed \(t\in(0,1)\), the interval \((0,s^{1-t})\) lies inside the deficiency region for small \(s\), and
\[
 \int_0^{s^{1-t}}(f_0-f_s)(y)dy
 =s\,t\log(1/s)+O(s)+o(s\log(1/s)).
\]
Indeed on this interval replacing \(1-e^{-s/y}/Z_\alpha(s)\) by \(1-e^{-s/y}\) changes the integral by at most \(\delta(s)s^{1-t}/Z_\alpha(s)\), and \(e^{-y}\) causes a lower-order error. After division by TV, the distribution function of \(\log(Y/s)/\log(1/s)\) tends to \(t\). Its mass below zero tends to zero, while the support has upper endpoint tending to one, so weak convergence to \(\operatorname{Uniform}[0,1]\) follows.

For \(\alpha>1\), the already established \(L^1\) derivative for \((f_0-f_s)/s\), together with \(d_{\mathrm{TV}}/s\to C_\alpha\), yields total-variation convergence of the normalized deficiency density to the displayed bulk law. This completes the proof of all claims.

## Verification
The attached standalone `check.py` uses symbolic differentiation to verify the stationary-current cancellation, an exact Bessel normalization identity evaluated numerically, and high-precision numerical quadrature for the three sharp TV regimes. It also checks the integral normalizing the subcritical boundary density and the critical logarithmic CDF at three points. Run `python check.py` with dependencies listed in `requirements.txt`. Numerical quadratures probe finite immigration parameters and do not prove the limits; the infinite-limit arguments are contained above.

## Relationship to prior work
Megías et al. (2026, arXiv:2609.30154) study the Gamma baseline for abundance fluctuations and distinguish regular and near-extinction regimes by its shape; the present scalar diffusion uses this zero-interaction Gamma context. Mallmin et al. (2026) already model immigration and derive the generalized inverse Gaussian stationary family. Neither stationary family nor the existence of this density is claimed to be new. Konzou (2021), Theorem 2, gives general explicit total-variation **upper bounds** for convergence of generalized inverse Gaussian distributions to Gamma laws, with half-integer rate corollaries and the one-crossing TV identity. That prior result already bears on the *orders* of the rates and is explicitly credited. The present claim concerns the matching sharp **constants for every fixed positive shape** and the three limiting **locations of the negative density discrepancy**, including the critical log-uniform law. An upper rate bound alone neither yields these sharp constants nor proves these signed-deficit localization limits.

## Limitations
The model is a one-species no-interaction ecological surrogate with environmental multiplicative noise and constant immigration. Its stationary law is previously known. No multispecies interaction, finite-time mixing, extinction risk for finite stochastic populations, or statistically optimal estimator is analyzed. The three regimes refer to fixed \(\alpha\), not a joint critical scaling where \(\alpha\) varies with immigration. Historical priority for all parts of the asymptotic/localization statement has not been independently certified; more general special-function or perturbation theory may subsume it.

## References
1. A. Megías, V. J. Ontiveros, D. Alonso, and J. A. Capitán, *Consistent determination of stability regimes in natural ecological communities from abundance time series*, arXiv:2609.30154 (first posted 2026-09-24). https://arxiv.org/abs/2609.30154
2. E. Mallmin et al., *Fluctuating Growth Rates Link Turnover and Unevenness in Species-Rich Communities*, *Ecology Letters* 29 (2026), e70333. https://doi.org/10.1111/ele.70333
3. E. Konzou, *Rate of convergence in total variation for the generalized inverse Gaussian and the Kummer distributions*, *Open Journal of Mathematical Sciences* 5 (2021), 182–191. https://doi.org/10.30538/oms2021.0155
4. E. Konzou, A. K. Koudou, and K. E. Gneyou, *Rate of convergence of generalized inverse Gaussian and Kummer distributions to the gamma distribution via Stein's method*, *Statistics & Probability Letters* 159 (2020), 108683.
