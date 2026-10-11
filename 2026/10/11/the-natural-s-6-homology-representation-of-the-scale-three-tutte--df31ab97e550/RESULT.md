# The natural \(S_6\)-homology representation of the scale-three Tutte–Coxeter Vietoris–Rips complex

## Finding

Let \(T\) be the 30-vertex Tutte–Coxeter graph and give its vertices the shortest-path metric. The set \(\{1,2,3,4,5,6\}\) acts by permutations on the 15 duads (two-element subsets) and on the 15 synthemes (partitions into three duads), hence on \(T\). Let \(K=\operatorname{VR}_{\le3}(T)\) be the flag complex whose faces have graph-metric diameter at most \(3\). As a rational representation of this natural \(S_6\)-action,

\[
\widetilde H_3(K;\mathbb Q)\cong S^{(3,2,1)}\otimes S^{(3,2,1)}.
\]

Here \(S^\lambda\) is the rational Specht module indexed by the partition \(\lambda\) of \(6\). The full decomposition is

\[
\begin{aligned}
\widetilde H_3(K;\mathbb Q)\cong {}& S^{(6)}\oplus2S^{(5,1)}\oplus3S^{(4,2)}\oplus4S^{(4,1,1)}\oplus2S^{(3,3)}\\
&\oplus5S^{(3,2,1)}\oplus4S^{(3,1,1,1)}\oplus2S^{(2,2,2)}\\
&\oplus3S^{(2,2,1,1)}\oplus2S^{(2,1,1,1,1)}\oplus S^{(1,1,1,1,1,1)}.
\end{aligned}
\]

In particular, the 256-dimensional homology has exactly one fixed line under \(S_6\) and exactly one copy of its sign representation. The statement concerns the natural label-permutation subgroup \(S_6\), not the additional automorphisms possibly interchanging the incidence classes.

## Assumptions and scope

A duad is a two-element subset of a fixed six-element set. A syntheme is a partition of the set into three duads. The graph \(T\) has 15 duads and 15 synthemes as vertices, and a duad is adjacent to a syntheme precisely when contained in it. All constructions use the inclusive distance threshold \(3\); the statement is unchanged for real radii \(3\le r<4\), since graph distances are integral. Homology and representations are over \(\mathbb Q\). The rational coefficient restriction is essential for the semisimple Specht decomposition; no assertion about modular representations is made.

## Proof

**1. The equivariant join.** Distinct duads are distance \(2\) in the incidence graph exactly when they are disjoint, otherwise distance \(4\). Distinct synthemes are distance \(2\) exactly when they share a duad, otherwise distance \(4\). Every duad–syntheme pair has distance \(1\) if incident and \(3\) otherwise. Thus every cross-class edge belongs to the scale-three Rips graph. The entire Rips complex is therefore exactly \(K=A*B\), where \(A\) is the clique complex of the duad disjointness graph and \(B\) the clique complex of the syntheme concurrency graph. This isomorphism is \(S_6\)-equivariant because the natural permutation action preserves the two vertex classes.

**2. Each join factor is equivariantly homotopy equivalent to the incidence graph.** The 15 maximal simplices of \(A\) are triangles indexed by synthemes; different triangles share at most a vertex. Insert an interior barycenter into each filled triangle and join it to its three vertices. The resulting triangulation equivariantly deformation retracts, triangle by triangle, to the union of the 15 three-spoke trees, which is a geometric realization of the duad–syntheme incidence graph \(T\). The construction is natural under label permutations. Dually, the 15 triangles of \(B\) are indexed by duads and an identical equivariant contraction gives \(B\simeq_{S_6}T\). Connectedness of \(T\), and its 30 vertices and 45 edges, give \(\widetilde H_1(T;\mathbb Q)\cong\mathbb Q^{16}\), with no other reduced homology. In particular both factor homologies are concentrated in degree \(1\).

**3. The first-homology character.** Orient every incidence edge from duad to syntheme. In the augmented simplicial chain exact sequence of the connected graph \(T\), the \(S_6\)-representation identity is

\[
[H_1(T;\mathbb Q)]=[\mathbb Q[\mathrm{Flags}]]-[\mathbb Q[\mathrm{Duads}]]-[\mathbb Q[\mathrm{Synthemes}]]+[\mathbf 1].
\]

