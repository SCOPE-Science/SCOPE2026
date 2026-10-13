# A sharp \(\sqrt{n\log n}\) ergotropy law for cold collective decay

## Finding
For every integer \(n\ge 1\), prepare \(n\) noninteracting identical qubits in the maximally mixed state, then expose them to zero-temperature *purely collective* spontaneous emission until stationarity. Let \(\mathcal W_n\) denote the ergotropy of the final state for the Hamiltonian \(H_n=\omega\sum_{i=1}^n |1\rangle_i\langle1|\), with \(\omega>0\). Then
\[
\boxed{\lim_{n\to\infty}\frac{\mathcal W_n}{\omega\sqrt{n\log n}}=\frac12.}
\]
The logarithm is natural. This is a sharp, subextensive scaling law for the number of qubits, including the leading constant. The finite-size passive rearrangement used in the proof is explicit below. The collective stationary-state decomposition and the general principle of passive spectral ordering are prior results, not asserted to be new.

## Assumptions and scope
The Hilbert space is \((\mathbb C^2)^{\otimes n}\). Write \(J_-=\sum_{i=1}^n |0\rangle_i\langle1|\) and \(J_+=J_-^\dagger\). The initial state is \(\rho_0=I/2^n\), and the Markovian evolution has generator
\[
\mathcal L(\rho)=-i[H_n,\rho]+\gamma\bigl(J_-\rho J_+-\tfrac12\{J_+J_-,\rho\}\bigr),\qquad \gamma>0.
\]
There is no individual decay, pumping, dephasing, interaction between qubits, or bath excitation. Define \(\rho_\infty=\lim_{t\to\infty}e^{t\mathcal L}(\rho_0)\). Ergotropy means \(\mathcal W_n=\operatorname{tr}(H_n\rho_\infty)-\min_U\operatorname{tr}(H_n U\rho_\infty U^\dagger)\), the minimum taken over arbitrary global unitaries. The time needed to reach stationarity and the cost of those unitaries are not counted.

Define, for \(0\le k\le\lfloor n/2\rfloor\),
\[
 g_{n,k}=\binom nk-\binom n{k-1},\qquad \lambda_{n,k}=\frac{n-2k+1}{2^n},\qquad \binom n{-1}=0.
\]
For \(r\in\{1,\dots,2^n\}\), let \(e_n(r)\) be the excitation count occupying the \(r\)-th lowest-energy slot, including its degeneracy:
\[
 e_n(r)=\min\bigl\{s\in\{0,\dots,n\}:\sum_{\ell=0}^s\binom n\ell\ge r\bigr\}.
\]
The stationary nonzero eigenvalues are \(\lambda_{n,k}\), each with multiplicity \(g_{n,k}\), ordered by increasing \(k\); their cumulative ranks equal \(R_{n,k}=\binom nk\). Thus the exact finite-size expression is
\[
\frac{\mathcal W_n}{\omega}=\sum_{k=0}^{\lfloor n/2\rfloor}\lambda_{n,k}\left[k g_{n,k}-\sum_{r=\binom n{k-1}+1}^{\binom nk}e_n(r)\right].
\]
It gives \(\mathcal W_1=\mathcal W_2=\mathcal W_3=0\) and \(\mathcal W_4=\omega/16\). This exact rearrangement formula is an intermediate tool, not an independent novelty assertion.

## Proof
**1. Conserved spin-sector weights and stationary eigenvalues.** In the Schur–Weyl decomposition, the \(k\)-th irreducible spin sector has angular momentum \(j=n/2-k\), magnetic ladder dimension \(2j+1=n-2k+1\), and multiplicity \(g_{n,k}\). Collective lowering acts on the spin ladder and preserves the multiplicity index. Because \(\rho_0=I/2^n\), the initial state has population \((2j+1)/2^n\) in each individual spin ladder. Zero-temperature emission sends each such ladder to its unique lowest-weight vector \(|j,-j\rangle\), while preserving this population. The Hamiltonian commutes with the spin-sector projectors. Consequently \(\rho_\infty\) has exactly \(g_{n,k}\) equal nonzero eigenvalues \(\lambda_{n,k}\) at excitation count \(k\); all other eigenvalues vanish. Their total mass is one because \(\sum_k g_{n,k}(n-2k+1)=2^n\). The strict order \(\lambda_{n,k}>\lambda_{n,k+1}\) holds whenever both tiers exist. This reduction is the zero-temperature specialization of the established collective-stationary-state structure [1].

