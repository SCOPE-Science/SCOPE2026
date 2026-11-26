# Reversibility and hidden dissipation in a telegraph-driven harmonic vortex

## Finding

A planar Brownian vortex whose torque changes sign at the jump times of a two-state process has an exact, sharp visibility boundary. **Its stationary planar-position trajectory is statistically invariant under time reversal at all time orders if and only if the two sign-switching rates are equal**, while the path-relative-entropy production of the *jointly observed* position and sign, when the sign is declared even under time reversal, is always \(2\omega^2/k>0\). At equal switching rates, the position trajectory is nonetheless non-Markov and has non-Gaussian two-time distributions. For all switching rates, the radius alone has the same law as the radius in equilibrium harmonic Brownian motion. These statements are about path distributions, not merely about stationary current or two-time covariance.

## Assumptions and scope

Let \(k,D,\omega,a,b>0\) and \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). Define the process on \(\mathbb R^2\times\{-1,1\}\) by
\[
dX_t=(-kX_t+\omega S_tJX_t)\,dt+\sqrt{2D}\,dW_t.
\]
The planar Brownian motion \(W\) is independent of the autonomous two-state Markov chain \(S\), with rates \(+1\to-1\) at \(a\) and \(-1\to+1\) at \(b\). Position coordinates are even under ordinary path reversal; the sign is also **declared time-even for the joint path-relative-entropy comparison**. A reversed jump path can be taken in its right-continuous version. No thermodynamic assertion is made for an alternative odd-parity treatment of the sign. Set \(q=D/k\), \(p_+=b/(a+b)\), \(p_-=a/(a+b)\), and \(\varphi(x)=(2\pi q)^{-1}\exp[-|x|^2/(2q)]\).

## Proof

**1. Stationarity and uniqueness.** For a fixed sign path, the fundamental matrix from \(u\) to \(t\) is \(U_{t,u}=e^{-k(t-u)}R(\omega\int_u^t S_v\,dv)\), where \(R(\theta)=\cos\theta\,I_2+\sin\theta\,J\). For a two-sided stationary sign path and independent Brownian motion, the integral
\[
X_t=\sqrt{2D}\int_{-\infty}^t U_{t,u}\,dW_u
\]
is well defined conditionally on the sign path and converges in mean square. Its conditional law at each single time is centered Gaussian with covariance \(2D\int_0^\infty e^{-2kv}\,dv\,I_2=qI_2\), independent of the sign path. Thus the stationary joint density is \(p_s\varphi(x)\). To prove uniqueness, couple two sign chains so they coalesce in finite time almost surely (independent until they meet, shared afterward), and use the same Brownian increments in the two position equations. After coalescence the difference in positions has norm decaying exactly at rate \(k\). In particular two stationary laws must agree on all bounded Lipschitz tests and hence coincide.

**2. Stationary reversal and joint path entropy.** The conditional stationary current is \(j_s(x)=\omega sJx\,p_s\varphi(x)\); the equilibrium gradient current cancels and \(\nabla\cdot(Jx\varphi)=0\). In the stationary inner product the generator
\[
(Lf)(x,s)=D\Delta f+(-kx+\omega sJx)\cdot\nabla f+c_s[f(x,-s)-f(x,s)],\qquad c_+=a,\quad c_-=b,
\]
has adjoint given by \(\omega\mapsto-\omega\) with the same jump rates, since \(p_+a=p_-b\). This is the generator of the label-preserving stationary reversal. The jump contribution to path relative entropy is zero. The diffusion contribution per unit time is
\[
\sigma=\sum_{s=\pm1}\int_{\mathbb R^2}\frac{|j_s(x)|^2}{D p_s\varphi(x)}\,dx
=\frac{\omega^2}{D}\,\mathbb E|X|^2=\frac{2\omega^2}{k}>0.
\]
Indeed, conditional on the sign path over the observation interval, the two path measures have the same initial Gaussian and diffusion coefficient \(\sqrt{2D}\); the diffusion likelihood formula for the linear drifts gives relative entropy \((4D)^{-1}\int\mathbb E|2\omega S_tJX_t|^2\,dt\). The rate is independent of the switching rates and diffusivity in the strictly positive parameter domain. It is a *joint path-law* quantity under the specified reversal convention, not a position-only entropy production.

