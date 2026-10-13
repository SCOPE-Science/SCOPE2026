# Cycle-controlled temporal cumulants and a forest Berry–Esseen theorem for quasifree fermions
## Finding
Let a finite number-conserving quasifree fermion system have one-particle Hamiltonian
\[
M=\operatorname{diag}(\varepsilon_1,\ldots,\varepsilon_L),
\]
initial covariance \(0\le R\le I\), and a Hermitian quadratic observable matrix \(a\). Its time-dependent expectation is
\[
A(t)=\operatorname{tr}\!\left(ae^{-itM}Re^{itM}\right).
\]
Assume the relative one-particle gaps are rationally independent:
\[
\sum_{j=2}^L n_j(\varepsilon_j-\varepsilon_1)=0,
\quad n_j\in\mathbb Z
\quad\Longrightarrow\quad n_2=\cdots=n_L=0.
\]
Put
\[
\overline A=\sum_{j=1}^L a_{jj}R_{jj},
\qquad
c_{jk}=a_{kj}R_{jk}\quad(j<k).
\]
For every active pair define \(r_{jk}=|c_{jk}|\), orient the edge \(j\to k\), and let \(\phi_{jk}=\arg c_{jk}\). The active coherence graph \(G\) has vertex set \(\{1,\ldots,L\}\) and edge \(\{j,k\}\) exactly when \(c_{jk}\ne0\).

For an oriented simple cycle \(C\), let \(\Phi_C\) be the signed sum of its edge phases. Reversing the cycle changes \(\Phi_C\) to \(-\Phi_C\), so \(\cos\Phi_C\) is well defined. The second, third, and fourth infinite-time temporal cumulants of \(A(t)-\overline A\) are
\[
\kappa_2=2\sum_{e\in E(G)}r_e^2,
\]
\[
\kappa_3=12\sum_{C\in\mathcal C_3(G)}
\left(\prod_{e\in C}r_e\right)\cos\Phi_C,
\]
and
\[
\kappa_4=-6\sum_{e\in E(G)}r_e^4
+48\sum_{C\in\mathcal C_4(G)}
\left(\prod_{e\in C}r_e\right)\cos\Phi_C,
\]
where each unoriented simple triangle or four-cycle is counted once. In particular, triangle fluxes are the only source of temporal skewness at third order, and four-cycles are the only genuinely multi-edge correction at fourth order.

There is also an exact all-orders statement on forests. The active edge phase differences are jointly independent uniform circle variables if and only if \(G\) is a forest. Hence, for a forest,
\[
A(t)-\overline A\ \overset{d}{=}\ \sum_{e\in E(G)}2r_e\cos\Theta_e,
\qquad
\Theta_e\stackrel{\mathrm{iid}}{\sim}\operatorname{Unif}[0,2\pi),
\]
and
\[
\varphi(s)=\prod_{e\in E(G)}J_0(2r_es).
\]
Writing
\[
\sigma^2=2\sum_e r_e^2>0,
\]
the classical Berry–Esseen inequality yields
\[
d_K\!\left(\frac{A-\overline A}{\sigma},N(0,1)\right)
\le C_{\mathrm{BE}}\frac{8\sqrt2}{3\pi}
\frac{\sum_e r_e^3}{\left(\sum_e r_e^2\right)^{3/2}}
\le C_{\mathrm{BE}}\frac{8\sqrt2}{3\pi}
\frac{\max_e r_e}{\left(\sum_e r_e^2\right)^{1/2}}.
\]
Thus a sequence of forest-supported observables has a quantitative Gaussian-equilibration theorem whenever
\[
\frac{\max_e r_e}{\left(\sum_e r_e^2\right)^{1/2}}\longrightarrow0.
\]

## Assumptions and scope
The theorem concerns finite, number-conserving quasifree fermions and quadratic observables. The covariance convention is the one-particle convention in which \(A(t)=\operatorname{tr}(ae^{-itM}Re^{itM})\). The relative-gap rational-independence assumption is shift invariant and is sufficient for the long-time flow of relative one-particle phases to be Haar on an \((L-1)\)-torus.

