# Sharp edge threshold for torsion in matching complexes of seven-vertex graphs

## Finding

For a finite simple graph \(G\), let \(\mathcal M(G)\) be the ordinary matching complex: its simplices are sets of pairwise vertex-disjoint edges of \(G\). Among **all simple graphs with at most seven vertices**, the torsion subgroup of \(\widetilde H_1(\mathcal M(G);\mathbb Z)\) is either zero or \(\mathbb Z/3\). Exactly **40 unlabeled isomorphism classes** have nonzero torsion; all have seven vertices. Their counts by number of graph edges are:

| Number of edges \(e\) | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| Classes with \(\mathbb Z/3\)-torsion | 1 | 3 | 9 | 10 | 8 | 5 | 2 | 1 | 1 |

Consequently **seven is the minimum possible underlying graph order for this torsion**, and **among graphs with at most seven vertices, thirteen edges is the sharp edge threshold**. No global minimum-edge assertion is made for larger graph orders. The unique isomorphism class at the thirteen-edge boundary is Graph Atlas graph `G1105`, encoded by graph6 `FbY|o`. For this graph,
\[
\widetilde H_1(\mathcal M(G1105);\mathbb Z)\cong\mathbb Z/3,
\qquad \widetilde H_i(\mathcal M(G1105);\mathbb Z)=0\ \text{for}\ i\ne1.
\]
The list of all 40 classes, in Graph Atlas indexing, is in `torsion_cases.json`.

## Assumptions and scope

Graphs are undirected, simple, unlabeled up to isomorphism, possibly disconnected, and may contain isolated vertices. The graph order is at most seven; the number of edges is unconstrained except by simplicity. Homology is reduced simplicial homology with integral coefficients. The matching-complex vertices are the **graph edges**, not the original graph vertices. An \(i\)-simplex is a matching consisting of \(i+1\) graph edges; thus for graph order at most seven the complex has dimension at most two. Zero-dimensional and empty complexes use the usual reduced-homology conventions.

## Proof

**Algebraic reduction.** For each graph, enumerate its matchings of sizes one, two and three, with orientations from increasing edge indices. The signed boundary \(\partial_2:C_2\to C_1\) sends the oriented triple \([a,b,c]\) to \([b,c]-[a,c]+[a,b]\). Since \(\partial_1\partial_2=0\), there is an exact sequence
\[
0\longrightarrow H_1(\mathcal M(G);\mathbb Z)
\longrightarrow C_1/\operatorname{im}\partial_2
\longrightarrow \operatorname{im}\partial_1\longrightarrow0.
\]
The group \(\operatorname{im}\partial_1\) is free abelian, so the torsion subgroups of \(H_1\) and \(C_1/\operatorname{im}\partial_2\) coincide. The nonunit entries in the integral Smith normal form of \(\partial_2\) therefore determine *all* first-homology torsion. There are no higher simplices to enumerate.

**Exhaustive calculation.** The standard Read–Wilson Graph Atlas lists exactly 1,253 isomorphism representatives through seven vertices, distributed by graph order \(0,1,2,3,4,5,6,7\) as \(1,1,2,4,11,34,156,1044\). The complete graph6 list appears in `atlas.g6`. The program `verify_exact.py` reconstructs each graph using a direct graph6 parser, enumerates all its matchings, forms every signed integral boundary and calculates exact Smith normal form over \(\mathbb Z\). All 1,253 records are processed. There are no nonunit Smith factors for the first 209 representatives of orders at most six. For the 1,044 seven-vertex representatives, exactly the 40 indexed in `torsion_cases.json` have a nonunit invariant, which is **precisely one factor of 3** in each case. Their edge-count distribution is the table above. Exactly one torsion representative has thirteen edges: `G1105`. No representative with at most twelve edges has first-homology torsion.

**Concrete integral witness.** With the original graph edges indexed lexicographically, the thirteen edges of `G1105` are

