# Four-coordinate threshold for geometric fixed points of binary Hamming Rips complexes

## Finding
For every integer \(k\ge4\) and every integer \(f\ge1\), let \(Q_n=\{0,1\}^n\) with Hamming distance and put
\[
X_n=\operatorname{VR}_{\le3}(Q_n,d_H).
\]
The symmetric group \(S_k\) permutes the first \(k\) coordinates and fixes the final \(f\) coordinates. Its **geometric** fixed-point space, not merely the invariant part of its homology, satisfies
\[
\boxed{
|X_{k+f}|^{S_k}\simeq
\begin{cases}
|X_f|\vee |X_f|\vee\bigvee^{2^{f+1}-1}S^1,&k=4,\\
|X_f|\sqcup|X_f|,&k\ge5.
\end{cases}}
\]
In both cases the fixed space has a canonical simplicial orbit-barycenter triangulation. In the first case the homotopy equivalence is not asserted to be a PL homeomorphism. The four-coordinate case is connected and has exactly \(2^{f+1}-1\) independent new loops; the five-or-more-coordinate case has exactly two connected components.

For instance, \(|X_4|\cong S^7\), since the only forbidden edges in its distance-three compatibility graph are the eight antipodal pairs. Thus with four free coordinates the \(S_4\)-fixed space is homotopy equivalent to \(S^7\vee S^7\vee\bigvee^{31}S^1\), whereas the \(S_5\)-fixed space with the same four free coordinates is \(S^7\sqcup S^7\).

## Assumptions and scope
All distances are ordinary integer Hamming distances, inclusive at scale three; the group acts only by coordinate permutations on a single contiguous labeled block, with at least one untouched coordinate. No claim is made about a cyclic subgroup in place of \(S_k\), general signed-permutation subgroups, or other Rips scales. The all-coordinate specialization \(f=0\) is excluded from the new statement because it has an earlier classification; the same argument independently gives \(S^1\) for \(k=4\) and \(S^0\) for \(k\ge5\) at that boundary.

## Proof
**Orbit-barycenter lemma.** For a finite simplicial complex \(K\) on whose vertices a finite group \(G\) acts, take one new vertex for each vertex orbit \(O\) which itself spans a simplex of \(K\). A collection of these new vertices spans a simplex exactly when the union of their original orbits is a face. Map its vertex to the barycenter of its orbit. Every fixed point has constant barycentric coefficients on each orbit, hence lies in exactly such a simplex; these affine maps agree on overlaps and give a canonical PL homeomorphism from the orbit-barycenter complex to \(|K|^G\). No freeness assumption is needed.

**Allowed orbits.** Label an \(S_k\)-orbit of binary words by \((w,z)\), where \(w\) is the Hamming weight of the first \(k\) coordinates and \(z\in\{0,1\}^f\) is the untouched suffix. The largest Hamming distance inside this orbit is exactly \(2\min(w,k-w)\). Since \(k\ge4\), the orbit spans a face at scale three precisely when \(w\in\{0,1,k-1,k\}\). Denote these orbit-vertices, with their suffixes, respectively by \(A_z,U_z,V_z,B_z\).

