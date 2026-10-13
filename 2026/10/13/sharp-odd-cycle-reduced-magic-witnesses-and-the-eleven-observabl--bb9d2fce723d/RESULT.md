# Sharp odd-cycle reduced-magic witnesses and the eleven-observable transition

## Finding

**Theorem.** Fix any integer \(k\ge2\) and put \(L=2k+1\). Let \(\mathcal M=(P_0,\ldots,P_{L-1})\) be distinct nonidentity Hermitian \(N\)-qubit Pauli involutions, for any \(N\) permitting their realization, such that \(P_iP_j=-P_jP_i\) exactly when \(j\equiv i\pm1\pmod L\), and \(P_iP_j=P_jP_i\) otherwise. For **every** density operator \(\rho\) set \(b_i=\operatorname{tr}(\rho P_i)\), with cyclic indices. The reduced robustness of magic of these specified measurements equals

\[
\operatorname{RoM}_{\mathcal M}(\rho)=\max\left\{1,\ \max_{0\le i<L}(|b_i|+|b_{i+1}|),\ \frac1k\sum_{i=0}^{L-1}|b_i|\right\}.
\]

The sharp capacity (supremum over all density operators, for **every** such Pauli realization) is

\[
\boxed{\sup_\rho\operatorname{RoM}_{\mathcal M}(\rho)=\max\left\{\sqrt2,\ \frac1k\cot\left(\frac{\pi}{2(2k+1)}\right)\right\}.}
\]

The odd-hole witness, rather than an anticommuting pair, strictly determines the capacity exactly for \(k=2,3,4\), corresponding to \(C_5,C_7,C_9\); for every \(k\ge5\), corresponding to \(C_{11}\) and longer odd cycles, the sharp capacity equals \(\sqrt2\). At \(C_5\), the exact capacity is \(\tfrac12\sqrt{5+2\sqrt5}\); at \(C_7\) and \(C_9\), it is respectively \(\tfrac13\cot(\pi/14)\) and \(\tfrac14\cot(\pi/18)\).

## Assumptions and scope

A Pauli involution means a Hermitian tensor product of single-qubit Pauli operators, with an overall sign, whose square is the identity and whose trace is zero. Only the stipulated odd-cycle commutation graph is assumed: no graph-state preparation, independence of Pauli labels, or particular signs are additionally imposed. Such realizations exist for every \(k\): use \(L\) Jordan--Wigner Majoranas \(\gamma_j\) on \(k\) qubits and \(P_j=i\gamma_j\gamma_{j+1\bmod L}\). Extra idle qubits may be appended. The quantity \(\operatorname{RoM}_{\mathcal M}\) is the minimum coefficient \(\ell_1\)-norm among **signed affine decompositions** of the measured expectation vector into projected stabilizer states, with the coefficients summing to one (as in [1, Eq. (2)]). It is *not* the full-state robustness of magic. The maximum is over physical density operators on the realization's Hilbert space.

## Proof

**1. Every allowed commuting context has independent Pauli labels.** Pass to binary symplectic labels of the measured Paulis. Their commutation matrix over \(\mathbb F_2\) is the adjacency matrix of \(C_L\). A kernel vector obeys \(v_{i-1}+v_{i+1}=0\), hence is two-periodic, and because \(L\) is odd it is constant. Thus the matrix has rank \(L-1\) and its only possible nonempty label dependency is the *entire* cycle. The entire cycle is not a commuting context. No independent set of \(C_L\) supports a Pauli-product relation. Consequently the projected stabilizer polytope is exactly the sign-relaxed one (the no-active-dependency theorem [1]); in particular its generating signed incidence vectors have arbitrary independent signs on an independent set.

**2. The odd-hole inequality gives the complete reduced polytope.** Let \(B\subset\mathbb R^L\) be that centrally symmetric projected stabilizer polytope. The coordinatewise absolute value of each signed independent-set incidence vertex is an independent-set incidence vector. For any convex combination, the triangle inequality bounds its absolute coordinates by a convex combination of such incidence vectors; the classical stable-set polytope is downward closed. Conversely, the signed extension of every convex combination of independent-set incidence vectors realizes every \(b\) with \(|b|\in\operatorname{STAB}(C_L)\), using balanced opposite signs wherever a coordinate must vanish. The latter classical polytope is characterized by

\[
 x_i\ge0,\quad x_i+x_{i+1}\le1\ (0\le i<L),\quad \sum_i x_i\le k.
\]

