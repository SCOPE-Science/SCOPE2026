# Disk retractions for two-particle symmetry quotients of complete bipartite graphs

## Finding

For every pair of integers \(m,n\geq 2\), let \(X_{m,n}=|K_{m,n}|\) be the topological realization of the complete bipartite graph and let
\[
B_2(X_{m,n})=\bigl((X_{m,n}\times X_{m,n})\setminus\Delta\bigr)/\mathfrak S_2
\]
be the collision-free unordered two-point configuration space. The full graph automorphism group \(G_{m,n}=\operatorname{Aut}(K_{m,n})\) acts diagonally. **The orbit space \(B_2(X_{m,n})/G_{m,n}\) admits a strong deformation retraction onto a finite simplicial complex that is PL-homeomorphic to the closed two-disk.** In particular,
\[
\boxed{B_2(X_{m,n})/G_{m,n}\simeq\ast\qquad(m,n\geq2).}
\]
The disk model depends only on whether the bipartition sizes agree. If \(m=n\), its face vector in dimensions zero, one, and two is \((11,22,12)\), and it has eight boundary edges. If \(m\ne n\), its face vector is \((19,42,24)\), and it has twelve boundary edges. These models have explicit sequences of respectively 22 and 42 elementary simplicial collapses to a vertex. The complete lists of simplices and collapse pairs are included in `quotient_models.json`.

The retraction conclusion is a **homotopy** statement: the original orbit space is noncompact, so it is not asserted to be homeomorphic to a compact disk. The disk is the compact deformation-retract model.

## Assumptions and scope

The graph is simple and its edges carry their usual closed-interval topology. Its two bipartition parts have positive cardinalities \(m,n\geq2\); points may move continuously along edges but may never coincide. The automorphism group is \(\mathfrak S_m\times\mathfrak S_n\) when \(m\ne n\), and \((\mathfrak S_m\times\mathfrak S_m)\rtimes C_2\) when \(m=n\), where the extra involution exchanges the sides. The two particle labels are forgotten independently of the graph automorphism action.

All triangulations and group actions used below are finite and exact. The proof does not assume that a graph-configuration discrete model is automatically equivariant: its retraction is defined directly and explicitly.

## Proof

**1. An equivariant triangulation with a full diagonal.** Write \(V\) and \(E\) for the vertex and edge sets of \(K_{m,n}\). Start with the ordinary product square complex \(X_{m,n}\times X_{m,n}\). For every ordered pair \((e,f)\in E^2\), introduce the center \(c_{ef}\) of the square \(e\times f\), and cone that square's four boundary edges to its center. Retain the original product vertices \(p_{uv}=(u,v)\), for \((u,v)\in V^2\). Thus if \(e=\{a,b\}\) and \(f=\{c,d\}\), the four triangles in the square are obtained by coning the four consecutive sides of the cycle
\[
p_{ac},\ p_{ad},\ p_{bd},\ p_{bc},\ p_{ac}.
\]
Call the resulting simplicial complex \(T\). Both permutations of the two factors and every graph automorphism act simplicially on \(T\); this coned-square triangulation makes no arbitrary diagonal choice.

The geometric diagonal \(\Delta=\{(x,x):x\in X_{m,n}\}\) is precisely the full induced subcomplex on
\[
V_{\Delta}=\{p_{uu}:u\in V\}\ \cup\ \{c_{ee}:e\in E\}.
\]
Indeed, within each square \(e\times e\), its diagonal consists of the two edges joining \(p_{aa}\), \(c_{ee}\), and \(p_{bb}\); there are no triangles spanned entirely by vertices of \(V_{\Delta}\).

Let \(K\) be the full subcomplex of \(T\) on vertices outside \(V_{\Delta}\). Every point \(z\in|T|\setminus|\Delta|\) has barycentric coordinates \(\lambda_v(z)\), with positive total weight
\[
s(z)=\sum_{v\notin V_{\Delta}}\lambda_v(z)>0.
\]
Define \(r(z)\in|K|\) by assigning weight \(\lambda_v(z)/s(z)\) to each vertex outside \(V_{\Delta}\), and zero weight to all vertices in \(V_{\Delta}\). The straight-line barycentric homotopy between \(z\) and \(r(z)\) stays off the diagonal, since its total weight outside \(V_{\Delta}\) is \((1-t)s(z)+t>0\). It fixes \(|K|\) pointwise and commutes with every simplex-permuting symmetry. Therefore it is an equivariant strong deformation retraction under the commuting actions of graph automorphisms and particle exchange.

**2. Exact finite orbit-complex reduction.** Set \(H=G_{m,n}\times\mathfrak S_2\). The preceding paragraph identifies the desired orbit-space homotopy type with \(|K|/H\). Barycentric subdivision removes inversions: a simplex of \(\operatorname{sd}K\) is a strict chain of nonempty faces of \(K\), and a symmetry preserving this chain setwise must fix each face (their dimensions are different). The quotient chains are classified by their \(H\)-orbits.

