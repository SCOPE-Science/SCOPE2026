# Exact thermal-magic boundary for the canonical Hubbard dimer

## Finding
Consider the repulsive two-site Hubbard model in the sector containing exactly one spin-up and one spin-down electron, with hopping \(t>0\), interaction \(U\geq0\), and canonical temperature \(T\geq0\), in units with \(k_{\mathrm B}=1\). Define \(q=U/(4t)\) and \(g=\sqrt{1+q^2}\). With magic measured relative to the full four-qubit stabilizer polytope (equivalently, log-free robustness of magic exceeding one), the exact finite-temperature criterion is

\[
\rho(U,T)\text{ is a stabilizer mixture}\quad\Longleftrightarrow\quad
\frac{1+q}{g}\tanh\!\left(\frac{2tg}{T}\right)\leq 1 \qquad (T>0).
\]

For each \(U>0\) there is one and only one critical temperature,

\[
T_{\mathrm c}(U)=\frac{2t\sqrt{1+(U/4t)^2}}{\operatorname{artanh}\!\left(\frac{\sqrt{1+(U/4t)^2}}{1+U/(4t)}\right)},
\]

and the thermal state is magic for \(0\leq T<T_{\mathrm c}(U)\) and free of magic for \(T\geq T_{\mathrm c}(U)\). At \(U=0\) it is free of magic for all temperatures, and we set \(T_{\mathrm c}(0)=0\). The function \(T_{\mathrm c}\) is continuous, strictly increasing for \(U>0\), and maps \((0,\infty)\) onto \((0,\infty)\); hence every \(T>0\) has a unique interaction threshold. Moreover, its two interaction regimes obey the exact reciprocal identity

\[
T_{\mathrm c}(U)=\frac{U}{4t}\,T_{\mathrm c}\!\left(\frac{16t^2}{U}\right)\qquad(U>0).
\]

Its sharp limits are

\[
T_{\mathrm c}(U)\sim\frac{4t}{\log(8t/U)}\quad(U/t\downarrow0),\qquad
T_{\mathrm c}(U)\sim\frac{U}{\log(U/(2t))}\quad(U/t\to\infty),
\]

and the inverse threshold at low temperature satisfies \(U_{\mathrm c}(T)\sim8t\exp(-4t/T)\) as \(T/t\downarrow0\). In contrast to the monotone thermal boundary, the symmetric two-eigenstate mixing interval of free magic is narrowest at \(U=4t\).

## Assumptions and scope
The mode order is \(1\uparrow,1\downarrow,2\uparrow,2\downarrow\), and the Hamiltonian is

\[
H=-t\sum_{\sigma=\uparrow,\downarrow}(c^\dagger_{1\sigma}c_{2\sigma}+c^\dagger_{2\sigma}c_{1\sigma})+U\sum_{j=1}^{2}n_{j\uparrow}n_{j\downarrow}.
\]

The thermal density matrix \(\rho(U,T)\) is the Gibbs state of the four-dimensional invariant sector with \(N_\uparrow=N_\downarrow=1\), embedded in the sixteen-dimensional occupation-qubit Hilbert space. It is **not** the unrestricted grand-canonical Gibbs state. Stabilizer states and Pauli measurements are the conventional four-qubit stabilizer resource theory, without an additional particle-number or parity superselection restriction. Temperature zero means the unique ground state. At \(U\to\infty\) we assert an asymptotic formula for the threshold, not finite-\(U\) vanishing of the ground-state magic.

Write, in the four-qubit occupation basis,

\[
|d_+\rangle=\frac{|1100\rangle+|0011\rangle}{\sqrt2},\qquad
|s_-\rangle=\frac{|1001\rangle-|0110\rangle}{\sqrt2},
\]
\[
|d_-\rangle=\frac{|1100\rangle-|0011\rangle}{\sqrt2},\qquad
|t_+\rangle=\frac{|1001\rangle+|0110\rangle}{\sqrt2}.
\]

## Proof
**1. Spectral reduction.** In the ordered orthonormal basis \((|d_+\rangle,|s_-\rangle,|d_-\rangle,|t_+\rangle)\), direct fermionic anticommutation gives

