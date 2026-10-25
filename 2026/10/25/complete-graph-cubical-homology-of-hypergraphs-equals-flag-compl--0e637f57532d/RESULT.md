# Complete-graph cubical homology of hypergraphs equals flag-complex homology

## Finding

Let \(H=(V,E)\) be a nonempty finite hypergraph, with every vertex in at least one hyperedge. Form its **two-section graph** \(G_H\): distinct vertices are adjacent precisely when they occur together in a hyperedge. Let \(K_H=\operatorname{Cl}(G_H)\) be the flag (clique) simplicial complex, whose simplices are all nonempty cliques.

For the normalized integral \(\times\)-cubical homology defined in Zaidi--Jamil [1], in which the \(n\)-dimensional test hypercube is the complete graph on \(\{0,1\}^n\), there are isomorphisms in **every** homological degree \(q\geq0\):

\[
H_q^{\times}(H;\mathbb Z)\cong H_q(K_H;\mathbb Z).
\]

A fixed ordering of \(V\) supplies an explicit integral chain quasi-isomorphism, and the comparison is compatible with inclusions and filtrations using the same vertex ordering. Consequently this cubical theory cannot distinguish finite hypergraphs with the same two-section graph, even when their higher hyperedges differ. The result is an all-degree identification, not merely an agreement of Betti numbers or a low-degree comparison.

## Assumptions and scope

All vertex sets and hyperedge collections are finite. The one-hyperedge-per-vertex coverage hypothesis excludes vertices without a valid singular zero-cube under [1]. The theory uses the complete-graph test cubes \(J_n^{\times}\) and the normalized integral boundary of [1, Section 3.1], **not** the Cartesian-cube discrete cubical graph theory. The target simplicial homology is unreduced integral homology. No regularity, uniformity, or connectivity assumption is imposed.

A normalized singular \(n\)-cube is a hypergraph morphism \(f:J_n^{\times}\to H\) modulo those constant in at least one coordinate. The differential has the sign convention

\[
\partial f=\sum_{i=1}^n(-1)^i\bigl(A_i f-B_i f\bigr),
\]

where \(A_i\) (respectively \(B_i\)) restricts the \(i\)-th coordinate to zero (respectively one). For \(n=0\), its generators are the vertices of \(H\).

## Proof

**1. Exact cube identification.** Because \(J_n^{\times}\) is the complete graph on all \(2^n\) Boolean vertices, a map \(f:\{0,1\}^n\to V\) is a hypergraph morphism precisely when each distinct pair of elements of its image lies together in some hyperedge of \(H\). Repetitions pose no obstacle because every vertex lies in a hyperedge. Thus \(\operatorname{im}f\) is a simplex of \(K_H\), and conversely any cube whose image is a simplex of \(K_H\) is a permitted singular \(\times\)-cube. The normalized chain complex \(C_*^{\times}(H;\mathbb Z)\) is therefore exactly the complex \(T_*(K_H)\) freely generated in degree \(n\) by coordinate-nondegenerate maps from \(\{0,1\}^n\) into individual simplices of \(K_H\), with the displayed boundary.

**2. Explicit comparison chain map.** Give \(V\) a total ordering. For an increasing oriented \(n\)-simplex \([v_0,\ldots,v_n]\), define the corner cube \(c_n(v_0,\ldots,v_n)\) by

\[
c_n(\varepsilon_1,\ldots,\varepsilon_n)=
\begin{cases}v_0,&\text{if all }\varepsilon_i=0,\\
v_j,&j=\max\{i:\varepsilon_i=1\},\text{ otherwise}.
\end{cases}
\]

This is nondegenerate for distinct vertices. Let \(\eta_n\) send the increasing simplex to this normalized cube, extended linearly. On restricting coordinate \(i\) to zero, one gets the corner cube with \(v_i\) omitted. Restricting coordinate one to one gives the corner cube \(c_{n-1}(v_1,\ldots,v_n)\). For every \(i\ge2\), restricting the \(i\)-th coordinate to one instead yields a cube independent of coordinate \(i-1\), hence zero after normalization. Accordingly

\[
\partial c_n(v_0,\ldots,v_n)
=\sum_{j=0}^n(-1)^j c_{n-1}(v_0,\ldots,\widehat v_j,\ldots,v_n),
\]

so \(\eta_*:C_*^{\mathrm{simp}}(K_H;\mathbb Z)\to T_*(K_H)\) is a chain map. The degree-zero map is the identity on vertices.

**3. Contractibility on each simplex.** If \(\Delta\) is a full simplex and \(w\) one of its vertices, extend every permitted cube \(f:\{0,1\}^n\to\Delta\) to \(P_nf:\{0,1\}^{n+1}\to\Delta\) by \(P_nf(\varepsilon,0)=f(\varepsilon)\) and \(P_nf(\varepsilon,1)=w\). All these cubes remain admissible because their images lie in a single simplex. This construction preserves degenerate cubes, hence descends to normalized chains. Put \(h_n=(-1)^{n+1}P_n\). Directly separating the last-coordinate faces gives

