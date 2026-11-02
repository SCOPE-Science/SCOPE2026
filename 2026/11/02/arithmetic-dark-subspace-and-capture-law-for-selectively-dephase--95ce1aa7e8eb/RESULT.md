# Arithmetic dark-subspace and capture law for selectively dephased quantum paths

## Finding

For a uniform finite quantum path with one irreversible sink and independently dephased chosen vertices, the **entire asymptotic trapping obstruction is controlled by one greatest common divisor**. Specifically, let \(q=N+1\) and
\[
g=\gcd\bigl(q,c,\{j:j\in S\}\bigr).
\]
Then the maximal surviving Hilbert subspace has dimension \(g-1\). Let \(\Pi_g\) be its orthogonal projector. For every trace-one initial state \(\rho_0\), the final absorbed probability is exactly
\[
P_{\mathrm{abs}}(\rho_0)=1-\operatorname{tr}(\Pi_g\rho_0).
\]
For a single occupied initial vertex \(a\),
\[
\boxed{P_{\mathrm{abs}}(a)=\begin{cases}1,&g\mid a,\\ 1-\dfrac{g}{N+1},&g\nmid a.\end{cases}}
\]
In particular, **all** initial states are eventually absorbed if and only if \(g=1\). If the sink by itself has dark states, a single dephaser at vertex \(1\) removes every one of them; an interior dephaser need not.

## Assumptions and scope

Take any integer \(N\ge2\) and label vertices \(1,\ldots,N\). Write \(P_j=|j\rangle\langle j|\), fix \(J>0\), and define the one-excitation nearest-neighbor Hamiltonian
\[
H=J\sum_{j=1}^{N-1}\bigl(|j\rangle\langle j+1|+|j+1\rangle\langle j|\bigr).
\]
Choose any sink vertex \(c\in\{1,\ldots,N\}\) and \(\kappa>0\), and any set \(S\) of noisy vertices, each with \(\gamma_j>0\); \(S\) may be empty or contain \(c\). There are no other loss channels, interactions, or site-energy detunings. The trace-decreasing Markovian dynamics is
\[
\dot\rho=\mathcal L\rho=-i[H,\rho]-\frac\kappa2\{P_c,\rho\}+\sum_{j\in S}\gamma_j\left(P_j\rho P_j-\frac12\{P_j,\rho\}\right).
\]
This is the system block of a trace-preserving evolution that records the lost weight in the sink, so \(P_{\mathrm{abs}}=1-\lim_{t\to\infty}\operatorname{tr}\rho(t)\). All assertions hold for **every** positive value of every rate and for **every** normalized positive-semidefinite initial density matrix; no weak-coupling limit is used. The shorthand \(\gcd(q,c,\varnothing)\) means \(\gcd(q,c)\).

Define \(q=N+1\), \(g=\gcd(q,c,\{j:j\in S\})\), and the normalized sine modes
\[
\phi_k(x)=\sqrt{\frac2q}\sin\left(\frac{\pi kx}{q}\right),\quad
1\le k\le N,\quad1\le x\le N.
\]
Let \(K_g=\operatorname{span}\{\phi_{rq/g}:1\le r\le g-1\}\), with \(K_1=\{0\}\), and let \(\Pi_g\) be the orthogonal projector onto \(K_g\).

## Proof

**1. Identify all simultaneously invisible modes.** The eigenvalues of \(H\) are \(2J\cos(\pi k/q)\), pairwise distinct for \(1\le k\le N\). The sine eigenvector satisfies \(\phi_k(x)=0\) if and only if \(q\mid kx\). Consequently, a mode is zero at the sink and at every dephased vertex precisely when
\[
q\mid kc,\qquad q\mid kj\quad\text{for every }j\in S.
\]
These congruences hold exactly when \(k\) is a multiple of \(q/g\), namely \(k=rq/g\), \(1\le r<g\). Thus \(\dim K_g=g-1\). Since \(H\) preserves \(K_g\), and every \(P_c\) and \(P_j\) annihilates it, its population is preserved exactly: for any initial \(\rho_0\),
\[
\operatorname{tr}(\Pi_g\rho(t))=\operatorname{tr}(\Pi_g\rho_0),\quad t\ge0.
\]

**2. Exclude any other persistent weight.** The orthogonal complement of \(K_g\) reduces \(H\) and every noise/sink projector. The density-matrix compression to this complement therefore evolves independently under a positive, trace-decreasing semigroup. Suppose its limiting trace is \(\ell>0\). The Cesàro averages of its evolution form a bounded family of positive matrices. A subsequence converges to a nonzero stationary positive matrix \(\sigma\) supported in \(K_g^\perp\), since \(\mathcal L T^{-1}\int_0^T\rho(t)\,dt=(\rho(T)-\rho(0))/T\to0\).

Taking traces in \(\mathcal L\sigma=0\) gives \(\kappa\operatorname{tr}(P_c\sigma)=0\), hence positivity implies \(P_c\sigma=\sigma P_c=0\). Multiply the stationary equation by \(\sigma\) and trace. Its Hamiltonian term vanishes, its sink term vanishes, and the pure-dephasing terms give the exact Hilbert–Schmidt identity
\[
0=-\frac12\sum_{j\in S}\gamma_j\|[P_j,\sigma]\|_2^2.
\]
Every rate being positive, \([P_j,\sigma]=0\) for each noisy site. It follows that \([H,\sigma]=0\). Nondegeneracy of the eigenvalues yields
\[
\sigma=\sum_{k=1}^{N}w_k|\phi_k\rangle\langle\phi_k|,\qquad w_k\ge0.
\]
From \(P_c\sigma=0\), any \(w_k>0\) requires \(\phi_k(c)=0\); in particular \(w_1=0\) because \(\phi_1(c)\ne0\). At each dephased vertex \(j\), commutation with \(P_j\) says \(\sigma|j\rangle=\alpha_j|j\rangle\), where \(\alpha_j=\langle j|\sigma|j\rangle\ge0\). Taking the inner product with \(\phi_1\) gives \(0=\alpha_j\langle\phi_1|j\rangle\). Since \(\phi_1(j)\ne0\), we have \(\alpha_j=0\), hence \(\sigma|j\rangle=0\). Therefore every \(w_k>0\) also requires \(\phi_k(j)=0\) for every \(j\in S\). The same conclusion is immediate when \(S\) is empty. By step 1, \(\sigma\) must be supported in \(K_g\), contradicting its support in \(K_g^\perp\). Thus \(\ell=0\).

