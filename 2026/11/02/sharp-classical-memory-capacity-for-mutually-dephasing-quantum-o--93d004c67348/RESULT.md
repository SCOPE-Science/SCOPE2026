# Sharp classical-memory capacity for mutually dephasing quantum observations

## Finding

A qubit experiences a fixed classical phase memory with \(M\ge2\) sectors: the memory label \(s\in\{1,\ldots,M\}\) is sampled once with probability \(p_s>0\), \(\sum_s p_s=1\), and retained throughout an experiment. In sector \(s\), the qubit evolves under \(U_s(t)=\exp(-\mathrm{i}\omega_st Z)\), with \(\omega_s\in\mathbb R\). Write
\[
\gamma(t)=\sum_{s=1}^M p_s\exp(-2\mathrm{i}\omega_s t).
\]
The reduced channel across any interval of length \(t\), with a causal break and fresh system preparation at its start, is completely dephasing in the \(Z\)-basis exactly when \(\gamma(t)=0\).

**Theorem (capacity, rigidity, and forced hidden coherence).**

1. If \(K\) observation times have completely dephasing pairwise intervening channels, then \(K\le M\). This bound is attained for every integer \(M\ge2\).
2. For any \(M\) observation times, their mean squared residual channel visibility satisfies the sharp, weight-dependent inequality
\[
 \frac{1}{M(M-1)}\sum_{i\ne j}|\gamma(t_i-t_j)|^2
 \ge \frac{M\sum_{s=1}^{M}p_s^2-1}{M-1}.
\]
For *every* strictly positive choice of \(p_s\), some frequency spectrum and regularly spaced times attain equality. In particular, exact pairwise dephasing at \(M\) times requires uniform memory weights.
3. For regularly spaced times \(t_k=k\tau\), \(k=0,\ldots,M-1\), with \(\tau>0\), simultaneous complete dephasing is possible **if and only if**
\[
 p_s=\frac1M\quad(1\le s\le M),\qquad
 \big\{\exp(2\mathrm{i}\omega_s\tau):1\le s\le M\big\}
 =\big\{\zeta\exp(2\pi\mathrm{i}j/M):0\le j<M\big\}
\]
for some unit complex number \(|\zeta|=1\), with multiplicities understood. Thus the optimal equally spaced phase spectrum is rigid up to relabeling and a common rotation.
4. At any such saturation, take the \(N=M-1\) intervening intervals, with **the same** memory label retained across all intervals, and normalize the process Choi operator to unit trace. Its nonzero eigenvalues are exactly
\[
 \lambda_k=2^{-N}\binom Nk,\qquad k=0,\ldots,N.
\]
Its relative entropy of coherence, with natural logarithms and complete dephasing on every Choi input/output leg, is
\[
 \mathcal C_{\rm rel}=N\ln2-H\big(\operatorname{Bin}(N,\tfrac12)\big),
\]
where \(H\) is Shannon entropy in nats. In particular, for \(N\to\infty\),
\[
 \mathcal C_{\rm rel}
 =N\ln2-\tfrac12\ln(\pi eN/2)+o(1).
\]
This exact process-level coherence is forced by maximal pairwise channel dephasing; it is not a separately optimized value.

**Physical realization.** For \(M=2^r\) and any \(r\ge1\), use \(r\) maximally mixed, unreset environmental qubits with
\[
 H=g Z_S\sum_{j=0}^{r-1}2^jZ_{E_j},\qquad g>0,
 \qquad \tau=\frac{\pi}{2Mg}.
\]
The \(M\) observation times \(0,\tau,\ldots,(M-1)\tau\) have all \(\binom M2\) pairwise channels completely dephasing. For two environmental qubits, this gives **four** mutually dephasing observation times and three intervals, with process coherence \(\frac34\ln3\) nats.

## Assumptions and scope

The system is one qubit with the computational \(Z\)-basis. The memory is a static, finite classical label: it may be realized as a diagonal environmental state in an orthonormal basis, with controlled Hamiltonian \(Z_S\otimes\sum_s\omega_s|s\rangle\langle s|\). Each \(p_s\) is strictly positive; repeated frequencies are allowed. An intervening reduced channel refers to a causal-break experiment in which the system is freshly prepared at the interval's start, without resetting the memory. Since the memory populations are conserved, an unconditional causal-break test (prior outcomes averaged, without postselection) uses the same weights at every interval. Conditioning on earlier measurement outcomes can change the posterior memory weights and is outside the pairwise-channel assertion. Exact pairwise complete dephasing means annihilation of both computational-basis off-diagonal matrix units, not merely dephasing from a fixed origin. The result makes no assertion about genuinely quantum memory or arbitrary system–environment Hamiltonians.