For completeness, here is an extremality proof of that description. On any face where some \(x_j=0\), the other vertices form a path of \(2k\) vertices, whose edge-and-nonnegativity polytope has only integral vertices (the edge incidence matrix of a bipartite path is totally unimodular); the displayed sum inequality is redundant, since the remaining vertices can be partitioned into \(k\) disjoint adjacent pairs. A vertex with every \(x_i>0\) would require \(L\) independent active constraints among the \(L\) edge bounds and the one sum bound. If all \(L\) edge bounds are active, oddness forces every \(x_i=1/2\), violating the sum bound. If exactly \(L-1\) edge bounds and the sum bound are active, write successive coordinates on the resulting length-\(L\) path as \(t,1-t,t,\ldots,t\). Their sum is \(k+t\), forcing \(t=0\), also a contradiction. Fewer active edge bounds cannot make a vertex. Therefore all vertices are independent-set incidence vectors.

It follows that \(B=\{b:|b_i|+|b_{i+1}|\le1,\ \sum_i|b_i|\le k\}\). The associated Minkowski gauge is

\[
\gamma_B(b)=\max\left\{\max_i(|b_i|+|b_{i+1}|),\ \frac1k\sum_i|b_i|\right\}.
\]

The signed-affine minimum \(\ell_1\) norm equals \(\max(1,\gamma_B(b))\): any decomposition has norm at least these two quantities. Conversely if \(\gamma_B(b)=g>1\), represent \(b/g\) by a convex combination of vertices of \(B\), assign total positive coefficient \((g+1)/2\) to that combination and total negative coefficient \((1-g)/2\) to the corresponding opposite vertices. This reconstructs \(b\), has coefficients summing to one and \(\ell_1\)-norm \(g\). For \(g\le1\), an ordinary convex decomposition attains one. This proves the first displayed formula.

**3. The edge capacity.** For adjacent anticommuting Hermitian Pauli involutions \(P,Q\), \((sP+tQ)^2=2I\) for signs \(s,t\in\{\pm1\}\). Hence \(|\langle P\rangle|+|\langle Q\rangle|\le\sqrt2\). Equality holds on a \(+1\) eigenstate of \((P+Q)/\sqrt2\), so the capacity of the edge contribution is exactly \(\sqrt2\).

**4. The odd-cycle capacity.** By maximizing over sign choices,

\[
\sup_\rho\sum_i|\langle P_i\rangle_\rho|=\max_{s_i\in\{\pm1\}}\lambda_{\max}\left(\sum_i s_iP_i\right).
\]

The alternating commutation matrix has one-dimensional radical and rank \(2k\). The central product \(\Omega=iP_0P_1\cdots P_{L-1}\) is a Hermitian involution (there are \(L\) anticommuting pairs in the total product); its possible eigenvalues are \(\pm1\). Choose a symplectic basis of the \(2k\)-dimensional quotient by the radical. Within either \(\Omega\)-eigenspace, one obtains \(k\) pairs of anticommuting Pauli monomials, with every other pair commuting. Diagonalizing one involution of the first pair and using the other to interchange its equally sized eigenspaces identifies that pair with \(X\otimes I,Z\otimes I\); repeat inside the commutant for the remaining pairs. This elementary induction reduces each finite-dimensional representation to a tensor product of \(k\) qubit Pauli pairs and an identity multiplicity factor. The only remaining central sign is accommodated by flipping one of the \(P_i\). Thus **each** allowed realization splits into copies of one of the two signed canonical models \(P_i^*=i\gamma_i\gamma_{i+1}\). This is the elementary finite Pauli/Clifford representation argument; it involves no assumption about the number of idle qubits.

For any sign vector, the canonical Hamiltonian is a quadratic Majorana cycle \(H_s=i\sum_i s_i\gamma_i\gamma_{i+1}\). Vertex-sign conjugations on the real skew adjacency matrix reduce its edge signs to a single loop-flux sign. The two fluxes have the same skew spectrum for **odd** \(L\): reversing every edge sign changes the flux (since \(L\) is odd) and negates the skew matrix, but a real skew-symmetric matrix has symmetric imaginary eigenvalues. Hence every signed model has the same top eigenvalue as the all-plus model. The latter is a real skew circulant with eigenvalues \(2i\sin(2\pi j/L)\), \(j=0,\ldots,L-1\). Orthogonal block diagonalization of a quadratic Majorana Hamiltonian gives its extreme energies as positive/negative sums of the positive singular-mode strengths. Accordingly

\[
\lambda_{\max}(H_s)=2\sum_{j=1}^{k}\sin\left(\frac{2\pi j}{L}\right)=\cot\left(\frac{\pi}{2L}\right).
\]

