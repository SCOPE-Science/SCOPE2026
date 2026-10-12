# Finite local dephasing cannot entanglement-break perfect spin-chain transfer
## Finding
Let a finite chain of qubits have a Hamiltonian that preserves total excitation number and has the polarized vacuum as an eigenstate. Prepare every site except one input site in the vacuum and subject every site to independent pure dephasing at the same finite rate. Write the noiseless one-excitation transition amplitude from input site \(j\) to output site \(k\) at time \(t\) as
\[
f_{kj}(t)=\langle k|e^{-it(H_1-E_0I)}|j\rangle .
\]
Then the reduced one-qubit transfer channel is entanglement breaking exactly when \(f_{kj}(t)=0\). Its transferred coherence is
\[
c_{kj}(t)=e^{-\kappa t}f_{kj}(t).
\]
Thus any finite-time perfect transfer remains non-entanglement-breaking for every finite dephasing rate.

For the engineered mirror-inverting chain studied by Clark, Klein, Bruderer and Jaksch, the mirror time is \(\tau=\pi/J\) and \(|f_{\bar j j}(\tau)|=1\). Therefore its dephasing-only transfer channel is never entanglement breaking at \(\tau\), for any finite chain length and any finite \(\kappa\). If \(p_{\bar j}(\tau)\) is the output-site excitation probability, the negative eigenvalue of the partially transposed normalized Choi state is
\[
\lambda_- = \frac{1-p_{\bar j}(\tau)-\sqrt{(1-p_{\bar j}(\tau))^2+4e^{-2\kappa\tau}}}{4}<0.
\]
In particular,
\[
\lambda_-\le \frac{1-\sqrt{1+4e^{-2\kappa\tau}}}{4}<0,
\]
which is a chain-length-independent analytic certificate of non-entanglement-breaking behavior.

## Assumptions and scope
The Hamiltonian is time independent, preserves excitation number, and leaves the vacuum invariant up to phase. The noise is exactly independent local Markovian pure dephasing with a common rate \(\kappa\), in the convention \(\frac{\kappa}{2}(Z\rho Z-\rho)\) on each spin. The channel is formed by placing an arbitrary qubit at one site, placing all other spins in the vacuum, evolving for a finite time, and tracing out every site except the chosen output site. The theorem concerns entanglement breaking of this reduced one-qubit channel. It does not claim that transfer fidelity stays large, and it does not cover relaxation, thermal excitation, depolarization, spatially correlated dephasing, non-Markovian noise, unequal dephasing rates, or initial states outside the vacuum-plus-one-excitation sector.

## Proof
Let \(|\Omega\rangle\) denote the vacuum and \(|m\rangle\) the state with one excitation at site \(m\). Because the Hamiltonian preserves excitation number, \(H|\Omega\rangle=E_0|\Omega\rangle\) and the one-excitation subspace evolves under a matrix \(H_1\).

Consider the operator \(X_m=|\Omega\rangle\langle m|\). For a local dephasing term at a site other than \(m\), the two basis states defining \(X_m\) have the same \(Z\)-eigenvalue, so that term annihilates \(X_m\). At site \(m\) their \(Z\)-eigenvalues are opposite, hence
\[
\frac{\kappa}{2}\sum_{\ell=1}^N (Z_\ell X_m Z_\ell-X_m)=-\kappa X_m.
\]
Therefore the entire vacuum-to-one-excitation coherence sector is an eigenspace of the dephasing superoperator with eigenvalue \(-\kappa\). The Hamiltonian part only mixes the operators \(X_m\), so on this sector the two generators commute. Starting with \(X_j\), one obtains
\[
X_j(t)=e^{-\kappa t}\sum_m \overline{\langle m|e^{-it(H_1-E_0I)}|j\rangle}\,X_m,
\]
up to the harmless convention of complex conjugating the amplitude. After all sites except \(k\) are traced out, only the \(m=k\) term contributes to an output off-diagonal element. Hence the magnitude of the reduced-channel coherence coefficient is exactly \(e^{-\kappa t}|f_{kj}(t)|\).

Pure dephasing and the Hamiltonian conserve excitation number. Thus the reduced channel has the form
\[
\Lambda_t(|0\rangle\langle0|)=|0\rangle\langle0|,
\]
\[
\Lambda_t(|1\rangle\langle1|)=(1-p_k(t))|0\rangle\langle0|+p_k(t)|1\rangle\langle1|,
\]
\[
\Lambda_t(|0\rangle\langle1|)=c_{kj}(t)|0\rangle\langle1|,
\]
with \(0\le p_k(t)\le1\). The normalized Choi state has, after partial transpose on the output qubit, a nontrivial two-dimensional block
\[
\frac12\begin{pmatrix}0&c_{kj}(t)\\ \overline{c_{kj}(t)}&1-p_k(t)\end{pmatrix}.
\]
Its determinant is \(-|c_{kj}(t)|^2/4\). Therefore it has one strictly negative eigenvalue exactly when \(c_{kj}(t)\ne 0\). For two-qubit states, positivity of the partial transpose is equivalent to separability, and a channel is entanglement breaking exactly when its Choi state is separable. Since \(e^{-\kappa t}>0\) for finite \(\kappa t\), entanglement breaking occurs exactly when \(f_{kj}(t)=0\).

