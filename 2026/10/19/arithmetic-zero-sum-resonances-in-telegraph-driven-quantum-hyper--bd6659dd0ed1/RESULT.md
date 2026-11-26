# Arithmetic zero-sum resonances in telegraph-driven quantum hypercubes

## Finding

For a weighted hypercube driven by **one common stationary symmetric telegraph sign**, the sharp total-variation relaxation exponent of the ensemble-averaged site probabilities is controlled by the smallest *nonzero* signed sum of the hopping strengths, even when exact signed-zero resonances survive in the limiting law.

Let \(n\ge1\), \(h_j>0\), and let the sign flip at the times of a rate-\(\lambda>0\) Poisson clock. Put
\[
\delta=\min\left\{\left|\sum_{j=1}^n\eta_jh_j\right|:\eta\in\{-1,0,1\}^n,\ \sum_j\eta_jh_j\ne0\right\},\qquad
q_\lambda(s)=\lambda-\operatorname{Re}\sqrt{\lambda^2-4s^2},
\]
using the square root with nonnegative real part. The set defining \(\delta\) is finite and nonempty. With \(P_t\) the ensemble-averaged site distribution from the origin, and \(\overline P\) the infinite-time Cesàro site distribution from the origin for the corresponding *clean* walk, the sharp statement is
\[
\limsup_{t\to\infty}t^{-1}\log\|P_t-\overline P\|_{\mathrm{TV}}=-q_\lambda(\delta).
\]
Here \(\|P-Q\|_{\mathrm{TV}}=\tfrac12\sum_z|P(z)-Q(z)|\) and \(\log 0=-\infty\). The unique switching rate maximizing the exponent \(q_\lambda(\delta)\) is \(\lambda=2\delta\), giving exponent \(2\delta\).

For the detuned strengths \((1,2,3+\epsilon)\), with fixed \(\lambda>0\) and \(0<\epsilon<\min(1/2,\lambda/2)\), the clean average is the uniform law \(U\), and the sharper equivalent is
\[
\|P_t-U\|_{\mathrm{TV}}\sim\frac1{16}\left(1+\frac{\lambda}{\sqrt{\lambda^2-4\epsilon^2}}\right)e^{-q_\lambda(\epsilon)t}.
\]
In this regime the exponential relaxation time grows as \(\lambda/(2\epsilon^2)\) as \(\epsilon\downarrow0\); this is a statement about the reciprocal asymptotic exponent, not a uniform-in-detuning estimate for every finite time.

## Assumptions and scope

Use the computational basis of \((\mathbb C^2)^{\otimes n}\), initial state \(|0^n\rangle\), and \(H(t)=\xi(t)H_0\) where \(H_0=\sum_jh_jX_j\) and \(X_j\) flips bit \(j\). The initial sign \(\xi(0)\) is symmetric and independent of the rate-\(\lambda\) Poisson clock. Average the measurement probabilities over sign paths. The clean walk uses \(H(t)=H_0\) and the same initial state and vertex measurement. Neither convergence of individual paths nor convergence to a maximally mixed density operator is asserted.

## Proof

Put \(S_t=\int_0^t\xi(u)\,du\). All Hamiltonians commute, so conditional propagation is \(\bigotimes_j\exp(-ih_jS_tX)\). If \(T\) is a subset of coordinates, its conditional parity mean is \(\prod_{j\in T}\cos(2h_jS_t)\). Hence its averaged parity mean is
\[
M_T(t)=2^{-|T|}\sum_{e\in\{\pm1\}^T}\Phi_t\!\left(\sum_{j\in T}e_jh_j\right),\qquad \Phi_t(s)=\mathbb E e^{2isS_t}.
\]
The transform for the two end-sign masses solves a two-component forward equation with diagonal entries \(2is-\lambda,-2is-\lambda\) and off-diagonal entries \(\lambda\). Summing and eliminating the signed difference gives \(\Phi''+2\lambda\Phi'+4s^2\Phi=0\), with \(\Phi_0=1\) and \(\Phi'_0=0\). Thus, if \(a=\sqrt{\lambda^2-4s^2}\),
\[
\Phi_t(s)=e^{-\lambda t}\left[\cosh(at)+\lambda\frac{\sinh(at)}a\right],
\]
with the bracket equal to \(1+\lambda t\) for \(a=0\). At \(s=0\) the transform is one; for \(s\ne0\) it tends to zero. In the clean walk, replace \(\Phi_t(s)\) by \(e^{2ist}\). Its Cesàro mean also selects just the zero terms. Thus the telegraph limit and clean Cesàro law coincide. For reference, the clean Walsh moment is the number of zero signed sums on \(T\) divided by \(2^{|T|}\) [1]. Only the terms with nonzero \(s\) appear in the telegraph relaxation about this law.

