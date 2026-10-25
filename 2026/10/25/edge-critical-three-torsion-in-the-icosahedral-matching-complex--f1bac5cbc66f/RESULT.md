# Edge-critical three-torsion in the icosahedral matching complex

## Finding
Let \(I\) be the twelve-vertex icosahedral graph, let \(e=\{u,v\}\) be **any** of its thirty edges, and let \(\mathcal M(G)\) be the ordinary matching complex of a graph \(G\). Then the integral homotopy types of the graph-edge deletion and link are
\[
\mathcal M(I-e)\simeq\bigvee^{68}S^3,\qquad
\mathcal M(I-\{u,v\})\simeq\bigvee^{2}S^2\vee\bigvee^{6}S^3.
\]
The full graph has \(\mathcal M(I)\simeq(\bigvee^{64}S^3)\vee M(\mathbb Z/3,3)\). In the graph-edge deletion cofibration, its integral connecting map
\[
\delta:H_3(\mathcal M(I-\{u,v\});\mathbb Z)\longrightarrow
 H_3(\mathcal M(I-e);\mathbb Z)
\]
is injective, with image a rank-six sublattice whose saturation has index **three**. Thus the three-torsion present in \(H_3(\mathcal M(I);\mathbb Z)\) disappears upon deleting *any single graph edge*, and the nonprimitive connecting image pinpoints where that torsion arises.

## Assumptions and scope
The graph is fixed as follows, with \(i\in\mathbb Z/5\mathbb Z\), \(u_i=1+i\), \(v_i=6+i\) and apices \(0,11\). Its edges are precisely
\[
\{0u_i,\ 11v_i,\ u_i u_{i+1},\ v_i v_{i+1},\ u_i v_i,\ u_i v_{i-1}: i\in\mathbb Z/5\mathbb Z\}.
\]
Graph-edge deletion \(I-e\) keeps all twelve graph vertices; \(I-\{u,v\}\) deletes the two endpoints and incident edges. The matching complex has graph edges as vertices and collections of pairwise endpoint-disjoint edges as faces. We use integral homotopy types, not merely mod-prime homology. The source of the graph and the public date of the prior matching-complex literature appear below.

## Proof
**Symmetry reduction.** The given graph has thirty edges and twelve degree-five vertices; its twenty triangles produce a triangulation of a two-sphere. The reproducible code enumerates the 120 adjacency-preserving vertex permutations exhaustively and confirms that the orbit of graph edge \(\{0,1\}\) contains all thirty graph edges. The types of \(I-e\), \(I-\{u,v\}\), and the connecting-map saturation index are consequently independent of the choice of \(e\).

**Exhaustive acyclic discrete-Morse reduction.** For each of the three finite graphs (whole, deletion, and endpoint removal), generate every matching simplex. Order graph edges lexicographically. At each pivot, pair any as-yet unpaired simplex \(\sigma\) that does not contain that pivot with \(\sigma\cup\{\mathrm{pivot}\}\), when both remain unpaired. This is a concrete complete matching on the nonempty face poset. Reverse every paired Hasse incidence and orient all unpaired codimension-one incidences downward. Full topological sorting of these explicitly enumerated finite directed graphs verifies **acyclicity** without extrapolation. The face vectors (dimensions beginning with zero), number of matched pairs, and critical-cell counts (dimensions zero through five) are:

| Graph | Face vector | Pairs | Critical cells |
|---|---|---:|---|
| \(I\) | \((30,315,1400,2535,1482,125)\) | 2850 | \((1,0,0,125,61,0)\) |
| \(I-e\) | \((29,294,1260,2197,1235,100)\) | 2495 | \((1,0,0,96,28,0)\) |
| \(I-\{u,v\}\) | \((21,140,338,247,25)\) | 374 | \((1,0,9,13,0,0)\) |

**Integral attaching degrees.** The script `verify_icosa_edge_profile.py` recursively substitutes each paired lower cell by signed facets of its paired upper cell; acyclicity makes this well-founded. Its oriented Morse matrices are \(125\times61\) (full), \(96\times28\) (deletion), and \(9\times13\) (link). Their rational ranks are \(61,28,7\), respectively. Exact fraction-free integer determinant computations provide a \(61\times61\) minor of absolute determinant \(3\) for the whole complex, a \(28\times28\) minor of determinant \(1\) for deletion, and a \(7\times7\) minor of determinant \(-1\) for the link. The full matrix has rank \(60\) over \(\mathbb F_3\): all its maximal minors are divisible by three; its displayed determinant shows their gcd is exactly three. Thus the full matrix has Smith invariants sixty units and one factor three. The other matrices' unit maximal minors establish that every nonzero invariant factor is one.