\[
\partial h_n+h_{n-1}\partial=\operatorname{id}
\]

in every positive degree, and \(\partial h_0=\operatorname{id}-\iota_w\epsilon\) in degree zero, where \(\epsilon\) is the augmentation and \(\iota_w\) selects the chosen vertex. Thus \(H_0(T_*(\Delta))=\mathbb Z\) and \(H_q(T_*(\Delta))=0\) for \(q>0\). The ordinary simplicial simplex chains have the same homology, and \(\eta\) induces the identity on \(H_0\). Therefore \(\eta\) is a quasi-isomorphism on every full simplex.

**4. Gluing without rationalization.** For finite simplicial subcomplexes \(A,B\) with \(K=A\cup B\), any permissible normalized cube has an image that is a simplex of \(A\) or of \(B\); the intersection of their sets of basis cubes consists exactly of the cubes supported in \(A\cap B\). Hence there is a degreewise split short exact sequence of integral chain complexes

\[
0\longrightarrow T_*(A\cap B)\longrightarrow T_*(A)\oplus T_*(B)
\longrightarrow T_*(K)\longrightarrow0.
\]

The same sequence holds for ordinary simplicial chains, and the maps \(\eta\) commute with all inclusions as long as the vertex order is fixed. Induct over the number of nonempty simplices of a finite complex: when the complex is not a full simplex, choose a maximal simplex \(\sigma\) and decompose \(K=A\cup\sigma\), with \(A\) obtained by deleting the maximal face alone and \(A\cap\sigma=\partial\sigma\). All three smaller complexes satisfy the comparison by induction; the full-simplex case was established in step 3. The long exact homology sequences and the five lemma show that \(\eta_*\) is a quasi-isomorphism for \(K\). If \(\sigma\) is a lone vertex, the boundary complex is empty, whose unaugmented chains vanish on both sides, so the argument still applies. No field-coefficient, rank, or finite-size restriction appears.

The claimed isomorphism follows from steps 1--4 for every \(q\ge0\), and compatibility with ordered inclusions follows already at the chain level.

## Verification

The self-contained Python 3 standard-library program `verify.py` exhaustively constructs normalized complete-graph cubes through dimension three for six small flag complexes, tests every permitted cubical face, checks the corner-cube simplicial chain-map identity and explicit simplex cone contraction, and compares mod-two homology in degrees zero and one. It inspected 20,874 normalized cubes and 41 simplices across the tests; it returned `VERIFY_OK`. The proof is integral, covers arbitrary dimensions and complexes, and does not extrapolate from these finite experiments. Reproduce using `python3 verify.py`.

## Relationship to prior work

Zaidi and Jamil [1, Sections 3 and 5] introduce \(\Gamma\)-, Cartesian \(\Box\)-, and complete-graph \(\times\)-cubical theories, their examples, and an excision theorem for \(\times\)-homology. Their displayed definitions are used verbatim here; the resulting all-degree identification with a two-section flag complex is not stated in the inspected paper. The paper's four-cycle calculation is consistent with the comparison. The cubical digital-graph homologies compared by Staecker [2] use a different cube adjacency and are explicitly known not to coincide with clique-complex simplicial homology in general. The present argument relies on the **complete** graph test cube, not that Cartesian adjacency. See also Barcelo and collaborators [3] for the distinct discrete cubical homology of ordinary graphs.

## Limitations

This is a statement about the complete-graph \(\times\)-cubical construction only; it asserts nothing analogous for the other two theories. It does not establish a homotopy equivalence between any spaces naturally realizing the entire cubical object, only an integral chain quasi-isomorphism. The comparison map explicitly depends on a vertex ordering; the asserted filtration compatibility is for a common ordering, not a claim of strict naturality under arbitrary vertex maps. The included computational sample is finite and not a substitute for the symbolic proof. Despite searches, an exhaustive international priority search and independent mathematical audit have not been performed.

## References

[1] S. H. A. Zaidi and S. S. Jamil, *A cubical approach to homology theories for hypergraphs*, arXiv:2610.08196v1, publicly submitted 2026-10-06, especially Sections 2--3 and 5. https://arxiv.org/abs/2610.08196

[2] P. C. Staecker, *The two digital homology theories*, arXiv:1907.00473 (2019); and *Digital homotopy relations and digital homology theories*, Applied General Topology 22 (2021), 223--250. https://arxiv.org/abs/1907.00473

[3] H. Barcelo, C. Greene, A. S. Jarrah, and V. Welker, *Discrete cubical and path homologies of graphs*, Algebraic Combinatorics 2 (2019), 417--437. https://doi.org/10.5802/alco.49
