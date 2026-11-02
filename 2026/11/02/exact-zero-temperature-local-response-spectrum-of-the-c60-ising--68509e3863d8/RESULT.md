# Exact zero-temperature local-response spectrum of the C60 Ising antiferromagnet

## Finding

Consider the truncated-icosahedral graph \(G\) with 60 vertices and 90 edges and the nearest-neighbor antiferromagnetic Ising Hamiltonian
\[
H(\sigma)=J\sum_{\{a,b\}\in E(G)}\sigma_a\sigma_b,\qquad J>0,\quad\sigma_a\in\{-1,+1\}.
\]
At zero external field, let \(C\) denote the zero-temperature limit of the connected two-point covariance matrix, with the Gibbs measure taken to the limit at fixed finite graph:
\[
C_{ab}=\lim_{\beta\to\infty}\left(\langle\sigma_a\sigma_b\rangle_\beta-\langle\sigma_a\rangle_\beta\langle\sigma_b\rangle_\beta\right).
\]
Then the **complete multiset of the 60 real eigenvalues** of \(C\) is
\[
\boxed{\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
0&30\\
2/5&11\\
74/125&5\\
104/125&4\\
112/25&4\\
(654-268\sqrt5)/125&3\\
(654+268\sqrt5)/125&3
\end{array}}
\]
Consequently the leading low-temperature local-field susceptibility satisfies
\[
\lim_{\beta\to\infty}\beta^{-1}\chi_{ab}(\beta)=C_{ab},\qquad
\chi_{ab}(\beta)=\left.\frac{\partial\langle\sigma_a\rangle_{\beta,\mathbf h}}{\partial h_b}\right|_{\mathbf h=0},
\]
where the field term is \(-\sum_b h_b\sigma_b\). The response has 30 null modes and 30 nonzero modes, despite the graph being connected. In particular the **uniform-field** leading Curie susceptibility vanishes exactly. The largest local-field-response eigenvalue is \((654+268\sqrt5)/125\).

The established, previously known zero-field energy and degeneracy are also recovered: \(E_{\min}=-66J\) and exactly 16,000 labeled spin configurations. They are included as supporting structure, **not as originality claims**. Every ground state has zero total magnetization. On the 30 bonds joining two different pentagons, \(C_{ab}=-1\); on the remaining 60 pentagonal bonds, \(C_{ab}=-3/5\).

## Assumptions and scope

The graph is the unique truncated icosahedron (the 60-site buckminsterfullerene graph). Every nearest-neighbor edge has the *same* positive coupling \(J\). Spins are classical, two-valued, and unconstrained. There are no other bonds or applied fields in the reference Gibbs measure. The graph is finite; the zero-temperature limit precedes any other thermodynamic or small-field limit. No statement about quantum Heisenberg spin correlations is made.

Construct \(G\) directly from the 12-vertex icosahedral graph \(I\). For each directed edge \((u,v)\) of \(I\), create a site. Join \((u,v)\) to \((v,u)\), and for any triangular face \(\{u,v,w\}\) of \(I\), join \((u,v)\) to \((u,w)\). This gives 30 cross-pentagon edges and 60 pentagonal edges.

## Proof

**1. Ground-state characterization.** Each of the 12 vertex-disjoint pentagons contributes at least one frustrated edge, since an odd cycle cannot be antialigned on every bond. Thus at least 12 of the 90 bonds satisfy \(\sigma_a\sigma_b=+1\), yielding \(H(\sigma)\ge J(2\cdot12-90)=-66J\). Equality holds precisely if each pentagon has exactly one frustrated edge and every cross-pentagon edge is unfrustrated.

The boundary of each of the 20 hexagons must have an even number of frustrated edges, because the product of spin products around any closed cycle is 1. At equality, this number is either zero or two. A frustrated pentagon edge belongs to exactly one hexagonal face; each such hexagon with two frustrations connects two different pentagons. The six selected hexagons consequently pair all 12 pentagons, giving a perfect matching of the original icosahedron. Conversely, a perfect matching of the icosahedron and the choice, for each of its six matched edges, of either adjacent triangular face determine 12 frustrated pentagon edges. Every pentagon has exactly one and every hexagon zero or two, so all facial parity conditions hold. By planar cycle-space generation and connectedness, precisely two opposite spin configurations realize each such frustration pattern. Direct matching recursion on the 12-vertex icosahedral graph gives exactly 125 perfect matchings, hence \(125\cdot2^6\cdot2=16000\) ground states.

Each pentagon has three spins of one sign and two of the opposite sign, and its sum equals the spin at the directed endpoint of its matched original edge. The paired pentagons have opposite such endpoint spins because their connecting edge is unfrustrated. Therefore every ground state obeys \(\sum_a\sigma_a=0\), not merely the ensemble mean.

**2. Reduction to 30 degrees of freedom.** For every undirected edge \(e=\{u,v\}\) of the original icosahedron, orient \(u<v\) and write \(x_e=\sigma_{(u,v)}\). The ground-state constraint on the interpentagon edge gives \(\sigma_{(v,u)}=-x_e\). Let \(U\) be the \(60\times30\) signed lifting matrix mapping these \(x_e\) into all 60 spins, so \(U^TU=2I_{30}\).