\[
H=\begin{pmatrix}U&-2t&0&0\\-2t&0&0&0\\0&0&U&0\\0&0&0&0\end{pmatrix}.
\]

The first block has energies \(E_-=U/2-2tg\) and \(E_+=U/2+2tg\). Its normalized eigenvectors \(|\psi_-\rangle\), \(|\psi_+\rangle\) have coordinates proportional to \((1,q+g)\), \((1,q-g)\), respectively. The other two eigenstates \(|d_-\rangle\), \(|t_+\rangle\) are ordinary four-qubit stabilizer states.

**2. A measured stabilizer code.** Numbering the Pauli factors by mode, define the three commuting independent Pauli observables

\[
S_1=-Z_1Z_3,\qquad S_2=-Z_2Z_4,\qquad S_3=(X_1X_2X_3X_4)(Z_1Z_2).
\]

Their joint \(+1\) eigenspace is exactly \(\mathcal C=\operatorname{span}\{|d_+\rangle,|s_-\rangle\}\), a two-dimensional stabilizer code. The other eigenstates \(|d_-\rangle,|t_+\rangle\) have eigenvalues \((+1,+1,-1)\). Effective logical Pauli operators can be chosen as \(\bar X=-Z_1X_2X_4\) and \(\bar Z=Z_1Z_2\): restricted to the indicated basis of \(\mathcal C\) they are the ordinary Pauli \(X\) and \(Z\).

Let \(\Pi=\prod_{j=1}^{3}(I+S_j)/2\). Because measuring a Pauli and conditioning on either nonzero-probability eigenvalue maps pure stabilizer states to pure stabilizer states, an arbitrary stabilizer mixture stays a stabilizer mixture after the normalized postselection \(\sigma\mapsto\Pi\sigma\Pi/\operatorname{tr}(\Pi\sigma)\). Conversely, any stabilizer mixture in \(\mathcal C\), mixed with the stabilizer projectors onto \(|d_-\rangle\) and \(|t_+\rangle\), remains a stabilizer mixture. These two observations prove that the entire Gibbs state lies in the stabilizer polytope **if and only if** its normalized \(\mathcal C\)-block does. Importantly, this necessity argument is independent of the positive Boltzmann weights of the other two energy levels.

**3. Exact logical Bloch vector.** In the basis \((|d_+\rangle,|s_-\rangle)\), the Bloch vectors of \(|\psi_-\rangle\) and \(|\psi_+\rangle\) are respectively \((g^{-1},0,-q/g)\) and \((-g^{-1},0,q/g)\). Since \(E_+-E_-=4tg\), the normalized projected Gibbs state has Bloch vector

\[
(r_x,r_y,r_z)=\tanh\!\left(\frac{2tg}{T}\right)(g^{-1},0,-q/g).
\]

The convex hull of pure one-qubit stabilizer states is exactly the octahedron \(|r_x|+|r_y|+|r_z|\leq1\). A Clifford encoding of the stabilizer code identifies this octahedron with precisely the stabilizer mixtures supported on \(\mathcal C\). Here \(r_x\geq0\) and \(r_z\leq0\), so sufficiency even has an explicit positive decomposition whenever \(r_x-r_z\leq1\): give weights \(r_x\) and \(-r_z\) to the logical \(+X\) and \(-Z\) stabilizer projectors and weight \(1-r_x+r_z\) to their logical maximally mixed state. Conversely the signed Pauli witness \(\bar X-\bar Z\) has expectation at most one on all logical-qubit stabilizer mixtures, while its expectation here is \(r_x-r_z\); conditional Pauli measurement transfers this obstruction to the full thermal state. Substitution establishes the stated necessary-and-sufficient criterion. For \(q>0\), \((1+q)/g>1\), and the hyperbolic tangent decreases strictly from one to zero as temperature increases; thus there is exactly one crossing. At \(q=0\), the Bloch vector is always on or inside the stabilizer octahedron.

**4. Uniqueness and asymptotics.** Set \(L(q)=\operatorname{artanh}(g/(1+q))\), so \(T_{\mathrm c}(U)=2tg/L(q)\). For \(q>0\),