**Exact compatibility graph.** Put \(\delta=d_H(z,z')\). Taking the largest distance over all pairs of representatives from two distinct orbits yields the following complete list of adjacencies within the same family and between neighboring families:
\[
\begin{array}{c|c}
\text{orbit families}&\text{adjacency condition}\\ \hline
A_zA_{z'},\ B_zB_{z'}&\delta\le3\\
U_zU_{z'},\ V_zV_{z'}&\delta\le1\\
A_zU_{z'},\ B_zV_{z'}&\delta\le2.
\end{array}
\]
There are no \(A\)-to-\(B\) or \(U\)-to-\(V\) edges because representatives can differ in all \(k\) initial coordinates. For \(k\ge5\) there are no other edges because the maximum first-block distance for \(A\)-to-\(V\) or \(U\)-to-\(B\) equals \(k-1\ge4\). For \(k=4\), precisely two further types survive: \(A_zV_z\) and \(U_zB_z\), one edge of each type for every suffix \(z\). These extra edges are maximal simplices: they have no common adjacent third vertex. Because the original Rips complex is flag, pairwise compatibility completely determines the orbit-barycenter complex.

**Reduction of the two principal pieces.** Let \(L_A\) denote the clique complex induced on all \(A_z,U_z\) and \(L_B\) the clique complex induced on all \(B_z,V_z\). In \(L_A\), the closed graph-neighborhood of \(U_z\) is contained in that of \(A_z\): every \(U_z\)-neighbor among \(A_{z'}\) has \(\delta\le2\), hence is adjacent to \(A_z\); every \(U_z\)-neighbor among \(U_{z'}\) has \(\delta\le1\), hence is adjacent to \(A_z\) as well. Thus \(U_z\) is a dominated vertex, and deleting all \(U_z\) successively is a strong simplicial collapse of \(L_A\) onto its \(A\)-induced subcomplex. The latter is exactly \(X_f\), via \(z\mapsto A_z\). Likewise \(L_B\) strongly collapses onto a second copy of \(X_f\) via deletion of all \(V_z\).

**Assembling components and loops.** For \(k\ge5\), the full orbit-barycenter complex is the disjoint union \(L_A\sqcup L_B\), yielding the second case. For \(k=4\), it is obtained from \(L_A\sqcup L_B\) by attaching exactly \(2\cdot 2^f\) distinct one-cells, namely \(A_zV_z\) and \(U_zB_z\), with no higher simplex containing an added edge. Both principal pieces are connected because \(X_f\) is connected for every \(f\ge1\) (the distance-one hypercube graph is contained in its one-skeleton). The standard graph-of-spaces argument takes one connecting edge as a spanning tree and slides all other edge endpoints to chosen basepoints inside the two connected pieces. Hence attaching \(m\) such edges yields the wedge of the two principal pieces with \(m-1\) circles. Taking \(m=2^{f+1}\) gives the first case, completing the proof.

## Verification
The accompanying dependency-free programs `orbit_fixed_checker.py` and `homology_check.py` construct each actual permutation orbit by enumerating all weight-\(w\) supports and then check every orbit-pair distance, without assuming the compatibility table. The first program compares the resulting orbit-vertices and edges against the claimed classifications for \(k=4,5,6,7\) and \(0\le f\le3\), also for \((k,f)=(4,4),(5,4)\), and independently enumerates all cliques to check Euler characteristics and connected components (18 cases). The second reconstructs all simplices and binary boundary matrices and computes reduced/unreduced Betti numbers by exact mod-two elimination for \(k=4,5\), \(0\le f\le3\) (eight cases, including boundary sanity checks). In particular, the tested four-coordinate cases have first Betti numbers \(1,3,7,15\) for \(f=0,1,2,3\), while the five-coordinate cases have two components and no first homology. At \(f=4\), Euler characteristics are \(-32\) and \(0\), respectively. These computations check finite examples; the unrestricted theorem follows from the orbit-distance and dominated-vertex proof above.

## Relationship to prior work
Galetto, Montaño, and Wellner, arXiv:2606.20784, Theorem 6.2, determine characteristic-zero homology representations of the ambient Hamming-cube Rips complexes at scale three. Such a representation theorem does not determine the actual topological fixed-point space of a noncyclic subgroup. Feng, arXiv:2305.07084, Theorem 24, determines the nonequivariant scale-three homotopy type; that result alone likewise does not imply the displayed fixed-space decomposition. Bendersky, Elia, and Grbić, DOI:10.1017/prm.2026.10175, study connectivity and cohomological structure rather than subgroup fixed-point spaces. The previously classified all-coordinate case \(f=0\) is explicitly excluded here. A literature and indexed-statement comparison found no equivalent general fixed-space theorem for untouched coordinates. Failure to find coverage is not itself proof of priority.

## Limitations
The result is a nonequivariant homotopy classification of geometric fixed-point subspaces for the specified \(S_k\)-action; it does not classify their further symmetry actions, arbitrary permutation subgroups, or other scale parameters. PL homeomorphism is asserted only for the canonical fixed-space orbit-barycenter triangulation, not for the final wedge. Mod-two computations are finite checks, not independent proof of the all-parameter classification. Equivalent unindexed or implicit published results remain possible, and no independent mathematical audit has been performed.

## References
1. F. Galetto, J. Montaño and Z. Wellner, *Homology of Vietoris–Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784 (first public 18 June 2026), especially Theorem 6.2. https://arxiv.org/abs/2606.20784
2. Z. Feng, *Homotopy types of Vietoris–Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (first public 11 May 2023), especially Theorem 24. https://arxiv.org/html/2305.07084v1
3. M. Bendersky, S. Elia and J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, published online 22 October 2026, DOI:10.1017/prm.2026.10175. https://doi.org/10.1017/prm.2026.10175
