# Ten facet-symmetry orbits of the Heawood Lipschitz-free ball

## Finding
Let \(H\) be the Heawood graph, the point-line incidence graph of the Fano plane. Give its fourteen vertices the unit-edge shortest-path metric, and let \(B\) denote the unit ball of the thirteen-dimensional **real** Lipschitz-free space \(\mathcal F(H)\). Then \(B\) has **exactly \(660\) facets**. Under the full Heawood graph automorphism group and global sign reversal, its facets form **exactly ten orbits**, of sizes
\[
168,\quad112,\quad112,\quad84,\quad56,\quad42,\quad28,\quad28,\quad28,\quad2.
\]
Every facet contains exactly \(21\) vertices of \(B\). Their normalized supporting potentials use two, three or four distinct integer heights, with exact multiplicities \(2\), \(252\) and \(406\), respectively.

Here are representatives of all ten orbits, with potential values given first at the seven points and then at the seven lines. Both types are indexed by \(1,\ldots,7\) interpreted as nonzero binary three-vectors. In each row the first point has value zero. The representatives are **facet normals**, not graph vertices.

| Orbit size | Seven point heights | Seven line heights |
| ---: | --- | --- |
| 168 | \((0,-2,-2,-2,-2,-2,-2)\) | \((-3,-1,-3,-1,-1,-1,-1)\) |
| 112 | \((0,-2,-2,-2,-2,-2,-2)\) | \((-3,-1,-3,-1,-3,-1,-1)\) |
| 112 | \((0,-2,-2,-2,0,-2,0)\) | \((-1,-1,-1,-1,-1,-1,-1)\) |
| 84 | \((0,-2,-2,-2,-2,-2,0)\) | \((-1,-1,-1,-1,-1,-1,-1)\) |
| 56 | \((0,-2,-2,-2,-2,-2,-2)\) | \((-3,-1,-1,-1,-1,-1,-1)\) |
| 42 | \((0,-2,-2,-2,-2,-2,0)\) | \((-3,-1,-1,-1,-1,-1,-3)\) |
| 28 | \((0,-2,-2,-2,-2,-2,-2)\) | \((-3,-1,-3,-1,-3,-1,-3)\) |
| 28 | \((0,-2,-2,-2,-2,-2,-2)\) | \((-1,-1,-1,-1,-1,-1,-1)\) |
| 28 | \((0,-2,-2,-2,-2,0,0)\) | \((-1,-1,-1,-1,-1,-1,-1)\) |
| 2 | \((0,0,0,0,0,0,0)\) | \((-1,-1,-1,-1,-1,-1,-1)\) |

## Assumptions and scope
Write \(P=L=\mathbb F_2^3\setminus\{0\}\), treating these as disjoint copies. A point \(p\in P\) is joined to a line \(q\in L\) exactly when the binary dot product \(p\cdot q\) vanishes. Each line contains three points, every pair of distinct points lies on one line, and the seven lines meet pairwise. The vertex labeling for the table uses binary integers \(1,\ldots,7\) and the root point \(p=1\). Real functions \(f\colon P\sqcup L\to\mathbb R\) are normalized by \(f(1)=0\). The Lipschitz norm is the maximum of \(|f(u)-f(v)|\) over the \(21\) incidence edges.

The graph metric is essential: the free-space ball equals the convex hull of the \(42\) oriented unit-edge molecules. A pair at larger distance contributes no new vertex, because its normalized molecule is a convex combination of oriented edge molecules along a shortest path. The graph is connected and bipartite, and its free space has real dimension \(14-1=13\).

## Proof
**1. Facet criterion.** The dual Lipschitz ball is the polytope defined, after fixing \(f(1)=0\), by the \(42\) inequalities \(|f(u)-f(v)|\le1\) for incidence edges. Its vertices correspond to facets of the polar free-space ball. For any such \(f\), the active inequalities have incidence-matrix rank \(14-c\), where \(c\) is the number of connected components of the graph of edges on which \(|f(u)-f(v)|=1\). Therefore \(f\) is a dual vertex precisely when its tight-edge graph is connected. Integrality follows by summing integer unit differences along an active spanning tree. This is the standard facet criterion, reconstructed here in these coordinates.

