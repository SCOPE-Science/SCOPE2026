# Integral mixed-dimensional homotopy of the Möbius–Kantor perfect-matching complex
## Finding
Let \(G=\operatorname{GP}(8,3)\) be the sixteen-vertex Möbius–Kantor graph, and let \(\mathcal M_{\mathrm p}(G)\) be the simplicial complex of **extendible matchings**: a set of edges is a face exactly when it is contained in a perfect matching of \(G\). Then the complete **integral homotopy type** is
\[
\boxed{\mathcal M_{\mathrm p}(G)\simeq\bigvee^4 S^2\vee\bigvee^8 S^3.}
\]
In particular, its reduced integral homology is \(\mathbb Z^4\) in degree two, \(\mathbb Z^8\) in degree three, and zero in every other degree. The conclusion is an ordinary homotopy equivalence, not an equivariant decomposition. It concerns the perfect-matching subcomplex, **not** the larger ordinary matching complex.

## Assumptions and scope
Take the vertices to be \(u_i,v_i\) for \(i\in\mathbb Z/8\mathbb Z\), with graph edges \(\{u_i,u_{i+1}\}\), \(\{u_i,v_i\}\), and \(\{v_i,v_{i+3}\}\) (indices modulo eight). In the executable, \(u_i=i\), \(v_i=8+i\), and the 24 undirected edge pairs are sorted lexicographically. Each edge receives its zero-based index; face subsets are represented by 24-bit integers. A perfect matching has eight pairwise vertex-disjoint edges covering all sixteen vertices. The simplicial complex is the downward closure of all perfect matchings; the empty simplex is included formally but omitted from the nonempty face-poset matching.

## Proof
**1. Exhaustive facets and exact face set.** A recursion chooses the smallest unmatched graph vertex and branches over each incident edge joining two unmatched vertices. This enumerates all perfect matchings without omission. An independently implemented eight-by-eight bipartite-permutation enumeration gives the **same 33 perfect matchings**. Taking the downward closure gives 6,051 nonempty simplices, with face vector by dimension zero through seven
\[
(24,228,984,1842,1752,924,264,33).
\]
As a separate membership check, enumerate all 11,068 graph matchings including the empty matching and solve the residual perfect-matching problem by a memoized vertex-mask recursion. Exactly the 6,052 faces including the empty simplex pass this independent extendibility test.

**2. A complete acyclic discrete-Morse matching.** Begin with all 6,051 nonempty faces unmatched. For each graph-edge bit \(b=0,\ldots,23\) in increasing order, scan the still-unmatched faces in increasing integer-mask order. Whenever a face \(\sigma\) omits \(b\) and both \(\sigma\) and \(\sigma\cup\{b\}\) are still unmatched, pair them and remove both. This explicit algorithm makes 3,014 pairings and leaves precisely one critical vertex, nine critical 2-simplices, and thirteen critical 3-simplices. The complete directed Hasse graph has 27,192 nonempty face incidences. Orient each nonmatched cover downward and each matched cover upward. Kahn's topological sort visits all 6,051 faces. This is a **complete finite acyclicity check**, not a sampled search. Forman's theorem supplies a CW model with one 0-cell, nine 2-cells and thirteen 3-cells and no other cells.

**3. Exact integral attaching degrees.** Orient each simplex by ascending edge labels. For an oriented incidence \(\rho<\tau\), the sign is \((-1)^j\), where \(j\) is the position of the omitted label in \(\tau\). Project the oriented 2-cell basis onto critical 2-cells as follows: a critical cell projects to itself; a 2-cell paired as the upper member of a 1–2 pair projects to zero; if a 2-cell \(\sigma\) is paired upward with a 3-cell \(\tau\), substitute its coefficient using the signed relation
\[
P(\sigma)=-[\sigma:\tau]^{-1}\!
\sum_{\substack{\rho<\tau\\\rho\ne\sigma}}[\rho:\tau]P(\rho).
\]
This is the usual integer gradient-path cancellation formula; its recursion terminates because of the verified acyclicity. Applying it to the oriented faces of all thirteen critical 3-cells computes the **entire 9-by-13 signed Morse boundary**. In ascending critical-mask order, the nine critical 2-cell masks are
```
276, 532, 1044, 1282, 2114, 4162, 131138, 524546, 1048596
```
and the thirteen critical 3-cell masks are
```
81986, 133378, 295172, 393474, 533508, 1050660, 1081860,
2101268, 4196372, 6291476, 8396868, 8454210, 8913156
```
The resulting integer matrix (rows are critical 2-cells, columns critical 3-cells) is
```
 0  0  0  0  0  0  0  0  0  0  0  0  0
 0  0  0  0 -1  0 -1  0  0  0  0  0 -1
 0  0  0  0  1 -1  1  1 -1 -1  0  0  0
 0 -1 -1  0 -1  1 -1  0  0  0  0  0  0
 0  1  1  0  0  0  0  0  0  0  0  0  0
 1  0  0  0  0 -1  0  0  0  0 -1 -1  0
 0  0  0  0  0  0  0  0  0  0  0  0  0
 0  0  0  0  0 -1  0  0  0  0  0  0 -1
 0  0  0  0  0  1  0  0  0  0  0  0  1
```
Exact rational row reduction gives rank five. Its submatrix on zero-based rows \((1,2,3,4,5)\) and columns \((0,1,4,5,7)\) has determinant **minus one**, checked by exact rational elimination. Consequently all five nonzero Smith invariants are one and the remaining invariants vanish.

