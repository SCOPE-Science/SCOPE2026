# Reentrant time-average uncertainty in a harmonically confined run-and-tumble particle with resetting

## Finding

A harmonically confined run-and-tumble particle whose position and velocity sign are fully renewed by an independent Poisson clock can have **two distinct positive-rate extrema** of the long-time variance of its empirical time-averaged position. A precise phase boundary separates the reentrant regime from an at-most-one-extremum regime. The reentrance is possible if and only if the dimensionless tumbling parameter \(g=2\gamma/k\) is below the universal constant \(g_c=1.09692461304432\ldots\), defined as the positive root of \(g^4+2g^3+g^2-3g-2=0\). This is a claim about *temporal estimation noise*, not about the positional one-time stationary variance or fourth moment.

## Assumptions and scope

Fix \(k>0\), \(v>0\), \(\gamma>0\), and reset intensity \(r>0\). Between resets, a real coordinate satisfies \(\dot X_t=-kX_t+v\sigma_t\), where \(\sigma_t\in\{-1,+1\}\) flips at independent rate \(\gamma\). At each point of a rate-\(r\) Poisson process, replace \(X_t\) by an independent draw \(Y\) with \(\mathbb EY=0\), \(0<s_Y^2=\mathbb EY^2<\infty\), and replace \(\sigma_t\) by an independent fair sign; these variables and all clocks are independent. Both coordinates reset. The regeneration cycles define a unique stationary process with finite second moment. Let \(C_r(t)=\mathbb E[X_0X_t]\) in stationarity, and define the asymptotic variance of the empirical mean by

\[
\mathcal V(r)=\lim_{T\to\infty}T\operatorname{Var}\!\left(\frac1T\int_0^T X_t\,dt\right)=2\int_0^\infty C_r(t)\,dt.
\]

The covariance is exponentially integrable, so the displayed limit exists. The extension to \(r=0\) is the stationary unreset process in its harmonic trap, not a reset cycle. Write \(x=r/k>0\), \(g=2\gamma/k>0\), \(S=k^2s_Y^2/v^2>0\). We classify *all* interior extrema as a function of \(x\) for each fixed \(g,S\), and exhibit a nontrivial reentrant interval.

## Proof

**(1) Exact temporal variance.** The stationary generator on polynomials gives

\[
\mathbb E[X\sigma]=\frac{v}{r+k+2\gamma},\qquad
\mathbb E[X^2]=\frac{r s_Y^2+2v\mathbb E[X\sigma]}{r+2k},\qquad \mathbb EX=0.
\]

Condition on no reset up to time \(t\). Trajectories after the first reset are centered and independent of the initial position, so their cross-correlation vanishes. The Markov evolution before reset therefore gives the exact covariance

\[
C_r(t)=e^{-(r+k)t}\mathbb E[X^2]
+v\mathbb E[X\sigma]\int_0^t e^{-(r+k)(t-u)}e^{-(r+2\gamma)u}\,du.
\]

Integrating each nonnegative term over \(t\ge0\), then substituting the stationary moments, yields

\[
\boxed{\mathcal I(r):=\int_0^\infty C_r(t)\,dt
=\frac{r s_Y^2}{(r+k)(r+2k)}+
\frac{v^2(3r+4\gamma+2k)}{(r+k)(r+2k)(r+2\gamma)(r+k+2\gamma)}.}
\]

Alternatively the independent regeneration cycles give the same formula using the variance-rate renewal-reward identity \(\mathcal V(r)=r\mathbb E[(\int_0^{T_r}X_t\,dt)^2]\), for exponential cycle length \(T_r\sim\operatorname{Exp}(r)\). This identity and the displayed covariance formula agree symbolically in the independent checker. Scaling leaves

\[
H_{g,S}(x):=\frac{k^3}{v^2}\mathcal I(kx)
=S\frac{x}{(x+1)(x+2)}+
\frac{3x+2g+2}{(x+1)(x+2)(x+g)(x+g+1)}.
\]

In particular \(H_{g,S}(0)=1/g\) and \(H_{g,S}(x)\to0\) as \(x\to\infty\).

**(2) Derivative reduction.** Put

\[
\begin{aligned}
P_g(x)={}&9x^4+(20g+32)x^3+(15g^2+57g+39)x^2\\
&+(4g^3+32g^2+48g+20)x+(6g^3+14g^2+12g+4),\\
R_g(x)={}&\frac{P_g(x)}{(x+g)^2(x+g+1)^2(2-x^2)},\quad 0\le x<\sqrt2.
\end{aligned}
\]

Every coefficient of \(P_g\) is strictly positive. Differentiation (checked by exact symbolic cancellation) yields

\[
H'_{g,S}(x)=\frac{(2-x^2)[S-R_g(x)]}{(x+1)^2(x+2)^2}
\quad (0\le x<\sqrt2).
\]