**3. Evaluate the site-source overlap.** Steps 1–2 show that \(\lim_{t\to\infty}\operatorname{tr}\rho(t)=\operatorname{tr}(\Pi_g\rho_0)\). If \(\rho_0=|a\rangle\langle a|\), orthonormality gives
\[
\langle a|\Pi_g|a\rangle=\frac2q\sum_{r=1}^{g-1}\sin^2\!\left(\frac{\pi r a}{g}\right).
\]
The root-of-unity identity \(\sum_{r=1}^{g-1}\sin^2(\pi ra/g)=0\) when \(g\mid a\), and \(=g/2\) otherwise, yields the displayed piecewise capture law. Because \(\dim K_g=g-1\), \(\Pi_g=0\) exactly when \(g=1\), proving the all-initial-state criterion.

## Verification

The provided `checker.py` builds the full complex Lindblad superoperator by Kronecker products, independently of the sine-mode formula. It evaluates the resolvent limit
\[
\lim_{\varepsilon\downarrow0}\varepsilon\operatorname{tr}\bigl[(\varepsilon I-\mathcal L)^{-1}|a\rangle\langle a|\bigr]
\]
at \(\varepsilon=10^{-8}\) and compares the corresponding absorption probability against the exact arithmetic prediction for **151 parameter instances**, including multiple dephasers with unequal positive rates. Every comparison passed within absolute error \(1.5\times10^{-4}\). A separate finite exact-nodal-index and floating-sine-sum check passed **37,908** individual parameter/source comparisons on path lengths up to \(79\). These are numerical and arithmetic corroborations, not substitutes for the proof.

For example, for \(N=11\), sink \(c=4\), and one noisy vertex \(S=\{6\}\), the gcd is \(g=2\). Then a source at vertex \(1\) has exact eventual absorption probability \(5/6\), whereas a source at vertex \(2\) is absorbed with probability \(1\). Changing the noisy site to \(1\) gives \(g=1\), removing all remaining dark modes for every initial state.

Run `python checker.py` with Python 3, NumPy and SciPy installed, and `python verify_arithmetic.py` with Python 3 alone. Both programs are included, use only the package contents, and do not access external data.

## Relationship to prior work

Caruso et al. (2009) established dark/invariant subspaces as the origin of incomplete quantum-network capture, including fully connected graphs, and showed that local dephasing destroys trapped interference. Their general-network appendix treats dark spaces without multiple site-selective dephasing; their explicit rate calculations concern other network geometries. Kassal and Aspuru-Guzik (2012) studied the *same homogeneous path Hamiltonian* with uniform dephasing, local trapping and additional bulk losses, and identified symmetry-protected loss-free modes for a central trap. Their full-text treatment does not give the selected-vertex gcd classification or the rate-independent asymptotic capture law for arbitrary initial density matrices with no bulk loss. Caruso (2014) analyzed different, edge-jump quantum stochastic walks on large graphs, including a numerical endpoint-sink chain, and did not give site-selected pure-dephasing absorption arithmetic. Le et al. (2017) provided the sine eigenmodes and their nodal positions on paths and reviewed the role of dephasing, but did not state the present complete partially-dephased sink/noise arithmetic rule or prove the general stationary-kernel exhaustion argument.

The mode formula and broad dark-state mechanism are established prior art. The finding is the **joint arithmetic condition on a trap and an arbitrary selected dephasing set**, its necessity and sufficiency for asymptotic capture, and the exact retained weight for all initial states. Full historical priority against all broader Lindblad fixed-point literature remains to be established.

## Limitations

This theorem uses uniform nearest-neighbor hopping on a *finite* path, a single sink, Markovian rank-one local dephasing, strictly positive rates on the listed sites, and no other losses. It concerns the infinite-time absorption probability; finite-time efficiency can depend strongly on the rate magnitudes and need not be monotone in dephasing. Nonuniform hopping, correlated dephasing, additional detunings, larger graphs, multiple sinks, and recombination losses are not classified. Independent external verification and exhaustive historical-priority assessment have not been performed.

## References

- F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, and M. B. Plenio, “Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport,” first public 2009-01-28, [arXiv:0901.4454](https://arxiv.org/abs/0901.4454); *J. Chem. Phys.* **131**, 105106 (2009).
- I. Kassal and A. Aspuru-Guzik, “Environment-assisted quantum transport in ordered systems,” first public 2012-01-25, [arXiv:1201.5202](https://arxiv.org/abs/1201.5202), *New J. Phys.* **14**, 053041 (2012).
- F. Caruso, “Universally Optimal Noisy Quantum Walks on Complex Networks,” first public 2013-12-06, [arXiv:1312.1832](https://arxiv.org/abs/1312.1832), *New J. Phys.* **16**, 055015 (2014).
- T. P. Le, L. Donati, S. Severini, and F. Caruso, “How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures,” first public 2017-07-24, [arXiv:1707.07482](https://arxiv.org/abs/1707.07482).