**4. From the matrix to homotopy.** The 2-skeleton of the Morse CW model is a wedge of nine 2-spheres, hence is simply connected and has \(\pi_2\cong H_2\cong\mathbb Z^9\). Thus the attaching maps of all thirteen 3-cells are classified by the displayed integer degree matrix. Unimodular changes of basis in the attaching spheres and 2-spheres realize the Smith reduction at the homotopy level. The five unit entries cancel five 2/3-cell pairs; the remaining eight trivial 3-cell attachments contribute eight 3-spheres, and the remaining four 2-cells contribute four 2-spheres. This proves the displayed ordinary integral homotopy equivalence.

## Verification
Execute `python3 verify_mk_perfect.py` using Python 3 and its standard library. The verifier reconstructs the complete graph and both independent perfect-matching enumerations; tests extendibility for every one of the 11,068 graph matchings; generates all 6,051 nonempty faces; checks the deterministic 3,014-pair Morse matching and acyclicity over all 27,192 Hasse covers; calculates the exact signed integral Morse boundary by terminating recursion; recomputes rank five and the determinant-minus-one unit minor; and separately computes all seven mod-two simplicial boundary ranks. The resulting independent boundary ranks, in dimensions one through seven, are
\[
(23,205,775,1059,693,231,33),
\]
which give the reduced mod-two Betti vector \((0,0,4,8,0,0,0,0)\). The successful terminal marker is `MOBIUS_KANTOR_PERFECT_MATCHING_WEDGE_4_S2_8_S3_VERIFIED`. The integral homotopy proof rests on the acyclic Morse matching and the integer degree matrix, **not** on the finite-field ranks.

## Relationship to prior work
Bayer, Jelić Milutinović and Vega define perfect-matching complexes and compute homotopy types for specified **finite planar honeycomb families**, not the nonplanar, cubic, 16-vertex Möbius–Kantor graph. Chandrakar and Singh's subsequently public polygonal-line-tiling work concerns open chains of polygons and two-row grids, not this graph. The Möbius–Kantor graph is not a polygonal-line tiling in either source's family.

The published calculation *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge* (record 4bfded76792e) gives the **ordinary** complex of **all** 11,067 nonempty matchings, with homotopy type \(\bigvee^8S^4\vee\bigvee^4S^5\). That result neither calculates nor implies the homotopy type of the proper 6,051-face **extendible** subcomplex; in particular, neither its Betti numbers nor its homotopy equivalence control the subcomplex's attaching degrees. An indexed 2026 theorem concerning *Möbius ladder graphs* addresses a different graph family, not \(\operatorname{GP}(8,3)\). The computations in this report therefore answer a different and more specific question than the inspected statements. No claim of exhaustive bibliographic uniqueness is made.

## Limitations
The result is an exact finite theorem about one canonical graph, not a uniform classification of all generalized Petersen graphs or all symmetric cubic graphs. The homotopy equivalence is nonequivariant; no group-action decomposition or inclusion-induced map into the ordinary matching complex is asserted. Exhaustive code is supplied for the indispensable finite arithmetic and face-poset checks. An equivalent unindexed theorem or calculation under a graph alias remains a residual bibliographic risk; unsuccessful searches alone cannot eliminate that risk.

## References
1. M. Bayer, M. Jelić Milutinović and J. Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803v1, first public 2022-09-06, subsequently *Electronic Journal of Combinatorics* 30 (2023), P2.45. Definition 1 and the family-specific theorems, especially Sections 2–4. https://arxiv.org/abs/2209.02803
2. H. Chandrakar and A. Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809v1, first public 2024-07-08, subsequently *Annals of Combinatorics* (2025). Introduction and Theorems 3.3, 4.1, 5.2–5.4. https://arxiv.org/abs/2407.05809
3. *The Möbius–Kantor matching complex is a mixed-dimensional sphere wedge*, publicly accessible report identifier 4bfded76792e (2026); the ordinary matching complex, not the extendible-matching subcomplex.
4. A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complex of Möbius Ladder Graph*, arXiv:2608.30601 (2026); a different graph family. https://arxiv.org/abs/2608.30601
5. R. Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics 134 (1998), 90–145.
