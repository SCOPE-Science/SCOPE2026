# A single bond-pair defect creates a sharp \(1/N\) fidelity window in a flat-band diamond channel

## Finding

For every integer \(N\ge2\), introduce the zero-energy flat-band channel of an open, unit-hopping diamond chain whose **only** altered hopping pair connects cell \(1\) to central site \(b_2\): the two amplitudes are \(1+\delta\) and \(1-\delta\), with \(-1<\delta<1\). Let \(P\) project onto the complete zero-mode subspace of the channel, let \(S,R\) couple with equal positive amplitude \(g\) to its projected end sites \(P|a_1\rangle\) and \(P|a_N\rangle\), and put \(Q=1+(N-1)\delta^2\). The exact effective couplings obey

\[
\eta_S=\|P|a_1\rangle\|^2=\frac{1}{2Q},\qquad
\eta_R=\|P|a_N\rangle\|^2=\frac{1+N\delta^2}{2Q},\qquad
\Lambda=\langle a_1|P|a_N\rangle=\frac{(-1)^{N+1}\delta}{2Q}.
\]

For every nonzero defect, and every real observation time,

\[
\left|\langle R|e^{-itH_{\mathrm{eff}}}|S\rangle\right|^2
\le \boxed{\frac{1}{1+N^2\delta^2/4}}.
\]

Outside a **countable exceptional set** of nonzero defect values, this bound is the exact supremum over all nonnegative observation times. At \(\delta=0\), end-to-end transfer is identically zero, despite the nonzero limit of the displayed ceiling as \(\delta\to0\). Consequently, for a generic nonzero defect to permit supremal transfer probability at least \(1-\varepsilon\), with \(0<\varepsilon<1\), it is necessary and sufficient that

\[
0<|\delta|\le\frac{2}{N}\sqrt{\frac{\varepsilon}{1-\varepsilon}}.
\]

For the scaling \(\delta=c/N\), where \(c>0\) is fixed and \(N>c\), the supremal probability is generically \((1+c^2/4)^{-1}\) and the nonzero frequency splitting has the sharp asymptotic

\[
\omega_+-\omega_- =\frac{g c\sqrt{c^2+4}}{2\sqrt2\,N}+O_c(gN^{-2}).
\]

The near-perfect transfer window is therefore \(O(N^{-1})\) in the isolated bond-pair defect, with an \(\Omega(N/g)\) slow-beat observation-time cost. These are exact or asymptotic statements **for the projected resonant effective Hamiltonian**, not for finite-coupling evolution of the complete channel.

## Assumptions and scope

Take the Hilbert space \(\mathbb C^N_{b}\oplus\mathbb C^{2N}_{a,c}\), with unit vectors \(|b_j\rangle,|a_j\rangle,|c_j\rangle\), and define the real matrix \(B:\mathbb C^{2N}\to\mathbb C^N\) by

\[
(B\psi)_1=\psi_{a_1}+\psi_{c_1},\qquad
(B\psi)_2=\psi_{a_2}+\psi_{c_2}+(1+\delta)\psi_{a_1}+(1-\delta)\psi_{c_1},
\]
\[
(B\psi)_j=\psi_{a_j}+\psi_{c_j}+\psi_{a_{j-1}}+\psi_{c_{j-1}}\quad(3\le j\le N).
\]

The bare channel Hamiltonian is \(H_{\mathrm{ch}}=\begin{pmatrix}0&B\\B^\top&0\end{pmatrix}\). The first \(N\) columns of \(B\) are not assumed to be the left sublattice; the displayed basis ordering fixes this unambiguously. Since \(B\) has full row rank, its flat-band projector onto the outer-site subspace is

\[
P=I_{2N}-B^\top(BB^\top)^{-1}B.
\]

The effective Hilbert space is \(\operatorname{span}\{|S\rangle,|R\rangle\}\oplus\operatorname{ran}P\). It is equipped with

