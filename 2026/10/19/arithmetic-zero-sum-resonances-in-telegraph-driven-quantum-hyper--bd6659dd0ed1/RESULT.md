# Arithmetic zero-sum resonances in telegraph-driven quantum hypercubes

## Finding
For a continuous-time quantum walker started at the origin of a weighted binary hypercube and driven by **one shared symmetric random-telegraph fluctuator**, the complete long-time vertex law is determined by the signed zero sums of the coordinate hopping strengths. Let \(n\ge1\), \(h_j>0\) for \(1\le j\le n\), and let the fluctuator flip sign at rate \(\lambda>0\). For every nonempty \(T\subseteq[n]\), define
\[
 N_T=\#\{\varepsilon\in\{-1,1\}^{T}:\sum_{j\in T}\varepsilon_jh_j=0\},\qquad N_\varnothing=1.
\]
The limiting observed vertex law \(P_\infty\), indexed by \(z\in\{0,1\}^n\), is
\[
 \boxed{P_\infty(z)=2^{-n}\sum_{T\subseteq[n]}(-1)^{\sum_{j\in T}z_j}\frac{N_T}{2^{|T|}}.}
\]
It is uniform **if and only if** no nonzero signed vector \(\eta\in\{-1,0,1\}^n\) satisfies \(\sum_j\eta_jh_j=0\). This criterion holds although the temporal noise is perfectly common to all coordinates. In particular it holds for superincreasing strengths \(h_j>\sum_{i<j}h_i\), and outside a finite union of proper hyperplanes in the positive weight orthant.

A second conclusion determines the exact exponential rate of convergence to this limiting law. Put
\[
 \delta=\min\{\left|\sum_j\eta_jh_j\right|>0:\eta\in\{-1,0,1\}^n\},\quad
 q_\lambda(\delta)=\lambda-\operatorname{Re}\sqrt{\lambda^2-4\delta^2}.
\]
The finite set is nonempty and thus \(\delta>0\). With total variation \(\|P-Q\|_{\mathrm{TV}}=\frac12\sum_z|P(z)-Q(z)|\),
\[
 \boxed{\limsup_{t\to\infty}\frac1t\log\|P_t-P_\infty\|_{\mathrm{TV}}=-q_\lambda(\delta).}
\]
The unique switching rate maximizing this asymptotic relaxation exponent is \(\lambda=2\delta\), and the maximum is \(2\delta\). The limsup is necessary: in the underdamped regime, oscillatory cancellation can occur at individual times.

The three-dimensional example \((h_1,h_2,h_3)=(1,2,3)\) has perfectly uniform single-bit and two-bit marginals but a nonuniform joint limit:
\[
 \boxed{P_\infty(z)=\frac18\left[1+\frac14(-1)^{z_1+z_2+z_3}\right].}
\]
Consequently the even-parity vertices each have probability \(5/32\), the odd-parity vertices each have probability \(3/32\), and the total-variation distance to uniform is \(1/8\). This is an exact higher-order correlation invisible to every pair of coordinate measurements.

For fixed \(\lambda>0\) and \(0<\epsilon<\min\{\tfrac12,\tfrac\lambda2\}\), perturb the strengths to \((1,2,3+\epsilon)\). The limiting vertex law becomes uniform, yet
\[
 \boxed{\|P_t-U\|_{\mathrm{TV}}\sim\frac{1}{16}\left(1+\frac{\lambda}{\sqrt{\lambda^2-4\epsilon^2}}\right)e^{-q_\lambda(\epsilon)t}\quad(t\to\infty),}
\]
where \(U\) denotes the uniform law. In particular \(q_\lambda(\epsilon)\sim2\epsilon^2/\lambda\) as \(\epsilon\downarrow0\), so the slow mixing scale diverges quadratically with inverse detuning. The limits of vanishing detuning and infinite time do not commute.

## Assumptions and scope
The Hilbert space is \((\mathbb C^2)^{\otimes n}\), with computational vertex basis \(\{|z\rangle:z\in\{0,1\}^n\}\). The weighted adjacency Hamiltonian is \(H_0=\sum_{j=1}^n h_jX_j\), with \(X_j\) the Pauli bit-flip on the \(j\)-th tensor factor. The classical process \(\xi(t)\in\{-1,1\}\) starts in its stationary symmetric law and flips at the times of an independent Poisson clock of rate \(\lambda\). The stochastic Hamiltonian is \(H(t)=\xi(t)H_0\); the walker starts in \(|0^n\rangle\). At time \(t\ge0\), \(P_t(z)\) is the position-basis measurement probability after averaging the density operator over the telegraph trajectories. All limits are for these **ensemble-averaged site probabilities**, not an assertion that the full averaged density matrix converges to the maximally mixed state, nor about individual noise trajectories.

