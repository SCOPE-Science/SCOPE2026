# An isotropic ten-mode response in the icosidodecahedral Ising plateau

## Finding

Let \(D=GP(10,2)\) denote the 20-vertex dodecahedral graph, and let \(G=L(D)\) be its 30-vertex line graph, the icosidodecahedron. Consider unit Ising spins \(\sigma_e\in\{-1,1\}\) on its vertices with uniform antiferromagnetic interaction and field
\[
H(\sigma)=J\sum_{\{e,f\}\in E(G)}\sigma_e\sigma_f-h\sum_{e\in E(D)}\sigma_e,
\qquad J>0,\quad 0<h<4J.
\]
At zero temperature the 36 ground states have exactly one down spin in each of the 20 triangular faces. Their down-spin indicator vectors \(n_e=(1-\sigma_e)/2\) are precisely the characteristic vectors of the 36 perfect matchings of \(D\). Put \(B\in\mathbb R^{20\times30}\) for the unsigned vertex-edge incidence matrix of \(D\), and let \(P\) be the Euclidean orthogonal projector onto \(\ker B\). For the uniform measure on these ground states, the full 30-site covariance is exactly
\[
\boxed{\operatorname{Cov}(n)=\frac23P,\qquad
\operatorname{Cov}(\sigma)=\frac83P.}
\]
Consequently there are exactly **ten equal, nonzero** covariance eigenvalues \(8/3\) for the spins, and twenty zero eigenvalues. With independent probe fields \(b_e\) coupled by \(-\sum_e b_e\sigma_e\), define \(\chi_{ef}(\beta)=\partial\langle\sigma_e\rangle_\beta/\partial b_f\) at \(b=0\). In the stated plateau interior,
\[
\boxed{\lim_{\beta\to\infty}\frac{\chi(\beta)}{\beta}=\frac83P.}
\]
Since \(A_G=B^{\mathsf T}B-2I\), the response projector \(P\) is also **exactly the spectral projector of the single-particle adjacency matrix onto its eigenvalue \(-2\)**. Thus the zero-temperature Ising fluctuation subspace coincides with the ten-dimensional one-magnon flat-band subspace.

There is also a complete exact two-site formula. For distinct sites \(e,f\), let \(c(e,f)\) count ground states with both spins down. For positive fugacities \(x,y\), the full ground-manifold generating polynomial is
\[
\boxed{Z_{ef}(x,y)=36+12(x-1)+12(y-1)+c(e,f)(x-1)(y-1).}
\]
The multiplicities and coefficients are completely determined by the line-graph distance \(d\), number \(p\) of common pentagonal faces, and number \(w\) of shortest paths:

| \(d\) | \(p\) | \(w\) | Pairs | \(c(e,f)\) |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | 60 | 0 |
| 2 | 0 | 1 | 60 | 7 |
| 2 | 1 | 1 | 60 | 5 |
| 3 | 0 | 1 | 60 | 3 |
| 3 | 0 | 2 | 60 | 2 |
| 4 | 0 | 1 | 60 | 4 |
| 4 | 0 | 3 | 60 | 5 |
| 5 | 0 | 4 | 15 | 4 |

This exhausts all \(\binom{30}{2}=435\) unordered pairs. In particular, \(\operatorname{Cov}(n_e,n_f)=(c(e,f)-4)/36\) for distinct sites. The normalized interaction of two pinning fugacities has an exact sign law:
\[
\frac{36 Z_{ef}(x,y)}{Z_e(x)Z_f(y)}-1
=\frac{(c(e,f)-4)(x-1)(y-1)}{4(x+2)(y+2)},
\qquad Z_e(x)=12(x+2).
\]
Two-site pinning can therefore be cooperative, antagonistic or exactly independent, depending on geometry.

## Assumptions and scope

The graph \(D\) is the simple graph with vertices \(0,\ldots,19\), and edges \(\{i,(i+1)\bmod10\}\), \(\{i,10+i\}\), and \(\{10+i,10+(i+2)\bmod10\}\) for \(i=0,\ldots,9\). The graph \(G=L(D)\) has one site for each edge of \(D\); two sites are neighbors precisely when the corresponding edges share an endpoint. Each spin is classical and takes values \(\pm1\). The homogeneous exchange \(J\) and field \(h\) satisfy the strict bounds above. The zero-temperature state is the limiting finite-temperature Gibbs state with **no** site-dependent probe fields. Susceptibility takes its derivatives before the \(\beta\to\infty\) limit; its nonzero Curie coefficient is not a finite-temperature susceptibility value.

## Proof

**1. Exact ground-state characterization.** Each edge of \(G\) belongs to a unique triangle, and each spin belongs to two such triangles. Write the Hamiltonian as the sum of 20 local energies \(J(\sigma_1\sigma_2+\sigma_2\sigma_3+\sigma_3\sigma_1)-(h/2)(\sigma_1+\sigma_2+\sigma_3)\). The energies for, respectively, zero, one, two and three down spins are
\[
3J-3h/2,\quad -J-h/2,\quad -J+h/2,\quad 3J+3h/2.
\]
For \(0<h<4J\), the unique local minimum is the one-down pattern, with every other local pattern costing at least \(\delta=\min\{h,4J-h\}>0\). The constraints are simultaneously realizable: one down spin per triangle selects one edge incident to each vertex of \(D\), hence a perfect matching. The ground energy is \(E_0=-20J-10h\) and every other state has at least \(\delta\) more energy.

