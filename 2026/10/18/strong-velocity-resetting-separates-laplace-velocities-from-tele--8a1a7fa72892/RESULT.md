# Strong velocity resetting separates Laplace velocities from telegraph transport

## Finding

Let \(S\) be a stationary symmetric telegraph process with flip rate \(\lambda>0\). Between resets let \(\dot V_r=\Sigma S-g(V_r)\), where \(\Sigma>0\). An independent rate-\(r\) Poisson clock resets only the velocity to zero, retaining \(S\). Start the velocity and sign in their joint stationary law and set \(X_r(t)=\int_0^t V_r(s)\,ds\) (no position resets). Define \(Y_r=rV_r/\Sigma\). With the drag hypotheses below and fixed \(\lambda,\Sigma,g\), the following hold as \(r\to\infty\):

1. For each fixed time,
   \[
   W_2\bigl(\mathcal L(Y_r(t)),\operatorname{Laplace}(0,1)\bigr)
   \le\sqrt{24\lambda/r}+\sqrt{6}\,L/r,
   \]
   with unit-scale Laplace density \(e^{-|y|}/2\).
2. At fixed distinct times \(t_1,\ldots,t_m\), the vector of rescaled velocities converges in law to \((S(t_j)E_j)_{j=1}^m\), where the \(E_j\) are independent mean-one exponentials independent of the whole sign process. In particular \(\operatorname{Var}(Y_r(0))\to 2\) and \(\operatorname{Cov}(Y_r(0),Y_r(t))\to e^{-2\lambda t}\) for every fixed \(t>0\). The limiting variance-normalized autocorrelation is \(\tfrac12 e^{-2\lambda t}\) for \(t>0\), and equals \(1\) at zero lag; its right-hand limit at zero is \(1/2\).
3. For each fixed \(T>0\), on the shared-orientation coupling,
   \[
   \left\|\sup_{0\le t\le T}\left|\frac r\Sigma X_r(t)-\int_0^tS(s)\,ds\right|\right\|_2\longrightarrow 0.
   \]
   Consequently \(r^2\operatorname{Var}(X_r(T))/\Sigma^2\to T/\lambda-(1-e^{-2\lambda T})/(2\lambda^2)\).

Instantaneous marks thus persist in the separated-time velocity law, but their fluctuations disappear from the integrated trajectory. The result compares finite-horizon paths and does not assert convergence of the instantaneous velocity to a continuous-path process, or a nonlinear long-time diffusivity limit.

## Assumptions and scope