\[
H_{\mathrm{eff}}=g\big(|S\rangle\langle Pa_1|+|R\rangle\langle Pa_N|+|Pa_1\rangle\langle S|+|Pa_N\rangle\langle R|\big),\quad g>0.
\]

All assertions quantify over every \(N\ge2\), every \(g>0\), and indicated \(\delta\in(-1,1)\), with the irrational-frequency qualification stated explicitly. This is precisely the first-order resonant flat-band model, not a uniform approximation to an unprojected channel at arbitrary \(g\) or at arbitrary times.

## Proof

**Step 1: determine the entire zero-mode projector.** Let \(M=BB^\top\). Writing \(M_0=M|_{\delta=0}\), one checks directly that \(M_0\) is tridiagonal with diagonal \((2,4,\ldots,4)\) and both off-diagonals equal to \(2\). The single antisymmetric bond perturbation leaves the off-diagonal matrix elements unchanged, so

\[
M=M_0+2\delta^2 e_2e_2^\top.
\]

The invertible lower bidiagonal matrix \(L\), with ones on the diagonal and subdiagonal, gives \(M_0=2LL^\top\). Therefore, for \(1\le i,j\le N\),

\[
(M_0^{-1})_{ij}=\frac{(-1)^{i+j}}2\big(N-\max\{i,j\}+1\big).
\]

In particular, \(e_2^\top M_0^{-1}e_2=(N-1)/2\). The rank-one resolvent formula is consequently exact:

\[
M^{-1}=M_0^{-1}-\frac{2\delta^2}{Q}M_0^{-1}e_2e_2^\top M_0^{-1},\qquad Q=1+(N-1)\delta^2.
\]

The column \(B|a_1\rangle\) equals \(u=e_1+(1+\delta)e_2\), whereas \(B|a_N\rangle=v=e_N\). Substitution into \(P=I-B^\top M^{-1}B\) gives

\[
1-u^\top M^{-1}u=\frac1{2Q},\quad
1-v^\top M^{-1}v=\frac{1+N\delta^2}{2Q},\quad
-u^\top M^{-1}v=\frac{(-1)^{N+1}\delta}{2Q}.
\]

These identities are valid including \(N=2\). They are independent of the choice of an orthonormal flat-band eigenbasis.

**Step 2: diagonalize only the two-dimensional endpoint Gramian.** The nonzero squared singular values of \(H_{\mathrm{eff}}/g\) are the eigenvalues of

\[
G=\begin{pmatrix}\eta_S&\Lambda\\\Lambda&\eta_R\end{pmatrix}.
\]

For \(\delta\ne0\), let \(\Delta=\sqrt{(\eta_S-\eta_R)^2+4\Lambda^2}\). Its eigenvalues are

\[
\lambda_\pm=\frac{2+N\delta^2\pm|\delta|\sqrt{4+N^2\delta^2}}{4Q}>0,
\qquad \omega_\pm=g\sqrt{\lambda_\pm}.
\]

The evolution restricted to \(S,R\) is \(\cos(gt\sqrt G)\). Applying the spectral projector formula for a real symmetric \(2\times2\) matrix yields the exact amplitude

\[
\langle R|e^{-itH_{\mathrm{eff}}}|S\rangle
=\frac{\Lambda}{\Delta}\big(\cos(\omega_+t)-\cos(\omega_-t)\big).
\]

Its absolute value never exceeds \(2|\Lambda|/\Delta=(1+N^2\delta^2/4)^{-1/2}\). If \(\delta=0\), then \(\Lambda=0\), so the amplitude vanishes at every time; the \(\delta\ne0\) derivation must not be extended through this degeneracy by cancellation.

**Step 3: sharpness and the observation-time tradeoff.** For \(\delta\ne0\), \(\omega_+/\omega_-\) is real-analytic in \(\delta\) on each of \((-1,0)\) and \((0,1)\) and is not constant (it tends to \(1\) as \(\delta\to0\), while it exceeds \(1\) elsewhere). The preimage of each rational number is discrete, hence the rational-ratio exception set is at most countable. For irrational ratio the continuous one-parameter phase orbit \((\omega_+t,\omega_-t)\bmod2\pi\) is dense in the two-torus, so the cosine difference approaches \(2\) in modulus. The upper bound is thus the actual supremum for every nonexceptional \(\delta\ne0\).

