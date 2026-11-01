# Proper-subgroup fixed-point collapses and four regular modules in a tetrahedral Morse-complex pair

## Finding
Let \(F=\mathcal M(\Delta^3)\) and \(B=\mathcal M(\partial\Delta^3)\) be the **ordinary** simplicial complexes of acyclic discrete-Morse matchings of the full tetrahedron and its boundary, respectively. The natural inclusion \(B\hookrightarrow F\) is equivariant for vertex relabeling by \(S_4\). Then:

1. For **every nontrivial subgroup** \(H\le S_4\), the canonical orbit-barycenter triangulation of \(|F|^H\) collapses by elementary simplicial collapses onto the embedded orbit-barycenter triangulation of \(|B|^H\). Hence \(|B|^H\hookrightarrow |F|^H\) is a simple-homotopy equivalence, including in empty cases.
2. The integral relative homology vanishes except in degree four, where
\[
H_q(F,B;\mathbb Z)\cong\begin{cases}\mathbb Z^{96},&q=4,\\0,&q\ne4.\end{cases}
\]
The complete rational tetrahedral action on this relative group is
\[
\boxed{H_4(F,B;\mathbb Q)\cong\mathbb Q[S_4]^{\oplus4}.}
\]

The new assertion is the **relative equivariant structure and the simultaneous geometric fixed-point collapses**. The rank \(96\) of the relative group itself was already calculated in the motivating paper; it is included to specify the context and complete the proof.

## Assumptions and scope
The abstract tetrahedron has vertex set \(\{0,1,2,3\}\). Represent a nonempty face by its nonzero four-bit characteristic mask. A Hasse-edge vertex of a Morse complex is a pair \((a,b)\) of faces with \(a\subset b\) and \(|b|=|a|+1\). A simplex is a set of such pairs with disjoint Hasse endpoints, whose reversals in the upward-oriented face-poset Hasse diagram leave an acyclic directed graph. The full tetrahedron has \(15\) nonempty faces and \(28\) primitive Hasse edges. Its boundary has \(14\) nonempty faces and \(24\) primitive Hasse edges. The four additional vertices of \(F\) are the pairs \(e_i=(\{0,1,2,3\}\setminus\{i\},\{0,1,2,3\})\). Every two such pairs share the same upper endpoint and hence are incompatible.

For a subgroup \(H\le S_4\), the *orbit-barycenter triangulation* of a geometric fixed locus has one vertex for each \(H\)-orbit of Hasse-edge vertices that itself forms an acyclic matching; a family of orbit vertices spans a simplex precisely when the union of their Hasse edges forms an acyclic matching. Map each orbit to the barycenter of its original simplex. This maps simplices affinely and bijectively onto fixed points of the corresponding original simplices (the barycentric coordinates are constant on each orbit). Its realizations are exactly \(|F|^H\) and \(|B|^H\); no assertion that the fixed locus is a subcomplex on pointwise-fixed original vertices is used.

## Proof
**A. Complete fixed-point collapse.** Each admissible orbit containing a top pair \(e_i\) must be the singleton \(\{e_i\}\), because two distinct top pairs share the full-tetrahedron endpoint. Such a singleton orbit is \(H\)-invariant exactly when label \(i\) is fixed by every element of \(H\). Therefore no new orbit vertex occurs unless \(H\) has a globally fixed tetrahedron label. The script `verify.py` enumerates the **entire subgroup lattice** of \(S_4\), generating each subgroup as a closure under composition, and proves there are \(30\) subgroups. Of its \(29\) nontrivial subgroups, six order-two transposition groups fix two labels, four order-three groups and four order-six point-stabilizer groups fix one label, and the other fifteen fix none.

For each of these \(29\) subgroups, the script reconstructs the **complete** orbit-simplex complexes independently for the full tetrahedron and its boundary; it embeds the latter by the canonical orbit map, and then deletes pairs \((\sigma,\tau)\) where \(\tau\) is a maximal simplex and \(\sigma\) is its unique codimension-one face not lying in the boundary subcomplex. It recomputes the maximal cofaces at each step. The verified numbers of elementary pairs are \(42\) for each transposition subgroup, \(2\) for each one-fixed-label subgroup, and zero when no label is fixed. The remaining simplex set is **exactly** the embedded boundary fixed complex in every case. This is a finite exhaustive proof because the subgroup generation, orbit generation, simplex membership and free-face conditions are defined by exhaustive deterministic algorithms and checked with assertions. For orientation, a transposition gives boundary/full face vectors \((8,22,24,8)\) and \((10,36,56,36,8)\), while a three-cycle gives \((2,1)\) and \((3,3,1)\). A double transposition has identical boundary and full fixed complexes, each with face vector \((8,8)\); a four-cycle gives both empty.

