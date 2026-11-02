# A sharp longitudinal anticorrelation threshold for a completely reset active Brownian particle

## Finding

A confined active Brownian particle with simultaneous Poisson resetting of position and absolute heading can display *negative stationary longitudinal position autocovariance*, although its transverse autocovariance is strictly positive at every finite lag. The longitudinal autocovariance has at most one positive zero for **all** positive physical parameters. When trap relaxation is no slower than rotational diffusion, its sign reversal begins at a unique reset rate determined by a cubic equation, independent of translational diffusivity and propulsion speed. At equality of trap and angular relaxation rates the threshold is explicitly \(r_c=(3+\sqrt{13})a/2\); on the anticorrelated side the covariance has a resonant \(h e^{-(r+a)h}\) contribution.

More precisely, define \(p=r/(r+a)\), \(q=(r+2a)/(r+4a)\), and \(s=2a/(r+4a)\). Put
\[
 m=\frac{vp}{k+r},\quad H=\frac{vq}{k+a+r},\quad G=\frac{vs}{k+a+r},\quad J=H-mp,
\]
\[
 V_x=\frac{2D+2vH}{2k+r}-m^2,\qquad
 V_y=\frac{2D+2vG}{2k+r},
\]
and, for \(h\geq0\),
\[
 \Phi(h)=\begin{cases}
 \dfrac{e^{-(r+a)h}-e^{-(r+k)h}}{k-a},&k\ne a,\\[4pt]
 h e^{-(r+k)h},& k=a.
 \end{cases}
\]
For the unique stationary process, its time-lagged connected coordinate autocovariances are *exactly*
\[
 \boxed{C_x(h)=V_x e^{-(r+k)h}+vJ\Phi(h),\qquad
 C_y(h)=V_y e^{-(r+k)h}+vG\Phi(h)>0.}
\]
The strict inequality for \(C_y\) holds at every finite \(h\geq0\); the stationary cross-coordinate covariance vanishes at every lag by reflection symmetry. The longitudinal sign is governed by
\[
 J=-\frac{va\,P(r)}{(r+a)^2(r+4a)(r+k)(r+k+a)},
 \quad P(r)=r^3-ar^2-(2a^2+5ak)r-2a^2k.
\]
The cubic \(P\) has exactly one positive root \(r_c\). For \(r\le r_c\), \(C_x(h)>0\) for every finite \(h\ge0\). For \(r>r_c\), the complete classification is:

- If \(k\ge a\), \(C_x\) has exactly one positive zero and is strictly negative at every larger lag.
- If \(0<k<a\), it has exactly one positive zero precisely when \(v|J|>(a-k)V_x\). At equality or when this inequality fails, \(C_x(h)>0\) at all finite nonnegative lags.

If the zero exists, its exact value is
\[
 h_0=\begin{cases}
 \dfrac{1}{k-a}\log\!\left(1+\dfrac{(k-a)V_x}{v|J|}\right),&k>a,\\[5pt]
 \dfrac{V_x}{v|J|},&k=a,\\[5pt]
 -\dfrac{1}{a-k}\log\!\left(1-\dfrac{(a-k)V_x}{v|J|}\right),&k<a.
 \end{cases}
\]
Thus at the onset \(r\downarrow r_c\) from above, the first negative-covariance lag diverges logarithmically for \(k>a\), but inversely linearly for \(k=a\). For \(k<a\) and positive translational diffusion, anticorrelation may occur only at intermediate reset rates and disappear again under very rapid resetting. This reentrance is demonstrated by the exact rational example in Verification below.

## Assumptions and scope

Let \(k,a,r,v,D\) be arbitrary strictly positive real numbers. Between resets, the two-dimensional overdamped particle follows
\[
 dX_t=(-kX_t+v\cos\Theta_t)\,dt+\sqrt{2D}\,dB^x_t,\quad
 dY_t=(-kY_t+v\sin\Theta_t)\,dt+\sqrt{2D}\,dB^y_t,
\]
\[
 d\Theta_t=\sqrt{2a}\,dB^\theta_t\pmod{2\pi},
\]
with three mutually independent standard Brownian motions. At the points of an independent Poisson process of rate \(r\), all three degrees of freedom are reset simultaneously and instantaneously to \((X,Y,\Theta)=(0,0,0)\). The equations are interpreted in the Itô sense. Stationary time covariance means
\[
 C_x(h)=\mathbb E[(X_0-\mathbb E X_0)(X_h-\mathbb E X_h)],\quad
 C_y(h)=\mathbb E[Y_0Y_h],\quad h\ge0.
\]
The reset origin and selected absolute heading define the longitudinal and transverse axes. Rates are expressed in consistent physical inverse-time units; \(D\) has units length squared per time, \(v\) length per time. No joint limit of parameters and observation lag is implicit.

