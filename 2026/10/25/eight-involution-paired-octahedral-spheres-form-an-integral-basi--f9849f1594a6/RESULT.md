# Eight involution-paired octahedral spheres form an integral basis for the Tietze matching complex

## Finding
Let \(T\) be the twelve-vertex Tietze graph, equivalently the flower graph \(J_3\), and let \(K=\mathcal M(T)=\operatorname{Ind}(L(T))\) be its ordinary matching complex, whose simplices are sets of pairwise vertex-disjoint edges of \(T\). The following are exact integral statements.

1. There is a homotopy equivalence \(K\simeq\bigvee^{16}S^3\), so \(\widetilde H_3(K;\mathbb Z)\cong\mathbb Z^{16}\) and all other reduced integral homology groups vanish.
2. Every induced subcomplex of \(K\) carrying nonzero third homology needs at least eight vertices (that is, eight selected graph edges). Exactly 63 eight-vertex subsets achieve the minimum. Each induced complex is \((S^0)^{*4}\cong S^3\), with a primitive integral fundamental class in \(\widetilde H_3(K;\mathbb Z)\).
3. The graph automorphism group has order 12 and acts on these 63 spheres in orbits of sizes \((6,12,12,3,12,12,6)\). Its unique nonidentity central involution \(\tau\) fixes three supports and exchanges 30 pairs. There are eight such exchanged pairs whose sixteen oriented fundamental classes form an *integral basis*, with basis-matrix determinant \(-1\). Therefore
\[
\widetilde H_3(K;\mathbb Z)\cong_{\mathbb Z[\langle\tau\rangle]}\mathbb Z[C_2]^{\oplus8}.
\]
Writing \(L^+=\ker(\tau_*-I)\) and \(L^-=\ker(\tau_*+I)\), the rational eigenspaces span but their integral sublattices do not:
\[
\widetilde H_3(K;\mathbb Z)/(L^++L^-)\cong(\mathbb Z/2\mathbb Z)^8.
\]
4. On \(\widetilde H_3(K;\mathbb Q)\), the automorphism character has values 16 on the identity, \(-2\) on each of the two elements of order three, and zero on the other nine elements. Under \(\operatorname{Aut}(T)\cong S_3\times C_2\), this is \((\mathbf1\oplus\operatorname{sgn}\oplus3V)\boxtimes(\mathbf1\oplus\varepsilon)\), where \(V\) is the two-dimensional standard representation of \(S_3\), and \(\varepsilon\) is the sign representation of \(C_2\). In particular the full-group rational invariant subspace is one-dimensional.

## Assumptions and scope
Start from the Petersen graph \(GP(5,2)\), with outer cycle edges \(\{i,i+1\}\), spokes \(\{i,i+5\}\), and inner edges \(\{i+5,(i+2\bmod5)+5\}\), for \(0\le i<5\). Replace vertex 0 and its three incident edges by the triangle \(\{10,11,12\}\), attaching its vertices to 1, 4 and 5 respectively. This is isomorphic to the standard flower-graph presentation \(J_3\) and fixes a completely reproducible model for the Tietze graph.

Number its eighteen edges from zero, in the following lexicographically increasing order (parenthesized pairs are *graph vertices*, not simplex indices):

```text
[(1,2),(1,6),(1,10),(2,3),(2,7),(3,4),(3,8),(4,9),(4,11),
 (5,7),(5,8),(5,12),(6,8),(6,9),(7,9),(10,11),(10,12),(11,12)]
```

Every nonempty face of \(K\) is encoded by the bit mask of its graph-edge indices, oriented by increasing indices. Integral simplicial boundaries use the conventional alternating signs. A graph automorphism permutes indices and acts on oriented simplices with the sign of the induced sorting permutation. These choices also define the explicit certificates below. No claim is made for larger flower snarks or arbitrary cubic graphs.

## Proof
**Finite complex and homotopy type.** Enumerate all nonempty masks from 1 to \(2^{18}-1\), retaining a mask exactly when its edges are pairwise endpoint-disjoint. The resulting face vector by dimensions zero through five is \((18,117,335,408,165,8)\), a total of 1,051 nonempty simplices. Apply successive unmatched-face toggles in the exact index order

```text
[1,10,2,13,6,3,17,0,14,11,16,8,7,12,9,4,15,5]
```

