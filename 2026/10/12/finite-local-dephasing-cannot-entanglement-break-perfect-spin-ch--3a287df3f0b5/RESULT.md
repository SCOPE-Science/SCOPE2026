# Finite local dephasing cannot entanglement-break perfect spin-chain transfer

## Finding
Let a finite chain of qubits have a Hamiltonian that preserves total excitation number and has the polarized vacuum as an eigenstate. Prepare every site except one input site in the vacuum and subject every site to independent pure dephasing at the same finite rate. Write the noiseless one-excitation transition amplitude from input site \(j\) to output site \(k\) at time \(t\) as
\[
f_{kj}(t)=\langle k|e^{-it(H_1-E_0I)}|j\rangle .
\]
Then the reduced one-qubit transfer channel is entanglement breaking exactly when \(f_{kj}(t)=0\). For the convention \(\Lambda_t(|0\rangle\langle1|)=c_{kj}(t)|0\rangle\langle1|\), its transferred coherence is
\[
c_{kj}(t)=e^{-\kappa t}\overline{f_{kj}(t)}.
\]
The adjoint matrix unit \(|1\rangle\langle0|\) has coefficient \(e^{-\kappa t}f_{kj}(t)\). Thus at any finite time of noiseless perfect transfer, adding finite-rate dephasing does not make the channel entanglement breaking.

For the engineered mirror-inverting chain studied by Clark, Klein, Bruderer and Jaksch, the mirror time is \(\tau=\pi/J\) and \(|f_{\bar j j}(\tau)|=1\). Therefore its dephasing-only transfer channel is never entanglement breaking at \(\tau\), for any finite chain length and any finite \(\kappa\). If \(p_{\bar j}(\tau)\) is the output-site excitation probability for an excited input, the negative eigenvalue of the partially transposed normalized Choi state is
\[
\lambda_- = \frac{1-p_{\bar j}(\tau)-\sqrt{(1-p_{\bar j}(\tau))^2+4e^{-2\kappa\tau}}}{4}<0.
\]
In particular,
\[
\lambda_-\le \frac{1-\sqrt{1+4e^{-2\kappa\tau}}}{4}<0,
\]
which is a chain-length-independent analytic certificate for fixed \(J\) and \(\kappa\).

## Assumptions and scope
The Hamiltonian is time independent, preserves excitation number, and leaves the vacuum invariant up to phase. The noise is exactly independent local Markovian pure dephasing with a common nonnegative rate \(\kappa\), in the convention \(\frac{\kappa}{2}(Z\rho Z-\rho)\) on each spin. The channel is formed by placing an arbitrary qubit at one site, placing all other spins in the vacuum, evolving for a finite time, and tracing out every site except the chosen output site. The theorem concerns entanglement breaking of this reduced one-qubit channel. It does not claim that transfer fidelity stays large, and it does not cover relaxation, thermal excitation, depolarization, spatially correlated dephasing, non-Markovian noise, unequal dephasing rates, or initial states outside the vacuum-plus-one-excitation sector.

## Proof
Let \(|\Omega\rangle\) denote the vacuum and \(|m\rangle\) the state with one excitation at site \(m\). Because the Hamiltonian preserves excitation number, \(H|\Omega\rangle=E_0|\Omega\rangle\) and the one-excitation subspace evolves under a matrix \(H_1\).

Consider the operator \(X_m=|\Omega\rangle\langle m|\). For a local dephasing term at a site other than \(m\), the two basis states defining \(X_m\) have the same \(Z\)-eigenvalue, so that term annihilates \(X_m\). At site \(m\) their \(Z\)-eigenvalues are opposite, hence
\[
\frac{\kappa}{2}\sum_{\ell=1}^N (Z_\ell X_m Z_\ell-X_m)=-\kappa X_m.
\]
Therefore the entire vacuum-to-one-excitation coherence sector is an eigenspace of the dephasing superoperator with eigenvalue \(-\kappa\). The Hamiltonian part only mixes the operators \(X_m\), so on this sector the two generators commute. Starting with \(X_j\), the noiseless evolution is \(e^{-itE_0}|\Omega\rangle\langle j|e^{itH_1}\), and with dephasing this gives
\[
X_j(t)=e^{-\kappa t}\sum_m \overline{\langle m|e^{-it(H_1-E_0I)}|j\rangle}\,X_m.
\]
After all sites except \(k\) are traced out, the trace of \(X_m\) vanishes for \(m\ne k\), and \(X_k\) reduces to \(|0\rangle\langle1|\). This gives the stated complex coefficient, not just its modulus.

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
with \(0\le p_k(t)\le1\). Apply the channel to the second factor of the normalized maximally entangled state. After partial transpose on the output, the two uncoupled diagonal entries are \(1/2\) and \(p_k(t)/2\), and the block on \(|01\rangle,|10\rangle\) is
\[
\frac12\begin{pmatrix}0&c_{kj}(t)\\ \overline{c_{kj}(t)}&1-p_k(t)\end{pmatrix}.
\]
Its determinant is \(-|c_{kj}(t)|^2/4\). Thus it has one strictly negative eigenvalue exactly when \(c_{kj}(t)\ne 0\). For two-qubit states, positivity of the partial transpose is equivalent to separability, and a channel is entanglement breaking exactly when its Choi state is separable. Since \(e^{-\kappa t}>0\) for finite \(\kappa t\), entanglement breaking occurs exactly when \(f_{kj}(t)=0\).

