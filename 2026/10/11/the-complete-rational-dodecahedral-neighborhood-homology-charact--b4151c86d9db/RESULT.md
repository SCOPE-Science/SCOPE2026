# The complete rational dodecahedral neighborhood-homology character

## Finding
Let \(D=GP(10,2)\) be the dodecahedral graph and let \(\mathcal N(D)\) be its ordinary Lovász **open-neighborhood complex**: a nonempty set of vertices is a simplex precisely when all its vertices have a common graph neighbor. The complete automorphism group is \(\operatorname{Aut}(D)\cong A_5\times C_2\). Let \(V_5\) denote the rational five-dimensional irreducible representation of \(A_5\), \(W_6\) its rational six-dimensional irreducible representation obtained from the two conjugate three-dimensional complex irreducibles, and \(\varepsilon\) the sign character of the central \(C_2\). Then

\[
\widetilde H_1(\mathcal N(D);\mathbb Q)\cong
((W_6\oplus V_5)\boxtimes\mathbf1)
\oplus((2V_5)\boxtimes\varepsilon).
\]

All other reduced rational homology groups vanish. The antipodal involution has respective \(+1\) and \(-1\) eigenspace dimensions \(11\) and \(10\). In particular the space of homology classes fixed by all rotations, and therefore by every graph automorphism, is zero. The nonequivariant homotopy equivalence \(\mathcal N(D)\simeq\bigvee^{21} S^1\) is background, **not** the newly asserted invariant.

## Assumptions and scope
All graphs are finite and simple. The vertices are the integers \(0,\ldots,19\). In the generalized Petersen labeling, outer vertices \(i\in\{0,\ldots,9\}\) form a ten-cycle, vertex \(i\) is joined by a spoke to \(10+i\), and the inner vertices have edges from \(10+i\) to \(10+(i+2\bmod10)\). Thus the edge set is given completely by these thirty unordered pairs. The group acts simplicially on \(\mathcal N(D)\) through its permutation action on the vertices. Homology representations and character decompositions are over \(\mathbb Q\). In this statement the central involution is the **graph antipodal symmetry**, not the abstract box-complex factor-swapping involution.

## Proof
**Topology.** Each of the twenty graph vertices has exactly three distinct neighbors, and all twenty neighbor triples are different. These triples are the maximal two-faces of \(\mathcal N(D)\). A distinct pair of triples shares at most one vertex: otherwise their two graph centers and two shared neighbors would form a four-cycle, contrary to the explicitly checkable edge list. Therefore all sixty one-faces of these twenty triangles are distinct, each contained in exactly one triangle. The one-skeleton is connected; this follows either by tracing the distance-two edges from any outer vertex or by the short exhaustive breadth-first certificate in the verifier. Remove each triangle and any one of its three free edges. These are twenty valid elementary simplicial collapses. The remaining connected graph has twenty vertices and forty edges, so its first Betti number is \(40-20+1=21\), giving \(\mathcal N(D)\simeq\bigvee^{21}S^1\) and proving that the only nontrivial reduced chain-homology representation is first homology.

**Entire automorphism group.** Fix root \(0\) and its three ordered neighbors \((1,9,10)\). Distances from these four vertices distinguish all twenty vertices. Thus an automorphism is uniquely specified by the image of vertex \(0\) (twenty choices) and the images of its three ordered neighbors (six choices). The verifier generates the permutations compatible with these distance signatures, checks exact preservation of all thirty edges, and exhibits 120 automorphisms; this matches the 120 upper bound and is exhaustive. Its two displayed vertex permutations of respective orders five and three generate a subgroup \(R\) of order sixty, namely the usual orientation-preserving dodecahedral rotation group \(A_5\). The antipodal permutation \(z\), sending each vertex to its unique distance-five vertex, is central (distance is automorphism-invariant), has order two, and lies outside \(R\). Consequently every automorphism belongs to \(R\sqcup zR\), so \(\operatorname{Aut}(D)\cong A_5\times C_2\). The group enumeration and its order distribution \((1,15,20,24)\) on elements of orders \((1,2,3,5)\) are exactly replayable in the verifier.

