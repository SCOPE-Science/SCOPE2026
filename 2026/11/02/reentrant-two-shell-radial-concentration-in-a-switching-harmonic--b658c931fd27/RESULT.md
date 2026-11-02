# Reentrant two-shell radial concentration in a switching harmonic trap

## Finding
For an isotropic Brownian particle in \(d\) spatial dimensions, let a harmonic confining drift switch between on and off at equal positive rates. The rescaled stationary Euclidean radius has a high-dimensional limiting density with **two disconnected intervals of switching-rate parameters exhibiting a boundary peak and a second, interior peak**. In these same intervals the genuine finite-dimensional radial density has at least two distinct strict local maxima for every sufficiently large integer dimension. Nevertheless, the full stationary density per unit spatial volume is always strictly decreasing away from the origin.

Precisely, let \(\alpha=r/\kappa>0\), and define
\[
\alpha_- = 1-\frac{\sqrt 3}{2},\qquad
\alpha_+ = 1+\frac{\sqrt 3}{2},\qquad
\beta=\frac\alpha2.
\]
If \(S_d=\sqrt{\kappa/(dD)}\,\|X\|\) denotes the stationary radius, then under a coupling across dimensions
\[
S_d\longrightarrow S_\infty\quad\text{almost surely},\qquad
 g_\alpha(s)=\frac{\beta^\beta}{\Gamma(\beta)}s^3(s^2-1)^{\beta-1}e^{-\beta(s^2-1)}\mathbf 1_{\{s>1\}}
\]
is the density of \(S_\infty\). It has an integrably divergent boundary peak at \(s=1\) exactly when \(\alpha<2\). In addition to this boundary peak, it has a distinct strict interior maximum **if and only if**
\[
0<\alpha<\alpha_-\quad\text{or}\quad\alpha_+<\alpha<2.
\]
There is a strict interior minimum between these two peaks. All interior critical radii arise from the roots
\[
u_\pm=\frac{2\alpha+1\pm\sqrt{4\alpha^2-8\alpha+1}}{2\alpha},
\qquad s_\pm=\sqrt{u_\pm},
\]
where the minimum is \(s_-\) and the maximum is \(s_+\). For \(\alpha\in[\alpha_-,\alpha_+]\), the limiting density is strictly decreasing on \((1,\infty)\), although its derivative vanishes at one radius at either endpoint. For \(\alpha\ge2\), the boundary is not divergent and the limiting density has exactly one interior maximum, at \(s_+\). Thus the additional exterior shell appears and disappears twice as the switching-rate ratio varies, before the boundary divergence disappears at \(\alpha=2\).

For each fixed \(\alpha\) in either open two-shell interval there exists an integer \(d_0(\alpha)\) such that, for every integer \(d\ge d_0(\alpha)\), the actual smooth radial density of \(S_d\) has at least two separated strict local maxima with an intervening strict local minimum. No claim of exactly two finite-dimensional maxima or a finite-dimensional threshold at \(\alpha_\pm\) is made.

## Assumptions and scope
Let \(\kappa,D,r>0\). Let \(J_t\) be an independent stationary two-state continuous-time Markov chain taking values in \(\{0,1\}\), switching in each direction at rate \(r\). Let \(B_t\) be standard \(d\)-dimensional Brownian motion, independent of \(J\). The position satisfies the Itô stochastic differential equation
\[
dX_t=-\kappa J_t X_t\,dt+\sqrt{2D}\,dB_t.
\]
The stationary law is unique and equals the zero-mean isotropic Gaussian scale mixture described below. The radial probability density means density with respect to \(ds\), including the Euclidean Jacobian. It is **not** the radial profile of probability density per unit \(d\)-dimensional volume. The limit is first in physical time to stationarity and then in integer dimension \(d\to\infty\), at a fixed parameter \(\alpha\).

Write \(\lambda\in(0,1)\) for the dimensionless effective instantaneous trap stiffness (equivalently inverse normalized conditional coordinate variance) in the stationary Gaussian mixture. Its density is
\[
p_\alpha(\lambda)=\frac{\beta^\beta e^\beta}{2\Gamma(\beta)}
(1-\lambda)^{\beta-1}\lambda^{-\beta-2}e^{-\beta/\lambda},\qquad 0<\lambda<1.
\]
Conditional on \(\lambda\), the dimensionless vector \(Z=\sqrt{\kappa/D}\,X\) is \(\lambda^{-1/2}G_d\), where \(G_d\) consists of independent standard Gaussian coordinates. This established mixture law is an input, also independently reconstructed in the proof.

