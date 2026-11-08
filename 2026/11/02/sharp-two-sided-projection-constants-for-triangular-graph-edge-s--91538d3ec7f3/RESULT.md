# Sharp two-sided projection constants for triangular graph edge spaces

## Finding

Let \(n\ge5\) be an integer and let \(G=J(n,2)=L(K_n)\) be the graph whose vertices are the two-element subsets of \([n]\), two vertices being adjacent precisely when they intersect in one label. Choose any reference orientation for its edges. In the real coordinate-\(\ell_1\) edge space \(\mathbb R^{E(G)}\), let \(B\) be the signed vertex-edge incidence matrix, \(C=\operatorname{im} B^{\mathsf T}\) its cut (gradient) space and \(Z=\ker B\) its circulation space. Then the relative projection constants, where the infima range over **all** real linear idempotents having the indicated range, are

\[
\inf_{P^2=P,\operatorname{im}P=C}\|P\|_{1\to1}=\frac{(n-2)(3n-1)}{n(n-1)},\qquad
\inf_{P^2=P,\operatorname{im}P=Z}\|P\|_{1\to1}=\frac{2(2n-5)}{n-1}.
\]

The infima are attained, respectively, by the complementary Euclidean orthogonal projections \(Q=B^{\mathsf T}(BB^{\mathsf T})^+B\) and \(R=I-Q\). Each is the **unique** projection onto its range commuting with the natural signed edge action of \(S_n\). No uniqueness is asserted among arbitrary (non-invariant) minimizers. The positive gap is
\[
\|R\|_{1\to1}-\|Q\|_{1\to1}=\frac{n^2-3n-2}{n(n-1)}>0.
\]
**In the stated order, the cut and circulation constants tend to \(3\) and \(4\), respectively**, as \(n\to\infty\). (This corrects a reversed ordering of the limits in a former prose sentence; the formulas and slogan already had the correct limits.)

## Definitions and domain

The graph is simple, connected, undirected, unweighted and has \(N=\binom n2\) vertices, degree \(2(n-2)\), and \(M=N(n-2)\) edges. The reference orientation gives \(B_{ve}=+1\) at the tail and \(-1\) at the head of each edge, so \(BB^{\mathsf T}\) is its usual combinatorial Laplacian. Hence \(\dim C=N-1\) and \(\dim Z=M-N+1\). The edge norm is \(\|x\|_1=\sum_{e\in E(G)}|x_e|\). Graph automorphisms act by signed coordinate permutations, which are isometries for this norm. The theorem excludes \(n=4\) (the classical octahedral \(K_{2,2,2}\) case), general \(J(n,k)\), edge weights and other norms.

## Proof

**Invariant projections and global optimality.** Fix the vertex \(u=\{1,2\}\) and let \(H\le S_n\) stabilize it. The orbits on graph vertices are \(A=\{u\}\), \(D=\{\{a,j\}:a\in\{1,2\},3\le j\le n\}\), and \(F=\{\{i,j\}:3\le i<j\le n\}\). An \(H\)-invariant signed edge flow vanishes on internal edges of \(D\) and \(F\): each such edge admits an \(H\)-symmetry interchanging its endpoints. The remaining two edge orbits join \(A\) to \(D\) and \(D\) to \(F\). An invariant flow has a single amplitude on each, and vanishing divergence first at \(u\) and then at any vertex of \(F\) forces both amplitudes to zero. Therefore \(Z^H=0\).

For any graph vertex \(v\), its signed star \(s_v=B^{\mathsf T}\mathbf1_v\in C\) is fixed by its stabilizer. The stars span \(C\) and are conjugate under \(S_n\). An \(S_n\)-equivariant projection onto \(Z\) sends each star to a fixed circulation, hence to zero. Since it acts as identity on \(Z\), the only such projection is \(R\). If \(P\) is an equivariant projection onto \(C\), \(T=P-Q\) vanishes on \(C\) and maps \(Z\) to \(C\). Its Euclidean adjoint maps \(C\) to \(Z\) equivariantly, so kills all stars; therefore \(T=0\). Thus \(Q\) is likewise the unique equivariant projection onto \(C\).