**Equivariant Lefschetz computation.** For a permutation \(g\) in this group, let \(\operatorname{tr}_{C_j}(g)\) be the signed fixed-face trace of its action on oriented \(j\)-simplices. Since the neighborhood complex is connected and has no positive homology except \(H_1\), the simplicial Lefschetz identity gives
\[
\chi_{H_1}(g)=1-\operatorname{tr}_{C_0}(g)+\operatorname{tr}_{C_1}(g)-\operatorname{tr}_{C_2}(g).
\]
The complete 120-permutation check gives the following constant traces for a rotation \(r\) of order \(1,2,3,5\), respectively:
\[
\chi_{H_1}(r)=(21,1,-3,1),\qquad
\chi_{H_1}(zr)=(1,-3,1,1).
\]
Both conjugacy classes of order-five rotations have the displayed rational trace. The central \(+1\) and \(-1\) eigenspace characters, obtained by taking half the sum and difference, are therefore
\[
\chi_+=(11,-1,-1,1),\qquad \chi_-=(10,2,-2,0).
\]

**Rational character decomposition.** The relevant rational \(A_5\)-irreducible characters on those four element orders are \(\chi_{V_5}=(5,1,-1,0)\), \(\chi_{W_6}=(6,-2,0,1)\), plus the trivial and four-dimensional irreducibles. Thus \(\chi_+=\chi_{W_6}+\chi_{V_5}\) and \(\chi_-=2\chi_{V_5}\). Semisimplicity of rational representations of finite groups establishes the asserted isomorphism. Because neither side contains a trivial \(A_5\)-constituent, there are no nonzero rotation-fixed or full-group-fixed first-homology vectors.

## Verification
The included, standalone Python 3 program `verify_dodeca_neighborhood.py` uses only the standard library. Run `python3 verify_dodeca_neighborhood.py` from its containing directory. It reconstructs the thirty graph edges, twenty neighborhoods, all twenty triangles and sixty edges of the simplicial complex; checks the free-face and connectivity claims; enumerates all 120 graph automorphisms using exact integer distance signatures; constructs the rotation subgroup and central involution; enumerates signed fixed simplices for every automorphism; and verifies the rational character identities and multiplicities. The final output is `VERIFY_OK`. All enumerations are finite, exhaustive for this specific graph, and employ integer arithmetic. No assertion about other graphs is inferred from numerical examples.

## Relationship to prior work
Matsushita's 2017 paper establishes general equivariant-topological connections among graph coloring, box complexes, and neighborhood complexes, but does not compute this dodecahedral graph-automorphism character. Shukla's 2018 classification of degree-at-most-three neighborhood complexes covers the nonequivariant wedge-of-circles conclusion for this graph; it does **not** provide the full rational \(A_5\times C_2\)-representation. Matsushita's later square-free Hom-complex classification is also nonequivariant with respect to this graph-automorphism representation. The dodecahedral independence complex, matching complex, and icosahedral neighborhood complex have different defining complexes, so their known homology statements do not imply the present character. The new contribution is the complete **representation**, not the already implied rank or homotopy type.

## Limitations
This is an exact rational homology representation for a **single canonical finite graph**. It does not assert an integral module classification, a formula for arbitrary generalized Petersen graphs, a new nonequivariant wedge calculation, a graph-coloring improvement, or an independence/certification result. A differently indexed prior equivariant calculation remains a possible novelty risk; a literature search alone is not a proof of absolute priority.

## References
1. T. Matsushita, *\(\mathbb Z_2\)-indices and Hedetniemi's conjecture*, arXiv:1710.05290v1 (first public 2017-10-15), https://arxiv.org/abs/1710.05290 . Primary MSC 55U10.
2. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526v1 (2018), https://arxiv.org/abs/1802.04526 .
3. T. Matsushita, *Hom complexes of graphs whose codomains are square-free*, arXiv:2412.19144 (2024), https://arxiv.org/abs/2412.19144 .
