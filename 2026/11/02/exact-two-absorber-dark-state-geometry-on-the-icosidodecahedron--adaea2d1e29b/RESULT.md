# Exact two-absorber dark-state geometry on the icosidodecahedron

## Finding

For the homogeneous continuous-time single-excitation quantum walk on the 30-vertex icosidodecahedral graph, the dimension accessible to **two distinct irreversible absorbing vertices** is exactly one of three integers, determined by their relative geometry:

| Geometric position of the two vertices | Number of unordered placements | Accessible dimension | Dark dimension | Uniform-mixture absorption |
|---|---:|---:|---:|---:|
| Opposite vertices (graph distance five) | 15 | 8 | 22 | \(4/15\) |
| Graph distance three, with two shortest paths | 60 | 12 | 18 | \(2/5\) |
| Every other distinct pair | 360 | 13 | 17 | \(13/30\) |

All entries hold for **every** choice of strictly positive hopping and absorption rates. In particular, pair distance alone does not determine eventual capture: two types of distance-three pair have different outcomes. The best uniformly mixed absorption fraction achievable with two absorbing vertices is \(13/30\), even though the graph is connected.

## Assumptions and scope

Let \(G\) be the line graph of the generalized Petersen graph \(GP(10,2)\). Its 30 vertices correspond to the 30 edges of \(GP(10,2)\), with adjacency when those edges share an endpoint. This is the icosidodecahedral graph. Let \(A\) denote its real symmetric \(30\)-by-\(30\) adjacency matrix. Choose distinct graph vertices \(u,v\), and set, on the single-excitation Hilbert space \(\mathbb C^{30}\),

\[
H_{\mathrm{eff}}=JA-\frac{i}{2}\bigl(\kappa_u|u\rangle\langle u|+\kappa_v|v\rangle\langle v|\bigr),\qquad J,\kappa_u,\kappa_v>0.
\]

The nonnormalized no-capture density matrix evolves as \(\rho(t)=e^{-itH_{\mathrm{eff}}}\rho_0e^{itH_{\mathrm{eff}}^\dagger}\). The eventual total absorption probability is \(P_{\mathrm{abs}}(\rho_0)=1-\lim_{t\to\infty}\operatorname{tr}\rho(t)\) for every initial trace-one positive density matrix \(\rho_0\). There are no additional dephasing, losses, on-site disorder, or interactions.

Define the bright Krylov space and its dark orthogonal complement by

\[
\mathcal K_{uv}=\operatorname{span}\{A^ke_u,A^ke_v:0\le k\le6\},\qquad \mathcal D_{uv}=\mathcal K_{uv}^{\perp},
\]

and let \(\Pi_{uv}\) be the orthogonal projection onto \(\mathcal K_{uv}\). A distance-three pair has two shortest paths precisely when the integer matrix entry \((A^3)_{uv}=2\).

## Proof

**Step 1: Exact finite spectral cutoff.** Order the 30 edges of \(GP(10,2)\) lexicographically, with vertices \(0,\ldots,9\) on the outer decagon, \(10,\ldots,19\) on the inner star, and edges

\[
\{i,i+1\pmod {10}\},\quad \{i,10+i\},\quad \{10+i,10+(i+2\pmod{10})\},\qquad 0\le i<10.
\]

The complete integer calculation in `verify.py` constructs this graph and verifies, entry by entry,

\[
(A-4I)(A-2I)(A-I)(A+I)(A+2I)(A^2-2A-4I)=0.
\]

Consequently \(A^7\) is a linear combination of \(I,A,\ldots,A^6\). Thus \(\mathcal K_{uv}\) is invariant under \(A\), and the finite 30-by-14 Krylov matrix in the definition yields its **full** rank, rather than just a lower bound. The same check finds one-site Krylov rank seven at all 30 sites.

**Step 2: Exhaustive geometric rank certificate.** For each of the \(\binom{30}{2}=435\) unordered pairs the checker computes the shortest-path distance by breadth-first search, the exact integer \((A^3)_{uv}\), and the exact Krylov rank by rational Gaussian elimination. Its entire result is:

| Distance | Number of length-three walks when distance is three | Pair count | Exact Krylov rank |
|---:|---:|---:|---:|
| 1 | not applicable | 60 | 13 |
| 2 | not applicable | 120 | 13 |
| 3 | 1 | 60 | 13 |
| 3 | 2 | 60 | 12 |
| 4 | not applicable | 120 | 13 |
| 5 | not applicable | 15 | 8 |