Clark et al. use engineered couplings for which mirror inversion occurs at \(\tau=\pi/J\), so \(|f_{\bar j j}(\tau)|=1\). Substitution gives the stated strictly negative Choi partial-transpose eigenvalue for every finite \(\kappa\).

## Verification
The accompanying `verify_dephasing_channel.py` checks the dephasing eigenoperator identity combinatorially for multiple chain sizes, checks the Choi-block determinant and eigenvalue formula over a deterministic grid, and checks the chain-length-independent negativity bound. Its recorded output is in `verification_output.txt` and ends with `VERIFY_OK`. These finite checks are regression tests only; the all-length statement is proved algebraically above.

The defining paper's full text was inspected at its Hamiltonian and mirror-time derivation, its local-noise definition, and its single-qubit dephasing subsection. It states that the dephasing result was obtained numerically over investigated chain lengths and couplings and contrasts this with an analytic commuting-generator proof supplied for local decay. A later paper by Jeske, Vogt and Cole studies perfect-transfer chains with spatially correlated dephasing and numerically evaluates transfer quality, but does not formulate an entanglement-breaking criterion; its full text contains no occurrence of “entanglement breaking”. Bayat and Omar study a different weak-end-coupling, measurement-assisted protocol for combating dephasing and do not dominate the exact reduced-channel statement here.

## Relationship to prior work
Clark, Klein, Bruderer and Jaksch numerically found that local dephasing did not make their mirror-inverting chain entanglement breaking over the broad parameter range they investigated. Their Section 7.2.2 explicitly describes the conclusion through numerical partial-transpose eigenvalues and a fitted effective noise model; their analytic commutation argument in Section 7.2.1 is specific to local decay and they state that coherent and dissipative contributions do not commute for dephasing. The present result uses a smaller invariant operator sector: although the full generators do not commute, the vacuum-to-one-excitation coherence sector is an exact dephasing eigenspace. This is enough to decide entanglement breaking without solving the population dynamics.

Jeske, Vogt and Cole later considered the same engineered perfect-transfer coupling profile under spatially correlated noise. Their paper focuses on transfer quality and correlation length; in the uncorrelated limit it describes dephasing-induced spreading, while for long correlations it notes loss of phase coherence to the ground state. It does not give the Choi/PPT equivalence proved here. Bayat and Omar treat a different transfer architecture and add repeated measurements to suppress dephasing.

Perfect-state-transfer literature indexed by MaRDI places this subject under MSC2020 \(81P45\), quantum information, communication and networks, among its classifications. That field is used here because the final claim is specifically a theorem about a one-qubit communication channel through a spin chain.

## Limitations
The theorem is exact only for the stated independent equal-rate pure-dephasing Lindbladian and a vacuum-initialized number-conserving chain. Unequal rates destroy the scalar action of the dissipator on the vacuum-to-one-excitation coherence sector, and spatial correlations change the generator. The theorem proves persistence of some channel entanglement, not useful fidelity: the negative Choi eigenvalue tends to zero as \(\kappa t\to\infty\), and strong dephasing can make the transmitted state operationally poor even though the channel is not exactly entanglement breaking at finite rate.

A residual originality risk is that an obscure or poorly indexed later source may have observed the same invariant-sector argument. Targeted database and web searches located later work on dephasing and state transfer, but no implication-equivalent entanglement-breaking theorem.

## References
1. S. R. Clark, A. Klein, M. Bruderer, D. Jaksch, “Graph state generation with noisy mirror-inverting spin chains,” arXiv:0705.3584v1 (first public 24 May 2007); New Journal of Physics 9, 202 (2007), DOI 10.1088/1367-2630/9/6/202.
2. J. Jeske, N. Vogt, J. H. Cole, “Excitation- and state-transfer through spin chains in the presence of spatially correlated noise,” arXiv:1308.3042v1; Physical Review A 88, 062333 (2013).
3. A. Bayat, Y. Omar, “Measurement-Assisted Quantum Communication in Spin Channels with Dephasing,” arXiv:1502.03468; New Journal of Physics 17, 103041 (2015).
4. A. Kay, “Perfect, efficient, state transfer and its application as a constructive tool,” International Journal of Quantum Information 8 (2010); MaRDI Q3587036, classified in quantum information/communication including MSC2020 \(81P45\).
