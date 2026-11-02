# A complete one-crossing phase diagram for a fourth-order time arrow in a resetting Brownian bath

## Finding
For a unit-relaxation harmonic coordinate driven by an independently Brownian bath that is reset to zero at rate \(\rho>0\), the fourth-order chronological asymmetry
\[
 A_\rho(t)=\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3],\qquad t>0,
\]
has the following **complete sign classification**. Let \(\rho_*=(3+\sqrt{33})/4\).

* If \(0<\rho\le1\), then \(A_\rho(t)<0\) at **every** positive lag.
* If \(1<\rho<\rho_*\), there exists **exactly one** \(t_0(\rho)\in(0,\infty)\): \(A_\rho(t)<0\) for \(0<t<t_0\), \(A_\rho(t_0)=0\), and \(A_\rho(t)>0\) for \(t>t_0\).
* If \(\rho\ge\rho_*\), then \(A_\rho(t)>0\) at **every** positive lag.

Thus the only possible lag-induced sign reversal is a single negative-to-positive crossing. Both boundary cases \(\rho=1\) and \(\rho=\rho_*\) are included, with strict signs for every \(t>0\). The exact Laplace transform and the existence of at least one crossing within the intermediate parameter regime were previously established; the new conclusion is the **global all-lag sign diagram and the uniqueness of its crossing**.

## Assumptions and scope
The stationary Markov process \((X_t,Y_t)\), with \(t\in\mathbb R\), evolves between reset epochs by
\[
 dX_t=(-X_t+Y_t)\,dt,\qquad dY_t=\sqrt{2}\,dW_t,
\]
with independent homogeneous Poisson resets of rate \(\rho>0\) sending \(Y_t\mapsto0\) while leaving \(X_t\) continuous. Brownian motion and the Poisson process are independent. Take the unique stationary law obtained from the bi-infinite driving system. Its required fourth moments are finite: the time since the previous reset is exponentially distributed, giving finite polynomial moments for \(Y\), and \(X\) is a stable exponential filter of \(Y\). All expectations are stationary and over both noises. The result concerns this normalized model and the specified unequal two-time fourth moments, not a universal time-reversal observable for every active process.

## Proof
**1. Exact finite-generator expression.** For a polynomial \(f\), the generator is
\[
 \mathcal Lf=(-x+y)\partial_x f+\partial_{yy}f
       +\rho\,[f(x,0)-f(x,y)].
\]
Its action closes on polynomials of bounded degree. Solving \(\mathbb E[\mathcal Lx^iy^j]=0\) through degree four and applying the degree-three/one resolvent gives the exact previously known transform (also independently reproduced by the accompanying checker):
\[
 \int_0^\infty e^{-st} A_\rho(t)\,dt
 =\frac{K_\rho Q_\rho(s)}{(s+\rho)^2(s+1)(s+3)(s+\rho+1)(s+\rho+2)},
 \quad s>0,
\]
where \(K_\rho=24/[\rho(\rho+1)^2(\rho+2)(\rho+3)]>0\), and
\[
\begin{aligned}
Q_\rho(s)={}&(6\rho^2-9\rho-9)s^2\\
 &+(17\rho^3-\rho^2-45\rho-27)s\\
 &+14\rho^4+23\rho^3-21\rho^2-42\rho-18.
\end{aligned}
\]
This established transform is an input to the following new **global sign argument**, rather than the novelty claim.

**2. Extract the signed core.** Define \(g_\rho\) as the inverse Laplace transform of \(Q_\rho(s)/[(s+\rho)^2(s+1)]\). For \(\rho\ne1\), partial fractions give
\[
\begin{aligned}
 g_\rho(t)&=a_\rho e^{-t}+(b_\rho+c_\rho t)e^{-\rho t},\\
 a_\rho&=\frac{2\rho(\rho+1)(7\rho+3)}{\rho-1},\\
 b_\rho&=-\frac{8\rho^3+35\rho^2+6\rho-9}{\rho-1},\\
 c_\rho&=-3(\rho+1)(\rho+2)(\rho+3).
\end{aligned}
\]
The removable singularity at \(\rho=1\) has the explicit value \(g_1(t)=-(12+32t)e^{-t}<0\). Put \(h_\rho(t)=e^{\rho t}g_\rho(t)\) when \(\rho\ne1\). Then
\[
\begin{aligned}
 h_\rho(0)&=3(2\rho^2-3\rho-3),\\
 h'_\rho(0)&=(\rho+1)(11\rho^2-9\rho-18),\\
 h''_\rho(t)&=a_\rho(\rho-1)^2e^{(\rho-1)t}.
\end{aligned}
\]
If \(0<\rho<1\), all three displayed quantities are strictly negative; as \(h'_\rho\) keeps decreasing, \(h_\rho(t)<0\) for \(t\ge0\). For \(\rho\ge\rho_*\), \(h_\rho(0)\ge0\), \(h'_\rho(0)>0\) and \(h''_\rho(t)>0\); hence \(g_\rho(t)>0\) for \(t>0\). If \(1<\rho<\rho_*\), then \(h_\rho(0)<0\), \(h''_\rho(t)>0\), and \(h_\rho(t)\to+\infty\) because \(a_\rho>0\) and \(\rho-1>0\). A strictly convex function beginning negative with strictly increasing derivative and diverging to positive infinity can cross zero exactly once, from negative to positive. Thus this is the complete sign pattern of \(g_\rho\).

