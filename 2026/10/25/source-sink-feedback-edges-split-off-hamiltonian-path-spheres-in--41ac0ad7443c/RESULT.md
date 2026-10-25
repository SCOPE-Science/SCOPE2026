# Source–sink feedback edges split off Hamiltonian-path spheres in multipath complexes

## Finding
Let \(D\) be a finite loopless digraph on \(n\ge3\) vertices with distinct vertices \(s,t\), where \(s\) has no incoming arcs and \(t\) has no outgoing arcs. Add the return arc \(b=t\to s\), and write \(G=D\cup\{b\}\). Denote by \(h(D;s,t)\) the number of directed Hamiltonian paths from \(s\) to \(t\) in \(D\). Then the multipath complex \(X(G)\) satisfies

\[
\widetilde H_{n-2}(X(G);\mathbb Z)\cong\mathbb Z^{h(D;s,t)}.
\]

Moreover, for every such path \(P\), the boundary of the formal simplex on the directed Hamiltonian cycle \(P\cup\{b\}\) is an embedded simplicial \((n-2)\)-sphere in \(X(G)\). These spheres give maps

\[
i:\bigvee_{P}S^{n-2}\longrightarrow X(G),\qquad
r:X(G)\longrightarrow\bigvee_{P}S^{n-2},\qquad r\circ i\simeq\mathrm{id}.
\]

The wedge is an abstract domain for the maps; the embedded spheres may intersect in more than their common vertex \(b\). If there are no Hamiltonian paths, the wedge is a point and the top reduced homology vanishes.

## Assumptions and scope
A **multipath** is an arc subset in which every weakly connected component with an arc is a directed simple path; isolated graph vertices are allowed. Equivalently, selected indegrees and outdegrees are at most one and the selected digraph contains no directed cycle. The **multipath complex** \(X(G)\) has the arcs of \(G\) as simplicial vertices and the multipaths as faces. Both orientations between a pair of vertices may be present in \(D\); no acyclicity assumption on \(D\) is made. All homology is reduced simplicial homology with integral coefficients. In particular, a face using \(k\) arcs has dimension \(k-1\).

For illustration, if \(D\) is the transitive tournament on \(n\ge3\) vertices, with \(s\) its first and \(t\) its last vertex, then \(h(D;s,t)=1\); reversing its long arc gives an essential \((n-2)\)-sphere homotopy retract. For \(n=m+2\) with \(m\ge1\), if there are all arcs from \(s\) to the \(m\) internal vertices, all arcs from internal vertices to \(t\), and both orientations between all distinct internal vertices, then \(h(D;s,t)=m!\). Consequently its return-edge multipath complex has a homotopy retract of \(m!\) spheres of dimension \(m\), and top integral homology of rank \(m!\).

## Proof
Write \(K=X(G)\) and \(d=n-2\). Every multipath on \(n\) graph vertices has at most \(n-1\) arcs, so \(K\) has dimension at most \(d\). Let \(A=\operatorname{st}_{K}(b)\) be the closed simplicial star of the added arc. Its defining condition is that an arc set can be extended by \(b\) to a multipath; it is a cone on \(b\), hence contractible.

A \(d\)-simplex of \(K\) comprises \(n-1\) arcs. Being a multipath, it is necessarily a Hamiltonian directed path. Every such simplex using \(b\) lies in \(A\). If a Hamiltonian path does not use \(b\), it belongs to \(D\), must start at \(s\) (whose indegree is zero), and must end at \(t\) (whose outdegree is zero). Such a path \(P\) cannot lie in \(A\), since adjoining \(b\) creates a directed Hamiltonian cycle. Thus \(C_d(K,A;\mathbb Z)\) has as a free basis exactly the \(h(D;s,t)\) Hamiltonian paths of \(D\).

Every codimension-one face of such a path \(P\) becomes compatible with \(b\): removing any path arc breaks the unique directed route from \(s\) to \(t\), and then adding the return arc produces only directed paths, never a directed cycle. Therefore every relative boundary \(\partial_d^{\mathrm{rel}}P\) is zero, and \(H_d(K,A;\mathbb Z)=\mathbb Z^{h(D;s,t)}\). The long exact sequence for \((K,A)\), together with contractibility of \(A\), gives an injective map \(H_d(K;\mathbb Z)\to H_d(K,A;\mathbb Z)\) (also when \(d=1\)).