## Proof

**Channel reduction.** For a matrix unit \(|0\rangle\langle1|\),
\[
 U_s(t)|0\rangle\langle1|U_s(t)^\dagger
 =e^{-2\mathrm{i}\omega_st}|0\rangle\langle1|.
\]
Averaging gives the claimed multiplier \(\gamma(t)\). Diagonal matrix units are fixed, hence complete dephasing is equivalent to \(\gamma(t)=0\).

**Sharp memory-size bound.** For arbitrary times \(t_0,\ldots,t_{K-1}\), introduce vectors
\[
 v_k=(\sqrt{p_s}\,e^{2\mathrm{i}\omega_st_k})_{s=1}^M\in\mathbb C^M.
\]
They have unit norm, and \(\langle v_j,v_k\rangle\) is either \(\gamma(t_j-t_k)\) or its complex conjugate, depending on inner-product convention. The requested pairwise dephasing makes the \(K\) vectors orthonormal, so \(K\le M\). The Fourier construction below attains equality, proving sharpness.

**Exact quantitative penalty.** Now take \(K=M\). Let \(V\) be the square matrix whose rows are the \(v_k\), and \(G=VV^\dagger\). Its diagonal entries are \(1\), and its off-diagonal squared moduli are the required squared visibilities. The diagonal entries of \(V^\dagger V\) are \(Mp_s\), independently of all times and frequencies. Therefore
\[
 \operatorname{Tr}(G^2)=\operatorname{Tr}[(V^\dagger V)^2]
 \ge\sum_s(Mp_s)^2.
\]
Subtracting the \(M\) diagonal squares of \(G\) and dividing by \(M(M-1)\) proves the inequality. Equality holds precisely when the columns of \(V\) are orthogonal. For any positive weights choose \(t_k=k\tau\) and \(e^{2\mathrm{i}\omega_s\tau}=\zeta e^{2\pi\mathrm{i}(s-1)/M}\); then the columns of \(V\) are orthogonal by a finite geometric sum. Uniformity of \(p_s\) is necessary for the right side to vanish, by strict convexity of squared weights.

**Rigidity of regular-clock saturation.** If all \(M\) observation vectors are orthonormal, the square \(V\) is unitary. Its column \(s\) has squared norm \(Mp_s\), hence \(p_s=1/M\). Put \(z_s=e^{2\mathrm{i}\omega_s\tau}\). Orthogonality of distinct columns yields
\[
 0=\sum_{k=0}^{M-1}(z_s/ z_t)^k
 \qquad (s\ne t).
\]
The ratio is nonunity and its \(M\)-th power is unity. Fixing one \(z_t\), all the other \(M-1\) phases must be the distinct nontrivial \(M\)-th roots times \(z_t\). Conversely, uniform weights and the stated root spectrum make all the time vectors orthogonal. This proves the equivalence, including necessity for *all* \(M\ge2\).

**Entire process spectrum.** In sector \(s\), the normalized one-interval Choi vector is, up to a physically irrelevant global phase,
\[
 |\phi_s\rangle=(|0_L\rangle+z_s|1_L\rangle)/\sqrt2,
 \quad |0_L\rangle=|00\rangle,\quad |1_L\rangle=|11\rangle.
\]
Retention of the same classical memory label gives the normalized multi-time process state
\[
 \rho_N=\frac1M\sum_{s=1}^M
  \big(|\phi_s\rangle\langle\phi_s|\big)^{\otimes N}.
\]
Let \(|D_k\rangle\) be the normalized symmetric logical \(N\)-qubit Dicke vector of weight \(k\). Its branch amplitude is \(2^{-N/2}\sqrt{\binom Nk}z_s^k\). Consequently,
\[
 \langle D_k|\rho_N|D_l\rangle
 =\frac{\sqrt{\binom Nk\binom Nl}}{2^N}
   \frac1M\sum_s z_s^{k-l}.
\]
At saturation, the last average vanishes whenever \(0<|k-l|<M\). Since \(0\le k,l\le N=M-1\), it vanishes for every \(k\ne l\). Hence \(\rho_N\) is diagonal in the Dicke basis and has precisely the claimed \(M\) positive eigenvalues. Full dephasing of its physical Choi legs has \(2^N\) nonzero equal diagonal entries \(2^{-N}\), so its entropy is \(N\ln2\). The relative-entropy coherence \(S(\Delta\rho_N)-S(\rho_N)\) follows.

