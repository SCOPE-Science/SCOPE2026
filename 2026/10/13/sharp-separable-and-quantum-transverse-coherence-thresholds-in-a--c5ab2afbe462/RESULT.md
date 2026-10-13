# Sharp separable and quantum transverse-coherence thresholds in a frustrated Ising triangle

## Finding
Let \(X_j,Z_j\) denote Pauli matrices on qubit \(j\in\{1,2,3\}\). Define the antiferromagnetic triangle
\[
H=Z_1Z_2+Z_2Z_3+Z_3Z_1,\qquad \rho_c=\frac{I+cX}{2},\quad 0\le c\le1.
\]
Among all three-qubit states \(\sigma\) satisfying \(\operatorname{Tr}_{\{1,2,3\}\setminus\{j\}}\sigma=\rho_c\) for every \(j\), there exists a state with \(\operatorname{Tr}(H\sigma)=-1\) precisely for \(0\le c\le2/3\). Among fully separable states with those same marginals, a state with energy \(-1\) exists precisely for \(0\le c\le1/3\).

Hence \(1/3<c\le2/3\) is an exact interval where attaining the frustrated ground energy with the stated local coherence certifies entanglement. Both thresholds are sharp. This is a statement about simultaneous energy and *exact one-body density matrices*, not about unconstrained energy minimization or genuine multipartite entanglement.

## Assumptions and scope
The three sites form a triangle with positive unit Ising couplings and no field. The computational basis consists of simultaneous \(Z\)-eigenstates; all normalized density matrices, including mixed states, are allowed. Fully separable means a convex mixture of three-fold product density matrices, equivalently of pure product states. The local \(Y\)- and \(Z\)-expectations are zero and the local \(X\)-expectations equal the real common parameter \(c\in[0,1]\).

## Proof
**Ground space.** On a computational string \(b\in\{0,1\}^3\), the eigenvalue of \(H\) is \(3\) for \(000\) and \(111\), and \(-1\) for each of the other six strings. Thus \(H+I\) is positive semidefinite and any state with energy \(-1\) is supported on the six-dimensional ground space \(\mathcal G\).

**Separable necessity.** In a single product state, put \(z_j=\langle Z_j\rangle\in[-1,1]\). Let independent signs \(B_j\in\{-1,+1\}\) have respective means \(z_j\). The product-state energy \(e=z_1z_2+z_2z_3+z_3z_1\) obeys
\[
1+e=4\Pr(B_1=B_2=B_3)\ge0.
\]
Equality holds exactly when some \(B_i\) is deterministically \(+1\) and a different \(B_j\) is deterministically \(-1\). Indeed \(\Pr(B_1=B_2=B_3)=\prod_jp_j+\prod_j(1-p_j)\), where \(p_j=(1+z_j)/2\), and both nonnegative products vanish exactly under that condition. Consequently two local factors are opposite pure \(Z\)-eigenstates, so their \(X\) expectations vanish. The remaining local \(X\) expectation is at most \(1\). Thus \(\sum_j\langle X_j\rangle\le1\) on every energy-minimizing product state. In any separable mixture with energy \(-1\), every product constituent of positive weight must also attain \(-1\), because all product energies are at least \(-1\). Hence \(3c\le1\), or \(c\le1/3\).

**Separable sufficiency.** For \(0\le c\le1/3\), take \(\rho_+=(I+Z)/2\), \(\rho_-=(I-Z)/2\), and \(\eta_c=(I+3cX)/2\). The product \(\rho_+\otimes\rho_-\otimes\eta_c\) has energy \(-1\). Average this product over the three cyclic permutations of sites and additionally average each term with its conjugate under \(X^{\otimes3}\). This gives a fully separable state of energy \(-1\) whose three single-site marginals all equal \(\rho_c\). Positivity of \(\eta_c\) is precisely why the construction covers \(c\le1/3\).

**Quantum necessity.** Let \(P\) project onto \(\mathcal G\). Compress the collective transverse observable: \(A=P(X_1+X_2+X_3)P|_{\mathcal G}\). Its matrix is the adjacency matrix of the induced subgraph of the three-cube on the six bitstrings other than \(000,111\). This graph is the cycle \(C_6\), and its adjacency spectrum is \(2,1,1,-1,-1,-2\). In particular \(A\le2I\). Every ground-energy state therefore satisfies \(3c=\langle X_1+X_2+X_3\rangle\le2\), giving \(c\le2/3\).

**Quantum sufficiency.** Set
\[
|\Psi\rangle=\frac1{\sqrt6}\sum_{b\in\{0,1\}^3\setminus\{000,111\}}|b\rangle.
\]
This vector is in \(\mathcal G\), and each site has \(\langle Z_j\rangle=\langle Y_j\rangle=0\). Exactly two undirected edges of \(C_6\) correspond to flipping any given qubit, so \(\langle X_j\rangle=2/3\). The equally weighted incoherent mixture of the six ground basis states has marginals \(I/2\). Convex mixtures of these two density matrices realize every \(0\le c\le2/3\) at ground energy. This completes both if-and-only-if statements.

## Verification
The standalone standard-library script `verification/verify.py` checks the energy spectrum, the induced six-cycle adjacency and degree, its real symmetric row-sum bound, the count of two edges for each spin flip, the \(2/3\) quantum marginal, and exact rational sample points of the separable product/twirling construction. Run `python3 verification/verify.py` from the extracted package root. These finite checks corroborate the explicit algebraic proof; none substitute for the proof of the quantified inequalities.

## Relationship to prior work
Géza Tóth and József Pitrik, *General method for obtaining the energy minimum of spin Hamiltonians for separable states*, arXiv:2605.03022v1 (publicly submitted 2026-05-04), formulate fixed-single-site-marginal separable-energy optimization. Their Theorem 1 supplies a bondwise lower bound, Theorem 2 treats its saturation on two-colorable graphs, and the antiferromagnetic supplemental section SM7 discusses a different collective-spin and symmetric-separability problem. In particular their paper does not state the two thresholds for a three-site antiferromagnetic triangle with the identical transverse marginal \(\rho_c\). Earlier general energy-based entanglement-witness literature, including Dowling, Doherty, and Bartlett (2004), motivates energy criteria but is not credited with the present thresholds. The new claim is the exact paired fixed-marginal feasibility boundary \(1/3\) versus \(2/3\), not frustration, graph spectra, or energy witnesses as independent general methods.

## Limitations
This is an exact finite three-site classification at the unperturbed *ground energy*, not a formula for minimal energy at arbitrary fixed \(c\), a many-site theorem, a field-dependent phase diagram, a bound on entanglement depth, or an experimentally noise-tolerant witness. The coherent endpoint may be entangled without being genuinely tripartite; only non-full-separability is proved. An unindexed equivalent specialized calculation is a remaining publication-priority risk, despite targeted comparisons of published records and primary work.

## References
1. G. Tóth and J. Pitrik, *General method for obtaining the energy minimum of spin Hamiltonians for separable states*, arXiv:2605.03022v1 (2026-05-04), https://arxiv.org/html/2605.03022v1 .
2. M. R. Dowling, A. C. Doherty, and S. D. Bartlett, *Energy as an entanglement witness for quantum many-body systems*, Phys. Rev. A 70, 062113 (2004), DOI:10.1103/PhysRevA.70.062113 .
