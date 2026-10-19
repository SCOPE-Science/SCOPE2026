# Singular weak-coupling entanglement window in a locally squeezed bosonic dimer

## Finding

A symmetric pair of coupled, locally damped bosonic modes has an exactly solvable **coupling–squeezing tradeoff**. Let \(r\) be the local bath squeezing and \(J\) the coherent intermode hopping. At every fixed \(r>0\), the smallest partially transposed symplectic eigenvalue of the stationary Gaussian state has the unique coupling minimizer
\[
J_*(r)=\frac{\gamma}{2}\sqrt{1-\tanh(2r)}.
\]
Its exact optimized value is
\[
\min_{J\ge0}\frac{2\tilde\nu_-}{y}=\frac1{\sqrt{1+\tanh(2r)}},\qquad y=2\bar n+1.
\]
It follows that there exists a finite squeezing and coupling producing positive logarithmic negativity if and only if \(1\le y<\sqrt2\). The global bound and its attainability statement are
\[
\sup_{r\ge0,J\ge0}E_N(r,J;y)
=\max\{0,\tfrac12-\log_2 y\}.
\]
When the right side is positive, it is a **strict nonattained supremum** over finite parameters. In particular, the vacuum-bath logarithmic negativity is strictly below one-half bit at every finite setting, although one-half bit is approached.

This saturation is singular: the optimal coupling vanishes when the squeezing diverges. Precisely, when \(J=\gamma z e^{-2r}\) with fixed \(z\ge0\),
\[
\lim_{r\to\infty}\frac{2\tilde\nu_-(r,\gamma z e^{-2r})}{y}
=F(z):=\sqrt{1+2z^2}-z.
\]
The convergence is uniform on compact \(z\)-intervals. For \(1\le y<\sqrt2\), the limiting logarithmic negativity is positive exactly for
\[
z_-(y)<z<z_+(y),\qquad
z_\pm(y)=\frac1y\pm\sqrt{\frac2{y^2}-1}.
\]
At \(y=1\) the limiting window is \(0<z<2\). The unique minimizer of \(F\) is \(z=1/\sqrt2\), with \(F=1/\sqrt2\). At or above \(y=\sqrt2\) no finite setting is entangled.

## Assumptions and scope

There are two resonant harmonic modes with annihilation operators \(a_1,a_2\) and number-conserving Hamiltonian \(H=J(a_1^\dagger a_2+a_2^\dagger a_1)\) in the frame rotating at the common oscillator frequency. The common damping strength is \(\gamma>0\), and both **independent local squeezed thermal baths** are phase-locked to that frame with equal bath squeezing \(r\ge0\), the same phase (chosen real by a common phase rotation), and the same thermal occupation \(\bar n\ge0\). The squeezed-bath GKSL generator and its coefficients are those in Ayoub–Castillo-Gonzalez–Bittner (2026), equations (2)–(8). We use \(\hbar=1\), canonical commutators \([x_j,p_k]=i\delta_{jk}\), and a vacuum quadrature variance of \(1/2\). Coupling \(J\ge0\) includes \(J=0\) as the decoupled boundary.

Write
\[
y=2\bar n+1,\quad K=\cosh(2r),\quad S=\sinh(2r),\quad
\mu=\frac{\gamma^2}{\gamma^2+4J^2},\quad
\chi=\frac{2\gamma J}{\gamma^2+4J^2}.
\]
The stationary logarithmic negativity is \(E_N=\max\{0,-\log_2(2\tilde\nu_-)\}\), where \(\tilde\nu_-\) is the smaller symplectic eigenvalue after partial transposition of the second mode. At \(r=0\) the state is separable for every \(J\). We do not assert a unique maximizer of \(E_N\) when all parameter choices are separable: uniqueness refers to minimization of \(\tilde\nu_-\).

## Proof

**1. Independent recovery of the stationary covariance.** Put \(M=-yS/2\) by choosing the real squeezed-bath phase. The linear Langevin drift on the ordered quadratures \((x_1,p_1,x_2,p_2)\) is
\[
A=\begin{pmatrix}
-\gamma/2&0&0&J\\0&-\gamma/2&-J&0\\
0&J&-\gamma/2&0\\-J&0&0&-\gamma/2
\end{pmatrix},
\]
whose eigenvalues have real part \(-\gamma/2\). Hence the covariance Lyapunov equation admits a unique stationary solution. Its diffusion matrix is \(D=\gamma\,\mathrm{diag}(a+M,a-M,a+M,a-M)\), where \(a=yK/2\). Solving \(AV+VA^{\mathsf T}+D=0\) gives
\[
V=\begin{pmatrix}
a+\mu M&0&0&-\chi M\\
0&a-\mu M&-\chi M&0\\
0&-\chi M&a+\mu M&0\\
-\chi M&0&0&a-\mu M
\end{pmatrix}.
\]
This also follows by writing the stationary anomalous moments \(\langle a_1^2\rangle=\langle a_2^2\rangle=\mu M\), \(\langle a_1a_2\rangle=-i\chi M\), together with \(\langle a_j^\dagger a_j\rangle=(yK-1)/2\) and vanishing normal intermode coherence. The standard two-mode partial-transpose symplectic invariant yields
\[
\tilde\nu_-=\sqrt{a^2-(\mu M)^2}-|\chi M|
=\frac y2 R(S,\mu),\quad
R(S,\mu)=\sqrt{1+(1-\mu^2)S^2}-\sqrt{\mu(1-\mu)}\,S.
\]
This agrees with equation (12) of the motivating paper, but the stationary moment calculation independently checks its physical normalization.

