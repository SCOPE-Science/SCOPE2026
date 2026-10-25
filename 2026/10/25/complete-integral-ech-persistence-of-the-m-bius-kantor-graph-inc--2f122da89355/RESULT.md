# Complete integral Čech persistence of the Möbius–Kantor graph, including a mixed degree-four/six stage

## Finding
Let \(G=GP(8,3)\) be the sixteen-vertex Möbius–Kantor graph. For every real \(r\geq0\), let \(\mathcal C_r(G)\) be the nerve of the **closed radius-\(r/2\) balls** centered at vertices of the geometric unit-edge graph, with shortest-path metric. The complete reduced integral persistence module is the following direct sum of interval modules. Multiplicities are integral ranks; endpoints are included on the left and excluded on the right:

\[
\begin{array}{c|c|c}
\text{homological degree}&\text{interval}&\text{multiplicity}\\ \hline
0 &[0,1)&15\\
1 &[1,3)&9\\
2 &[3,4)&47\\
4 &[4,5)&41\\
6 &[4,5)&2\\
9 &[5,6)&1\\
10 &[5,6)&4\\
14 &[6,7)&1
\end{array}
\]

There are no other reduced persistence bars, and every integral homology group is torsion-free. In particular, the newly determined consecutive stages have
\[
\mathcal C_3(G)\simeq \bigvee^{47}S^2,
\qquad
\widetilde H_i(\mathcal C_4(G);\mathbb Z)\cong
\begin{cases}
\mathbb Z^{41},&i=4,\\
\mathbb Z^2,&i=6,\\
0,&\text{otherwise}.
\end{cases}
\]
The scale-three and scale-four nerves are pure of dimensions five and nine respectively, so both are nonshellable.

## Assumptions and scope
Write the vertices as \(u_0,\ldots,u_7,v_0,\ldots,v_7\), with indices modulo eight. The undirected edges are exactly \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). Every geometric edge has length one. The nerve is intrinsic to the **continuous geometric graph**, not the graph-metric Vietoris–Rips clique complex. Closed balls fix all critical-scale endpoint conventions. Reduced homology is taken with coefficients in \(\mathbb Z\); the theorem concerns this one canonical finite graph, not all generalized Petersen graphs. The homotopy type at scale four is *not* asserted to be a sphere wedge.

## Proof
**1. Exact Čech generators.** In a unit-edge graph, an intersection of closed vertex-centered balls of radius \(r/2\) may be tested at a graph vertex for even integral \(r\), or at an edge midpoint for odd integral \(r\). Thus, at scale \(2t\) the maximal generating faces are the closed vertex neighborhoods \(N_t[x]\), and at scale \(2t+1\) they are \(N_t[x]\cup N_t[y]\) as \(xy\) ranges over graph edges. This is the general graph Čech neighborhood identity (Adams–Shukla–Singh, Lemma 2.2). The nerve does not change between consecutive integer scales. Breadth-first enumeration from each of the sixteen explicitly listed vertices gives the distance distribution \((1,3,6,5,1)\) at distances zero through four. Hence scales zero through seven suffice: at scale seven the nerve is already the full fifteen-simplex.

**2. Complete finite face-poset calculation.** Encode a nonempty face as a sixteen-bit mask. Generate the faces by taking every nonempty submask of every maximal neighborhood generator. The resulting numbers of nonempty faces at scales \(0,1,\ldots,7\) are exactly
\[
(16,40,168,976,11028,64444,65534,65535).
\]
For each scale, run the following deterministic algebraic discrete-Morse construction. For \(i=0,1,\ldots,15\) in that order, match every still-unmatched face \(F\) not containing vertex \(i\) to \(F\cup\{i\}\) whenever both are still unmatched. Each pair is a codimension-one incidence. Orient **all** matched Hasse incidences upward and all other codimension-one incidences downward, then topologically sort the entire directed face-incidence graph. Exact exhaustive topological sorts visit every face at each scale and thus certify acyclicity, without relying on probabilistic search or a homology guess.

The number of matched pairs and the **complete** list of critical-cell counts by dimension are:

| Scale | Matched pairs | Critical cells by dimension |
|---|---:|---|
| \(0\) | \(0\) | \(16\) vertices |
| \(1\) | \(15\) | one vertex, nine \(1\)-cells |
| \(2\) | \(79\) | one vertex, nine \(1\)-cells |
| \(3\) | \(464\) | one vertex, forty-seven \(2\)-cells |
| \(4\) | \(5492\) | one vertex, forty-one \(4\)-cells, two \(6\)-cells |
| \(5\) | \(32218\) | one vertex, two \(9\)-cells, five \(10\)-cells |
| \(6\) | \(32766\) | one vertex, one \(14\)-cell |
| \(7\) | \(32767\) | one vertex |

Acyclic discrete Morse theory gives a homotopy-equivalent CW complex with exactly these cells. Where critical dimensions are not consecutive, the integral cellular differential is necessarily zero. Therefore the scale-three complex is a wedge of forty-seven two-spheres, and at scale four the entire integral reduced homology is free of ranks forty-one in degree four and two in degree six. This proves the two previously unresolved stages integrally, including the absence of torsion. The script additionally computes ordinary mod-two simplicial boundary ranks as an independent numerical cross-check.

