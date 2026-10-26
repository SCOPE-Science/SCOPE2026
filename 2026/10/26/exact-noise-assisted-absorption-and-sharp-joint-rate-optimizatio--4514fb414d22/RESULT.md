# Exact noise-assisted absorption and sharp joint-rate optimization on quantum stars

## Finding

**Theorem.** Consider the star graph with hub \(0\) and \(m\ge 2\) leaves \(1,\ldots,m\). With coherent hub–leaf coupling \(J>0\), a hub population sink of strength \(\kappa>0\), independent leaf dephasing of strength \(\gamma_L>0\), and hub dephasing of strength \(\gamma_H\ge0\), start a single excitation at any one leaf. The excitation is eventually absorbed with probability one. Its exact mean absorption time is
\[
\tau_m(J,\kappa,\gamma_L,\gamma_H)
=\frac{m+1}{\kappa}+\frac{m-1}{\gamma_L}
 +\frac{\kappa+\gamma_L+\gamma_H}{4J^2}.
\]
The global minimum over positive sink and leaf-dephasing rates and nonnegative hub dephasing is unique:
\[
\kappa_*=2J\sqrt{m+1},\qquad
\gamma_{L,*}=2J\sqrt{m-1},\qquad \gamma_{H,*}=0,
\]
with value
\[
\tau_{m,*}=\frac{\sqrt{m+1}+\sqrt{m-1}}{J}
\sim\frac{2\sqrt m}{J}\quad(m\to\infty).
\]
At exactly \(\gamma_L=0\), a localized leaf excitation is absorbed with probability only \(1/m\), for all \(\gamma_H\ge0\). Thus complete absorption for every \(\gamma_L>0\) is discontinuous at zero leaf dephasing.

## Assumptions and scope

Use units with \(\hbar=1\), and the single-excitation Hilbert space with orthonormal site vectors \(|0\rangle,|1\rangle,\ldots,|m\rangle\). Let \(P_j=|j\rangle\langle j|\) and
\[
H=J\sum_{i=1}^m(|0\rangle\langle i|+|i\rangle\langle0|).
\]
The trace-decreasing no-absorption density matrix evolves by the explicitly normalized master equation
\[
\dot\rho=-i[H,\rho]-\frac\kappa2\{P_0,\rho\}
+\sum_{j=0}^m \gamma_j\bigl(P_j\rho P_j-\tfrac12\{P_j,\rho\}\bigr),
\qquad \gamma_0=\gamma_H,\quad\gamma_j=\gamma_L\ (j\ge1).
\]
In particular, \(\kappa\) is the *population* loss rate at the hub, and an off-diagonal hub–leaf coherence decays at the non-Hamiltonian rate \((\kappa+\gamma_H+\gamma_L)/2\). Initially \(\rho(0)=|1\rangle\langle1|\). The survival probability is \(S(t)=\operatorname{tr}\rho(t)\), with \(\tau_m=\int_0^\infty S(t)\,dt\). No homogeneous loss at the leaves, static disorder, thermal pumping, or excitation creation is included.

## Proof

**1. Reduction without changing the observable.** The Liouvillian and trace are invariant under permutations of the \(m\) leaves. Every localized leaf therefore has the same survival function as the averaged initial state \(\rho(0)=m^{-1}\sum_{i=1}^mP_i\). This averaging is valid for the trace observable, although it does not replace the actual localized input by a coherent superposition.

Let \(a=\rho_{00}\), \(b=\rho_{ii}\) for any leaf \(i\), \(d=\rho_{ij}\) for distinct leaves, and \(\rho_{0i}=iv\), where \(v\in\mathbb R\). Write \(s=(\kappa+\gamma_L+\gamma_H)/2\). Permutation invariance and the master equation give the closed system
\[
\begin{aligned}
\dot a&=-\kappa a-2mJv,\\
\dot b&=2Jv,\\
\dot d&=2Jv-\gamma_Ld,\\
\dot v&=-J\bigl(b+(m-1)d-a\bigr)-sv,
\end{aligned}
\]
with \(a(0)=d(0)=v(0)=0\) and \(b(0)=1/m\). The trace is \(a+mb\).

**2. Strict absorption for positive leaf noise.** The evolution is completely positive and trace decreasing, with \(\dot S=-\kappa a\le0\). To show that no positive trace can survive, consider any trajectory lying forever in the zero-loss set \(a=0\). Positivity forces all hub row/column entries to vanish. The hub–leaf equation then forces the leaf density block \(R(t)\) to satisfy \(R(t){\bf1}=0\). Inside the hub-free set the leaf block undergoes only local dephasing, so its off-diagonal entries decay as \(e^{-\gamma_Lt}\), while its diagonal entries remain fixed. Taking \(t\to\infty\) in \(R(t){\bf1}=0\) shows every diagonal entry vanishes. A positive-semidefinite matrix with zero diagonal is zero. Hence the largest invariant subset of \(a=0\) is the zero density matrix. The finite-dimensional invariance principle (or a compactness argument for omega-limit sets) shows \(\rho(t)\to0\). Its positive linear semigroup has no nondecaying spectral mode; in finite dimension this implies exponential decay and finiteness of each integral below.