## Proof

**1. Invariant law and angular moments.** The process is a Poisson regenerative process: the independent backward age from the most recent reset has density \(r e^{-rt}\), and the entire within-cycle evolution is independent of earlier cycles. A stationary version is obtained by concatenating two-sided Poisson cycles. Uniqueness follows by coupling at the first common reset. Its first two spatial moments are finite because the harmonic force damps displacements and the reset age has exponential tails. For every integer harmonic \(n\ge1\), the stationary generator acting on \(\cos(n\Theta)\) gives \(\mathbb E\cos(n\Theta)=r/(r+n^2 a)\). Consequently
\[
 \mathbb E\cos\Theta=p,\qquad
 \mathbb E\cos^2\Theta=q,\qquad
 \mathbb E\sin^2\Theta=s,\qquad \mathbb E\sin\Theta=0.
\]

**2. Stationary coordinate moments.** The reset generator has action
\[
 \mathcal L X=-(k+r)X+v\cos\Theta,\quad
 \mathcal L(X\cos\Theta)=-(k+a+r)X\cos\Theta+v\cos^2\Theta,
\]
\[
 \mathcal L(Y\sin\Theta)=-(k+a+r)Y\sin\Theta+v\sin^2\Theta,
\]
\[
 \mathcal L X^2=-(2k+r)X^2+2vX\cos\Theta+2D,
\]
with the analogous identity for \(Y^2\). Taking stationary expectations yields exactly \(\mathbb E X=m\), \(\mathbb E(X\cos\Theta)=H\), \(\mathbb E(Y\sin\Theta)=G\), \(\operatorname{Var}(X)=V_x\), and \(\operatorname{Var}(Y)=V_y\). Here \(V_x>0\) and \(V_y>0\) by \(D>0\). The same formulas are also obtained by integrating the no-reset moments against the exponential stationary reset age.

**3. Two-time regression.** Conditional on the initial state, the Markov generator closes the conditional expectations of the orientation harmonics and the coordinates. After centering at the stationary means,
\[
 \mathbb E[X_h-m\mid X_0,Y_0,\Theta_0]
 =e^{-(k+r)h}(X_0-m)+v\Phi(h)(\cos\Theta_0-p),
\]
\[
 \mathbb E[Y_h\mid X_0,Y_0,\Theta_0]
 =e^{-(k+r)h}Y_0+v\Phi(h)\sin\Theta_0.
\]
Multiply respectively by \(X_0-m\) and \(Y_0\), then average over the stationary law. This proves both asserted covariance formulas. Symmetry under \((Y,\Theta)\mapsto(-Y,-\Theta)\) forces cross-coordinate covariances to vanish. Since \(G>0\), \(V_y>0\), and \(\Phi(h)\ge0\), the transverse autocovariance is strictly positive.

**4. Cubic sign certificate.** Substituting the angular moments and the stationary mean into \(J=H-mp\), taking a common denominator, yields the displayed identity \(J=-vaP(r)/Q\), where \(Q=(r+a)^2(r+4a)(r+k)(r+k+a)>0\). The coefficient signs of \(P\), ordered by descending powers, are \(+,-,-,-\). Descartes' rule of signs gives at most one positive zero, and continuity with \(P(0)<0\), \(P(r)\to+\infty\) gives at least one. Its positive zero is simple, as the unique positive root lies after the only positive critical point and the polynomial is increasing there. At \(k=a\), factorization gives \(P(r)=(r+2a)(r^2-3ar-a^2)\), yielding the stated exact threshold.