## Proof
**1. Effective-stiffness law.** Conditional on a full past switching path, the stationary Gaussian coordinate variance \(V\) obeys \(\dot V=-2\kappa J V+2D\). With time divided by \(\kappa\) and \(\lambda=D/(\kappa V)\), its deterministic evolution between switch events is \(\dot\lambda=2\lambda(J-\lambda)\). In stationary state the joint on/off densities have the form \(p_{\mathrm{on}}(\lambda)=\lambda p_\alpha(\lambda)\) and \(p_{\mathrm{off}}(\lambda)=(1-\lambda)p_\alpha(\lambda)\): indeed their total probability flux is
\[
2\lambda(1-\lambda)\lambda p_\alpha-2\lambda^2(1-\lambda)p_\alpha=0.
\]
The on-state balance equation is
\[
\frac{d}{d\lambda}\bigl(2\lambda^2(1-\lambda)p_\alpha(\lambda)\bigr)=
\alpha(1-2\lambda)p_\alpha(\lambda).
\]
Solving this first-order equation and normalizing gives precisely the density displayed above. An explicit normalization check comes from the substitution \(T=\beta(\lambda^{-1}-1)\):
\[
\mathbb P(T\in dt)/dt=
\frac12\frac{t^{\beta-1}e^{-t}}{\Gamma(\beta)}+
\frac12\frac{t^\beta e^{-t}}{\Gamma(\beta+1)},\quad t>0.
\]
Thus \(T\) is a half-and-half mixture of gamma distributions of shapes \(\beta\) and \(\beta+1\), both with unit rate. This also gives existence of the conditional stationary Gaussian mixture; convergence of the effective variance to its stationary law follows from positive recurrent two-state switching and the stabilizing on intervals.

**2. High-dimensional radius and its density.** Couple all dimensions using one draw of \(\lambda\) and an infinite sequence of independent standard normal random variables \(G_i\). By the strong law,
\[
S_d=\lambda^{-1/2}\sqrt{d^{-1}\sum_{i=1}^dG_i^2}
\longrightarrow\lambda^{-1/2}=\sqrt{1+T/\beta}\quad\text{almost surely}.
\]
The stated formula for \(g_\alpha\) follows by the change of variables \(T=\beta(s^2-1)\) in the gamma mixture. It integrates to one. Since \(g_\alpha(s)\asymp(s-1)^{\beta-1}\) as \(s\downarrow1\), the boundary behavior is as claimed.

