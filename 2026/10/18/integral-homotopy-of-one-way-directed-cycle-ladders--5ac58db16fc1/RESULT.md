# Integral homotopy of one-way directed cycle ladders

## Finding

For every integer \(n\ge 3\) and every bijection \(\phi:\mathbb Z/n\to\mathbb Z/n\), form the directed graph \(D_{n,\phi}\) from two vertex-disjoint, coherently oriented \(n\)-cycles and a perfect matching of arcs pointing **only from the first cycle to the second**. Its multipath simplicial complex satisfies

\[
\mathcal X(D_{n,\phi})\simeq S^{n-1}\vee S^{2n-3}.
\]

Both sphere summands occur once. In particular, the reduced integral homology is infinite cyclic in degrees \(n-1\) and \(2n-3\) and zero in every other degree; no torsion occurs. The simplicial isomorphism type is independent of the matching permutation \(\phi\). The complex has exactly \(5^n-2^{n+1}+1\) faces when the empty face is included.

An example is a coherently oriented pentagonal prism with outward-to-inward spokes, or an analogously oriented Petersen graph \(GP(5,2)\); in either case the multipath complex is \(S^4\vee S^7\).

## Assumptions and scope

All complexes are finite and considered by geometric realization. Let the vertices be \(a_i,b_j\), indexed by \(\mathbb Z/n\). The directed arcs are

\[
a_i\longrightarrow a_{i+1},\qquad b_j\longrightarrow b_{j+1},\qquad a_i\longrightarrow b_{\phi(i)}.
\]

The edges of the digraph, rather than the graph vertices, are the vertices of \(\mathcal X(D_{n,\phi})\). A set of arcs is a face precisely when its spanning directed subgraph is a disjoint union of directed paths and isolated vertices. Thus every vertex has selected indegree and outdegree at most one and the selected arcs form no directed cycle.

The two rim orientations must be coherent and both sets of spokes must be directed from the outer to the inner rim; no classification is asserted for bidirected rungs or arbitrary orientations. The result allows any permutation of the spoke endpoints. For an inner rim originally specified with a step coprime to \(n\), reindex that rim along its oriented cycle to obtain the displayed model.

## Proof

Write \(o_i=(a_i,a_{i+1})\), \(s_i=(a_i,b_{\phi(i)})\), and \(t_i=(b_{\phi(i)-1},b_{\phi(i)})\). As \(\phi\) is a permutation, the \(t_i\) enumerate all inner rim arcs. Denote the two collections of rim arcs by \(O=\{o_i\}\) and \(T=\{t_i\}\).

**Step 1: an exact face description.** Since no spoke points from the inner rim back to the outer rim, every directed cycle in a selected subgraph with indegree/outdegree at most one is an entire outer or inner rim. The only local conflicts involving a spoke are \(s_i\) with \(o_i\) (shared tail) and \(s_i\) with \(t_i\) (shared head). Thus, prior to forbidding the two complete rims, an arc set is a face of the join

\[
J=\bigast_{i\in\mathbb Z/n}\bigl(\Delta\{o_i,t_i\}\sqcup\{s_i\}\bigr).
\]

In each factor, the five allowed subsets are \(\varnothing,\{o_i\},\{t_i\},\{o_i,t_i\},\{s_i\}\). The desired complex \(X=\mathcal X(D_{n,\phi})\) consists of precisely those faces of \(J\) which omit at least one \(o_i\) and at least one \(t_i\). The complete outer rim is contained in exactly \(2^n\) faces of \(J\) (each inner arc optional); the same holds for the complete inner rim, with overlap one. Inclusion–exclusion yields exactly \(5^n-2^{n+1}+1\) faces, counting the empty face.

**Step 2: cover by two explicit subcomplexes.** Let \(L\subset X\) consist of faces involving only rim arcs. The exclusion of the two complete rims gives

\[
L=\partial\Delta(O)*\partial\Delta(T)\cong S^{2n-3}.
\]

