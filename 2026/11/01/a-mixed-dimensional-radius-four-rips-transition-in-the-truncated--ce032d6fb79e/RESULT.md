# A mixed-dimensional radius-four Rips transition in the truncated dodecahedron

## Finding
Let \(D\) be the dodecahedral graph \(\operatorname{GP}(10,2)\), let \(S(D)\) denote its once-subdivided graph, and let \(T=L(S(D))\). Endow the sixty vertices of \(T\) with graph shortest-path distance. For the *inclusive* graph-metric Rips complex \(K_r=\operatorname{VR}_{\le r}(T)\), the following hold:

\[
K_3\searrow K_2\searrow K_1\simeq\bigvee^{11}S^1.
\]

The first collapse removes exactly 860 elementary free-face pairs; the second removes exactly 180. The natural inclusions \(K_1\hookrightarrow K_2\hookrightarrow K_3\) are simple-homotopy equivalences. At radius four,

\[
\widetilde H_i(K_4;\mathbb F_2)\cong
\begin{cases}
\mathbb F_2,&i=2,\\
\mathbb F_2^{12},&i=4,\\
0,&\text{otherwise}.
\end{cases}
\]

Thus, across thresholds zero through four the positive-degree \(\mathbb F_2\)-barcode contains exactly eleven degree-one intervals \([1,4)\), together with one degree-two and twelve degree-four intervals *born at four*. Their death times beyond four are not determined here. The coexistence of degree-two and degree-four homology at the same radius is the principal new phenomenon.

## Assumptions and scope
The dodecahedral graph has vertices \(u_j,v_j\) for \(j\in\mathbb Z/10\mathbb Z\), and undirected edges \(u_ju_{j+1}\), \(u_jv_j\), and \(v_jv_{j+2}\). It has twenty vertices and thirty edges. An element of \(V(T)\) is a directed incidence \((x,y)\) of an edge \(xy\in E(D)\). Two distinct incidences are adjacent precisely when their first coordinates agree or they are reversals of each other. Thus \(T\) has sixty vertices, ninety edges, twenty disjoint vertex-fibre triangles, and diameter ten. This is the usual cubic truncated dodecahedron.

All Rips complexes in this statement are on the **sixty discrete graph vertices**, not the continuous geometric realization or Euclidean polyhedron. A set of flags is a simplex of \(K_r\) exactly if all pairwise graph distances are at most \(r\). Because distances are integral, the asserted stages are constant for real parameters between integer thresholds, with the left endpoint included. Homology at radius four is taken over \(\mathbb F_2\); the lower-scale homotopy statements are integral.

## Proof
**1. Exhaustively specified finite chain groups.** The accompanying dependency-free checker constructs the above graph from the twenty-vertex generalized-Petersen presentation, uses breadth-first search from each vertex to obtain all sixty-by-sixty shortest-path distances, and enumerates all cliques of each distance power \(T^r\) by a bitset backtracking over lexicographically increasing vertex indices. Every nonempty simplex therefore appears exactly once. With components indexed by simplex dimension, the face vectors are

\[
\begin{aligned}
f(K_1)&=(60,90,20),\\
f(K_2)&=(60,210,200,60),\\
f(K_3)&=(60,390,760,690,300,50),\\
f(K_4)&=(60,630,2380,4230,3864,1850,480,60).
\end{aligned}
\]

**2. The relative collapses.** For each original vertex \(x\) let \(F_x=\{(x,y):y\sim_D x\}\) denote the three-element incidence fibre. Its flag simplex is a triangle. Every radius-three clique either projects to one fibre, projects to two adjacent fibres, or contains a projected distance-two pair centered at some vertex \(x\). The last case has a uniquely determined center because the dodecahedral graph has girth five. Group these extra faces by center; in each group toggle the fixed flag \((x,\min N_D(x))\) and delete lower/upper pairs in descending face size. This first stage has 320 pairs and leaves only faces contained in \(F_x\cup F_y\) for an edge \(xy\in E(D)\).

Among these two-fibre faces, those absent from \(K_2\) contain non-reversal incidences on both sides of their unique base edge. Toggle the bridge flag \((x,y)\), again in descending cardinality; 540 free-face pairs delete precisely the remaining radius-three extras. Thus \(K_3\searrow K_2\) by 860 elementary pairs. Analogously, toggle the appropriate bridge flags in the mixed faces of \(K_2\setminus K_1\) to obtain two descending-cardinality stages of ninety pairs each, proving \(K_2\searrow K_1\). All unique-center, face-partition, coface, and maximality claims are checked **against the complete current face sets** by the standalone program, rather than inferred from counts or a partial traversal.

