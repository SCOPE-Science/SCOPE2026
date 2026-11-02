# Coherent cancellation of critical slowing in a lossy bipartite quantum walk

## Finding
For the translation-invariant two-sublattice quantum walk originally studied by Rudner and Levitov, a particle initially localized on a nondecaying site has an infinite mean survival time when the two hopping strengths coincide. Nevertheless, a *normalizable, finitely supported coherent preparation* can have finite mean survival time at this same critical coupling. The precise criterion is one Fourier zero, and among preparations occupying at most \(L\) consecutive nondecaying sites an explicit sine-envelope state uniquely minimizes that lifetime.

More precisely, let \(v,w,\gamma>0\), \(\Delta\in\mathbb R\), and let \(f=(f_0,\ldots,f_{L-1})\) satisfy \(\sum_{j=0}^{L-1}|f_j|^2=1\). Let \(F(z)=\sum_{j=0}^{L-1}f_jz^j\) and define the mean survival time \(\tau=\int_0^\infty\Vert\psi(t)\Vert^2\,dt\). For every \(v,w>0\), with the possibility of \(+\infty\),
\[
\tau=\frac2\gamma+\frac{\Delta^2+\gamma^2/4}{\gamma}\int_{-\pi}^{\pi}\frac{|F(e^{ik})|^2}{|v+we^{ik}|^2}\,\frac{dk}{2\pi}.
\]
In particular, at the critical point \(v=w=h>0\), \(\tau<\infty\) **if and only if** \(F(-1)=0\). All such initial states still undergo complete absorption asymptotically.

For an arbitrary positive integer \(L\ge2\), the sharp minimum over all normalized initial states supported on at most \(L\) consecutive nondecaying sites is
\[
\boxed{\tau_{\min,L}=\frac2\gamma+\frac{\Delta^2+\gamma^2/4}{4\gamma h^2\cos^2(\pi/(2L))}.}
\]
A minimizing vector, uniquely up to translation and global phase within each fixed block of \(L\) sites, is the normalized convolution of \((\sin(\pi/L),\ldots,\sin((L-1)\pi/L))\) with \((1,1)\). For \(L=2\), the symmetric two-site state \((1,1)/\sqrt2\) has a finite mean lifetime while the one-site preparation has an infinite mean lifetime. For \(L=1\), no normalized critical finite-lifetime preparation exists.

For any fixed normalized finite-support initial vector with \(F(-1)\ne0\), as \(v,w\to h>0\),
\[
\tau\sim\frac{\Delta^2+\gamma^2/4}{\gamma}\frac{|F(-1)|^2}{|v^2-w^2|}.
\]
If \(F(-1)=0\), the mean survival time instead converges to its finite critical value. At criticality, the separately optimized uniform loss rate for the minimizing length-\(L\) state is \(\gamma_*=2\sqrt{\Delta^2+8h^2\cos^2(\pi/(2L))}\).

## Assumptions and scope
The Hilbert space is \(\ell^2(\mathbb Z)\otimes\mathbb C^2\), in infinite one-dimensional volume, with units \(\hbar=1\). The Hermitian hoppings are translation invariant and nearest-neighbor. On Fourier transforming, the non-Hermitian Bloch Hamiltonian is
\[
H(k)=\begin{pmatrix}\Delta&v+we^{ik}\\v+we^{-ik}&-i\gamma/2\end{pmatrix},\quad k\in[-\pi,\pi).
\]
Here the upper component is the nondecaying sublattice; only the lower component is dissipative. The state evolves by \(i\partial_t\psi=H\psi\). Initially all amplitude is on the upper sublattice and \(\psi_A(k,0)=F(e^{ik})\), \(\psi_B(k,0)=0\). Coefficients may be complex, with norm one. The only parameter restriction is \(v,w,\gamma>0\), and real \(\Delta\). The finite-block optimum assumes integer \(L\ge2\); it is not an optimization over arbitrary infinitely supported states or multiple decay channels.

