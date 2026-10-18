# The complete \(S_4\) homology character of the truncated-tetrahedron matching complex

## Finding
Let \(T\) denote the standard twelve-vertex truncated-tetrahedral graph, and let \(K=\mathcal M(T)\) be its ordinary **matching complex**. The full graph-automorphism group acts on the complex and is naturally isomorphic to \(S_4\). The nonzero reduced integral homology is
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{22},\qquad
\widetilde H_i(K;\mathbb Z)=0\quad(i\ne3).
\]
**The new result is the complete natural rational homology representation.** In the conjugacy-class order \((1^4),(2,1^2),(2^2),(3,1),(4)\), its character is
\[
\chi_3=(22,0,2,-2,-2).
\]
Write \(S^\lambda\) for the rational irreducible Specht module of \(S_4\) indexed by a partition \(\lambda\) of four. Then
\[
\boxed{\widetilde H_3(K;\mathbb Q)\cong
S^{(1,1,1,1)}\oplus3S^{(3,1)}\oplus2S^{(2,1,1)}\oplus3S^{(2,2)}.}
\]
Thus every nontrivial rational irreducible \(S_4\)-representation occurs, but the trivial representation does not. In particular,
\[
\dim\widetilde H_3(K;\mathbb Q)^{S_4}=0,\qquad
\dim\widetilde H_3(K;\mathbb Q)^{A_4}=1.
\]
The nonequivariant wedge \(K\simeq\bigvee^{22}S^3\) was calculated previously; the claim is not priority over that homotopy classification.

## Assumptions and scope
Fix \(B=\{0,1,2,3\}\). The graph has vertex set \(V(T)=\{(a,b)\in B^2:a\ne b\}\). Distinct vertices \((a,b),(c,d)\) form an edge precisely when either \(a=c\), or \((c,d)=(b,a)\). Consequently \(T\) has four disjoint triangles (twelve internal triangle edges), together with six reversal edges. A matching is a set of pairwise endpoint-disjoint graph edges; a \(q\)-simplex of \(K\) is a matching of size \(q+1\). We use ordinary oriented simplicial chains for signs and reduced homology for all formulas.

Any \(p\in S_4\) sends \((a,b)\mapsto(p(a),p(b))\), defining a graph and simplicial-complex automorphism. These are **all** graph automorphisms: the four triangles are the only three-cycles, hence any automorphism permutes their four vertex-disjoint components. The six reversal edges uniquely connect each pair of triangles, and within each triangle the vertex \((a,b)\) is identified by the other triangle to which its unique reversal edge leads. Thus an automorphism is uniquely determined by the permutation of the four triangles. No larger symmetry group is assumed.

## Proof
**1. Exact integral homology concentration.** Lexicographically order the eighteen graph edges and represent a simplex by its eighteen-bit indicator. Enumerating all mutually disjoint edge sets gives exactly \(1009\) nonempty simplices, with dimension-wise face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(18,117,332,390,144,8).
\]
Process first the six reversal-edge bits and then the twelve triangle-edge bits. For each bit, pair every currently unpaired nonempty face not containing that bit with its one-bit augmentation, provided both remain unpaired. The procedure produces exactly \(493\) distinct cover pairs, leaving one critical vertex and \(22\) critical three-simplices. Reorient each nonempty face-poset covering relation downward except for matching pairs, which point upward. Exhaustive topological sorting processes all \(1009\) vertices over all \(3558\) directed covering incidences. Thus the directed graph is acyclic, and this is a genuine discrete-Morse matching, not merely a reduction of chain ranks.

The resulting CW homotopy model has one zero-cell and twenty-two three-cells, with no intermediate cells. Every three-cell attaches to the zero-skeleton by the constant map, so \(K\simeq\bigvee^{22}S^3\). This independently verifies the previously known nonequivariant homology used below and proves the integral assertion. The complete finite certificate is implemented in `verify_truncated_tetra_character.py`.

**2. Signed Lefschetz character.** For \(g\in S_4\), let \(C_q(K;\mathbb Q)\) carry the oriented-simplex basis determined by increasing graph-edge index. The diagonal coefficient of an oriented simplex is zero unless \(g\) fixes its underlying matching set. A setwise-fixed simplex contributes the sign of the permutation of its \(q+1\) edge labels. Therefore
\[
\operatorname{tr}(g\mid\widetilde H_3)
=1-\sum_{q=0}^5(-1)^q\operatorname{tr}(g\mid C_q).
\]
Indeed, this is the reduced equivariant Euler-Poincaré identity, since reduced homology vanishes outside degree three and the contribution of the empty face is one.