Consequently, for a label permutation \(g\),

\[
\chi_{H_1}(g)=\#\mathrm{Flags}^{g}-\#\mathrm{Duads}^{g}-\#\mathrm{Synthemes}^{g}+1.
\]

Enumerating the 11 conjugacy classes, the character has the following nonzero values: identity \(16\), class \((3,3)\) value \(-2\), class \((5,1)\) value \(1\), and class \((3,1,1,1)\) value \(-2\); every other cycle type has value \(0\). Its character norm equals \(1\) and it agrees on all classes with the Frobenius character formula for the Specht module \(S^{(3,2,1)}\). Therefore

\[
H_1(A;\mathbb Q)\cong H_1(B;\mathbb Q)\cong S^{(3,2,1)}
\]

as \(S_6\)-modules. The module identification is not an assertion of canonical equivalence between the two factors; it is an equality of their irreducible isomorphism types.

**4. Join Künneth and complete decomposition.** The natural reduced chain equivalence of joins gives an \(S_6\)-equivariant isomorphism \(\widetilde H_3(A*B;\mathbb Q)\cong\widetilde H_1(A;\mathbb Q)\otimes\widetilde H_1(B;\mathbb Q)\), because the label permutations preserve the ordering of the two factors and hence introduce no factor-swap sign. This proves the tensor-square claim and vanishing of all other reduced rational homology. Multiplying the class character values gives \(\chi_{H_3}(g)=\chi_{(3,2,1)}(g)^2\). Taking inner products with all eleven \(S_6\)-irreducible rational characters produces the multiplicities in the Finding, whose dimension-weighted sum is \(256\). The inner product with the trivial character is \(1\); the inner product with sign is likewise \(1\).

## Verification

Run `python3 verify.py` using Python \(3\). The standalone program regenerates duads, synthemes, incidence flags, both triangle complexes, and the 720 group actions, computing both signed simplicial Euler traces and the incidence fixed-flag character independently for every permutation. It then computes all eleven Specht character tables from the Frobenius alternant formula, checks the exact inner products and the dimension sum, and prints `VERIFY_EQUIV_OK`. A second standalone program `verify_rips.py` independently enumerates the scale-two and scale-three flag complexes, checks the full scale-three join face vector and mod-two boundary ranks, and prints `VERIFY_OK`. These finite checks are exhaustive for the named 30-vertex graph, not a claim about all generalized quadrangles or about integral representation structure.

## Relationship to prior work

Adamaszek's clique-complex results concern graph-power complexes and give useful general context, but do not identify this natural \(S_6\)-representation. Adams, Frick, and Virk treat homotopy groups of Vietoris simplicial complexes versus metric thickenings, not the label-symmetry action in the finite incidence example. Earlier nonequivariant calculations give the homotopy type \(K\simeq\bigvee^{256}S^3\) of this very complex; that homotopy-type statement and the underlying 16-dimensional Betti number are not new. Also, the abstract decomposition of the Kronecker square of \(S^{(3,2,1)}\) is accessible within symmetric-group representation theory, and the multiplicities are not claimed to be algebraically new independently of the geometric identification. The contribution here is the identification of the geometric Rips homology action as that tensor square and the resulting complete equivariant classification for this canonical graph.

## Limitations

Only the natural label-permutation \(S_6\) action on rational homology is determined. No representation under a larger graph automorphism group and no integral-lattice or mod-prime decomposition is asserted. Equivalent equivariant calculations in unindexed literature remain a residual originality risk. The cited 2022 source establishes general Rips/topological context rather than implying the finite-equivariant computation.

## References

- Henry Adams, Florian Frick, Žiga Virk, *Vietoris thickenings and complexes have isomorphic homotopy groups*, arXiv:2206.08812v1 (first public June 17, 2022), primary MSC 55N31; Journal of Applied and Computational Topology 7 (2023), 221–241.
- Michał Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433 (2011), Israel Journal of Mathematics 196 (2013), 295–319.
- Kenneth McCabe, *Lower Bounds for Approximating the Vietoris-Rips Filtration*, arXiv:2607.06524 (2026), for modern graph-metric incidence-complex context; no equivariant theorem from this work is assumed.
