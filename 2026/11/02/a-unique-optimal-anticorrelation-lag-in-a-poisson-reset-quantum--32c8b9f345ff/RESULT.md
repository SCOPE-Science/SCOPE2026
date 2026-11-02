# A unique optimal anticorrelation lag in a Poisson-reset quantum Bose gas

## Finding

For the stationary center-quench harmonic Bose gas defined below, the connected two-time cross-particle position covariance is, for every \(h\ge 0\),
\[
C(h)=\frac{4a^2 e^{-rh}}{(q^2+1)^2(q^2+4)}
\big[(5q^2+2)\cos(\omega h)+q(2q^2-1)\sin(\omega h)\big],\qquad q=\frac r\omega>0.
\]
The equal-time correlation is strictly positive, but the lagged correlation changes sign infinitely often. Its first positive zero is
\[
h_0(q)=\frac1\omega\left[\frac\pi2+\arctan\frac{q(2q^2-1)}{5q^2+2}\right].
\]
For fixed trap frequency, the first negative-correlation onset is earliest at one and only one positive reset-rate ratio,
\[
q_*=\sqrt{\frac{3\sqrt{41}-17}{20}}=0.332368222931927\ldots,
\qquad \omega h_0(q_*)=1.46969205192847\ldots.
\]
In contrast, the already-studied equal-time cross-particle covariance is greatest at
\[
q_{\mathrm{static}}=\sqrt{\frac{3\sqrt{21}-13}{10}}=0.273445988244026\ldots<q_*.
\]
Thus the protocol that maximizes instantaneous collective positional correlation is distinct from the one that produces the earliest temporal anticorrelation. The covariance and the first-zero result hold for any particle count \(N\ge2\) and are independent of the oscillator ground-state width.

## Assumptions and scope

Let \(N\ge2\) noninteracting identical bosons occupy a one-dimensional harmonic potential, with mass \(m>0\), frequency \(\omega>0\), initial oscillator center \(+a\) for \(a>0\), and oscillator ground state \(\rho_0=(|\psi_0\rangle\langle\psi_0|)^{\otimes N}\). Each free-evolution interval uses the Hamiltonian
\[
H=\sum_{j=1}^N\left[\frac{p_j^2}{2m}+\frac12m\omega^2(x_j+a)^2\right].
\]
At independent Poisson epochs of rate \(r>0\), all bosons are simultaneously prepared anew in \(\rho_0\). The re-preparation is idealized as instantaneous. Let \(\mathcal T_h\) be the trace-preserving reset quantum channel over lag \(h\) and let \(\rho_*\) be its stationary density matrix. For distinct tensor factors \(i\ne j\), define the ordered quantum-regression correlator
\[
C(h)=\operatorname{Tr}[x_j\mathcal T_h(x_i\rho_*)]-\operatorname{Tr}[x_i\rho_*]\operatorname{Tr}[x_j\rho_*].
\]
Because the observables act on different factors and every conditioned state is a tensor product, the answer is real. Its symmetric average over ordered distinct pairs is permutation invariant and is the off-diagonal moment of the collective two-time position-density correlator. This is **not** a same-particle autocorrelation or an assertion about strongly invasive simultaneous position measurements on the entire gas.

## Proof

**1. Conditional coherent-state means.** The Gaussian ground state remains a coherent Gaussian state under a harmonic center quench. At time \(t\ge0\) since re-preparation, the position of any factor has mean
\[
m(t)=a(2\cos(\omega t)-1).
\]
The conditioned many-boson state is a tensor product. The stationary backward reset age \(A\) is exponentially distributed with rate \(r\); hence
\[
\rho_*=r\int_0^\infty e^{-rt}U_t\rho_0U_t^\dagger\,dt,
\qquad U_t=e^{-iHt/\hbar}.
\]

**2. Exact time-regression reduction.** For any trace-class \(B\) for which the indicated moments exist, splitting trajectories according to whether a reset occurs before time \(h\) yields
\[
\mathcal T_h(B)=e^{-rh}U_hBU_h^\dagger+r\operatorname{Tr}(B)\int_0^h e^{-rt}U_t\rho_0U_t^\dagger\,dt.
\]
The no-reset term in \(\operatorname{Tr}[x_j\mathcal T_h(x_i\rho_*)]\) equals \(e^{-rh}\mathbb E[m(A)m(A+h)]\) because \(i\ne j\). The reset term contributes \(\mathbb E[m(A)]r\int_0^h e^{-rt}m(t)dt\). Since the future stationary mean is \(\mathbb E[m(A)]\), cancellation gives the exact identity
\[
C(h)=e^{-rh}\operatorname{Cov}(m(A),m(A+h)),\qquad A\sim\operatorname{Exp}(r).
\]
This establishes the quantum meaning of the two-time observable; an unrelated i.i.d. sampling of stationary snapshots would incorrectly give zero at positive lags.