**Asymptotic entropy.** For \(K\sim\operatorname{Bin}(N,1/2)\), Stirling's formula uniformly in the central window \(|K-N/2|\le N^{2/3}\) gives
\[
 -\ln\big(2^{-N}\binom NK\big)
 =\tfrac12\ln(\pi N/2)+\frac{2(K-N/2)^2}{N}+o(1)
\]
in expectation over that window. Standard Chernoff bounds make the tail contribution \(o(1)\) because the binomial logarithm is at most \(N\ln2\). Using \(\mathbb E(K-N/2)^2=N/4\) yields the entropy asymptotic in the finding.

**Spin construction.** The environment eigenvalues of \(\sum_{j=0}^{r-1}2^j Z_{E_j}\) are exactly the odd integers \(-(M-1),-(M-3),\ldots,M-1\), once each. At the specified \(\tau\), their sector phases \(e^{2\mathrm{i}\omega_s\tau}\) form a rotated complete set of \(M\)-th roots. Uniformly mixed memory supplies weights \(1/M\). At \(M=4\), the Dicke eigenvalues are \((1,3,3,1)/8\), yielding \(\mathcal C_{\rm rel}=\frac34\ln3\). All boundaries follow from the same arguments; there is no thermodynamic-limit assumption in any finite formula.

## Verification

Execute `python verify.py` with NumPy available. The standalone checker reconstructs the binary-weight Ising spectra for memory sizes \(2,4,8,16\), verifies every pairwise channel cancellation, diagonalizes independent Gram matrices and, for memory sizes up to \(8\), reconstructs the full normalized process density matrices directly. It also tests the sharp visibility inequality at arbitrary time grids and its equality with nonuniform memory weights. A separate direct Choi reconstruction checks the channel phase convention. A successfully executed run produced **326 finite assertions**. These finite checks are consistency tests; the analytic proof above establishes the unbounded-size statements.

## Relationship to prior work

Sajnok and Costa, arXiv:2610.08241v1 (first public version October 6, 2026), define coherence for multi-time processes and exhibit a two-memory-qubit Ising model with three pairwise incoherent channels at three observation times. Their main-text equations (25)–(45) provide the dephasing model and a two-interval process matrix. Appendix A gives linear multi-time coherence while hiding **fixed-origin**, rather than all pairwise, channel coherence. The result above instead determines the sharp arbitrary-number bound on **mutually pairwise** dephasing observations, a necessary-and-sufficient uniform-clock saturation classification, a sharp quantitative penalty for memory imbalance, and the forced process spectrum at saturation.

The general process-tensor framework and finite-dimensional phase orthogonality are established tools. The eigenvalues of a uniformly sampled regular phase-state ensemble also have a known binomial-modulo-frequency formulation in multi-copy state-discrimination literature, including the published record *Exact multi-copy discrimination law for regular rebit polygons* (published-finding corpus record `9659df84ea8e`). The binomial-spectrum identity should not be regarded as independent mathematical priority over that general ensemble result. What is asserted here is the **combined physical dephasing-capacity and rigidity classification** and its consequent process-coherence statement; the latter spectral calculation is supplied as a transparent self-contained consequence. No claim of independent priority certification is made.

## Limitations

The bound and rigidity hold for a conserved **classical** phase label and exact projective-basis dephasing. They do not constrain quantum memories that coherently evolve, arbitrary noncommuting interactions, imperfectly implemented controls, or generic entanglement measurements. The quantitative visibility bound is universal over frequency choices and time grids but need not be attained when a frequency spectrum is externally fixed. Equally spaced times are required only for the root-of-unity **rigidity characterization**, not for the dimension bound or visibility inequality. The asymptotic coherence law concerns the saturated family with \(M=N+1\); it is not a statement about arbitrary temporal sampling. Existing phase-ensemble spectral results overlap with the entropy component, as explicitly acknowledged; full priority across process-tensor literature remains open to independent assessment.

## References

1. K. Sajnok and F. Costa, *Multi-time advantage for certifying quantum coherence*, arXiv:2610.08241v1 (October 6, 2026), https://arxiv.org/html/2610.08241v1. Relevant equations (25)–(45) and Appendix A, especially (66)–(73).
2. G. E. Fux et al., *Process Tensor Approaches to Non-Markovian Quantum Dynamics*, arXiv:2509.07661v1 (September 9, 2025), https://arxiv.org/html/2509.07661v1. Relevant process-tensor formalism in Section II.
3. *Exact multi-copy discrimination law for regular rebit polygons*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-multi-copy-discrimination-law-for-regular-rebit-polygons--9659df84ea8e. Title and abstract-level summary available; detailed full text was not accessible during the present comparison.
