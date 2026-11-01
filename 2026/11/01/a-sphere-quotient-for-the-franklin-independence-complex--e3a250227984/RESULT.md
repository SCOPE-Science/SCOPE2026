# A sphere quotient for the Franklin independence complex

## Finding
Let \(F\) be the twelve-vertex Franklin graph, and let \(K=\operatorname{Ind}(F)\) be its simplicial complex of independent vertex sets. Under its full automorphism group \(G=\operatorname{Aut}(F)\), the **ordinary geometric orbit space** is a homotopy two-sphere:

\[
\boxed{|K|/G\simeq S^2.}
\]

More precisely, the barycentric orbit \(\Delta\)-complex has 630 cells and admits a certified sequence of exactly 299 elementary collapses to a connected closed \(\Delta\)-surface with 7 vertices, 15 edges, and 10 triangular faces. That surface is homeomorphic to \(S^2\). Here the quotient is the ordinary orbit space, not the homotopy/Borel quotient.

## Assumptions and scope
Number the vertices by \(\mathbb Z/12\mathbb Z\). The graph has the cycle edges \(\{i,i+1\}\) and the chords \(\{i,i+5\}\) for even \(i\) (equivalently, the LCF construction \([5,-5]^6\)); the graph is simple and undirected, with 12 vertices and 18 edges. Its full graph automorphism group is computed, rather than assumed, by exhaustive adjacency-preserving backtracking. It contains 48 elements.

An independent set contains no graph edge; \(K\) includes the empty simplex but only nonempty independent sets index barycentric vertices. Every topological statement concerns the usual geometric realization. The orbit quotient is by **all** 48 automorphisms acting on vertices. There are no coefficient-field assumptions: the final conclusion is an integral homotopy statement.

## Proof
**1. A finite quotient \(\Delta\)-complex.** There are exactly 195 nonempty independent sets, with face numbers, in dimensions \(0,\ldots,5\),
\[
(12,48,76,45,12,2).
\]
The barycentric subdivision \(\operatorname{sd}K\) has simplices indexed by strictly nested chains of nonempty independent sets. The automorphism action is *without inversions*: a group element stabilizing such a chain must fix each of its vertices because its members have distinct cardinalities. Hence \(|\operatorname{sd}K|/G\) has a genuine finite orbit \(\Delta\)-complex, with one open cell for each \(G\)-orbit of chains; it is homeomorphic to \(|K|/G\).

The certificate encodes each independent set as a 12-bit integer and a chain as its ordered sequence of integers. It uses the lexicographically least image under all 48 automorphisms as an orbit representative. Enumerating all independent sets and all ordered set partitions of each set (whose successive block unions are its chains) produces the quotient cell numbers
\[
(c_0,c_1,c_2,c_3,c_4,c_5)=(16,81,180,203,120,30).
\]
This gives Euler characteristic \(16-81+180-203+120-30=2\).

**2. Exact elementary collapses.** The attached `franklin_collapse_certificate.json` records 299 ordered pairs \((\tau,\sigma)\), where \(\tau\) is a codimension-one face of \(\sigma\). Its standalone verifier reconstructs all cells and, before deleting each pair, checks that \(\sigma\) is the **only remaining cell in any higher dimension** containing \(\tau\), and that the face occurs exactly once on \(\sigma\). The latter holds because removing different entries of a strictly ranked chain gives different rank signatures; the checker verifies distinct facets explicitly. Consequently each step is a geometric elementary \(\Delta\)-collapse (not merely a chain-complex cancellation). The residual \(\Delta\)-complex has \((c_0,c_1,c_2)=(7,15,10)\) and no cells of higher dimension.

**3. The residual is a sphere.** The attached certificate records every surviving vertex, edge and triangle by its chain representative. Reconstruction verifies that the one-skeleton is connected, all 15 edges meet exactly two triangles, and the link of each vertex is a single combinatorial circle. The seven vertex-link lengths, including possible two-edge circles in the \(\Delta\)-complex sense, are \((2,2,2,4,4,6,10)\) up to ordering. Thus the residual is a connected closed two-manifold. Its Euler characteristic is \(7-15+10=2\); the classification of closed connected surfaces identifies it as the two-sphere. The 299 collapses are deformation retractions, proving the stated homotopy equivalence.

## Verification
Run `python3 verify_franklin.py franklin_collapse_certificate.json` using Python 3 and its standard library. The script independently reconstructs the graph and all 48 automorphisms by constrained backtracking, independently generates barycentric chains by ordered set partitions, enumerates all 630 orbit cells, tests every geometric free-face condition, replays all 299 collapses, and checks connectedness, two-incidence edges, circular links and Euler characteristic 2. Its exact signed simplex traces also give an independent Burnside/Lefschetz check of the quotient Euler characteristic. The recorded result is `FRANKLIN_QUOTIENT_SPHERE_VERIFY_OK`.

## Relationship to prior work
The Franklin graph is a canonical symmetric cubic graph appearing in Franklin's 1934 six-color discussion of the Klein bottle; it also has the 6-crossed-prism and Knödel graph descriptions. General independence-complex methods of Marietti and Testa and the triangle-free suspension theorem of Barmak do not determine the homotopy type after quotienting by the full graph automorphism group. In particular, a nonequivariant suspension or homology calculation does not imply this concrete ordinary orbit-space sphere. Related calculations of *edge-matching* complexes of the Franklin graph concern independent sets of **edges**, not independent sets of **vertices**, and do not imply the stated result. The concrete quotient collapse and its manifold links are additional information.

## Limitations
The theorem concerns this specific graph, its vertex-independence complex, and its entire automorphism group. It does not determine the homotopy type of the quotient for arbitrary subgroups, general crossed prisms, or any Borel-equivariant construction. Exhaustive finite verification is complete for the explicitly defined twelve-vertex object, but an equivalent calculation could exist in unindexed literature. The proof has not received independent external mathematical validation.

## References
1. Philip Franklin, *A Six Color Problem*, Journal of Mathematics and Physics **13** (1934), 363–369, DOI 10.1002/sapm1934131363; graph identification and LCF notation also recorded in Eric Weisstein, *Franklin Graph*, MathWorld, https://mathworld.wolfram.com/FranklinGraph.html.
2. Richard Ehrenborg and Gábor Hetyei, *The topology of the independence complex*, European Journal of Combinatorics **27** (2006), 906–923, DOI 10.1016/j.ejc.2005.04.010.
3. Mario Marietti and Damiano Testa, *Cores of simplicial complexes*, arXiv:math/0703351v1 (first posted 2007-03-12), https://arxiv.org/abs/math/0703351.
4. Jonathan Ariel Barmak, *Star clusters in independence complexes of graphs*, arXiv:1007.0418v1 (first posted 2010-07-02), https://arxiv.org/abs/1007.0418.