\[
L'(q)=\frac{q-1}{2qg},\qquad
\operatorname{sgn}\frac{d}{dq}\frac{g}{L(q)}
=\operatorname{sgn}\left(\frac{q}{g}L(q)-\frac{q-1}{2q}\right).
\]

For \(0<q\leq1\) the last expression is positive. For \(q>1\), \(L(q)>g/(1+q)\), and \(q/(1+q)>(q-1)/(2q)\), so it is also positive. Further, \(L(q)=\frac12\log(2/q)+O(q)\) as \(q\downarrow0\), while \(L(q)=\frac12\log(2q)+O(q^{-1})\) as \(q\to\infty\). The substitution \(q\mapsto1/q\) preserves \(g/(1+q)\) and divides \(g\) by \(q\), proving the reciprocal identity above. The asserted critical-temperature asymptotics follow. The first expansion first implies \(q_{\mathrm c}(T)=\exp[-\Theta(t/T)]\) by logarithmic inversion. Substituting back into the exact critical relation sharpens it to \(\log(2/q_{\mathrm c}(T))=4t/T+O(q_{\mathrm c}(T)+q_{\mathrm c}(T)^2t/T)=4t/T+o(1)\), which proves the prefactor in the inverse exponential law.

Finally, for a convex two-state combination \((1-\lambda)|\psi_-\rangle\langle\psi_-|+\lambda|\psi_+\rangle\langle\psi_+|\), the logical octahedron test gives \(|1-2\lambda|\leq g/(1+q)\). The right-hand side of this inequality is minimized (i.e. the free interval is narrowest) when \(g/(1+q)\) is minimized, uniquely at \(q=1\). This contrasts with the strictly increasing thermal critical temperature.

## Verification
Run `python verify.py` with the dependency in `requirements.txt` from this package. The script reconstructs sixteen-dimensional Jordan–Wigner fermionic operators, their four-dimensional invariant sector, the spectral eigenvectors, the commuting Pauli-code projector, and the logical Bloch vectors using exact SymPy arithmetic. It also independently tests finite-temperature Bloch formulas at twenty parameter pairs and checks the increasing threshold numerically across thirteen positive interaction values. Its expected completion signal is `VERIFY_OK`. These finite checks test algebra and sample cases; the all-parameter and asymptotic statements follow from the displayed analytic proof, not from finite enumeration.

## Relationship to prior work
Zavatti, Bellomia and Capone (arXiv:2605.18494, first publicly submitted 18 May 2026), especially Secs. III and V and Appendix B, provide the Hubbard eigenstates, four-qubit magic framework, a plotted thermal magic-death boundary, and the qualitative explanation that cancellation between the two non-stabilizer eigenstates causes thermal death. Those observations and the standard one-qubit stabilizer octahedron are prior results. The contribution here is the exact analytic all-interaction threshold, a proof of the full-state equivalence via commuting-Pauli postselection, its strict monotonicity, and both sharp asymptotic regimes and inverse onset. No claim is made about a new Hubbard spectrum, the first observation of magic death, or a new qubit-octahedron description.

## Limitations
The theorem concerns only the half-filled, fixed-spin-number canonical ensemble, four occupation-ordered qubits, repulsive \(U\geq0\), and standard qubit stabilizer magic. It determines where log-free robustness equals one, **not** the magnitude of robustness outside the free region. It does not cover unrestricted particle-number ensembles, larger lattices, dynamical quenches, superselection-constrained resource theories, entanglement thresholds, or finite-time preparation effects. A related earlier formula outside the inspected literature cannot be categorically excluded.

## References
1. E. Zavatti, G. Bellomia and M. Capone, *Quantum magic of strongly correlated fermions – the Hubbard dimer*, arXiv:2605.18494, v1 submitted 2026-05-18; v2 dated 2026-06-24. https://arxiv.org/abs/2605.18494 ; full text https://arxiv.org/html/2605.18494v2 .
2. S. Bravyi and A. Kitaev, *Universal quantum computation with ideal Clifford gates and noisy ancillas*, Physical Review A 71, 022316 (2005), arXiv:quant-ph/0403025 (general stabilizer and magic-state framework).
