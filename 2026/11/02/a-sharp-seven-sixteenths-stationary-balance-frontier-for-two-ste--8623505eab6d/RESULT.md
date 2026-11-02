# A sharp seven-sixteenths stationary-balance frontier for two-step probability-simplex preservation

## Finding
Consider the optimized, second-order, A-stable two-step family with prescribed stiff-decay factor \(\kappa\in[0,1)\) introduced by Jensen, Ketcheson and Lóczi [1, Eq. (25)]. Applied with constant timestep to an irreducible two-state continuous-time Markov generator, the family preserves the probability simplex for **every positive timestep and every independent pair of probability-vector histories** if and only if
\[
\boxed{\frac13\le\kappa\le\frac1{\sqrt{1-m}}-1,\qquad
m=\frac{\min(a,b)}{a+b}.}
\]
Here \(a,b>0\) are the chain's two transition rates and \(m\in(0,1/2]\) is its smaller stationary probability. Consequently, **some member of the family** is unconditionally probability-simplex preserving for this chain if and only if
\[
\boxed{m\ge\frac7{16},\quad\text{equivalently}\quad \frac{\max(a,b)}{\min(a,b)}\le\frac97.}
\]
At the sharp stationary-balance boundary \(m=7/16\), the only admissible parameter is \(\kappa=1/3\). In the symmetric chain \(m=1/2\), all and only \(1/3\le\kappa\le\sqrt2-1\) qualify. These assertions include equality at both parameter endpoints, and apply to every finite \(h>0\).

## Assumptions and scope
All computations are in exact arithmetic. Work with row probability vectors \(\mu=(x,1-x)\) and the time-homogeneous irreducible generator
\[
Q=\begin{pmatrix}-a&a\\b&-b\end{pmatrix},\qquad a,b>0.
\]
Let \(\gamma=a+b\), \(t=h\gamma\), and let \(\pi=(b/\gamma,a/\gamma)\) be the stationary row vector. Relabel the states so that the first stationary coordinate is \(m=\min(a,b)/\gamma\); this has no effect on the assertion. We require each of the two starting rows \(\mu_0,\mu_1\) to be a probability vector, but **do not** impose that they lie on a trajectory obtained from a prescribed starter. The condition concerns each update for arbitrary such histories; by induction it also guarantees every subsequent update remains a probability vector. It does not claim positivity for arbitrary unnormalized nonnegative histories, or for general Markov chains with three or more states.

For \(0\le\kappa<1\), set \(D=(3-\kappa)(1+\kappa)\) and use the source's constant-step coefficients
\[
\begin{aligned}
c_0&=\frac{3\kappa-1}{3-\kappa}, &c_1&=\frac{4(1-\kappa)}{3-\kappa},\\
\beta_0&=\frac{2\kappa^2}{D}, &\beta_1&=\frac{4\kappa}{D}, &\beta_2&=\frac2D.
\end{aligned}
\]
Thus \(c_0+c_1=1\), \(\beta_j\ge0\), and \(\beta_2>0\). The formula under study is
\[
\mu_{n+2}(I-h\beta_2Q)
=\mu_{n+1}(c_1I+h\beta_1Q)
+\mu_n(c_0I+h\beta_0Q).
\]
This is the source's optimized family written with \(c_j=-\alpha_j\), not a newly proposed integration method.

## Proof
**1. Reduction to one scalar coordinate.** Put \(P=\mathbf1\pi\), the rank-one stochastic stationary projector. Since \(Q=-\gamma(I-P)\) and \(\beta_2>0\), the implicit matrix \(I-h\beta_2Q\) is invertible for every \(h>0\), acts as the identity on the stationary direction, and acts by multiplication by \(1+t\beta_2\) on the centered direction. The two previous states can be written \(\mu_{n+1}=(u,1-u)\), \(\mu_n=(v,1-v)\), with \(u,v\in[0,1]\). Their successor is \((x_t,1-x_t)\) because \(Q\mathbf1=0\) and \(c_0+c_1=1\). Direct projection onto the centered subspace gives
\[
x_t=m+\frac{c_1-t\beta_1}{1+t\beta_2}(u-m)
+\frac{c_0-t\beta_0}{1+t\beta_2}(v-m).
\]
Since \(\beta_1/\beta_2=2\kappa\) and \(\beta_0/\beta_2=\kappa^2\), this is the **exact interpolation identity**
\[
\boxed{x_t=\frac{x_0+t\beta_2x_\infty}{1+t\beta_2},\quad
x_0=c_1u+c_0v,\quad
x_\infty=(1+\kappa)^2m-2\kappa u-\kappa^2v.}
\]
The coefficients of \(x_0\) and \(x_\infty\) are strictly positive and sum to one whenever \(t>0\). Therefore the successor belongs to the simplex for all \(t>0\), \(u,v\in[0,1]\) precisely when **both** limiting affine maps belong to \([0,1]\) for all \(u,v\in[0,1]\): sufficiency follows from interpolation, and necessity follows by taking \(t\downarrow0\) and \(t\to\infty\) at any fixed \(u,v\). The endpoint maps themselves need only be nonnegative; equality cannot invalidate a finite-time convex combination.

