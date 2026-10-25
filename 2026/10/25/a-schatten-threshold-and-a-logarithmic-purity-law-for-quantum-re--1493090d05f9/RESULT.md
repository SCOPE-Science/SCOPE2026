# A Schatten threshold and a logarithmic purity law for quantum resetting with memory

## Finding

Consider the uniform-history quantum-resetting evolution in which a state evolving under a self-adjoint Hamiltonian is reset, at fixed Poisson rate \(r>0\), to a state sampled uniformly from its own earlier averaged history. On any separable Hilbert space and for every initial density matrix, define \(\Pi_H(\rho_0)=\sum_{E\in\sigma_p(H)}P_E\rho_0P_E\), where the sum ranges over distinct eigenvalues and \(P_E\) are the corresponding spectral projections. The following statements hold jointly.

1. **Schatten threshold:** For every \(1<p<\infty\), \(\|\rho(t)-\Pi_H(\rho_0)\|_{\mathcal S_p}\to0\). Convergence in trace norm occurs **if and only if** \(\operatorname{Tr}(P_{\mathrm{pp}}\rho_0)=1\), where \(P_{\mathrm{pp}}\) projects onto the pure-point spectral subspace. If this condition fails there is no trace-norm limit at all. For purely continuous \(H\), the limiting purity is zero although \(\operatorname{Tr}\rho(t)=1\) at every finite time.

2. **Continuum spectral-purity rate:** Let \(H\) act as multiplication by \(E\) on \(L^2([0,1],dE)\) (units \(\hbar=1\)). For a pure initial vector \(\psi\) with bounded energy density \(w(E)=|\psi(E)|^2\) normalized by \(\int_0^1w=1\),
\[
\lim_{t\to\infty}\sqrt{\log(rt)}\,\operatorname{Tr}(\rho(t)^2)
=r\sqrt{\frac{\pi}{2}}\int_0^1w(E)^2\,dE.
\]
In particular the flat-band state has \(\operatorname{Tr}(\rho(t)^2)\sim r\sqrt{\pi/(2\log(rt))}\), despite having no nonzero stationary trace-class state.

3. **No uniform compact-resolvent decoherence rate:** For any prescribed positive function \(\varepsilon(t)\to0\), there exist a self-adjoint compact-resolvent Hamiltonian with simple pure-point spectrum and a pure initial state of finite energy moments of every polynomial order, for which trace-norm convergence nevertheless satisfies \(\limsup_{t\to\infty}\|\rho(t)-\Pi_H(\rho_0)\|_1/\varepsilon(t)=\infty\).

Taken together, these give a topology-sensitive separation between relaxation of quantum observables, loss of purity, and trace-norm stationarity without requiring a positive minimum Bohr-frequency gap.

## Assumptions and scope

The averaged dynamics for \(t>0\) obeys the quantum Volterra equation
\[
\frac{d\rho}{dt}=-i[H,\rho]-r\rho+\frac r t\int_0^t\rho(s)\,ds,
\qquad \rho(0)=\rho_0\ge0,\quad \operatorname{Tr}\rho_0=1.
\]
The mild random-unitary construction defines the evolution also for unbounded self-adjoint \(H\), for which the displayed commutator is understood on its natural domain or in the mild sense. The rate \(r>0\) is fixed, the earlier time is chosen uniformly in the full interval \([0,t]\), and resets act on the whole quantum density matrix. Schatten \(\mathcal S_p\) norms use the ordinary, unnormalized operator trace. Part 2 uses the spectral interval \([0,1]\) only to fix units; a finite interval of any length admits the analogous formula with its actual spectral density.

## Proof

