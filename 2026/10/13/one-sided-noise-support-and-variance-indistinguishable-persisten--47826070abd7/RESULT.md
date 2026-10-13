# One-sided noise support and variance-indistinguishable persistence in logistic population maps

## Finding

For the **exact** real-valued additive-noise logistic recursion
\[
X_{n+1}=rX_n(1-X_n)+\varepsilon_n,\qquad r>0,
\]
any i.i.d. real innovation law with finite second moment and unbounded negative support forces
\[
\mathbb P_x\!\left(\lim_{n\to\infty}X_n=-\infty\right)=1
\quad\text{for every finite }x\in\mathbb R.
\]
Consequently, its Markov kernel has no invariant probability measure on the real line. Only a finite second moment and access to arbitrarily large negative shocks are needed; Gaussianity, a density, symmetry and tail-exponential bounds are not needed.

This obstruction is structurally different from a small, bounded innovation: for every \(1<r<3\), a sufficiently weak symmetric two-point law has a positive invariant interval and a unique stationary law on that interval, geometrically attractive in the \(1\)-Wasserstein metric. The distinction persists even at exactly equal innovation means and variances. At \(r=2\), two such laws of variance \(1/256\) are the symmetric two-point law \(\pm 1/16\) and the centered, one-sided unbounded exponential law \((1-E)/16\), with \(E\sim\operatorname{Exp}(1)\). The first supports a stationary positive population on \([3/8,5/8]\); for the second all finite trajectories diverge to negative infinity almost surely.

At these same parameters, both laws feed the same *formal* Gaussian moment-closure equation of Yang and Han (2026), and its feasible equilibrium quartic has at least two roots. This is a precise example in which noise variance does not determine stationary persistence of the underlying process. The statement concerns the exact unmodified recurrence; the approximation's algebraic results are not contradicted.

## Assumptions and scope

The innovation sequence \((\varepsilon_n)_{n\ge0}\) is independent and identically distributed, real-valued and independent of the finite initial state. Write \(v=\mathbb E[\varepsilon_0^2]<\infty\). For the first assertion it is sufficient that
\[
\mathbb P(\varepsilon_0<-T)>0\qquad\text{for every }T>0;
\]
centering is not necessary for the escape proof, but is imposed in the comparison with the motivating ecological model. No reflection, truncation, or absorbing boundary at zero is imposed. In particular, negative states remain mathematically legitimate states of this formal recursion, although not legitimate population sizes.

For the bounded-noise assertion fix any \(1<r<3\), let \(u=1-1/r\), and choose \(h>0\) so small that
\[
0<u-h<u+h<1,\qquad q=|2-r|+2rh<1.
\]
Let \(J=[u-h,u+h]\) and \(0<a\le(1-q)h\). Use independently sampled innovations with probability \(1/2\) at each of \(-a\) and \(+a\).

## Proof

**1. An escape trap with uniform probability of permanent descent.** For all real \(x\),
\[
r x(1-x)=r\!\left(\frac14-(x-\tfrac12)^2\right)\le\frac r4.
\]
Choose \(L>0\) satisfying
\[
L\ge\frac4r,\qquad L^4\ge\frac{128v}{15r^2},
\]
and define the deterministic thresholds
\[
a_0=L,\qquad a_{j+1}=\frac r2a_j^2\quad(j\ge0).
\]
Then \(a_{j+1}\ge2a_j\), hence \(a_j\ge2^jL\) and \(a_j\to\infty\). If \(X_k\le-a_j\), writing \(X_k=-s\) with \(s\ge a_j\) gives
\[
rX_k(1-X_k)=-rs(1+s)\le-r a_j^2.
\]
Thus \(\varepsilon_k\le(r/2)a_j^2\) guarantees \(X_{k+1}\le-a_{j+1}\). Markov's inequality applied to the square of the innovation, followed by a geometric bound, shows
\[
\sum_{j=0}^{\infty}
\mathbb P\!\left(\varepsilon_0>\frac r2a_j^2\right)
\le\sum_{j=0}^{\infty}\frac{4v}{r^2a_j^4}
\le\frac{64v}{15r^2L^4}\le\frac12.
\]
By independence and the union bound, starting below \(-L\), the probability of obeying *all* successive threshold restrictions is at least \(1/2\). On this event the trajectory descends below \(-a_j\) and tends to \(-\infty\).

