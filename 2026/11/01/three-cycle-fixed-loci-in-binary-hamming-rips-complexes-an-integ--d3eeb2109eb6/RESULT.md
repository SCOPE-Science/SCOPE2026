# Three-cycle fixed loci in binary Hamming Rips complexes: an integral mixed-sphere splitting

## Finding

For every integer \(m\ge 1\), let \(Q_{m+3}=\{0,1\}^{m+3}\) have Hamming distance, and let
\(X_m=\operatorname{VR}_{\le 2}(Q_{m+3})\) be the inclusive Vietoris–Rips complex.
The cyclic permutation \(\rho=(1\,2\,3)\) acts on the first three coordinates, leaving the other \(m\) coordinates fixed. Put \(F_m=|X_m|^{\langle\rho\rangle}\) and \(K_m=\operatorname{VR}_{\le 2}(\{0,1\}^m)\). Then

\[
F_m=|X_m|^{\mathfrak S_3}\simeq K_m\vee K_m\vee\bigvee^{2^{m+1}-1}S^1.
\]

The equality is an equality of actual geometric fixed-point subsets; indeed the \(\langle\rho\rangle\)-fixed and \(\mathfrak S_3\)-fixed subsets coincide at **every** Vietoris–Rips scale. The homotopy splitting above concerns the radius-two stage.

For \(m\le2\), \(K_m\) is contractible. For \(m\ge3\), the established hypercube theorem gives \(K_m\simeq\bigvee^{c_m}S^3\), where

\[
c_m=\sum_{0\le j<i<m}(j+1)\bigl(2^{m-2}-2^{i-1}\bigr).
\]

Consequently, all reduced integral homology of \(F_m\) is free, with \(\widetilde H_1(F_m;\mathbb Z)\cong\mathbb Z^{2^{m+1}-1}\), and with \(\widetilde H_3(F_m;\mathbb Z)\cong\mathbb Z^{2c_m}\) when \(m\ge3\); all other reduced integral groups vanish. In particular, \(\pi_1(F_m)\) is the free group on \(2^{m+1}-1\) generators, although the ambient \(X_m\) is simply connected.

Let \(B_m=(\mathbb Z/2)^m\rtimes\mathfrak S_m\) act on the untouched coordinates. The complete integral \(B_m\)-module on first homology is the augmentation lattice

\[
H_1(F_m;\mathbb Z)\ \cong\ \ker\!\left(\mathbb Z^{\{0,1\}^m\times\{1,2\}}\xrightarrow{\,\sum\,}\mathbb Z\right),
\]

where \(B_m\) permutes the background words and preserves the two labels. Complementation of the first three coordinates interchanges the labels and acts on this kernel by **minus** that permutation. No explicit decomposition of the integral third-homology module is asserted.

## Assumptions and scope

The binary alphabet, inclusive Hamming threshold two, and coordinate action are essential. The integer \(m\) is at least one, so both copies of \(K_m\) are connected. Geometric fixed points mean the fixed subset of the realization of the full clique complex, not the realization of its subcomplex of pointwise fixed vertices. The stated integral homotopy and module results hold uniformly for every such \(m\).

## Proof

**1. Orbit-barycenter model.** A point in a simplex of a complex with a vertex-permutation action is fixed exactly when its barycentric coefficients are constant on each group orbit. Hence the geometric fixed set is triangulated by barycenters of admissible vertex-orbits: an orbit is admissible if its complete vertex set forms a face. A collection of admissible orbits spans a face precisely when their union spans a face. Since \(X_m\) is a flag complex, this is equivalent to pairwise cross-distances at most two.

Write a binary vertex as \((u,z)\), where \(u\in\{0,1\}^3\) is the moving block and \(z\in\{0,1\}^m\). The four cyclic orbit types of \(u\) are \(A=\{000\}\), \(B=\{111\}\), \(C=\{100,010,001\}\), and \(D=\{110,101,011\}\). Each is an internal clique at threshold two. The transposition of two moving coordinates preserves each of these four orbits, so cyclic and full symmetric-group vertex orbits coincide. This proves equality of geometric fixed sets for all scales.

**2. Exact orbit adjacency.** Label orbit vertices \(A_z,B_z,C_z,D_z\) by their common untouched word \(z\). If \(b=d_H(z,y)\), the maximum cross-distance of two orbit types is the maximum of their three-bit cross-distances plus \(b\). Direct inspection of the four listed three-bit sets gives all permitted edges at scale two:

- \(A_zA_y\) and \(B_zB_y\) when \(1\le b\le2\);
- \(A_zC_y\) and \(B_zD_y\) when \(b\le1\);
- \(A_zD_y\) and \(B_zC_y\) when \(b=0\).

There are no other edges, including no edges between distinct \(C\)-vertices, between distinct \(D\)-vertices, between any \(C\) and \(D\), or between any \(A\) and \(B\). The full \(A\)- and \(B\)-vertex subcomplexes are therefore disjoint copies \(K_m^A,K_m^B\) of \(K_m\).

For each fixed \(z\), the link of \(C_z\) consists of the entire simplex on \(\{A_y:d_H(y,z)\le1\}\), disjoint from the isolated link vertex \(B_z\). This is indeed a simplex: any two binary words at distance at most one from \(z\) differ in at most two coordinates. Similarly the link of \(D_z\) is the simplex on \(\{B_y:d_H(y,z)\le1\}\), disjoint from the link vertex \(A_z\). No simplex contains two distinct peripheral vertices of types \(C\) or \(D\).