The uniform ground-state average has \(\langle\sigma\rangle=0\) by global spin inversion. Choose one representative from each of the 8,000 inversion pairs and let \(X\) be the \(8000\times30\) matrix of the corresponding \(x_e\) vectors. Then
\[
C=U\left(\frac{X^TX}{8000}\right)U^T,\qquad
B:=\frac{X^TX}{32}=125\left(2\frac{X^TX}{8000}\right).
\]
Because \(U^TU=2I\), the nonzero eigenvalues of \(C\) are those of \(B/125\). The matrix \(C\) has at least 30 zero eigenvalues.

**3. Exact finite matrix certificate.** The accompanying standard-library checker independently constructs the original graph and its faces, exhausts all 125 matchings and 64 face choices, recovers each unique spin state by graph propagation, and builds \(B\) using integer additions. All entries of \(X^TX\) are divisible by 32. Exact integer multiplication proves
\[
(B-50I)(B-74I)(B-104I)(B-560I)
(B^2-1308B+68596I)=0.
\]
Exact integer Gaussian elimination over \(\mathbb Q\), with content removal at each row step, proves
\[
\begin{array}{c|ccccc}
T&B-50I&B-74I&B-104I&B-560I&B^2-1308B+68596I\\\hline
\dim\ker T&11&5&4&4&6
\end{array}.
\]
These five mutually coprime factors account for all 30 dimensions. The irreducible quadratic has two roots \(654\pm268\sqrt5\), with equal multiplicity three because the matrix has rational entries and conjugate eigenvalues must have equal algebraic multiplicity. Thus \(B\) has no zero eigenvalue and the other 30 eigenvalues of \(C\) are zero, giving precisely the stated full spectrum. The trace check \(\operatorname{tr}C=60\) agrees with the diagonal identity \(C_{aa}=1\).

**4. Magnetic response.** With field energy \(-\sum_a h_a\sigma_a\), differentiating the finite Gibbs sum gives \(\chi(\beta)=\beta\operatorname{Cov}_\beta(\sigma)\). All positive-temperature configurations are finite in number, so the covariance tends to its uniform ground-state value as \(\beta\to\infty\). The uniform vector lies in \(\ker C\) since every ground state has total spin zero, completing the response assertion.

## Verification

Run `python3 verify_c60.py` from the directory containing this document. It requires only Python's standard library and checks the graph, exact 125-matchings census, 8,000 distinct ground-state frustration patterns, energy and magnetization, full covariance reduction, integer annihilating identity, exact rational matrix ranks, nearest-neighbor bond correlations, and all 1,770 unordered two-point correlations grouped by graph distance. The matrix identity and rational ranks are exact arithmetic checks, not finite-precision eigenvalue fits. The 8,000-pattern census is exhaustive because the proof establishes the bijection between *every* minimum-energy state and the constructed matching/face choices.

## Relationship to prior work

The antiferromagnetic Ising model on this precise graph is **not new**. Rasetti and Regge (1981) develop dimer/Pfaffian treatments of icosahedral Ising lattices; Samuel (1993) solves the Ising model on the truncated-icosahedral C60 graph; Dai and Xu (2024) explicitly report the known 16,000 ground-state degeneracy and its residual entropy. The main claim here is neither a new exact Ising partition function nor that already known degeneracy. The separate, exact **full connected covariance eigenvalue multiset and local-field response-nullspace classification** is the assessed distinction.

Konstantinidis (2006) studies classical-vector and quantum Heisenberg models on related fullerene geometry; Rausch, Plorin and Peschke (2020) calculate quantum \(S=1/2\) Heisenberg correlation functions on C60. Their spin operators, Gibbs measures and measured matrices differ from this classical two-valued zero-field ensemble; the quantum two-point values do not entail the stated Ising covariance spectrum. The primary 1993 Ising solution and 1981 paper were not available in full text for comprehensive comparison, so a hidden equivalent spectrum in those sources remains a priority risk. The finite-size field-free partition function alone does not directly specify this spectral factorization, but all-pair couplings or local-field generating functions, if provided therein, might imply it. No claim of independent certification is made.

## Limitations

This is an exact theorem only for a finite 60-site homogeneous nearest-neighbor classical Ising graph. It says nothing about extra next-neighbor bonds, spatial disorder, quantum spin states, dynamics, finite-temperature leading corrections, or a thermodynamic-limit transition. The theorem gives the eigenvalues, their multiplicities, a 30-dimensional pair-antipodal nullspace, and exact bond and distance-pair checks, but does not supply a concise symbolic real-space eigenvector basis. Historical novelty remains provisional, particularly because the 1981 and 1993 full texts could not be inspected.

## References

- M. Rasetti and T. Regge, *Dimer covering and Ising model on lattices homogeneous under the icosahedral group*, Rivista del Nuovo Cimento **4** (1981), 1–34. https://doi.org/10.1007/BF02740736
- S. Samuel, *The solution of the Ising model on the truncated icosahedron lattice of C60*, Journal of Mathematical Physics **34** (1993), 2331–2341. https://doi.org/10.1063/1.530119
- N. P. Konstantinidis, *The Icosahedral Symmetry Antiferromagnetic Heisenberg Model*, first public 2006-10-09, arXiv:cond-mat/0610218. https://arxiv.org/abs/cond-mat/0610218
- R. Rausch, C. Plorin, and M. Peschke, *The antiferromagnetic S=1/2 Heisenberg model on the C60 fullerene geometry*, arXiv:2011.12083 (2020). https://arxiv.org/abs/2011.12083
- Z. Dai and X. Y. Xu, *Residual entropy from temperature incremental Monte Carlo method*, arXiv:2402.17827 (2024). https://arxiv.org/abs/2402.17827
