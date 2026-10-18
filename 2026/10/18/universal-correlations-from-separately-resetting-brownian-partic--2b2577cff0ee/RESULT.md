# Universal correlations from separately resetting Brownian particles in a common fluctuating environment

## Finding

Consider two otherwise independent Brownian particles, independently returned to zero at a *shared, randomly fluctuating instantaneous rate*, without simultaneous resets. Their stationary displacements are uncorrelated, but their squared displacements have an exact positive correlation. If the distribution of instantaneous rates has a density behaving as \(f(\lambda)\sim c\lambda^{\alpha}\) near zero, with \(c>0\) and \(-1<\alpha<1\), then in the slow-rate-refresh limit their Pearson correlation has the universal value

\[
\boxed{\lim_{\nu\downarrow0}\operatorname{Corr}(X_1^2,X_2^2)
=\frac{1-2^{-\alpha}}{3\alpha}},\qquad \alpha\ne0,
\]

with the continuous value \(\boxed{\log(2)/3}\) at \(\alpha=0\). The limit is independent of the particle diffusivity, the rate density's prefactor, and its behavior away from zero. In particular, an exponentially distributed instantaneous resetting rate gives \(\log(2)/3\approx0.2310490602\), even though each particle has its *own* independently timed resetting events.

For any positive refresh rate \(\nu\), write the following expectations over the instantaneous-rate distribution \(F\):

\[
 A=\mathbb E_F\frac1{\lambda+\nu},\quad B=\mathbb E_F\frac1{2\lambda+\nu},\quad
 A_2=\mathbb E_F\frac1{(\lambda+\nu)^2},\quad
 C=\mathbb E_F\frac1{(\lambda+\nu)(2\lambda+\nu)},
\]
\[
 S=1-\nu A,\qquad R=1-\nu B.
\]

The exact correlation at stationarity is

\[
\boxed{\operatorname{Corr}(X_1^2,X_2^2)
=\frac{2CS/R-A^2}{6A_2-A^2}.}
\]

For nondegenerate \(F\) supported on strictly positive rates it lies strictly between zero and \(1/3\); it is zero for a deterministic positive resetting rate. The ordinary positional covariance always vanishes.

## Assumptions and scope

Fix a diffusion coefficient \(D>0\) and an environment refresh rate \(\nu>0\). The stationary common environment \(\lambda_t\) is piecewise constant: independent exponential waiting times of parameter \(\nu\) separate refreshes, each refresh redraws a rate from the same probability law \(F\) on \((0,\infty)\), and the environment evolves independently of particle motion and particle resets. Given its *entire* environment path, the two resetting point processes are conditionally independent Cox processes with instantaneous intensities \(\lambda_t\). Each particle independently evolves according to Brownian generator \(D\partial_{xx}\) between its own resets and returns to zero when its own reset occurs. The two Brownian noises are independent. A reset of either particle does not reset the environment or the other particle.

All expectation and covariance quantities refer to the joint stationary law of the environment and both particles. For the universality statement, additionally assume \(F\) has a density \(f\) with \(f(\lambda)/(c\lambda^{\alpha})\to1\) as \(\lambda\downarrow0\), for some \(c>0\) and \(-1<\alpha<1\); no assumption about the density away from zero beyond being a probability density is needed. The limit sends the environment refresh rate \(\nu\) to zero *after* choosing the stationary law at each strictly positive \(\nu\). No simultaneous particle resets occur.

## Proof

**Stationary existence and moment finiteness.** Construct the environment on the whole real time axis using a stationary Poisson redraw clock. Conditional on this environment, define each reset process by an independent unit-rate Poisson random measure thinned at intensity \(\lambda_t\), and use independent Brownian increments following its most recent reset. Each process has a last reset almost surely. To verify finite moments, let \(\Phi_q(t)=\mathbb E\exp[-q\int_{-t}^0\lambda_s\,ds]\) for \(q>0\). Conditioning on the first environment refresh yields a renewal equation whose time-integral equals \(A_q/(1-\nu A_q)\), with \(A_q=\mathbb E_F[(\nu+q\lambda)^{-1}]\), and \(0<\nu A_q<1\). Its renewal kernel has an exponential moment for a sufficiently small positive tilt because that strict inequality persists by continuity. Hence \(\Phi_q\) decays at least exponentially and the individual most-recent-reset ages have all polynomial moments; consequently the positional moments used below are finite. This also justifies generator moment identities by truncation and dominated convergence.