Each triangle of \(T\) lies in a single product square \(e\times f\). Consequently every chain of faces of \(K\) involves at most two different left-part vertices and at most two different right-part vertices of \(K_{m,n}\). Two such chains have the same symmetry orbit precisely when their incidences, equality patterns on each bipartition part, coordinate order, and (when permitted) side-exchange patterns agree. Any bijection between the at most two used vertices in a side extends to a permutation of the entire side because its size is at least two. This proves that the orbit-chain incidence structure is **independent of the actual sizes** \(m,n\), except for the presence of the side-exchanging automorphism when \(m=n\).

It therefore suffices to enumerate the two representative cases \((m,n)=(2,2)\) and \((m,n)=(2,3)\). Exact enumeration gives, respectively, \((4,5,2)\) and \((6,9,4)\) orbits of the zero-, one-, and two-dimensional faces of \(K\). More importantly, in both cases **each set of face-orbit vertices representing a strict inclusion chain occurs in precisely one chain orbit**. Thus the orbit of \(\operatorname{sd}K\) is an ordinary abstract simplicial complex (not merely a \(\Delta\)-complex with parallel simplices). Its full face lists and their canonical orbit construction appear in the supplied certificate and verifier.

**3. The quotients are disks.** For equal bipartition sizes, the resulting quotient complex has 11 vertices, 22 edges and 12 triangles. Every edge belongs to one or two triangles; eight edges belong to exactly one triangle. Every vertex link is a connected interval or circle, the boundary edges form one eight-edge cycle, and the complex is connected with Euler characteristic \(11-22+12=1\). It is therefore a compact connected triangulated two-manifold with nonempty boundary and Euler characteristic one, hence a closed disk.

For unequal bipartition sizes the identical checks give 19 vertices, 42 edges, 24 triangles, a single twelve-edge boundary cycle, and Euler characteristic \(19-42+24=1\), again a disk. These conclusions can alternatively be certified by the 22- and 42-pair elementary collapse sequences, which reduce their respective quotient complexes to a single vertex. All pairs are checked for freeness *at the step where they are removed*.

The finite calculations are exhaustive: there are four or six orbit types of original zero-faces, five or nine orbit types of one-faces, and two or four orbit types of two-faces, so the entire quotient has been enumerated. The size-independence argument in Step 2 transfers the verified finite classifications to every \(m,n\geq2\). This completes the proof. \(\square\)

## Verification

Run `python verify.py` in the directory containing `quotient_models.json`. It requires only the Python standard library. The verifier constructs the coned-square triangulation, checks that the diagonal is a full subcomplex, enumerates every group element and every orbit of nonempty face chains, tests uniqueness of the quotient simplex keys, verifies that the quotient's face set equals the supplied certificate, inspects all vertex links and boundary cycles, and replays every elementary collapse with an exact freeness test. It also independently checks the predicted orbit counts for \((m,n)=(3,3)\) and \((3,4)\), which are not used as the canonical representative models.

The finite program establishes the complete representative orbit enumerations. The extension from those finite cases to all sizes is the separate equality-pattern proof in Step 2, not an inference from finitely many experiments. The recorded successful output is `verification_output.txt`.

## Relationship to prior work

Barnett and Farber, *Topology of Configuration Space of Two Particles on a Graph, I* (first posted March 12, 2009, arXiv:0903.2180), study homology, intersection forms and equivariant deformation under particle interchange. Their discussion includes the classical observation that the ordered deleted-product model for \(K_{3,3}\) is a genus-four closed surface. This does not determine the additional quotient by all graph automorphisms, nor give either disk triangulation described here.

Prue and Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups* (first posted September 30, 2009, arXiv:0909.5511), establish sufficient subdivision conditions for replacing graph-configuration spaces by cubical complexes. The present proof instead constructs a coordinatewise canonical equivariant deformation for two points, and the cited subdivision theorem by itself does not classify the symmetry quotient.

Maciążek and Sawicki, *Non-abelian Quantum Statistics on Graphs* (2019, DOI:10.1007/s00220-019-03583-5), compute configuration-space homology for several graph families including complete bipartite graphs; the work does not give the complete graph-automorphism orbit-space disk models. Related existing rational representation calculations for \(K_{m,n}\) imply some vanishing invariant homology, but vanishing rational homology does **not** imply an actual disk retraction or contractibility of an orbit space.

## Limitations

The statement concerns ordinary, collision-free, unordered **two-point** configuration spaces and the quotient by the **entire** graph automorphism group. It does not classify quotients by proper subgroups, higher-particle configuration spaces, Borel-equivariant homotopy, integral equivariant homology, or the original noncompact orbit space up to homeomorphism. The finite certificates establish the indicated compact simplicial models but do not establish that these models are minimal. The publication-priority comparison is based on inspected accessible literature and indexed results; an equivalent unindexed treatment cannot be excluded. Independent mathematical audit has not been performed.

## References

1. K. Barnett and M. Farber, *Topology of Configuration Space of Two Particles on a Graph, I*, arXiv:0903.2180, first submitted 2009-03-12. https://arxiv.org/abs/0903.2180
2. P. Prue and T. Scrimshaw, *Abrams's Stable Equivalence for Graph Braid Groups*, arXiv:0909.5511, first submitted 2009-09-30. https://arxiv.org/abs/0909.5511
3. T. Maciążek and A. Sawicki, *Non-abelian Quantum Statistics on Graphs*, *Communications in Mathematical Physics* 371 (2019), 921–973. https://doi.org/10.1007/s00220-019-03583-5