**B. Relative homology from four stars.** Because the four top-pair vertices \(e_i\) are mutually incompatible, every relative simplex of the pair \((F,B)\) contains exactly one of them. Thus its relative simplicial chain complex is a **direct sum** of four augmented link complexes, each shifted upward one degree. Specifically, for \(e_3=(\{0,1,2\},\{0,1,2,3\})\), the link \(L=\operatorname{lk}_F(e_3)\) has \(21\) vertices and \(2122\) faces including the empty face, with counts by cardinality from zero through six of
\[
(1,21,162,560,846,468,64).
\]
The verifier constructs every link face from the Hasse relation, endpoint disjointness, and acyclicity. On its **augmented** face poset (including the empty face), the explicit greedy ascending-vertex pairing in the `VERTEX_ORDER` variable gives \(1049\) disjoint face/coface pairs, including the empty face paired to a vertex, and leaves precisely \(24\) critical faces, **all cardinality four**. The verifier constructs every directed cover of this entire \(2122\)-element augmented face poset, reverses exactly the matched arrows, and proves acyclicity by complete topological sorting. Standard acyclic-matching cancellation for the augmented integral cellular chains gives a chain-homotopy equivalent reduced complex with \(24\) generators only in degree three and therefore
\[
\widetilde H_q(L;\mathbb Z)\cong\begin{cases}\mathbb Z^{24},&q=3,\\0,&q\ne3.\end{cases}
\]
The four links are isomorphic by tetrahedral vertex permutations, so direct-sum shifted relative chains give \(H_4(F,B;\mathbb Z)\cong\mathbb Z^{4\cdot24}\) and every other relative homology group zero. The assertion concerns homology, not an unproved equivariant integral splitting.

**C. Regular rational action from fixed points.** Let \(g\in S_4\) be nonidentity. Part A supplies an actual elementary collapse \(|F|^{\langle g\rangle}\searrow |B|^{\langle g\rangle}\), hence their Euler characteristics coincide. Equivariant simplicial Lefschetz--Euler theory (or direct signed simplex traces) identifies the relative alternating rational chain trace of \(g\) with the difference of these fixed-space Euler characteristics, so it is zero. By Part B, all relative homology is concentrated in even degree four; therefore \(\operatorname{tr}(g\mid H_4(F,B;\mathbb Q))=0\) for every nonidentity \(g\). At the identity the trace is \(96\). The regular \(S_4\)-character equals \(24\) at the identity and zero elsewhere. Character theory over \(\mathbb Q\) therefore yields exactly four copies of \(\mathbb Q[S_4]\). This uses the complete relative character, not the already known absolute fourth-homology character.

## Verification
Run `python3 verify.py` in the directory containing this document. Only Python 3 standard-library modules are used. The certificate reconstructs all \(30\) subgroups, verifies every one of the \(29\) proper-subgroup relative collapses, independently constructs the \(2122\)-face link, and checks its complete \(1049\)-pair augmented acyclic matching. It asserts all counts and reports `ALL CHECKS PASSED`. The exact scope and proof of exhaustive coverage are the finite combinatorial definitions in Part A and the complete directed acyclicity test in Part B. Logs are not substituted for these arguments.

## Relationship to prior work
Scoville's 2026 paper gives the nonequivariant homotopy types \(F\simeq\bigvee^{99}S^4\) and \(B\simeq\bigvee^{21}S^3\vee\bigvee^{24}S^4\), constructs the inclusion, and explicitly computes the **previously known** relative group of rank \(96\) in degree four. It does not determine its \(S_4\)-module or the behavior of the inclusion on all proper-subgroup geometric fixed sets. Two prior published mathematical records separately calculate the complete **absolute** \(S_4\)-character of \(H_4(F;\mathbb Q)\), namely \((99,1,-1,0,-1)\), but do not calculate the relative action or fixed-point collapses of the pair. Relative characters cannot be recovered from that absolute character without knowing the boundary representation and the inclusion morphism; they are independently established here.

## Limitations
The statement is for the ordinary complexes of the full three-simplex and its boundary, not higher-dimensional simplices or pure discrete-Morse matching complexes. The geometric fixed-point result applies only to **nontrivial** subgroups, not the identity subgroup: the nonequivariant inclusion is not a homotopy equivalence. The relative module splitting is asserted only over \(\mathbb Q\); no integral group-ring splitting is claimed. Literature searches and direct comparisons do not eliminate the possibility of equivalent unindexed work. No independent mathematical audit is claimed.

## References
1. N. A. Scoville, *The complex of discrete Morse matchings of the n-simplex: homotopy types and structural results*, arXiv:2604.18172v1, first public date 2026-04-20; particularly §4.1, Proposition 16, relative computation, Theorem 20 and Table 2. https://arxiv.org/abs/2604.18172
2. M. K. Chari and M. Joswig, *Discrete Morse Complexes*, arXiv:math/0011234v1 (2000). https://arxiv.org/abs/math/0011234
3. M. Lin and N. A. Scoville, *On the automorphism group of the Morse complex*, arXiv:1904.10907v1 (2019). https://arxiv.org/abs/1904.10907
4. *The complete \(S_4\)-character on tetrahedral discrete Morse matching homology*, published mathematical finding, identifier `aa2567a7706d`, October 11, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-complete-s-4-character-on-tetrahedral-discrete-morse-matchin--aa2567a7706d
5. *The \(S_4\)-character of tetrahedral Morse-complex homology*, published mathematical finding, identifier `3b1fdcb3c035`, October 11, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-s-4-character-of-tetrahedral-morse-complex-homology--3b1fdcb3c035