The last equality follows from the finite sine-sum formula. Taking a maximum-eigenstate attains this value, proving that the odd-hole contribution has sharp capacity \(\cot(\pi/(2L))/k\), for every representation and central sign.

**5. Exactly where the dominant witness changes.** Put \(f(x)=\cot(\pi/(4x+2))\) for \(x>0\), and extend continuously by \(f(0)=0\). Its derivative is \(f'(x)=\frac4\pi(y/\sin y)^2\) with \(y=\pi/(4x+2)\). Since \(y/\sin y\) is strictly increasing for \(0<y<\pi/2\), while \(y\) decreases with \(x\), the derivative \(f'(x)\) strictly decreases. Thus \(f\) is strictly concave and \(f(k)/k\) strictly decreases. Direct exact comparisons bracket the crossing: \(\cot(\pi/18)/4>\sqrt2\), since \(\tan(3\arctan(1/(4\sqrt2)))=95\sqrt2/232>1/\sqrt3\); while \(\cot(\pi/22)/5<\sqrt2\), since \(\tan(\pi/22)>\pi/22>1/(5\sqrt2)\). Hence \(k=2,3,4\) and only those yield odd-hole dominance. All extrema asserted are attained by the explicitly described eigenstates. \(\square\)

## Verification

The accompanying standalone `verify.py` tests the canonical Pauli realization and every commutation relation for \(L=5,7,9,11,13,15,17\). It compares exact finite-matrix spectra for multiple signed Hamiltonians against the closed cotangent formula, verifies the \(C_5\) characteristic polynomial \(\lambda^4-10\lambda^2+5\) **symbolically for all 32 sign patterns**, and compares 256 independently sampled pure-state measurement vectors against an independently solved signed-affine linear program. These finite tests are checks on the analytic arguments, not proofs for arbitrary lengths or arbitrary representations. `requirements.txt` specifies the numerical and symbolic libraries; run `python verify.py` from the extracted directory.

## Relationship to prior work

Liu et al. [1] introduce the sign-relaxed reduced stabilizer polytope, prove its exactness without active dependencies, and solve **perfect-graph** frustration models with clique capacity \(\sqrt{\omega}\). An odd cycle of length at least five is not perfect; the odd-hole inequality adds a genuinely different witness. The h-perfect/odd-cycle stable-set facts and simultaneous squared-Pauli uncertainty analysis in Xu et al. [2] supply classical polyhedral context but do **not** evaluate reduced robustness or its sharp witness-capacity crossover. The generator-to-generator free-fermion mapping for line-graph Hamiltonians in Chapman et al. [3] provides the known fermionic mechanism behind the *spectral* calculation; no novelty is claimed for diagonalizing a generic quadratic free-fermion Hamiltonian. Varela et al. [4] introduce the reduced-magic measurement framework but do not report the present odd-cycle capacity classification. The contribution here is the combined all-length, all-realization, exact reduced-magic formula **and** its three-cycle-to-clique sharp crossover.

## Limitations

Only the reduced (measurement-projected) robustness is computed; the full state's magic may be larger. The theorem requires **exactly** the specified anticommutation cycle. Additional measured Paulis, commutation edges, or active Pauli dependencies change the projected polytope. The capacity is a supremum over states for a *fixed* measurement set, not a statement about typical states, experimental noise robustness, or computational advantage. The ingredients of sign-relaxed polytopes, odd-cycle facets, and free-fermion diagonalization are established earlier; an equivalent all-length synthesis in otherwise unindexed literature remains a priority risk. Independent validation has not been performed.

## References

[1] Y. Liu, A. Gasull, M. Hu, R. Zhang, F. Baccari, J. Tura, *Graph Theoretic Approach to Quantum Nonstabilizerness*, arXiv:2607.26154v1 (first public 2026-07-28), https://arxiv.org/html/2607.26154v1 .

[2] K.-M. Xu et al., *Simultaneous variances of Pauli strings, weighted independence numbers, and a new kind of perfection of graphs*, arXiv:2511.13531v1, https://arxiv.org/html/2511.13531v1 .

[3] A. Chapman, S. Elman, and R. L. Mann, *A Unified Graph-Theoretic Framework for Free-Fermion Solvability*, arXiv:2305.15625v1, https://arxiv.org/html/2305.15625v1 .

[4] A. Varela et al., *Predicting Magic from Very Few Measurements*, arXiv:2602.18939v1, https://arxiv.org/html/2602.18939v1 .
