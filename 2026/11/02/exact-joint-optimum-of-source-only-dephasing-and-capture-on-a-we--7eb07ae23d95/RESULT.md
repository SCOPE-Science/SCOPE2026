# Exact joint optimum of source-only dephasing and capture on a weighted quantum star

## Finding

For a quantum star of \(N\ge2\) leaves with arbitrary positive couplings \(J_1,\ldots,J_N\), the mean time to irreversible capture at the central hub, when the first leaf is initially excited and only that leaf is dephased, obeys the exact identity
\[
T(\gamma,\kappa)=\frac{\Omega^2}{2a^2\gamma}+\frac{\gamma}{2a^2}+\frac{3}{\kappa}+\frac{\kappa}{4a^2},
\qquad a=J_1,\quad \Omega=\sqrt{\sum_{j=1}^N J_j^2}.
\]
For every positive pair of rates, capture occurs with probability one. The unique minimizers are
\[
\gamma_*=\Omega,\qquad \kappa_*=2\sqrt3\,a,
\qquad \min T=\frac{\Omega+\sqrt3\,a}{a^2}.
\]
The optimum noise rate depends on the entire coupling vector, whereas the optimum sink rate depends only on the input-to-hub coupling. In particular, for equal couplings \(J_j=J>0\), \(\gamma_*=J\sqrt N\), \(\kappa_*=2\sqrt3 J\), and \(\min T=(\sqrt N+\sqrt3)/J\).

## Assumptions and scope

Fix \(N\in\{2,3,\ldots\}\), positive real \(J_j\), source state \(|1\rangle\), and central state \(|h\rangle\). Work in the one-excitation space \(\mathbb C^{N+1}\) with \(\hbar=1\) and zero on-site detuning. The Hamiltonian and projectors are
\[
H=\sum_{j=1}^N J_j(|j\rangle\langle h|+|h\rangle\langle j|),
\quad P=|1\rangle\langle1|,\quad Q=|h\rangle\langle h|.
\]
For rates \(\gamma,\kappa>0\), the trace-decreasing density evolution on this space is
\[
\frac{d\rho}{dt}=\mathcal L(\rho):=-i[H,\rho]
+2\gamma\left(P\rho P-\frac12\{P,\rho\}\right)
-\frac\kappa2\{Q,\rho\},\qquad \rho(0)=P.
\]
Thus a coherence between the source and any other state decays directly at rate \(\gamma\), and occupied-hub population is removed at rate \(\kappa\). The environment causes no other loss or dephasing. Define the survival probability \(S(t)=\operatorname{tr}\rho(t)\) and mean capture time \(T=\int_0^\infty S(t)\,dt\). Neither a competing recombination channel nor arbitrary initial states are included.

## Proof

**Exact invariant reduction.** Put \(a=J_1>0\), \(b=\sqrt{\sum_{j=2}^N J_j^2}>0\), and \(\Omega=\sqrt{a^2+b^2}\). Introduce \(|s\rangle=|1\rangle\) and \(|r\rangle=b^{-1}\sum_{j=2}^N J_j|j\rangle\). The three-dimensional space spanned by \(|s\rangle,|r\rangle,|h\rangle\) is invariant under the Hamiltonian, source dephasing, and sink removal. Starting from \(P\), the density remains supported in that space; the orthogonal leaf-dark sector is never populated. In the ordered basis \((s,r,h)\),
\[
H_{\mathrm{red}}=\begin{pmatrix}0&0&a\\0&0&b\\a&b&0\end{pmatrix},
\qquad P_{\mathrm{red}}=\begin{pmatrix}1&0&0\\0&0&0\\0&0&0\end{pmatrix},
\quad Q_{\mathrm{red}}=\begin{pmatrix}0&0&0\\0&0&0\\0&0&1\end{pmatrix}.
\]

**Decay in the populated sector.** For an arbitrary complex \(3\times3\) matrix \(Z\), the real part of the Hilbert–Schmidt form is
\[
\operatorname{Re}\operatorname{tr}(Z^\dagger\mathcal L Z)
=-\gamma\|[P,Z]\|_{\mathrm F}^2
-\frac\kappa2\left(\|QZ\|_{\mathrm F}^2+\|ZQ\|_{\mathrm F}^2\right)\le0.
\]
If an eigenmatrix had a purely imaginary eigenvalue, equality would require \([P,Z]=0\) and \(QZ=ZQ=0\). These conditions force \(Z\) to be diagonal in the \((s,r,h)\) basis with diagonal \((z_s,z_r,0)\). Its eigenvalue equation then requires \([H,Z]\) to vanish, which gives \(az_s=bz_r=0\) and therefore \(Z=0\), a contradiction. Every eigenvalue of the reduced generator consequently has strictly negative real part. It follows that the integrated density \(X=\int_0^\infty\rho(t)\,dt\) is well defined and is the unique solution of \(\mathcal L X=-P\) in this sector.