**3. Explicit relative elementary collapses.** For each \(z\), put \(N(z)=\{y:d_H(y,z)=1\}\). In descending order of \(|S|\), for every nonempty \(S\subseteq N(z)\), pair the face \(\{C_z\}\cup\{A_y:y\in S\}\) with the face obtained by adjoining \(A_z\). All these lower faces are free when removed in that order because larger neighbor subsets have already been removed, and no other peripheral type belongs to a containing simplex. Apply the analogous pairs with \(D_z\), \(B_y\), and \(B_z\). Pairs for different \(z\) do not interfere, as no simplex contains two peripheral vertices. This is an explicit sequence of elementary simplicial collapses for every \(m\).

The residual complex \(R_m\) consists precisely of \(K_m^A\sqcup K_m^B\) and, for each \(z\in\{0,1\}^m\), the two internally disjoint paths

\[
A_z-C_z-B_z,\qquad A_z-D_z-B_z.
\]

There are exactly \(2^{m+1}\) such paths. Both core complexes are connected, hence attaching \(k\) disjoint paths between two connected spaces produces their wedge together with \(k-1\) circles. Setting \(k=2^{m+1}\) yields the asserted homotopy equivalence.

**4. Integral homology and symmetry.** The Adamaszek–Adams theorem supplies \(K_m\simeq *\) for \(m=1,2\) and \(K_m\simeq\bigvee^{c_m}S^3\) for \(m\ge3\). Applying it to the two core summands proves the free integral homology groups. The edge paths have a canonical orientation from the \(A\)-core to the \(B\)-core. In the relative homology sequence of \((R_m,K_m^A\sqcup K_m^B)\), the \(2^{m+1}\) path classes form a free relative first-chain module, and its boundary sends each path to the difference of the two component generators. The two core spaces have vanishing first homology. Thus ordinary \(H_1(R_m;\mathbb Z)\) is exactly the kernel of the summation map. The untouched-coordinate symmetry group permutes these paths by \(z\), preserving their orientation. Complementation of the moving block exchanges the two cores and the two path types, reversing orientation. This proves the claimed integral module action.

## Verification

The accompanying `verify.py` independently reconstructs the cyclic orbits from the original binary vertex set and Hamming metric. It compares every orbit-pair edge with the above exhaustive rule, verifies that coordinate transpositions preserve each cyclic orbit, and constructs every simplex of the resulting flag complex for \(m=0,1,2,3,4\). It then executes the precise elementary free-face removals, checks the remaining faces against the two-core-plus-path model, and computes the mod-two reduced Betti numbers directly from boundary matrices. The verified Betti vectors for \(m=1,2,3,4\) have nonzero ranks \((\beta_1,\beta_3)=(3,0),(7,0),(15,2),(31,18)\). The \(m=0\) run is a separate boundary sanity check, not part of the new parameter range. All checks returned `VERIFY_OK`.

The finite checker does not prove the theorem for arbitrary \(m\); the unlimited orbit classification and elementary-collapse construction above do. The quoted three-sphere multiplicity relies on the previously published hypercube homotopy theorem.

## Relationship to prior work

Adamaszek and Adams determine the ordinary homotopy type of \(\operatorname{VR}_{\le2}(Q_m)\), which supplies the two core summands but not the geometric three-cycle fixed-space decomposition. Galetto, Montaño, and Wellner study the full hyperoctahedral action on rational ambient homology; a rational character does not determine the homotopy type or free fundamental group of a subgroup's geometric fixed space. Bendersky, Elia, and Grbić study ambient connectivity, coconnectivity, and cohomology constructions rather than the present fixed locus. Earlier coordinate-cycle fixed-space calculations for moving blocks of length at least four do not cover the three-coordinate boundary: at this boundary the fixed space becomes connected and acquires exponentially growing first homology. The coincidence of cyclic and full symmetric fixed sets is specific to three binary moving coordinates.

## Limitations

The result classifies the radius-two geometric fixed space for a three-coordinate cycle over the binary alphabet. It does not classify all higher-radius fixed spaces or integral third-homology symmetry modules. The published rational-action preprint of Galetto, Montaño, and Wellner was accessible through its abstract and bibliographic record, but its complete text could not be inspected during the literature comparison. An equivalent unpublished or unindexed result cannot be ruled out. Independent mathematical validation has not been performed.

## References

1. M. Adamaszek and H. Adams, *On Vietoris–Rips complexes of hypercube graphs*, arXiv:2103.01040v1 (first public 2021-03-01), Theorem 1. Published in *Journal of Applied and Computational Topology* 6 (2022), 177–192.
2. F. Galetto, J. Montaño, and Z. Wellner, *Homology of Vietoris-Rips complexes of hypercube graphs via group actions*, arXiv:2606.20784v1 (first public 2026-06-18).
3. M. Bendersky, S. Elia, and J. Grbić, *Cohomological properties of the Vietoris–Rips complex of a hypercube graph*, arXiv:2605.00705v1 (first public 2026-05-01), and *Proceedings of the Royal Society of Edinburgh Section A* (published online 2026-10-22), doi:10.1017/prm.2026.10175.
4. H. Adams and Ž. Virk, *Lower bounds on the homology of Vietoris–Rips complexes of hypercube graphs*, arXiv:2309.06222v1 (first public 2023-09-12), especially Theorem 2.4 and the discussion of radius two.
