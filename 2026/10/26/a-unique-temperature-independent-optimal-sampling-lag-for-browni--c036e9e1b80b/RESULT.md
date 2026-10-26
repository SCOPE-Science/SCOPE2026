# A unique temperature-independent optimal sampling lag for Brownian-gyrator circulation

## Finding

In the stationary two-temperature Brownian gyrator, an oriented area formed from **two exact observations**, separated by a lag \(t>0\), has a unique lag maximizing its single-pair mean-to-standard-deviation ratio. For every coupling \(0<|u|<1\) and distinct positive bath temperatures \(T_x,T_y\), this lag is independent of both temperatures. It depends only on \(v=|u|\) and is the unique positive solution of
\[
 v\coth(vt_*)=\frac{1}{1-e^{-2t_*}}.
\]
Moreover \(t_*(v)\) increases strictly with \(v\), tends to \(0.7968121300\ldots\) as \(v\downarrow0\), and obeys
\[
 t_*(v)=\frac12\log\frac{1}{1-v}+o(1)\qquad(v\uparrow1).
\]
This optimizes a **single stationary two-position chord observable**, not a time-integrated stochastic area, an angular-velocity ratio, or the statistical efficiency of correlated samples along a finite trajectory. The optimal statistical lag is strictly **shorter** than the lag maximizing the unstandardized mean circulation, which is \(t_{\mathrm{mean}}=\operatorname{artanh}(v)/v\); this distinction persists in both small-coupling and near-instability limits.

## Assumptions and scope

Let \(W^x,W^y\) be independent standard Brownian motions, let \(T_x,T_y>0\) be distinct, and let \(-1<u<1\), \(u\ne0\). Consider the unique stationary solution of
\[
 dX_s=(-X_s+uY_s)\,ds+\sqrt{2T_x}\,dW^x_s,\qquad
 dY_s=(-Y_s+uX_s)\,ds+\sqrt{2T_y}\,dW^y_s.
\]
The relaxation rate on each diagonal is normalized to one. For a lag \(t>0\), define the oriented chord area (twice the signed triangle area)
\[
 Q_t=X_0Y_t-Y_0X_t,
 \qquad L_t=Q_t/t,
 \qquad \mathcal R(t)=\frac{|\mathbb E L_t|}{\sqrt{\operatorname{Var}(L_t)}}.
\]
Multiplication by \(1/t\) cancels in \(\mathcal R(t)\). Observations are exact positions on the *continuous-time* stationary diffusion; no Euler discretization is assumed.

Put \(\Delta=T_x-T_y\) and
\[
 d=\det\Sigma=T_xT_y+\frac{u^2(T_x+T_y)^2}{4(1-u^2)}>0,
\]
where \(\Sigma\) is the stationary covariance matrix. For every \(t>0\),
\[
 \boxed{\mathbb E Q_t=\Delta e^{-t}\sinh(ut),\qquad
 \operatorname{Var}(Q_t)=2d(1-e^{-2t})+\Delta^2e^{-2t}\sinh^2(ut).}
\]
In particular,
\[
 \mathcal R(t)^2=\frac{\Delta^2\sinh^2(ut)}{2d(e^{2t}-1)+\Delta^2\sinh^2(ut)}.
\]
The formula and optimum are valid for either sign of the coupling. The strict nonzero-coupling and unequal-temperature hypotheses are necessary for a unique informative maximum: for \(u=0\) or \(T_x=T_y\), the mean signed area vanishes at all lags and \(\mathcal R\equiv0\). The endpoints \(|u|=1\) are excluded because the drift is not asymptotically stable and the stationary covariance does not exist.

## Proof

