# Parity-resolved Bessel entanglement crossover at weak delta-scattering transmission

## Finding

Fix a repulsive delta interaction of strength \(\gamma>0\) in the homogeneous one-dimensional coined scattering walk. At each observation size \(n\), allow its incident wavenumber \(k_n>0\) to depend on \(n\). Define \(\theta_n=\arctan(k_n/\gamma)\). Suppose \(n\to\infty\) through one fixed parity and \(n\theta_n\to\tau\in[0,\infty)\). Starting at the origin with equal, in-phase coin amplitudes, the reduced coin states converge in trace norm to

\[
\rho_{\mathrm{even}}(\tau)=\frac12\bigl[I+R_{\mathrm{even}}(\tau)\sigma_x\bigr],\qquad
\rho_{\mathrm{odd}}(\tau)=\frac12\bigl[I+R_{\mathrm{odd}}(\tau)\sigma_x\bigr],
\]
\[
R_{\mathrm{even}}(\tau)=\frac{1+B(\tau)}2,\qquad
R_{\mathrm{odd}}(\tau)=\frac{1-B(\tau)}2,\qquad
B(\tau)=\begin{cases}J_1(2\tau)/\tau,&\tau>0,\\1,&\tau=0.\end{cases}
\]

Consequently the coin–position entanglement entropy, in bits, has the parity-dependent limits

\[
\lim S_{2m}=h_2\!\left(\frac{3+B(\tau)}4\right),\qquad
\lim S_{2m+1}=h_2\!\left(\frac{3-B(\tau)}4\right),
\]

where each limit is taken along a wavenumber sequence with the stated scaled-time limit, \(J_1\) is the Bessel function of the first kind, and \(h_2(u)=-u\log_2 u-(1-u)\log_2(1-u)\), with its continuous endpoint convention.

In particular, at \(\tau=0\) the even-time entropy tends to \(0\) while the odd-time entropy tends to \(1\) bit. Both curves approach \(h_2(3/4)\) as \(\tau\to\infty\), but cross at precisely the positive zeros of \(J_1(2\tau)\). At large \(\tau\), their difference has the oscillatory envelope

\[
S_{\mathrm{even}}(\tau)-S_{\mathrm{odd}}(\tau)
=-\frac{\log_2 3}{2\sqrt\pi\,\tau^{3/2}}
\cos\left(2\tau-\frac{3\pi}{4}\right)+O(\tau^{-5/2}).
\]

Here \(S_{\mathrm{even}}(\tau)\) and \(S_{\mathrm{odd}}(\tau)\) denote the limiting functions, **not** finite-wavenumber large-time asymptotics. The stated joint limit does not assert uniform convergence at diverging \(\tau\).

## Assumptions and scope

The position space is \(\ell^2(\mathbb Z)\), the coin space is \(\mathbb C^2\), and \(\sigma_x\) is the standard Pauli matrix in the ordered basis \((|+\rangle,|-\rangle)\). The initial vector is \(|0\rangle\otimes\chi\), with \(\chi=(|+\rangle+|-\rangle)/\sqrt2\). Each step first applies the homogeneous coin inherited from a delta scatterer with \(a=d=\omega=1\), \(b=0\), \(c=2\gamma\), then shifts the plus and minus components right and left by one site, respectively. No intermediate measurements or decoherence occur. The incident wavenumber is a fixed positive parameter during any one experiment of \(n\) steps; it changes only between the experiments in the scaling sequence.

The amplitudes are \(r(k)=-\gamma/(\gamma-ik)\) and \(t(k)=-ik/(\gamma-ik)\). Since \(t(k)/r(k)=ik/\gamma\), the associated coin \(C_k=\bigl(\begin{smallmatrix}t&r\\r&t\end{smallmatrix}\bigr)\) equals, up to a common phase irrelevant to density matrices,
\[
C_{\theta}=\cos\theta\,\sigma_x+i\sin\theta\,I,
\qquad\theta=\arctan(k/\gamma).
\]

