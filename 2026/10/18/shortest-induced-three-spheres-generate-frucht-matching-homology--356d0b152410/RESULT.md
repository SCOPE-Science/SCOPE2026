# Shortest induced three-spheres generate Frucht matching homology integrally

## Finding

Let \(F\) be the twelve-vertex, eighteen-edge Frucht graph, with its edge labeling specified below. Let \(K=\mathcal M(F)\) be its **ordinary matching complex**: vertices of \(K\) are edges of \(F\), and a simplex is any set of pairwise vertex-disjoint graph edges. For \(W\subseteq E(F)\), let \(K[W]\) be the full subcomplex on the indicated matching-complex vertices.

The exact integral homology of \(K\) is
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{20},\qquad
\widetilde H_j(K;\mathbb Z)=0\quad(j\ne3).
\]

The **minimum** cardinality of an edge set \(W\) for which the inclusion \(K[W]\hookrightarrow K\) carries a nonzero class in \(\widetilde H_3(-;\mathbb Z)\) is eight. Exactly **87** such eight-edge sets exist. Each gives a subcomplex combinatorially isomorphic to the boundary of a four-dimensional cross-polytope:
\[
K[W]\cong (S^0)^{*4}\cong S^3.
\]

Every one of their fundamental classes maps to a **primitive nonzero** element of \(\widetilde H_3(K;\mathbb Z)\). The 87 classes generate this entire integral group; moreover, the lexicographically indexed carriers numbered
\[
0,1,2,3,4,5,7,8,9,12,18,19,21,22,28,29,30,32,33,43
\]
form one integral basis. Indexing is specified by the standalone verifier and starts at zero. There is no claim that every choice of twenty carriers is a basis.

## Assumptions and scope

All homology is unreduced in degree zero and reduced otherwise, with integral coefficients unless explicitly indicated. The graph is finite, undirected, simple, and has labeled vertex set \(\{0,\ldots,11\}\). Its lexicographically ordered edge list is
\[
\begin{gathered}
(0,1),(0,6),(0,7),(1,2),(1,7),(2,3),(2,8),(3,4),(3,9),\\
(4,5),(4,9),(5,6),(5,10),(6,10),(7,11),(8,9),(8,11),(10,11).
\end{gathered}
\]
This is the standard NetworkX labeling of the Frucht graph, which is a canonical smallest asymmetric cubic graph. The simplex orientation is increasing order of the above edge indices. All 87 counted subcomplexes are induced on exactly eight vertices of the **matching complex**, not eight graph vertices. Their associated graph edges together span all twelve graph vertices.

## Proof

**1. Sharp flag-support lemma.** If a finite flag complex has nonzero reduced homology in degree \(d\ge0\), then it has at least \(2d+2\) vertices. If equality holds, it is the boundary of a \((d+1)\)-dimensional cross-polytope. For the first assertion, take a vertex-minimal induced subcomplex \(L\) with nonzero \(\widetilde H_d\). For any vertex \(v\), the deletion \(L-v\) has vanishing \(\widetilde H_d\). The union of \(L-v\) with the (contractible) closed star of \(v\), whose intersection is \(\operatorname{lk}_L(v)\), gives nonzero \(\widetilde H_{d-1}(\operatorname{lk}_L(v))\). Induction from the disconnected two-vertex case therefore forces at least \(2d\) neighbors of \(v\). Since flagness makes a universal vertex a cone point, \(v\) also has a nonneighbor; hence \(|V(L)|\ge2d+2\). If equality holds, every vertex has exactly one nonneighbor; the missing edges form a perfect matching, and flagness identifies the cross-polytope boundary. The same conclusion applies if the ambient flag complex has exactly \(2d+2\) vertices. As \(K\) is flag, \(d=3\) gives a sharp lower bound of eight.

**2. Enumerating all equality carriers.** An induced eight-vertex octahedral three-sphere in \(K\) corresponds to four pairs of incident edges of \(F\), with no graph vertex common to different pairs: equivalently, a spanning decomposition into four disjoint two-edge paths \(P_3\). The graph has exactly 36 unordered incident-edge pairs, three centered at each of its twelve vertices. Testing all lexicographic four-tuples of these 36 pairs with disjoint graph-vertex supports, and identifying eight-edge sets, gives exactly 87. All are induced \((S^0)^{*4}\). The flag-support lemma proves there are no other eight-edge subcomplexes with nonzero third homology. This count is verified by exhaustive deterministic enumeration, not a sampling procedure.

**3. Exact chain ranks and integral torsion.** Enumerating all nonempty matchings gives the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,333,397,152,8).
\]
For signed simplicial boundaries \(\partial_i:C_i(K;\mathbb Z)\to C_{i-1}(K;\mathbb Z)\), the integer column ranks for \(i=1,\ldots,5\) are
\[
(17,100,233,144,8).
\]
A complete integer elimination realizes **each** boundary image by independent columns whose pivots are all \(\pm1\), with every other boundary column an integral combination of these. The ordered-pivot triangular minors are unimodular; thus these boundary images are primitive sublattices. Rank-nullity gives \(397-233-144=20\) in degree three, zero other reduced ranks, and no integral torsion. The accompanying verifier recomputes every oriented simplex, every signed boundary, every chain-complex identity, and every stated unit pivot.