The exact factorization of the cosine difference gives

\[
\big|\langle R|e^{-itH_{\mathrm{eff}}}|S\rangle\big|
\le C_N(\delta)\left|\sin\frac{(\omega_+-\omega_-)t}{2}\right|.
\]

If a time \(t\ge0\) achieves probability at least \(\theta^2 C_N(\delta)^2\), with \(0<\theta\le1\), then \(t\ge 2\arcsin(\theta)/(\omega_+-\omega_-)\). Finally, put \(\delta=c/N\) and expand the exact eigenvalue formula: \(\omega_+-\omega_-=gc\sqrt{c^2+4}/(2\sqrt2N)+O_c(gN^{-2})\). The fidelity condition follows by solving the exact envelope inequality for \(|\delta|\); for generic \(\delta\ne0\), density makes it sufficient as well.

## Verification

Execute the standalone `verify.py` using Python 3 and NumPy. The script rebuilds the physical channel incidence matrix, its exact flat-band projector, the effective Hamiltonian, and all displayed formulas independently. It checks rank-one determinant identities, projection properties, the two endpoint Gram entries, direct matrix-exponential transition amplitudes against the closed form, and the large-size beat-frequency limit. On the recorded run, **2,818 comparisons passed**, with maximum observed numerical discrepancy \(7.59\times10^{-15}\). The numerical checks corroborate but do not replace the exact matrix identities and analytical density argument above.

## Relationship to prior work

Almeida et al. [1], particularly their Eqs. (2), (7)–(15), introduce the disordered diamond-chain flat-band channel, its two-hub effective reduction and a **general** transfer envelope written through abstract endpoint overlaps. Those results are used rather than claimed as new. The contribution here is to solve the *microscopic flat-band projection problem* exactly for a single symmetry-breaking bond pair and obtain its determinant-controlled endpoint Gramian, discontinuous zero-defect boundary, **sharp length-dependent ceiling**, and \(N^{-1}\) defect versus \(N/g\) beat-time law. These are not an unconditional extension to all disorder patterns. Flach et al. [2] study detangling and Fano-localization mechanisms in diamond and other flat-band lattices but not this two-endpoint effective transfer invariant. Gligorić et al. [3] analyze flux-caged diamond chains under several disorder types, without this zero-flux isolated defect and sender–receiver optimization.

## Limitations

The full chain contains dispersive modes omitted from first-order resonant projection; the result does not assert exact full-channel transfer bounds at arbitrary finite \(g\), or uniform control over arbitrarily long waiting times. The numerical verification is finite and is not an independent audit. At rational frequency ratios, the exact supremum can be below the envelope, and no generic equality is asserted. At \(\delta=0\), transmission is zero despite the discontinuous limiting envelope. Since the general two-hub formula was known, the originality claim concerns the computed microscopic projector and associated sharp finite-size design law, not general star-network spectral theory.

## References

[1] G. M. A. Almeida, R. F. Dutra, A. M. C. Souza, M. L. Lyra, F. A. B. F. de Moura, *Flat-band quantum communication induced by disorder*, arXiv:2307.15360 (first posted 28 July 2023), Phys. Rev. A 108, 022407 (2023), https://arxiv.org/html/2307.15360v1.

[2] S. Flach, D. Leykam, J. D. Bodyfelt, P. Matthies, A. S. Desyatnikov, *Detangling Flat Bands into Fano Lattices*, arXiv:1311.5689 (2013), EPL 105, 30001 (2014), https://arxiv.org/abs/1311.5689.

[3] G. Gligorić, D. Leykam, A. Maluckov, *Influence of different disorder types on Aharonov-Bohm caging in the diamond chain*, arXiv:1909.07055 (2019), Phys. Rev. A 101, 023839 (2020), https://arxiv.org/abs/1909.07055.
