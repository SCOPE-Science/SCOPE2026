# Critical independence and sharp Dirichlet rigidity for minimum spacing and above-mean counts

## Finding
For any \(m\ge3\), let \(X=(X_1,\ldots,X_m)\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\), with \(\alpha>0\). Let \(Z=\min_i X_i\) and \(N(t)=\sum_i\mathbf 1\{X_i>t\}\), for \(0<t<1\). The two random variables \(Z\) and \(N(t)\) are independent **if and only if** \(\alpha=1\) and \(t=1/m\).

For \(\alpha=1\), the whole conditional law of \(N(t)\) given \(Z=u\) is stochastically nondecreasing in \(u\) below \(t=1/m\), invariant at \(t=1/m\), and stochastically nonincreasing in \(u\) above \(t=1/m\). This yields, for any integrable nondecreasing \(g\) for which \(g(Z)\) is not almost surely constant and the covariance is finite,
\[
\operatorname{sgn}\operatorname{Cov}(g(Z),N(t))=
\begin{cases}
+1,&0<t<1/m,\\
0,&t=1/m,\\
-1,&1/m<t<1.
\end{cases}
\]
The zero denotes genuine independence, not merely vanishing linear covariance. In particular,
\[
\operatorname{Cov}(Z,N(t))=\frac{(1-mt)(1-t)^{m-1}-(1-mt)_+^m}{m(m-1)}.
\]

Moreover, for every fixed \(\alpha>0\) and \(u=1/m-h\), the conditional mean at the critical threshold satisfies
\[
\mathbb E_\alpha[N(1/m)\mid Z=u]
=(m-1)\left(\frac{m-1}{m}\right)^{m-2}
+(\alpha-1)\frac{(m-2)(m-1)^{m-1}}{2m^{m-3}}h^2
+O_{m,\alpha}(h^3),\qquad h\downarrow0.
\]
The coefficient is nonzero for every \(\alpha\ne1\); it is a quantitative sharpness mechanism for the independence characterization.

## Assumptions and scope
The symmetric Dirichlet law has the density proportional to \(\prod_{i=1}^m x_i^{\alpha-1}\) on \(x_i>0\), \(\sum_i x_i=1\). All exceedances are strict and \(0<t<1\); no threshold equality causes a probability mass because the joint law is continuous. The minimum has support \((0,1/m)\). Conditional distributions are stated for \(0<u<1/m\) using their continuous-density versions. The restriction \(m\ge3\) is essential: for \(m=2\), \(N(1/2)=1\) almost surely for every symmetric Dirichlet parameter, giving a degenerate additional independence case.

## Proof
**1. A conditional simplex transformation.** Almost surely, the minimizer \(J=\operatorname*{argmin}_i X_i\) is unique. Fix \(J=j\), \(Z=u\), and write \(k=m-1\). For the remaining labels let
\[
Y_i=\frac{X_i-u}{1-mu}\quad (i\ne j),\qquad \sum_{i\ne j}Y_i=1.
\]
The change of variables on the \((m-2)\)-dimensional conditional face gives a density proportional to
\[
\prod_{i\ne j}[u+(1-mu)Y_i]^{\alpha-1}
\]
relative to the uniform measure on the \((k-1)\)-simplex. The omitted factor \(u^{\alpha-1}(1-mu)^{m-2}\) depends on \(u\) but not on \(Y\). By symmetry, \(J\) is uniform and independent of \(Z\). If \(\alpha=1\), the residual \(Y\sim\operatorname{Dirichlet}(1,\ldots,1)\) is independent of \(Z\) and \(J\).

