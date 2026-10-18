# The full hyperoctahedral homology representation of the four-cube independence complex

## Finding

Write \(Q_4\) for the graph on \(V=(\mathbb F_2)^4\) with edges between words differing in exactly one coordinate, and set \(K=\operatorname{Ind}(Q_4)\). Its full graph automorphism group is \(G=T\rtimes S_4\), where \(T=(\mathbb F_2)^4\) acts by translations and \(S_4\) permutes coordinates. Every automorphism is uniquely \(g=(t,p)\), acting by \(v\mapsto t+p(v)\), and \(|G|=384\).

Let \(\psi_u(t)=(-1)^{u\cdot t}\) for \(u,t\in T\), with dot product over \(\mathbb F_2\); let \(\mathrm{Std}_3\) denote the rational three-dimensional standard representation of \(S_4\). Fix \(u_0=(1,1,1,0)\). Its stabilizer in \(S_4\) is the \(S_3\) permuting its three nonzero coordinates. Then, as rational representations,

\[
\boxed{\widetilde H_3(K;\mathbb Q)\cong
\operatorname{Inf}_{S_4}^{G}(\operatorname{sgn}_{S_4}\otimes\mathrm{Std}_3)
\ \oplus\
\operatorname{Ind}_{T\rtimes S_3}^{G}(\psi_{u_0}\otimes\operatorname{sgn}_{S_3}).}
\]

Both summands are absolutely irreducible, pairwise nonisomorphic, and have dimensions three and four. All other reduced rational homology groups vanish. For every \(t\in T\) and \(p\in S_4\), the complete character is