For each \(i\), let \(W_i=\operatorname{st}_X(s_i)\) be the **closed simplicial star** of the spoke vertex. Put \(W=\bigcup_i W_i\). Every face with at least one spoke belongs to some \(W_i\); hence \(X=L\cup W\). For each nonempty index set \(I\), \(\bigcap_{i\in I}W_i\) is the closed star of the simplex of spokes indexed by \(I\): the spokes do not conflict with each other and no directed cycle can involve them. This intersection is contractible. Consequently, the nerve of the star cover is a full \((n-1)\)-simplex, so \(W\) is contractible by the nerve lemma for subcomplex covers.

**Step 3: identify the overlap.** A rim-only face extends by spoke \(s_i\) exactly when it contains neither \(o_i\) nor \(t_i\). Thus

\[
B:=L\cap W
=\bigcup_{i\in\mathbb Z/n}\Delta\bigl((O\cup T)\setminus\{o_i,t_i\}\bigr).
\]

Intersections of any proper nonempty family of these \(n\) covering simplices are nonempty simplices, because some rim-pair \(\{o_j,t_j\}\) remains available. The intersection of all \(n\) is geometrically empty. Their nerve is \(\partial\Delta^{n-1}\), so another application of the nerve lemma yields

\[
B\simeq S^{n-2}.
\]

**Step 4: homotopy pushout.** All intersections and inclusions are inclusions of simplicial subcomplexes, hence cofibrations. The gluing square \(B\to L\), \(B\to W\) is a homotopy pushout. As \(W\) is contractible, \(X\) is homotopy equivalent to the homotopy cofiber of \(B\to L\). This map is null-homotopic: \(B\simeq S^{n-2}\), whereas \(L\cong S^{2n-3}\), and \(n-2<2n-3\) for all \(n\ge3\). Therefore

\[
X\simeq L\vee\Sigma B\simeq S^{2n-3}\vee S^{n-1}.
\]

This proves the claimed integral homotopy type without inference from finite enumeration. The relabeling \(t_i\) shows the same canonical local face description for every \(\phi\), yielding the matching-permutation independence.

## Verification

The standalone, standard-Python script `verify_multipath.py` checks the exact face criterion in two independent ways: direct directed indegree/outdegree limits followed by a directed-cycle search, and the local three-arc exclusions plus the two forbidden full rims. For \(n=3,4,5\), including nonidentity matchings and a step-two inner rim, the two face sets coincide. Exact mod-two boundary elimination independently recovers one class in each predicted degree. The script prints `FINITE_CHECKS_OK` on success. Its exhaustive finite cases support the definitions and calculations, but the all-length conclusion follows from the preceding topological proof.

## Relationship to prior work

The 2022 foundational treatment by Caputi, Collari, Di Trani, and Smith defines multipath complexes and computes homotopy types for individual directed polygons, linear digraphs, small grids and tournaments. Their dynamical-region framework does not give a decomposition of the present connected two-rim, matched graph into independent joins. The 2024 quiver-minor comparison with matching complexes applies to digraphs **without** directed cycles; our family has two. Work on **bidirectional** polygonal digraphs considers a different directed edge set. Later conflict-hypergraph treatments encode directed path restrictions generally but do not assert this two-rim homotopy formula. Unlike these results, the present argument computes two specific integral sphere summands simultaneously and proves independence of the spoke permutation.

## Limitations

The statement concerns two rim cycles of the same length joined by a complete **one-way** matching, with both rim orientations coherent. It does not classify arbitrary generalized Petersen orientations, reversed spokes, unequal rim lengths, extra cross-edges, or multipath persistence maps. Its claim of previously unreported coverage is limited by searchable and inspected literature; an unindexed equivalent result may exist. The mathematical proof itself is not contingent on the bibliographic search.

## References

1. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (August 9, 2022), §§2–4. https://arxiv.org/abs/2208.04656
2. L. Caputi, C. Collari, E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (January 2, 2024), §§1,4. https://arxiv.org/abs/2401.01248
3. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670 (2026), §§1–2. https://arxiv.org/abs/2601.05670
4. Deshpande and Sawant, *Vertex decomposable complexes of directed forests, conflict graphs and chordality*, arXiv:2602.14936v1 (2026), §§5–6. https://arxiv.org/abs/2602.14936