The one-step shock \(\varepsilon_n\le-L-r/4\) forces \(X_{n+1}\le-L\) regardless of the current real state. Its probability
\[
p_L=\mathbb P(\varepsilon_0\le-L-r/4)>0
\]
is positive by unbounded negative support. Future innovations are independent of this shock. Consequently, for every initial state \(x\),
\[
\mathbb P_x(X_n\to-\infty)\ge p_L/2=:\delta>0.
\]

**2. Upgrading a uniform positive probability to certainty.** Let \(\mathcal F_n\) be the history through time \(n\), and set \(A=\{X_k\to-\infty\}\). The Markov property and tail invariance of this event give
\[
\mathbb P_x(A\mid\mathcal F_n)
=\mathbb P_{X_n}(A)\ge\delta\qquad\text{a.s. for all }n.
\]
As \(n\to\infty\), bounded martingale convergence gives \(\mathbb P_x(A\mid\mathcal F_n)\to\mathbf1_A\) almost surely because \(A\) is measurable with respect to the infinite trajectory. Since \(\mathbf1_A\) cannot equal zero while being at least \(\delta>0\), \(\mathbb P_x(A)=1\).

If an invariant probability \(\pi\) on \(\mathbb R\) existed, start the process with \(X_0\sim\pi\), independently of its future innovations. The preceding result holds after integration over \(\pi\). Thus for each fixed \(B\in\mathbb R\), dominated convergence yields \(\mathbb P_\pi(X_n>B)\to0\). Stationarity would instead make this probability equal to \(\pi((B,\infty))\) at every time. It follows that \(\pi((B,\infty))=0\) for all \(B\), contradicting total mass one.

**3. A positive stationary law for bounded noise.** The deterministic map \(f(x)=rx(1-x)\) fixes \(u=1-1/r\), and on \(J\) its derivative satisfies
\[
\sup_{x\in J}|f'(x)|\le |2-r|+2rh=q<1.
\]
For any \(x\in J\), \(\lvert f(x)-u\rvert\le qh\). Hence adding either \(-a\) or \(+a\) with \(a\le(1-q)h\) leaves the image in \(J\). Moreover, coupling two copies of the recursion with identical innovations contracts their distance by at least the factor \(q\) at each step. The Markov operator on probability measures supported in the compact interval \(J\) is therefore a strict contraction in the complete \(1\)-Wasserstein metric. It has exactly one invariant probability supported in \(J\), and every initial probability supported in \(J\) approaches it geometrically in that metric. All sample paths started in \(J\) remain strictly positive.

**4. Exact matching of the first two innovation moments.** Take \(r=2\), \(J=[3/8,5/8]\), \(a=1/16\), and \(q=1/2\). On \(J\) the deterministic map lies in \([15/32,1/2]\); adding symmetric \(\pm1/16\) yields an interval contained in \([13/32,9/16]\subset J\). The derivative magnitude on \(J\) is at most \(1/2\). Thus the bounded law supports a unique geometrically attracting stationary probability on \(J\).

For the unbounded law let \(E\sim\operatorname{Exp}(1)\) and set \(\varepsilon=(1-E)/16\). Since \(\mathbb E E=1\) and \(\operatorname{Var}(E)=1\), this law also has mean zero and variance \(1/256\), but is unbounded below. The first part therefore proves its lack of any stationary probability and almost-sure descent to \(-\infty\) from every finite real initial state. More quantitatively, choosing \(L=2\) gives the bound \(1/3840\) on the sum of future trap-failure probabilities, while the one-step forcing event has probability \(p_L=\exp(-41)\). Thus a descent trap can be extremely rare on finite observation horizons, even though the eventual behavior is almost sure.

