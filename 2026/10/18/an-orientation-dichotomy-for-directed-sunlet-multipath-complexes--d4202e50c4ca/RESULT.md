# An orientation dichotomy for directed sunlet multipath complexes

## Finding

For every integer \(n\ge3\), form a directed sunlet \(D(n,\epsilon)\) from a coherently oriented \(n\)-cycle by attaching exactly one pendant arc at each rim vertex. Each pendant is oriented either inward or outward, as specified below. Write \(X(n,\epsilon)\) for its multipath simplicial complex.

**Complete orientation classification.** If every pendant has the same direction, \(X(n,\epsilon)\) is a triangulated \((n-1)\)-ball. If at least one pendant points inward and another outward, then there is an explicit sequence of elementary simplicial collapses

\[
X(n,\epsilon)\searrow \partial\Delta(E)\cong S^{n-2},
\]

where \(E\) is the set of all \(n\) coherently directed rim arcs. In particular, in the mixed case the inclusion of the unaugmented rim-cycle multipath complex \(\partial\Delta(E)\) is a simple-homotopy equivalence; in the uniform case it is nullhomotopic.

There is also an exact face enumerator. Set

\[
q=\#\{i\pmod n:\epsilon_i=\mathrm{in},\;\epsilon_{i+1}=\mathrm{out}\}.
\]

Equivalently, \(q\) counts outward-to-inward transitions. If the empty face is counted, the face polynomial is

\[
\sum_{\sigma\in X(n,\epsilon)}t^{|\sigma|}
=(1+t)^q(1+2t)^{n-2q}(1+3t+t^2)^q-t^n.
\]

Consequently, mixed orientations have exactly one nonzero reduced integral homology group, namely \(\widetilde H_{n-2}(X(n,\epsilon);\mathbb Z)\cong\mathbb Z\), while uniform orientations have zero reduced integral homology. If a rotation through \(k\) rim positions preserves the pendant orientation word, then its action on the mixed-case integral generator is multiplication by \((-1)^{n-\gcd(n,k)}\).

## Assumptions and scope

Let \(v_i\) (indices modulo \(n\)) be the distinct vertices of the core, and \(w_i\) their distinct pendant leaves. The \(2n\) arcs are

\[
e_i=(v_i,v_{i+1}),\qquad
s_i=\begin{cases}(v_i,w_i),&\epsilon_i=\mathrm{out},\\ (w_i,v_i),&\epsilon_i=\mathrm{in}.
\end{cases}
\]

There are no further arcs and no antiparallel pairs. A multipath is a subset of these arcs whose directed subgraph has indegree and outdegree at most one at each vertex and has no directed cycle. The multipath complex has the arcs as its vertices and the multipaths, including the empty face, as its faces. The statement concerns all \(2^n\) orientations of the pendant arcs for each \(n\ge3\), with the core orientation held coherent.

## Proof

**1. Exact face model.** Any directed cycle in the directed sunlet is the full rim cycle: each pendant leaf has total degree one, and every rim edge points consecutively around the same cyclic order. Thus cycle-freeness adds exactly the prohibition on selecting all rim arcs \(E=\{e_0,\ldots,e_{n-1}\}\). The only possible indegree/outdegree conflict involving \(s_i\) is with \(e_i\) when \(s_i\) is outward, or with \(e_{i-1}\) when it is inward. There is no conflict between distinct pendants. Each pendant is therefore incompatible with **exactly one** rim arc.

Let \(Y\) be the simplicial complex obtained by imposing those pairwise incompatibilities but not yet prohibiting the full rim cycle. For every \(i\), let \(k_i\) count the pendants incompatible with \(e_i\). By construction \(k_i\in\{0,1,2\}\). The pendant arcs assigned to different rim edges are disjoint, so \(Y\) is the simplicial join of \(n\) local complexes: the local complex at \(e_i\) either selects \(e_i\) alone or selects an arbitrary subset of the \(k_i\) incompatible pendants. Its face polynomial is

\[
(1+t)+(1+t)^{k_i}-1.
\]

Since every pendant conflicts with one rim arc, no pendant can coexist with all rim arcs. Thus \(E\) is a maximal face of \(Y\), and \(X(n,\epsilon)=Y\setminus\{E\}\) as simplicial complexes: all proper faces of \(E\) remain.

**2. Face polynomial.** A cyclic word on the symbols inward/outward has equally many inward-to-outward and outward-to-inward transitions. At an inward-to-outward transition across \(e_i\) the value of \(k_i\) is zero; at an outward-to-inward transition it is two; and at every unchanged adjacent pair it is one. Hence exactly \(q\) local factors have \(k_i=0\), exactly \(q\) have \(k_i=2\), and the remaining \(n-2q\) have \(k_i=1\). Multiplying the local polynomials and subtracting the unique prohibited \(n\)-arc face \(E\) proves the enumerator.

