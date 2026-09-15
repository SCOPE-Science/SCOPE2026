# Two-sided tropical Torelli recovery from the mu-polystable decomposition is false

## Context
The target asks whether, for fixed genus g>=3 and a fixed nondegenerate universal polarization mu of degree d, the mu-polystable polyhedral decomposition P^trop_mu(X) of the tropical Jacobian determines the metric biconnected components of a bridgeless stable weighted tropical curve X. The biconditional claims: P^trop_mu(X) isomorphic to P^trop_mu(X') as polyhedral complexes if and only if the biconnected components of X and X' are pairwise isomorphic as weighted metric graphs.

## Definitions
- T: banana/theta minimal model with 2 vertices v0,v1, 4 parallel edges, all vertex weights 0. Genus g=|E|-|V|+1=3.
- X: T with edge-lengths (1,1,1,1). X': T with edge-lengths (1,1,1,2).
- mu: canonical universal polarization of degree d=1, mu(v)=d(2w(v)-2+val(v))/(2g-2)=1/2 per vertex.
- P^trop_mu(X): polyhedral complex obtained as colimit of polytopes P_{E,D}(X) over the mu-polystable poset PSD_mu, glued along faces per specialization (Abreu-Andria-Pacini-Taboada Props 6.1-6.2).
- Isomorphism of polyhedral complexes: combinatorial isomorphism (bijection of cells preserving face poset/gluing), the standard meaning in Abreu et al.

## Result
The admitted biconditional is FALSE. The only-if direction fails: X and X' have isomorphic mu-polystable polyhedral complexes but non-isomorphic biconnected components as weighted metric graphs. The if direction is not addressed and may hold; the biconditional as stated is refuted.

## Proof / evidence
1. Hypotheses: T is bridgeless (deleting any edge leaves 3 parallel edges, connected), stable (valence 4>=3, weights 0), biconnected (no cut vertex), hence each of X,X' has a single biconnected component. Verified computationally.
2. Nondegeneracy: for the only nonempty proper subsets {v0},{v1}, mu({v})-delta({v})/2=1/2-4/2=-3/2, non-integral, so mu is nondegenerate. Hence mu-semistable equals mu-stable and PSD_mu(T) coincides with the (v0,mu)-quasistable poset QD(T).
3. Same complex: cells P_{E,D}(X) are indexed by PSD_mu and glued per poset order. Stability numbers beta_{E,D}(V)=deg(D|_V)-mu_E(V)+delta/2 use only integer divisor values, mu-values, and cut sizes, never edge-lengths. Direct enumeration of QD_{v0,mu}(T) from the beta-formula gives 32 pseudo-divisors with rank distribution {0:4,1:12,2:12,3:4} and maximal rank 3=b1(T). Every F with |F|<=3 is nondisconnecting, so every cell is simple (P=K) with length-independent face relations. Since X,X' share model T and mu, posets and gluings agree, so the complexes are isomorphic as polyhedral complexes.
4. Different blocks: Aut(T) permutes the 4 parallel edges (and may swap vertices), so metric isomorphism classes are classified by sorted length tuples: (1,1,1,1) vs (1,1,1,2) differ.
5. Corroboration: Jacobian volumes via Kirchhoff matrix-tree sums over spanning-tree complements are 4 for X and 7 for X', so even the principally polarized Jacobians differ. Consistent with classical tropical Torelli (Brannetti-Melo-Viviani): Jacobians remember only total C1-set lengths; the polystable subdivision adds no further metric data.

## Limitations
Refutation uses the combinatorial (face-poset) reading of polyhedral-complex isomorphism. Under a metric cell-by-cell isometry reading the two complexes differ, but so do the blocks, so that reading does not engage the target's intent. The converse direction (matching metric blocks implies same complex) is not disproved.

## Reproducibility
Run output/artifacts/enumerate_theta.py (pure Python, stdlib only): checks genus, bridges, stability, biconnectivity, mu nondegeneracy, enumerates quasistable pseudo-divisors from the beta-formula, checks length multisets and Jacobian volumes, writes theta_counterexample.json with the 32-item poset summary and volumes.

## References
- A. Abreu, M. Pacini, The universal tropical Jacobian and the skeleton of the Esteves universal Jacobian, Proc. LMS 120(3), 2020 (arXiv:1806.05527).
- A. Abreu, S. Andria, M. Pacini, D. Taboada, A universal tropical Jacobian over M_g^trop (arXiv:1912.08675): mu-polystability, PSD=QD, Props 6.1-6.2, Thm 6.6.
- S. Brannetti, M. Melo, F. Viviani, On the tropical Torelli map, Adv. Math. 2011: fibers via C1-sets/3-edge-connectivization.
