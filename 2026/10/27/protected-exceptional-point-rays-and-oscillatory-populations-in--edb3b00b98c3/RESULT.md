# Protected exceptional-point rays and oscillatory populations in a qutrit Arosh oscillator

## Finding

In the qutrit Arosh quantum oscillator with pumping rate \(a>0\) and nonlinear loss rate \(b>0\), the three occupation probabilities evolve autonomously, despite the production of stationary quantum coherence. Their two nonzero characteristic exponents are
\[
\lambda_{\pm}=-\frac{3a+b}{2}\pm\frac12\sqrt{a^2-6ab+b^2}.
\]
The exact **oscillatory-relaxation interval** is
\[
3-2\sqrt2<\frac ab<3+2\sqrt2.
\]
At the two bounding rays \(a/b=3\pm2\sqrt2\), the population dynamics has a nontrivial rank-one Jordan nilpotent and a genuine \(t e^{-(3a+b)t/2}\) relaxation term. These are actual non-diagonalizable points of the **full nine-dimensional quantum Liouvillian**, not merely coincidences in a fitted population rate matrix. Remarkably, the same exceptional-point rays and population responses persist under every diagonal Hamiltonian perturbation and any collection of diagonal Lindblad dephasing operators at arbitrary nonnegative rates.

For an initially vacant oscillator \(|0\rangle\langle0|\), its vacuum occupation crosses its equilibrium value infinitely often precisely inside the oscillatory interval; outside, it crosses at most once. At a bounding ray its displacement is a linear polynomial times a decaying exponential. Thus these rays separate three operationally distinct photon-count relaxation regimes while remaining invariant under arbitrary diagonal detuning and dephasing.

## Assumptions and scope

Let \(\mathcal H_3=\operatorname{span}\{|0\rangle,|1\rangle,|2\rangle\}\). Let \(c|n\rangle=\sqrt n|n-1\rangle\), \(c^\dagger|2\rangle=0\), and \(x=(c+c^\dagger)/\sqrt2\). Write \(\mathcal D[L](\rho)=L\rho L^\dagger-\{L^\dagger L,\rho\}/2\). Consider all quantum Markov generators
\[
\mathcal L(\rho)=-i[H,\rho]+a\mathcal D[c^\dagger](\rho)+b\mathcal D[xc](\rho)+\sum_{j=1}^{m}d_j\mathcal D[F_j](\rho),
\]
where \(a,b>0\), \(H=\operatorname{diag}(h_0,h_1,h_2)\) is any Hermitian diagonal matrix, each \(F_j\) is any complex diagonal matrix, \(d_j\ge0\), and \(m\ge0\) is arbitrary finite. Oscillator units are chosen so that the source's baseline is \(H=\operatorname{diag}(0,1,2)\) and all \(d_j=0\). There is no assumption that the initial state is diagonal.

Let \(p(t)=(\rho_{00}(t),\rho_{11}(t),\rho_{22}(t))^\top\). Denote \(K=\begin{psmallmatrix}-a&0&b\\a&-2a&0\\0&2a&-b\end{psmallmatrix}\), \(\pi=(2b,b,2a)^\top/(2a+3b)\), \(\Pi=\pi\mathbf1^\top\), \(Q=I_3-\Pi\), and \(m_0=(3a+b)/2\). The matrix \(Q\) is the spectral complement of the stationary population projection.

## Proof

**Autonomous occupation quotient.** In the qutrit basis, \(c^\dagger\) has nonzero entries \((1,0)=1\) and \((2,1)=\sqrt2\), while \(xc\) has \((1,1)=1/\sqrt2\), \((0,2)=1\), and \((2,2)=\sqrt2\). Consequently the gain dissipator contributes transitions \(0\to1\) at rate \(a\) and \(1\to2\) at rate \(2a\). The nonlinear loss jump contributes \(2\to0\) at rate \(b\) (its diagonal entries induce no population transfer). Both the diagonal Hamiltonian and every diagonal dephasing jump have zero diagonal action on every density operator. Therefore \(\dot p=Kp\) for **all** initial states, with no unproved diagonal-state invariance assumption. The invariant stationary distribution is \(K\pi=0\) and \(\mathbf1^\top\pi=1\).

**Exact population spectrum.** Direct expansion yields
\[
\det(zI_3-K)=z\bigl[z^2+(3a+b)z+2a^2+3ab\bigr].
\]
The two other roots have discriminant \(\Delta=a^2-6ab+b^2=b^2[(a/b)-(3-2\sqrt2)][(a/b)-(3+2\sqrt2)]\). In particular, the exponents are complex conjugates only between the two stated rays. The zero eigenvalue is simple at all positive rates.