Clark et al. use engineered couplings for which mirror inversion occurs at \(\tau=\pi/J\), so \(|f_{\bar j j}(\tau)|=1\). Substitution gives the stated strictly negative Choi partial-transpose eigenvalue for every finite \(\kappa\). For fixed \(x=|c_{\bar j j}(\tau)|>0\), the function \(y\mapsto(y-\sqrt{y^2+4x^2})/4\) is increasing for \(y\ge0\). Since \(y=1-p_{\bar j}(\tau)\le1\), its value at \(y=1\) gives the displayed bound.

## Verification
The accompanying `verify_dephasing_channel.py` checks the dephasing eigenoperator identity combinatorially for multiple chain sizes and checks the Choi-block determinant, eigenvalue formula and norm-based bound over a deterministic grid. Its recorded output is in `verification_output.txt` and ends with `VERIFY_OK`. These finite checks are regression tests only; the all-length statement and the complex-conjugation convention are proved algebraically above. For example, for two sites with \(E_0=0\) and \(H_1=g\begin{pmatrix}0&1\\1&0\end{pmatrix}\), \(g>0\), at \(t=\pi/(2g)\) the propagator is \(-i\begin{pmatrix}0&1\\1&0\end{pmatrix}\). The coefficient on \(|0\rangle\langle1|\) for transfer from site 1 to 2 is then \(i e^{-\kappa t}\), not \(-i e^{-\kappa t}\).

## Relationship to prior work
Clark, Klein, Bruderer and Jaksch numerically found that local dephasing did not make their mirror-inverting chain entanglement breaking over the broad parameter range they investigated. Their Section 7.2.2 describes the conclusion through numerical partial-transpose eigenvalues and a fitted effective noise model; their analytic commutation argument in Section 7.2.1 is specific to local decay, and they state that coherent and dissipative contributions do not commute for dephasing. The present result uses a smaller invariant operator sector: although the full generators need not commute, the vacuum-to-one-excitation coherence sector is an exact dephasing eigenspace. This is enough to decide entanglement breaking without solving the population dynamics.

Jeske, Vogt and Cole later considered the same engineered perfect-transfer coupling profile under spatially correlated noise. Their paper focuses on transfer quality and correlation length; in the uncorrelated limit it describes dephasing-induced spreading, while for long correlations it notes loss of phase coherence to the ground state. Bayat and Omar treat a different transfer architecture and add repeated measurements to suppress dephasing. The distinction here is the exact coherence factor and the resulting Choi criterion for the reduced channel under independent equal-rate dephasing.

## Limitations
The theorem is exact only for the stated independent equal-rate pure-dephasing Lindbladian and a vacuum-initialized number-conserving chain. Unequal rates destroy the scalar action of the dissipator on the vacuum-to-one-excitation coherence sector, and spatial correlations change the generator. The theorem proves persistence of some channel entanglement, not useful fidelity: the negative Choi eigenvalue tends to zero as \(\kappa t\to\infty\), and strong dephasing can make the transmitted state operationally poor even though the channel is not exactly entanglement breaking at finite rate. Other literature may contain the same invariant-sector argument.

## References
1. S. R. Clark, A. Klein, M. Bruderer, D. Jaksch, “Graph state generation with noisy mirror-inverting spin chains,” arXiv:0705.3584v1; New Journal of Physics 9, 202 (2007), DOI 10.1088/1367-2630/9/6/202.
2. J. Jeske, N. Vogt, J. H. Cole, “Excitation- and state-transfer through spin chains in the presence of spatially correlated noise,” arXiv:1308.3042v1; Physical Review A 88, 062333 (2013).
3. A. Bayat, Y. Omar, “Measurement-Assisted Quantum Communication in Spin Channels with Dephasing,” arXiv:1502.03468; New Journal of Physics 17, 103041 (2015).
