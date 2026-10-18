# Critical alignment yields a sharp square-root enhancement of spatial relaxation

## Finding

At the mean-field alignment threshold of a two-velocity run-and-tumble hydrodynamic equation, each fixed nonzero spatial Fourier mode has two sharply different relaxation channels. Although the spatially uniform magnetization decays only as \(t^{-1/2}\), the dominant nonuniform channel decays as \(e^{-t+c_n\sqrt t}t^{-3/8}\), with a universal logarithmic exponent and an explicit frequency-dependent stretching coefficient.

**Theorem.** On the unit torus \(\mathbb T=\mathbb R/\mathbb Z\), let nonnegative \(C^1\) orientation densities \(\rho_\pm(x,t)\) solve, for \(t\geq0\),
\[
\partial_t\rho_+=-\partial_x\rho_+-e^{-m(t)}\rho_++e^{m(t)}\rho_-,\qquad
\partial_t\rho_-=\partial_x\rho_-+e^{-m(t)}\rho_+-e^{m(t)}\rho_-,
\]
where the conserved total mass is one and \(m(t)=\int_{\mathbb T}(\rho_+-\rho_-)\,dx\). Assume \(0<m(0)<1\). For every integer \(n\geq1\), write \(k_n=2\pi n\), \(\omega_n=\sqrt{k_n^2-1}\), and
\[
w_n(t)=\begin{pmatrix}\int_{\mathbb T}e^{-ik_nx}\rho_+(x,t)\,dx\\[2pt]
\int_{\mathbb T}e^{-ik_nx}\rho_-(x,t)\,dx\end{pmatrix}.
\]
There is a complex one-dimensional subspace \(E_n^{\mathrm{fast}}\subset\mathbb C^2\), depending only on \(m(0)\) and \(n\), such that for every \(w_n(0)\notin E_n^{\mathrm{fast}}\),
\[
\boxed{\ \|w_n(t)\|_2=C_n t^{-3/8}\exp\!\left(-t+\frac{\sqrt3\,k_n}{\sqrt{k_n^2-1}}\sqrt t\right)(1+o(1)),\quad t\to\infty,\ }
\]
with \(0<C_n<\infty\). The exceptional subspace is the unique space of initial coefficients asymptotic to the other, faster channel. In particular, the generic sharp stretching coefficient is
\[
\boxed{\ \lim_{t\to\infty}\frac{\log\|w_n(t)\|_2+t}{\sqrt t}=\frac{\sqrt3\,k_n}{\sqrt{k_n^2-1}}.\ }
\]
The set of admissible real nonnegative smooth initial orientation profiles realizing the generic behavior is open and dense *relative to profiles with positive orientation densities and fixed strictly positive mean magnetization*, at each fixed mode; the exceptional condition imposes two real linear constraints on its Fourier coefficient.

At the exactly symmetric initial state \(m(0)=0\), the magnetization stays zero and every nonzero mode instead satisfies \(\|w_n(t)\|_2\asymp e^{-t}\), with no stretched-exponential factor. For negative initial magnetization the same generic statement holds with the slow Fourier branch exchanged under orientation and reflection symmetry. No assertion of this type is made for the microscopic finite-particle process before taking its hydrodynamic limit.

## Assumptions and scope

The system is the deterministic hydrodynamic PDE of Pulvirenti, Redig and van Wiechen for two velocity states with unit ballistic speed and Curie--Weiss flip rates \(c(\sigma,m)=e^{-\sigma\beta m}\), specialized to critical coupling \(\beta=1\). Its unit torus is essential to the stated formula: every nonzero spatial wave number then obeys \(k_n>1\), avoiding the overdamped/underdamped threshold. Time is measured in units where the unbiased orientation-flip rate is one. Initial total mass is one, orientations are nonnegative, and \(0<m_0<1\). The PDE is linear in each spatial mode once the global magnetization is known, but is nonlinear through its global feedback. One can prescribe arbitrary sufficiently small complex Fourier coefficients by real sine/cosine perturbations of strictly positive constant initial densities while keeping \(m_0\) fixed.

## Proof