All quantifiers concern arbitrary sequences of positive wavenumbers satisfying the stated limit, along either even or odd time indices. The limit is for the reduced **coin** density operator, after tracing over position; it is not the position Shannon entropy or a many-particle entanglement entropy.

## Proof

**1. Uniform two-step limit.** Fourier-transform the position coordinate, with quasimomentum \(q\in[-\pi,\pi)\). Write \(D(q)=\operatorname{diag}(e^{iq},e^{-iq})\) and \(A(q)=D(q)\sigma_x\). Then \(A(q)\) is a Hermitian involution, \(A(q)^2=I\), and
\[
U_\theta(q)=D(q)C_\theta=\cos\theta\,A(q)+i\sin\theta\,D(q).
\]
The identity \(A(q)D(q)+D(q)A(q)=2\cos q\,A(q)\) implies
\[
U_\theta(q)^2=\cos^2\theta\,I+2i\sin\theta\cos\theta\cos q\,A(q)-\sin^2\theta\,D(q)^2
=e^{2i\theta\cos q A(q)}+O(\theta^2),
\]
where the operator-norm error is bounded by a constant times \(\theta^2\), uniformly in \(q\) for \(\theta\) near zero. Every matrix in the telescoping product is unitary, so for \(n=2m+p\), \(p\in\{0,1\}\),
\[
\sup_q\left\|U_{\theta_n}(q)^n-A(q)^p e^{i\tau\cos q A(q)}\right\|
\le C n\theta_n^2+C\theta_n+|n\theta_n-\tau|\longrightarrow0.
\]
The last step follows from \(n\theta_n\to\tau\), hence \(n\theta_n^2\to0\). Applying these multipliers to the constant Fourier initial spinor and using Plancherel gives norm convergence of the global pure states. Contractivity of partial trace and the pure-state trace-distance bound then give trace-norm convergence of the reduced coin states.

**2. Compute the limiting Bloch vector.** In Pauli notation \(A(q)=\cos q\,\sigma_x-\sin q\,\sigma_y\). The initial coin has Bloch vector \((1,0,0)\). Conjugation by \(\exp(i\tau\cos q A(q))\) rotates it around the axis \((\cos q,-\sin q,0)\), giving the \(x\) component
\[
b_{x,\mathrm{even}}(q)=\cos^2q+\sin^2q\cos(2\tau\cos q).
\]
An additional factor \(A(q)\) for odd parity reflects the component perpendicular to this axis, producing
\[
b_{x,\mathrm{odd}}(q)=\cos^2q-\sin^2q\cos(2\tau\cos q).
\]
Under \(q\mapsto-q\), the \(y\)- and \(z\)-components of both integrands are odd, and therefore integrate to zero. Since the initial position is localized, the reduced coin operator is exactly the uniform average over \(q\). Thus its only nonzero Bloch component is \(R_{\mathrm{even/odd}}\), with
\[
R_{\mathrm{even/odd}}(\tau)=\frac12\pm\int_{-\pi}^{\pi}\frac{dq}{2\pi}\sin^2q\cos(2\tau\cos q).
\]

**3. Evaluate the Bessel integral.** The standard Fourier–Bessel identities and recurrence give
\[
\int_{-\pi}^{\pi}\frac{dq}{2\pi}\sin^2q\cos(z\cos q)
=\frac{J_0(z)+J_2(z)}2=\frac{J_1(z)}{z},
\]
with continuous value \(1/2\) at \(z=0\). Substituting \(z=2\tau\) yields \(R_{\mathrm{even/odd}}=(1\pm B(\tau))/2\). The two eigenvalues of \(\frac12(I+R\sigma_x)\) are \((1\pm R)/2\). Von Neumann entropy is continuous on the two-dimensional state space, giving the displayed binary-entropy formulas.

