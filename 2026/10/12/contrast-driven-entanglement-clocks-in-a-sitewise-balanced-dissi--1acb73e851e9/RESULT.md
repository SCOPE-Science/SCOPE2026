# Contrast-driven entanglement clocks in a sitewise-balanced dissipative Kitaev dimer

## Finding

**Theorem (complete finite-time crossing classification).** Let \(J>0\) and \(\gamma_1,\gamma_2\geq0\). Consider two fermionic modes with the compact Kitaev Hamiltonian \(H=-J X_1X_2\) in the Jordan–Wigner spin representation, and Lindblad dynamics
\[
\frac{d\rho}{dt}=-i[H,\rho]+\sum_{j=1}^{2}\gamma_j\bigl(\mathcal D[c_j]\rho+\mathcal D[c_j^\dagger]\rho\bigr),\qquad
\mathcal D[L]\rho=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
\]
with \(c_1=\sigma^-\otimes I\), \(c_2=Z\otimes\sigma^-\), and \(\sigma^-=|0\rangle\langle1|\). Start in any Fock product state \(|n_1n_2\rangle\), \(n_1,n_2\in\{0,1\}\). In particular, loss and gain are balanced separately at each site, but their common site-specific rates need not agree between sites.

For a one-site reduced density matrix, let an **entanglement-spectrum crossing** mean equality of its two eigenvalues. For the bipartition \(A=\{1\}\), \(B=\{2\}\), define the **twisted-negativity singular-spectrum crossing** by equality of the two largest singular values of \(T_A=\rho^{R_A}Z_1\), with fermionic partial time reversal \(R_A\) defined below. Write \(\delta=\gamma_2-\gamma_1\) and \(s=|\delta|/(4J)\). The following statements hold at every finite time \(t\geq0\).

1. **Exact crossing equivalence:** the twisted-negativity gap closes precisely when *at least one* one-site entanglement-spectrum gap closes. If \(z_j(t)=\operatorname{tr}(\rho(t)Z_j)\), this condition is exactly \(z_1(t)z_2(t)=0\).

2. **Oscillatory regime:** when \(|\delta|<4J\), both one-site gaps close infinitely often. Set \(\Omega=\sqrt{4J^2-\delta^2/4}\), \(\varphi=\arcsin(\delta/(4J))\). The respective first finite closing times are
\[
t_1=\frac{\pi/2+\varphi}{\Omega},\qquad
 t_2=\frac{\pi/2-\varphi}{\Omega}.
\]
They coincide if and only if the rates are equal. The site with the larger balanced gain/loss rate closes first.

3. **Critical and overdamped regimes:** when \(|\delta|=4J\), only the higher-rate site has a finite closing, at \(t=1/(2J)\); the other never closes at finite time. When \(|\delta|>4J\), only the higher-rate site has a finite closing, occurring exactly once at
\[
t=\frac{1}{\nu}\operatorname{artanh}\!\left(\frac{2\nu}{|\delta|}\right),\qquad
\nu=\sqrt{\delta^2/4-4J^2}.
\]
The lower-rate gap tends to zero only asymptotically as \(t\to\infty\).

4. **Sharp first negativity clock:** for all nonnegative site rates, the first twisted-negativity singular-spectrum crossing is
\[
\boxed{\quad t_N=\frac{1}{2J}
\begin{cases}
\displaystyle\frac{\arccos(s)}{\sqrt{1-s^2}},&0\leq s<1,\\[6pt]
1,&s=1,\\[4pt]
\displaystyle\frac{\operatorname{arccosh}(s)}{\sqrt{s^2-1}},&s>1.
\end{cases}\quad}
\]
It depends only on the **difference** of the two site rates, not on a common rate added to both. It is continuous and strictly decreasing in \(s\), from \(\pi/(4J)\) at zero contrast to zero as \(s\to\infty\). In particular, the later one-site closing diverges as \(s\uparrow1\), while the *earlier negativity closing remains finite*, tending to \(1/(2J)\).

## Assumptions and scope

The Hamiltonian is the zero-chemical-potential, equal-hopping-and-pairing point of an **open two-site** Kitaev chain; the spin representation \(H=-JX_1X_2\) fixes all sign conventions. Site \(j\) has equal fermionic particle-loss and particle-gain rates \(\gamma_j\), each multiplying a standard Lindblad dissipator. No assumption of weak noise or weak contrast is made. The initial state is an occupation-basis product projector. The theorem concerns **spectral degeneracies at finite time**, not a positivity threshold for physical logarithmic negativity, not a many-site theorem, and not a claim that entanglement survives until the spectral closing.