**1. Stationary covariance and unequal-temperature current.** Set
\[
 A=\begin{pmatrix}-1&u\\u&-1\end{pmatrix},\qquad
 \Sigma=\begin{pmatrix}a&c\\c&b\end{pmatrix}.
\]
The Lyapunov equation \(A\Sigma+\Sigma A+2\operatorname{diag}(T_x,T_y)=0\) gives
\[
 c=\frac{u(T_x+T_y)}{2(1-u^2)},\qquad
 a=T_x+uc,\qquad b=T_y+uc.
\]
Therefore \(a-b=\Delta\), and direct multiplication yields the displayed formula for \(d=ab-c^2\). The conditional mean propagator is
\[
 M_t=e^{At}=e^{-t}\begin{pmatrix}\cosh(ut)&\sinh(ut)\\\sinh(ut)&\cosh(ut)\end{pmatrix}.
\]
The cross-covariance \(C_t=\mathbb E[(X_0,Y_0)^\top(X_t,Y_t)]=\Sigma M_t^\top\) has antisymmetric component
\[
 (C_t)_{12}-(C_t)_{21}=(a-b)e^{-t}\sinh(ut)=\Delta e^{-t}\sinh(ut).
\]
This is precisely \(\mathbb E Q_t\).

**2. Exact finite-lag fluctuations.** For any two jointly centered Gaussian planar vectors \(Z,Z'\), both with covariance \(\Sigma\), and cross-covariance \(C=\mathbb E[ZZ'^\top]\), Wick's identity gives
\[
 \operatorname{Var}(\det[Z,Z'])
 =2(\det\Sigma-\det C)+\big(C_{12}-C_{21}\big)^2.
\]
Indeed expand \(\mathbb E[(Z_1Z'_2-Z_2Z'_1)^2]\), pair the four Gaussian variables in each term, and subtract the squared mean. Since \(\det M_t=e^{-2t}\), we have \(\det C_t=d e^{-2t}\); insertion proves the variance identity above. No independence between the two observations is assumed.

**3. Reduction to one scalar objective.** Because \(d>0\) and \(\Delta\ne0\), maximizing \(\mathcal R^2\) is equivalent to maximizing
\[
 F_v(t)=\frac{\sinh^2(vt)}{e^{2t}-1},\qquad v=|u|\in(0,1).
\]
This reduction removes both temperatures *exactly*, not approximately. The function is positive and continuous on \((0,\infty)\), tends to zero as \(t\downarrow0\) and as \(t\to\infty\), and has logarithmic derivative
\[
 \frac{d}{dt}\log F_v(t)
 =2v\coth(vt)-\frac{2}{1-e^{-2t}}.
\]
Hence critical points are exactly the roots of
\[
 G_v(t):=v\coth(vt)(1-e^{-2t})=1.
\]
The function \(G_v\) tends to \(2\) at zero and \(v<1\) at infinity. Its derivative is
\[
 G'_v(t)=\frac{ve^{-2t}}{\sinh^2(vt)}
 \big[\sinh(2vt)-v(e^{2t}-1)\big]<0.
\]
For the strict inequality, convexity of \(\sinh\) with \(\sinh(0)=0\) gives \(\sinh(2vt)\le v\sinh(2t)\), and \(\sinh(2t)<e^{2t}-1\) for \(t>0\). Thus \(G_v=1\) has exactly one solution, where \(F_v\) changes from strictly increasing to strictly decreasing. It is the unique global optimizer.

**4. Dependence on coupling and endpoint limits.** At every fixed positive \(t\),
\[
 \partial_vG_v(t)=(1-e^{-2t})
 \frac{\tfrac12\sinh(2vt)-vt}{\sinh^2(vt)}>0.
\]
Combined with \(\partial_tG_v<0\), this proves \(t_*(v)\) increases strictly with \(v\). As \(v\downarrow0\), \(G_v(t)\to(1-e^{-2t})/t\), a strictly decreasing function from 2 to 0; its unique level-one solution is the positive root of \(1-e^{-2t}=t\), numerically \(0.7968121300\ldots\).

As \(v\uparrow1\), the roots diverge because \(G_1(t)=1+e^{-2t}>1\) at every fixed finite \(t\). Set \(\varepsilon=1-v\) and \(q=e^{-2t_*(v)}\). Rewriting the root equation using \(\coth(vt)=(1+q^v)/(1-q^v)\) gives the exact identity
\[
 \varepsilon=(1+v)q^v-vq-vq^{v+1}.
\]
Since \(q\downarrow0\) and \(q^v\ge q\), it follows that \(\varepsilon\ge q(1-vq)\); hence \(q\le 2\varepsilon\) eventually. The reverse bound \(\varepsilon\le(1+v)q^v\) gives \(q\ge(\varepsilon/(1+v))^{1/v}\). These two bounds imply \(\varepsilon|\log q|\to0\), so \(q^v/q=q^{-\varepsilon}=1+o(1)\). Dividing the exact identity by \(q\) then yields \(\varepsilon/q\to1\), proving \(t_*=(1/2)\log(1/\varepsilon)+o(1)\).

**5. Comparison with a maximum-mean circulation measurement.** The absolute unstandardized expected chord area is proportional to \(e^{-t}\sinh(vt)\), whose logarithmic derivative is \(v\coth(vt)-1\). Its unique peak lies at \(t_{\mathrm{mean}}=\operatorname{artanh}(v)/v\). At the SNR maximum, \(v\coth(vt_*)=1/(1-e^{-2t_*})>1\). Since \(t\mapsto v\coth(vt)\) decreases strictly, \(t_*<t_{\mathrm{mean}}\). The strict gap tends to \(1-0.7968121300\ldots\) as \(v\downarrow0\) and to \((\log2)/2\) as \(v\uparrow1\), by the expansions already proved and \(\operatorname{artanh}(v)/v=\frac12\log(2/(1-v))+o(1)\). Maximizing signal strength and maximizing its standardized signal-to-noise ratio therefore lead to quantitatively different sampling recommendations.

## Verification

The standalone checker `brownian_gyrator_optimal_checker.py` evaluates the stationary Lyapunov equation with a numerical matrix solver, independently constructs the cross-covariance using matrix exponentials, and evaluates all four Gaussian pairings. It also carries out an independent four-dimensional Gauss-Hermite integration for representative parameters, verifies the scalar optimizer and its monotonicity, and checks the boundary asymptotics. Run with `python brownian_gyrator_optimal_checker.py` in an environment containing Python, NumPy, and SciPy. The checker passed 716 deterministic assertions. Analytic identities and inequalities above, not finite tests, establish the theorem for all parameters.

## Relationship to prior work

Viot, Argun, Volpe, Imparato, Rondoni and Oshanin introduced a detailed discrete-step fluctuation analysis of the Brownian gyrator and explicitly raised the possibility of an optimal discretization interval. Their supplementary construction uses a finite-step **Euler noise update**; it does not establish this unique optimum for **two exact observations of the stationary continuous-time process**, its temperature-independence, or the logarithmic approach to the stability boundary. The ordinary stationary covariance and Gaussian-moment tools are standard antecedents, not claimed new. Du Buisson, Mnyulwa and Touchette analyze the full time-**integrated stochastic area** and its long-time large deviations; this is a different observable and optimization question. Du Buisson and Touchette also provide a general treatment of linear-diffusion time-integrated observables, not the single-chord finite-lag optimization.

## Limitations

The result optimizes only the ratio of the one-chord ensemble mean to its standard deviation. It is **not** a statement about optimum sampling for a fixed total experimental recording time: adjacent chord observations may be statistically dependent. It does not optimize the probability of detecting the correct sign, the Fisher information, the angular velocity with a fluctuating radius denominator, or a discretized numerical integrator. Measurement noise, nonstationary starts, asymmetric drift matrices, inertia, and colored forcing are outside the proved domain. Scholarly priority against any unlocated equivalent result remains open pending independent review.

## References

1. P. Viot, A. Argun, G. Volpe, A. Imparato, L. Rondoni, G. Oshanin, *Destructive effect of fluctuations on the performance of a Brownian gyrator*, arXiv:2307.05248 (first posted 2023-07-11), especially Eq. (1), Sec. 6, and supplementary Eqs. (S11)-(S16).
2. J. du Buisson, T. D. P. Mnyulwa, H. Touchette, *Large deviations of the stochastic area for linear diffusions*, arXiv:2307.06245 (2023), especially the path-integrated observable and Sec. VI.
3. J. du Buisson, H. Touchette, *Dynamical large deviations of linear diffusions*, arXiv:2212.12022 (first posted 2022-12-22).