Suppose \(g\) is odd, nondecreasing and \(C^1\) near \([-b,b]\), with \(b>0\), \(g(0)=0\), \(g(b)=\Sigma\), and \(L=\sup_{|v|\le b}|g'(v)|\). Both drifts point inward or are tangent at the endpoints. The interval is invariant and any reset starts the velocity at zero in it. Examples are \(g(v)=\tan v\) with \(b=\arctan\Sigma\) and \(L=1+\Sigma^2\), and \(g(v)=\tanh v\) with \(0<\Sigma<1\), \(b=\operatorname{arctanh}\Sigma\), and \(L\le 1\). The examples are taken at fixed parameters; estimates involving \(L\) are not uniform over unbounded drag slopes.

## Proof

On a two-sided stationary construction let \(A_r(t)\) be the time since the last reset, \(Z_r(t)=rA_r(t)\), and \(\tau=t-A_r(t)\). Velocity is determined by the sign history since \(\tau\), which gives uniqueness of its law in the stationary joint process. The ages are independent of the sign trajectory, and at each time \(A_r(t)\sim\operatorname{Exp}(r)\). Drag opposes velocity and \(\pm b\) are barriers, so \(|V_r(t)|\le\min(b,\Sigma A_r(t))\). Integrating the equation after \(\tau\) gives
\[
Y_r(t)-S(t)Z_r(t)=r\int_\tau^t (S(s)-S(t))\,ds-\frac r\Sigma\int_\tau^t g(V_r(s))\,ds.
\]
The first term is zero if there is no flip since the reset and has magnitude at most \(2rA_r(t)\) otherwise. Given age \(a\), the flip probability is at most \(\lambda a\). The second term has magnitude at most \(LrA_r(t)^2/2\). The squared \(L^2\) norms are thus at most \(4r^2\lambda\mathbb E A_r^3=24\lambda/r\) and \(L^2r^2\mathbb E A_r^4/4=6L^2/r^2\), respectively. The triangle inequality gives the claimed bound because \(S(t)Z_r(t)\) is unit Laplace.

For distinct observation times take nonoverlapping backward windows of common length \(d>0\) smaller than the minimum separation (any \(d>0\) for one time). The clipped ages \(A_r(t_j)\wedge d\) are independent. If a clipped age equals \(d\), add to it an independent fresh \(\operatorname{Exp}(r)\) age; these extended variables are independent exponentials of rate \(r\) and independent of \(S\). They agree with the actual ages whenever all windows contain a reset, whose complement has probability at most \(m e^{-rd}\). The preceding coupling bound then gives the joint limit. The bound \(|Y_r(t)|\le Z_r(t)\) gives bounded fourth moments and uniform integrability of products at pairs of times. The telegraph identity \(\mathbb E[S(0)S(t)]=e^{-2\lambda t}\), exponential moments \(\mathbb E E_j=1\), \(\mathbb E E_j^2=2\), and sign symmetry prove the covariance and variance formulas.

For the path limit put \(B_r(t)=S(t)(Z_r(t)-1)\) and \(H_r(t)=\int_0^t B_r(s)\,ds\). Conditional on no intervening reset, the scaled age increases deterministically; conditional on a reset, its future law no longer depends on the old age. Together with stationarity this gives \(\mathbb E[Z_r(t)-1\mid Z_r(s)]=e^{-r(t-s)}(Z_r(s)-1)\) for \(t\ge s\). Thus \(\mathbb E[B_r(t)B_r(s)]=e^{-(r+2\lambda)|t-s|}\) and \(\mathbb E H_r(t)^2\le 2T/(r+2\lambda)\) on \([0,T]\). On a grid of \(n\) equal intervals, the squared maximum of grid values of \(H_r\) is bounded by the sum of their squares. On each interval, the squared increment from the left endpoint is at most \((T/n)\int_{\mathrm{interval}} B_r(s)^2\,ds\); the maximum of these bounds is at most their sum. Hence
\[
\mathbb E\sup_{[0,T]}|H_r|^2\le \frac{4nT}{r+2\lambda}+\frac{2T^2}{n}.
\]
Taking \(n=\max(1,\lfloor\sqrt r\rfloor)\) gives convergence to zero. The squared \(L^2\) supremum of the integrated error \(\int_0^t(Y_r-SZ_r)\,ds\) is at most \(T^2(\sqrt{24\lambda/r}+\sqrt{6}L/r)^2\) by Cauchy–Schwarz and stationarity. Adding the two errors proves the path limit. Symmetry and \(L^2\) convergence give convergence of the variances; that of the integrated sign is \(2\int_0^T (T-u)e^{-2\lambda u}\,du=T/\lambda-(1-e^{-2\lambda T})/(2\lambda^2)\).

## Verification and linear benchmark

The unchanged companion `verify.py` (Python and NumPy) provides finite event-driven numerical tests for \(\tan v\) and \(\tanh v\) at \(r=20,80\). The theorem is analytic; these simulations do not prove any limit. For linear drag \(g(v)=\kappa v\), \(\kappa>0\), stationarity of the generator on \(VS,V^2\) gives \(C=\mathbb E[VS]=\Sigma/(r+\kappa+2\lambda)\) and \(Q=\mathbb E[V^2]=2\Sigma C/(r+2\kappa)\). The velocity covariance \(c(t)\) solves \(c'(t)=\Sigma C e^{-2\lambda t}-(r+\kappa)c(t)\) with \(c(0)=Q\). Integrating yields \(D_r=\int_0^\infty c(t)\,dt=(Q+\Sigma C/(2\lambda))/(r+\kappa)\), so \(r^2D_r/\Sigma^2\to 1/(2\lambda)\). This is a comparison, not a new long-time formula or an interchange of finite-horizon and large-time limits for nonlinear drag.

## Relationship to prior work and limitations

Howlader, Mondal and Das ([arXiv:2606.00560](https://arxiv.org/abs/2606.00560), Eqs. (1)–(5), stationary density and transport results) treat the same protocol and find cusp-like velocity densities and the \(r^{-2}\) effective diffusivity scaling numerically. Olsen and Löwen ([arXiv:2401.12685](https://arxiv.org/abs/2401.12685), Eqs. (1)–(7), (55)) give general renewal-based partial reset transport formulas. These studies motivate the problem but do not state the simultaneous limits proved here for a retained telegraph driver. The [nonlinear-drag diffusivity record](https://github.com/Resultary/2026/tree/main/2026/11/8/SCOPE-the-first-nonlinear-drag-fingerprint-of-diffusion-under-velocity--a93c21e7816d), proof §§1–3, uses the same stationary backward-age representation, gives the linear benchmark, and proves a nonlinear large-\(r\) expansion for the long-time Green–Kubo coefficient. Its observable is long-time diffusivity, not a separated-time velocity law or a finite-horizon path limit. The contribution here is the quantitative velocity law, joint marking, and integrated path limit, not the protocol, the age representation alone, or the diffusion exponent. This comparison does not establish historical priority. Resetting the sign, taking \(\lambda\) to scale with \(r\), nonsmooth friction, and arbitrary nonstationary initial laws are outside the stated theorem.
