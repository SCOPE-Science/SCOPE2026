# Infinite variance at mean-optimal Poisson resetting for an exponentially distributed fixed target

## Finding

A target distance is sampled **once**, not resampled on resetting. For a one-dimensional Brownian searcher with diffusivity \(D>0\), resetting to the origin at homogeneous Poisson rate \(r>0\), and absorbing target distance \(R\sim\operatorname{Exp}(\lambda)\), \(\lambda>0\), define \(q=\sqrt{r/D}\) and \(z=q/\lambda\). Let \(T\) be the time of the first target encounter, including all failed search attempts and resets. For every integer \(m\ge1\),

\[
\mathbb E[T^m]<\infty\quad\Longleftrightarrow\quad m q<\lambda.
\]

The exact first two moments, on their respective finite domains, are

\[
\mathbb E T=\frac{q}{r(\lambda-q)},\quad 0<z<1,
\qquad
\mathbb E T^2=\frac{\lambda^2q}{r^2(\lambda-q)^2(\lambda-2q)},\quad 0<z<\tfrac12.
\]

Consequently the squared coefficient of variation is

\[
\operatorname{CV}(T)^2=\frac{1}{z(1-2z)}-1,\qquad 0<z<\tfrac12.
\]

The unique finite-mean minimizing reset rate is \(r_{\mathrm{mean}}=D\lambda^2/4\), where \(z=1/2\), \(\mathbb ET=4/(D\lambda^2)\), but \(\mathbb ET^2=\infty\). In contrast, the unique coefficient-of-variation minimum on the finite-variance interval is at \(r_{\mathrm{CV}}=D\lambda^2/16=r_{\mathrm{mean}}/4\), where \(\operatorname{CV}(T)^2=7\) and \(\mathbb ET=16/(3D\lambda^2)\), just \(4/3\) times the minimum mean. The interval \(D\lambda^2/4\le r<D\lambda^2\) has finite mean but infinite variance.

## Assumptions and scope

The particle evolves as \(dX_t=\sqrt{2D}\,dB_t\) between instantaneous resets to \(0\), and the independent resets form a Poisson process of rate \(r>0\). Initially \(X_0=0\); a strictly positive distance \(R\) is sampled from density \(\lambda e^{-\lambda R}\) independently of particle and reset noise. The target remains at that sampled location for the entire trajectory. Hitting the target is absorbing. Expectations average over **both** the quenched choice of target and the conditional search histories. At each fixed target distance all positive integer passage-time moments are finite, but this does not imply their integrability against an unbounded target-distance distribution.

## Proof

**1. Conditional first-passage transform.** For a fixed distance \(R>0\), write \(\tau_R\) for the first Brownian hit without resetting. Its Laplace transform is \(\phi_R(s)=\mathbb E e^{-s\tau_R}=\exp[-R\sqrt{s/D}]\). A first-attempt decomposition against an independent exponential reset clock gives, for \(s\ge0\),

\[
F_R(s)=\mathbb E[e^{-sT}\mid R]
=\frac{(r+s)\phi_R(r+s)}{s+r\phi_R(r+s)}.
\]

This is because successful first attempts contribute \(\phi_R(r+s)\), and resetting before target encounter contributes \(r[1-\phi_R(r+s)]/(r+s)\) times a fresh conditional copy of the passage transform. The displayed formula follows by solving the resulting renewal equation.

**2. First two conditional moments.** Differentiate the transform at \(s=0\) (legitimate for every fixed \(R\), where the transform has a nonzero analytic neighborhood of zero). Setting \(q=\sqrt{r/D}\) gives

\[
\mathbb E[T\mid R]=\frac{e^{qR}-1}{r},
\qquad
\mathbb E[T^2\mid R]=\frac{2e^{2qR}-(2+qR)e^{qR}}{r^2}.
\]

Since both conditional moments are nonnegative, Tonelli's theorem permits averaging even when the result diverges. Integration against \(\lambda e^{-\lambda R}\,dR\) yields the announced formulas on \(\lambda>q\) and \(\lambda>2q\), respectively. At and beyond each boundary the corresponding integral diverges: its positive leading term has the growth \(e^{mqR}\), and the lower-order terms cannot cancel it.

**3. General integer-moment boundary.** Put \(u=qR\), \(p=e^{-u}\), and \(Y_R=rpT\). Replacing \(s\) by \(wrp\) in the exact transform yields

\[
\mathbb E[e^{-wY_R}\mid R]
=\frac{(1+wp)\,\exp[-u(\sqrt{1+wp}-1)]}
{w+\exp[-u(\sqrt{1+wp}-1)]}.
\]