**1. Autonomous magnetization and its critical asymptotics.** Integrating the PDE over \(x\) gives exactly
\[
\dot m=2\sinh m-2m\cosh m=-\frac23m^3-\frac1{15}m^5+O(m^7).
\]
For \(m\in(0,1)\), \(\sinh m-m\cosh m<0\) (its derivative is \(-m\sinh m\)), hence \(m(t)\downarrow0\) and remains positive. With \(u=m^{-2}\),
\[
\dot u=\frac43+\frac{2}{15u}+O(u^{-2}),\qquad
u(t)=\frac43t+\frac1{10}\log t+O(1).
\]
The second estimate follows first from \(u(t)/t\to4/3\), then from integration of \(u'-4/3=2/(15u)+O(u^{-2})\). Consequently,
\[
m(t)=\frac{\sqrt3}{2\sqrt t}+O\!\left(\frac{\log t}{t^{3/2}}\right),\quad
\int_1^t m(s)\,ds=\sqrt3\sqrt t+C_m+o(1),\quad
\int_1^t m(s)^2\,ds=\frac34\log t+C_{m,2}+o(1).
\]
The constants depend on the strictly positive initial magnetization. Furthermore \(m'(t)=O(t^{-3/2})\), and \(\int_1^\infty m(s)^3\,ds<\infty\).

**2. The exact Fourier matrix.** At frequency \(k=2\pi n\), spatial integration yields the exact two-dimensional nonautonomous system
\[
\dot w=A_k(m(t))w,\qquad
A_k(m)=\begin{pmatrix}-ik-e^{-m}&e^m\\e^{-m}&ik-e^m\end{pmatrix}.
\]
Its eigenvalues are
\[
\lambda_\pm(m)=-\cosh m\pm\sqrt{1+(\sinh m-ik)^2}.
\]
Put \(\omega=\sqrt{k^2-1}>0\), and choose the analytic square-root branch equal to \(i\omega\) at zero. Direct Taylor expansion, using \(1+(\sinh m-ik)^2= -\omega^2-2ikm+m^2+O(m^3)\), gives
\[
\sqrt{1+(\sinh m-ik)^2}
=i\omega-\frac{k}{\omega}m+\frac{i}{2\omega^3}m^2+O(m^3).
\]
Thus the mode with the larger real part for all sufficiently large times is \(\lambda_s=\lambda_-\) (for \(m>0\)):
\[
\operatorname{Re}\lambda_s(m)=-1+\frac{k}{\omega}m-\frac12m^2+O(m^3),
\qquad \operatorname{Re}(\lambda_s-\lambda_f)=\frac{2k}{\omega}m+O(m^3)>0.
\]
The imaginary parts approach \(-\omega\) and \(+\omega\), so the eigenvalues stay distinct and separated in modulus.

**3. Asymptotic diagonalization, including the exceptional channel.** Fix a sufficiently large \(t_0\). Choose an analytic eigenvector matrix \(P(m)\) near \(m=0\), nonsingular there, with first column the slow eigenvector. Setting \(z=P(m(t))^{-1}w\) gives
\[
\dot z=\bigl(\mathrm{diag}(\lambda_s,\lambda_f)+R(t)\bigr)z,\qquad
R(t)=-P^{-1}\frac{dP}{dm}m'(t),\quad \|R(t)\|=O(t^{-3/2}).
\]
For completeness, the two-channel asymptotic-integration argument is as follows. Absorb the integrable diagonal entries of \(R\) into the diagonal exponents. The off-diagonal Volterra kernels are controlled by
\[
\exp\!\left(-\int_t^v\operatorname{Re}(\lambda_s-\lambda_f)(s)\,ds\right)
\leq \exp[-c(\sqrt v-\sqrt t)]\quad(v\geq t\geq t_0)
\]
for some \(c>0\), because \(m(t)\sim\sqrt3/(2\sqrt t)\). More explicitly, the forward-invariant slow graph \(z_f=h_s(t)z_s\) solves a Riccati equation with negative real linear coefficient \(\lambda_f-\lambda_s\). Starting at a sufficiently late \(t_0\) with \(h_s(t_0)=0\), its variation-of-constants equation and the displayed kernel yield \(h_s(t)=O(t^{-1})\). The complementary fast graph \(z_s=h_f(t)z_f\) has positive real linear coefficient \(\lambda_s-\lambda_f\); selecting the unique bounded solution by backward integration from infinity yields \(h_f(t)=O(t^{-1})\). The nonlinear graph terms are contractions because the forcing is \(O(t^{-3/2})\) and \(\int_t^\infty v^{-3/2}\exp[-c(\sqrt v-\sqrt t)]\,dv=O(t^{-1})\). On each graph the amplitude logarithmic derivative is \(\lambda_{s/f}+R_{s/f,s/f}+O(t^{-5/2})\), and the terms after \(\lambda_{s/f}\) are integrable. The graphs are independent for large time, so they yield linearly independent solutions
\[
w_s(t)=(v_s(0)+o(1))\exp\!\left(\int_{t_0}^t\lambda_s(m(s))\,ds\right),\quad
w_f(t)=(v_f(0)+o(1))\exp\!\left(\int_{t_0}^t\lambda_f(m(s))\,ds\right),
\]
with fixed nonzero limiting eigenvectors \(v_s(0),v_f(0)\). The integrable diagonal remainders alter the finite nonzero prefactors only. In particular, the growing relative separation \(\exp(\int\operatorname{Re}(\lambda_s-\lambda_f))\to\infty\) makes the slow component dominate every solution outside the one-dimensional fast-solution subspace. In the displayed Volterra estimate the absorbed bounded initial interval changes constants but not powers or exponents.

**4. Critical exponent and normalization.** The expansion from step 2 and the integrals in step 1 imply
\[
\int_{t_0}^t\operatorname{Re}\lambda_s(m(s))\,ds
=-t+\frac{\sqrt3 k}{\omega}\sqrt t-\frac38\log t+C+o(1).
\]
The \(O(m^3)\) term is integrable. The slow solution's eigenvector converges to a finite nonzero vector, and the asymptotic diagonalization provides a nonzero finite scalar coefficient. Thus its Euclidean norm is precisely a positive constant times the exponential of the preceding expression, up to \(1+o(1)\). Any solution not in the fast-solution subspace has this law. The exceptional subspace is one-dimensional because the fundamental solutions are independent. For \(m_0=0\), \(m\equiv0\), and \(A_k(0)\) is diagonalizable with eigenvalues \(-1\pm i\omega\); its oscillatory similarity transform and inverse are uniformly bounded, giving \(\|w(t)\|_2\asymp e^{-t}\) for every nonzero coefficient.

The result concerns fixed \(n\) as \(t\to\infty\); it does not assert uniformity in \(n\), finite-size microscopic fluctuations, or a spatial pointwise remainder after summing infinitely many Fourier modes. This completes the proof.

## Verification

The included standalone script `verify.py` checks the autonomous magnetization law, both Fourier equations and their eigenvalue expansions, and integrates the original coupled complex Fourier system. The implementation rescales \(w\) by \(e^t\) to avoid numerical underflow. For one positive magnetization and the first nonzero Fourier mode, it checks that
\[
\log\|e^tw_n(t)\|_2-\frac{\sqrt3k_n}{\omega_n}\sqrt t+\frac38\log t
\]
approaches a finite limit (numerical values are reported by the script). These tests check the calculation but do not replace the Volterra proof of the infinite-time assertion.

## Relationship to prior work

Pulvirenti, Redig and van Wiechen (2025 preprint; 2026 journal) rigorously derive the full nonlinear hydrodynamic PDE and its autonomous mean-field magnetization ODE; the latter yields the critical alignment threshold. The present analysis accepts both as prior results. Their hydrodynamic theorem holds on fixed finite time intervals and their paper studies trajectory large deviations. Its text does not derive fixed nonzero spatial Fourier asymptotics at the critical coupling or the square-root exponential enhancement with logarithmic prefactor.

Redig and van Wiechen (2024) address stationary fluctuations for independent and exclusion-interacting run-and-tumble systems, including limiting Gaussian-field covariances; those are not the nonstationary critical mean-field switching law studied here. Van Ginkel, van Gisbergen and Redig (2021) treat constant-rate internal Markov dynamics and its transport/diffusivity asymptotics. They do not incorporate algebraically decaying self-consistent Curie--Weiss switching. General results on asymptotic integration of linear ODEs underpin step 3; the claim is the resulting explicit, physically motivated critical spatial relaxation law, not the general ODE method.

## Limitations

The result applies to the deterministic hydrodynamic equation, on the **unit** torus, at exactly \(\beta=1\), at each fixed nonzero Fourier mode, and for strictly nonzero initial magnetization. Its sharp asymptotic holds outside an explicitly identified codimension-one exceptional solution space; it is not claimed for every Fourier perturbation. The limit \(N\to\infty\) that produces the hydrodynamic equation precedes \(t\to\infty\). The theorem does not address a full many-mode norm without smoothness/summability control or arbitrary torus lengths (where some wave numbers can be at or below the critical spectral frequency). Novelty is assessed against identified accessible sources and is not an assertion that all possible literature has been exhausted.

## References

1. E. Pulvirenti, F. Redig, and H. van Wiechen, *Hydrodynamic limit and large deviations for run-and-tumble particles with mean-field switching rates*, arXiv:2509.22254v1 (first public posting September 26, 2025); Journal of Statistical Physics **193**, 51 (2026), DOI:10.1007/s10955-026-03609-y. Main source for the PDE and the magnetization reduction.
2. F. Redig and H. van Wiechen, *Stationary Fluctuations of Run-and-Tumble Particles*, Markov Processes and Related Fields **30** (2024), 297--331, DOI:10.61102/1024-2953-mprf.2024.30.2.003.
3. B. van Ginkel, B. van Gisbergen, and F. Redig, *Run-and-Tumble Motion: The Role of Reversibility*, Journal of Statistical Physics **183**, 44 (2021), DOI:10.1007/s10955-021-02787-1.