## Proof
**Step 1: two-state integrated survival identity.** Fix a Bloch momentum with \(s=|v+we^{ik}|>0\), and remove the off-diagonal phase by a unitary diagonal rotation. Write the amplitudes as \(u(t),b(t)\) with \((u(0),b(0))=(1,0)\) and
\[
i\dot u=\Delta u+s b,\qquad i\dot b=s u-i\gamma b/2.
\]
The generator is dissipative and has no real eigenvalue for \(s>0\): a nondecaying eigenvector would have \(b=0\) from the loss identity and then \(u=0\) from the coupling equation. Thus both amplitudes decay exponentially at each fixed \(s>0\). Define \(p_u=|u|^2\), \(p_b=|b|^2\), and \(c=u\overline b\). Their exact identities are
\[
\dot p_u=-2s\operatorname{Im}c,\quad
\dot p_b=2s\operatorname{Im}c-\gamma p_b,\quad
\dot c=(-\gamma/2-i\Delta)c+is(p_u-p_b).
\]
Integrate from zero to infinity. Norm loss gives \(\int p_b=1/\gamma\); the upper-population identity yields \(\int\operatorname{Im}c=1/(2s)\). Integrating the last equation and taking real and imaginary parts yields \(\int\operatorname{Re}c=\Delta/(\gamma s)\) and
\[
\int_0^\infty(p_u-p_b)\,dt=\frac{\gamma/4+\Delta^2/\gamma}{s^2}.
\]
Consequently the mean survival integral in one unit-amplitude Bloch mode is exactly
\[
T(s)=\frac{2}{\gamma}+\frac{\Delta^2+\gamma^2/4}{\gamma s^2}.
\]

**Step 2: arbitrary coherent initial preparation.** Parseval's identity decomposes the total survival norm into the integral of nonnegative modal norms \(|F(e^{ik})|^2\Vert e^{-iH(k)t}(1,0)^T\Vert^2\). Tonelli's theorem permits exchanging time and momentum integrals even when the result is infinite; Step 1 proves the displayed formula. If \(v=w=h\), the zero-coupling mode is only \(k=\pi\), a set of zero Lebesgue measure. Every other mode decays, and each mode norm is no greater than its initial norm. Dominated convergence therefore proves \(\Vert\psi(t)\Vert^2\to0\), hence absorption probability one, without assuming a finite first moment.

**Step 3: exact critical finiteness threshold.** At \(v=w=h\),
\[
|v+we^{ik}|^2=4h^2\cos^2(k/2).
\]
A finite polynomial \(F\) has \(\int|F(e^{ik})|^2/\cos^2(k/2)\,dk<\infty\) exactly when \(F(-1)=0\): otherwise the integrand has a nonintegrable quadratic singularity at \(k=\pi\). If \(F(-1)=0\), the factor theorem gives a unique polynomial \(G(z)=\sum_{j=0}^{L-2}g_jz^j\) with \(F(z)=(1+z)G(z)\). Parseval cancels the singular factor and yields
\[
\int_{-\pi}^{\pi}\frac{|F(e^{ik})|^2}{|h(1+e^{ik})|^2}\frac{dk}{2\pi}
=\frac{1}{h^2}\sum_{j=0}^{L-2}|g_j|^2.
\]
The complex phases of the coefficients do not affect this equivalence.

**Step 4: sharp constrained optimization.** Write \(f=B_Lg\) for the convolution \((1+z)G(z)\). The rectangular \(L\times(L-1)\) matrix \(B_L\) has two unit entries in each column, on consecutive rows. Its Gram matrix \(B_L^*B_L\) has diagonal entries \(2\) and adjacent off-diagonal entries \(1\). Its eigenvalues are \(2+2\cos(j\pi/L)\), \(j=1,\ldots,L-1\). The maximal eigenvalue is simple and equals \(4\cos^2(\pi/(2L))\), with eigenvector \(g_j\propto\sin((j+1)\pi/L)\). By the Rayleigh–Ritz inequality, normalizing \(\Vert f\Vert=1\) gives
\[
\frac{\Vert g\Vert^2}{\Vert B_Lg\Vert^2}\ge\frac1{4\cos^2(\pi/(2L))},
\]
with equality exactly on that one-dimensional eigenspace. The minimum and uniqueness follow. States with \(F(-1)\ne0\) have infinite time and cannot compete. A translation only multiplies \(F(e^{ik})\) by a unit-modulus Bloch phase and does not alter the lifetime.