```text
(0,1) (0,5) (0,6) (1,3) (1,4) (2,3) (2,4)
(2,5) (2,6) (3,5) (3,6) (4,5) (4,6)
```

The matching complex has face numbers \((f_0,f_1,f_2)=(13,42,30)\). Its \(42\)-by-\(30\) integral second boundary has Smith diagonal consisting of twenty-nine 1s and one 3. Its one-skeleton is connected, so the first boundary has rank twelve. Thus the reduced homology stated above follows, including zero second homology.

A further signed certificate in `torsion_certificate.json` supplies an explicit one-cycle \(z\) and two-chain \(c\) satisfying \(\partial_1z=0\) and \(\partial_2 c=3z\). The four-term cycle is
\[
z=-[e_0,e_5]+[e_0,e_6]+[e_1,e_5]-[e_1,e_6],
\]
where \(e_i\) is the graph edge with index \(i\) in the displayed list. The boundary \(\partial_2\) is injective over the rationals (rank thirty), while at least one coefficient of the given \(c\) is not divisible by three. Hence the unique rational preimage of \(z\) is \(c/3\), not an integral chain; \(z\) is nonzero of exact order three.

## Verification

With Python, NetworkX and SymPy installed, run `python verify_exact.py` and `python verify_modular.py` in the directory of the supplied files. Both programs were executed successfully on the embedded data. The exact script verifies every Smith factor, the complete torsion-case list, the edge distribution and the explicit integral torsion-cycle certificate. The second script independently constructs the same matching complexes as clique complexes of complements of line graphs and performs sparse rank elimination over prime fields. It reproduces all 40 torsion-class indices. For `G1105`, the integral second boundary has rank thirty, whereas its rank modulo three is twenty-nine; ranks modulo two, five, seven and 101 are thirty. `VERIFICATION.md` describes the checks and their limitations. The accompanying graph6 data are frozen, and the checker compares them with a freshly constructed standard Graph Atlas enumeration.

## Relationship to prior work

Shareshian and Wachs, drawing on Bouc, establish the existence of 3-torsion in the matching complex of the **complete graph on seven vertices** and broader complete-graph results. Those statements do not determine the minimum number of edges needed in an arbitrary seven-vertex graph, the unique sparse witness, or all 40 isomorphism classes.

Adamaszek classifies first-homology torsion in general flag complexes having **at most twelve simplicial vertices**; the thirteen-edge witness here has thirteen *matching-complex* vertices and lies beyond that bound. Goeckner, Herr, Jones and Rowlands classify two-dimensional Buchsbaum matching complexes, which is a different condition from integral torsion and does not supply this torsion census. Read–Wilson's Graph Atlas supplies the graph representatives, not their matching-complex homology. These distinctions concern mathematical implication, not mere title matching.

## Limitations

This is an exhaustive finite classification for original graph order at most seven, not a formula for larger graphs and not a classification of homotopy or fundamental groups. The completeness of unlabeled representatives relies on the established Graph Atlas catalog; the entire input enumeration is included for reproduction. Exact integral Smith calculations, rather than finite-field tests alone, establish the torsion assertion. An equivalent enumeration in unindexed literature remains possible. Independent external audit has not been performed.

## References

1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first posted 2004-09-03), especially §1 and Theorem 1.3; https://arxiv.org/abs/math/0409054.
2. M. Adamaszek, *Small Flag Complexes with Torsion*, arXiv:1208.3892 (first posted 2012-08-19), Theorem 1; https://arxiv.org/abs/1208.3892.
3. B. Goeckner, F. Herr, L. Jones II and R. Rowlands, *A characterization of two-dimensional Buchsbaum matching complexes*, arXiv:2110.11302 (first posted 2021-10-21), Theorem 4.1 and appendix; https://arxiv.org/abs/2110.11302.
4. R. C. Read and R. J. Wilson, *An Atlas of Graphs*, Oxford University Press, 1998. Graph Atlas enumeration documented at https://networkx.org/documentation/stable/reference/generated/networkx.generators.atlas.graph_atlas_g.html.
