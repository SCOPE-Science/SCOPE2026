# Radius-three Rips homology of girth-eight bipartite graphs and generalized quadrangles

## Finding
Let \(G\) be a finite connected simple bipartite graph of diameter at most \(4\) and girth at least \(8\), with the convention that an acyclic graph has infinite girth. Put \(b=|E(G)|-|V(G)|+1\). Give its vertices the unweighted shortest-path metric, and define the inclusive Vietoris–Rips complex using pairwise distances at most \(r\). For every real \(3\le r<4\),
\[
\operatorname{VR}_{\le r}(G)\simeq\bigvee^{b^2}S^3.
\]
Here a zero-fold wedge means a contractible space. In particular its reduced integral homology is free and concentrated in degree \(3\), with rank \(b^2\).

More precisely, write \(V(G)=P\sqcup L\), and put \(M=H_1(G;\mathbb Z)\). The natural type-preserving graph automorphism group acts on the integral third homology as the diagonal tensor square
\[
\widetilde H_3(\operatorname{VR}_{\le3}(G);\mathbb Z)\cong M\otimes_{\mathbb Z}M.
\]
For a graph automorphism exchanging \(P\) and \(L\), the action in this identification is its induced action on both factors followed by tensor-factor interchange, **without** a negative interchange sign. If \(b>0\), a nonzero rational third-homology class is fixed by the **entire** finite graph automorphism group. Consequently
\[
\dim_{\mathbb Q}H_3\bigl(\operatorname{VR}_{\le3}(G)/\operatorname{Aut}(G);\mathbb Q\bigr)\ge1.
\]

For the point–line incidence graph of any finite generalized quadrangle of order \((s,t)\), with \(s,t\ge2\), the graph has diameter \(4\), girth \(8\), and \(b=s^2t^2\). Thus its radius-three Rips complex is a wedge of \(s^4t^4\) three-spheres and its full-automorphism quotient has nonzero rational third homology. This includes nonclassical generalized quadrangles whenever they exist.

## Assumptions and scope
All graphs are finite, connected, unweighted, simple and bipartite. The girth hypothesis rules out four-cycles and six-cycles; the diameter hypothesis means all point–line pairs have graph distance \(1\) or \(3\). A *generalized quadrangle of order* \((s,t)\) has \(s+1\) points per line, \(t+1\) lines per point, and its point–line incidence graph has diameter \(4\) and girth \(8\). The finite-thickness assumption \(s,t\ge2\) ensures positive cycle rank. No existence is asserted for unsupported parameter pairs. The stated automorphism action applies to graph automorphisms, including possible exchanges of the two bipartition classes; no assumption that all graph automorphisms arise from collineations is needed.

## Proof
The one-vertex graph is a degenerate case: its Vietoris–Rips complex is a point, its cycle rank is zero, and its reduced homology and quotient statements are immediate. In the following six steps assume \(G\) has at least one edge, so both color classes and the neighborhood simplices are nonempty.

**1. The threshold graph is a complete join between its colors.** Distinct vertices in the same bipartition class have even distance, hence distance \(2\) or \(4\); point–line pairs have odd distance, hence distance \(1\) or \(3\). Let \(A\) be the clique complex on \(P\), joining two distinct points exactly when they have a common neighbor in \(L\); let \(B\) be the corresponding clique complex on \(L\). Every cross-color pair has distance at most \(3\), so the threshold-three clique complex is **literally** the simplicial join \(A*B\).

**2. Cliques on one color have a unique opposite-color common neighbor.** In a bipartite graph without four-cycles, two vertices on one side have at most one common neighbor. If three are pairwise distance two but have three distinct pairwise common neighbors, these vertices and neighbors would form a six-cycle; if two pairwise common neighbors agree, uniqueness forces the third to agree as well. Thus every pairwise distance-two triple shares a neighbor. For any larger clique, fixing one pair and applying this triple property to every other vertex shows that the entire clique shares its unique opposite-color neighbor. Therefore \(A\) is the union of the full simplices \(\Delta(N(\ell))\), for \(\ell\in L\), with any two of these simplices intersecting in at most a vertex. A dual statement holds for \(B\).

**3. Each factor has the homotopy type of the incidence graph.** Attach to \(A\), for every \(\ell\in L\), the cone \(\ell*\Delta(N(\ell))\), introducing the new apex \(\ell\). Each attachment is along a nonempty contractible simplex, so the inclusion of \(A\) into the resulting complex \(Y_A\) is a homotopy equivalence. In \(Y_A\), for each \(\ell\) and every face \(\sigma\subseteq N(\ell)\) of at least two points, pair \(\sigma\) with \(\sigma\cup\{\ell\}\), removing pairs in descending order of face size. No face \(\sigma\) of size at least two belongs to two opposite-neighbor simplices, by the absence of four-cycles. Thus all pairings are legal elementary collapses and leave exactly the point vertices, line-apex vertices, and point–line incidence edges: the original graph \(G\). The constructions are natural for color-preserving graph automorphisms. Consequently \(A\simeq G\) and, dually, \(B\simeq G\), and the induced integral first-homology identifications are compatible with graph symmetries. If an automorphism exchanges the colors, it exchanges these two constructions.

**4. The integral homotopy type and action.** A connected finite graph of cycle rank \(b\) is homotopy equivalent to a wedge of \(b\) circles. Both \(A\) and \(B\) are connected, so
\[
A*B\simeq\Sigma(A\wedge B)\simeq\bigvee^{b^2}S^3.
\]
The integral reduced homology Künneth isomorphism for a join identifies \(\widetilde H_3(A*B;\mathbb Z)\) with \(H_1(A;\mathbb Z)\otimes H_1(B;\mathbb Z)\). There are no torsion terms. The orientation convention for interchanging a degree-\(p\) join cycle with a degree-\(q\) join cycle gives sign \((-1)^{(p+1)(q+1)}\). Here \(p=q=1\), so this sign is positive. Hence type-exchanging automorphisms use the ordinary tensor flip, followed or preceded by the induced same graph automorphism on both factors.

