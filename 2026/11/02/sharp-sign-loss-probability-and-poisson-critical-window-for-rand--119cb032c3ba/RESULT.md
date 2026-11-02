# Sharp sign-loss probability and Poisson critical window for randomized SDIRK

## Finding

For the randomized two-stage singly diagonally implicit Runge--Kutta (SDIRK) scheme specified below, scalar-decay endpoint positivity undergoes a **three-regime sharp transition**. With normalized timestep \(r>0\), the probability of a negative one-step multiplier is

\[
p(r)=\begin{cases}
0,&0<r\le2,\\
1-\dfrac{2}{r}+\sqrt{2-\dfrac4r},&2<r<1+\sqrt3,\\
1,&r\ge1+\sqrt3.
\end{cases}
\]

The transition starts with a square-root cusp, \(p(2+\delta)\sim\sqrt\delta\), as \(\delta\downarrow0\). Across \(N\) independent steps at the near-critical scale \(r_N=2+c/N^2\) with fixed \(c\ge0\), the number of sign reversals converges to a Poisson law of mean \(\sqrt c\). This gives a sharp \(N^{-2}\) critical window for positivity failure along an entire trajectory.

## Assumptions and scope

Let \(\lambda>0\), \(h>0\), \(r=\lambda h\), and \(y_0>0\). Apply the following two-stage method to \(y'=-\lambda y\) in exact real arithmetic, drawing fresh independent \(X_n\sim\mathrm{Uniform}[1/2,1]\) at every timestep:

\[
\begin{array}{c|cc}
X_n&X_n&0\\
1-X_n&1-2X_n&X_n\\\hline
&1/2&1/2
\end{array}.
\]

The distribution is continuous; zero multipliers are null-probability events. Write \(B_N\) for the number of strictly negative one-step multipliers in the first \(N\) updates. If \(p=p(r)\), the exact finite-trajectory laws, valid for every integer \(N\ge1\), are

\[
B_N\sim\operatorname{Binomial}(N,p),\qquad
\Pr(y_N>0)=\frac{1+(1-2p)^N}{2},\qquad
\Pr(y_j>0\text{ for all }0\le j\le N)=(1-p)^N.
\]

For every fixed \(c\ge0\), using the triangular array of independent samples with \(r_N=2+c/N^2\) yields

\[
B_N\Rightarrow\operatorname{Poisson}(\sqrt c),\qquad
\Pr(y_j>0\;\forall\,0\le j\le N)\longrightarrow e^{-\sqrt c},\qquad
\Pr(y_N>0)\longrightarrow\frac{1+e^{-2\sqrt c}}2.
\]

This regime varies the timestep with the number of *repeated steps*; it is not a fixed-final-time vanishing-step convergence result.

## Proof

For a deterministic tableau parameter \(x\in[1/2,1]\), solve the two scalar stage equations using the initial value normalized to one. The stage values divided by \(-\lambda\) are

\[
Y_1=\frac1{1+xr},\qquad
Y_2=\frac{1-r(1-2x)Y_1}{1+xr}.
\]

Thus the one-step multiplier is

\[
R_x(-r)=1-\frac r2(Y_1+Y_2)
=\frac{q_r(x)}{2(1+rx)^2},\qquad
q_r(x)=2+(4x-2)r+(2x^2-4x+1)r^2.
\]

The denominator is strictly positive. As a quadratic in \(x\), \(q_r\) is strictly convex for \(r>0\), with

\[
q_r(1/2)=2-r^2/2,\quad q_r(1)=2+2r-r^2,\quad
\frac{\partial q_r}{\partial x}=4r\bigl(1+r(x-1)\bigr).
\]

For \(0<r\le2\), this derivative is nonnegative throughout \([1/2,1]\) and \(q_r(1/2)\ge0\); at \(r=2\) equality is attained only at the endpoint \(x=1/2\). Hence \(p(r)=0\) in that range. If \(r>2\), the discriminant as a quadratic in \(x\) is \(8r^3(r-2)\), and the roots are

\[
x_\pm(r)=1-\frac1r\pm\sqrt{\frac{r-2}{2r}}.
\]

For all \(r>2\), \(x_-(r)<1/2\): indeed, \(\sqrt{2(r-2)/r}>(r-2)/r\). The other root satisfies \(1/2<x_+(r)<1\) exactly when \(2<r<1+\sqrt3\), since \(q_r(1)>0\) is equivalent to \(r<1+\sqrt3\). The quadratic is negative precisely for sampled \(x\in[1/2,x_+(r))\). Uniform sampling on an interval of length \(1/2\) gives

\[
p(r)=2\bigl(x_+(r)-1/2\bigr)
=1-\frac2r+\sqrt{2-\frac4r}.
\]

For \(r\ge1+\sqrt3\), both endpoint values of the convex quadratic are nonpositive, so its values on the interval are strictly negative except possibly at \(x=1\); hence \(p(r)=1\). The formula is continuous at both thresholds. In the middle regime its derivative is strictly positive:

\[
p'(r)=\frac2{r^2}+\frac2{r^2\sqrt{2-4/r}}>0.
\]

Expanding at \(r=2+\delta\) gives \(p(2+\delta)=\sqrt\delta+O(\delta)\). Since the multipliers depend on independent draws and are almost surely nonzero, their signs are independent Bernoulli trials. This proves the binomial reversal count and the finite-trajectory formulas (using the even-parity binomial identity).

Under \(r_N=2+c/N^2\), one has \(Np(r_N)\to\sqrt c\) and \(p(r_N)\to0\). The binomial Poisson limit proves the claimed count law. The two positivity limits follow directly from \((1-p(r_N))^N\to e^{-\sqrt c}\) and \((1-2p(r_N))^N\to e^{-2\sqrt c}\). More generally, if \(\delta_N\downarrow0\), then \(Np(2+\delta_N)\sim N\sqrt{\delta_N}\); thus a nondegenerate finite limit arises precisely on the \(N^{-2}\) scale.

For completeness, a related exact mean-multiplier identity is

\[
\mathbb E R_X(-r)=2-\frac1{1+r}+4\log\!\left(\frac{r+2}{2(r+1)}\right).
\]

Its derivative is \(-(3r+2)/[(r+1)^2(r+2)]<0\), so its sign has a unique transition at \(r\approx2.2132783420\). This expectation statement follows by elementary integration of the same rational multiplier and is not needed for the sign-reversal/Poisson law.

## Verification

Run `python verify.py` with Python 3.10+ and SymPy 1.10+. It reconstructs the rational stability multiplier directly from the tableau, checks exact rational stage solutions, checks root/discriminant and mean-multiplier identities symbolically, compares positivity probabilities with deterministic node integration, and performs seeded Monte Carlo sign tests. On the reviewed package the script printed:

`PASS: 1041 stage/probability/critical-window checks, and 12 symbolic assertions.`

`Mean multiplier sign-crossing: 2.21327834201749`

The mathematical proof above, not the finite checks, establishes the universal formulas and weak limit.

## Relationship to prior work

Eisenmann, Jans, Kruse and Podhaisky (2026) give the randomized tableau, independent sampling assumption, stability function, samplewise algebraic/A-stability and root-mean-square convergence. Their relevant Sections 3, 5 and 7 do not analyze the probability of a negative scalar multiplier, the sign-count distribution, or the \(N^{-2}\) Poisson critical window. The present result addresses these *positivity* questions, not A-stability or convergence rates. Ketcheson, Higueras and Kocsis (2015/2018) develop absolute-monotonicity/SSP theory for different numerical positivity questions; its threshold coefficients do not provide the present probability law for a uniformly random SDIRK tableau. Bochacik and Przybyłowicz (2024/2025) study a different randomized implicit RK family and stochastic stability regions; only their accessible abstract was compared, leaving a residual literature-access limitation.

## Limitations

The theorem concerns the exact scalar negative-real-axis test problem with positive initial value, independent continuous uniform tableau parameters, and a constant normalized step within each trajectory. A-stability is not the same as preservation of a positive cone. The theorem neither classifies positivity on systems or nonlinear equations nor identifies a general strong-stability-preserving radius. The critical window is a long-trajectory asymptotic, not a consistency or convergence limit at fixed physical time. No exhaustive historical-priority determination or independent verification is asserted.

## References

1. M. Eisenmann, M. Jans, R. Kruse, H. Podhaisky, *Error Bound and Stability Analysis for a Randomized Singly Diagonally Implicit Runge--Kutta Method*, arXiv:2607.18928v1, first submitted 2026-07-21. https://arxiv.org/abs/2607.18928
2. I. Higueras, D. I. Ketcheson, T. A. Kocsis, *Optimal monotonicity-preserving perturbations of a given Runge--Kutta method*, arXiv:1505.04024, J. Sci. Comput. 76 (2018), 1337--1369. https://arxiv.org/abs/1505.04024
3. T. Bochacik, P. Przybyłowicz, *Convergence and stability of randomized implicit two-stage Runge--Kutta schemes*, arXiv:2404.19059v1, 2024; subsequent journal version with Ł. Stępień, BIT Numer. Math. 65 (2025), article 7. https://arxiv.org/abs/2404.19059
