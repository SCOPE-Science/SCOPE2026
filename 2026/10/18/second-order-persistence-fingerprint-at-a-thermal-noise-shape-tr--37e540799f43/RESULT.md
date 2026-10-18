# Second-order persistence fingerprint at a thermal-noise shape transition

## Finding
Consider the stationary density of a one-dimensional harmonically trapped run-and-tumble particle with thermal diffusion. The Gaussian-convolution representation and the critical noise equation are known [1–3]. The new quantitative statement here is the **second-order law for the positions of its two peaks as the critical noise is approached**, together with a persistence-dependent change of sign in its first nonuniversal coefficient.

Fix trap relaxation \(\kappa>0\), propulsion speed \(v>0\), symmetric direction-flip rate \(\gamma>0\), and thermal diffusivity \(D>0\). Put
\[
\ell=\gamma/\kappa,\qquad R=v/\kappa,\qquad \nu=D/(\kappa R^2)=D\kappa/v^2.
\]
For each \(0<\ell<1\) there is a unique critical \(\nu_c(\ell)>0\) at which the stationary density changes from two peaks (\(0<\nu<\nu_c\)) to one (\(\nu\geq\nu_c\)). Let \(z_\pm(\nu)\) be the dimensionless peak positions, in units of \(R\), and let \(\delta=\nu_c-\nu\downarrow0\). Then
\[
\boxed{z_\pm(\nu)^2=3\delta+K(\ell)\delta^2+O_\ell(\delta^3),\quad
 K(\ell)=\frac{3\{1+(2\ell-9)\nu_c(\ell)\}}{10\nu_c(\ell)^2}.}
\]
The universal leading term follows from the Gaussian heat equation and is **not** asserted as a new general smoothing principle. The explicit next coefficient is specific to the trapped telegraph model. It is negative at small \(\ell\), positive sufficiently near \(\ell=1\), and consequently vanishes for at least one intermediate persistence ratio. In fact,
\[
\lim_{\ell\downarrow0}K(\ell)=-\frac{12}{5},\qquad
\lim_{\ell\uparrow1}K(\ell)=+\infty.
\]
For physical peak coordinates \(x_\pm=Rz_\pm\), the expansion gives
\[
 x_\pm^2=\frac{3(D_c-D)}{\kappa}+\frac{K(\ell)(D_c-D)^2}{v^2}+O_\ell((D_c-D)^3),
 \quad D_c=\frac{v^2}{\kappa}\nu_c(\ell),
\]
where the remainder is understood at fixed \(v,\kappa,\gamma\). Thus the first correction beyond universal square-root splitting contains an explicit signature of directional persistence. No uniqueness of the zero of \(K\) is claimed.

## Assumptions and scope
The position \(X_t\) satisfies
\[
 dX_t=(-\kappa X_t+vS_t)\,dt+\sqrt{2D}\,dW_t,
\]
where \(S_t\in\{-1,+1\}\) flips at rate \(\gamma\), the Brownian motion is independent of \(S\), and both are stationary on the infinite time axis. A single stationary distribution exists. The dimensionless stationary density is
\[
 P_{\ell,\nu}(z)=\int_{-1}^1 p_\ell(y)\frac{e^{-(z-y)^2/(2\nu)}}{\sqrt{2\pi\nu}}\,dy,
 \quad p_\ell(y)=\frac{\Gamma(\ell+1/2)}{\sqrt\pi\Gamma(\ell)}(1-y^2)^{\ell-1}{\bf1}_{|y|<1}.
\]
This beta law and Gaussian convolution are established in the cited literature. The theorem concerns fixed \(0<\ell<1\) and \(\nu\) sufficiently close to its critical value from below; the separate limits \(\ell\downarrow0\) and \(\ell\uparrow1\) are limits of the coefficient, not uniform joint-limit remainders.

