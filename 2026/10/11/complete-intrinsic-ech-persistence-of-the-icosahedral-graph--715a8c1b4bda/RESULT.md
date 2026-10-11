# Complete intrinsic Čech persistence of the icosahedral graph

## Finding
Let \(I\) be the twelve-vertex graph of the regular icosahedron, with every edge assigned length one. For each real \(r\geq0\), let \(\mathcal C_r(I)\) be the nerve of the closed radius-\(r/2\) balls in the geometric realization of \(I\), with one ball centered at each graph vertex. Then the complete sequence of homotopy types is
\[
\mathcal C_r(I)\simeq
\begin{cases}
\bigsqcup^{12}\{\mathrm{pt}\},&0\leq r<1,\\
\bigvee^{19}S^1,&1\leq r<2,\\
S^2,&2\leq r<3,\\
\bigvee^{10}S^4,&3\leq r<4,\\
S^{10},&4\leq r<5,\\
\{\mathrm{pt}\},&r\geq5.
\end{cases}
\]
In particular, the **entire reduced integral persistent homology**, for the increasing Čech filtration, is given by eleven degree-zero bars \([0,1)\), nineteen degree-one bars \([1,2)\), one degree-two bar \([2,3)\), ten degree-four bars \([3,4)\), and one degree-ten bar \([4,5)\); all other reduced bars are absent. These intervals refer to the original real-valued scale \(r\), not the ball radius.

## Assumptions and scope
Use the following explicit model, with subscripts modulo five. The vertices are two poles \(N,S\), upper-ring vertices \(a_i\), and lower-ring vertices \(b_i\), for \(i\in\mathbb Z/5\mathbb Z\). The edges are exactly
\[
\{N,a_i\},\quad\{S,b_i\},\quad\{a_i,a_{i+1}\},\quad
\{b_i,b_{i+1}\},\quad\{a_i,b_i\},\quad\{a_i,b_{i-1}\}.
\]
In the verification files, \(N=0\), \(S=1\), \(a_i=2+i\), and \(b_i=7+i\), with \(0\leq i<5\). This is the standard icosahedral graph: it is connected, five-regular, has thirty edges and twenty triangular faces, and has graph diameter three. All distances are shortest-path distances in the one-dimensional geometric realization, not Euclidean chord distances between the polyhedron's vertices.

A face of \(\mathcal C_r(I)\) is a nonempty set of ball centers whose radius-\(r/2\) closed balls have a common point. In the usual convention, the empty simplex is also present; it is excluded from face counts and from the discrete-Morse matching. An integral homotopy type at every real \(r\geq0\), rather than just mod-two Betti numbers at sampled parameters, is asserted.

## Proof
For any finite graph with unit edges, the graph Čech simplex formula in Adams–Shukla–Singh, Lemma 2.2, gives \(\mathcal C_r=\mathcal C_{\lfloor r\rfloor}\). For even integer \(r=2k\), the generating simplices are the closed distance-\(k\) vertex neighborhoods \(B_k(v)\). For odd integer \(r=2k+1\), they are \(B_k(u)\cup B_k(v)\), indexed by graph edges \(uv\). This follows by testing the vertices and edge midpoints of the metric realization; it is the relevant formula for this Čech convention.

The model has twelve vertices and thirty edges, so at \(r=0\) there are twelve isolated vertices, and at \(r=1\) the nerve is the graph itself. Its first Betti number is \(30-12+1=19\), and any connected graph is a wedge of that many circles.

At \(r=2\), the twelve generating simplices are the six-vertex sets \(B_1(v)\). Enumerating all their nonempty subsets yields the face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5)=(12,60,140,150,72,12),
\]
comprising exactly \(446\) nonempty faces. The accompanying explicit certificate pairs \(222\) codimension-one incident faces, leaving precisely one critical vertex and one critical two-simplex. Its verifier checks that these are a partition of every nonempty face and that, on reversing the matched Hasse incidences, the directed Hasse graph is acyclic; all \(1572\) incidences are checked. Forman's discrete-Morse theorem supplies a CW complex with one zero-cell and one two-cell. The attaching map of the two-cell has image in a point, hence \(\mathcal C_2(I)\simeq S^2\) integrally.

At \(r=3\), the thirty generating simplices are \(B_1(u)\cup B_1(v)\) over all edges \(uv\). Each has eight vertices. Their subset union has face vector
\[
(f_0,f_1,f_2,f_3,f_4,f_5,f_6,f_7)
=(12,66,220,465,612,452,180,30),
\]
comprising \(2037\) nonempty faces. The second explicit certificate pairs \(1013\) codimension-one incident faces and leaves exactly one critical vertex and ten critical four-simplices. The directed Hasse graph, containing \(9924\) incidences, is verified acyclic by a complete topological sort. The resulting Morse CW complex has no positive-dimensional cells except ten four-cells, all attached to a point. Therefore \(\mathcal C_3(I)\simeq\bigvee^{10}S^4\) integrally.