**4. Primitive fundamental cycles.** For one carrier, order the four incident-edge pairs \((a_i,b_i)\) by the lexicographic rule in the verifier. The oriented fundamental three-cycle is the simplicial join of the four zero-cycles \([a_i]-[b_i]\). It has exactly sixteen \(\pm1\) tetrahedra; the verifier checks \(\partial_3z=0\) for every one of the 87 cycles. Reduce these cycles integrally modulo \(\operatorname{im}\partial_4\), using the explicit all-unit boundary basis. All 87 resulting coordinate vectors are nonzero and have coefficient gcd one. Their classes are therefore primitive in the free quotient \(C_3/\operatorname{im}\partial_4\), hence also primitive in \(H_3(K;\mathbb Z)\).

**5. Integral generation.** The 87 reduced cycles admit an exact integer column elimination with **twenty** additional unit pivots. The twenty carriers listed above are the chosen independent unit-pivot columns, so their span is a primitive rank-twenty sublattice \(L\) of \(C_3/\operatorname{im}\partial_4\). Since they are cycles, \(L\subseteq H_3(K;\mathbb Z)\). The latter is a primitive rank-twenty sublattice of this quotient, because the quotient by the kernel of the induced boundary embeds in the free group \(C_2\). Two nested primitive lattices of equal finite rank are equal. Thus \(L=H_3(K;\mathbb Z)\), proving all integral claims.

## Verification

The embedded standalone `verify_frucht.py` is executable using Python 3 standard-library modules only. It constructs all \(1025\) nonempty simplices and verifies exact integer identities and the 87-carrier enumeration. Its final line begins `VERIFY_OK_FRUCHT_MATCHING_COMPLEX` and it outputs the selected twenty carrier descriptions. Independent `verify_modular.py` reconstructs the boundary matrices separately and checks their ranks and the augmented sphere-cycle rank modulo \(2,3,5,101\). Modular calculations corroborate but are **not** the basis for the integral conclusion.

Reproduce with `python3 verify_frucht.py` and `python3 verify_modular.py`. Neither requires downloaded data or nonstandard libraries.

## Relationship to prior work

Björner–Lovász–Vrećica–Živaljević introduced foundational connectivity results for chessboard and matching complexes, chiefly for complete underlying graphs. Jonsson developed discrete-Morse methods for finite simplicial complexes. Bayer–Goeckner–Jelić Milutinović classify when an **entire** matching complex is a homology manifold, including the standard octahedral matching complexes of disjoint unions of \(P_3\) paths. The induced sphere shape itself is not new. Their classification does not determine the Frucht matching-complex integral homology, the number of its spanning four-path carriers, the induced inclusion classes, or their integral generation. Engström's claw-free independence-complex connectivity results likewise do not determine this exact lattice.

The distinct independence complex \(\operatorname{Ind}(F)\) of the same graph has been studied previously; it is not the eighteen-vertex matching complex \(\mathcal M(F)=\operatorname{Ind}(L(F))\) considered here. No claimed distinction relies solely on different terminology.

## Limitations

Only this exact twelve-vertex graph, its ordinary matching complex, and integral homology of specified induced inclusions are settled. No homotopy equivalence to a wedge of spheres, no classification of other cubic graphs, no homological statement about all flag complexes, and no unconditional publication-priority claim are made. Exact computations certify this finite theorem; they do not prove extensions beyond the stated graph. The standalone codes provide machine-checkable finite calculations, not an independent scientific audit.

## References

1. A. Björner, L. Lovász, S. T. Vrećica and R. T. Živaljević, *Chessboard Complexes and Matching Complexes*, J. London Math. Soc. 49 (1994), 25–39, https://doi.org/10.1112/jlms/49.1.25 (publisher online date 1994-02-01).
2. J. Jonsson, *Optimal Decision Trees on Simplicial Complexes*, Electron. J. Combin. 12 (2005), R3, https://doi.org/10.37236/1900 (published 2005-01-07).
3. M. Bayer, B. Goeckner and M. Jelić Milutinović, *Manifold Matching Complexes*, arXiv:1906.03328 (2019), https://arxiv.org/abs/1906.03328; in particular the definition, disjoint-union sphere examples, and Theorem 4.3.
4. A. Engström, *Independence Complexes of Claw-Free Graphs*, Eur. J. Combin. 29 (2008), 234–241, https://doi.org/10.1016/j.ejc.2006.09.007.
5. NetworkX, `frucht_graph` graph data and labeling, https://networkx.org/documentation/stable/reference/generated/networkx.generators.small.frucht_graph.html.