**The exact scalar response and positivity.** The earlier-history protocol gives the scalar multiplier
\[
f_r(\omega,t)={}_1F_1\!\left(\frac{i\omega}{r+i\omega};1;-(r+i\omega)t\right).
\]
For each bounded spectral matrix block with Bohr frequency \(\omega=E-E'\), the density matrix is multiplied by \(f_r(\omega,t)\). This is the exact response derived in the motivating work, not a new scalar formula. The full channel is also a probability mixture of unitary maps \(X\mapsto e^{-iHs}Xe^{iHs}\): between memory-reset events a realized branch propagates unitarily, while a reset replaces its branch by the ensemble at a previously chosen time. Conditioning on this history gives a random effective elapsed unitary time. Consequently \(|f_r(\omega,t)|\le1\), \(f_r(0,t)=1\), and the maps are trace-preserving, completely positive, and contractions on trace class. For every fixed \(\omega\ne0\), Kummer asymptotics imply \(f_r(\omega,t)\to0\). Its power exponent is \(\operatorname{Re}[i\omega/(r+i\omega)]=\omega^2/(r^2+\omega^2)>0\).

**Schatten topology.** Identify the Hilbert–Schmidt space \(\mathcal S_2\) with the space on which the unitary conjugation group \(X\mapsto e^{-iHt}Xe^{iHt}\) acts. The corresponding Liouvillian is self-adjoint. Spectral calculus expresses the channel on \(\mathcal S_2\) as its scalar multiplier \(f_r\). Since this multiplier is bounded by one and tends pointwise to the indicator of its zero-frequency spectral eigenspace, dominated convergence in the Liouvillian spectral measure proves Hilbert–Schmidt convergence to the orthogonal projection onto the fixed-point space. A compact Hilbert–Schmidt operator commuting with \(H\) cannot carry a nonzero continuous-spectrum component: its nonzero finite-multiplicity singular subspaces are finite-dimensional invariant subspaces of \(H\), and hence span eigenvectors. Its fixed-point projection is exactly the trace-class convergent series \(\Pi_H(\rho_0)\). For \(p\ge2\), \(\|X\|_p\le\|X\|_2\). For \(1<p<2\), interpolation gives \(\|X\|_p\le\|X\|_1^{2/p-1}\|X\|_2^{2-2/p}\), while \(\|\rho(t)-\Pi_H(\rho_0)\|_1\le2\). These prove the Schatten assertion.

The trace of the fixed-point operator is \(m=\operatorname{Tr}(P_{\mathrm{pp}}\rho_0)\). If \(m<1\), trace-norm convergence to that operator is impossible since the trace difference equals \(1-m\); convergence to any other trace-class operator would contradict uniqueness of the Hilbert–Schmidt limit. If \(m=1\), positivity forces \(\rho_0=P_{\mathrm{pp}}\rho_0P_{\mathrm{pp}}\). Approximate \(\rho_0\) in trace norm by finite-eigenvalue compressions, apply the finite-block limit \(f_r(\omega,t)\to0\), then remove the approximation using trace-class contractivity. This proves the asserted 'if and only if'. When \(P_{\mathrm{pp}}=0\), Hilbert–Schmidt convergence to zero is precisely \(\operatorname{Tr}(\rho(t)^2)\to0\).

**Sharp logarithmic purity.** For the multiplication Hamiltonian and the specified pure initial state, spectral multiplication and the Hilbert–Schmidt formula give the exact identity
\[
\operatorname{Tr}(\rho(t)^2)=\int_0^1\!\int_0^1w(E)w(E')|f_r(E-E',t)|^2\,dE\,dE'.
\]
Write \(L=\log(rt)\). On each fixed compact Bohr-frequency interval, uniformly in a neighborhood of zero, the Kummer large-argument expansion on the negative right-half-plane ray gives
\[
f_r(\omega,t)=\frac{((r+i\omega)t)^{-a(\omega)}}{\Gamma(1-a(\omega))}[1+o(1)],\qquad a(\omega)=\frac{i\omega}{r+i\omega}.
\]
The representation extends continuously at \(\omega=0\), where both sides are one. Uniformly when \(\omega=y/\sqrt L\) with bounded \(y\), its squared modulus tends to \(e^{-2y^2/r^2}\), because \(\operatorname{Re}a(\omega)=\omega^2/(r^2+\omega^2)\). The same expansion and compactness on \(|\omega|\le1\) yield a uniform integrable majorant \(C e^{-cL\omega^2}\) for sufficiently large \(L\) (with positive constants depending on \(r\)); the contribution from frequencies bounded away from zero decays by a positive power of \(t\). Consequently \(\sqrt L\,|f_r(\cdot,t)|^2\) is an approximate identity of mass
\[
\int_{-\infty}^{\infty}e^{-2y^2/r^2}\,dy=r\sqrt{\pi/2}.
\]
The autocorrelation \(G(\omega)=\int w(E)w(E-\omega)\,dE\), extending \(w\) by zero off its band, is bounded, continuous at zero in view of \(w\in L^2\), and has \(G(0)=\int w^2\). Applying the approximate identity to the exact purity expression proves the claimed sharp coefficient. The dominated convergence includes energies at the band endpoints and requires no spectral gap.

**Arbitrarily slow compact-resolvent convergence.** Fix any \(\varepsilon(t)>0\) decreasing to zero only in the limiting sense, with no monotonicity needed. Select \(T_n\uparrow\infty\) such that \(\varepsilon(T_n)<2^{-n}/n\). On a basis \(\{e_{n,0},e_{n,1}:n\ge1\}\) take \(He_{n,0}=3n\,e_{n,0}\) and \(He_{n,1}=(3n+\delta_n)e_{n,1}\), with \(0<\delta_n<1/4\) so small that \(|f_r(\delta_n,T_n)|\ge1/2\); such \(\delta_n\) exists by continuity of \(f_r\) at zero for each finite time. The spectrum is simple and diverges, giving compact resolvent. Let \(\psi=\sum_{n\ge1}\sqrt{2^{-n-1}}(e_{n,0}+e_{n,1})\), so \(\|\psi\|=1\), and put \(\rho_0=|\psi\rangle\langle\psi|\). All polynomial energy moments are finite since the weights decay geometrically and energies grow linearly. The compression to the \(n\)-th two-dimensional block of the difference from the spectral pinching has off-diagonals \(2^{-n-1}f_r(\delta_n,t)\) and no diagonals. Its trace norm is \(2^{-n}|f_r(\delta_n,t)|\), no greater than the full trace norm. At \(t=T_n\) the full trace distance is at least \(2^{-n-1}>n\varepsilon(T_n)/2\). Hence its ratio to the arbitrarily prescribed rate has infinite limsup. The state nevertheless converges in trace norm by the pure-point theorem already proved.

## Verification

The reproducible Python program `check.py` evaluates the exact confluent-hypergeometric multiplier independently of its Kummer asymptotic, verifies the scalar Volterra equation by numerical quadrature, checks qubit-block positivity and exact trace-distance identities, and computes flat-band purity integrals. The packaged finite checker returned **49 passing deterministic assertions**. Its computations are finite numerical diagnostics and do not establish the infinite-dimensional spectral, large-time, or arbitrary-rate arguments, which are proved above.

## Relationship to prior work

De Mauro, Kulkarni and Majumdar (2026), *Quantum resetting with memory* (arXiv:2608.02297v1), establish the exact hypergeometric multiplier, the decay of fixed nonzero Bohr-frequency coherences, and thermal-free-particle continuum applications. Their trace-matrix relaxation bound assumes a positive minimum nonzero Bohr gap. The present contribution addresses a distinct sharp norm-topology boundary on general infinite spectra, a spectral-continuum purity constant, and the absence of a universal rate even for compact-resolvent Hamiltonians with finite energy moments. These statements are consequences of the common response kernel only after new spectral and asymptotic analysis; they are not claims of a new underlying memory-resetting dynamics. Rose, Touchette, Lesanovsky and Garrahan (2018), *Spectral properties of simple classical and quantum reset processes* (arXiv:1806.01298), treat fixed-state Markovian resets rather than a state sampled from its own full past. The Hilbert–Schmidt spectral theorem and standard properties of the Kummer function are used as classical tools.

## Limitations

The theorem describes ensemble-averaged, full-memory resets at constant positive rate, not trajectories with single-run measurements, finite-history windows, nonuniform historical kernels or time-dependent resetting. The trace-norm stationary limit need not be a normalized state when the initial spectral measure has continuous mass; this is a mathematical absence of normal stationarity, not nonconservation of quantum probability. The sharp logarithmic purity constant is proved only for a rank-one initial state with bounded energy density on a finite absolutely continuous spectral band; no matching general result is claimed for arbitrary singular-continuous measures. Arbitrarily slow convergence is a worst-case construction over Hamiltonians and initial states, not a universal prediction for a particular physical Hamiltonian. Independent priority checking against broad quantum ergodic and dephasing theorems is outstanding.

## References

- M. de Mauro, M. Kulkarni and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1, first publicly posted August 3, 2026. https://arxiv.org/abs/2608.02297
- D. C. Rose, H. Touchette, I. Lesanovsky and J. P. Garrahan, *Spectral properties of simple classical and quantum reset processes*, arXiv:1806.01298, 2018. https://arxiv.org/abs/1806.01298
- NIST Digital Library of Mathematical Functions, Chapter 13, *Confluent Hypergeometric Functions*, for large-argument asymptotics. https://dlmf.nist.gov/13
