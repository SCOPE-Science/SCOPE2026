# Three-colorability-controlled vacancy ordering in cubic line-graph spin-1 antiferromagnets

## Finding

**Theorem.** Let \(G\) be a finite simple cubic graph on \(n\) vertices which admits a proper three-edge coloring, and let the sites of the classical antiferromagnet be the edges of \(G\), joined by interactions whenever the edges share an endpoint. Each site has \(s_e\in\{-1,0,1\}\). At zero magnetic field and \(J>0\), its Hamiltonian is
\[
H=J\sum_{\{e,f\}\in E(L(G))}s_es_f+D\sum_{e\in E(G)}s_e^2,
\]
with arbitrary real single-ion anisotropy \(D\). Then
\[
E_0(D)=\begin{cases}
n(3D/2-J),&D\leq0,\\
n(D-J),&0\leq D\leq J,\\
0,&D\geq J.
\end{cases}
\]
All ground states are characterized by the three incident edge labels at **every** vertex of \(G\):

| Anisotropy | Exactly permitted local triples, up to permutation |
|---|---|
| \(D<0\) | \((1,1,-1)\) or \((-1,-1,1)\) |
| \(D=0\) | \((1,1,-1)\), \((-1,-1,1)\), or \((1,-1,0)\) |
| \(0<D<J\) | \((1,-1,0)\) |
| \(D=J\) | \((1,-1,0)\) or \((0,0,0)\) |
| \(D>J\) | \((0,0,0)\) |

In particular, the open intermediate phase consists **exactly** of proper three-edge colorings of \(G\), with the three colors labeled \(-1,0,+1\). For **any** finite simple cubic graph, even without a known coloring, the sharp local inequality \(E_0(D)\geq n(D-J)\) for \(0<D<J\) becomes equality **if and only if** the graph is three-edge-colorable. At \(D=J\), ground configurations are precisely disjoint even cycles of occupied edges, with signs alternating along each cycle, and the zero-spin assignment elsewhere; the empty cycle collection is allowed.

For the cuboctahedron \(L(Q_3)\), where \(Q_3\) is the three-dimensional cube, the ordered degeneracies across the five regimes \(D<0\), \(D=0\), \(0<D<J\), \(D=J\), \(D>J\) are exactly
\[
450,\qquad3054,\qquad24,\qquad69,\qquad1.
\]
At \(D=0\), the \(3054\) states have \(8,9,10,11,12\) occupied sites with respective counts \(24,288,1044,1248,450\). At \(D=J\), the \(69\) states have \(0,4,6,8\) occupied sites with respective counts \(1,12,32,24\). With the usual uniform zero-field Gibbs measure, the zero-temperature magnetic Curie coefficient \(\lim_{\beta\to\infty}\chi/\beta=\operatorname{Var}_0(\sum_e s_e)\) equals \(64/25\) for \(D<0\), \(880/509\) for \(D=0\), and \(0\) for all \(D>0\), including \(D=J\).

## Assumptions and scope

The graph is finite, undirected, simple, cubic, and three-edge-colorable for the explicit ground-energy formula and classification in all anisotropy regimes. The more general coloring-if-and-only-if statement requires only a finite simple cubic graph. There are \(3n/2\) spin sites, one for each edge of \(G\); each line-graph bond is counted once. Interactions are homogeneous and antiferromagnetic, the single-ion term is homogeneous, and there is no external field. Counts for \(Q_3\) refer to **labeled** configurations, without factoring graph automorphisms or global reversal.

## Proof

Because \(G\) is simple and cubic, every pair of incident edges is counted exactly once in one of its vertex stars. Every spin's squared magnitude belongs to precisely two stars. Hence the exact decomposition is
\[
H=\sum_{v\in V(G)}\left[J(s_{e_1}s_{e_2}+s_{e_2}s_{e_3}+s_{e_3}s_{e_1})+\frac D2\sum_{i=1}^3s_{e_i}^2\right]
=\frac12\sum_v\left[J\Big(\sum_{e\ni v}s_e\Big)^2+(D-J)\sum_{e\ni v}s_e^2\right].
\]
The six distinct local energy types up to permutation and global sign are
\[
\begin{array}{c|rrrrrr}
\text{triple}&000&100&110&1\bar10&111&11\bar1\\\hline
\epsilon&0&D/2&J+D&D-J&3J+3D/2&-J+3D/2
\end{array}
\]
where \(\bar1=-1\), and the type \(1\bar10\) represents one positive, one negative, and one zero. Direct comparison of these six affine functions of \(D\) gives the complete local minimizing types displayed above. Thus the sum of local minima is a global lower bound, including both endpoints.