**5. A homology class survives all finite symmetries.** Regard \(M_{\mathbb Q}=H_1(G;\mathbb Q)\) as the kernel of the cellular boundary \(\partial:\mathbb Q^{E(G)}\to\mathbb Q^{V(G)}\), with edges assigned arbitrary orientations and the standard orthonormal edge basis. Every graph automorphism acts on the edge space by a signed permutation matrix, preserving \(M_{\mathbb Q}\) and its orthogonal projection \(\pi\). Therefore
\[
C=\sum_{e\in E(G)}\pi(e)\otimes\pi(e)\in M_{\mathbb Q}\otimes M_{\mathbb Q}
\]
is nonzero when \(b>0\) and invariant under all diagonal graph actions. It is symmetric under tensor interchange, hence fixed also by every color-exchanging automorphism. Because the action is simplicial and finite, rational homology of its orbit-space quotient is the invariant subspace (equivalently use a barycentric subdivision and rational averaging). The class represented by \(C\) proves the asserted nonvanishing.

**6. The generalized-quadrangle count.** A quadrangle of order \((s,t)\) has \((s+1)(st+1)\) points, \((t+1)(st+1)\) lines, and \((s+1)(t+1)(st+1)\) incidences. Hence
\[
 b=(st+1)\bigl((s+1)(t+1)-(s+1)-(t+1)\bigr)+1=s^2t^2.
\]
Substituting into the general result gives the displayed \(s^4t^4\) three-spheres.

## Verification
The standalone standard-library script `check_gq_rips.py` reconstructs the eight-cycle and the order-\((2,2)\) generalized-quadrangle incidence graph in its duad–syntheme model. It verifies every pairwise distance, common-neighbor hypothesis and size of each join factor, enumerates every simplex at radius \(3\), and performs exact mod-two boundary elimination. The eight-cycle gives \((b,\beta_3)=(1,1)\). For the order-\((2,2)\) quadrangle, \(b=16\), each factor has face counts \((15,45,15)\), the full Rips complex has face vector \((30,315,1380,2475,1350,225)\), and its mod-two Betti vector is \((1,0,0,256,0,0)\). An independent enumeration of all \(720\) label-permutation automorphisms checks the integral graph-cycle character formula and finds invariant multiplicity one for its tensor square. These are finite corroborations; the proof above, not an extrapolation, establishes the universal integral and automorphism statements.

## Relationship to prior work
The literature on Rips complexes of graph metrics and graph powers supplies the starting point, in particular Adamaszek and collaborators' metric-gluing theorem (2017 preprint, 2018 proceedings), Saleh–Titz Mite–Witzel's Platonic-solid computations (2023), and Feng's hypercube graph computations (2023). These concern different graph families and do not establish the diameter-four/girth-eight join characterization.

A published result on the scale-three Rips complex of the 30-vertex Tutte–Coxeter graph establishes the single order-\((2,2)\) case with \(256\) three-spheres. A separate published calculation identifies its natural \(S_6\)-homology character as a tensor square. Those findings are contained as *special cases* of the present theorem, and therefore are not claimed anew; their exact statements do not imply the uniform result for all finite generalized quadrangles, its integral module for every graph in the stated class, or the surviving class under the **full** graph automorphism group. Previously published scale-two projective-plane and affine-plane incidence results use different incidence geometries and thresholds. McCabe's 2026 generalized-polygon girth-stability statement applies at threshold \(2\) for girth \(8\), not at threshold \(3\). The general family theorem is the contribution.

## Limitations
This is not a computation of the full persistence barcode or the scale-two topology. The full quotient's rational third Betti number is shown to be at least one, not determined exactly for arbitrary graphs. No assertion is made about arbitrary graphs with shorter girth or larger diameter, integral homology of the orbit-space quotient, or the existence of any particular generalized quadrangle. The source comparison cannot exclude an unindexed equivalence or an unknown more general theorem; an accessible excerpt of the 2026 approximation paper was not substituted for its entire text.

## References
- M. Adamaszek et al., *On Homotopy Types of Vietoris-Rips Complexes of Metric Gluings*, arXiv:1712.06224 (first public 2017-12-18); proceedings version, *Vietoris-Rips and Čech Complexes of Metric Gluings*, SoCG 2018, DOI:10.4230/LIPIcs.SoCG.2018.3.
- N. Saleh, T. Titz Mite, S. Witzel, *Vietoris–Rips complexes of Platonic solids*, arXiv:2302.14388 (first public 2023-02-28).
- Z. Feng, *Homotopy types of Vietoris-Rips complexes of Hypercube Graphs*, arXiv:2305.07084 (first public 2023-05-11).
- K. McCabe, *Lower Bounds for Approximating the Vietoris-Rips Filtration*, arXiv:2607.06524 (2026), compared only in accessible material.
- *The scale-three Rips complex of the Tutte–Coxeter graph is a wedge of 256 three-spheres*, public mathematical record (2026), inspected in full.
- *The natural S6-homology representation of the scale-three Tutte–Coxeter Vietoris–Rips complex*, public mathematical record (2026), inspected in full.
- *Scale-two Vietoris–Rips complexes of finite projective-plane incidence graphs*, public mathematical record (2026), inspected in full.