**Exact evolution including the boundaries.** Set \(B=K+m_0Q\), and let \(\omega^2=\Delta/4\). The characteristic identity on the zero-sum plane is \(B^2=\omega^2Q\), while \(BQ=QB=B\) and \(\Pi B=B\Pi=0\). Thus, with analytic continuation at \(\omega=0\),
\[
 e^{tK}=\Pi+e^{-m_0t}\left[\cosh(\omega t)Q+\frac{\sinh(\omega t)}{\omega}B\right].
\]
When \(\Delta<0\), writing \(\Omega=\sqrt{-\Delta}/2\) turns the hyperbolic functions into \(\cos(\Omega t)\) and \(\sin(\Omega t)/\Omega\). When \(\Delta=0\), the exact formula is
\[
 e^{tK}=\Pi+e^{-m_0t}(Q+tB),\qquad B^2=0,\ B\ne0.
\]
At either boundary, \(K+m_0I_3\) has rank \(2\): its minor from rows \(0,1\) and columns \(0,2\) is \(-ab\ne0\), while its determinant vanishes; hence the repeated nonstationary eigenvalue has geometric multiplicity one and yields a genuine size-two Jordan block. At all other positive ratios the population matrix has three distinct eigenvalues.

**Witness and structural protection.** For \(p(0)=(1,0,0)^\top\), the vacuum deviation is a nonzero oscillatory combination \(e^{-m_0t}(A\cos\Omega t+C\sin\Omega t)\) if \(\Delta<0\), because \(A=1-\pi_0>0\). It consequently changes sign infinitely often. For \(\Delta>0\) it is a combination of two distinct real decaying exponentials and hence has at most one zero. At \(\Delta=0\) it is \(e^{-m_0t}(A+Ct)\), again with at most one zero.

Finally, the diagonal-population map \(T:\mathcal B(\mathcal H_3)\to\mathbb C^3\), \(T(\rho)=\operatorname{diag}(\rho)\), is surjective and intertwines \(\mathcal L\) and \(K\): \(T\mathcal L=KT\). Its kernel is invariant, so \(K\) is the induced linear transformation of the **full Liouvillian** on the quotient by \(\ker T\). Every quotient of a diagonalizable linear operator is diagonalizable (its minimal polynomial divides the original square-free minimal polynomial). Thus defective \(K\) forces defective \(\mathcal L\), independently of the values of the diagonal Hamiltonian and pure-dephasing terms. No assertion is made that these are the only exceptional points in the rest of the full Liouvillian spectrum.

## Verification

The standalone \(\texttt{verification.py}\) independently builds the full nine-dimensional GKSL matrix from the three-dimensional jump matrices, verifies that projection to occupations intertwines with \(K\), compares population propagators with full matrix exponentials, and checks both rank-two Jordan conditions and the analytic closed propagator across many positive rates. It passed \(1,820\) finite assertions. The exact classification follows from the analytic characteristic polynomial, Cayley–Hamilton identity, and quotient argument, not finite enumeration.

## Relationship to prior work

Chattopadhyay–Pendse–Gupta (arXiv:2610.19904v1, 14 October 2026) introduce the finite Arosh oscillator and compute its stationary qutrit state and Wigner profile. The present claim concerns the **entire transient population semigroup**, two exact real-to-complex spectral transitions, and their persistence as Liouvillian exceptional points under arbitrary diagonal detuning and dephasing. These statements are not present in the inspected qutrit stationary-state sections of that paper. A distinct prior exact analysis of the **stationary Wigner-negativity topology** of the same model concerns the geometry of a static phase-space quasidistribution; its claim does not imply this time-dependent propagator or perturbation-protected Jordan property.

Tay (arXiv:2304.05792) establishes Liouvillian exceptional points and Jordan behavior in different continuous-variable oscillator master equations. Larson–Qvarfort (arXiv:2306.12322) investigates exceptional points in periodically driven qubit Lindblad systems. General three-state cyclic Markov theory supplies useful algebraic context; the possibility of a more general published quotient-protection theorem subsuming the present specialized claim remains an originality risk.

## Limitations

The result is exact for a **three-level truncation**, not for the untruncated Arosh oscillator. It concerns occupation observables and two identifiable branches of the Liouvillian spectrum, not a classification of the entire nine-dimensional spectrum, its global gap, or all possible exceptional points. Protection holds for diagonal Hamiltonian terms and diagonal dephasing jumps, not arbitrary coherent drives or dissipators that couple occupation populations differently. The Jordan term is a transient signature, not a nondecaying quantum mode. Independent external audit has not been performed.

## References

1. R. Chattopadhyay, V. Pendse, S. Gupta, *Single and coupled quantum van der Pol oscillators: Wigner-function dynamics, exact qutrit solutions, and synchronization*, arXiv:2610.19904v1 (first public 2026-10-14), https://arxiv.org/abs/2610.19904.
2. B. A. Tay, *Liouvillian exceptional points in continuous variable system*, arXiv:2304.05792 (2023), https://arxiv.org/abs/2304.05792.
3. J. Larson and S. Qvarfort, *Exceptional points and exponential sensitivity for periodically driven Lindblad equations*, arXiv:2306.12322 (2023), https://arxiv.org/abs/2306.12322.
4. N. Ben Arosh, M. C. Cross, R. Lifshitz, *Quantum limit-cycles and the Rayleigh and van der Pol oscillators*, arXiv:2011.02706 (2020), https://arxiv.org/abs/2011.02706.
