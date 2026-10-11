# Sphere-wedge topology of three-cut complexes of circular ladders

## Finding
For every integer \(n\ge5\), let \(G_n=C_n\mathbin{\square}K_2\), with vertices
\(a_i,b_i\) indexed by \(i\in\mathbb Z/n\mathbb Z\) and edges
\(a_i a_{i+1}\), \(b_i b_{i+1}\), and \(a_i b_i\).
Let \(\Delta_3(G_n)\) be the ordinary three-cut complex, defined to have as facets the complements of three-vertex subsets inducing disconnected subgraphs. Then
\[
\Delta_3(G_n)\simeq\bigvee^{2n^2-8n+1}S^{2n-4}.
\]
Consequently, \(\widetilde H_j(\Delta_3(G_n);\mathbb Z)\) is \(\mathbb Z^{2n^2-8n+1}\) for \(j=2n-4\) and zero otherwise. The assertion includes all \(n\ge5\), not just values enumerated computationally.

## Assumptions and scope
All graphs are finite and simple. Cyclic indices are taken modulo \(n\). The ordinary three-cut complex is **not** the total three-cut complex (the latter requires independent triples). Put \(N=2n\). Let \(K_n=\Delta_3(G_n)^\vee\) be the combinatorial Alexander dual. A subset \(F\subseteq V(G_n)\) is a face of \(K_n\) exactly when **every** three-element subset of \(F\) induces a connected graph. For \(|F|\le2\), this condition is vacuous.

## Proof
**1. Classification of dual faces.** The circular ladder for \(n\ge5\) is triangle-free and three-regular. Every connected induced triple is thus a path of length two. For each of \(2n\) centers there are \(\binom32=3\) such triples, giving exactly \(6n\) two-faces of \(K_n\). Its one-skeleton is complete. If every induced triple of a four-vertex set is connected, then the four induced triples each contain at least two edges. Every graph edge belongs to precisely two triples, so the induced four-vertex graph has at least four edges. Since it is triangle-free, it has at most four edges, with equality only for a four-cycle. Conversely, all triples in any four-cycle are connected. In \(C_n\mathbin{\square}K_2\) for \(n\ge5\), the only four-cycles are the \(n\) squares \(\{a_i,a_{i+1},b_i,b_{i+1}\}\). If a five-vertex set had every triple connected, all five of its four-subsets would be four-cycles. Counting the incidences of edges with four-subsets gives \(5\cdot4=3e\), where \(e\) is the number of edges on the five-set, impossible. No face has size five or more. Thus \(K_n\) has \(2n\) vertices, \(\binom{2n}{2}\) edges, \(6n\) triangles, and \(n\) tetrahedra, and no larger faces.

**2. The integral boundary rank and a saturated image.** Orient simplices by increasing vertex labels, or arbitrarily but consistently. Let \(\partial_2:C_2(K_n;\mathbb Z)\to C_1(K_n;\mathbb Z)\). The \(6n\) connected triples split into \(2n\) horizontal three-vertex paths and \(4n\) mixed paths, four belonging to each of the \(n\) squares. For each horizontal path, the edge joining its two end vertices is a distance-two chord in one of the two rings. When \(n\ge5\), that chord belongs to **no other** connected triple. The \(2n\) corresponding rows of \(\partial_2\) form a diagonal \(\pm1\) block on the \(2n\) horizontal-path columns and vanish on the mixed-path columns.

For a square in cyclic order \((A,B,C,D)=(a_i,a_{i+1},b_{i+1},b_i)\), take the three edge rows \(AC\), \(BD\), \(AB\) and the three triangle columns \(ABC\), \(BCD\), \(CDA\). Their oriented boundary matrix has determinant \(\pm1\): the first diagonal occurs only in columns \(ABC,CDA\), the second only in \(BCD\), and the top horizontal edge \(AB\) only in \(ABC\). The chosen diagonal rows occur in no other square's mixed triangles; the top-edge row \(AB\) also occurs in no other square's mixed triangles. Concatenate all \(n\) blocks with the \(2n\) chord rows and columns. Ordering horizontal-path columns first, the selected \(5n\)-square minor is block triangular with \(\pm1\) diagonal blocks, hence determinant \(\pm1\). Therefore \(\operatorname{rank}\partial_2\ge5n\), and its image is a primitive sublattice of \(C_1(K_n;\mathbb Z)\).

Each square contributes its entire tetrahedral boundary, a nonzero two-cycle in \(C_2(K_n;\mathbb Z)\). These \(n\) cycles are linearly independent because their mixed-path triangles are disjoint. Selecting one of their mixed-path triangles per square gives a signed identity minor in the square-boundary columns, so their span is primitive in \(C_2(K_n;\mathbb Z)\). It follows that \(\operatorname{rank}\partial_2\le6n-n=5n\). We conclude \(\operatorname{rank}\partial_2=5n\). Since the primitive span of the \(n\) square boundaries has the same rank as \(\ker\partial_2\), they generate the entire kernel integrally. Also, \(\operatorname{im}\partial_2\) is saturated. The \(n\) tetrahedra also have pairwise disjoint triangle supports, so \(\partial_3\) is injective and \(\operatorname{im}\partial_3=\ker\partial_2\). Thus \(H_2(K_n;\mathbb Z)=H_3(K_n;\mathbb Z)=0\).