The active graph depends jointly on the observable and the initial covariance through \(c_{jk}=a_{kj}R_{jk}\); sparsity of \(a\) or \(R\) separately is not required. Zero coefficients are omitted. The cumulant formulas hold for arbitrary finite simple active graphs. The exact independent-cosine representation and Berry–Esseen bound require that active graph to be a forest.

The statement that cycles obstruct independence is only about the simultaneous edge-difference variables induced by Haar vertex phases. A cyclic graph can still have approximately Gaussian temporal statistics because of cancellation, weak weights, or more general central-limit mechanisms. No converse to Gaussian equilibration is claimed.

## Proof
In the energy basis,
\[
A(t)=\sum_{j,k}a_{kj}R_{jk}e^{it(\varepsilon_k-\varepsilon_j)}.
\]
Hermiticity gives \(a_{jk}=\overline{a_{kj}}\) and \(R_{kj}=\overline{R_{jk}}\), hence
\[
A(t)-\overline A
=2\sum_{j<k}r_{jk}
\cos\!\left((\varepsilon_k-\varepsilon_j)t+\phi_{jk}\right).
\]
By the stated rational independence, Kronecker–Weyl equidistribution replaces infinite-time averaging by Haar averaging of the relative vertex phases. Thus the temporal law is the law of
\[
X(\theta)=2\sum_{e=(u,v)}r_e\cos(\theta_u-\theta_v+\phi_e)
\]
under uniform vertex phases, modulo one irrelevant global phase.

Expand each cosine as
\[
2r_e\cos(\theta_u-\theta_v+\phi_e)
=r_e e^{i(\theta_u-\theta_v+\phi_e)}
+r_e e^{-i(\theta_u-\theta_v+\phi_e)}.
\]
A monomial survives Haar integration exactly when the signed selected edge multiset has zero net incidence at every vertex. For the second moment, the only surviving terms are an edge paired with itself in opposite orientations, giving
\[
\mathbb E X^2=2\sum_e r_e^2.
\]
For three factors, a connected zero-incidence simple support must be a triangle. The two cyclic orientations contribute the phase factor \(2\cos\Phi_C\); accounting for the \(3!\) orders gives
\[
\mathbb E X^3=12\sum_{C\in\mathcal C_3(G)}
\left(\prod_{e\in C}r_e\right)\cos\Phi_C.
\]
Since \(\mathbb E X=0\), this is \(\kappa_3\).

For four factors, the disconnected two-edge pairings are exactly the terms removed by \(3(\mathbb E X^2)^2\) in the fourth cumulant. A single edge used four times contributes the fourth cumulant of \(2r_e\cos\Theta\):
\[
\mathbb E(2r_e\cos\Theta)^4-3\left\{\mathbb E(2r_e\cos\Theta)^2\right\}^2
=6r_e^4-12r_e^4=-6r_e^4.
\]
The only connected simple zero-incidence support on four selected edges is a four-cycle. The two cyclic orientations and the \(4!\) orders give \(48(\prod_{e\in C}r_e)\cos\Phi_C\). This proves the formula for \(\kappa_4\).

For the forest statement, orient every edge arbitrarily. The integer incidence vectors of a forest are linearly independent and form a primitive sublattice of the zero-sum vertex lattice. Equivalently, after selecting one root in each component, the change of angular coordinates from vertex phases to the root phases together with the oriented edge differences has determinant \(\pm1\). Haar measure therefore sends the edge differences to independent uniform circle variables. Conversely, every cycle imposes the exact modular relation that the signed sum of its edge differences is zero, so all active edge differences cannot be jointly independent. This proves the if-and-only-if statement.