**3. Uniform case.** If \(q=0\), a cyclic binary word has no transitions, so all pendants point in the same direction. Every \(k_i=1\), and the local complex consists of the two mutually exclusive vertices \(e_i\) and the unique pendant assigned to it. Their join is the boundary of the \(n\)-dimensional crosspolytope, \((S^0)^{*n}\cong S^{n-1}\). The face \(E\) is one of its facets. Removing precisely that facet, while retaining its boundary, leaves a PL \((n-1)\)-ball, establishing the claimed stronger geometric statement.

**4. Mixed case: explicit relative collapse.** If \(q>0\), choose an index \(j\) where \(\epsilon_j=\mathrm{in}\) and \(\epsilon_{j+1}=\mathrm{out}\). The rim arc \(e_j\) has no pendant incompatibility. For any face \(\sigma\in X(n,\epsilon)\) that contains at least one pendant and does not contain \(e_j\), pair it with \(\sigma\cup\{e_j\}\). This upper face is always legal: adding \(e_j\) creates no indegree/outdegree conflict; furthermore every selected pendant forces the absence of some rim arc other than \(e_j\), so adding \(e_j\) cannot complete the directed rim cycle.

Perform these pairs in descending order of the cardinality of the lower face. At the moment the pair \((\sigma,\sigma\cup\{e_j\})\) is removed, any other one-vertex coface of \(\sigma\) has already been removed in a strictly larger pair. Thus \(\sigma\) is a free face of \(\sigma\cup\{e_j\}\), so each removal is an elementary simplicial collapse. After all pairs are removed, exactly the faces with no pendant remain. Those are all **proper** subsets of \(E\), namely \(\partial\Delta(E)\). This proves the simple collapse to \(S^{n-2}\) for every mixed orientation, integrally and in every dimension.

**5. Symmetry.** The rim inclusion commutes with each cyclic rotation preserving the orientation word. In the mixed case it induces an integral homology isomorphism, so the rotation action agrees with the action on the oriented boundary of the rim simplex. The permutation of its \(n\) rim vertices by shift \(k\) has \(\gcd(n,k)\) cycles and sign \((-1)^{n-\gcd(n,k)}\), giving the asserted character without assuming an equivariant collapse.

## Verification

The supplied standalone `verify_sunlet.py` uses the original arcs, indegree/outdegree constraints and directed-cycle search to enumerate the multipath complexes for every pendant orientation at \(n=3,4,5,6\). Independently, it constructs the forbidden-pair model, compares the **entire** face sets, checks every coefficient of the all-parameter face polynomial, computes reduced homology over \(\mathbb F_2\), and in each mixed case actually replays the descending elementary collapses, checking every free-face condition and the exact surviving rim boundary. The numbers of tested orientations are \(8,16,32,64\); the total numbers of successfully checked elementary collapse pairs are \(66,528,3720,24666\), respectively. All tests pass. These finite checks are corroborative; the universal claim follows from Steps 1–5, not from extrapolation.

## Relationship to prior work

Caputi, Collari, Di Trani and Smith determine multipath homotopy for coherently oriented polygons, linear graphs, selected grids and transitive tournaments, and introduce dynamical-module splittings [1]. In particular, their cycle result identifies the subcomplex \(\partial\Delta(E)\), but does not classify what happens after one independently oriented pendant edge is added at every cycle vertex. The 2022 path-poset study [2] develops the definition and examples but does not provide this full orientation classification. The categorical quiver-minor comparison [3] gives a matching-complex description **when there are no directed cycles**, a hypothesis violated here. The later bidirectional-polygon study [4] concerns antiparallel rim arcs and a distinct two-edge attachment operation; those results do not imply this simple-collapse dichotomy for singly oriented sunlets. Relevant indexed results on bidirected double stars and bidirected polygons similarly concern different graphs or directed-edge sets. No equivalent classification was identified in the searches described in `AUDIT.json`.

## Limitations

The coherent orientation of the core, exactly one distinct pendant leaf per rim vertex, and \(n\ge3\) are required. The theorem does not classify bidirected core edges, multiple leaves at one vertex, arbitrary orientations of the rim, or directed homology theories other than the multipath simplicial complex. Its rotation statement is about the induced integral homology character, not equivariant homotopy equivalence or fixed-point spaces. Unindexed equivalent prior literature remains possible; independent mathematical auditing has not been performed.

## References

[1] L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (public August 9, 2022), especially Definitions 2.1–2.2 and §§4.1–4.2. https://arxiv.org/abs/2208.04656

[2] L. Caputi, C. Collari and S. Di Trani, *Combinatorial and topological aspects of path posets, and multipath cohomology*, arXiv:2110.11206 (2021/2022), especially §6. https://arxiv.org/abs/2110.11206

[3] L. Caputi, C. Collari and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248v1 (January 2, 2024), especially Theorem 4.20. https://arxiv.org/abs/2401.01248

[4] L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (January 9, 2026), especially Proposition 2.3 and Theorem 2.8. https://arxiv.org/abs/2601.05670