at each step pairing a surviving face without that index to its surviving coface with the index, if both survive. The 517 pairs leave precisely one critical zero-face and sixteen critical three-faces. Orient every unmatched codimension-one incidence downwards and reverse the 517 matched arrows. The explicit verifier constructs all 3,744 such directed Hasse incidences and topologically sorts all 1,051 vertices, proving acyclicity. Forman's discrete Morse theorem therefore gives a CW model with just one zero-cell and sixteen three-cells. Since there are no cells in intermediate dimensions, every three-cell attaches to the point. This proves the asserted integral wedge homotopy equivalence, not merely a finite-field Betti calculation.

**Minimum support.** We use the following flag-complex support lemma. If a finite flag complex has nonzero reduced homology in degree \(d\ge0\), it has at least \(2(d+1)\) vertices; if equality holds, it is the join of \(d+1\) copies of \(S^0\). For \(d=0\), a disconnected complex needs at least two vertices, and exactly two must be nonadjacent. Inductively, take a complex with a nonzero \(d\)-cycle supported on the fewest possible vertices and choose any vertex \(v\). Its deletion has zero \(d\)-homology by minimality; the link-deletion Mayer–Vietoris sequence then forces nonzero \((d-1)\)-homology in \(\operatorname{lk}(v)\). The inductive lemma gives at least \(2d\) vertices adjacent to \(v\). Since a flag complex with a vertex adjacent to all others is a cone, at least one additional vertex is nonadjacent. Thus there are at least \(2d+2\) vertices. At equality every vertex has exactly one nonneighbor (the same argument applies to every vertex, since removing any vertex from a minimum-vertex carrier kills top homology); the graph complement is a perfect matching, and the flag complex is precisely the cross-polytope boundary. Apply this with \(d=3\).

**Complete eight-vertex carrier census.** Eight selected graph edges give an induced octahedral sphere precisely when their edge-intersection graph is four independent edges: each selected graph edge intersects *exactly one* other selected edge, and all other cross-pairs are endpoint-disjoint. Exhaust all \(\binom{18}{8}\) choices and check this condition; exactly 63 pass. If the four intersecting pairs, sorted by increasing first edge index, are \((a_i,b_i)\), orient their octahedral fundamental cycle as the join \((a_1-b_1)*\cdots*(a_4-b_4)\). Explicitly it consists of 16 oriented matching faces; a selector contributes the sign \((-1)^{\text{number of second choices}+\text{inversions of selected indices}}\). Signed simplicial boundary is identically zero for each cycle.

**Integral homology coordinates.** Project each integral three-chain onto the sixteen critical three-cells by eliminating matched three/four-face pairs in a topological order of the corresponding gradient dependency digraph. Every pivot coefficient in the oriented boundary of its paired four-face is \(+1\) or \(-1\), hence the projection is integral. Direct exact checking shows that this projection vanishes on each of the 165 oriented four-face boundaries. The projection is an isomorphism on \(H_3\), because the Morse model has no critical four-cells and exactly sixteen critical three-cells. The greatest common divisor of the sixteen coordinates of each of the 63 fundamental cycles equals 1; each is primitive and nonzero in homology.

**Involution-paired unimodular basis.** Exhaustive graph isomorphism enumeration finds twelve automorphisms and exactly two central elements. Let \(\tau\) denote the nonidentity central involution. The following eight rows give paired octahedral-support masks, with the right column obtained from the left by \(\tau\) (bits use the graph-edge index convention above):

```text
115299 115907
180835 181443
157797 149710
15141  3486
27941  3022
7109   19766
47881  44314
80177  72090
```

Form a sixteen-by-sixteen integer matrix whose columns are the aforementioned critical-cell coordinates of these fundamental cycles, in row order and with the first and second mask of each row adjacent. Exact integer determinant is \(-1\). These sixteen classes therefore form an *integral* basis, while \(\tau\) exchanges the two support spheres in each pair, possibly reversing the selected fundamental orientations. Orient the second sphere compatibly with the image of the first to obtain eight literal transposition blocks. That proves \(\mathbb Z[C_2]^{\oplus8}\), rather than a statement only over \(\mathbb Q\). On one transposition block with basis \(u,v\), the invariant and anti-invariant integral sublattices are generated by \(u+v\) and \(u-v\); their sum has index two. Taking eight blocks gives the asserted quotient \((\mathbb Z/2)^8\).