At \(r=2\) and \(v=1/256\), the Yang--Han Gaussian moment-closure equilibrium polynomial is
\[
Q(m)=16m^4-32m^3+18m^2-3m-\frac1{128}.
\]
Its exact signs are \(Q(1/4)=-9/128\), \(Q(3/8)=7/256\), and \(Q(1/2)=-1/128\). It consequently has at least two zeros in the *formally feasible* interval \((0,1/2)\), by the intermediate value theorem. The polynomial is identical for the two innovation laws because their means and variances coincide. Its roots describe the formal closure, **not** invariant measures of both exact processes.

## Verification

The supplied `verify.py` checks the rational interval inclusions, the uniform derivative bound in the matched-variance example, three exact quartic signs, and the exact rational trap-failure bound. Running `python3 verify.py` prints `VERIFY_OK`. The all-time statements are analytic consequences of the preceding infinite-sequence probability argument; finite rational checks or Monte Carlo experiments do not verify them independently.

## Relationship to prior work

Yang and Han (2026) introduce precisely this additive-noise ecological recurrence and study its Gaussian moment-closure bifurcation. Their closure results are algebraic and conditional on moment relations; the source also interprets finite-time simulations as persistence evidence. The present theorem distinguishes stationary distributions of the exact Markov chain from equilibria of that formal closure. It does not reassert their quartic as a new fact.

Bassols-Cornudella and Lamb (2023) explicitly note that a Gaussian-driven random logistic map tends to negative infinity almost surely, while modest bounded perturbations allow bounded attractors. Thus the **Gaussian escape phenomenon and the broad bounded-versus-Gaussian contrast are prior knowledge**. The increment here is the all-growth-rate, distribution-free *one-sided negative-support criterion* under only a second-moment hypothesis, together with the explicit same-variance non-Gaussian stationary/escaping pair tied to the 2026 closure polynomial. Gutiérrez, Iglesias and Rodríguez (1993) address dichotomous noise and invariant densities, but not the stated one-sided unbounded-tail hypothesis. Castro and collaborators (2023) treat a distinct multiplicative random logistic map with absorption.

## Limitations

The conclusion for the unbounded-noise law is divergence to **negative** infinity of a formal real-valued recursion, not a biologically meaningful negative population trajectory. The claim does not apply to truncated-at-zero, reflected, absorbed, or density-dependent-noise models. Bounded-noise stationary-law uniqueness is asserted on the constructed invariant interval only, not among all probability measures on the full real line. The result does not infer the actual stationary distribution from the Gaussian moment closure, and it does not assert that every bounded-support innovation admits persistence. The exponentially rare shock in the example may lie far beyond practical simulation horizons. Existing Gaussian escape literature substantially predates this result; broader unindexed distribution-free statements might limit the originality of its generalization.

## References

1. Y. Yang and X. Han, “Equilibrium and bifurcation analysis of a stochastic logistic difference equation with additive noise,” *Discrete and Continuous Dynamical Systems - S*, early access 2026-05-18, DOI: 10.3934/dcdss.2026151.
2. B. Bassols-Cornudella and J. S. W. Lamb, “Noise-induced chaos: A conditioned random dynamics perspective,” *Chaos* **33** (2023), 121102, DOI: 10.1063/5.0175466; preprint arXiv:2308.07116.
3. J. M. Gutiérrez, A. Iglesias and M. A. Rodríguez, “Logistic map driven by dichotomous noise,” *Physical Review E* **48** (1993), 2507–2513, DOI: 10.1103/PhysRevE.48.2507.
4. M. M. Castro, V. P. H. Goverse, J. S. W. Lamb and M. Rasmussen, “On the quasi-ergodicity of absorbing Markov chains with unbounded transition densities, including random logistic maps with escape,” *Ergodic Theory and Dynamical Systems* **44** (2024), 1818–1855, arXiv:2209.01281, DOI: 10.1017/etds.2023.69 (distinct multiplicative-noise model).