For \(x\ge\sqrt2\), both the reset-position contribution and the active-motion contribution have strictly negative derivatives, so \(H'_{g,S}(x)<0\) there. The number and type of extrema therefore reduce to the intersections of the horizontal line \(S\) with \(R_g\) on \((0,\sqrt2)\).

**(3) A single trough in the auxiliary curve.** Another exact differentiation gives

\[
R'_g(x)=\frac{2(x+1)(x+2)Q_g(x)}{(x+g)^3(x+g+1)^3(2-x^2)^2},
\]

where

\[
\begin{aligned}
Q_g(x)={}&9x^5+(30g+21)x^4+(41g^2+57g+13)x^3\\
&+6(g+1)(5g^2+5g-1)x^2\\
&+6(g+1)(2g^3+3g^2-2)x\\
&+2(g+1)(g^4+2g^3+g^2-3g-2).
\end{aligned}
\]

The quartic \(q(g)=g^4+2g^3+g^2-3g-2\) has one positive root by Descartes' sign rule, with \(1<g_c<6/5\), and its sign is negative below and positive above that root. The only coefficients of \(Q_g\) whose signs can change are its constant, linear, and quadratic coefficients. Their positive sign-change thresholds occur in strictly increasing order: \(5g^2+5g-1=0\) has its root in \((0,1/5)\), \(2g^3+3g^2-2=0\) in \((3/5,4/5)\), and \(q(g)=0\) in \((1,6/5)\). Thus, for \(0<g<g_c\), its coefficient sequence, from constant to highest power, has **exactly one** negative-to-positive sign change. The leading coefficient is positive and its constant coefficient is negative; Descartes' rule therefore gives exactly one positive zero, \(x_*(g)\). Since \(R_g(x)\to+\infty\) as \(x\uparrow\sqrt2\) while its initial derivative is negative, the zero lies in \((0,\sqrt2)\). The curve \(R_g\) decreases strictly to \(x_*\), then increases strictly to infinity. For \(g\ge g_c\), every coefficient of \(Q_g\) is nonnegative and each coefficient of positive degree is strictly positive, so \(R_g\) increases strictly for \(x>0\).

Set \(S_0(g)=R_g(0)=(3g^2+4g+2)/[g^2(g+1)]\); for \(0<g<g_c\) set \(S_*(g)=R_g(x_*(g))\), where \(0<S_*<S_0\). From the derivative sign, for \(0<g<g_c\) and \(S_*<S<S_0\), there are exactly two positive-rate extrema: first a strict local minimum at the lower intersection, then a strict local maximum at the higher intersection. If \(S>S_0\) there is one strict maximum; if \(S\le S_*\) there is none (at equality a stationary horizontal inflection). At \(S=S_0\), the derivative vanishes at the excluded zero-rate endpoint and one interior maximum remains. When \(g\ge g_c\), there is exactly one interior maximum if \(S>S_0\), and none if \(S\le S_0\). This completes the classification.

**(4) An exact reversal past the baseline.** At \(g=1/2\) and \(S=11\), direct rational evaluation yields

\[
R_{1/2}(0)=\frac{38}{3}>11>\frac{513}{56}=R_{1/2}(1/2),
\qquad H_{1/2,11}(0)=2<\frac{31}{15}=H_{1/2,11}(1/2).
\]

The derivative is initially negative but is positive at \(x=1/2\), and eventually strictly negative. Hence the time-average variance first decreases below the no-reset value, rises past it, and later decreases toward zero. A symmetric two-point reset law \(Y\in\{-\sqrt{11}v/k,+\sqrt{11}v/k\}\) with equal probabilities realizes these parameters, with \(\gamma=k/4\); the result does not rely on Gaussian resetting.

## Verification

`checker.py` uses exact SymPy polynomial simplification to verify the generator/regeneration identity, scaled Green–Kubo expression, first-derivative and second-derivative factorizations, and all rational witness inequalities. It also integrates the stationary time covariance independently at 45-digit precision. Run `python checker.py` after installing `sympy` and `mpmath` as declared in `requirements.txt`. The included `checker_output.txt` is a record of one actual successful execution. The symbolic identities support algebraic consistency; the coefficient-sign and renewal arguments above establish the mathematical theorem. No finite simulation is used as a substitute for the global phase proof.

## Relationship to prior work

Olsen, *Steady-state moments under resetting to a distribution* (arXiv:2310.04840v1, initially public 2023-10-07), treats the same active-harmonic resetting model and derives single-time stationary moments and their dependence on the resetting distribution (including variance/kurtosis behavior). Those stationary moment results and the model are antecedents, not claimed to be new here. The new observable is the asymptotic variance of an empirical time average, whose Green–Kubo time-integral depends on temporal correlations and has a distinct two-extremum phase diagram. Guéneau, Majumdar and Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables* (arXiv:2306.09453v1), analyze a related but different reset rule in which driving noise is reset while position remains continuous. General generator and regenerative identities are standard mathematical ingredients, not new claims.

## Limitations

The result assumes full simultaneous resetting of position and velocity sign, independent Poisson reset times, an independent centered reset-position distribution with finite **positive** variance, and strictly positive harmonic relaxation and tumble rates. It concerns the stationary long-time time-average variance, not full temporal spectra, large deviations, finite-sample uncertainty, or interacting particle systems. No claim is made that an equivalent specialized phase criterion is absent from all literature; independent scholarly priority assessment has not been performed. Numerical root digits are descriptive; uniqueness is established analytically by coefficient signs.

## References

1. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840v1 (2023-10-07), https://arxiv.org/abs/2310.04840 .
2. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453v1 (2023), https://arxiv.org/abs/2306.09453 .
3. Standard stationary Markov-generator and regenerative-reward identities are reproduced and derived in the proof above.