**Step 5: near-critical boundary and loss optimization.** Let \(a=v^2+w^2\) and \(b=2vw\). For \(v\ne w\), the normalized reciprocal Bloch denominator is a circular Poisson kernel with total mass \(1/|v^2-w^2|\) that concentrates at \(k=\pi\) as \(v,w\to h>0\). Integrating the continuous function \(|F(e^{ik})|^2\) gives the stated leading divergence. When \(F(-1)=0\), write \(F=(1+z)G\); the ratio \(|1+e^{ik}|^2/|v+we^{ik}|^2\) is uniformly bounded near \(v=w=h\) if \(v\) and \(w\) approach \(h\) from arbitrary paths: indeed its maximum is at most \(4/(v+w)^2\). Dominated convergence yields a finite limit. Finally, at fixed \(f\), letting \(I\) be the positive inverse-coupling integral gives \(\tau=(2+\Delta^2 I)/\gamma+\gamma I/4\); differentiating proves the unique optimum \(\gamma_*=2\sqrt{\Delta^2+2/I}\). Substitute the sharp \(I\) from Step 4.

## Verification
The accompanying standalone Python checker `check_critical_walk.py` uses independent continuous-time Lyapunov-equation integration of the two-level dynamics rather than invoking the integrated-population derivation. It also numerically performs Bloch integration, independently diagonalizes convolution Gram matrices, and compares randomized normalized cancelling preparations with the sharp bound. Running `python check_critical_walk.py` with NumPy and SciPy yielded **231 passed comparisons**, maximum normalized discrepancy below \(9\times10^{-14}\). These finite checks corroborate the analytical proof and do not substitute for the infinite-volume argument.

## Relationship to prior work
Rudner and Levitov [1] introduced the dissipative bipartite walk, established its topological displacement transition, and identified a divergent mean dwell time for a state initially localized on one nondecaying site. Their formula near critical coupling is derived through a Golden Rule approximation. Rudner and Levitov [2] further analyzed the spin-pumping realization and near-dark states. Rudner, Levin, and Levitov [3] developed the general Bloch dark-state topology and associated lifetime divergences. These prior mechanisms are not claimed here. The new scope is an exact mean-lifetime formula with arbitrary finite coherent upper-sublattice preparation, a necessary-and-sufficient Fourier cancellation condition at criticality, and a sharp all-\(L\) optimal preparation bound with a distinguished minimizing wavepacket. Thiel, Kessler, and Barkai [4] studied quantization of the mean decay time with a single decay channel initialized in the decaying state, a different regime. Historical priority in wider wavepacket and absorbing-SSH literature has not been independently certified.

## Limitations
The theorem concerns a spatially infinite, translation-invariant Markovian-loss two-band walk; the initial state lies entirely on the nondecaying sublattice. The exact critical cancellation requires coherent relative phases and is not robust to arbitrary incoherent preparation errors. The minimization is over a contiguous block of \(L\) cells, not arbitrarily scattered or infinitely supported states. Finite systems, boundaries, disordered couplings, nonlinearities, stochastic dephasing, and preparation or readout errors are not covered. The result proves asymptotic total absorption even where the mean lifetime is infinite; this is not a finite-time absorption guarantee. Independent expert verification and exhaustive historical-priority verification have not been performed.

## References
1. M. S. Rudner and L. S. Levitov, *Topological Transition in a Non-Hermitian Quantum Walk*, arXiv:0807.2048v1 (first public 2008-07-13), https://arxiv.org/abs/0807.2048.
2. M. S. Rudner and L. S. Levitov, *Phase Transitions in Dissipative Quantum Transport and Mesoscopic Nuclear Spin Pumping*, arXiv:1005.4809v1 (2010-05-26), https://arxiv.org/abs/1005.4809.
3. M. S. Rudner, M. Levin, and L. S. Levitov, *Survival, Decay, and Topological Protection in Non-Hermitian Quantum Transport*, arXiv:1605.07652v1 (2016-05-24), https://arxiv.org/abs/1605.07652.
4. F. Thiel, D. A. Kessler, and E. Barkai, *Quantization of the Mean Decay Time for Non-Hermitian Quantum Systems*, arXiv:1912.08649v1 (2019-12-18), https://arxiv.org/abs/1912.08649.