**4. Endpoints and oscillations.** From \(J_1(z)\sim z/2\) as \(z\downarrow0\), one has \(B(0)=1\). The first four positive crossing parameters are approximately \(1.9158529851\), \(3.5077933349\), \(5.0867340675\) and \(6.6618459682\). Each zero of \(J_1\) is simple and its sign changes across consecutive positive zeros; the binary entropy is strictly decreasing on \([1/2,1]\), so these are exactly the parity-curve crossings. Finally the Bessel large-argument expansion yields \(B(\tau)=(\sqrt\pi\,\tau^{3/2})^{-1}\cos(2\tau-3\pi/4)+O(\tau^{-5/2})\). Taylor expansion of the binary entropy around \(3/4\), where \(h_2'(3/4)=-\log_2 3\), gives the stated difference.

## Verification

The standalone script `verify.py` constructs the same walk twice: from a direct position-space recurrence and from independent Fourier-space propagation. It checks 36 finite-step matrix equalities for \(0\le n\le11\) and three coin angles, sixteen quadrature/Bessel identities, and 192 normalization/symmetry/finite-size crossover checks at eight scaled times and six even/odd lengths. All 244 assertions passed with NumPy and SciPy. Numerical tests corroborate the derivation; they are not proofs of the infinite-sequence statement. The proof itself controls the uniform matrix products and evaluates the limiting integral analytically.

## Relationship to prior work

Spak dos Santos, Tsutsui and Andrade, arXiv:2609.03272v1 (first public September 3, 2026), establish the delta-scattering coin and its fixed-wavenumber spectra and long-time entanglement, including the loss of uniform decay at zero transmission. Their Eqs. (18), (24), (39)–(44) supply the physical parametrization and fixed-parameter comparison, not the moving-wavenumber parity-resolved Bessel law. Carneiro et al. (2005) numerically observed anomalous entanglement oscillation at the swap-coin endpoint; they did not give this joint scaling function. Ide, Konno and Machida (2011) treat fixed-coin long-time entanglement for arbitrary nondegenerate coins. Manighalam and Kon (2020), extending earlier work, establish the general two-step discrete-to-continuous-time quantum-walk limit. Thus the effective limiting dynamics itself is known. The result here adds a physical delta-scattering scaling identification and an explicit two-parity **reduced-state and entropy** crossover with sharp Bessel zeros and asymptotic envelope. It is not presented as a newly discovered continuous-time quantum walk.

## Limitations

Only the homogeneous delta-interaction family, the specified localized equal-phase initial coin, and finite scaled times \(\tau\) are proved. The result does not cover arbitrary initial phases, inhomogeneous scatterers, noisy dynamics, or a uniform joint limit with diverging \(\tau\). The large-\(\tau\) expansion applies to the **limiting crossover functions**, not to a finite-wavenumber walk without another uniformity proof. General two-step continuum-limit methods in prior literature make portions of the dynamical argument standard; literature-wide priority of the explicit parity-resolved Bessel entropy formula has not been independently verified.

## References

1. A. Spak dos Santos, T. T. Tsutsui and F. M. Andrade, *Discrete-time quantum walks with energy-dependent coins*, arXiv:2609.03272v1 (September 3, 2026), https://arxiv.org/html/2609.03272v1.
2. I. Carneiro et al., *Entanglement in coined quantum walks on regular graphs*, New Journal of Physics 7 (2005), 156, DOI:10.1088/1367-2630/7/1/156; https://strathprints.strath.ac.uk/78869/1/Carneiro_etal_NJP_2005_Entanglement_in_coined_quantum_walks.pdf.
3. Y. Ide, N. Konno and T. Machida, *Entanglement for discrete-time quantum walks on the line*, arXiv:1012.4164v2 (2011), https://arxiv.org/html/1012.4164v2.
4. M. Manighalam and M. Kon, *General methods and properties to evaluate continuum limits of the 1D discrete time quantum walk*, Quantum Information Processing 19 (2020), 379, DOI:10.1007/s11128-020-02880-6; https://link.springer.com/article/10.1007/s11128-020-02880-6.