**Exact conditional moment equations.** Let \(M=\mathbb E X_i^2\), \(P=\mathbb E X_1^2X_2^2\), and \(H=\mathbb E X_i^4\), and denote their conditional expectations at environmental rate \(\lambda\) by \(m(\lambda)\), \(p(\lambda)\), and \(h(\lambda)\). The generator of the joint process consists of two independent diffusion terms, an independent reset-to-zero term for each particle with rate \(\lambda\), and an environmental redraw operator \(\nu(\mathbb E_F-I)\). Since the stationary rate marginal is \(F\), integrating the stationary joint balance against a bounded function of \(\lambda\) gives, almost everywhere under \(F\),

\[
 (\lambda+\nu)m(\lambda)=2D+\nu M,
\]
\[
 (2\lambda+\nu)p(\lambda)=4D\,m(\lambda)+\nu P,
\]
\[
 (\lambda+\nu)h(\lambda)=12D\,m(\lambda)+\nu H.
\]

The coefficient \(2\lambda\) in the mixed fourth moment is essential: *either* independently timed reset kills the product. By contrast, one reset at a shared event would kill the product at rate \(\lambda\). Integration gives

\[
 M=\frac{2DA}{S},\qquad
 P=\frac{8D^2 C}{SR},\qquad
 H=\frac{24D^2 A_2}{S^2}.
\]

Indeed, solving the first balance gives \(m(\lambda)=2D/[S(\lambda+\nu)]\), which inserted in the other two balances produces the stated values. The squared-displacement covariance is \(P-M^2\), and the common marginal squared-displacement variance is \(H-M^2\); their quotient simplifies to the displayed exact correlation. Conditional sign symmetry also gives \(\mathbb E[X_1X_2]=0\), hence zero positional covariance.

**Strict nonzero dependence and the upper bound.** Conditional on the *whole* environment trajectory, the two particles are independent and identically distributed, and their conditional second moment is

\[
 U(\lambda_{(-\infty,0]})=2D\int_0^\infty
 \exp\left(-\int_{-t}^0\lambda_s\,ds\right)dt.
\]

Thus \(P-M^2=\operatorname{Var}(U)\ge0\). If \(F\) is nondegenerate, vary the current independently sampled rate while fixing the preceding environment and the positive length of the current plateau. The integral above is strictly decreasing in that rate; hence \(U\) is nonconstant and \(P-M^2>0\). Let \(T_i\) be the time since particle \(i\)'s most recent reset. The \(T_i\) are conditionally independent given the environment. Conditional Gaussian Brownian increments give \(P=4D^2\mathbb E[(\mathbb E[T_i\mid\lambda_\cdot])^2]\) and \(H=12D^2\mathbb E[T_i^2]\). Conditional Jensen implies \(3P\le H\). Since \(M>0\),

\[
0<\frac{P-M^2}{H-M^2}<\frac13.
\]

If \(F\) is a point mass, the two reset processes are actually independent, and their squared-displacement correlation is exactly zero.

**Slow-refresh universality.** Suppose \(f(\lambda)\sim c\lambda^{\alpha}\) with \(-1<\alpha<1\). Rescale the rate integral by \(\lambda=\nu t\). Dominated convergence on the near-zero region and a fixed positive lower cutoff on the remaining region imply

\[
 A_2\sim c\nu^{\alpha-1}K_\alpha,\qquad
 C\sim c\nu^{\alpha-1}J_\alpha,
\]

where

\[
 K_\alpha=\int_0^\infty\frac{t^\alpha}{(1+t)^2}\,dt,
 \qquad
 J_\alpha=\int_0^\infty\frac{t^\alpha}{(1+t)(1+2t)}\,dt.
\]

Both integrals are finite and positive precisely for \(-1<\alpha<1\). One also has \(\nu A\to0\), \(\nu B\to0\), and \(A^2=o(A_2)\): for negative \(\alpha\), \(A=O(\nu^{\alpha})\); at zero \(A=O(\log(1/\nu))\); and for positive \(\alpha\), \(A=O(1)\). Inserting these bounds in the exact correlation formula yields the limit \(J_\alpha/(3K_\alpha)\).

The ratio has an elementary integral evaluation valid throughout the entire exponent range. The identity

\[
\frac1{(1+t)(1+2t)}=\int_{1/2}^1\frac{da}{(t+a)^2}
\]

and Tonelli's theorem give, after \(t=au\),

\[
 \frac{J_\alpha}{K_\alpha}=\int_{1/2}^1a^{\alpha-1}\,da
 =\begin{cases}(1-2^{-\alpha})/\alpha,&\alpha\ne0,\\ \log2,&\alpha=0.\end{cases}
\]