Since each critical CW complex has exactly one zero-cell and critical cells in two consecutive degrees \(d,d+1\), with \(d\ge2\), the degree matrix completely determines its homotopy type: \(\pi_d(\bigvee S^d)\cong\mathbb Z^r\), and unimodular basis changes correspond to homotopy equivalences of wedges of spheres. The resulting reduced forms give \(\bigvee^{64}S^3\vee M(\mathbb Z/3,3)\), \(\bigvee^{68}S^3\), and \(\bigvee^2S^2\vee\bigvee^6S^3\), respectively.

**Nonprimitive connecting map.** The vertex-deletion decomposition of a matching complex at the vertex corresponding to graph edge \(e\) gives a homotopy cofibration
\[
\mathcal M(I-e)\longrightarrow\mathcal M(I)\longrightarrow
 \Sigma\mathcal M(I-\{u,v\}).
\]
Its reduced integral homology long exact sequence, combined with the just-proved homotopy types, contains
\[
0\to\mathbb Z^6\xrightarrow{\delta}\mathbb Z^{68}
\to\mathbb Z^{64}\oplus\mathbb Z/3\to\mathbb Z^2\to0.
\]
Here \(H_4(\mathcal M(I))=0\) proves injectivity of \(\delta\). The quotient \(\mathbb Z^{68}/\operatorname{im}\delta\) is the kernel of the surjection \(\mathbb Z^{64}\oplus\mathbb Z/3\to\mathbb Z^2\), which contains the entire \(\mathbb Z/3\) torsion subgroup and no other torsion. Therefore the saturation index of \(\operatorname{im}\delta\) is exactly three. The argument determines the image's index, not a preferred integral basis for the connecting homomorphism.

## Verification
Run `python3 verify_icosa_edge_profile.py` in a directory containing only the supplied verifier. It uses the Python 3 standard library, regenerates the three graphs and their face posets, checks Hasse incidence counts and topological sorting, constructs oriented Morse matrices, verifies their ranks and exact determinant minors, and enumerates all automorphisms. The printed `MINOR_CERTIFICATE` lines give reproducible row and column selections, with determinant values \(-3,1,-1\). The embedded `verify_icosa_edge_profile.out` is an actual successful run whose last line is `VERIFY_OK_ICOSAHEDRAL_EDGE_TORSION_PROFILE`. The proof is a complete finite calculation supplemented by the general discrete-Morse and cofiber theorems; finite testing is sufficient here because the mathematical objects have finite, fixed size and all cases are covered by transitivity.

## Relationship to prior work
The published result *Three-torsion in the icosahedral matching complex: a planar counterexample* already proves the whole-complex wedge-plus-Moore homotopy type. That prior discovery is acknowledged, not reclaimed. The present finding newly identifies the homotopy types **after each single graph-edge deletion**, the endpoint-deletion links, and the exact index-three obstruction to splitting the deletion–link cofibration. Shareshian and Wachs establish three-torsion in classical complete-graph matching and chessboard complexes, not this edge-critical phenomenon. Bayer, Jelić Milutinović and Vega prove that **outerplanar** graphs have sphere-wedge matching complexes; the graph \(I-e\), with twelve vertices and twenty-nine edges, is not outerplanar (an outerplanar simple twelve-vertex graph has at most twenty-one edges). Their theorem does not imply this example. Related published edge-deletion splittings for the Franklin and rhombic-dodecahedral graphs concern torsion-free parents and do not imply the nonprimitive index here.

## Limitations
The assertion is for this icosahedral graph and single-edge deletions only. It does not prove edge-minimality among **all** planar graphs with torsion or determine all multi-edge deletions. The connecting-map calculation identifies its image's saturation index but gives no canonical bases or equivariant integral splitting. All computation and the associated source code must be trusted to implement the explicitly specified finite graph and Morse procedure; a formal proof assistant or independent human audit has not been used. An equivalent computation in unindexed graph-complex catalogues cannot be ruled out.

## References
1. J. Shareshian and M. L. Wachs, *Torsion in the Matching Complex and Chessboard Complex*, arXiv:math/0409054 (first public 2004-09-03), https://arxiv.org/abs/math/0409054.
2. A. Engström, *Independence complexes of claw-free graphs*, arXiv:math/0512420 (first public 2005-12-17), https://arxiv.org/abs/math/0512420.
3. M. Bayer, M. Jelić Milutinović and J. Vega, *Matching Complexes of Outerplanar Graphs*, arXiv:2411.04601 (first public 2024-11-07), https://arxiv.org/abs/2411.04601.
4. *Three-torsion in the icosahedral matching complex: a planar counterexample*, public scientific record (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-three-torsion-in-the-icosahedral-matching-complex-a-planar-count--28565ad1ea1a.