**Closed integrated density.** Direct entrywise multiplication with the displayed generator verifies that
\[
X=\begin{pmatrix}
\dfrac{b^2}{2a^2\gamma}+\dfrac1\kappa+\dfrac\gamma{2a^2}+\dfrac\kappa{4a^2}
&-\dfrac{b}{2a\gamma}&\dfrac{i}{2a}\\[6pt]
-\dfrac{b}{2a\gamma}&\dfrac1\kappa+\dfrac1{2\gamma}&0\\[6pt]
-\dfrac{i}{2a}&0&\dfrac1\kappa
\end{pmatrix}
\]
satisfies \(\mathcal L X=-P\). The strict spectral decay above makes this algebraic certificate the actual integrated density, rather than merely a formal resolvent. Its trace is
\[
T=\operatorname{tr}X=\frac{b^2+a^2}{2a^2\gamma}+\frac\gamma{2a^2}+\frac3\kappa+\frac\kappa{4a^2}.
\]
The trace-decreasing equation gives \(S'(t)=-\kappa\rho_{hh}(t)\). Since \(S(t)\to0\), integration proves total capture probability \(\kappa X_{hh}=1\).

**Sharp and unique rate optimum.** Arithmetic–geometric mean gives
\[
\frac{\Omega^2}{2a^2\gamma}+\frac\gamma{2a^2}\ge\frac\Omega{a^2},
\qquad \frac3\kappa+\frac\kappa{4a^2}\ge\frac{\sqrt3}{a}.
\]
Equality in the first inequality holds exactly when \(\gamma=\Omega\); equality in the second holds exactly when \(\kappa=2\sqrt3a\). Since both variables are independent and the rate domain is strictly positive, these are the unique joint global minimizers.

**Zero-dephasing boundary.** At \(\gamma=0\), the normalized leaf state \(|d\rangle=(b|s\rangle-a|r\rangle)/\Omega\) is a dark eigenvector of \(H_{\mathrm{red}}\) with no hub amplitude. The initial source has nonzero dark weight \(|\langle d|s\rangle|^2=b^2/\Omega^2>0\), so \(S(t)\) does not decay to zero and \(\int_0^\infty S(t)\,dt=\infty\). The bright part is eventually captured; total capture probability is \(a^2/\Omega^2\). Thus the weak-noise divergence in the positive-rate formula is genuine.

## Verification

The accompanying standalone `check_dephasing_star.py` requires Python 3, NumPy and SciPy. Execute `python3 check_dephasing_star.py`. It independently constructs the original \((N+1)^2\)-dimensional Liouvillian for unequal random couplings, solves the reachable reduced master equation, verifies the closed matrix \(X\) upon embedding in the original space, compares finite-time matrix-exponential integrals, and tests joint rate minimization for additional random parameter families. Successful execution records 96 original-space certificate/resolvent comparisons, three finite-time tests, and 345 rate-optimum test groups. The proof is algebraic and spectral; these finite cases are diagnostics, not a proof of universal validity.

## Relationship to prior work

Noise-assisted quantum transport and its Lindblad setting are established by Plenio and Huelga (2008), including local dephasing and transport on chains. Kassal and Aspuru-Guzik (2012) analyze ordered *linear chains* and circles with dephasing on all sites, competing uniform loss and optimization of a capture-efficiency objective; their three-site chain is not the same site-specific noise model or the same mean-time objective. Pepe, Pouthier and Yalouz (2023) study *extended stars* with peripheral energy defects and a delocalized initial excitation, global environmental dephasing and a half-absorption-time observable. These papers establish techniques and related motivations, but their explicitly examined results do not imply the source-only weighted-star joint optimum stated here. In particular, invariant-subspace reduction and noise-assisted transport are not claimed as new.

Gaab and Bardeen (2004) is a directly relevant earlier Haken–Strobl study of topology, coherence time and trap time. Its accessible abstract and secondary discussions already report the qualitative existence of joint optimal dephasing/trapping parameters. The entire article could not be inspected; that earlier paper may contain a specialized expression covering part or all of the present result. Accordingly, historical priority is provisional and any claim of an unprecedented joint optimum *as a phenomenon* is excluded. The assessed mathematical contribution is the explicit source-only, arbitrarily weighted-star formula, including exact separability and unique rates.

## Limitations

The theorem assumes zero on-site detuning, exactly one initially occupied peripheral site, source-only dephasing with the given normalization, fixed positive coherent couplings, and instantaneous Markovian capture with no competing loss. The full \((N+1)\)-state Lindbladian can have unexcited stationary dark states when \(N>2\); only its reachable three-state block is strictly decaying. Different preparation, additional dephasing, detuning, finite trap bandwidth, or recombination can change the formulas. The proof does not establish uniqueness or historical priority across all prior literature, and no independent scientific audit has been carried out.

## References

1. M. B. Plenio and S. F. Huelga, *Dephasing assisted transport: Quantum networks and biomolecules*, arXiv:0807.4902 (first publicly submitted 2008-07-30), https://arxiv.org/abs/0807.4902 ; New J. Phys. 10, 113019 (2008).
2. I. Kassal and A. Aspuru-Guzik, *Environment-assisted quantum transport in ordered systems*, arXiv:1201.5202 (first publicly submitted 2012-01-25), https://arxiv.org/html/1201.5202v2 ; New J. Phys. 14, 053041 (2012).
3. L. Pepe, V. Pouthier and S. Yalouz, *Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing*, arXiv:2308.15857 (first submitted 2023-08-30), https://arxiv.org/html/2308.15857v2.
4. K. M. Gaab and C. J. Bardeen, *The effects of connectivity, coherence, and trapping on energy transfer in simple light-harvesting systems studied using the Haken–Strobl model with diagonal disorder*, J. Chem. Phys. 121, 7813–7820 (2004), https://doi.org/10.1063/1.1786922 (full text not inspected).