\[
\boxed{\chi(t,p)=\operatorname{sgn}(p)(\#\operatorname{Fix}_{[4]}(p)-1)
+\sum_{\substack{|u|=3\\p(u)=u}}
\operatorname{sgn}(p|_{\operatorname{supp}(u)})\,(-1)^{u\cdot t}.}
\]

Here \(|u|\) is Hamming weight; each summand in the second term comes from a fixed three-coordinate support. Under translations alone the character multiplicities are three copies of the trivial character and one copy of each of the four weight-three characters, with every other character absent. In particular,

\[
\dim\widetilde H_3(K;\mathbb Q)^T=3,
\qquad \dim\widetilde H_3(K;\mathbb Q)^G=0.
\]

## Assumptions and scope

The independence complex has as its simplices all subsets of \(V\) with no edge of \(Q_4\). All homology is reduced simplicial homology, and all representations concern the natural action induced by simplicial automorphisms, not an arbitrary action on a wedge of spheres. A translation character \(\psi_u\) acts on a one-dimensional line by \(t\mapsto(-1)^{u\cdot t}\). The sign on a restricted permutation \(p|_{\operatorname{supp}(u)}\) is defined only when the support is stabilized by \(p\), as required by the summation condition. The result is for this four-dimensional hypercube; no extension to other dimensions or integral equivariant lattice classification is asserted.

## Proof

**(1) The graph symmetry group.** Every translation and coordinate permutation preserves Hamming-one adjacency, yielding \(T\rtimes S_4\) of order \(16\cdot24\). Conversely, any graph automorphism is determined by the image of the zero word and the permutation it induces on its four neighbors. After fixing these, vertices at distance two are forced as the alternative common neighbors of two distinct unit words, and vertices at larger distance are forced inductively by their neighbors in the preceding Hamming layer. Thus there are no additional graph automorphisms.

**(2) Concentration of homology.** Enumerate all \(2^{16}\) subsets of the sixteen vertices, retaining exactly those containing no Hamming-one pair. The numbers of nonempty independent sets of cardinalities one through eight are \((16,88,208,228,128,56,16,2)\); no larger independent set exists. On the \(742\) nonempty faces, at pivot \(v=0,1,\ldots,15\) pair each still-unmatched face not containing \(v\) with the still-unmatched face obtained by adjoining \(v\), when that face is allowed. The sixteen pair counts are

\[
(176,134,10,4,5,5,13,4,0,3,4,3,3,1,1,1).
\]

These \(367\) pairs leave exactly one zero-dimensional and seven three-dimensional critical cells. Direct every cover relation of the nonempty-face poset downwards and reverse the \(367\) matched relations. There are \(2816\) directed cover relations. The supplied standalone checker reconstructs every relation and verifies that a topological sorting algorithm visits all \(742\) faces. This gives an exact, finite certificate of acyclicity. By the discrete-Morse theorem the complex is homotopy equivalent to a CW complex with one zero-cell and seven three-cells, hence to a wedge of seven three-spheres. In particular its only reduced rational homology is seven-dimensional in degree three. This nonequivariant conclusion is also established by the same-object result cited below; it is used here to localize the Lefschetz traces, not claimed as the new contribution.

**(3) Equivariant Lefschetz trace.** For any \(g=(t,p)\), let \(\mathcal O(g)\) be its permutation orbits on the sixteen vertices. Discard an orbit if it contains an edge of \(Q_4\). Make a conflict graph \(C_g\) on the remaining orbits, joining two orbit-vertices if any graph edge connects their member vertices. A simplex fixed setwise by \(g\) is exactly a union of pairwise compatible orbit-vertices, hence corresponds to an independent set of \(C_g\). For a fixed nonempty simplex containing \(k\) selected orbits and \(m\) original vertices, its oriented simplicial action has sign \((-1)^{m-k}\). Its reduced chain-Lefschetz contribution is therefore \((-1)^{m-1}(-1)^{m-k}=(-1)^{k-1}\); the empty simplex contributes \(-1\). Thus the reduced Lefschetz number is \(-I(C_g;-1)\), where \(I\) denotes the independence polynomial, while concentration in degree three makes it \(-\chi(g)\). Consequently

\[
\chi(g)=I(C_g;-1).
\]

The verifier evaluates this polynomial by vertex deletion and closed-neighborhood deletion on all \(384\) group elements; independently it sums signed setwise-fixed oriented simplices on all \(742\) faces. The two exhaustive procedures agree. The character takes the values \(7,5,3,1,-1,-3\) on respectively \(1,4,6,188,161,24\) automorphisms. In particular translations of weights \(0,1,2,3,4\) have traces \(7,1,3,5,-1\).

**(4) Fourier and stabilizer determination.** For every \(u\in T\) the multiplicity of \(\psi_u\) in the restricted homology representation is exactly

\[
 m_u=\frac1{16}\sum_{t\in T}(-1)^{u\cdot t}\chi(t,\mathrm{id}).
\]

The preceding exact traces give \(m_0=3\), \(m_u=1\) when \(|u|=3\), and \(m_u=0\) otherwise. The three-dimensional translation-fixed subspace carries, on the five cycle types \((1^4),(2,1,1),(2,2),(3,1),(4)\), the \(S_4\)-character \((3,-1,-1,0,1)\). To calculate this, average \(\chi(t,p)\) over \(t\); it equals \(\operatorname{sgn}(p)(\#\operatorname{Fix}(p)-1)\), proving the first summand.

The other four one-dimensional \(T\)-eigenspaces are indexed by the four weight-three \(u\). The stabilizer \(S_3\) of \(u_0\) acts on its eigenspace by its sign character: the Fourier-projected trace

\[
\frac1{16}\sum_{t\in T}(-1)^{u_0\cdot t}\chi(t,p)
\]

is \(-1\) for any transposition inside its three-coordinate support and \(+1\) for a three-cycle. Since coordinate permutations transitively permute these four eigenspaces, their sum is exactly the displayed induced module. The sign-twisted standard \(S_4\)-module is absolutely irreducible, and the induced module is absolutely irreducible because it has four distinct one-dimensional \(T\)-character spaces permuted transitively by \(S_4\). They are nonisomorphic because \(T\) acts trivially on one and nontrivially on the other. Their characters add to the boxed formula. Neither summand contains a \(G\)-fixed vector.

## Verification

Run `python3 verify_q4_character.py` using Python 3 standard library only. The checker reconstructs the graph, enumerates all possible faces, rebuilds the pivot matching, verifies matching-acyclicity on the complete incidence digraph, enumerates all \(384\) automorphisms, compares two independent Lefschetz evaluations on each, checks all predicted character values and Fourier projections, and establishes zero full-group average. Its expected final line is `VERIFY_OK vertices=16 faces=742 matching_pairs=367 critical=1x0+7x3 acyclic_incidences=2816 group=384 rank_H3=7 translation=3+4 all_character_checks=384 globally_fixed=0`. Every finite universe exhaustively checked is explicitly bounded; no unverified extrapolation to arbitrary cube dimension is used.

## Relationship to prior work

Bousquet-Mélou, Linusson and Nevo [1] established discrete-Morse methods for grid independence complexes and evaluated alternating independent-set counts, but their homotopy classifications cover open and cylindrical rather than the four-by-four toroidal case; they give no full automorphism-homology character. Barmak [2] proved suspension homotopy for independence complexes of triangle-free graphs, which applies to \(Q_4\) but neither specifies this module nor its character. The more recent same-object homotopy computation [3] establishes \(\operatorname{Ind}(Q_4)\simeq\bigvee^7 S^3\), with exact matching data, and explicitly leaves equivariant decomposition outside its claim. Full hyperoctahedral characters for the four-cube's *three-cut* and *Čech* complexes [4,5] concern different simplicial complexes, with different defining faces and homology degrees; their representations do not imply the character here. The contribution here is the full natural \(T\rtimes S_4\)-module structure, specifically the three-plus-four irreducible decomposition and the weight-three translation spectrum.

## Limitations

This is an exact rational-equivariant classification for a single natural finite graph, not an integral representation-lattice classification or an infinite-dimensional family theorem. Although exhaustive algebra and two independent Lefschetz implementations establish the finite calculation, they are not independent external scientific validation. The conclusion is original relative to inspected and indexed sources; an unindexed equivalent representation computation cannot be excluded. The nonequivariant sphere-wedge homotopy is already known and not claimed to be new.

## References

[1] M. Bousquet-Mélou, S. Linusson and E. Nevo, *On the independence complex of square grids*, arXiv:math/0701890, first public version 2007-01-30. https://arxiv.org/abs/math/0701890

[2] J. A. Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418, first public version 2010-07-02. https://arxiv.org/abs/1007.0418

[3] *The four-cube independence complex is a wedge of seven three-spheres*, scientific record, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-four-cube-independence-complex-is-a-wedge-of-seven-three-sph--9947aaad144c/RESULT.md

[4] *The total three-cut complex of the four-cube: a 129-sphere wedge and its hyperoctahedral character*, scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-total-3-cut-complex-of-the-4-cube-a-129-sphere-wedge-and-its--ccb644c2e2a2

[5] *The hyperoctahedral homology character of the four-cube Čech nerve at scale three*, scientific record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-hyperoctahedral-homology-character-of-the-four-cube-ech-nerv--89c403fdb3a1
