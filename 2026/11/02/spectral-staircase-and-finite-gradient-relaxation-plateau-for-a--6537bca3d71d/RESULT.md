# Spectral staircase and finite-gradient relaxation plateau for a saturating run-and-tumble process

## Finding
Consider a run-and-tumble particle with constant speed \(v>0\) on the whole line, whose right-to-left and left-to-right reversal rates are, respectively, \(\gamma_0+\gamma_1\tanh(gx)\) and \(\gamma_0-\gamma_1\tanh(gx)\), with \(\gamma_0>\gamma_1>0\) and gradient \(g>0\). Define \(\nu=\gamma_1/(vg)\). Its nonstationary, square-integrable density-relaxation spectrum has exactly \(\lceil\nu\rceil-1\) discrete *spatial* levels, indexed by integers \(1\le n<\nu\), each producing two decay exponents
\[
s_{n,\pm}=-\gamma_0\pm\sqrt{\gamma_0^2-v^2g^2 n(2\nu-n)}.
\]
The remaining spatial continuum begins at \(\gamma_1^2/v^2\) (in the spatial Schrödinger operator), with slow temporal spectral edge \(-\gamma_0+\sqrt{\gamma_0^2-\gamma_1^2}\). Therefore the sharp slowest nonstationary spectral decay rate is
\[
G(g)=\begin{cases}
\gamma_0-\sqrt{\gamma_0^2-2v\gamma_1g+v^2g^2},&0<g<\gamma_1/v,\\
\gamma_0-\sqrt{\gamma_0^2-\gamma_1^2},&g\ge\gamma_1/v.
\end{cases}
\]
It rises strictly with gradient until \(g=\gamma_1/v\), then *saturates exactly* at the spatial-continuum relaxation edge. Nonstationary bound states enter sequentially at \(g=\gamma_1/(vn)\), for integers \(n\ge1\), from the continuum threshold. The eigenmode of index \(n\) has parity \((-1)^n\); consequently the first even nonstationary bound density mode exists exactly when \(g<\gamma_1/(2v)\). The two parity channels therefore have distinct onset thresholds for discrete relaxation.

## Assumptions and scope
The motion is the two-state Markov velocity process \(\dot X_t=vS_t\) with \(S_t\in\{-1,+1\}\) and the indicated space- and direction-dependent Poisson reversal rates. The parameters satisfy \(v,g>0\) and \(0<\gamma_1<\gamma_0\), so all rates stay strictly positive. The stationary joint position-orientation density is \(p_{+,\star}=p_{-,\star}=p_\star/2\), with \(p_\star(x)=Z^{-1}\cosh(gx)^{-2\nu}\) and \(Z=\int_{\mathbb R}\cosh(gx)^{-2\nu}\,dx\). This stationary law was previously obtained by Jain and Chatterjee and is assumed known, not claimed as new.

The spectral assertion concerns the density perturbation \(p=p_++p_-\) after conjugation by \(\cosh(gx)^{-\nu}\), in the Hilbert space \(L^2(\mathbb R,dx)\), with compatible initial \(p\) and \(p_t=-v\partial_x(p_+-p_-)\). Equivalently the original perturbation belongs to \(L^2(p_\star^{-1}dx)\). We exclude the invariant stationary mass mode. The decay rate is a *spectral abscissa*, not an assertion of universal pointwise exponential asymptotics or of a sharp operator-norm bound without possible edge prefactors.