**3. Sufficiency of the sharp reversibility boundary.** When \(a=b=\lambda\), let \((\mathcal T f)(x,s)=f(x,-s)\). The stationary measure is invariant under this involution and \(L^*=\mathcal T L\mathcal T\). Thus the stationary reversed joint process has the same law as the forward process with every sign flipped. Projecting away the sign gives path reversal of position: for every integer \(m\ge1\) and \(0\le t_1<\cdots<t_m\le T\),
\[
(X_{t_1},\ldots,X_{t_m})\ \stackrel{d}{=}\ (X_{T-t_1},\ldots,X_{T-t_m}).
\]
The coordinates on the right are in decreasing time order. This gives the full reversal law of the continuous position path, not merely zero mean circulation.

**4. Necessity.** At stationarity \(\mathbb ES=(b-a)/(a+b)\) and \(S_t\) is independent of \(X_t\) at each fixed time. The mean oriented Stratonovich area growth per unit time is
\[
T^{-1}\mathbb E\int_0^T(X_t^1\circ dX_t^2-X_t^2\circ dX_t^1)
=\omega\,\mathbb E[S|X|^2]=\frac{2D\omega(b-a)}{k(a+b)}.
\]
Independent Brownian coordinates give zero cross-noise Stratonovich corrections. Reversal changes the sign of this area functional. Equivalently, the derivative at \(t=0+\) of \(\mathbb E[X_t^2X_0^1]-\mathbb E[X_t^1X_0^2]\) equals the same expression, whereas stationarity and path reversal would require this antisymmetric lag covariance to vanish. Thus \(a\ne b\) rules out reversibility.

**5. Exact two-time law, non-Markovianity and nonlinear visibility.** Assume \(a=b=\lambda\), and set \(\Theta_t=\omega\int_0^t S_u\,du\). The conditional transition is \(X_t=e^{-kt}R(\Theta_t)X_0+N_t\), with \(N_t\) conditionally centered Gaussian and independent of \(X_0\) given the sign path. Its covariance is \(q(1-e^{-2kt})I_2\). Symmetry gives \(\mathbb E\sin\Theta_t=0\). For \(v>0\), let \(m_v(t)=\mathbb E\cos(v\int_0^tS_u\,du)\). The two-state generator yields
\[
m_v''+2\lambda m_v'+v^2m_v=0,\qquad m_v(0)=1,\quad m_v'(0)=0.
\]
Thus \(\mathbb E[X_tX_0^{\mathsf T}]=q e^{-kt}m_\omega(t)I_2\). For \(\lambda>\omega\), with \(z=\sqrt{\lambda^2-\omega^2}\),
\[
m_\omega(t)=e^{-\lambda t}[\cosh(zt)+(\lambda/z)\sinh(zt)].
\]
At \(\lambda=\omega\) this is \(e^{-\lambda t}(1+\lambda t)\); for \(\lambda<\omega\), put \(z=\sqrt{\omega^2-\lambda^2}\) and use \(\cos(zt)+(\lambda/z)\sin(zt)\) in the bracket. In the last regime the diagonal covariance changes sign infinitely often despite exact path reversibility.