A proper three-edge coloring always exists by hypothesis. Assign \((1,1,-1)\) to the three color classes when \(D<0\); assign \((1,-1,0)\) when \(0<D<J\); use either construction at \(D=0\), the latter at \(D=J\), and all zeros at \(D>J\). Every local bound is then attained at every vertex, proving the energy formula. Conversely, any global minimizer must minimize each individual star, since their lower bounds sum to the already attained global minimum. This proves all five local classifications for all real \(D\), including the equality cases. In the interior, the local rule uses the labels \(-1,0,1\) exactly once at each vertex; that is precisely a proper three-edge coloring. The same lower-bound argument applies to any cubic graph, and equality in \(0<D<J\) itself constructs a proper coloring, proving the stated if-and-only-if without requiring that graph to be colorable a priori.

At \(D=J\), each nonempty vertex has two occupied incident edges carrying opposite signs; all other vertices have degree zero in the occupied subgraph. Its connected components are cycles on which signs alternate, forcing even length. Conversely any vertex-disjoint even cycles with alternating signs achieve the bound.

For the cube, the exact degeneracies can be certified by exhaustive integer enumeration of the \(3^{12}=531441\) labeled spin assignments. In the included checker, one method traverses all assignments and records their integer energy \(2H/J\) for anisotropy test values \(2D/J=-2,0,1,2,4\). A structurally independent method enumerates allowed triples over the four disjoint vertex stars on one bipartition class of the cube, then checks the remaining four stars. Its complete joint counters of occupancy and magnetization agree **exactly** with the first method at all five anisotropy values. The analytical local-type characterization makes the counter valid on each entire open anisotropy interval, not merely at the sampled values. The exact magnetization second moments are \(1152/450=64/25\) and \(5280/3054=880/509\), respectively; all \(D>0\) minimizers have zero net magnetization.

## Verification

Execute `python3 checker.py` in the same directory. The script uses only Python's standard library. It enumerates all 531441 cube configurations and separately all \(3^9=19683\) configurations for \(K_{3,3}\), checks the five specified ground energies, all cube counts and occupancy distributions, and reproduces the complete cube occupancy/magnetization counters using the disjoint-star construction. Both approaches are finite, exact-integer checks. The general theorem is proved by the star decomposition, not inferred from finite tests. The \(K_{3,3}\) check supplies an additional independent cubic bipartite example, not a universal certificate.

## Relationship to prior work

Schnack and Schnalle [1] studied the cuboctahedral antiferromagnetic *quantum Heisenberg* cluster, providing physical motivation for the graph but not the ternary classical-spin, tunable-vacancy theorem. Hwang, Park and Kwak [2] directly studied the antiferromagnetic Blume–Capel model on kagomé lattices; their work analyzes critical magnetic fields using density-of-states simulations and explicitly lists nonzero single-ion anisotropy as future work. Their Hamiltonian is the closest conceptual precedent, but the local cubic-line-graph classification, exact crystal-field coexistence manifolds and cuboctahedral degeneracy/response counts are not derived there. Changlani and Läuchli [3] analyze the *quantum Heisenberg* spin-1 kagomé magnet; they do not imply the ternary classical local-star result. The familiar graph-theoretic notions of edge coloring and even-cycle covers are used here, not claimed as new.

## Limitations

The universal ground-energy formula assumes three-edge-colorability. It does not claim the same energy for non-three-edge-colorable cubic graphs. All results are finite-volume, strictly zero-temperature characterizations, except the specified asymptotic susceptibility limits, and do not establish a thermodynamic-limit phase transition or quantum-spin behavior. The Curie coefficient assumes zero probing field before zero-temperature limit; the limit order matters. Historical priority for a potentially equivalent color/occupancy formulation elsewhere remains to be checked independently; absence of a match in examined sources is not a uniqueness proof.

## References

1. J. Schnack and R. Schnalle, *Frustration effects in antiferromagnetic molecules: the cuboctahedron*, arXiv:0810.2165 (first made public 2008-10-13). https://arxiv.org/abs/0810.2165
2. C.-O. Hwang, S. Park and W. Kwak, *Study of the Antiferromagnetic Blume-Capel Model on kagomé Lattice*, Journal of Physics: Conference Series **750**, 012016 (2016), DOI:10.1088/1742-6596/750/1/012016. https://doi.org/10.1088/1742-6596/750/1/012016
3. H. J. Changlani and A. M. Läuchli, *Trimerized ground state of the spin-1 Heisenberg antiferromagnet on the kagome lattice*, arXiv:1406.4767 (2014). https://arxiv.org/abs/1406.4767