These classes partition all 435 unordered pairs; every rank is calculated over \(\mathbb Q\), without numerical tolerances. Distinct vertices at distance three cannot have length-three walks with repeated vertices, so the computed walk count is exactly the number of shortest paths. This finishes the geometric classification.

**Step 3: Absorption from spectral accessibility.** Since \(A\) is Hermitian and \(\mathcal K_{uv}\) is invariant, \(\mathcal D_{uv}\) is reducing and every vector in it vanishes at \(u,v\). The evolution on \(\mathcal D_{uv}\) is therefore unitary. On the bright subspace, suppose \(H_{\mathrm{eff}}z=\lambda z\) with \(\operatorname{Im}\lambda=0\). Taking the imaginary part of \(\langle z,H_{\mathrm{eff}}z\rangle\) and using strict positivity of the two rates gives \(z_u=z_v=0\). Then \(Az=(\lambda/J)z\), so \(z\) is orthogonal to every \(A^ke_u,A^ke_v\), contradicting \(z\in\mathcal K_{uv}\) unless \(z=0\). All eigenvalues of the bright restriction thus have strictly negative imaginary part (the dissipative quadratic form also excludes positive imaginary parts). Its finite-dimensional evolution decays to zero even if Jordan blocks occur.

It follows that for every initial state

\[
P_{\mathrm{abs}}(\rho_0)=\operatorname{tr}(\Pi_{uv}\rho_0),\qquad \dim\mathcal D_{uv}=30-\operatorname{rank}\mathcal K_{uv}.
\]

For \(\rho_0=I/30\) the absorption probability is \(\operatorname{rank}\mathcal K_{uv}/30\). This yields the table and proves independence from all positive coupling-rate magnitudes.

## Verification

Run `python3 verify.py` in a directory containing this file. Only Python's standard library is needed. The checker builds the icosidodecahedron directly, verifies degree four and 60 edges, verifies the integer annihilating-matrix identity, checks all 30 one-site ranks, and computes exact rational ranks for every unordered two-site placement. Its asserted counts are \(15\), \(60\), and \(360\) for bright dimensions \(8\), \(12\), and \(13\), respectively. The 435-case exhaustive calculation is a complete finite certificate when combined with the analytic spectral cutoff and dissipation argument, not a sampling extrapolation.

## Relationship to prior work

Rousochatzakis, Läuchli, and Mila analyze the physical icosidodecahedral molecular-magnet topology and its one-magnon spectrum. Caruso and coauthors develop the general invariant-subspace interpretation of coherent trapping and irreversible transfer, especially for fully connected networks. Le, Donati, Severini, and Caruso explain graph-theoretic dark spaces, including paths, complete graphs, and cylinders, and methods to suppress trapping. Those spectral and absorption frameworks are prior art. The specific **exhaustive two-absorber classification on the icosidodecahedron**, including the distinction between two classes of distance-three pairs, is the claim assessed here; it is not asserted to extend to other graph families.

## Limitations

The conclusions require homogeneous Hermitian hopping, exactly two distinct positive-rate local absorbers, a single excitation, and an exact icosidodecahedral graph. They do not quantify finite-time decay rates, establish robustness to missing bonds or on-site disorder, or address local dephasing, interactions, or multiple excitation sectors. The finite-graph rank computations are exact and exhaustive, but historical publication priority is not independently certified.

## References

1. I. Rousochatzakis, A. M. Läuchli, F. Mila, *Highly Frustrated Magnetic Clusters: The kagomé on a sphere*, arXiv:0711.3231 (first posted 2007-11-20), Phys. Rev. B **77**, 094420 (2008). https://arxiv.org/abs/0711.3231
2. F. Caruso, A. W. Chin, A. Datta, S. F. Huelga, M. B. Plenio, *Highly efficient energy excitation transfer in light-harvesting complexes: The fundamental role of noise-assisted transport*, arXiv:0901.4454 (2009). https://arxiv.org/abs/0901.4454
3. T. P. Le, L. Donati, S. Severini, F. Caruso, *How to Suppress Dark States in Quantum Networks and Bio-Engineered Structures*, arXiv:1707.07482 (2017), J. Phys. A **51**, 365306 (2018). https://arxiv.org/abs/1707.07482