**3. Exponential-age trigonometry.** Write \(q=r/\omega\). Direct Laplace integration gives
\[
\begin{aligned}
\mathbb E\cos(\omega A)&=\frac{q^2}{q^2+1},&
\mathbb E\sin(\omega A)&=\frac q{q^2+1},\\
\mathbb E\cos^2(\omega A)&=\frac12\left(1+\frac{q^2}{q^2+4}\right),&
\mathbb E[\sin(\omega A)\cos(\omega A)]&=\frac q{q^2+4}.
\end{aligned}
\]
Therefore, with \(D_q=(q^2+1)^2(q^2+4)>0\),
\[
\operatorname{Var}(\cos\omega A)=\frac{5q^2+2}{D_q},\quad
\operatorname{Cov}(\cos\omega A,\sin\omega A)=\frac{q(1-2q^2)}{D_q}.
\]
Substitution into \(\cos(\omega(A+h))=\cos(\omega A)\cos(\omega h)-\sin(\omega A)\sin(\omega h)\) proves the displayed covariance.

**4. Every zero and the sharp optimum.** Set
\[
\eta(q)=\frac{q(2q^2-1)}{5q^2+2}.
\]
Dividing by the strictly positive zero-lag covariance shows \(C(h)/C(0)=e^{-rh}[\cos(\omega h)+\eta(q)\sin(\omega h)]\). Hence its positive zeros are exactly
\[
h_k(q)=\omega^{-1}\big[\pi/2+\arctan\eta(q)+k\pi\big],\qquad k=0,1,2,\ldots,
\]
with alternating strict signs on consecutive open intervals. Direct differentiation yields
\[
\eta'(q)=\frac{10q^4+17q^2-2}{(5q^2+2)^2}.
\]
The numerator is strictly increasing as a function of \(q^2\) on the positive axis, begins negative and tends positive infinity. Thus \(\eta\), and hence every \(h_k\), has exactly one strict global minimum at the positive radical \(q_*\) stated above. The sine coefficient itself changes sign at \(q=1/\sqrt2\), where the first zero occurs at exactly one-quarter oscillator period. Finally,
\[
\frac{d}{dq}\frac{5q^2+2}{D_q}=
-\frac{4q(5q^4+13q^2-1)}{(q^2+1)^3(q^2+4)^2},
\]
which proves the unique equal-time maximizer \(q_{\mathrm{static}}\). To see its strict separation from \(q_*\), the increasing polynomials \(5z^2+13z-1\) and \(10z^2+17z-2\) have positive zeros strictly below and above \(z=1/10\), respectively.

## Verification

The accompanying `CHECKER.py` evaluates the stationary-age covariance by independent numerical quadrature, tests 30 parameter-lag combinations against the closed form, checks the analytic first zero and its sign change, compares the exact optimum with a numerical minimizer, and performs a one-million-sample event-driven reset-age Monte Carlo check. The exact proof above, not the finite tests, establishes the all-parameter statement. The checker uses Python, NumPy, SciPy and their standard numerical APIs and prints a single PASS summary on success.

## Relationship to prior work

Kulkarni, Majumdar and Sabhapandit (arXiv:2407.20342, first public 2024-07-29) established the center-quench bosonic reset model, stationary conditional-product law, equal-time position correlations, and spatial counting/order statistics. Those premises are credited. The result here concerns the **ordered stationary two-time off-diagonal correlator** and a unique rate optimizing its first sign reversal; these do not follow from the equal-time covariance alone without temporal regression.

Magoni, Carollo, Perfetto and Lesanovsky (arXiv:2202.12655) study reset-induced collective quantum correlations in coherent spin systems rather than this Bose-gas observable. Mesquita, Kulkarni, Majumdar and Sabhapandit (arXiv:2509.00487) study a distinct frequency-quench Bose gas primarily through stationary spatial observables. Kohnen and Nyman (Phys. Rev. A 91, 033612, 2015) analyze thermal Bose-gas spatiotemporal density coherence without global Poisson re-preparation. General quantum resetting renewal channels are prior technique; none of the inspected model-specific results was found to give the exact first-zero optimization above.

## Limitations

This is a position-based connected **two-time** quantum-regression observable, not a claim about entanglement, same-particle two-time noise, a Markovian position-trajectory interpretation of continuous projective measurements, or response to measurement backaction. Only instantaneous joint Poisson re-preparation, the noninteracting displaced harmonic trap, and \(r,\omega,a>0\) are treated. The zero-reset limit refers to \(r\downarrow0\) and not a stationary distribution at \(r=0\). Finite-noise estimation and experimental attainability of the ideal reset protocol are not established. Publication-priority exclusion beyond the inspected sources is not independently guaranteed.

## References

1. M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Dynamically emergent correlations in bosons via quantum resetting*, arXiv:2407.20342v1 (2024), https://arxiv.org/html/2407.20342v1.
2. N. Mesquita, M. Kulkarni, S. N. Majumdar and S. Sabhapandit, *Dynamically generated correlations in a trapped bosonic gas via frequency quenches*, arXiv:2509.00487v1 (2025), https://arxiv.org/html/2509.00487v1.
3. M. Magoni, F. Carollo, G. Perfetto and I. Lesanovsky, *Emergent quantum correlations and collective behavior in non-interacting quantum systems subject to stochastic resetting*, arXiv:2202.12655 (2022), https://arxiv.org/abs/2202.12655.
4. M. Kohnen and R. A. Nyman, *Temporal and spatiotemporal correlation functions for trapped Bose gases*, Phys. Rev. A **91**, 033612 (2015), https://doi.org/10.1103/PhysRevA.91.033612.