**2. Exact passive sorting.** Passive rearrangement assigns decreasing state eigenvalues to increasing Hamiltonian eigenvalues. The first \(R_{n,k}=\sum_{a=0}^{k}g_{n,a}=\binom nk\) positive eigenvalues occupy energy slots \(e_n(1),\ldots,e_n(R_{n,k})\); the telescoping identity gives the displayed finite-size formula. Equivalently define a rank-valued random variable \(Q_n\) by \(\Pr\{Q_n=r\}=\lambda_{n,k}\) for \(\binom n{k-1}<r\le\binom nk\). Then
\[
\frac{E_{\mathrm{pas},n}}{\omega}=\mathbb E[e_n(Q_n)],
\quad
\frac{E_{\mathrm{ss},n}}{\omega}=\frac n2-\mathbb E[J_n],
\]
where \(J_n=n/2-k\) has distribution \(\Pr\{J_n=n/2-k\}=g_{n,k}\lambda_{n,k}\).

**3. Rank and energy quantiles.** Set \(R_n=\binom n{\lfloor n/2\rfloor}\). Stirling's formula gives \(R_n=2^n n^{-1/2+o(1)}\). For every fixed \(c>0\), with \(m_n(c)=\lfloor n/2-c\sqrt{n\log n}\rfloor\), binomial moderate deviations give
\[
 B_n(c):=\sum_{\ell=0}^{m_n(c)}\binom n\ell=2^n n^{-2c^2+o(1)},\qquad
 \binom n{m_n(c)}=2^n n^{-1/2-2c^2+o(1)}.
\]
For completeness, the upper estimate for \(B_n(c)\) is the Hoeffding binomial-tail bound. For the matching logarithmic lower estimate, sum the last \(\lfloor\sqrt n/\log n\rfloor\) binomial coefficients below \(m_n(c)\). Stirling's formula at these indices gives uniformly \(2^n n^{-1/2-2c^2+o(1)}\), and multiplying by the window size yields the claimed power of \(n\). This is valid since the displacement is \(o(n^{2/3})\).

Set \(Y_n=(n/2-e_n(Q_n))/\sqrt{n\log n}\). Every positive rank satisfies \(Q_n\le R_n\). For fixed \(0<c<1/2\), \(B_n(c)>R_n\) eventually, so \(Y_n\ge c\) with probability one. For fixed \(c>1/2\), choose \(a>0\) such that \(1/2+2a^2<2c^2\). The binomial estimates yield \(B_n(c)<\binom n{m_n(a)}\) eventually. On \(\{Y_n>c\}\), the ranked eigenvalue therefore comes from a sector with \(k\le m_n(a)\), and hence \(J_n\ge a\sqrt{n\log n}\).

**4. Spin-moment control.** Let \(\mathbf J=\tfrac12\sum_i(\sigma_x^{(i)},\sigma_y^{(i)},\sigma_z^{(i)})\). Since the initial state is maximally mixed, cross terms have zero trace and
\[
\mathbb E[J_n(J_n+1)]=\operatorname{tr}(\rho_0\mathbf J^2)=\frac{3n}{4}.
\]
Thus \(\mathbb E J_n\le\sqrt{3n/4}=O(\sqrt n)\), and Markov's inequality gives
\[
\Pr\{Y_n>c\}\le\Pr\{J_n\ge a\sqrt{n\log n}\}\le\frac{3}{4a^2\log n}\longrightarrow0.
\]
Together with the lower bound from Step 3, \(Y_n\to1/2\) in probability.