**3. The one nontrivial integer Morse differential.** At scale five, the two critical degree-nine cells and five critical degree-ten cells have signed integer Morse boundary matrix, in the deterministic critical-mask ordering,
\[
\partial_{10}^{\mathrm{Morse}}=
\begin{pmatrix}
0&1&-1&0&0\\
0&1&-1&0&0
\end{pmatrix}.
\]
Its nonzero image is generated by the primitive vector \((1,1)\). This has one unit Smith invariant, so scale-five reduced integral homology is exactly \(\mathbb Z\) in degree nine and \(\mathbb Z^4\) in degree ten, and zero in other degrees. These high-degree groups were already established in the prior published Alexander-duality treatment of this graph; their reproduction here supplies a coherent independent check for the full barcode. The checker constructs the signed boundary directly by exact gradient-path elimination, rather than inferring it from mod-two ranks.

**4. Endpoint stages and the surviving circle classes.** The scale-one nerve is the connected triangle-free graph \(G\) itself, hence \(\bigvee^9S^1\) because \(G\) has sixteen vertices and twenty-four edges. At scale two, for each graph vertex \(x\), collapse the tetrahedron on \(N_1[x]\) along the opposite triangular face on its three neighbors, then collapse each of the three remaining triangles with the corresponding neighbor-neighbor edge. The absence of three- and four-cycles guarantees that these are free faces. The specified sixty-four elementary collapses leave precisely \(G\). Therefore **the inclusion** \(\mathcal C_1(G)\hookrightarrow\mathcal C_2(G)\) is a homotopy equivalence, and all nine degree-one classes survive through scale two.

At scale six, every vertex has exactly one antipode at distance four, given by \(u_i\leftrightarrow u_{i+4}\) and \(v_i\leftrightarrow v_{i+4}\). Consequently the sixteen generating scale-six facets are all complements of single vertices: \(\mathcal C_6(G)=\partial\Delta^{15}\cong S^{14}\). At scale seven, each generating edge-neighborhood union is the full vertex set, so \(\mathcal C_7(G)=\Delta^{15}\). These high-scale statements, too, agree with and are credited to the earlier Alexander-duality treatment.

**5. Persistence maps.** Scale zero has sixteen connected components, giving fifteen reduced degree-zero bars ending at scale one. The only homological degree nonzero at two *successive* nontrivial scales is degree one at scales one and two; the sixty-four-collapse retraction proves that its inclusion map is an isomorphism. All other degree-preserving maps between successive scales have either zero domain or zero codomain. Thus the table in the Finding section gives the complete integral interval decomposition, with no unexplained extension or torsion.

## Verification
Run `python3 verify.py` with Python 3 and its standard library from the directory containing that file. The script builds all graph edges and sixteen breadth-first shortest-path vectors; enumerates all faces and all codimension-one Hasse incidences for each scale; reconstructs every matching and checks disjointness and complete directed-acyclicity by topological sort; independently checks mod-two Betti numbers at scales three, four and five; verifies all sixty-four relative free-face collapses from scale two onto the original graph; and constructs the exact signed integral Morse boundary matrix at scale five. It checks purity at scales three and four, the antipodal boundary sphere at six, and the full simplex at seven. A successful replay prints `VERIFY_OK`. It checks finite exhaustive objects, not an infinite-family theorem.

## Relationship to prior work
Adams, Shukla and Singh introduced the same intrinsic graph Čech convention and proved the even/odd neighborhood generator identity, studying hypercubes rather than the Möbius–Kantor graph. A published result, *High-dimensional Čech persistence of the Möbius–Kantor graph by Alexander duality*, already gives the high-degree barcode and the scale-five/scale-six calculations; **those parts are not claimed as new here**. That result explicitly restricts its full persistence conclusion to degrees at least nine and does not determine the forty-seven degree-two classes at scale three or the mixed degree-four/six groups at scale four. The separately published graph-metric Rips classification for this graph concerns pairwise-distance clique complexes, which are not these Čech nerves. The new content is the integral scale-three/scale-four classification and its combination with the known high-degree stages into the first full **all-degree** Čech barcode for this graph on the inspected evidence.

## Limitations
The complex at scale four has a reduced CW model with \(41\) four-cells and \(2\) six-cells, but this does **not** establish a wedge-of-spheres homotopy type: nontrivial six-cell attaching maps are not excluded. The result is finite and relies on an exhaustive deterministic exact-combinatorial certificate; it does not assert a family-wide generalization or independent expert validation. Literature searches and source comparisons do not rule out unindexed equivalent work.

## References
1. H. Adams, S. Shukla, A. Singh, *Čech complexes of hypercube graphs*, initially publicly posted 12 December 2022, arXiv:2212.05871, https://arxiv.org/abs/2212.05871. In particular Lemma 2.2 and Theorem 6.1.
2. *High-dimensional Čech persistence of the Möbius–Kantor graph by Alexander duality*, public research record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-high-dimensional-ech-persistence-of-the-m-bius-kantor-graph-by-a--8e4e37847049. The earlier high-degree calculation and its explicit low-degree limitation are credited.
3. *Mixed-dimensional Rips homotopy and full persistence of the Möbius–Kantor graph*, public research record (11 October 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mixed-dimensional-rips-homotopy-and-full-persistence-of-the-m-bi--16db962cc064. Distinct Vietoris–Rips construction, used for comparison.
4. R. Forman, *Morse theory for cell complexes*, Advances in Mathematics 134 (1998), 90–145; acyclic discrete-Morse matchings and integral CW reduction (standard theorem).
