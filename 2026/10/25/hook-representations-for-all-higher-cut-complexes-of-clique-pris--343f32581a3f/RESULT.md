# Hook representations for all higher cut complexes of clique prisms

## Finding
For all integers \(n\ge k\ge4\), let \(G_n=K_n\mathbin{\square}K_2\) be the Cartesian graph prism, with vertices \([n]\times\{+,-\}\). Let \(\Delta_k(G_n)\) be its **ordinary** \(k\)-cut complex: a face is a subset of vertices whose complement contains \(k\) vertices inducing a disconnected graph. The group \(S_n\times C_2\) acts by simultaneous permutations of the column labels and by exchange of the two layers.

Write \(U_n=\ker(\mathbb Q^n\xrightarrow{\sum}\mathbb Q)\) for the standard rational augmentation representation and \(\epsilon\) for the nontrivial one-dimensional character of the layer-exchange factor. Then the **entire graded rational homology representation** is
\[
\widetilde H_j(\Delta_k(G_n);\mathbb Q)\cong
\begin{cases}
\bigwedge^{k-1} U_n\boxtimes\epsilon^{\,n+1},&j=2n-k-2,\\
0,&j\ne2n-k-2.
\end{cases}
\]
In particular, the nonzero \(S_n\)-constituent is the **single irreducible hook Specht module** \(S^{(n-k+1,1^{k-1})}\), of dimension \(\binom{n-1}{k-1}\). Layer exchange acts by \((-1)^{n+1}\), independent of the cut parameter.

For \(\sigma\in S_n\) with cycle lengths \(\lambda_1,\ldots,\lambda_a\) and \(b\in\{0,1\}\), its complete nonzero-degree character is
\[
\chi(\sigma,\epsilon^b)=(-1)^{(n+1)b}
[t^{k-1}]\,\frac{\prod_{i=1}^{a}(1-(-t)^{\lambda_i})}{1+t}.
\]
Here \([t^{k-1}]\) extracts the indicated coefficient. In particular, the full-group invariant subspace is zero for all \(n\ge k\ge4\), because the hook is nontrivial under \(S_n\).

## Assumptions and scope
The graph product is Cartesian, not categorical; edges join distinct vertices in one layer or the two vertices in one column. The cut complex is ordinary, not total, except that the two notions happen to coincide at cut size two (outside the claimed range). Rational reduced simplicial homology is used, with the usual orientation of ordered simplex vertices. No other graph automorphisms or parameters are implicit. The natural group is \(S_n\times C_2\) for the stated range.

## Proof
**1. Identify the Alexander dual.** Set \(V=[n]\times\{+,-\}\), so \(|V|=2n\). Let \(C=\Delta_k(G_n)^\vee\), the simplicial complex consisting of vertex sets containing **no** disconnected \(k\)-element induced subgraph. A set of vertices with entries in at least \(k\) different columns contains a disconnected induced \(k\)-set precisely when it uses both signs: one may select a vertex from each of \(k\) columns, with at least one selected sign of each kind and with no selected column repeated. This includes the case when both signs are present in the same column, since \(k\ge2\) and another occupied column is available. A set occupying fewer than \(k\) columns contains no such configuration. Thus, if \(B\) denotes the complex of sets supported on at most \(k-1\) columns, and \(A_+\), \(A_-\) the full simplices on the two layers, then
\[
C=B\cup A_+\cup A_-.
\]
The intersections \(K_\pm=B\cap A_\pm\) are the \((k-2)\)-skeleta of the simplices on \(n\) vertices.

**2. Compute the dual's equivariant homology.** Define \(r_+:B\to K_+\) by replacing each negative-layer vertex by its positive-layer partner, leaving positive vertices fixed. This is a simplicial retraction because no face gains an occupied column. The maps \(\mathrm{id}_B\) and \(\iota_+r_+\) are contiguous: the union of a face with its image has the same occupied columns. Hence \(K_+\hookrightarrow B\) is an \(S_n\)-equivariant homotopy equivalence. The analogous statement holds for \(K_-\). Moreover, layer exchange \(\tau:B\to B\) is contiguous to the identity, so it acts trivially on \(\widetilde H_*(B)\).

The simplex attachments \(A_\pm\) have disjoint nonempty geometric realizations outside \(B\), and relative excision gives
\[
H_j(C,B;\mathbb Q)\cong H_j(A_+,K_+;\mathbb Q)\oplus H_j(A_-,K_-;\mathbb Q).
\]
Each relative group is the degree-shifted reduced homology of \(K_\pm\). The only nonzero reduced homology of \(K_\pm\) is in degree \(k-2\), where the augmented simplex chain complex identifies it with \(\bigwedge^{k-1}U_n\) (the kernel of exterior contraction by the all-ones covector). The long exact sequence for \((C,B)\) now identifies \(\widetilde H_{k-1}(C)\) with the kernel of the sum of the two isomorphisms
\[
\widetilde H_{k-2}(K_+)\oplus\widetilde H_{k-2}(K_-)
\longrightarrow\widetilde H_{k-2}(B).
\]
All other reduced homology vanishes. Identifying both summands with the same copy of \(\widetilde H_{k-2}(B)\), the kernel consists of pairs \((a,-a)\). Therefore \(S_n\) acts on it as \(\bigwedge^{k-1}U_n\), while \(\tau\) interchanges the two summands and hence acts by \(-1\). This step is uniform for every \(n\ge k\ge4\).

