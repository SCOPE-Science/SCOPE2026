# Reversibility and hidden dissipation in a telegraph-driven harmonic vortex

## Finding

A planar Brownian vortex whose torque changes sign at the jump times of a two-state process has an exact, sharp visibility boundary. **Its planar-position trajectory is statistically invariant under time reversal at all time orders if and only if the two sign-switching rates are equal**, while the path-relative-entropy production of the *jointly observed* position and sign, when the sign is declared even under time reversal, is always \(2\omega^2/k>0\). At equal switching rates, the position trajectory is nonetheless non-Markov and has non-Gaussian two-time distributions; its radius alone is indistinguishable in law from equilibrium harmonic Brownian motion. The contrast is a statement about path distributions, not merely about stationary current or two-time covariance.

## Assumptions and scope

Let \(k,D,\omega>0\), \(a,b>0\), and \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). On \(\mathbb R^2\times\{-1,1\}\), define
\[
dX_t=(-kX_t+\omega S_tJX_t)\,dt+\sqrt{2D}\,dW_t.
\]
The planar Brownian motion \(W\) is independent of the autonomous two-state Markov chain \(S\), whose rates are \(+1\to-1\) at \(a\) and \(-1\to+1\) at \(b\). Position coordinates are even under ordinary path reversal; the hidden sign is also **declared time-even for the joint path-relative-entropy comparison**. No thermodynamic assertion is made for an alternative odd-parity treatment of the sign. Set \(q=D/k\), \(p_+=b/(a+b)\), \(p_-=a/(a+b)\). Write \(\varphi(x)=(2\pi q)^{-1}\exp[-|x|^2/(2q)]\).

The theorem asserts (i) unique stationary measure \(p_s\varphi(x)\,dx\), (ii) exactly reversible **projected position path** if and only if \(a=b\), (iii) stationary fixed-label joint reversal-relative-entropy rate \(\sigma=2\omega^2/k\), (iv) at \(a=b=\lambda>0\) the explicit covariance, strict non-Markov property and strictly non-Gaussian two-time statistic below, and (v) equality in law of the complete squared-radius process and its equilibrium Ornstein–Uhlenbeck counterpart.

## Proof

**1. Stationarity and uniqueness.** Fix a two-sided stationary sign path. The fundamental matrix from \(u\) to \(t\) equals \(U_{t,u}=e^{-k(t-u)}R(\omega\int_u^tS_v\,dv)\), where \(R(\theta)=\cos\theta\,I_2+\sin\theta\,J\). Hence
\[
X_t=\sqrt{2D}\int_{-\infty}^tU_{t,u}\,dW_u
\]
converges in mean square. Conditional on the entire sign path, this integral is centered Gaussian with covariance \(2D\int_0^\infty e^{-2kv}\,dv\,I_2=qI_2\). Thus the stationary joint density factors as stated, and all stationary one-time position laws are the same isotropic Gaussian. Uniqueness follows by coupling two finite-state sign chains after a finite almost-sure meeting time, then using the same Brownian path: once the sign paths agree, the Euclidean distance between their positions decays exactly as \(e^{-kt}\), since the skew drift preserves norm.

**2. Stationary currents and joint path entropy.** The continuous conditional stationary current is \(j_s(x)=\omega sJx\,p_s\varphi(x)\): the equilibrium gradient current cancels, while \(\nabla\cdot(Jx\varphi)=0\). Sign jumps satisfy detailed balance \(p_+a=p_-b\). For the label-preserving stationary reversal the diffusion contribution to the relative-entropy rate is therefore
\[
\sigma=\sum_{s=\pm1}\int_{\mathbb R^2}\frac{|j_s(x)|^2}{D p_s\varphi(x)}\,dx
=\frac{\omega^2}{D}\,\mathbb E|X|^2=\frac{2\omega^2}{k}>0.
\]
The jump contribution is zero. The result does not depend on the switching rates or diffusivity (within the strictly positive parameter domain). It is a *joint path-law* quantity under the specified time-reversal convention, not a directly measured observable-position entropy production.