## Proof
**Commuting propagation.** Since \([H(s),H(t)]=0\) for all times, write \(S_t=\int_0^t\xi(s)\,ds\) and \(U_\xi(t)=e^{-iS_tH_0}=\bigotimes_{j=1}^ne^{-ih_jS_tX}\). Conditional on \(S_t\), the site bits are independent, with \(\Pr(Z_j=1\mid S_t)=\sin^2(h_jS_t)\). Thus the parity expectation is \(\mathbb E[(-1)^{Z_j}\mid S_t]=\cos(2h_jS_t)\).

**The fluctuator transform.** Put \(\Phi_t(\omega)=\mathbb E[e^{2i\omega S_t}]\). If \(v_+(t)\), \(v_-(t)\) are the two sign-conditioned transforms, their exact forward equations are
\[
 \frac{d}{dt}\binom{v_+}{v_-}=
 \begin{pmatrix}2i\omega-\lambda&\lambda\\\lambda&-2i\omega-\lambda\end{pmatrix}\binom{v_+}{v_-},\qquad v_\pm(0)=\frac12.
\]
Summing gives \(\Phi_t''+2\lambda\Phi_t'+4\omega^2\Phi_t=0\), with \(\Phi_0=1\) and \(\Phi'_0=0\). Its exact solution is
\[
 \Phi_t(\omega)=e^{-\lambda t}\left[\cosh\big(t\sqrt{\lambda^2-4\omega^2}\big)+\lambda t\,\operatorname{sinhc}\big(t\sqrt{\lambda^2-4\omega^2}\big)\right],
\]
where \(\operatorname{sinhc}(w)=\sinh(w)/w\), continuously extended at zero. This expression is real, even in \(\omega\), and includes both overdamped and underdamped regimes. At the double root it equals \((1+\lambda t)e^{-\lambda t}\); for \(\omega=0\) it equals one. For every fixed \(\omega\ne0\) it converges exponentially to zero.

**Exact Fourier inversion and zero-sum classification.** Let \(Y_j=(-1)^{Z_j}\) and \(M_T(t)=\mathbb E[\prod_{j\in T}Y_j]\). The elementary product-to-sum identity gives
\[
 M_T(t)=2^{-|T|}\sum_{\varepsilon\in\{-1,1\}^{T}}\Phi_t\left(\sum_{j\in T}\varepsilon_jh_j\right),\qquad M_\varnothing(t)=1.
\]
Taking limits yields \(M_T(\infty)=N_T/2^{|T|}\). Walsh orthogonality yields \(P_t(z)=2^{-n}\sum_T(-1)^{\sum_{j\in T}z_j}M_T(t)\), proving the first boxed formula. The limit is uniform precisely when all its nontrivial Walsh moments vanish. Since every \(N_T\) is a nonnegative integer, this occurs precisely when all nonempty signed support sums are nonzero, equivalently the stated \(\{-1,0,1\}\) dissociation condition.

**Sharp exponential exponent.** The finitely many nonzero arguments in all Walsh moments are precisely the positive magnitudes of nonzero signed subset sums. The telegraph transform at frequency magnitude \(\omega>0\) has upper exponential decay rate \(-[\lambda-\operatorname{Re}\sqrt{\lambda^2-4\omega^2}]\), including a harmless polynomial factor at the critical root. This decay exponent is nondecreasing in \(\omega\), giving the upper total-variation bound with exponent \(-q_\lambda(\delta)\).

Choose a nonempty support \(T\) and signs realizing \(|\sum_{j\in T}\varepsilon_jh_j|=\delta\). The difference \(M_T(t)-M_T(\infty)\) is a sum of telegraph transforms over only nonzero signed sums, with strictly positive coefficients. When \(\lambda>2\delta\), the slowest real exponential \(e^{-q_\lambda(\delta)t}\) has a strictly positive coefficient and all larger frequencies decay strictly faster. When \(\lambda=2\delta\), the term \(t e^{-\lambda t}\) has positive coefficient and dominates oscillatory terms of order \(e^{-\lambda t}\). When \(0<\lambda<2\delta\), all nonzero terms are \(e^{-\lambda t}\) times finite real trigonometric polynomials; at least one nonzero Fourier coefficient survives because every equal-frequency coefficient is positive. The mean-square of this nonzero trigonometric polynomial has a strictly positive limit, ensuring a sequence of arbitrarily large times with amplitude bounded below. In every regime, \(\limsup t^{-1}\log|M_T(t)-M_T(\infty)|=-q_\lambda(\delta)\). Since \(|M_T(t)-M_T(\infty)|\le2\|P_t-P_\infty\|_{\mathrm{TV}}\), the reverse bound follows.