**2. Unique optimal coupling at finite squeezing.** Fix \(r>0\), put \(t=\tanh(2r)\in(0,1)\), and use the bijection between \(J\in[0,\infty)\) and \(\mu\in(0,1]\). Dividing by \(K=1/\sqrt{1-t^2}\), minimize
\[
G_t(\mu)=\sqrt{1-t^2\mu^2}-t\sqrt{\mu(1-\mu)}.
\]
Its derivative is negative for \(0<\mu\le1/2\). For \(1/2<\mu<1\), clearing the strictly positive derivative denominators shows its sign is the sign of
\[
(2\mu-1)\sqrt{1-t^2\mu^2}-2t\mu\sqrt{\mu(1-\mu)}.
\]
The difference of the squares of these two nonnegative terms factors exactly as
\[
(2\mu-1)^2(1-t^2\mu^2)-4t^2\mu^3(1-\mu)
=((2-t)\mu-1)((2+t)\mu-1).
\]
On this interval the second factor is strictly positive. Therefore the derivative changes from negative to positive precisely at \(\mu_*=1/(2-t)\), which is the unique global minimum (both boundary limits exceed it). Substitution yields \(G_t(\mu_*)=\sqrt{1-t}\) and hence
\[
J_*(r)=\frac\gamma2\sqrt{1-t},\qquad
\min_J R=\frac1{\sqrt{1+t}}.
\]
This minimizer depends on \(r\) and \(\gamma\), not on thermal occupancy \(\bar n\).

**3. Global resource/temperature boundary.** Because \(t<1\) at every finite \(r\), the above bound satisfies \(R>1/\sqrt2\). Conversely, following \(J_*(r)\) while \(r\to\infty\) makes \(R\downarrow1/\sqrt2\). Therefore
\[
\inf_{r,J}2\tilde\nu_-=\frac y{\sqrt2},\qquad
\sup_{r,J}E_N=\left[\frac12-\log_2 y\right]_+.
\]
If \(y<\sqrt2\), the supremum is positive and cannot be attained with finite \(r,J\). If \(y\ge\sqrt2\), \(E_N=0\) everywhere. For \(1<y<\sqrt2\), the exact strict squeezing requirement for **any** entanglement is
\[
\tanh(2r)>y^2-1,
\quad\text{equivalently}\quad
r>r_{\min}(y)=\frac14\log\frac{y^2}{2-y^2}.
\]
As \(y\uparrow\sqrt2\), \(r_{\min}(y)=\frac14\log(2/(2-y^2))+o(1)\). In terms of occupation number, the thermal feasibility condition is \(\bar n<(\sqrt2-1)/2\). For a physical thermal mode of frequency \(\omega>0\), this is equivalent to \(T<\omega/[2k_B\log(1+\sqrt2)]\).

**4. Sharp joint weak-coupling/high-squeezing window.** Set \(j=2J/\gamma\). The exact formula can be rewritten without approximating either parameter as
\[
R=\frac{\sqrt{(1+j^2)^2+(2+j^2)(jS)^2}-jS}{1+j^2}.
\]
Under \(J=\gamma ze^{-2r}\) for fixed \(z\ge0\), one has \(j\to0\) and \(jS=z(1-e^{-4r})\to z\). Therefore \(R\to F(z)=\sqrt{1+2z^2}-z\), with an \(O(e^{-4r})\) error uniform when \(z\) stays in a compact interval. The limiting negativity is exactly \(\max\{0,-\log_2(yF(z))\}\).

Solving \(yF(z)<1\) is equivalent to the quadratic inequality
\[
z^2-\frac{2z}{y}+1-\frac1{y^2}<0.
\]
It has a nonempty positive interval precisely when \(1\le y<\sqrt2\), and its roots are \(z_\pm=y^{-1}\pm\sqrt{2y^{-2}-1}\). This proves the stated sharp limiting window, including the endpoints (which have zero limiting logarithmic negativity). Differentiating \(F\) shows its unique minimum at \(z=1/\sqrt2\), with value \(1/\sqrt2\). The exact finite-squeezing optimizer obeys \(J_*(r)\sim\gamma e^{-2r}/\sqrt2\), so it converges to this distinguished scaling path.