**3. Exact critical-point classification.** For \(s>1\), direct differentiation gives
\[
\frac{g_\alpha'(s)}{g_\alpha(s)}=
\frac{-\alpha s^4+(2\alpha+1)s^2-3}{s(s^2-1)}.
\]
Putting \(u=s^2>1\), critical points therefore correspond to zeros of
\[
Q_\alpha(u)=\alpha u^2-(2\alpha+1)u+3.
\]
The discriminant is \(\Delta=4\alpha^2-8\alpha+1\), and \(Q_\alpha(1)=2-\alpha\). For \(0<\alpha<2\), both real roots are strictly above one precisely when \(\Delta>0\), equivalent to the two stated intervals. The numerator of \(g_\alpha'/g_\alpha\) is \(-Q_\alpha(u)\); hence the signs are negative, positive, negative across the two roots, giving the interior minimum and maximum. At either discriminant-zero endpoint \(Q_\alpha\ge0\) with a double zero and the density remains strictly decreasing. When \(\alpha\ge2\), the smaller root is at or below one and the larger root is above one; the density rises and then falls, with one interior maximum. The quadratic exhausts the possibilities.

**4. The finite-dimensional two-shell consequence.** Conditional on \(\lambda\), the normalized radius \(S_d\) has density
\[
h_{d,\lambda}(s)=\frac{2(d\lambda/2)^{d/2}}{\Gamma(d/2)}s^{d-1}e^{-d\lambda s^2/2},\quad s>0,
\]
so \(f_{d,\alpha}(s)=\int_0^1p_\alpha(\lambda)h_{d,\lambda}(s)\,d\lambda\). For \(d\ge2\), its derivative is strictly positive wherever \(0<s<\sqrt{1-1/d}\), because the derivative of each conditional density has the positive factor \((d-1)/s-d\lambda s\).

Further, \(f_{d,\alpha}\to g_\alpha\) in \(C^1\) on each compact interval contained in \((1,\infty)\). One direct justification sets \(Y_d=\sqrt{d^{-1}\sum_i G_i^2}\), \(U=\lambda^{-1/2}\), and writes \(\log S_d=\log U+\log Y_d\). The density of \(\log U\) is smooth on \((0,\infty)\), has at worst an integrable power singularity at zero, and decays faster than exponentially at infinity. The density of \(\log Y_d\) is a smooth approximate identity concentrated at zero, with its mass and every fixed-order derivative outside any neighborhood of zero exponentially small in \(d\). Convolution therefore converges together with one derivative on compacts at positive distance from zero; returning to \(s=e^x\) yields the claimed \(C^1\) convergence. The same conclusion follows by first-order differentiable Laplace asymptotics of the displayed integral with interior saddle \(\lambda=s^{-2}\).

Fix an \(\alpha\) in either two-shell window. Choose three radii \(1<a<s_-<b<s_+<c\). Their limiting density derivatives have signs negative, positive and negative, respectively. For every sufficiently large \(d\) the same is true of \(f'_{d,\alpha}(a),f'_{d,\alpha}(b),f'_{d,\alpha}(c)\); meanwhile \(f'_{d,\alpha}(0.9)>0\) for every \(d\ge6\). By continuity there must be a local maximum between \(0.9\) and \(a\), a local minimum between \(a\) and \(b\), and another local maximum between \(b\) and \(c\). The integral is real-analytic for \(s>0\) and cannot be constant on an interval, so the selected extrema can be strict. This proves the eventual finite-dimensional statement without assuming any particular finite-dimensional number of stationary points.

**5. No contradiction with central unimodality.** The complete vector spatial density equals a positive mixture of \((\lambda\kappa/(2\pi D))^{d/2}\exp[-\lambda\kappa\|x\|^2/(2D)]\). Its radial derivative is strictly negative for every radius \(\|x\|>0\). The second radial-histogram maximum is created by the surface-volume Jacobian and concentration of the conditional chi radius, not by a second maximum in probability per unit volume.

## Verification
The accompanying `verify.py` uses exact symbolic differentiation and discriminant identities, gamma-mixture normalization quadrature, and direct independent integration of the finite-dimensional conditional-chi density and derivative. In particular, at \(\alpha=0.1\) and \(d=100\) the computed radial-density derivative has signs \(+,-,+,-\) at radii \(0.95,1.30,2.20,3.50\). The theorem for all dimensions above an unspecified threshold follows analytically from \(C^1\) convergence and the sign argument, not from those four computations. Run `python verify.py` with Python 3, SymPy and SciPy.

## Relationship to prior work
Frydel (2024) derives the exact Gaussian mixture, its density \(p_\alpha\), its higher-dimensional extension, and a crossover at \(\alpha=2\) for the effective-stiffness endpoint. Those established formulas are the starting point, not a new contribution. The additional results here concern the **Euclidean-radius histogram**, its sharp pair of disjoint shell windows, and rigorous persistence of two local radial maxima for sufficiently high finite dimension. The manuscript's observed monotonicity of the full spatial density is consistent with, rather than contrary to, the radial-volume effect.

Biroli, Kulkarni, Majumdar and Schehr (2023/2024) derive a related common-Gaussian-mixture structure for a gas in a switching trap and analyze large-particle-number extremes, including a farthest-particle observable in fixed dimension. Their extreme-value law is distinct from the present single-vector \(d\to\infty\) norm concentration; the cited work does not supply the present two-window radius-mode classification. The correspondence of mixture mechanisms is acknowledged. Existing analytic mixture formulas make the limiting density derivable, so publication priority for the particular mode classification remains to be checked independently.

## Limitations
The sharp intervals classify the limiting radial density, **not** the entire finite-dimensional phase diagram. The rigorous finite-dimensional statement is existence of at least two strict separated local maxima for each fixed parameter in the two windows once dimension is sufficiently large; it supplies no effective universal dimension cutoff, no assertion of exactly two finite-dimensional maxima, and no statement at the window boundaries. The dimension limit is not interchangeable with a switching-rate limit approaching a critical boundary. The statement is about Euclidean radial histograms, not the vector density or marginal coordinates. The two-state switching rates are symmetric, on stiffness is positive and off stiffness is exactly zero; unequal switching rates, positive residual off-stiffness, and nonquadratic traps are not covered. The spectral/thermodynamic interpretation of a phase transition is not claimed. Independent publication-priority review has not been performed.

## References
1. D. Frydel, *Statistical mechanics of passive Brownian particles in a fluctuating harmonic trap*, arXiv:2407.12213v1 (first public 2024-07-16), revised version arXiv:2407.12213v2, Phys. Rev. E **110**, 024613 (2024). https://arxiv.org/abs/2407.12213 ; https://doi.org/10.1103/PhysRevE.110.024613 .
2. M. Biroli, M. Kulkarni, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations between particles in a switching harmonic trap*, arXiv:2312.02570 (first public 2023-12-05), Phys. Rev. E **109**, L032106 (2024). https://arxiv.org/abs/2312.02570 .