**Full symmetry character.** Transport the sixteen fundamental cycles under each of the twelve graph automorphisms, accounting for the permutation sign of oriented matching simplices, then express their images in the unimodular basis. The resulting matrices are integral with determinant \(\pm1\); direct exact traces by element order are \(16,-2,0,0\) for orders 1,3,2,6 respectively. The character decomposition follows from the \(S_3\times C_2\) character table. Averaging over the twelve automorphisms gives invariant dimension \((16+2(-2))/12=1\). Both this action and the simpler signed Lefschetz character were separately computed by independent finite routines.

## Verification
Install dependencies from `requirements.txt`, then run

```text
python3 verify_tietze_central_lattice.py
python3 verify_tietze_independent.py
```

The first completely regenerates faces, the acyclic matching, every octahedral cycle, exact integer homology coordinates, all twelve graph automorphisms, the specified unimodular determinant, and the full integral involution quotient. It returns `VERIFY_OK_TIETZE_SHORTEST_OCTAHEDRAL_REGULAR_C2_LATTICE`. The second builds the graph by an *independent* flower-graph presentation, checks isomorphism to the triangle-expanded Petersen graph, computes independent mod-two boundary ranks, and obtains the symmetry character directly from signed Lefschetz traces. It returns `VERIFY_OK_INDEPENDENT_TIETZE_J3_AND_LEFSCHETZ`. Both are complete finite certificates for this one graph; no infinite classification is inferred from experiments.

## Relationship to prior work
The underlying Tietze graph and its identification with the three-petal flower construction are classical graph-theoretic objects. Engström [1] develops broader methods for independence complexes. Barmak's claw-free independence-complex methods and matching-complex connectivity bounds [2] do not compute this integral topological type or its shortest carriers. Jonsson [3] analyzes matching complexes of *complete* graphs, whose hypotheses do not cover this graph. Bayer, Jelić Milutinović, and Vega [4] prove sphere-wedge results for *outerplanar* graph matching complexes; the Tietze graph has the Petersen graph as a minor after contracting its replacement triangle, so that scope does not apply. An accessible published result on the Petersen graph matching complex [5] gives \(\bigvee^5S^2\vee\bigvee^5S^3\) for the ten-vertex Petersen graph itself, not the twelve-vertex triangle expansion and not the present integral octahedral-carrier and involution-lattice assertion. Comparison by implication therefore does not identify an existing covering theorem in these sources. Unindexed or unpublished equivalents cannot be ruled out.

## Limitations
The theorem classifies the one explicitly defined finite Tietze graph, not arbitrary flower snarks or graph matching complexes. The claim of minimum support concerns **induced** subcomplexes and cycles supported on their vertices, not arbitrary subdivisions or geometric volume. The basis certificates are exact but computationally assisted, with reproducibility depending on the specified graph, orientation, and integer calculation. The original Tietze graph predates the cited 2005 manuscript; the qualifying source date used in the accompanying metadata is the earliest exact day-verified public mathematical manuscript among the stated sources, *not* the date the graph was discovered. No independent external audit or unconditional publication-priority certification has been performed.

## References
[1] A. Engström, *Complexes of Directed Trees and Independence Complexes*, arXiv:math/0508148v1, first publicly posted 2005-08-08, https://arxiv.org/pdf/math/0508148. General independence-complex methods.

[2] J. A. Barmak, *Star Clusters in Independence Complexes of Graphs*, arXiv:1007.0418v1, publicly posted 2010-07-02, https://arxiv.org/html/1007.0418v1, Section 5.

[3] J. Jonsson, *Exact Sequences for the Homology of the Matching Complex*, arXiv:1203.5641v1, publicly posted 2012-03-26, https://arxiv.org/pdf/1203.5641, Theorem 3.4 and Section 5.

[4] M. Bayer, M. Jelić Milutinović, J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601v2, https://arxiv.org/pdf/2411.04601, Theorem 2.

[5] *The Petersen matching complex is a wedge of five two-spheres and five three-spheres*, published mathematical record, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-the-petersen-matching-complex-is-a-wedge-of-five-two-spheres-and--80050a324367/RESULT.md.

[6] *Tietze Graph*, MathWorld, https://mathworld.wolfram.com/TietzeGraph.html, graph identity and original graph context.
