# Complete Rips homotopy and persistence of the Pappus graph
## Finding
Let \(G\) be the eighteen-vertex Pappus graph with unit-edge shortest-path distance \(d_G\). For every real \(r\ge0\), define the **inclusive** Vietoris–Rips complex \(K_r=\mathrm{VR}_{\le}(V(G),d_G;r)\), consisting of all subsets of diameter at most \(r\). Then
\[
K_r\simeq
\begin{cases}
\bigsqcup^{18}\mathrm{pt},&0\le r<1,\\
\bigvee^{10}S^1,&1\le r<2,\\
\bigvee^{26}S^2,&2\le r<3,\\
\bigvee^{64}S^5,&3\le r<4,\\
\mathrm{pt},&r\ge4.
\end{cases}
\]
This is a classification of the homotopy type **at every scale**. In particular, all integral homology is torsion-free. Over every coefficient field, the complete persistence barcode has seventeen degree-zero intervals \([0,1)\), one degree-zero interval \([0,\infty)\), ten degree-one intervals \([1,2)\), twenty-six degree-two intervals \([2,3)\), and sixty-four degree-five intervals \([3,4)\), and no other nonempty intervals of positive length.

## Assumptions and scope
The Pappus graph is the cubic incidence (Levi) graph of the Pappus \(9_3\) configuration. The following explicit labeled model fixes every combinatorial assertion in the proof. Its vertices are \(\{0,1,\ldots,17\}\), with the eighteen cycle edges joining consecutive labels modulo \(18\). Add nine chords using the standard LCF list `(5,7,-7,7,-7,-5)` repeated three times: for each label \(i\), add the unordered edge joining \(i\) to \(i+s_i\pmod{18}\), where \(s_i\) is the corresponding list entry. Duplicate undirected chords are included only once. This produces exactly twenty-seven edges. It agrees with the standard LCF presentation of the Pappus graph (MathWorld, *Pappus Graph*).

The two bipartition classes are the even and odd labels, each with nine vertices. All graph distances, and the finite partitions used below, can be verified by eighteen breadth-first searches in the self-contained `verify_pappus_rips.py`. There are no probabilistic or limiting hypotheses; the result concerns this canonical finite graph only. Sphere wedges with \(m\) summands mean the one-point wedge of \(m\) copies of that sphere.

## Proof
**1. Exact metric partitions.** The graph is connected, bipartite, has eighteen vertices and twenty-seven edges, and has diameter four. In the chosen labels, the unordered pairs at distance four form exactly six vertex-disjoint triangles:

`(0,10,14), (1,11,15), (2,6,16), (3,7,17), (4,8,12), (5,9,13)`.

This assertion means that within each listed triple every pair has distance four, while no pair from different triples has distance four. Three triples lie entirely in each bipartition class. To verify it, use the displayed cycle-and-chord adjacency and ordinary BFS from each of the eighteen vertices; the included verifier constructs every graph edge and distance and checks precisely these six triples. For two distinct vertices in the same bipartition class, bipartiteness and diameter four force distance two or four. For vertices in opposite classes, distance is one or three. Thus at scale two, the induced graph on each nine-vertex color class is the complete tripartite graph \(K_{3,3,3}\), with the three forbidden triples as its parts, and a cross-class edge is present precisely when the two endpoints were adjacent in \(G\). At scale three, the **only missing edges** are the edges within the six distance-four triples.

**2. Radius zero and one.** No edges occur before radius one. At radius one the complex is just the original graph, since a bipartite graph has no triangles. A connected graph with eighteen vertices and twenty-seven edges has first Betti number \(27-18+1=10\) and is homotopy equivalent to \(\bigvee^{10}S^1\).