**3. Sufficiency of the sharp reversibility boundary.** When \(a=b=\lambda\), the backward generator acting on \(f(x,s)\) is
\[
(Lf)(x,s)=D\Delta f+(-kx+\omega sJx)\cdot\nabla f+\lambda[f(x,-s)-f(x,s)].
\]
With respect to the product stationary density, its adjoint is obtained by replacing \(\omega\) with \(-\omega\). Define the sign involution \((Tf)(x,s)=f(x,-s)\). Direct substitution gives \(L^*=TLT\). Because the stationary measure is invariant under \(T\), the time-reversed stationary joint process has the same law as the forward process with every sign flipped. Projecting away the sign makes these laws identical. Therefore for every integer \(n\ge1\), every \(0\le t_1<\cdots<t_n\le T\), and every bounded measurable test function, the position vectors at \((t_1,\ldots,t_n)\) and \((T-t_n,\ldots,T-t_1)\) have the same law (at stationarity). This is the full finite-dimensional path-reversibility statement, not merely zero mean circulation.

**4. Necessity.** If \(a\ne b\), stationarity gives \(\mathbb ES=(b-a)/(a+b)\). The mean oriented Stratonovich area growth per time equals
\[
\lim_{T\to\infty}T^{-1}\mathbb E\int_0^T(X_t^1\circ dX_t^2-X_t^2\circ dX_t^1)
=\omega\,\mathbb E[S|X|^2]
=\frac{2D\omega(b-a)}{k(a+b)}\ne0.
\]
The cross-noise Stratonovich corrections vanish for isotropic independent Brownian coordinates. Reversal changes the sign of this oriented area functional; a stationary reversible position path cannot have a nonzero rate. Equivalently \(\frac{d}{dt}|_{0+}(\mathbb E[X_t^2X_0^1]-\mathbb E[X_t^1X_0^2])=2D\omega(b-a)/[k(a+b)]\). This establishes the converse for all positive rates.

**5. Exact two-time law, non-Markovianity and nonlinear visibility.** Assume \(a=b=\lambda\), and put \(\Theta_t=\omega\int_0^tS_u\,du\). The conditional transition formula is \(X_t=e^{-kt}R(\Theta_t)X_0+N_t\), with \(N_t\), conditional on the sign path, centered Gaussian and independent of \(X_0\). Symmetry forces \(\mathbb E\sin\Theta_t=0\). Let \(m_v(t)=\mathbb E\cos(v\int_0^t S_u\,du)\) for \(v>0\). Conditioning on the two-state chain gives the exact initial-value problem
\[
m_v''+2\lambda m_v'+v^2m_v=0,\quad m_v(0)=1,\quad m_v'(0)=0.
\]
Thus \(\mathbb E[X_tX_0^{\mathsf T}]=q e^{-kt}m_\omega(t)I_2\). For \(\lambda>\omega\), letting \(z=\sqrt{\lambda^2-\omega^2}\),
\[
m_\omega(t)=e^{-\lambda t}[\cosh(zt)+(\lambda/z)\sinh(zt)].
\]
At \(\lambda=\omega\), \(m_\omega(t)=e^{-\lambda t}(1+\lambda t)\); for \(\lambda<\omega\), use \(z=\sqrt{\omega^2-\lambda^2}\) and replace the bracket by \(\cos(zt)+(\lambda/z)\sin(zt)\). In the last regime, the diagonal stationary position covariance changes sign infinitely often despite exact path reversibility.