Each of the twenty triangles in \(K_1\) can be collapsed along one free edge, producing a connected graph with sixty vertices and seventy edges. Its cycle rank is \(70-60+1=11\). Therefore all three lower stages have homotopy type \(\bigvee^{11}S^1\). Since the two relative collapses remove no face of the smaller stages, the indicated inclusions induce isomorphisms integrally on all homology groups.

**3. Exact fourth-stage homology.** Over \(\mathbb F_2\), the simplicial boundary of a \(k\)-simplex is the sum of its \(k+1\) codimension-one faces. Indexing all previously enumerated faces, the verifier represents boundary columns as integers with one bit per row and uses exact Gaussian elimination over \(\mathbb F_2\); the face lists include *all* 13,554 nonempty faces of \(K_4\). The ranks of the maps from chain degrees one through seven are, in order,

\[
59,\;571,\;1808,\;2422,\;1430,\;420,\;60.
\]

Combining these ranks with the face vector gives precisely \(\beta_2=2380-571-1808=1\) and \(\beta_4=3864-2422-1430=12\). Every other positive-degree Betti number vanishes; the graph is connected. The Euler-characteristic cross-check gives \(\chi(K_4)=14\), agreeing with \(1+1+12\). The calculation is finite and exhaustive and needs no extrapolation from sampled graphs.

**4. Filtration maps.** The collapse equivalences prove that the eleven integral degree-one generators from radius one persist through radius three. The computed \(\beta_1(K_4;\mathbb F_2)=0\) kills all their mod-two images at radius four. There is no homology in degrees two or four at earlier stages, so their respective one and twelve mod-two classes are born at four. No claim about their behavior at higher radii follows from these data.

## Verification
Run `python3 verify_truncated_dodecahedron.py` from the extracted files. The verifier uses the Python standard library only. It checks cubic degree, graph size and diameter, every Rips simplex through threshold four, the complete mod-two boundary ranks, the Euler characteristic, and the two explicit *elementary* relative collapses. Each purported lower face is checked to have exactly one surviving codimension-one coface, namely its paired upper face; the upper face is checked maximal before deletion. Every resulting face set is compared to its independently generated target. The saved actual terminal output ends with `VERIFY_TRUNCATED_DODECAHEDRON_RIPS_MOD2_PASS`. The finite computations prove the finite assertions, not any unclaimed all-graphs extension.

## Relationship to prior work
Saleh, Titz Mite and Witzel (first arXiv posting 2023-02-28, arXiv:2302.14388) classify the Rips complexes of the five **Platonic** solids and explicitly identify Archimedean solids as a potential extension; the truncated dodecahedron is not among their classified solids. Adamaszek (arXiv:1104.0433) develops clique complexes of graph powers and general structural criteria; the short three-cycles in the truncated graph preclude the direct high-girth stability criterion. Neither paper implies the radius-four rank pair calculated here.

Related accessible calculations establish the scale-two-to-three **intrinsic Čech**, not graph-metric Rips, persistence of \(L(S(H))\) for triangle-free \(H\). That general result is relevant to the early stages and is not claimed as a discovery here. Other published finite computations classify Rips complexes on the truncated cube and truncated octahedron, whose underlying graphs and face sets are different. The previously known graph-metric Rips results for the original dodecahedral graph also do not imply those of its sixty-vertex truncation. Targeted phrase, alias, parameter and stronger-coverage searches did not identify a covering radius-four result for the truncated dodecahedron.

## Limitations
The computation gives complete reduced homology of \(K_4\) **only over \(\mathbb F_2\)**. It does not determine integral torsion, the homotopy type at radius four, its equivariant automorphism action, or later deaths of the degree-two and degree-four classes. The complete filtration at scales above four is not computed. A previously unindexed equivalent calculation cannot be categorically excluded. The source-date attribution refers to the inspiring Platonic-solids paper, not to a publication of this new finite calculation.

## References
1. N. Saleh, T. Titz Mite and S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388, first public 2023-02-28. https://arxiv.org/abs/2302.14388
2. M. Adamaszek, *Clique complexes and graph powers*, arXiv:1104.0433, first public 2011-04-03. https://arxiv.org/abs/1104.0433
3. H. Adams, S. Shukla and A. Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871, first public 2022-12-12, as background on the distinct Čech filtration. https://arxiv.org/abs/2212.05871
4. *Scale-three Čech persistence survives vertex truncation of triangle-free graphs*, mathematical research record `050621e1a6fe`, accessed 2026-10-29, for the related Čech comparison.
5. *Complete graph-metric Vietoris–Rips filtration of the truncated octahedral graph*, mathematical research record `3b8391bcadb8`, accessed 2026-10-29, for a different Archimedean graph.
6. *A mixed-dimensional Rips wedge for the truncated cube*, mathematical research record `4fae71a21a80`, accessed 2026-10-29, for a different truncation.