Because \(H\) is bipartite, the endpoint parity of the integer heights alternates along every tight edge. If the tight edges connect all vertices, all point heights have one parity and all line heights the opposite parity. Every original incidence edge therefore joins values whose difference is an odd integer of absolute value at most one. Hence **every edge is tight**. Conversely, an integer potential with absolute difference exactly one along all incidence edges defines a facet because the whole graph is connected. Thus the facets are in bijection with normalized integer graph homomorphisms to the two-way infinite path, with unit steps on all \(21\) edges.

**2. Point-level classification.** Every two Fano points have a common line. Since both point heights differ by one in absolute value from that line's height, their difference is \(0\) or \(\pm2\). In particular all point heights are even and differ pairwise by at most two. With the first point normalized to zero, either all are zero, or every point height lies in \(\{0,2\}\), or every point height lies in \(\{-2,0\}\). The two families overlap only when all seven point heights vanish.

Fix a subset \(S\) of \(k\) of the six nonroot points to take height \(2\), and assign zero to the other points. A line incident to both point-height classes is forced to height \(1\). A line whose three points have the same height has exactly two admissible heights, one above and one below those points. Write \(m(S)\) for the number of such monochromatic lines. Every pair consisting of one point of \(S\) and one point outside \(S\) lies on exactly one Fano line. Each mixed line contains either one or two points of \(S\), so it accounts for exactly two cross pairs. Therefore
\[
 m(S)=7-\frac{k(7-k)}2.
\]
For this point pattern, the \(m(S)\) monochromatic lines each offer two independent height choices, while all other lines are forced. The number of facets in the positive envelope is consequently
\[
 T=\sum_{k=0}^{6}\binom6k\,2^{7-k(7-k)/2}
 =128+96+60+40+30+24+16=394.
\]
Negating point heights gives another \(394\) facet normals, but the \(2^7=128\) normals with all point heights zero have been counted twice. Thus the exact total is
\[
 F(H)=2T-2^7=\boxed{660}.
\]
If all point heights vanish, exactly two line assignments use only two heights, and the other \(126\) use three. For a nonconstant point assignment, the unique choice putting every line between its incident extreme point heights uses three heights, yielding \(2(2^6-1)=126\) more. Any other choice has four heights: no Fano line monochromatic in \(S\) can be disjoint from a Fano line monochromatic in its complement, as two Fano lines always intersect. Hence the height-level counts are \(2,252,406\), respectively. Every original edge is tight, so every facet uses precisely one signed molecule per graph edge, giving \(21\) vertices.

**3. Ten symmetry orbits.** The point-line incidence graph has \(336\) vertex automorphisms. Exactly \(168=|\mathrm{GL}(3,2)|\) preserve the point/line classes: such a symmetry is an invertible binary linear map on the point vectors, with contragredient action on line normals. Swapping the point and line classes via the symmetric incidence relation doubles this group. Combining these automorphisms with global negation of a potential yields at most \(672\) transformations, with output renormalized at point \(1\).

The complete orbit calculation is finite and exhaustively certified by the accompanying standard-Python program `verify_heawood.py`: it constructs all \(168\) invertible three-bit linear maps and both point/line actions, verifies preservation of every one of the \(21\) incidence edges, constructs all \(660\) facet normals, and partitions that entire set into disjoint orbits. It returns the ten representatives displayed above and orbit cardinalities \(168,112,112,84,56,42,28,28,28,2\). Their sum is \(660\); disjointness and invariance are checked as set equalities rather than inferred from numerical totals. The code's finite-loop exhaustion establishes precisely the asserted orbit classification, not a statement about higher-dimensional projective planes.