**5. Uniform integrability and the sharp coefficient.** Since \(0\le Y_n\) and the largest eigenvalue of \(\rho_\infty\) is \((n+1)/2^n\), Hoeffding's inequality gives, for every \(u\ge1\),
\[
\Pr\{Y_n>u\}\le\frac{n+1}{2^n}\sum_{\ell\le n/2-u\sqrt{n\log n}}\binom n\ell
\le (n+1)n^{-2u^2}.
\]
The right-hand side is bounded, uniformly for \(n\ge2\), by an integrable Gaussian-decay envelope in \(u\ge1\). Hence \(\{Y_n\}\) is uniformly integrable and \(\mathbb E Y_n\to1/2\). Using Step 2,
\[
\frac{\mathcal W_n}{\omega\sqrt{n\log n}}
=\mathbb E Y_n-\frac{\mathbb E J_n}{\sqrt{n\log n}}\longrightarrow\frac12.
\]
This proves the claim for every positive \(\omega,\gamma\) under the stated model.

## Verification
The standalone script `artifacts/verify.py` independently forms the collective lowering and total-spin matrices in computational bases for \(n\le7\), identifies dark-sector spin multiplicities by numerical diagonalization, and checks the stationary energy against the closed formula. It also independently computes the exact passive rearrangement for \(1\le n<40\), verifies \(\mathcal W_4/\omega=1/16\), and prints finite-size normalized values. Execution returned `VERIFY_OK`. These checks do not establish the infinite-size limit; the moderate-deviation and moment argument above does. Run from the package directory using `python3 artifacts/verify.py` after installing the package listed in `artifacts/requirements.txt`.

## Relationship to prior work
Ahmadi, Ravichandran, Mazurek, Barzanjeh and Horodecki [1] already derive the collective-dissipation steady state \(\rho_{\rm SS}=\bigoplus_j(\chi_j\otimes\tau_j)\), explicitly give the Gibbs-product sector populations, calculate steady-state ergotropy, and show its activation and dependence on system size. Their Eq. (88) implies the eigenvalue formula used here at zero reservoir temperature. The present mathematical claim is **only** the sharp \(\sqrt{n\log n}\) thermodynamic-limit law with coefficient \(1/2\) at the simultaneous endpoint of maximally mixed input and zero-temperature collective emission. The published thermodynamic-limit population-inversion test in [1] treats interior thermal parameters and does not give this endpoint growth exponent or coefficient.

Çakmak [2] introduced ergotropy analysis under collective thermal dissipation, including ground and random initial-state scaling, but not the present maximally mixed input with sharp asymptotic work law. Watanabe, Chen and Venkatesh [3] give asymptotic ergotropy-to-energy bounds for a different collective-charging framework; the available description does not imply the cold-decay spectral-quantile limit here. We do not claim a new stationary-state formula, an alternative proof of a result already in [1], or a universal law across different quantum-battery dynamics.

## Limitations
The theorem addresses an ideal collective Markovian Lindbladian, a maximally mixed input, exact zero bath temperature, noninteracting qubits, and *unrestricted global-unitary* ergotropy. It says nothing about nonzero individual dissipation, realistic finite-time charging, the cost or circuit depth of extraction, the extension to finite input or bath temperature, or whether physical device noise preserves this scaling. The large-system constant is asymptotic and finite-size convergence is slow because the \(O(\sqrt n)\) spin-moment correction competes with the leading \(\sqrt{n\log n}\) term. Searches cannot exclude unpublished or differently indexed derivations.

## References
[1] B. Ahmadi, A. B. Ravichandran, P. Mazurek, S. Barzanjeh, and P. Horodecki, *Harnessing Environmental Noise for Quantum Energy Storage*, arXiv:2510.06384v1 (first posted 2025-10-07), https://arxiv.org/html/2510.06384v1 .

[2] B. Çakmak, *Ergotropy from coherences in an open quantum system*, Physical Review E 102, 042111 (2020), arXiv:2005.08489, https://arxiv.org/pdf/2005.08489 .

[3] G. Watanabe, C. Chen, and B. P. Venkatesh, *Scaling law of asymptotic freedom in collective charging of quantum batteries*, arXiv:2606.10054v1 (2026), https://arxiv.org/abs/2606.10054 .