**3. Radius two: a null-attached homotopy pushout.** Write \(P\) and \(L\) for the even and odd color classes. Let \(U\) be the subcomplex of \(K_2\) consisting of all simplices using only vertices in \(P\), together with every face \(\{\ell\}\cup\sigma\), where \(\ell\in L\) and \(\sigma\) is any subset of its three neighbors in \(P\). Define \(V\) symmetrically by interchanging \(P\) and \(L\). The absence of four-cycles in \(G\) shows that no clique of \(K_2\) contains at least two points and at least two lines: two distinct points have at most one common neighbor in \(L\). Consequently \(K_2=U\cup V\). Moreover, \(U\cap V=G\) as a one-dimensional simplicial complex, because their only common mixed simplices are the original incidence edges.

For every \(\ell\in L\), the simplex \(\{\ell\}\cup N_G(\ell)\) is attached in \(U\) solely along the simplex on \(N_G(\ell)\). It collapses simplicially onto that base, and these cone removals are independent for different \(\ell\). Therefore \(U\) deformation retracts to the induced clique complex on \(P\), and likewise \(V\) retracts to the corresponding complex on \(L\). Each induced graph is \(K_{3,3,3}\), so each induced clique complex is the join of three discrete three-point sets. A discrete three-point set has reduced homotopy type \(S^0\vee S^0\); the join of three such sets is therefore a wedge of \(2^3=8\) two-spheres. In particular, \(U\simeq\bigvee^8 S^2\) and \(V\simeq\bigvee^8 S^2\) are simply connected.

The inclusion maps \(G\hookrightarrow U\) and \(G\hookrightarrow V\) are nullhomotopic: \(G\) is a connected one-dimensional CW-complex and both targets are simply connected. Because the subcomplex inclusions are cofibrations, the union \(U\cup_G V\) is the homotopy pushout of this diagram. Replacing the two maps by the nullhomotopic maps yields
\[
K_2\simeq U\vee V\vee\Sigma G
\simeq \bigvee^{8+8+10}S^2
=\bigvee^{26}S^2.
\]
Here \(\Sigma G\) denotes unreduced suspension; for a connected graph \(G\simeq\bigvee^{10}S^1\), its suspension is \(\bigvee^{10}S^2\). This argument proves the **integral homotopy type**, not just a mod-two Betti number. Directly, the eighteen three-simplices of \(K_2\) are the closed graph-neighborhood tetrahedra, and each has a free triangular face; thus the radius-two complex also collapses to a two-dimensional simplicial complex.

**4. Radius three: six-factor join.** Two distinct vertices are adjacent in the radius-three graph if and only if they are not in the same one of the six distance-four triples. Hence that graph is complete six-partite, with three vertices per part. Its clique complex is the simplicial join
\[
K_3=D_3*D_3*D_3*D_3*D_3*D_3,
\]
where \(D_3\) denotes the discrete three-point complex. Since \(D_3\simeq S^0\vee S^0\), the join–smash suspension identity gives \(K_3\simeq\bigvee^{2^6}S^5=\bigvee^{64}S^5\). This is an exact identification of the simplices, not only a homology calculation.

**5. Radius four and persistence.** Since the graph diameter is four, \(K_4\) is the full simplex and is contractible. Every distance is integral, so the complex stays unchanged on each displayed half-open interval. The nonzero reduced homology occurs in different positive degrees at consecutive thresholds; hence every positive-dimensional class born at one threshold dies at the next. Connectivity at threshold one gives the stated zero-dimensional intervals. These observations determine the entire interval decomposition over any field.

## Verification
The included standard-library script `verify_pappus_rips.py` independently constructs the eighteen-vertex LCF graph and computes all vertex distances by BFS. It checks connectivity, degree, bipartition, diameter, and the six distance-four triples. It exhaustively constructs every simplex of \(K_1\), \(K_2\), and \(K_3\), checks the purported radius-two cover and its incidence-graph intersection, checks the eighteen neighborhood tetrahedra and free faces, and checks the six-partite radius-three simplex construction.

As an independent arithmetic check, it computes the mod-two boundary ranks from the full lists of simplices. It obtains face vectors \((18,27)\), \((18,81,108,18)\), and \((18,135,540,1215,1458,729)\) at radii one, two, and three, respectively. Their boundary ranks are \((17)\), \((17,64,18)\), and \((17,118,422,793,665)\), giving exactly the Betti multiplicities in the theorem. A separate triangle-relator elimination checks simple connectivity at radius two by killing all sixty-four non-tree edge generators.