**3. Integral homology.** The full one-skeleton is connected and has \(\operatorname{rank}\partial_1=2n-1\). Hence
\[
H_1(K_n;\mathbb Z)\cong\mathbb Z^{\binom{2n}{2}-(2n-1)-5n}
=\mathbb Z^{2n^2-8n+1}.
\]
The group is torsion-free because the image of \(\partial_2\) is primitive, while \(\ker\partial_1\) is itself primitive in \(C_1\). In particular, the reduced integral cohomology of \(K_n\) is concentrated in degree one, with the same rank, by the universal coefficient theorem.

**4. Passage to the three-cut complex.** Combinatorial Alexander duality, with the convention that the empty face belongs to a nonvoid complex, yields \(\widetilde H_i(\Delta_3(G_n);\mathbb Z)\cong\widetilde H^{2n-i-3}(K_n;\mathbb Z)\). Thus the only nonzero reduced integral homology of \(\Delta_3(G_n)\) is in degree \(2n-4\) and has rank \(2n^2-8n+1\). Because \(K_n\) has no faces of cardinality at least five, every set of at least five vertices of \(G_n\) contains a disconnected triple; equivalently, \(\Delta_3(G_n)\) contains the full \((2n-6)\)-skeleton of a \((2n-1)\)-simplex. It is therefore \((2n-7)\)-connected, in particular simply connected for \(n\ge5\). The integral homology vanishing in the next two degrees improves the connectivity to \((2n-5)\) by successive applications of Hurewicz. This finite complex has dimension exactly \(2n-4\), so the Hurewicz theorem followed by Whitehead's theorem identifies its homotopy type as the indicated wedge of \((2n-4)\)-spheres. This proves the claim for all \(n\ge5\).

## Verification
The standalone `VERIFY.py` rebuilds the circular ladder and its Alexander dual from graph adjacency, enumerates connected triples and four-cliques of the dual for \(5\le n\le9\), and checks the precise incidence rows used in the unimodular-minor argument. It independently calculates \(\partial_2\) and \(\partial_3\) ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\), checks the local integer determinants, and prints `VERIFY_OK`. The ranks are \((25,5),(30,6),(35,7),(40,8),(45,9)\) for \(n=5,6,7,8,9\). These finite checks are corroboration, **not** the proof for arbitrary \(n\); the preceding integer minor and duality arguments are uniform.

## Relationship to prior work
Bayer, Denker, Jelić Milutinović, Rowlands, Sundaram, and Xue (arXiv:2304.13675, initially public April 26, 2023) introduced and studied ordinary cut complexes, including cycles and prisms **over cliques** \(K_m\mathbin{\square}K_2\), not circular ladders \(C_n\mathbin{\square}K_2\). Chandrakar, Hazra, Rout, and Singh (arXiv:2408.07646) determined results for rectangular (nonperiodic) grids \(P_2\mathbin{\square}P_n\); adjoining two wraparound edges changes both the graph and its cut complex. Chauhan, Shukla, and Vinayak (arXiv:2512.04486, Conjecture 4.6(ii)) **already proposed precisely the integral homology ranks** displayed above, supported by the first few small cases in their Table 5. That prediction is **not claimed as an original conjecture** here. What is established beyond those published computations and that conjecture is a proof for all \(n\ge5\), integral torsion exclusion, and a sphere-wedge homotopy classification.

## Limitations
The theorem does not cover \(n=4\), where distance-two chords are shared and a distinct homology pattern occurs. The proof treats the ordinary three-cut complex only; no assertion about total cut complexes, higher cut parameters, group representations, or shellability is made. The cited comparison distinguishes explicitly conjectured homology from a proven homotopy theorem, but uncatalogued subsequent results may require further literature comparison.

## References
- M. Bayer, M. Denker, M. Jelić Milutinović, R. Rowlands, S. Sundaram, and L. Xue, *Topology of Cut Complexes of Graphs*, arXiv:2304.13675 (first public 2023-04-26), https://arxiv.org/abs/2304.13675 .
- H. Chandrakar, N. R. Hazra, D. Rout, and A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646 (first public 2024-08-14), https://arxiv.org/abs/2408.07646 .
- P. Chauhan, S. Shukla, and K. Vinayak, *Total 2-cut complexes of powers of cycle graphs and Cartesian products of certain graphs*, arXiv:2512.04486 (first public 2025-12-04), especially Conjecture 4.6(ii) and Table 5, https://arxiv.org/abs/2512.04486 .