This proves the universal limits without assuming an exponential distribution of rates. The limiting correlation is a strictly decreasing function of \(\alpha\), with range \((1/6,1/3)\) as \(\alpha\) runs over \((-1,1)\).

**Explicit exponential example.** If \(f(\lambda)=L^{-1}e^{-\lambda/L}\) with \(L>0\), then

\[
 A=\frac{e^{\nu/L}E_1(\nu/L)}{L},\quad
 B=\frac{e^{\nu/(2L)}E_1(\nu/(2L))}{2L},\quad
 A_2=\frac1{L\nu}-\frac AL,\quad C=\frac{2B-A}{\nu},
\]

where \(E_1(z)=\int_z^\infty e^{-u}u^{-1}du\). These expressions in the general formula give the exact finite-refresh correlation, and its slow-refresh value \(\log2/3\). The leading mixed moment and single-particle fourth moment diverge as \(P\sim8D^2\log2/(L\nu)\) and \(H\sim24D^2/(L\nu)\), while \(M=O(\log(1/\nu))\). Thus the limit is a ratio of divergent fourth-order moments, not a finite-moment limit of the frozen-rate mixture.

## Verification

The companion standalone script `CHECK.py` independently solves the two-environment-state moment balances for a nondegenerate discrete rate law, cross-checks the exact integral formula and the deterministic-rate boundary, and evaluates slow-refresh correlations for gamma-distributed rates with exponents \(-1/2\), \(0\), \(1/2\). It also checks high-precision convergence to \(\log2/3\) for exponentially distributed rates and validates the integral identity used in the asymptotic proof. Numerical and finite-state checks corroborate, but do not replace, the analytic arguments above. Run it with Python 3 and the dependency declared in `requirements.txt`.

## Relationship to prior work

Arutkin and Reuveni (2025) introduced the Poisson-refreshed stochastic resetting intensity and derived the exact stationary *one-particle* distribution and its asymptotic regimes; that one-body analysis and the exponential-rate law are not claimed here. The present model uses the same intensity process but adds two particles with **separate conditional reset clocks**. The joint mixed moment and its universal rate-density-dependent correlation are not results of the one-particle Fourier transform alone.

De Mauro, Biroli, Majumdar and Schehr (2025) treat several independent Brownian particles whose resetting times are **simultaneous** and share a renewal age, even when the inter-reset law is general. Their resetting generator has one shared reset event and is not the two independent conditional Cox hazards considered here. Boyer and Majumdar (2025) extend simultaneous resetting to memory of past positions, again with jointly reset coordinates. Mesquita, Majumdar and Sabhapandit (2025) demonstrate correlations from a common fluctuating *diffusivity*, not a shared fluctuating *reset rate*. These works demonstrate a general mechanism for environmental correlations but do not present the stated independent-reset correlation formula or the universal small-intensity exponent law. A broad prior theorem for Markov-modulated Cox resetting might imply parts of this result, so independent literature validation is still warranted.

## Limitations

The microscopic model has independent Brownian noises, independent particle-reset point processes conditional on a common piecewise-constant environmental hazard, zero reset locations, and redraws independent of particle evolution. The universality theorem fixes the instantaneous-rate law and takes stationary distributions before the slow-refresh limit. It does not describe simultaneous resetting, interacting particles, spatially dependent hazards, or nonstationary coupled limits. It does not claim a universal limiting *joint position distribution*, only the stated squared-displacement correlation; fourth moments diverge in the slow-refresh family. The stationary correlation at a finite refresh rate generally depends on the complete rate law.

## References

1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first publicly posted 2025-09-29). https://arxiv.org/abs/2509.25365 . Relevant material: §§2–4 and equations (23)–(24).
2. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658v1 (2025). https://arxiv.org/abs/2509.06658 . Relevant material: introduction and the exact stationary renewal joint law.
3. D. Boyer and S. N. Majumdar, *Emerging correlations between diffusing particles evolving via simultaneous resetting with memory*, arXiv:2510.21972v1 (2025). https://arxiv.org/abs/2510.21972 . Relevant material: §§I–III, the shared-reset generator and squared-displacement correlation observable.
4. N. Mesquita, S. N. Majumdar and S. Sabhapandit, *Dynamically emergent correlations in a Brownian gas with diffusing diffusivity*, arXiv:2506.20859v1 (2025). https://arxiv.org/abs/2506.20859 . Relevant model: a common fluctuating diffusion coefficient.