## Verification
Run `python3 verify_heawood.py` from the same directory as this document. The program uses only the Python 3 standard library. It independently enumerates facet potentials by (a) Fano point patterns and line-height choices and (b) all possible \(-1,0,1\) increments on the edges of a spanning tree, checking all other graph-edge inequalities and tight-edge connectivity. Both procedures return the exact same \(660\)-element set. It separately generates the \(336\) graph automorphisms, verifies their incidence preservation, and checks the full orbit partition and displayed representatives. Its final message is `ALL EXACT CHECKS PASSED`.

The analytic count \(660\) does not depend on this computation; the finite exhaustive program certifies the more refined ten-orbit classification. No statistical sampling, floating-point tolerances or unbounded searches are used.

## Relationship to prior work
Higashitani, Jochemko and Michałek (first public 2018) give the general integral tight-edge facet criterion and formulas for complete multipartite graphs. Their Theorem 3.1 supplies a starting point, but their explicitly enumerated families do not include the Fano incidence graph. D'Alì, Delucchi and Michałek (2019 preprint) revisit this criterion and derive graph-family enumerations and a planar-bipartite dual-flow formula; the Heawood graph is **nonplanar**, so this latter formula does not evaluate its facets. Chen, Davis and Korchevskaia (2021 preprint) characterize facets by maximal bipartite subgraphs; here that subgraph is the whole Heawood graph, and their result does not supply its \(660\) individual orientations or symmetry orbits. Braun and Bruegge (2022 preprint) analyze sparse graph families and small-order extremal tables, not this Fano-incidence orbit census. Deza and Dutour Sikirić (2015) do list **Heawood cut-polytope** facets, but their polytope is the convex hull of \(2^{13}\) cut vectors in a \(21\)-dimensional edge-coordinate space, with \(5{,}361{,}194\) facets and nine symmetry orbits; it is not this \(13\)-dimensional symmetric edge polytope with \(42\) vertices. Consequently, neither their tabulated invariant nor their nine orbit classes imply the present ten-orbit classification.

The general correspondence between tight-height functions and facets is **not claimed as new**. The contribution is its exact Fano-plane count, closed point-subset classification, level distribution, and complete ten-orbit decomposition for this canonical thirteen-dimensional transportation-norm ball. A general combinatorial criterion can imply a numerical invariant after a nontrivial evaluation without already containing that evaluation. The literature comparison is best-knowledge, not a proof that no independent calculation exists.

## Limitations
The claim concerns the real free space over this fixed finite graph, not arbitrary finite projective planes, graph-weight perturbations, full face vectors or automorphism groups of the polytope beyond the specified graph automorphism and sign action. The stated ten orbits use precisely that specified group, not necessarily every affine symmetry of the polytope. An existing unindexed computation or inaccessible catalog could contain the same facet count or orbit decomposition. Computational checks are exhaustive for the finite graph but are not an independent scientific audit.

## References
1. A. Higashitani, K. Jochemko and M. Michałek, *Arithmetic aspects of symmetric edge polytopes*, arXiv:1807.07678v1, first publicly posted 2018-07-20; Theorem 3.1 and Proposition 3.4.
2. A. D'Alì, E. Delucchi and M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1, first publicly posted 2019-10-11; Section 3 and Section 4.5.
3. T. Chen, R. Davis and E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315v1, first publicly posted 2021-07-26; Theorem 3 and Section 4.3.
4. B. Braun and K. Bruegge, *Facets of symmetric edge polytopes for graphs with few edges*, arXiv:2201.13303v1, first publicly posted 2022-01-31; extremal tables and sparse-graph formulas.
5. M. Deza and M. Dutour Sikirić, *Enumeration of the facets of cut polytopes over some highly symmetric graphs*, arXiv:1501.05407, first circulated 2015; Table 2 (a different polytope construction).