For \(0<\lambda\le2\delta\), \(q_\lambda(\delta)=\lambda\); for \(\lambda>2\delta\), \(q_\lambda(\delta)=\lambda-\sqrt{\lambda^2-4\delta^2}\), which is strictly decreasing in \(\lambda\). Thus its unique maximum is attained at \(\lambda=2\delta\).

**Three-way correlation and near-resonance coefficient.** At strengths \((1,2,3)\), the only nontrivial zero-sum signs have support \(T=\{1,2,3\}\), with two choices \(1+2-3=0\) and its negative. Hence \(M_{123}(\infty)=2/8=1/4\), while every other nontrivial Walsh moment vanishes. Walsh inversion gives the parity-biased joint law and its uniform lower-order marginals.

For \((1,2,3+\epsilon)\) with \(0<\epsilon<1/2\), all nontrivial signed sums are nonzero and the smallest magnitude is \(\epsilon\). The triple moment is exactly
\[
 M_{123}(t)=\frac14[\Phi_t(\epsilon)+\Phi_t(2+\epsilon)+\Phi_t(4+\epsilon)+\Phi_t(6+\epsilon)].
\]
All other nonconstant Walsh moments have frequencies at least \(1\), so decay at a strictly faster exponent than \(q_\lambda(\epsilon)\). Because \(\lambda>2\epsilon\), the leading term of \(\Phi_t(\epsilon)\) is \(\frac12(1+\lambda/\sqrt{\lambda^2-4\epsilon^2})e^{-q_\lambda(\epsilon)t}\). Walsh inversion then gives the total-variation prefactor \(1/8\) times this amplitude. Expanding the square root yields \(q_\lambda(\epsilon)\sim2\epsilon^2/\lambda\), while at \(\epsilon=0\) the nonuniform stationary parity moment survives. This proves the noncommuting limits.

## Verification
The accompanying Python verifier uses two independent routes: (i) direct matrix exponentiation of the block generator for the telegraph-conditioned quantum density matrices, followed by site-diagonal extraction, and (ii) the closed-form fluctuator transform and Walsh inversion. It compares 96 site probabilities for several two- and three-coordinate weight configurations and switching rates, with maximum absolute discrepancy below \(6\times10^{-16}\). It separately checks five exact limiting profiles, the three-way parity bias, a long-time near-resonance prefactor, and seven trial rates around the analytic unique optimum. Run `python verify.py` with the dependencies listed in `requirements.txt`. Finite tests support, but do not replace, the full proof for arbitrary \(n\) and positive real weights.

## Relationship to prior work
Moore and Russell [1] study coherent walks on homogeneous hypercubes and their long-time mixing properties. Wold and collaborators [2] give the two-state telegraph-noise transform for qubit decoherence. Benedetti and collaborators [3] study stochastic tunneling on one-dimensional lattices with *independent* link fluctuators and noncommuting dynamical Hamiltonians; their analytical and numerical statements do not specialize to the present common-fluctuator, weighted-hypercube Fourier moments. Rossi and collaborators [4] analyze spatially correlated dynamical noise on one-dimensional lattices, not the exact signed-zero-sum criterion or its optimal asymptotic gap. The new claim concerns the signed-arithmetic classification of the *ensemble-averaged position law*, its sharp convergence exponent, and higher-order invisible-to-pairs resonance. The standard telegraph transform, Walsh inversion, and deterministic homogeneous hypercube dynamics themselves are not claimed as novel.

## Limitations
The model assumes exactly one globally shared stationary symmetric telegraph process multiplying every hopping term, commuting Hamiltonians, no on-site disorder, no independent environmental channels, and a vertex-localized pure input. Long-time position mixing does not imply convergence of the full quantum density operator to a completely mixed state. The rate is an asymptotic logarithmic limsup, not a uniform nonoscillatory mixing bound at every time. The near-resonance coefficient holds in the stated small-detuning overdamped parameter range. Finite tests do not certify infinite-dimensional statements or publication priority; a more general previously published Fourier-resonance theorem might subsume this specialization.

## References
1. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137, first public version 29 April 2001.
2. H. J. Wold, H. Brox, Y. M. Galperin, and J. Bergli, *Decoherence of a qubit due to a quantum fluctuator or to a classical telegraph noise*, arXiv:1206.2174, first public version 11 June 2012.
3. C. Benedetti, F. Buscemi, P. Bordone, and M. G. A. Paris, *Non-Markovian continuous-time quantum walks on lattices with dynamical noise*, arXiv:1510.08652, first public version October 2015.
4. M. A. C. Rossi and collaborators, *Continuous-time quantum walks on spatially correlated noisy lattices*, arXiv:1707.01441, first public version July 2017.
