# Endpoint laws for the stationary radius of partially reset three-dimensional Brownian motion

## Finding
Let \(0<c<1\), let \(R\) follow a three-dimensional Bessel process between the events of an independent rate-\(c\) Poisson process, and set \(R\mapsto cR\) at every event. Write \(\pi_c\) for its stationary distribution. The exact small-radius coefficient is
\[
K(c)=\lim_{r\downarrow0}\frac{\pi_c((0,r))}{r^3}
=\frac{2(2c)^{3/2}}{3\pi}\int_0^\infty t^2\prod_{j=0}^\infty (1+c^{2j}t^2)^{-1}\,dt.
\]
It is finite and strictly positive for every \(c\in(0,1)\), and obeys the two sharp endpoint limits
\[
\boxed{\lim_{c\downarrow0}\frac{K(c)}{\sqrt c}=\frac{2\sqrt2}{3},\qquad
\lim_{c\uparrow1}\frac{K(c)}{(1-c)^{3/2}}=\frac4{3\sqrt\pi}.}
\]
Consequently \(K\) is continuous, vanishes at both parameter endpoints, and attains a strictly positive global maximum at at least one interior contraction factor. The cubic fixed-parameter law disagrees with the super-polynomial small-radius assertion for this particular conditioned Bessel process in Lemma 12 of Kolb--Wübker (2026). The original contributions claimed here are the **sharp two-parameter endpoint asymptotics of the coefficient** and their resulting interior-maximum law, rather than fixed-parameter existence or smoothness of the invariant density.

## Assumptions and scope
Brownian motion has generator \(\frac12\Delta\) in \(\mathbb R^3\). The reset clock is independent, with rate equal to the contraction parameter \(c\). This special rate is exactly the rate appearing in Proposition 10 of Kolb--Wübker for the positive-conditioning transform of the rate-one partially reset one-dimensional Brownian motion. The reset acts on the spatial position, not on elapsed time or Brownian path history. All limits in the cubic law are taken with \(c\) fixed before \(r\downarrow0\); the endpoint limits then concern its coefficient \(K(c)\). No joint \(r,c\)-scaling statement is asserted.

## Proof
**Radial lift and invariant law.** Consider a three-dimensional vector process \(Y\) driven by standard Brownian increments and the same rate-\(c\) Poisson clock, with resets \(Y\mapsto cY\). Rotational invariance and the radial Markov property show that \(|Y|\) has the prescribed Bessel-with-reset semigroup. The usual squared-radius generator is \(\frac12(f''+2f'/r)\) between resets; the radial jump is \(r\mapsto cr\). Two vector trajectories with identical driving Brownian motion and reset epochs have separation \(c^{N_t}(Y_0-Y'_0)\), where \(N_t\) counts resets, and the separation tends to zero almost surely, which yields uniqueness of the invariant probability law by coupling from any finite starting points.

Let \(E_0,E_1,\ldots\) be independent exponential variables of rate \(c\); let \(B^{(j)}\) be independent standard three-dimensional Brownian motions, also independent of the \(E_j\). The stationary vector, read backward across Poisson intervals, has the almost surely and \(L^1\)-convergent representation
\[
Y_\infty\ \stackrel d=\ \sum_{j=0}^\infty c^j B^{(j)}_{E_j}.
\]
This uses a **vector sum before taking its norm**: the stationary radius is \(|Y_\infty|\), not the sum of the successive radial lengths. Convergence follows from \(\mathbb E|B^{(j)}_{E_j}|<\infty\) and geometric weights. Independent increments over backward Poisson intervals prove invariance; synchronous contraction proves uniqueness. For a single term, integrating the Gaussian Fourier transform over an exponential time gives
\[
\mathbb Ee^{i\langle\xi,B_E\rangle}=\frac{c}{c+|\xi|^2/2}.
\]
Independence therefore yields
\[
\varphi_c(\xi)=\mathbb Ee^{i\langle\xi,Y_\infty\rangle}
=\prod_{j=0}^\infty\left(1+\frac{c^{2j}|\xi|^2}{2c}\right)^{-1}.
\]
The first two factors give \(\varphi_c\in L^1(\mathbb R^3)\) for every fixed \(c>0\), and every factor is positive. Fourier inversion gives a continuous radial density \(f_c\) with
\[
f_c(0)=\frac1{(2\pi)^3}\int_{\mathbb R^3}\varphi_c(\xi)\,d\xi>0.
\]
The mass of a vanishing centered ball is its volume times \(f_c(0)\) up to a relative \(o(1)\). Using spherical coordinates and \(\xi=\sqrt{2c}\,t\theta\) gives the displayed integral formula for \(K(c)=\frac{4\pi}{3}f_c(0)\). In particular \(\pi_c((0,r))\sim K(c)r^3\).

**Strong-contraction boundary.** Define the integral \(I(c)=\int_0^\infty t^2\prod_{j\ge0}(1+c^{2j}t^2)^{-1}\,dt\). With \(s=ct\),
\[
cI(c)=\int_0^\infty \frac{s^2}{s^2+c^2}\frac1{1+s^2}
\prod_{k=1}^\infty(1+c^{2k}s^2)^{-1}\,ds.
\]
For every \(s>0\) the integrand tends to \((1+s^2)^{-1}\) as \(c\downarrow0\), and is bounded above by this integrable function. Dominated convergence gives \(cI(c)\to\pi/2\). Substituting this in \(K(c)=2(2c)^{3/2}I(c)/(3\pi)\) gives \(K(c)/\sqrt c\to2\sqrt2/3\).