**2. Finite exact second-moment certificate.** Let \(\mathcal M\) be the perfect matchings of \(D\). Define
\[
K_{ef}=\#\{M\in\mathcal M:e\in M, f\in M\},
\qquad Q_{ef}=K_{ef}-4.
\]
The diagonal entries of \(K\) equal 12, and there are 36 matchings in total, so \(Q=36\operatorname{Cov}(n)\). The accompanying deterministic `check.py` independently enumerates matchings and evaluates endpoint-deletion recurrences in integer arithmetic. It checks all 435 distinct pairs, all twelve pentagonal faces and all 900 matrix-product entries, yielding the **exact integer identities**
\[
Q^{2}=24Q,\qquad BQ=0,\qquad \operatorname{tr}(Q)=240.
\]
These are finite exhaustive facts, not inferences from floating-point experiments: every vertex-subset matching count is obtained from the recurrence that pairs the smallest unmatched vertex with one of its remaining neighbors. The program checks the full set of integer identities and prints the complete eight-class table.

**3. From the certificate to the projector.** The symmetric matrix \(Q\) satisfying \(Q^2=24Q\) is 24 times an orthogonal projector. Its rank is \(\operatorname{tr}(Q)/24=10\). The connected graph \(D\) contains pentagons; hence the unsigned incidence matrix \(B\) has full row rank 20. Indeed, a real vector in the left nullspace of \(B\) would alternate sign along every edge, and the odd cycle forces it to vanish. Thus \(\dim\ker B=30-20=10\). Since \(BQ=0\), the range of \(Q\) is contained in \(\ker B\); the equal dimensions give \(Q=24P\). Consequently \(\operatorname{Cov}(n)=Q/36=(2/3)P\) and \(\operatorname{Cov}(\sigma)=4\operatorname{Cov}(n)\).

**4. Spectrum, susceptibility and pinning.** For a simple graph, \(B^{\mathsf T}B=2I+A_G\), proving the flat-band statement. The finite-volume fluctuation-dissipation identity gives \(\chi(\beta)=\beta\operatorname{Cov}_\beta(\sigma)\). Because the energy gap \(\delta\) separates the 36 ground states, the Gibbs covariance converges to the uniform-ground-state covariance as \(\beta\to\infty\). The pair polynomial follows by partitioning the 36 matchings into the four membership types for \(e,f\): their respective counts are \(12+c\), \(12-c\), \(12-c\), \(c\). Substituting into the polynomial yields its formula and the pinning sign law.

## Verification

Run `python3 check.py` using only the Python standard library. It constructs \(GP(10,2)\) explicitly, enumerates all 36 matchings, checks the count independently by vertex-subset recursion, compares all 435 double-edge counts by these two methods, identifies the twelve pentagonal cycles, verifies the entire pair-geometric classification, and checks \(Q^2=24Q\), \(BQ=0\) and \(\operatorname{tr}Q=240\) in integer arithmetic. The expected terminal message is `ALL_EXACT_CHECKS_PASS matchings=36 faces=12 pairs=435 rank_projection=10`. The proof of the Gibbs limit, susceptibility and incidence-rank statements is analytical and does not rely on an untested extrapolation from code.

## Relationship to prior work

Rousochatzakis, Läuchli and Mila established the 36 one-up-up-down Ising configurations of this cluster and their correspondence with perfect matchings of the dodecahedron. Their work also separately describes ten independent localized one-magnon modes. Both are acknowledged premises, not asserted discoveries. The present statement identifies the **full second-moment operator** of the uniformly weighted Ising plateau as a scalar multiple of the one-magnon flat-band spectral projector, together with the exact site-resolved Curie susceptibility and complete two-pin generating functions. These identities do not follow from the two known dimensions alone. Kunisada and Fukumoto analyzed quantum Heisenberg **bond-spin** correlations in a different zero-field state, not this uniform classical Ising occupancy covariance. The known total of 36 dodecahedral perfect matchings does not itself determine their pairwise cooccupancies or the projector identity. No claim of independent historical-priority certification is made.

## Limitations

This is an exact finite-cluster Ising result, not a statement about all kagome lattices, quantum Heisenberg ground states, perturbed exchange couplings or thermodynamic-limit phases. The equal-weight classical plateau is selected by the stated order of limits. Exact local biases at fixed strength may split the manifold; the Curie-coefficient formula concerns derivatives at zero bias. Although the code proves every finite integer identity exhaustively, its source and the priority comparison should be independently checked before publication. The flat-band identity is specific to the incidence representation and does not imply that the 36-state quantum dimer Hamiltonian has the same spectrum.

## References

- I. Rousochatzakis, A. M. Läuchli and F. Mila, *Highly Frustrated Magnetic Clusters: The kagomé on a sphere*, first submitted 2007-11-20, https://arxiv.org/abs/0711.3231 ; Phys. Rev. B **77**, 094420 (2008), https://doi.org/10.1103/PhysRevB.77.094420 . See particularly the one-magnon discussion and the icosidodecahedral Ising manifold.
- N. Kunisada and Y. Fukumoto, *Dimer-dimer correlations and magnetothermodynamics of S=1/2 spherical kagome clusters*, Physics Procedia **75** (2015), 687–694, https://doi.org/10.1016/j.phpro.2015.12.089 .
- *Number of perfect matchings of the Dodecahedron*, MathOverflow discussion (2015), https://mathoverflow.net/questions/192159/number-of-perfect-matchings-of-the-dodecahedron .