The verifier evaluates these exact signed counts separately for every one of the twenty-four permutations, both by traversing all simplices and independently by enumerating unions of cycles in the induced permutation of the eighteen graph edges. A setwise-fixed simplex is necessarily a union of those edge-label cycles; its sign equals the product of the cycle signs. These two finite methods agree on all group elements. The class sizes \((1,6,3,8,6)\) and resulting traces are
\[
\begin{array}{c|rrrrr}
\text{cycle type}&(1^4)&(2,1^2)&(2^2)&(3,1)&(4)\\\hline
\text{class size}&1&6&3&8&6\\
\operatorname{tr}(g\mid\widetilde H_3)&22&0&2&-2&-2
\end{array}
\]
(with the stated class order and no unexamined automorphisms).

**3. Exact representation decomposition.** The rational irreducible characters of \(S_4\), in this class order, are
\[
\begin{array}{c|rrrrr}
S^{(4)}&1&1&1&1&1\\
S^{(1,1,1,1)}&1&-1&1&1&-1\\
S^{(3,1)}&3&1&-1&0&-1\\
S^{(2,1,1)}&3&-1&-1&0&1\\
S^{(2,2)}&2&0&2&-1&0
\end{array}
\]
Taking scalar products with \(\chi_3\) using conjugacy-class sizes and dividing by \(24\) yields, in table order, the five exact nonnegative integer multiplicities \((0,1,3,2,3)\), which sum by dimension to \(22\). Semisimplicity in characteristic zero proves the displayed module isomorphism. The absence of the trivial summand proves vanishing of full invariants. The alternating invariants have dimension \((22+3\cdot2+8\cdot(-2))/12=1\), completing the claimed symmetry statement.

## Verification
Run `python3 verify_truncated_tetra_character.py` using only Python 3's standard library. It builds the graph from its exact ordered-pair description, enumerates every matching, constructs every greedy Morse pair, confirms acyclicity by a full directed-Hasse-graph topological sort, and evaluates all twenty-four automorphisms with two independent signed fixed-simplex methods. The executable also checks the group-class sizes and all five exact Specht multiplicities. Its final marker is `VERIFIED: finite acyclic Morse matching and two independent signed Lefschetz methods on 24 elements`. This is a finite exhaustive mathematical certificate for the stated single graph, not an extrapolation to all truncated polyhedra.

## Relationship to prior work
The previously published same-object computation *Edge-orbit matching-complex homotopy of the truncated tetrahedron* establishes the integral wedge of twenty-two three-spheres and stronger nonequivariant edge-deletion/link decompositions. Its complete `RESULT.md` was inspected. It does not identify an \(S_4\)-action on third homology, give signed class traces, or state a Specht-module decomposition. The nonequivariant splitting does not imply the character without equivariant maps; the rank \(22\) is an input, not the new contribution. A work titled *The complete \(S_4\)-character on tetrahedral discrete Morse matching homology* computes a different, ninety-nine-dimensional fourth-homology module of the **discrete Morse complex of the three-simplex**, and is not a calculation for matchings of the truncated-tetrahedral graph. A separate octahedral matching-complex representation concerns a different graph and an eleven-dimensional first homology. All three primary result texts were inspected and compared at the level of spaces, dimensions and group actions.

Engström's *Independence complexes of claw-free graphs* (first public version 2005-12-17) provides earlier broad topology and connectivity literature relevant to matching complexes (independence complexes of line graphs). The complete-hypergraph matching-representation results of Bate, Everitt, Ford and Ramos concern all-subset hyperedges or complete-graph matching complexes, not the sparse eighteen-edge truncated-tetrahedral graph. The indexed searches under the graph, its once-subdivided-\(K_4\) line-graph description, equivariant matching homology, and the exact \(S_4\)-character found no stronger or identical covered statement. These searches do not prove universal publication priority.

## Limitations
The irreducible representation decomposition is **rational**, not a claim that the integral homology lattice splits into integral Specht summands. The theorem is specific to the stated twelve-vertex graph and its full automorphism group. It does not give an infinite-family result, an equivariant wedge decomposition, or independent external scientific validation. Unknown or unindexed equivalent work could exist.

## References
1. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420v1, first public version 2005-12-17, https://arxiv.org/abs/math/0512420.
2. *Edge-orbit matching-complex homotopy of the truncated tetrahedron*, published research record, full result inspected, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-edge-orbit-matching-complex-homotopy-of-the-truncated-tetrahedro--f5ae4a359c83/RESULT.md.
3. *The complete \(S_4\)-character on tetrahedral discrete Morse matching homology*, published research record, full result inspected, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-complete-s-4-character-on-tetrahedral-discrete-morse-matchin--aa2567a7706d/RESULT.md.
4. *The full octahedral symmetry representation of the matching complex*, published research record, full result inspected, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-the-full-octahedral-symmetry-representation-of-the-matching-comp--c700eceb52bb/RESULT.md.
5. M. Bate, B. Everitt, S. Ford and E. Ramos, *Homology of matching complexes and representations of symmetric groups*, arXiv:2312.13750, https://arxiv.org/html/2312.13750v3.