Fix one such path \(P\). The \(n\) arcs of \(P\cup\{b\}\) form one directed Hamiltonian cycle, which is not itself a multipath, but **every proper subset** is a multipath. Hence its formal oriented simplicial boundary

\[
z_P=\partial[\,P\cup\{b\}\,]\in C_d(K;\mathbb Z)
\]

is an integral cycle, by \(\partial^2=0\). Exactly one facet of this boundary omits \(b\), namely \(P\); every other facet contains \(b\) and belongs to \(A\). Thus the image of \([z_P]\) in \(H_d(K,A;\mathbb Z)\) is \(\pm[P]\). Since these images form the entire relative basis, the map from absolute to relative top homology is also surjective; the displayed integral isomorphism follows, with \([z_P]\) providing a canonical signed basis. No \((d+1)\)-chains exist in \(K\), so no hidden higher boundaries arise.

For the asserted homotopy splitting, let \(q:|K|\to |K|/|K^{(d-1)}|\) collapse its \((d-1)\)-skeleton. Since \(K\) has dimension at most \(d\), the quotient is a wedge of one \(d\)-sphere for every \(d\)-simplex. Compose \(q\) with the projection onto precisely those coordinates indexed by the \(b\)-free Hamiltonian paths in \(D\); this is \(r\). Map one sphere for each \(P\) into \(|K|\) using the simplicial boundary of the formal \(n\)-arc simplex \(P\cup\{b\}\), and identify the vertex \(b\) as a common basepoint to obtain \(i\). On that sphere, \(r\) collapses all top facets containing \(b\) and maps the remaining facet \(P\) with degree \(\pm1\) onto its own coordinate sphere. It does not map to any other chosen coordinate. Choose orientations to obtain degree \(+1\) on every summand. The composite is homotopic to the identity, including for \(d=1\), where it traverses its own circle exactly once. Thus the wedge is a homotopy retract.

## Verification
The accompanying standalone Python 3 file `verify_feedback.py` reconstructs all allowed finite source–sink digraphs for \(n=3,4,5\) (respectively \(8,128,8192\) digraphs), including digraphs with bidirected internal arcs and directed cycles. It enumerates all top simplices as directed spanning paths, computes the mod-two rank of their simplicial boundary matrix, and checks that its nullity equals the Hamiltonian \(s\)-to-\(t\) path count. It also checks signed boundary-of-boundary cancellation for the return-edge cycles of all transitive tournaments through \(n=8\) and all complete bidirected-interior examples through \(n=7\). All listed checks passed. The infinite and integral assertions follow from the preceding proof, not from finite enumeration or mod-two extrapolation. Reproduce with `python3 verify_feedback.py`.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith (2022, Theorem 3.5) compute a **reduced Euler characteristic** for a transitive tournament with its extremal arc reversed. Their Theorem 5.1 establishes wedge-type behavior for *transitive* tournaments before reversing the long arc. Neither theorem gives the top integral homology of the reversed tournament or the source–sink feedback theorem for arbitrary digraphs, and the reduced Euler characteristic does not determine these top groups. The general definitions and path-poset context are from Caputi, Collari and Di Trani (2021). The acyclic-digraph comparison by Caputi, Collari and Ramos (2024) does not directly cover the return-edge digraphs when they acquire Hamiltonian directed cycles. This result is specifically a statement about **simplicial multipath complexes**, not the different directed path-homology theory.

## Limitations
The result does not calculate lower-dimensional homology, torsion in other degrees, the full homotopy type, or an equivariant splitting. An abstract homotopy retract need not be a wedge-shaped embedded subcomplex: the contributing cycle-boundary spheres may overlap geometrically. Novelty is assessed against the sources identified below, but other unindexed equivalent work remains a possible risk. The finite checker verifies only bounded cases over the field with two elements; it is not the proof of the integral theorem.

## References
1. L. Caputi, C. Collari, S. Di Trani, and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first posted 2022-08-09, especially Theorems 3.5 and 5.1; https://arxiv.org/html/2208.04656v1.
2. L. Caputi, C. Collari, and S. Di Trani, *Combinatorial and Topological Aspects of Path Posets, and Multipath Cohomology*, arXiv:2110.11206, first posted 2021-10-21; https://arxiv.org/html/2110.11206v2.
3. L. Caputi, C. Collari, and E. Ramos, *The weak categorical quiver minor theorem and its applications: matchings, multipaths, and magnitude cohomology*, arXiv:2401.01248, first posted 2024-01-02; https://arxiv.org/abs/2401.01248.