## Proof
Let \(p=p_++p_-\) and \(q=p_+-p_-\). The forward equations give
\[
\partial_tp=-v\partial_xq,\qquad
\partial_tq=-v\partial_xp-2\gamma_0q-2\gamma_1\tanh(gx)p.
\]
Differentiating the first and eliminating \(q\) yields
\[
\partial_t^2p+2\gamma_0\partial_tp
=v^2\left(\partial_x^2p+2\frac{\gamma_1}{v}\partial_x(\tanh(gx)p)\right).
\]
Put \(a=\gamma_1/v=g\nu\) and \(\Phi(x)=\nu\log\cosh(gx)\), and set \(p=e^{-\Phi}\psi\). Direct differentiation, using \(\Phi'=a\tanh(gx)\), gives
\[
\partial_t^2\psi+2\gamma_0\partial_t\psi=-v^2H\psi,
\quad H=-\partial_x^2+a^2-(a^2+ag)\operatorname{sech}^2(gx).
\]
On writing \(z=gx\), \(g^{-2}H=H_\nu=-\partial_z^2+\nu^2-\nu(\nu+1)\operatorname{sech}^2z\). Define \(A_\nu=\partial_z+\nu\tanh z\). Then \(H_\nu=A_\nu^*A_\nu\) and \(A_\nu A_\nu^*=H_{\nu-1}+(2\nu-1)\). The normalized ground eigenfunction is proportional to \(\operatorname{sech}^{\nu}z\), with eigenvalue zero. Repeated intertwining from the ground states of \(H_{\nu-n}\) gives exactly the additional eigenvalues \(n(2\nu-n)\), for positive integers \(n<\nu\); their parity alternates. They are square integrable exactly for \(\nu-n>0\). To see completeness, iterate the factorization until the residual parameter is in \((0,1]\). Its partner operator has no spectrum below the asymptotic threshold because the residual partner potential \(\nu(1-\nu)\operatorname{sech}^2z\) is nonnegative when \(0<\nu\le1\); thus no further bound levels exist. The potential converges exponentially to \(\nu^2\), so Weyl's theorem gives essential spectrum \([\nu^2,\infty)\). At integer \(\nu=n\), the threshold solution does not decay and is not in \(L^2\).

For a spatial eigenvalue \(E\) of \(H\), temporal separation gives \(s^2+2\gamma_0s+v^2E=0\). Because \(\gamma_0>\gamma_1\) and all bound eigenvalues obey \(v^2E<\gamma_1^2\), the two rates \(s_{n,\pm}\) are real. The slow edge of the continuum is obtained from \(E=a^2\), and larger continuum eigenvalues do not have slower real parts (for \(v^2E>\gamma_0^2\) the real part is \(-\gamma_0\)). The smallest positive spatial eigenvalue is \(g^2(2\nu-1)\) if \(\nu>1\); otherwise the continuum threshold \(a^2\). This proves \(G(g)\). For \(g<\gamma_1/v\), differentiation of its first branch gives \(G'(g)=v(\gamma_1-vg)/\sqrt{\gamma_0^2-2v\gamma_1g+v^2g^2}>0\); the second branch is constant. Parity and the even-sector threshold follow from the intertwining eigenfunctions.

The separated temporal solution at spatial index \(n=0\) has formal exponents \(0\) and \(-2\gamma_0\). The latter is **not an admissible mass-preserving forward density mode**, because it changes the total mass; only the stationary exponent zero survives. This removes an elimination-induced spurious branch. No other nonzero, integrable solution can have identically zero position perturbation, since \(p_t=-v\partial_xq\) would then force a spatially constant, nonintegrable \(q\).

## Verification
The accompanying `verify_spectrum.py` independently compares the discrete Schrödinger eigenvalues against centered finite-difference discretizations on a large interval, verifies the exact conjugation identity symbolically, and checks the temporal exponents and their threshold/gradient classification at three distinct gradient values. Executable command: `python verify_spectrum.py`. The analytical factorization and spectral argument, not finite-grid numerics, establish the infinite-line conclusions.

## Relationship to prior work
Jain and Chatterjee, arXiv:2405.13521, derive the stationary \(\cosh\)-power density for these exact rates (Sec. III.2.1) and calculate the step-rate \(g\to\infty\) Green function, with slow decay scale \(\gamma_0-\sqrt{\gamma_0^2-\gamma_1^2}\) (Appendix E). They do **not** present a finite-gradient discrete eigenvalue ladder or the exact finite-gradient plateau threshold; their Sec. IV uses numerical studies for general finite gradients. Singh, Sabhapandit, and Kundu, arXiv:2004.11041, analyze *piecewise power-law* spatial reversal rates rather than these smooth saturating rates. Mallmin, Blythe, and Evans, arXiv:1810.00813, solve an interacting lattice ring model, not this inhomogeneous infinite-line process. The Pöschl–Teller factorization and its bound-state spectrum are classical mathematics; the claim is their exact physical realization here and the resulting saturation and parity-resolved relaxation thresholds, not invention of that factorization.

## Limitations
The spectral gap is established in the stated weighted density space; convergence rates for arbitrary singular initial laws and total-variation norms require separate estimates. Continuum-edge behavior may have algebraic prefactors, and a specially prepared initial condition can annihilate the slowest mode. The critical thresholds are level-merging points, not claimed thermodynamic phase transitions. The result is restricted to constant speed, tanh reversal-rate profiles, and \(\gamma_0>\gamma_1\); arbitrary saturating rates and spatially varying speeds are not covered. A general kinetic-to-Schrödinger mapping in the literature could subsume the derivation, and independent verification of publication priority is outstanding.

## References
1. K. Jain and S. Chatterjee, *Run-and-tumble particle with saturating rates*, arXiv:2405.13521 (v1 first posted 2024-05-22), https://arxiv.org/html/2405.13521v2 .
2. P. Singh, S. Sabhapandit, and A. Kundu, *Run-and-Tumble particle in inhomogeneous media in one dimension*, arXiv:2004.11041 (2020), https://arxiv.org/abs/2004.11041 .
3. E. Mallmin, R. A. Blythe, and M. R. Evans, *Exact spectral solution of two interacting run-and-tumble particles on a ring lattice*, arXiv:1810.00813 (2018), https://arxiv.org/abs/1810.00813 .
4. Classical Pöschl–Teller potential and factorization (standard supersymmetric quantum mechanics); no priority is claimed for its known spectral theorem.