**2. Zero-step endpoint.** As \(c_0+c_1=1\) and \(c_1>0\), the affine map \(x_0=c_1u+c_0v\) carries the square into \([0,1]\) if and only if \(c_0\ge0\), namely \(\kappa\ge1/3\). If \(\kappa<1/3\), the histories \(u=0,v=1\) give \(x_0=c_0<0\), hence \(x_t<0\) for all sufficiently small positive \(t\).

**3. Infinite-stiffness endpoint.** For \(\kappa\ge0\), the affine map \(x_\infty\) is nonincreasing in each argument. Thus its minimum and maximum over the history square are
\[
\min x_\infty=1-(1+\kappa)^2(1-m),\qquad
\max x_\infty=(1+\kappa)^2m.
\]
As \(0<m\le1/2\), the minimum is nonnegative if and only if \((1+\kappa)^2(1-m)\le1\); this condition also implies \((1+\kappa)^2m\le1\). Therefore \(x_\infty\) maps the entire square to \([0,1]\) if and only if
\[
\kappa\le(1-m)^{-1/2}-1.
\]
When this inequality fails, the histories \(u=v=1\) give \(x_\infty<0\), so \(x_t<0\) for sufficiently large but finite \(t\). More explicitly, since then \(x_0=1\), any \(t>-1/(\beta_2x_\infty)\) works.

**4. Sharp balance frontier.** Combining the two necessary-and-sufficient conditions proves the parameter interval in the Finding. It is nonempty exactly when \(1/3\le(1-m)^{-1/2}-1\), equivalently \((1-m)\le9/16\), or \(m\ge7/16\). For the stationary masses \(a/(a+b)\), \(b/(a+b)\), the inequality is equivalent to \(\max(a,b)/\min(a,b)\le9/7\). At \(m=1/2\), the upper parameter endpoint is \(\sqrt2-1\). At the lower mass boundary, the endpoints coincide at \(1/3\). This completes the proof, including both failure regimes and all equality boundaries.

## Verification
The standalone `verify.py` uses only Python's standard-library `fractions.Fraction`. It constructs the full implicit two-by-two Markov update by exact matrix inversion, independently evaluates the boxed scalar interpolation identity, and compares them over a rational grid of parameters, step sizes and all four history-square vertices. It additionally checks exact rational boundary instances and finite-time counterexamples on both sides of the sharp parameter interval. Executing `python3 verify.py` yields `PASS: 2637 exact-rational identities, boundary and matrix checks`. The universal assertion comes from the preceding algebraic proof, not from finite sampling.

## Relationship to prior work
Jensen, Ketcheson and Lóczi [1] supply and optimize the underlying A-stable \(L(\kappa)\)-stable family; the method coefficients, order and A-stability are **not new claims here**. The new claim is its complete all-step probability-simplex-invariance classification for two-state Markov generators with arbitrary probability histories, including the exact \(7/16\) stationary-balance barrier. Classical monotonicity-preserving linear multistep analysis [2,3] concerns different families, general-purpose norm/monotonicity hypotheses and/or prescribed starters, and does not state this specific sharp stationary-mass criterion. Related positivity analyses of Runge–Kutta and Crank–Nicolson updates address different numerical maps. The scalar-decay positivity results with a fixed backward-Euler or exact starter for the same family do not imply this theorem: their histories are restricted to a one-dimensional orbit, whereas the present universal quantifier covers the full product of two probability simplices, and the object is a coupled two-state Markov system.

## Limitations
The classification is exact-arithmetic, constant-step, linear, autonomous and two-state. It does not establish SSP bounds for arbitrary nonlinear ODEs, preservation for three or more states, positivity with unnormalized independent histories, or robustness under roundoff. The same mathematical model proof and literature review are not an independent audit. Historical priority remains uncertain, particularly regarding more general implicit-multistep cone invariance criteria that might imply this formula after specialization.

## References
[1] T. Jensen, D. I. Ketcheson, and L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, first public 2026-10-15, Eq. (25), https://arxiv.org/abs/2610.22685.

[2] W. Hundsdorfer, S. J. Ruuth, and R. J. Spiteri, *Monotonicity-preserving linear multistep methods*, CWI report/PDF, https://ir.cwi.nl/pub/4231/04231D.pdf.

[3] L. Lóczi, *Exact optimal values of step-size coefficients for boundedness of linear multistep methods*, 2016, https://arxiv.org/abs/1609.07858.

[4] L. Bonaventura and A. Della Rocca, *Monotonicity, positivity and strong stability of the TR-BDF2 method and of its SSP extensions*, 2015, https://arxiv.org/abs/1510.04303.