Write \(\epsilon_j=(-1)^{n_j}\). For convenience define real functions
\[
(C_\delta(t),S_\delta(t))=
\begin{cases}
(\cos(\Omega t),\sin(\Omega t)/\Omega),&|\delta|<4J,\\
(1,t),&|\delta|=4J,\\
(\cosh(\nu t),\sinh(\nu t)/\nu),&|\delta|>4J,
\end{cases}
\]
with \(\Omega,\nu\) as above. The complete relevant state coefficients are
\[
\begin{aligned}
z_1(t)&=\epsilon_1 e^{-(3\gamma_1+\gamma_2)t/2}\bigl(C_\delta(t)+\tfrac\delta2S_\delta(t)\bigr),\\
z_2(t)&=\epsilon_2 e^{-(\gamma_1+3\gamma_2)t/2}\bigl(C_\delta(t)-\tfrac\delta2S_\delta(t)\bigr),\\
w_1(t)&=2J\epsilon_1 e^{-(3\gamma_1+\gamma_2)t/2}S_\delta(t),\\
w_2(t)&=2J\epsilon_2 e^{-(\gamma_1+3\gamma_2)t/2}S_\delta(t),\\
r(t)&=\epsilon_1\epsilon_2 e^{-2(\gamma_1+\gamma_2)t}.
\end{aligned}
\]
Thus
\[
\rho(t)=\tfrac14\bigl[I+z_1Z_1+z_2Z_2+w_1Y_1X_2+w_2X_1Y_2+rZ_1Z_2\bigr].
\]
These formulas also specify all finite-time normalization and rate conventions.

## Proof

**1. Exact invariant Pauli sector.** Direct evaluation of the Lindblad adjoint on the five nonconstant Pauli strings gives
\[
\begin{array}{ll}
\dot z_j=-2\gamma_jz_j-2Jw_j,&
\dot w_j=2Jz_j-(\gamma_1+\gamma_2)w_j,\quad j=1,2,\\
\dot r=-2(\gamma_1+\gamma_2)r.&
\end{array}
\]
The identity remains closed because the Hamiltonian is \(-JX_1X_2\), the jump operators are the stated fermionic Jordan–Wigner operators, and the initial Fock projector has no other Pauli components. Initially \(z_j=\epsilon_j\), \(w_j=0\), \(r=\epsilon_1\epsilon_2\). Each two-dimensional subsystem has mean decay \((3\gamma_j+\gamma_{3-j})/2\) and squared oscillation frequency \(4J^2-\delta^2/4\). Exponentiating these real \(2\times2\) matrices proves all five coefficient formulas, including the continuous exceptional-point limit \(|\delta|=4J\).

**2. A dynamically exact quadratic relation.** Differentiate \(z_1z_2+w_1w_2\) using the equations just displayed. The coherent cross terms cancel exactly, leaving
\[
\frac{d}{dt}(z_1z_2+w_1w_2)
=-2(\gamma_1+\gamma_2)(z_1z_2+w_1w_2).
\]
Equality with \(r(t)\) holds initially and hence for all times:
\[
\boxed{\quad r(t)=z_1(t)z_2(t)+w_1(t)w_2(t).\quad}
\]
This is a direct dynamical identity rather than an inferred Gaussian approximation.

**3. Complete twisted-negativity singular spectrum.** Choose the four ordered Jordan–Wigner Majoranas \(a_1=X_1\), \(b_1=Y_1\), \(a_2=Z_1X_2\), \(b_2=Z_1Y_2\). Define fermionic partial time reversal \(R_A\) by multiplying an ordered Majorana monomial containing \(k\) Majoranas from site \(A\) by \(i^k\), and extending linearly. For the state above, \(T_A=\rho^{R_A}Z_1\) is Hermitian and has two real \(2\times2\) spectral blocks. Set
\[
A_*=\sqrt{(1+r)^2+(w_1-w_2)^2},\qquad
B_*=\sqrt{(1-r)^2+(w_1+w_2)^2}.
\]
Its four eigenvalues, including multiplicity, are exactly
\[
\frac{-z_1-z_2\pm A_*}{4},\qquad
\frac{-z_1+z_2\pm B_*}{4}.
\]
Therefore the largest singular value of the first block is \((A_*+|z_1+z_2|)/4\), while that of the second is \((B_*+|z_1-z_2|)/4\). The quadratic identity from Step 2 gives
\[
A_*^2-B_*^2=4(r-w_1w_2)=4z_1z_2,
\qquad
(z_1+z_2)^2-(z_1-z_2)^2=4z_1z_2.
\]
If \(z_1z_2>0\), both comparisons strictly favor the first block, and the two singular values within that block have a strict gap because \(A_*>0\) and \(z_1+z_2\ne0\). If \(z_1z_2<0\), the same strict argument favors the second block, where \(B_*>0\) and \(z_1-z_2\ne0\). If \(z_1z_2=0\), the two blocks have identical largest singular values, giving an exact leading degeneracy. This proves the claimed **if and only if** statement without assuming it from a general Gaussian-state result. Each one-site density matrix is \((I+z_j Z)/2\), so its two eigenvalues are \((1\pm z_j)/2\), establishing the first part.