For comparison, if \(J>0\) is fixed as \(r\to\infty\), then \(R\) diverges because \(\sqrt{1-\mu^2}-\chi>0\) for every fixed \(0<\mu<1\); consequently \(E_N\) eventually vanishes. If \(J=0\) exactly, the steady state is a product and \(R=1\). This explains why the entangled strong-squeezing limit requires a shrinking coupling.

**5. Complementary fixed-coupling optimum.** For \(J>0\), let \(A=1-\mu^2\) and \(B=\sqrt{\mu(1-\mu)}\). The function \(R(S)=\sqrt{1+AS^2}-BS\) has a unique minimum over \(S\ge0\) at \(S_*=\sqrt{\mu/(1-\mu^2)}\), and the minimum is \(1/\sqrt{1+\mu}\). This yields a separate finite-coupling entanglement feasibility test \(y<\sqrt{1+\mu}\). It is consistent with the nonattained joint optimum when \(\mu\uparrow1\).

## Verification

A standalone script `verify.py` solves the real-quadrature Lyapunov equation independently, reconstructs the partial-transpose symplectic spectrum from matrix eigenvalues, checks exact derivative-polynomial factorization symbolically, compares the analytic minimizers against finite coupling grids, and tests the high-squeezing scaling window and its endpoints. Its reproducible execution passed 1057 checks using Python, NumPy, SciPy and SymPy. These finite checks are safeguards against algebraic/normalization errors, not substitutes for the all-parameter proof above. Run with `python verify.py` after installing `requirements.txt`.

## Relationship to prior work

Ayoub, Castillo-Gonzalez and Bittner (2026) supply the squeezed-reservoir dynamical model and the exact stationary partially transposed symplectic eigenvalue in their equation (12), together with qualitative finite-squeezing entanglement domes and phase-reference dependence. **Neither that formula nor those observations are claimed as new.** The present claim is the global closed-form optimal coupling, a nonattained joint ceiling, the critical thermal occupation and squeezing-resource threshold, and the singular joint limit with its exact two-sided coupling window.

Schuch, Wolf and Cirac (2005/2006) optimize noisy Gaussian squeezing devices supplemented with passive control operations. Their dynamical resource class does not prescribe this pair of identical, continuously acting local squeezed thermal dissipators with one fixed coherent hopping, and their result does not supply this model's temperature boundary or weak-coupling/high-squeezing window. Ge, Tasgin and Zubairy (2015) study Gaussian nonclassicality/entanglement under static beam-splitter mixing, not this driven-dissipative stationary balance.

The formulas above follow analytically from a model whose finite-parameter stationary covariance is already known. Residual originality risk remains if a more general Gaussian optimal-control or singular-perturbation theorem implicitly subsumes the sharp joint scaling and thermal window; a search cannot demonstrate universal absence of such coverage.

## Limitations

The assertions apply to **equal** resonance frequencies in a co-rotating phase-locked frame, **equal** Markovian local decay rates and thermal occupations, **identical-phase** squeezed baths, passive coherent hopping, and Gaussian stationarity. The laboratory-fixed squeezing phase analyzed by the motivating paper is a different Floquet problem and is excluded. No universality is claimed for detuned or unequal baths, arbitrary squeezing phases, non-Markovian noise, or the energetic cost of realizing arbitrarily large squeezing. The half-bit quantity is logarithmic negativity, **not** an assertion of half a maximally entangled two-qubit Bell pair. Numerical verification is finite and does not certify the infinite-parameter theorem independently.

## References

1. Areeda Ayoub, Alfonso Castillo-Gonzalez, Eric R. Bittner, *Phase-Reference Control of Steady-State Entanglement in Open Quantum Systems*, arXiv:2605.03978v1, first posted 2026-05-05. https://arxiv.org/html/2605.03978v1
2. Norbert Schuch, Michael M. Wolf, J. Ignacio Cirac, *Optimal squeezing and entanglement from noisy Gaussian operations*, arXiv:quant-ph/0505145, 2005; *Phys. Rev. Lett.* **96**, 023004 (2006). https://arxiv.org/abs/quant-ph/0505145
3. Wenchao Ge, Mehmet Emre Tasgin, M. Suhail Zubairy, *Conservation relation of nonclassicality and entanglement for Gaussian states in a beam-splitter*, arXiv:1506.04937, 2015. https://arxiv.org/abs/1506.04937