**2. The critical independence and stochastic order.** For \(\alpha=1\), conditionally on \(Z=u\),
\[
N(t)\overset d=\mathbf1\{u>t\}+\sum_{i=1}^{m-1}\mathbf1\{Y_i>q_t(u)\},\qquad q_t(u)=\frac{t-u}{1-mu}.
\]
For \(u\ne t\), its derivative is \(q_t'(u)=(mt-1)/(1-mu)^2\). When \(t<1/m\), the threshold decreases as \(u\) increases and the minimum's own exceedance eventually adds one. When \(t>1/m\), the threshold increases with \(u\), and the minimum never exceeds \(t\). Coupling all conditional laws with the same \(Y\) yields the stochastic directions asserted. At \(t=1/m\), \(q_t(u)=1/m\) for every \(u\), and \(\mathbf1\{u>t\}=0\); the conditional law is constant, proving independence. In the two off-critical regimes, there is a positive-probability interval of \(u\) on which the conditional mean changes strictly; the endpoints of its support have distinct conditional means. The independent-copy covariance identity, \(2\operatorname{Cov}(g(Z),f(Z))=\mathbb E[(g(Z)-g(Z'))(f(Z)-f(Z'))]\), gives the strict covariance signs for every \(g\) nonconstant and nondecreasing almost surely.

**3. Exact uniform-simplex covariance.** For \(\alpha=1\), \(\Pr(Z>u)=(1-mu)^{m-1}\) for \(0<u<1/m\), and \(\mathbb EZ=1/m^2\). Also \(\mathbb EN(t)=m(1-t)^{m-1}\). For a fixed coordinate, integrate \(\Pr(X_1>t,Z>u)\) over \(u\). It equals \([1-t-(m-1)u]_+^{m-1}\) for \(0<u<t\), and \((1-mu)_+^{m-1}\) for \(u\ge t\). Thus
\[
\mathbb E[Z\mathbf1\{X_1>t\}]=\frac{(1-t)^m}{m(m-1)}-\frac{(1-mt)_+^m}{m^2(m-1)}.
\]
Summing over coordinates and subtracting \(\mathbb EZ\,\mathbb EN(t)\) proves the displayed covariance. Its sign agrees with the stochastic order and vanishes precisely at \(t=1/m\).

**4. Uniqueness of the critical parameter.** For arbitrary \(\alpha>0\), if \(t<1/m\), every conditional sample with \(u>t\) has \(N(t)=m\), whereas for sufficiently small positive \(u\), there is positive conditional probability that \(N(t)<m\). If \(t>1/m\), conditional samples for \(u\) sufficiently near \(1/m\) have \(N(t)=0\), whereas at sufficiently small \(u\) there is positive probability of an exceedance. Consequently, independence can occur only at \(t=1/m\).

For that threshold set \(u=1/m-h\) with \(h>0\) small, and let \(Q=\sum_{i=1}^{m-1}Y_i^2\). Relative to uniform \(Y\), the conditional density weight is
\[
W_h(Y)=\prod_{i=1}^{m-1}\left[\frac1m+h(mY_i-1)\right]^{\alpha-1}.
\]
Using \(\sum_iY_i=1\), one has \(\sum_i(mY_i-1)=1\) and \(\sum_i(mY_i-1)^2=m^2Q-m-1\). The first-order term of \(\log W_h\) is constant in \(Y\), so normalized expectation expands as
\[
\mathbb E_\alpha[N(1/m)\mid Z=1/m-h]
=\mathbb E_1[N(1/m)]-\frac{(\alpha-1)m^4h^2}{2}
\operatorname{Cov}_{\nu}(N(1/m),Q)+O_{m,\alpha}(h^3),
\]
where \(\nu=\operatorname{Dirichlet}(1,\ldots,1)\) has \(m-1\) coordinates. For \(k=m-1\), \(Y_1\sim\operatorname{Beta}(1,k-1)\),
\[
\mathbb E[Q\mid Y_1=y]=y^2+\frac{2(1-y)^2}{k},\quad \mathbb EQ=\frac2{k+1},
\]
so integrating this quadratic conditional mean against the beta density on \(y>1/(k+1)\) yields
\[
\operatorname{Cov}_{\nu}(N(1/m),Q)=-\frac{(m-2)(m-1)^{m-1}}{m^{m+1}}<0.
\]
Also \(\mathbb E_\nu N(1/m)=(m-1)((m-1)/m)^{m-2}\). Substitution proves the claimed expansion, whose nonzero quadratic coefficient for \(\alpha\ne1\) rules out independence. This completes the if-and-only-if classification.

## Verification
The standalone `verify.py` performs exact-rational sign tests through \(m=59\), derives the critical quadratic-concentration covariance independently by finite polynomial integration through \(k=21\), and evaluates exact conditional expectations for \(m=3,\alpha=2\) at four near-critical minimum values. Additional deterministic quadrature tests cover three nonunit Dirichlet parameters. It reports 261 passed checks. These checks establish consistency of finite identities but do not replace the general proof. Execute with `python verify.py`; the script requires Python 3 and SciPy.

## Relationship to prior work
Uniform spacings and symmetric Dirichlet laws are classical. Griffiths and Spanò study canonical correlation kernels for Dirichlet measures, not minimum-versus-threshold-count independence; Telgarsky studies Dirichlet sparsity bounds but not minimum-conditioned independence or local parameter rigidity. Pyke's historical survey develops spacing distribution theory; its full text addresses classical distributions and asymptotics, but does not state this fixed-dimensional minimum/count independence and rigidity theorem. Previously accessible exact spacing exceedance results concern maximum, Shannon entropy, quadratic concentration, and pairwise exceedance counts; none implies the parameter-uniqueness classification merely by replacing a statistic's name. The familiar Dirichlet simplex density and beta moments are standard, not novel contributions. The claimed contribution is the complete independence/monotone-regression phase classification and the exact second-order rigidity coefficient.

## Limitations
The characterization requires symmetry of the Dirichlet parameters and at least three coordinates; it does not address general nonsymmetric Dirichlet laws. It concerns a deterministic exceedance threshold and minimum, not statistical independence between the minimum and the entire count process. An equivalent historical result in other spacing literature cannot be excluded even after full-text inspection of Pyke’s survey. Finite numerical checks are corroboration, not formal verification of the general theorem. The result does not imply that the same classification holds for non-Dirichlet compositions.

## References
- R. C. Griffiths and D. Spanò, *Orthogonal polynomial kernels and canonical correlations for Dirichlet measures*, arXiv:1003.5131, first public version March 26, 2010; *Bernoulli* 19 (2013), 548–598.
- M. Telgarsky, *Dirichlet draws are sparse with high probability*, arXiv:1301.4917, first public version January 21, 2013.
- R. Pyke, *Spacings*, *Journal of the Royal Statistical Society, Series B* 27 (1965), 395–436; historical full-text comparison.