Given any projection onto either invariant range, average its conjugates under \(S_n\). The average is still the identity on the range and has image in the range, hence is a projection. Its operator norm cannot increase because signed edge permutations are \(\ell_1\) isometries. Uniqueness of the equivariant projection proves that \(Q\) and \(R\) attain the **unrestricted** minima.

**One exact potential column.** By edge transitivity it suffices to use the oriented edge from \(\{1,2\}\) to \(\{1,3\}\). Set
\[
a=\frac{n+1}{2n(n-1)},\qquad b=\frac1{2n(n-1)}.
\]
On graph vertices, define \(\phi(\{1,2\})=a\), \(\phi(\{1,3\})=-a\), \(\phi(\{2,j\})=b\), \(\phi(\{3,j\})=-b\) for \(4\le j\le n\), and set all other values to zero. The mean is zero. Direct adjacency counting yields
\[
(BB^{\mathsf T}\phi)(\{1,2\})=(2n-3)a-(n-3)b=1,
\qquad(BB^{\mathsf T}\phi)(\{2,j\})=(n+1)b-a=0,
\]
with the antisymmetric values \(-1\) at \(\{1,3\}\) and zero at every other vertex. Hence \(BB^{\mathsf T}\phi=B\mathbf1_e\), and the \(e\)-column of \(Q\) equals \(B^{\mathsf T}\phi\).

**Column norm.** The nonzero differences \(|\phi(v)-\phi(w)|\) for edges occur in the following exhaustive types:

| Type | Multiplicity | Difference |
| --- | ---: | ---: |
| \(+a\) to \(-a\) | \(1\) | \(2a\) |
| \(\pm a\) to corresponding \(\pm b\) | \(2(n-3)\) | \(a-b\) |
| \(\pm a\) to zero | \(2(n-2)\) | \(a\) |
| \(\pm b\) to zero | \(2(n-3)(n-2)\) | \(b\) |
| \(+b\) to \(-b\) | \(n-3\) | \(2b\) |

Their sum is
\[
\sum_f|Q_{fe}|=4(n-2)a+2(n-3)(n-2)b
=\frac{(n-2)(3n-1)}{n(n-1)}.
\]
The diagonal entry is \(Q_{ee}=2a=(n+1)/(n(n-1))<1\). Since \(R=I-Q\), its column norm is
\[
\sum_f|R_{fe}|=1+\sum_f|Q_{fe}|-2Q_{ee}=\frac{2(2n-5)}{n-1}.
\]
The \(S_n\)-action is transitive on unoriented edges, changing only irrelevant column signs. Every column of \(Q\) and of \(R\) therefore has its respective displayed norm, equal to the \(\ell_1\to\ell_1\) operator norm. Combining this calculation with invariant averaging proves the theorem. The gap is positive for all \(n\ge5\), and the two rational limits are \(3\) and \(4\).

## Computation and limitation

The unchanged standalone `johnson_cycle_checker.py` constructs the actual signed incidence and exact rational projection columns for \(3\le n\le9\); it checks the Laplacian system, symmetry, all column sums, and diagonal effective resistance. Independent exact Laplacian-pseudoinverse calculations also confirmed the formulas for \(n=5,6\). These finite tests are consistency checks; the preceding group symmetry and potential proof applies to every integer \(n\ge5\). No formal or external expert certification is implied.

## Prior work and remaining priority risk

Dilworth, Kutzarova, and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (arXiv:2305.12582, 2023; published 2024), establish general invariant-projection techniques and work out tori/Hamming graphs. Their inspected theorems do not supply the sharp triangular-graph values. Abascal and collaborators, *A non-iterative parallelizable eigenbasis algorithm for Johnson graphs* (arXiv:1812.04230, 2018), study vertex-space spectral projectors, not these relative edge-cut/circulation constants. The familiar \(J(4,2)\cong K_{2,2,2}\) specialization is excluded. Equivalent formulas under other terminology remain a historical-priority risk; no assertion of absolute novelty is made.