Were the observed stationary position process Markov, its linear conditional expectation \(\mathbb E[X_t\mid X_0=x]=e^{-kt}m_\omega(t)x\) would obey the composition law \(m_\omega(t+u)=m_\omega(t)m_\omega(u)\). But \(m_\omega'(0)=0\) and \(m_\omega''(0)=-\omega^2<0\); no continuous multiplicative function can satisfy both. Hence it is strictly non-Markov for every finite \(\lambda>0\).

For non-Gaussianity, conditional on \(\Theta_t\), Isserlis' identity gives \(\operatorname{Cov}((X_t^1)^2,(X_0^2)^2\mid\Theta_t)=2q^2e^{-2kt}\sin^2\Theta_t\). Conditional means of both squares equal \(q\), so averaging yields
\[
\operatorname{Cov}((X_t^1)^2,(X_0^2)^2)
=q^2e^{-2kt}[1-m_{2\omega}(t)]>0\quad (t>0).
\]
The strict inequality follows because, with positive switching rate, the integrated telegraph sign has a continuous component on a nonempty interval, so \(\mathbb E\sin^2\Theta_t>0\). Meanwhile \(\mathbb E[X_t^1X_0^2]=0\). A centered joint Gaussian pair with this zero cross-covariance would have zero covariance of the squares; the observed two-time law is therefore not Gaussian.

**6. A complete equilibrium radial alias.** Itô's formula for \(Z_t=|X_t|^2\) eliminates the skew force \(X\cdot JX=0\) and gives the autonomous one-dimensional generator
\[
(\mathcal Ag)(z)=(4D-2kz)g'(z)+4Dz g''(z),\qquad z\ge0.
\]
Its stationary law is exponential with mean \(2D/k\); by uniqueness of the squared-Bessel/CIR diffusion martingale problem, its entire stationary temporal law coincides with the squared-radius of the *equilibrium* planar Ornstein–Uhlenbeck process \(dY=-kYdt+\sqrt{2D}\,dW\). Thus neither arbitrary radius-only data nor any time-antisymmetry statistic of the symmetric-switching position path distinguishes the hidden fixed-label dissipation. Under this specified model, however, \(\sigma\) can be inferred from the curvature \(m_\omega''(0)=-\omega^2\), so a zero observed path-entropy rate must not be described as the physical impossibility of model-based inference.

## Verification

The standalone `verify.py` tests the Gaussian stationary Fokker–Planck equation, vanishing rotational divergence, adjoint-involution identities on polynomials and both sign values, the telegraph characteristic recurrence and its first derivatives, the radial generator on three powers, the exact area-current and entropy algebra, the Wick identity, and independent matrix-exponential evaluations in oscillatory, critical and overdamped parameter regimes. Run `python verify.py`; required packages are `sympy`, `scipy`, and `numpy`. Every test is reproducible and passes. These checks corroborate the infinite-parameter mathematical argument above; finite polynomial tests or numerical comparisons alone do not prove the general theorem.

## Relationship to prior work

Cerasoli et al., arXiv:2201.04903, develop spectral diagnostics for the classical two-temperature Brownian gyrator, with no finite-rate randomly reversed torque. Di Terlizzi, Baiesi and Ritort, arXiv:2403.10442, solve the continuously driven Brownian vortex and obtain its nonequilibrium entropy production, but the fixed-direction rotational drive is distinguishable from its reverse and their model does not have sign-switching and exactly reversible projected paths. These are primary **background frameworks**, not results claimed anew.

Kawaguchi and Nakayama, arXiv:1209.6333, establish general hidden-entropy-production principles under elimination. Knight, Kaveh and Pruessner, arXiv:2507.22199, importantly already show that **symmetric hidden telegraph self-propulsion can leave an additive active-particle position trajectory exactly time reversible while the full trajectory is irreversible**. Accordingly, that qualitative phenomenon is explicitly **not claimed as novel**. Their additive-noise model does not state this state-dependent multiplicative angular-drift model, its if-and-only-if switching-rate boundary, the exact \(2\omega^2/k\) rate, the autonomous radial-law alias, or the strictly positive orthogonal squared-coordinate two-time statistic. The claimed contribution is the combined sharp analysis of this rotationally driven model. General operator-intertwining or hidden-process theorems could imply parts of the symmetry proof; determining complete priority requires independent literature review.

## Limitations

The statement assumes positive trap rate, diffusion, torque magnitude and *finite strictly positive* switching rates. It assumes isotropic Gaussian thermal noise, planar harmonic confinement and sign switching independent of the position. No result is asserted for inertial dynamics, nonlinear torques, asymmetric diffusion or a thermodynamic interpretation in which the chirality variable is declared odd under time reversal. The positive entropy rate refers to fixed-label reversal of the fully observed Markov law; its numerical value must not be presented as a parity-independent physical heat-production rate. The stationary position is not dynamically identical to an equilibrium Ornstein–Uhlenbeck process (only its complete radial process is). The broader idea that hidden telegraph propulsion can mask irreversibility predates this result; the novelty assessment concerns this precise all-parameter rotational model theorem, not the general principle. Independent priority and physical-model validation have not been carried out.

## References

1. S. Cerasoli et al., *Spectral fingerprints of non-equilibrium dynamics: The case of a Brownian gyrator*, arXiv:2201.04903 (first submitted 2022-01-13), https://arxiv.org/abs/2201.04903.
2. I. Di Terlizzi, M. Baiesi and F. Ritort, *Variance sum rule: proofs and solvable models*, arXiv:2403.10442 (first submitted 2024-03-15), https://arxiv.org/abs/2403.10442; especially Section 5.
3. K. Kawaguchi and Y. Nakayama, *Fluctuation theorem for hidden entropy production*, arXiv:1209.6333 (2012), https://arxiv.org/abs/1209.6333.
4. J. Knight, F. Kaveh and G. Pruessner, *Self-propulsion symmetries determine entropy production of active particles with hidden states*, arXiv:2507.22199 (2025), https://arxiv.org/abs/2507.22199; compare symmetric-telegraph case and Table 1.