**3. Three strictly positive exponential filters preserve the one-crossing bound.** The remaining resolvent factors are positive-time exponential kernels:
\[
 A_\rho=K_\rho\,g_\rho*e^{-3t}*e^{-(\rho+1)t}*e^{-(\rho+2)t},
\]
where convolution is on \([0,\infty)\). If a continuous function \(f\) is initially negative and has at most one negative-to-positive sign change, write \(F(t)=\int_0^t e^{-\lambda(t-u)}f(u)\,du\) for \(\lambda>0\). Since
\[
 \frac{d}{dt}\bigl(e^{\lambda t}F(t)\bigr)=e^{\lambda t}f(t),
\]
\(e^{\lambda t}F(t)\) decreases strictly while \(f<0\) and increases strictly after \(f\) becomes positive. As \(F\) starts at zero and is immediately negative, it has **at most one** zero at positive time and can change sign only from negative to positive. Repeating for the three kernels shows \(A_\rho\) has **at most one** positive zero in the intermediate regime. Fixed signs of \(g_\rho\) yield strict fixed signs of \(A_\rho\) in the other regimes.

**4. The intermediate crossing really occurs.** When \(1<\rho<\rho_*\), the core has the positive slow tail \(g_\rho(t)\sim a_\rho e^{-t}\) with \(a_\rho>0\), while the three subsequent filters decay at rates \(3\), \(\rho+1\), and \(\rho+2\), all strictly exceeding one. Therefore the final convolution has the positive tail
\[
 A_\rho(t)\sim \frac{K_\rho a_\rho}{(3-1)(\rho+1-1)(\rho+2-1)}e^{-t}
 =\frac{24(7\rho+3)}{\rho(\rho-1)(\rho+1)^2(\rho+2)(\rho+3)}e^{-t}>0.
\]
The initial convolution is strictly negative before the first core sign switch; the uniqueness argument therefore supplies exactly one finite positive zero. This completes all three regimes, including their endpoints.

## Verification
The companion Python file `verify.py` reconstructs stationary degree-two/four moments from the generator, obtains the degree-three/one polynomial-semigroup resolvent independently, verifies the rational transform, partial fractions, endpoint identities, and asymptotic residues symbolically, and compares direct matrix exponentials with three consecutively integrated convolution filters at 35 parameter/lag pairs. All 35 comparisons and eight additional sign samples passed. For \(\rho=1.5\), direct evaluation gives \(A_\rho(1)\approx-0.021306965280\) and \(A_\rho(3)\approx0.025443791234\), consistent with a unique zero. These finite numerical tests are not used to infer uniqueness; the positive-convolution sign argument proves it for every \(\rho,t\) in scope. Reproduce with `python verify.py` using Python, SymPy, NumPy and SciPy.

## Relationship to prior work
Guéneau, Majumdar and Schehr's 2023 harmonic resetting-bath paper supplies the motivating model and stationary-moment methodology. An earlier exact quartic-lag analysis of this same model (claim identifier `2d5b968b-afd9-4686-ad3d-5e3c13527f07`) already established the complete Laplace transform used here, the short- and long-lag signs, and the **existence** of a lag reversal for \(1<\rho<\rho_*\), explicitly leaving its uniqueness unasserted. That transform and the existence statement are not claimed as new. The present result closes the previously unresolved global lag-sign problem by a signed-core reduction and a threefold positive-convolution argument; in particular it proves **uniqueness** inside the inversion interval and **absence of any reversals** outside it. General variation-diminishing principles for positive exponential kernels are established mathematics, not a novel abstract lemma. Work on irreversibility in Gaussian active Ornstein–Uhlenbeck models and resetting statistics concerns different noise mechanisms or observables and does not give this exact model-wide zero-count classification.

## Limitations
The result is confined to a Poisson-reset Brownian bath, unit harmonic relaxation, and this particular fourth-order two-time asymmetry. It does not bound a statistical estimator's finite-sample error, establish the full pathwise entropy-production rate, or extend to non-Poissonian resetting. It uses an earlier exact transform: a sufficiently general, unidentified previous sign-variation or complete spectral theorem might subsume the new qualitative classification. The comparison of prior mathematics is best-knowledge and independent publication-priority certification has not been performed. This is not a claim of independent validation.

## References
1. Guéneau, Majumdar, Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453 (first publicly available 2023-06-15), https://arxiv.org/abs/2306.09453.
2. Mori, Majumdar, Schehr, *Time to reach the maximum for a stationary stochastic process*, arXiv:2207.12329, https://arxiv.org/abs/2207.12329. Different time-irreversibility diagnostic.
3. Dabelow, Eichhorn, *Irreversibility in Active Matter: General Framework for Active Ornstein-Uhlenbeck Particles*, Frontiers in Physics 8 (2021), doi:10.3389/fphy.2020.582992. Gaussian active-bath comparison.
4. Earlier exact quartic-lag analysis of this model, claim identifier `2d5b968b-afd9-4686-ad3d-5e3c13527f07` (prior recoverable research record). Its transform and lag-crossing existence were known; zero-count uniqueness was explicitly not claimed.