**3. Exact integration.** Denote \(A=\int_0^\infty a\,dt\), \(B=\int_0^\infty b\,dt\), \(D=\int_0^\infty d\,dt\), and \(V=\int_0^\infty v\,dt\). Integrating the first three differential equations gives
\[
A=\frac1\kappa,\qquad V=-\frac1{2mJ},\qquad D=-\frac1{m\gamma_L}.
\]
Integrating the last equation, with both endpoint coherences zero, gives
\[
B=A-(m-1)D-\frac{s}{J}V
=\frac1\kappa+\frac{m-1}{m\gamma_L}+\frac{s}{2mJ^2}.
\]
Therefore
\[
\tau_m=A+mB
=\frac{m+1}{\kappa}+\frac{m-1}{\gamma_L}+\frac{s}{2J^2},
\]
which is the asserted formula because \(s=(\kappa+\gamma_L+\gamma_H)/2\).

**4. Global optimality.** Separate the positive-rate contributions:
\[
\tau_m=
\left(\frac{m+1}\kappa+\frac\kappa{4J^2}\right)
+\left(\frac{m-1}{\gamma_L}+\frac{\gamma_L}{4J^2}\right)
+\frac{\gamma_H}{4J^2}.
\]
For each of the first two brackets, the arithmetic–geometric mean inequality gives equality uniquely at the displayed values of \(\kappa_*\) and \(\gamma_{L,*}\). The last term is uniquely smallest at \(\gamma_H=0\). Summing the two exact minima establishes global optimality and the sharp square-root asymptotic.

**5. Singular zero-noise boundary.** When \(\gamma_L=0\), the leaf subspace orthogonal to the uniform leaf vector, \(D=\{\psi:\psi_0=0,\sum_{i=1}^m\psi_i=0\}\), is invariant under both the Hamiltonian and hub-only dephasing. The squared norm of the projection of \(|1\rangle\) onto \(D\) is \(1-1/m\). The complementary two-dimensional bright sector couples to the lossy hub and decays completely for \(J,\kappa>0\). Thus \(\Pr(\mathrm{absorbed})=1/m\) at \(\gamma_L=0\), but equals one at every \(\gamma_L>0\). The unconditional absorption time is infinite when nonabsorption has positive probability.

## Verification

The standalone `verify_star.py` constructs the *full*, unsymmetrized \((m+1)^2\)-dimensional Liouvillian, inverts its integrated resolvent independently of the four-variable reduction, and compares against the displayed formula for 84 parameter tuples with \(m=2,\ldots,8\); it also verifies six algebraic optimum cases. The independent exact-arithmetic script `verify_exact.py` uses rational parameters and exact symbolic linear algebra for \(m=2,3,4\), two rate configurations at each size. Both scripts passed. For replication, install Python 3 with NumPy and SciPy for the first script and SymPy for the second; run `python verify_star.py` and `python verify_exact.py`.

The analytical argument, not finite testing, proves the results for all stated real rates and all \(m\ge2\). The numerical and symbolic experiments do not constitute infinite-domain certification or independent peer validation.

## Relationship to prior work

The general phenomena of decoherence-assisted quantum transport, trapping on networks, and the Haken–Strobl master equation are established. Marais et al. (2013) give analytic decoherence-assisted transfer in a fully connected network coupled to spin environments, rather than this star with independent Markov site noise and a local irreversible sink. Novo et al. (2015) examine coherent transport on nonregular networks, including star graphs and traps, without the current joint dephasing control. Pepe, Pouthier, and Yalouz (2023 preprint; 2024 journal version) study a dephased *extended* star with peripheral detunings and predominantly delocalized initial excitations; their primary characteristic absorption time is a median, with strong-dephasing mean-first-passage approximations, not the exact localized-leaf mean and site-selective global optimum proved here. Alterman, Berman, and Strauch (2023 preprint; 2024 journal version) solve an open *complete* graph, where leaf–leaf couplings differ from this star. These distinctions concern graph generators, starting states, exact observables, and rate freedoms, not just terminology; general master-equation tools are prior art.

## Limitations

The result assumes a uniform one-generation star, one excitation, a sink only at the hub, Markov pure dephasing, and identical leaf rates. The optimization is global only **within this parameterized model**; no assertion is made for arbitrary graph topology, disorder, non-Markov environments, collective dephasing, coherent initial superpositions, or additional loss channels. No claim of exhaustive historical priority or independent scientific validation is made.

## References

1. A. Marais, I. Sinayskiy, A. Kay, F. Petruccione, and A. Ekert, “Decoherence-assisted transport in quantum networks,” *New Journal of Physics* **15** (2013), 013038, DOI: 10.1088/1367-2630/15/1/013038. Public 17 January 2013.
2. L. Novo, S. Chakraborty, M. Mohseni, H. Neven, and Y. Omar, “Systematic Dimensionality Reduction for Quantum Walks: Optimal Spatial Search and Transport on Non-Regular Graphs,” *Scientific Reports* **5** (2015), 13304, DOI: 10.1038/srep13304.
3. L. Pepe, V. Pouthier, and S. Yalouz, “Optimized excitonic transport mediated by local energy defects: survival of optimization laws in the presence of dephasing,” arXiv:2308.15857, first submitted 30 August 2023; *Physical Review E* **109** (2024), 014303.
4. S. Alterman, J. Berman, and F. W. Strauch, “Optimal Conditions for Environment-Assisted Quantum Transport on the Fully Connected Network,” arXiv:2309.00164, first submitted 31 August 2023; *Physical Review E* **109** (2024), 014310.