**Weak-contraction boundary.** Put \(\delta=1-c^2\) and \(\sigma_c^2=1/[c(1-c^2)]\); this is the variance of any coordinate of \(Y_\infty\). The characteristic function of \(Y_\infty/\sigma_c\) is
\[
\psi_c(\xi)=\prod_{j=0}^\infty\left(1+\frac{\delta c^{2j}}2|\xi|^2\right)^{-1}.
\]
Since \(\sum_{j\ge0}\delta c^{2j}=1\) and \(\sum_{j\ge0}\delta^2c^{4j}=\delta/(1+c^2)\to0\), taking logarithms shows \(\psi_c(\xi)\to e^{-|\xi|^2/2}\) for each fixed \(\xi\).

This convergence is also in \(L^1(\mathbb R^3)\). Indeed, for \(c\in[0.9,1)\), take the first \(N=\lceil4/\delta\rceil\) factors. For all their indices \(j\), \(c^{2j}\ge e^{-6}\), so
\[
0<\psi_c(\xi)\le\left(1+\frac{e^{-6}\delta}2|\xi|^2\right)^{-4/\delta}
\le\left(1+\frac{e^{-6}}2|\xi|^2\right)^{-4},
\]
where the last inequality follows from Bernoulli's inequality. The last bound is integrable in \(\mathbb R^3\). Fourier inversion and dominated convergence thus imply that the normalized density at zero tends to \((2\pi)^{-3/2}\). Rescaling back gives
\[
K(c)\sim\frac{4\pi}{3}(2\pi)^{-3/2}[c(1-c^2)]^{3/2}
\sim\frac4{3\sqrt\pi}(1-c)^{3/2}.
\]
Finally continuity of \(K\) on \((0,1)\) follows by dominated convergence on compact subintervals applied to its positive product integral. The two endpoint limits prove that its continuous extension to \([0,1]\) is zero at both endpoints and positive inside, hence it has a positive interior maximum.

## Verification
A standalone numerical checker evaluates the convergent Fourier integral and compares its two endpoint normalizations, checks the stationary second moment, and checks a finite-product characteristic-function identity. In particular, the generator at \(f(r)=r^2\) gives \(\mathbb E_{\pi_c}R^2=3/[c(1-c^2)]\). For the scalar sum of independent \(\mathrm{Gamma}(2,\sqrt{2c})\) lengths asserted in Corollary 11 of Kolb--Wübker, the second moment would instead be
\[
\frac1{c(1-c^2)}+\frac2{c(1-c)^2},
\]
which exceeds the required moment by \(4/[(1-c)^2(1+c)]>0\). This supplies a separate exact algebraic cross-check that vector increments cannot be replaced by independent radial lengths. The analytic proof, not finite quadrature, establishes the limits.

## Relationship to prior work
Kolb and Wübker (2026), Proposition 10, identify the positive-conditioned partially reset Brownian motion with a three-dimensional Bessel process reset at rate \(c\). Their Corollary 11 proposes an additive Erlang representation for the invariant radial law and Lemma 12 derives super-polynomial suppression near the origin. The moment identity above rules out that radial-sum representation, while the actual invariant radius has the cubic small-ball law.

Grzywny, Palmowski, Szczypkowski and Trojan (arXiv:2412.15626, first public December 20, 2024), Theorem A and Proposition 2.22, already establish stationary density existence and smoothness for multidimensional Brownian motion under partial resetting. The present result does **not** claim those foundational facts or the fixed-\(c\) cubic exponent as new. It evaluates the **sharp moving-parameter endpoint laws** for the conditioned Bessel setting in which the reset intensity equals its contraction factor, which the inspected fixed-parameter density and space-time asymptotics do not report. The general density formulas provide context and a route to the integral expression, but do not by themselves state the two constants in the nonuniform parameter limits.

## Limitations
No uniqueness of the maximizing contraction factor is shown. No joint asymptotic in \(r\) and \(c\), no higher-order endpoint expansion, and no reassessment of subsequent quasistationary conclusions in the motivating work is claimed. Independent priority verification has not been performed; a general parameter-uniform stationary-density theorem outside the inspected literature could subsume the endpoint limits. All endpoint estimates are for the specific conditioning-induced clock rate \(c\); changing the reset intensity changes their constants and scales.

## References
1. T. Grzywny, Z. Palmowski, K. Szczypkowski and B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626 (first public December 20, 2024); Annals of Applied Probability 36 (2026), 1110–1177.
2. M. Kolb and A. Wübker, *Brownian Motion With Partial Resetting Conditioned to Stay Positive*, Bulletin of the London Mathematical Society 58 (2026), e70314, DOI:10.1112/blms.70314 (first public March 5, 2026).
3. M. Biroli, Y. Feld, A. K. Hartmann, S. N. Majumdar and G. Schehr, *Resetting by rescaling: exact results for a diffusing particle in one-dimension*, Physical Review E 110 (2024), 044142 (one-dimensional comparison).