For a forest, the characteristic function factorizes because
\[
\mathbb E e^{is2r_e\cos\Theta_e}=J_0(2r_es).
\]
Finally, for \(Y_e=2r_e\cos\Theta_e\),
\[
\operatorname{Var}(Y_e)=2r_e^2,
\qquad
\mathbb E|Y_e|^3=\frac{32}{3\pi}r_e^3,
\]
because \(\mathbb E|\cos\Theta|^3=4/(3\pi)\). Applying the classical Berry–Esseen inequality to the independent centered summands gives
\[
\frac{\sum_e\mathbb E|Y_e|^3}{\left(\sum_e\operatorname{Var}(Y_e)\right)^{3/2}}
=rac{8\sqrt2}{3\pi}
\frac{\sum_e r_e^3}{\left(\sum_e r_e^2\right)^{3/2}},
\]
and \(\sum_e r_e^3\le(\max_e r_e)\sum_e r_e^2\) gives the second bound.

## Verification
The accompanying `verify.py` independently expands torus moments by signed-edge enumeration on a graph containing both a triangle and a four-cycle and reproduces the displayed \(\kappa_2\), \(\kappa_3\), and \(\kappa_4\) formulas for nonzero phases. It also checks the unimodular vertex-to-edge coordinate transformation on representative forests and checks the Berry–Esseen prefactor algebra. Running `python3 verify.py` prints `VERIFY_OK`.

The checker is supplementary. The proof of the general theorem is the zero-incidence characterization of Haar-surviving monomials and the unimodular incidence structure of forests; no finite graph enumeration is used to infer an infinite family statement.

## Relationship to prior work
Campos Venuti and Zanardi map the long-time statistics of quadratic observables in quasifree fermion systems with rationally independent one-particle energies to the infinite-temperature partition function of a generalized classical \(XY\) model. They conjecture broad Gaussian equilibration and prove it in specific examples. In their quantum \(XY\)-magnetization example the generating function factorizes into Bessel factors, making the fluctuation a sum of independent variables; they then use a Lyapunov condition to obtain a central limit theorem. That mapping and that model-specific independent-sum argument are prior inputs, not claimed here.

The new statement extracts the topology of the general interaction matrix left implicit in that mapping. It gives exact graph-cycle formulas for the third and fourth temporal cumulants for arbitrary active support, characterizes forests as exactly the supports for which all active edge phases become independent, and supplies a finite-system Berry–Esseen error bound for that entire class.

Brandão and Cramer use a Berry–Esseen-type theorem for energy distributions in short-range quantum lattice systems when proving equivalence of ensembles. That result concerns quantum measurement distributions of Hamiltonians in correlated states, not the infinite-time distribution of a single expectation value in quasifree unitary dynamics, and it does not imply the graph-cycle formulas or the forest factorization here.

Targeted searches using the source identifier, quasifree-fermion and Gaussian-equilibration terminology, graph-cycle cumulants, forest phase independence, and Berry–Esseen terminology did not locate an implication-equivalent statement. Classical high-temperature \(XY\) expansions are an important residual comparison because linked-cluster methods encode cycle information in related partition functions; no searched source was found stating this temporal-statistics theorem with these exact coefficients and the forest finite-size bound.

## Limitations
The rational-independence assumption is strong. Resonant spectra require averaging on a lower-dimensional torus, where additional integer relations can create further cumulant terms and invalidate the forest independence conclusion.

The Berry–Esseen estimate is an upper bound and no optimal universal constant is asserted. It applies directly only in the forest case. For cyclic graphs, the low-order cumulant formulas remain exact but no quantitative central limit theorem is claimed.

The result concerns number-conserving quasifree fermions. Bogoliubov–de Gennes Hamiltonians with pairing require a doubled one-particle representation and are not included without a separate derivation.

## References
1. L. Campos Venuti and P. Zanardi, *Gaussian Equilibration*, arXiv:1208.1121, Phys. Rev. E 87, 012106 (2013), DOI: 10.1103/PhysRevE.87.012106.
2. F. G. S. L. Brandão and M. Cramer, *Equivalence of Statistical Mechanical Ensembles for Non-Critical Quantum Systems*, arXiv:1502.03263 (2015).
3. A standard form of the Berry–Esseen theorem for independent, not necessarily identically distributed, centered summands is used in the final step.