To reproduce, save the embedded `verify_pappus_rips.py` and execute `python3 verify_pappus_rips.py` with a standard CPython installation. Successful exact verification ends with `VERIFY_OK`. These finite computations establish the graph-specific combinatorial premises; the stated homotopy and persistence conclusions follow by the written topological argument.

## Relationship to prior work
Adamaszek's *Clique complexes and graph powers* establishes the graph-power/Vietoris–Rips correspondence and general collapse criteria. Its girth bound \(\mathrm{girth}(G)\ge 3r+1\) at radius two would require girth at least seven, whereas the Pappus graph has girth six. In fact, its radius-two complex has nontrivial second homology, so the criterion's collapse-to-graph conclusion is inapplicable.

Larrión, Pizaña, and Villarroel-Flores prove a fundamental-group equivalence between the clique complex of the square of a connected bipartite graph and the squared induced graphs on each side. Kawamura develops a homological refinement in *A variant of the bipartite relation theorem and its application to clique graphs*. Both supply a relevant structural setting, but neither paper computes the Pappus graph's two-sphere multiplicity or its higher-radius filtration. The radius-two calculation here specializes the square-cover method to the two \(K_{3,3,3}\) subcomplexes, with the critical extra suspension summand determined by their gluing graph.

The published result *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs* treats a different incidence system, in which every two points lie on a common line and every two lines intersect. A Pappus \(9_3\) configuration lacks those axioms: three disjoint triples in each class have pairwise graph distance four, so its radius-two clique complex is not the suspension of the entire incidence graph and the projective-plane theorem does not imply the present formula. The same public corpus contains a computation of the Pappus **matching complex**, a different simplicial construction; its degree-five mod-two homology rank forty does not cover the present Rips degree-five multiplicity sixty-four.

Adamaszek and Adams classify Vietoris–Rips complexes of the circle and establish a fundamental early persistence benchmark. Their cyclic-graph hypotheses do not describe the Pappus graph. The complete four-threshold homotopy classification and field-independent barcodes stated here are not direct consequences of any of these statements.

## Limitations
This is an exact classification for the single standard unweighted graph, not a theorem for every cubic symmetric graph, every Levi graph, or a continuously weighted deformation. The symmetry action on homology and maps between specific geometric sphere generators have not been classified; the persistence intervals follow because adjacent positive-degree homology groups vanish. The originality comparisons do not rule out a differently titled, unindexed equivalent computation. The exact verifier checks combinatorial topology on this finite graph; it does not constitute independent external validation.

## References
Adamaszek, M., *Clique complexes and graph powers*, arXiv:1104.0433, first posted 2011-04-03; in particular Section 2, Proposition 2.2, and Section 3, Theorem 3.1. https://arxiv.org/abs/1104.0433.

Adamaszek, M.; Adams, H., *The Vietoris–Rips complexes of a circle*, arXiv:1503.03669, first posted 2015-03-12; Pacific Journal of Mathematics 290 (2017), 1–40; primary MSC2010 55U10 and 05E45. https://arxiv.org/abs/1503.03669.

Larrión, F.; Pizaña, M. A.; Villarroel-Flores, R., *The fundamental group of the clique graph*, European Journal of Combinatorics 30 (2009), 288–294; DOI 10.1016/j.ejc.2007.12.006.

Kawamura, K., *A variant of the bipartite relation theorem and its application to clique graphs*, Contributions to Discrete Mathematics 6 (2011), 91–100; DOI 10.55016/ojs/cdm.v6i2.62059. https://cdm.ucalgary.ca/article/download/62059/46707/177343.

Weisstein, E. W., *Pappus Graph*, MathWorld; LCF and cubic distance-regular realization. https://mathworld.wolfram.com/PappusGraph.html.

*Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, publicly available research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-scale-two-vietoris-rips-complexes-of-finite-projective-plane-inc--c3740b96b3c3.