As \(R\to\infty\), \(p\to0\) and \(up\to0\). On every fixed complex disk \(\lvert w\rvert\le c<1/2\), both numerator and denominator converge uniformly to \(1\) and \(1+w\), respectively, and the denominator stays bounded away from zero. Thus the conditional transforms converge locally uniformly as analytic functions to \(1/(1+w)\). Cauchy's derivative formula at zero gives, for every fixed integer \(m\ge1\),

\[
\mathbb E[Y_R^m\mid R]\longrightarrow m!,
\quad\text{hence}\quad
\mathbb E[T^m\mid R]\sim m!\,r^{-m}e^{mqR}.
\]

These conditional moments are continuous and bounded on compact intervals of \(R\) by the same transform. Integrating their positive asymptotic exponential growth against the target density proves \(\mathbb E T^m<\infty\) precisely for \(\lambda>mq\), including divergence at equality. This is a moment criterion, not merely an assertion about finitely sampled trajectories.

**4. Competing optimal rates.** In the finite-mean domain \(0<z<1\), substitute \(r=D\lambda^2z^2\) into the first-moment expression to obtain \(\mathbb ET=1/[D\lambda^2z(1-z)]\). The denominator has its unique maximum at \(z=1/2\); the boundary values of the mean diverge. In the finite-variance domain \(0<z<1/2\), division of the exact second moment by the square of the mean gives \(\operatorname{CV}^2=[z(1-2z)]^{-1}-1\). The quadratic \(z(1-2z)\) is uniquely maximal at \(z=1/4\). Direct substitution gives the exact optimal values and their \(4/3\) tradeoff.

## Verification

The accompanying `verification.py` independently differentiates the conditional Laplace transform numerically (nine parameter checks), integrates conditional moments against the exponential distance density (six high-precision quadratures), tests five large-distance higher-moment normalizations, and checks the exact optimum and coefficient-of-variation identities. The program requires Python 3 and `mpmath`. It prints `PASS` on success. Numerical tests corroborate the exact proof; divergence of moments and minimizer uniqueness follow analytically, not from finite quadratures or simulations.

## Relationship to prior work

Evans and Ray [1] study the **same fixed, random target** setting and identify the exponential target distribution conjugate to Poisson resetting, including the mean-first-passage optimum. Their first-passage renewal formalism and mean-optimal protocol are prior results. The mathematical contribution here is the target-averaged **complete positive-integer moment integrability boundary**, explicit second moment, infinite-variance consequence **at** the known mean optimum, and the distinct exact coefficient-of-variation optimum.

Evans and Majumdar [2] study mean optimization for spatially distributed targets and reset locations; their transition in the reset-location optimization is a different phase boundary. García-Valladares and collaborators [3] analyze the first two search-time moments for **two fixed-magnitude, opposite-sign target locations**, with two spatially dependent reset rates. Their divergence occurs in a singular zero-disorder-probability limit of optimized strategies. It is an important conceptual predecessor about mean-versus-variance reliability, but neither its target law nor its resetting model supplies this exponential-distance all-moment theorem. Formula-level consequences of broader regeneration or mixture-integrability results could independently imply portions of the claim; publication priority is not independently certified.

## Limitations

The exact results concern one-dimensional Brownian motion with instantaneous homogeneous Poisson resets and a **single fixed target sampled once** from a one-sided exponential distance law. They do not apply without modification if the target is redrawn after each reset, the reset clock is not Poissonian, resets occur at nonzero travel cost, or targets have different distance tails. Optimization of the coefficient of variation is over **constant positive Poisson rates with finite second moment**, not over arbitrary restart-time protocols. The all-moment criterion concerns integer moments only; fractional moments and exact passage-time survival asymptotics are not claimed. Comparison with an as-yet unidentified general regeneration theorem is an outstanding novelty risk.

## References

[1] M. R. Evans and S. Ray, *Stochastic resetting prevails over sharp restart for broad target distributions*, arXiv:2410.01941 (first version 2024-10-02; revised version consulted 2025-05-19), https://arxiv.org/abs/2410.01941 .

[2] M. R. Evans and S. N. Majumdar, *Diffusion with Optimal Resetting*, arXiv:1107.4225, https://arxiv.org/abs/1107.4225 .

[3] G. García-Valladares, C. A. Plata, A. Prados and A. Manacorda, *Optimal resetting strategies for search processes in heterogeneous environments*, arXiv:2305.14245, https://arxiv.org/abs/2305.14245 .