**4. Finite-time root census and sharp clock.** The strictly positive exponential factors in the coefficient formulas do not affect zero locations. In the oscillatory regime, use \(\delta/(2\Omega)=\tan\varphi\) to rewrite the brackets as multiples of \(\cos(\Omega t\mp\varphi)\). Their respective first positive roots give \(t_1\) and \(t_2\), and periodicity gives infinitely many later roots. When \(\delta=0\), they agree; otherwise, the larger-rate site's root comes first.

For \(\delta>0\) in the overdamped regime, the second bracket has exactly one zero because \(\tanh(\nu t)=2\nu/\delta\) has exactly one finite solution, whereas the first bracket is strictly positive for every finite \(t\ge0\); for \(\delta<0\), exchange the two sites. At \(|\delta|=4J\), the relevant factors are \(1\mp2Jt\), proving the exceptional-point classification.

Finally \(\min(t_1,t_2)\) simplifies to the displayed piecewise formula using \(\varphi=\arcsin(\delta/(4J))\) below threshold and \(\operatorname{artanh}(\sqrt{s^2-1}/s)=\operatorname{arccosh}(s)\) above threshold. Strict monotonicity follows from the strictly increasing ratio \(\theta/\sin\theta\) for \(0<\theta\le\pi/2\) when \(s=\cos\theta\), and the strictly decreasing ratio \(u/\sinh u\) for \(u>0\) when \(s=\cosh u\). Both branches tend to unity as \(s\to1\). This completes the proof.

## Verification

The reproducible scripts `verify_symbolic.py` and `verify.py` are included. Install the dependencies listed in `requirements.txt` and run `python verify_symbolic.py` followed by `python verify.py`. The symbolic script checks the Lindblad adjoint sector for independent symbolic rates, the exact Majorana partial-time-reversal characteristic polynomial, and the invariant quadratic identity. The numerical script independently constructs the \(16\times16\) Lindblad superoperator and the fermionic partial-time-reversal map, and executes 1,521 checks covering four initial occupation patterns, distinct coherent scales, underdamped and overdamped contrasts, both signs of contrast, and the critical boundary. Successful output is `VERIFY_SYMBOLIC_OK` and `VERIFY_OK 1521 direct matrix/Lindblad/singular-spectrum checks`.

These finite checks corroborate, but do not replace, the analytic proof for all \(J>0\), \(\gamma_j\ge0\), and finite \(t\).

## Relationship to prior work

Chowdhary, Chirame, Haas, and Jha (arXiv:2610.03889v1, publicly posted 2026-10-02) derive Gaussian parity criteria for one-site entanglement and twisted negativity gaps. Their balanced gain/loss theorem explicitly uses a common rate at **every site**, yielding unchanged clocks under uniform damping; their stronger dephasing and gain-versus-loss-imbalanced analyses concern different channels. The present two-site theorem instead treats **equal gain and loss at each site with unequal rates between sites**, deriving a full spectral formula and a sharp contrast-driven bifurcation: the earlier negativity clock speeds up while the later one-site clock disappears at critical contrast. The Gaussian parity criterion from the earlier paper is credited and independently recovered here in the two-site model; it is not claimed as new.

Sayyad, Yu, Grushin, and Sieberer (arXiv:2011.10601) study entanglement crossings and critical slowing in dissipative topological quenches, while Starchl and Sieberer (arXiv:2304.01836) analyze parity-time-symmetric dissipative fermionic quench dynamics. Their established dynamical settings provide relevant precedent for damping transitions, but the present specified local-rate, sitewise-balanced two-mode crossing law is a distinct statement. Full-text comparisons beyond the motivating paper remain a residual priority limitation.

## Limitations

The theorem is confined to the **two-site compact-point** Kitaev Hamiltonian with balanced loss and gain separately on each site, and to occupation-product initial states. It does not give crossing times for longer chains, arbitrary quadratic couplings, non-Gaussian states, or general initial states. It classifies degeneracies of the **twisted** fermionic negativity singular spectrum, not arbitrary choices of fermionic negativity convention or a sudden-death time of ordinary entanglement. The finite checks cannot prove novelty, and mathematically equivalent older reductions may remain unindexed.

## References

1. S. Chowdhary, S. Chirame, S. Haas, and R. Jha, *Exact Temporal Criticalities of Entanglement and Negativity in Gaussian and Non-Gaussian Dissipative Kitaev Chains*, arXiv:2610.03889v1 (2026-10-02), https://arxiv.org/html/2610.03889v1 .
2. S. Sayyad, J. Yu, A. G. Grushin, and L. M. Sieberer, *Entanglement Spectrum Crossings Reveal non-Hermitian Dynamical Topology*, arXiv:2011.10601, https://arxiv.org/abs/2011.10601 .
3. E. Starchl and L. M. Sieberer, *Quantum Quenches in Driven-Dissipative Quadratic Fermionic Systems with Parity-Time Symmetry*, arXiv:2304.01836, https://arxiv.org/abs/2304.01836 .