Each nonzero term is bounded by a constant times \((1+t)e^{-q_\lambda(|s|)t}\). The function \(q_\lambda\) is nondecreasing in its positive frequency argument. Finiteness of the Walsh sum gives the upper bound on the logarithmic limsup. For the converse select a support \(T\) attaining \(\delta\). In the overdamped case \(\lambda>2\delta\), every other frequency magnitude decays strictly faster and the coefficient of \(e^{-q_\lambda(\delta)t}\) is a sum of positive terms. At \(\lambda=2\delta\), the coefficient of \(t e^{-\lambda t}\) is positive, while other frequencies contribute \(O(e^{-\lambda t})\). In the fully underdamped case \(\lambda<2\delta\), the rescaled parity difference is a finite real trigonometric polynomial with distinct frequencies \(\sqrt{4s^2-\lambda^2}\) after grouping frequency magnitudes. Each cosine coefficient is positive. Its Cesàro mean square is positive by integrating products of distinct-frequency sinusoids, and boundedness then gives arbitrarily large times at which its absolute value is bounded below by a positive constant. In all cases the selected Fourier coefficient supplies the lower bound because its absolute difference is at most twice the total variation. This argument yields a limsup, not necessarily a limit in the underdamped case. As a function of \(\lambda\), \(q_\lambda(\delta)\) equals \(\lambda\) up to \(2\delta\), and has negative derivative on \((2\delta,\infty)\), proving the optimal switching statement.

For \((1,2,3+\epsilon)\) in the indicated range there are no nonempty zero signed sums. In the triple parity the magnitudes are \(\epsilon,2+\epsilon,4+\epsilon,6+\epsilon\), each with weight \(1/4\). Every other nonempty support has frequencies of magnitude at least one. The \(\epsilon\) term alone contributes on the slowest exponential scale; its telegraph coefficient is \(\tfrac12(1+\lambda/\sqrt{\lambda^2-4\epsilon^2})\). Taking the Walsh inverse gives the leading triple-parity bias at all eight vertices, with total variation equal asymptotically to half the absolute triple moment. Finally \(q_\lambda(\epsilon)\sim 2\epsilon^2/\lambda\).

## Verification and relationship to prior work

The bundled `verify.py` compares a telegraph-conditioned density-matrix propagator against the scalar transform and Walsh formula in finite examples, and tests one detuning example and several switching rates. These tests support the computation but do not establish the all-weight limsup, which is proved above.

The clean weighted hypercube's all-weight Cesàro profile and the signed-zero-sum uniformity criterion are already established in [1]; they are context and not claimed here as new. Moore–Russell [2] treat the clean equal-weight case. The one-frequency telegraph transform is classical and appears in the qubit model of Wold et al. [3]. The retained claim is the **common-clock total-variation rate for the whole site law**, including its underdamped lower bound, the uniquely optimal switching rate, and the explicit detuned total-variation equivalent. Lattice walks with independent links or spatially correlated domains [4,5] do not use the scalar commuting clock considered here.

This is an exact finite-dimensional theorem for the specified model, not a bound for independent hopping noise or a uniform finite-time mixing threshold. The comparison does not establish absolute publication priority.

1. *Sharp uniform averaging design for anisotropically weighted hypercubes*, [Resultary record 58400972baab](https://github.com/Resultary/2026/tree/main/2026/10/13/SCOPE-sharp-uniform-averaging-design-for-anisotropically-weighted-hype--58400972baab), Finding items 1–2 and Proof steps 1–3.
2. C. Moore and A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137, Eq. (10).
3. H. J. Wold et al., *Decoherence of a qubit due to a quantum fluctuator or to a classical telegraph noise*, arXiv:1206.2174, Eqs. (8)–(9), (12).
4. C. Benedetti et al., *Non-Markovian continuous-time quantum walks on lattices with dynamical noise*, arXiv:1510.08652, §I.
5. M. A. C. Rossi et al., *Continuous-time quantum walks on spatially correlated noisy lattices*, arXiv:1707.01441.