**3. Equivariant Alexander duality.** Combinatorial Alexander duality gives
\[
\widetilde H_j(\Delta_k(G_n);\mathbb Q)
\cong\det(\mathbb Q[V])\otimes\widetilde H^{2n-j-3}(C;\mathbb Q)
\]
as \(S_n\times C_2\)-modules. The determinant of the induced permutation of \(V\) is trivial on a simultaneous column permutation (it acts twice) and is \((-1)^n\) on layer exchange (it consists of \(n\) transpositions). Thus the dual's \(-1\) layer eigenvalue becomes \((-1)^{n+1}\). The rational standard module is self-dual under its invariant inner product, as are its exterior powers. Since the only nonzero degree of \(C\) is \(k-1\), the only degree of the Alexander dual is \(2n-(k-1)-3=2n-k-2\). This proves the asserted module and homology concentration.

**4. Character and irreducibility.** The degree-\((k-1)\) exterior power of the standard \(S_n\)-module is the hook irreducible \(S^{(n-k+1,1^{k-1})}\). If \(\sigma\) has cycle lengths \(\lambda_i\), the determinant generating function on \(\mathbb Q^n\) is \(\prod_i(1-(-t)^{\lambda_i})\). Dividing by \(1+t\) removes the trivial line. Extracting the coefficient of degree \(k-1\), then multiplying by the layer eigenvalue, gives the character formula. Because \(k-1\ge3\), this hook is nontrivial, hence has no global \(S_n\)-invariants.

## Verification
The accompanying `verify.py` independently builds graph-induced disconnected subsets by adjacency and breadth-first component tests, then checks that this literal definition agrees with the dual-complex criterion for all \(25{,}488\) examined vertex subsets. It computes signed Lefschetz traces directly from simplices for \(212\) conjugacy-class-and-layer-swap tests with \(2\le n\le6\), \(2\le k\le n\), including all small instances of the claimed range. Separate exact mod-two boundary elimination confirms homology ranks and degrees for six cases with \(4\le n\le6\). These tests do not replace the all-parameter proof above.

Run `python verify.py` with Python 3 and its standard library. Successful output contains `PRISM_CUT_EQUIVARIANT_LEFSCHETZ_VERIFIED 212` and `PRISM_CUT_GRAPH_FACE_EQUIVALENCE_VERIFIED 25488`.

## Relationship to prior work
Bayer–Denker–Jelić Milutinović–Rowlands–Sundaram–Xue, *Topology of Cut Complexes of Graphs* (arXiv:2304.13675, Section 7.3, Theorem 7.19) proved the precise nonequivariant wedge-of-\(\binom{n-1}{k-1}\) spheres in degree \(2n-k-2\), using discrete Morse matching; that sphere count and degree are NOT new here. The 2023 source's table and Section 7.3 do not determine the \(S_n\times C_2\)-homology module. Its complete-multipartite equivariant results apply to different graphs, and its cycle-case cyclic characters also have different objects.

The related published classification of ordinary three-cut complexes of rook graphs \(K_m\square K_n\) concerns \(m,n\ge3\) and **cut size three**, not the higher cut parameters \(k\ge4\) and one factor \(K_2\) treated here. The published full coordinate-symmetry classification for total two-cut Hamming complexes is restricted to **cut size two**. *Topology of Cut Complexes II* (arXiv:2407.08158) focuses on disjoint graph unions, squared paths and grids; only its accessible abstract and metadata were checked in this comparison. Thus the present result is the full natural symmetry representation across all higher cut parameters of clique prisms, rather than another nonequivariant sphere count.

## Limitations
The theorem concerns rational homology representations, not an equivariant homotopy equivalence, an integral-lattice identification, or new nonequivariant sphere counts. The case \(k=2\) is outside scope because related stronger representation results cover total two-cut Cartesian products; \(k=3\) is excluded to avoid proximity to published rook-graph three-cut results. Search coverage cannot exclude differently formulated or unindexed antecedents.

## References
1. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675v1, first public 2023-04-26, especially Sections 1, 7.1, 7.3; https://arxiv.org/abs/2304.13675 .
2. M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, L. Xue, *Total Cut Complexes of Graphs*, arXiv:2209.13503v1, first public 2022-09-27; https://arxiv.org/abs/2209.13503 .
3. M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158v1, first public 2024-07-11; https://arxiv.org/abs/2407.08158 .
4. A. Björner, M. Tancer, *Combinatorial Alexander Duality: A Short and Elementary Proof*, arXiv:0710.1172; https://arxiv.org/abs/0710.1172 .