## Proof
**1. Exact critical equation and uniqueness.** Define \(t=(2\nu)^{-1}\), and let
\[
 M_\ell(t)=\int_0^1 u^{-1/2}(1-u)^{\ell-1}e^{-tu}\,du,
 \qquad q_\ell(t)=-\frac{M_\ell'(t)}{M_\ell(t)}.
\]
Writing \(U=y^2\) under the exponentially tilted beta law, differentiation of the Gaussian convolution gives
\[
\frac{P_{\ell,\nu}''(0)}{P_{\ell,\nu}(0)}=\frac{q_\ell(t)-\nu}{\nu^2}.
\]
Consequently the critical equation \(P''(0)=0\), previously known in implicit form [2,3], is equivalent to \(F_\ell(t):=2tq_\ell(t)-1=0\). Integration by parts in \(M_\ell\) yields
\[
 t\langle U^{j+2}\rangle_t=(t+j+\ell+\tfrac12)\langle U^{j+1}\rangle_t-(j+\tfrac12)\langle U^j\rangle_t,
\qquad j\ge0.
\]
At any zero of \(F\), \(\langle U\rangle_t=1/(2t)=\nu\). The recurrence at \(j=0\) then gives \(\langle U^2\rangle_t=(2\ell+1)\nu^2\), hence \(\operatorname{Var}_t(U)=\ell/(2t^2)\). Since \(q_\ell'(t)=-\operatorname{Var}_t(U)\), at **every** zero
\[
 F_\ell'(t)=2q_\ell(t)+2tq_\ell'(t)=\frac{1-\ell}{t}>0.
\]
Moreover \(F_\ell(0)=-1\) and, as \(t\to\infty\), Laplace asymptotics give \(F_\ell(t)\sim(1-\ell)/t>0\). Continuity and strictly upward crossing at each zero prove existence and uniqueness for \(0<\ell<1\). Smooth parameter dependence follows from the implicit-function theorem. The tilted law has \(\partial_\ell q_\ell(t)=\operatorname{Cov}_t(U,\log(1-U))<0\); therefore \(t_c(\ell)\) strictly increases and \(\nu_c(\ell)=1/(2t_c(\ell))\) strictly decreases.

**2. Fourth and sixth derivatives at the threshold.** The same moment recurrence at \(j=1\) gives, at \(\nu=\nu_c\),
\[
\langle U^3\rangle_t=2(\ell-1)\nu_c^2+(4\ell^2+8\ell+3)\nu_c^3.
\]
Gaussian differentiation expressed through Hermite polynomials yields
\[
\frac{P^{(4)}(0)}{P(0)}=\frac{\langle U^2\rangle-6\nu\langle U\rangle+3\nu^2}{\nu^4}
=\frac{2(\ell-1)}{\nu_c^2}<0,
\]
\[
\frac{P^{(6)}(0)}{P(0)}=\frac{\langle U^3\rangle-15\nu\langle U^2\rangle+45\nu^2\langle U\rangle-15\nu^3}{\nu^6}
=\frac{2(\ell-1)\{1+(2\ell-9)\nu_c\}}{\nu_c^4}.
\]
Thus the flat peak at criticality is quartically nondegenerate.

**3. Peak splitting and its second coefficient.** Gaussian convolution obeys the heat equation \(\partial_\nu P=\tfrac12\partial_z^2P\). At the critical point set \(A(\nu)=P''(0;\nu)\), \(B(\nu)=P^{(4)}(0;\nu)/6\), and \(C(\nu)=P^{(6)}(0;\nu)/120\). Analyticity gives, for small nonzero \(z\),
\[
 0=P'(z;\nu)/z=A(\nu)+B(\nu)z^2+C(\nu)z^4+O(z^6).
\]
The heat equation implies \(A'(\nu_c)=3B_c\), \(A''(\nu_c)=30C_c\), and \(B'(\nu_c)=10C_c\). With \(\delta=\nu_c-\nu\) and \(z^2=3\delta+k\delta^2+O(\delta^3)\), substitution yields \(B_c k-6C_c=0\), or
\[
 k=\frac{6C_c}{B_c}=\frac{3}{10}\frac{P^{(6)}(0;\nu_c)}{P^{(4)}(0;\nu_c)}
=\frac{3\{1+(2\ell-9)\nu_c\}}{10\nu_c^2}.
\]
Because \(B_c<0\), the implicit-function theorem for the analytic equation in \(z^2,\nu\) produces two nonzero stationary points for \(\delta>0\), and they are strict local maxima. No other peaks occur: the original even beta density has two peaks and one central trough for \(\ell<1\); the Gaussian kernel is strictly totally positive, and its variation-diminishing/zero-number property bounds the sign changes of the differentiated convolution by three. Symmetry, negative derivative for \(z>1\), and the local signs at the origin therefore force exactly two maxima below threshold and one at or above it. Equivalently, a standard smooth two-peak approximation to the beta density and the Gaussian zero-number principle establish this bound in the singular-edge limit. For \(\ell\ge1\), the beta law is log-concave; Gaussian smoothing is strictly unimodal.

**4. Genuine persistence dependence and sign reversal.** As \(\ell\downarrow0\), \(p_\ell\) converges weakly to equal masses at \(\pm1\); the critical equation tends to \(\nu_c=1\), giving \(K\to-12/5\). As \(\ell\uparrow1\), the initial law tends to the uniform law on \([-1,1]\), whose Gaussian convolution has \(P''(0)<0\) at every positive noise level. The unique critical variance therefore tends to zero. In the formula for \(K\), the numerator tends to 1, so \(K\to+\infty\). Continuity then forces at least one persistence ratio with \(K=0\). These asymptotics concern only the second coefficient and do not establish a unique crossing.

## Verification
A standalone checker `verify.py` independently evaluates Gaussian-convolution derivatives by Gauss–Jacobi quadrature and locates \(\nu_c\) and the nonzero stationary peak using scalar root-finding. It compares the exact moment identities and the expansion for \(\ell=0.5\) and \(\ell=0.9\), with additional critical-line and coefficient checks for other persistence ratios. For example, \(\nu_c(0.5)\approx0.31646434035\), \(K(0.5)\approx-4.58827650\), while \(\nu_c(0.9)\approx0.11912623750\), \(K(0.9)\approx3.00804349\). This numerical check is corroboration, not a replacement for the preceding infinite-domain proof.

## Relationship to prior work
The exact stationary beta density, Gaussian smoothing, qualitative finite-noise shape transition, and implicit critical-noise equation are established in [1–3] and are not claimed to be new. In particular, [2, Sec. V.1.1, Eqs. (96)–(98)] explicitly derives the curvature-based phase boundary and its limiting regimes. The distinction assessed here is the **explicit postcritical peak-position expansion through the first model-dependent correction**, its closed dependence on persistence via \(\nu_c\), and the forced sign reversal in that coefficient. The universal leading coefficient itself is a direct consequence of the heat equation and is not claimed as a standalone novelty. Broader smoothing and local-bifurcation theory can provide the formal expansion framework, but the reported beta-model evaluation and persistence sign reversal were not located in the checked literature.

## Limitations
This is a stationary, one-dimensional, symmetric telegraph-propulsion model with additive white thermal noise and a harmonic trap. The expansion is for fixed \(0<\ell<1\), not uniform as \(\ell\) approaches 0 or 1. The zero of \(K\) is proved to exist, not proved unique. No claim is made about interacting particles, nonharmonic potentials, anisotropic driving, noise-colored baths, finite-time switching dynamics, or statistical estimation under measurement noise. The leading square-root mode law is generic to Gaussian smoothing; novelty rests on the explicit next-order coefficient and its sign transition.

## References
[1] F. J. Sevilla and J. A. Meléndez Mora, “Nonequilibrium statistics of harmonically trapped run-and-tumble particles: An exact convolution approach,” arXiv:2608.21781v1 (first posted 2026-08-22), https://arxiv.org/abs/2608.21781.

[2] M. Guéneau, S. N. Majumdar, and G. Schehr, “Exact Stationary State of a \(d\)-dimensional Run-and-Tumble Particle in a Harmonic Potential,” arXiv:2602.08436v1 (first posted 2026-02-09), https://arxiv.org/html/2602.08436v2, particularly Sec. V.1.1.

[3] S. Sabhapandit and S. N. Majumdar, “Noninteracting particles in a harmonic trap with a stochastically driven center,” arXiv:2404.02480v1 (first posted 2024-04-03), https://arxiv.org/pdf/2404.02480, Sec. 4.1.

[4] Classical Gaussian variation-diminishing theorem (Schoenberg–Karlin theory) and the one-dimensional parabolic zero-number principle, used only for the global mode count.