Were the stationary observed position Markov, its linear conditional mean \(\mathbb E[X_t\mid X_0=x]=e^{-kt}m_\omega(t)x\) would obey the semigroup composition law \(m_\omega(t+u)=m_\omega(t)m_\omega(u)\). This is impossible since \(m_\omega'(0)=0\) but \(m_\omega''(0)=-\omega^2\). Hence it is non-Markov for every finite \(\lambda>0\).

Conditional on \(\Theta_t\), the joint two-time law is Gaussian with orthogonal cross-covariance of magnitude \(q e^{-kt}|\sin\Theta_t|\). Isserlis' identity gives covariance \(2q^2e^{-2kt}\sin^2\Theta_t\) between \((X_t^1)^2\) and \((X_0^2)^2\) conditionally on \(\Theta_t\). The conditional means of the two squares are constant and equal to \(q\). Averaging gives
\[
\operatorname{Cov}((X_t^1)^2,(X_0^2)^2)=q^2e^{-2kt}[1-m_{2\omega}(t)]>0\qquad(t>0).
\]
The event of exactly one switch gives the integrated phase a continuous component on a nonempty interval, proving strict positivity. Meanwhile \(\mathbb E[X_t^1X_0^2]=0\). A centered joint Gaussian pair with this zero cross-covariance would have zero covariance of the squares. The two-time law is therefore non-Gaussian at each positive lag.

**6. An equilibrium radial alias.** Itô's formula for \(Z_t=|X_t|^2\) gives the autonomous generator
\[
(\mathcal Ag)(z)=(4D-2kz)g'(z)+4Dz g''(z),\qquad z\ge0,
\]
and the stationary law is exponential with mean \(2D/k\). For arbitrary \(a,b>0\), put \(\Theta_t=\omega\int_0^t S_u\,du\) and take \(Y_t=R(-\Theta_t)X_t\). The finite-variation rotation cancels the skew drift; conditional on the sign path, the rotated Wiener integral is standard Brownian motion independent of the stationary Gaussian \(Y_0=X_0\). Thus \(Y_t\) solves the equilibrium planar Ornstein–Uhlenbeck equation in law, and \(|X_t|=|Y_t|\) at every time. Radius-only data cannot distinguish this rotation from the equilibrium process, and time-antisymmetry tests on the position path cannot distinguish its forward and reversed laws for symmetric switching. Under the specified model one can nevertheless infer \(\omega^2\) from the curvature \(m_\omega''(0)\); a zero observed path-entropy rate does not preclude model-based inference.

## Verification

The standalone `verify.py` tests the Gaussian stationary Fokker–Planck equation, vanishing rotational divergence, adjoint-involution identities on polynomials and both sign values, the telegraph characteristic recurrence and its first derivatives, the radial generator on three powers, the area-current and entropy algebra, the Wick identity, and matrix-exponential comparisons in oscillatory, critical and overdamped parameter regimes. Reproduce with `python verify.py` (SymPy, SciPy and NumPy). These finite checks corroborate the analytic proof; they do not establish the all-parameter or path-law statements by themselves.

## Relationship to prior work

Cerasoli et al. [1] develop spectral diagnostics for the two-temperature Brownian gyrator. Di Terlizzi, Baiesi and Ritort [2] solve the continuously driven Brownian vortex and obtain its entropy production; its torque has fixed direction, so it does not have the finite-rate sign-switching projection studied here. Kawaguchi and Nakayama [3] establish general hidden-entropy-production principles. Knight, Kaveh and Pruessner [4] already exhibit exactly reversible projected position paths with hidden symmetric telegraph self-propulsion under their chosen reversal. This qualitative phenomenon is not claimed as new. In contrast with additive self-propulsion, the present angular drift is linear in position and multiplies the hidden sign. The claim is the sharp classification and accompanying observable formulas for this specific rotational model, not novelty for the constant-torque entropy expression, the telegraph characteristic function, or general operator-intertwining arguments.

## Limitations

The statement assumes a harmonic trap, isotropic additive Brownian noise, a positive torque magnitude, and autonomous sign switching at finite strictly positive rates. No result is asserted for inertial dynamics, nonlinear torques or anisotropic diffusion. The positive entropy rate is for fixed-label reversal of the joint Markov law, not a parity-independent physical heat-production rate. Only the radial process matches the equilibrium Ornstein–Uhlenbeck counterpart; the planar position path has a different law.

## References

1. S. Cerasoli et al., *Spectral fingerprints of non-equilibrium dynamics: The case of a Brownian gyrator*, arXiv:2201.04903. https://arxiv.org/abs/2201.04903
2. I. Di Terlizzi, M. Baiesi and F. Ritort, *Variance sum rule: proofs and solvable models*, arXiv:2403.10442, especially Section 5. https://arxiv.org/abs/2403.10442
3. K. Kawaguchi and Y. Nakayama, *Fluctuation theorem for hidden entropy production*, arXiv:1209.6333. https://arxiv.org/abs/1209.6333
4. J. Knight, F. Kaveh and G. Pruessner, *Self-propulsion symmetries determine entropy production of active particles with hidden states*, arXiv:2507.22199, symmetric-telegraph case and Table 1. https://arxiv.org/abs/2507.22199