Each vertex of \(I\) has exactly one antipode at graph distance three; all remaining vertices lie at distance at most two. Hence \(B_2(v)\) is the complement of one vertex, and the twelve such complements range over all vertex deletions. At \(r=4\), the Čech complex is consequently the boundary of an eleven-simplex, \(\partial\Delta^{11}\cong S^{10}\). For each edge \(uv\), the antipodes of \(u\) and \(v\) are distinct, so \(B_2(u)\cup B_2(v)=V(I)\). Thus \(\mathcal C_5(I)\) is the full eleven-simplex and stays contractible thereafter.

The listed nonzero reduced integral homology dimensions at consecutive integer scales are disjoint. Therefore every map between consecutive nonzero positive-dimensional homology groups has zero target in its degree. In degree zero, the eleven extra connected components die at the passage from twelve points to the connected graph at scale one. Together with constancy on each \([k,k+1)\), these observations determine all the stated persistent-homology intervals over \(\mathbb Z\).

## Verification
From the directory containing both accompanying files, run `python3 verify_icosahedral_cech.py`. It requires only Python's standard library and reads `MORSE_CERTIFICATE.json`. The verifier independently constructs the ring-and-poles graph, recomputes graph distances and all simplices, verifies the number and size of each Čech generator, checks the complete facet enumerations at all six integer scales, and validates every matching pair from the **stored** certificate. It also checks each Hasse incidence, acyclicity by topological sorting, the critical-cell dimensions, and direct boundary-matrix ranks over \(\mathbb F_2\) for scales two and three.

The independently computed mod-two simplicial boundary ranks at scale two, for differentials in ascending dimension, are \((11,49,90,60,12)\). At scale three they are \((11,55,165,300,302,150,30)\). The corresponding reduced Betti groups over \(\mathbb F_2\) are a single class in degree two and ten classes in degree four. These mod-two calculations corroborate the face/Morse certificate, but they do **not** replace the acyclic-matching proof of integral homotopy type. A successful replay ends with `VERIFY_OK`.

## Relationship to prior work
Adams, Shukla and Singh introduce precisely this intrinsic graph Čech filtration and its parity-dependent generating simplices. Their classified higher-scale examples are hypercube graphs, not the icosahedral graph; their general small-scale nerve-recovery guarantee stops before scale two for a girth-three graph. The present six-stage homotopy and complete integer persistence classification is not an implication of those hypercube results.

Previte's distance-neighborhood construction encompasses the scale-two closed-neighborhood part, but her dissertation's graph calculations concern other families, including paths, trees, cycles and their one-point unions, not this icosahedral classification. Matsushita's closed-neighborhood work gives general structural identifications and fundamental-group relationships and some complete multipartite/product examples, but not the numeric homotopy types here or the odd-scale transition. A separate reported calculation for the **Lovász open-neighborhood** complex of the icosahedral graph gives \(\bigvee^{23}S^2\); its maximal faces are open neighborhoods and its simplicial face vector differs, so it does not cover the present closed-neighborhood scale two or edge-neighborhood scale three. The nearby Euclidean cuboctahedron Vietoris–Rips filtration uses a different vertex set, metric and simplicial construction.

## Limitations
The theorem concerns this finite graph and the intrinsic, vertex-centered closed-ball Čech convention; it does not classify all Platonic graphs or metric thickenings with every geometric point as a center. The explicit Morse certificate is finite and exhaustive for these complexes, not a formal proof about arbitrary graphs. The preliminary literature and indexed-record searches do not rule out obscure or unindexed equivalent computations. Since the scale-two nerve is pure five-dimensional with nontrivial degree-two homology, and the scale-three nerve is pure seven-dimensional with nontrivial degree-four homology, both are non-shellable pure complexes.

## References
1. Henry Adams, Samir Shukla and Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first posted 12 December 2022), in particular Lemma 2.2, Lemma 2.3 and the main hypercube calculations. https://arxiv.org/abs/2212.05871
2. Corrine Previte, *The D-neighborhood complex of a graph*, Colorado State University PhD thesis (2014), especially the construction and the family-focused chapters. https://api.mountainscholar.org/server/api/core/bitstreams/3fa27974-eeb1-4df9-9be0-df5e71069ab5/content
3. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (first posted 16 November 2025), especially §§1, 3–5. https://arxiv.org/abs/2511.12608
4. A published exact computation, *The icosahedral neighborhood complex is a wedge of twenty-three 2-spheres* (2026), with explicit open-neighborhood definition, archived at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-icosahedral-neighborhood-complex-is-a-wedge-of-twenty-three--07e6e60de0e7
5. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145, DOI:10.1006/aima.1997.1650.