**5. All-lag sign classification.** Write
\[
 C_x(h)=e^{-(r+k)h}\bigl[V_x+vJf(h)\bigr],\qquad
 f(h)=\begin{cases}(e^{(k-a)h}-1)/(k-a),&k\ne a,\\h,&k=a.\end{cases}
\]
The function \(f\) starts at zero and is strictly increasing, since \(f'(h)=e^{(k-a)h}>0\). Its upper limit is infinite if \(k\ge a\), and \(1/(a-k)\) if \(k<a\). Therefore \(J\ge0\) gives strict positivity. If \(J<0\), the bracket strictly decreases and crosses zero at most once; it crosses exactly under the two stated inequalities. Directly solving the bracket equation gives the three explicit zero formulas. Because \(J\) vanishes linearly at \(r_c\), the exact zero formulas give logarithmic divergence of \(h_0\) for \(k>a\) and reciprocal divergence for \(k=a\).

**6. Thermal reentrance at weaker confinement.** When \(k<a\), the slow-mode coefficient is \(A=V_x+vJ/(a-k)\). For fixed \(k,a,v,D>0\), its large-rate expansion is
\[
 A=\frac{2D}{2k+r}-\frac{v^2k}{(a-k)r^2}+O(r^{-3}),\qquad r\to\infty.
\]
Hence \(A>0\) for all sufficiently large \(r\) if \(D>0\), whereas the active contribution alone is eventually negative. The exact rational example below exhibits strict positivity, negativity, and restored positivity at three increasing rates, proving a genuine reentrant regime rather than inferring it from a numerical plot.

## Verification

A standalone `check.py` uses exact rational arithmetic for 90 positive-parameter triples, verifies the cubic numerator identity and all positive stationary variances, tests exact finite-lag sign-crossing formulas in resonant and nonresonant regimes, and independently samples stationary paths using exponentially distributed reset ages and direct Brownian orientation increments. All checks passed in the present reproduction. The simulation is a finite-step diagnostic, **not** the proof of the sign theorem or of a limit.

As an exact reentrant certificate, take \(k=1/2\), \(a=v=1\), and \(D=1/200\). The sign of the slow longitudinal mode \(A=V_x+vJ/(a-k)\) at rates \(r=1,10,100\) is determined without rounding:
\[
 A(1)=\frac{101}{360}>0,\qquad
 A(10)=-\frac{15457}{11157300}<0,\qquad
 A(100)=\frac{11218439}{1076844213900}>0.
\]
Thus at \(r=10\) the autocovariance has exactly one positive zero (approximately \(h_0=3.5925910052\) in these units), whereas at \(r=1\) and \(r=100\) it stays positive for all finite lags. For the independent resonant example \(k=a=v=1\), the critical rate is \(r_c=(3+\sqrt{13})/2\), and the autocovariance changes sign precisely at \(h_0=V_x/(v|J|)\) when \(r>r_c\).

The embedded checker may be run from its own containing directory with `python check.py`, using Python 3 and NumPy. It does not require external paper files, hidden state, or external services. For direct analytic reproduction, substituting the displayed test parameters into the formulas is sufficient.

## Relationship to prior work

Shee (arXiv:2409.06920v1, first public 2024-09-11), sections 2–4 and Appendix D, derives the complete-reset harmonic-trap model and one-time longitudinal displacement moments, including its stationary variance. That prior result is credited; it does **not** report stationary two-time longitudinal and transverse position autocovariances or the sharp single-zero/anticorrelation phase boundary. Kumar, Sadekar and Basu (arXiv:2008.03294v1) examine joint position-orientation resetting without harmonic confinement and focus on one-time marginal distributions. Chaudhuri and Dhar (arXiv:2005.14234v1) give moment recursion and trapping crossovers in the absence of resetting. Standard Markov semigroup regression readily supplies the analytic *method*, and some displayed coefficients are reconstructible from prior one-time moments. The specific sign-changing connected two-time observable, the unique positive root criterion, the transverse positivity contrast, the resonant onset and the thermal reentrance require the additional calculations here. General regenerative-covariance identities constitute a residual broader-coverage/prior-art risk; this is not a proof of publication novelty.

## Limitations

This is a stationary single-particle theorem for full simultaneous Poisson resetting to one fixed absolute heading and position. Partial or random-heading resets, nonharmonic traps, angular drift/chirality, non-Poisson renewal protocols, and interactions are not covered. A negative covariance at a positive lag is not a negative variance, negative diffusivity, or a thermodynamic phase transition. The exact sign boundaries concern expectations; the negative tail can be exponentially small and difficult to estimate experimentally. The theorem does not claim a closed stationary density, general inference guarantees, or a unique connected reentrant rate interval for every \(k<a\). Independent scientific and publication-priority auditing has not been performed.

## References

1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920v1 (2024-09-11), https://arxiv.org/html/2409.06920v1 .
2. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294v1 (2020-08-07), https://arxiv.org/html/2008.03294v1 .
3. D. Chaudhuri and A. Dhar, *Active Brownian particle in harmonic trap: exact computation of moments, and re-entrant transition*, arXiv:2005.14234v1 (2020-05-28), https://arxiv.org/abs/2005.14234 .
