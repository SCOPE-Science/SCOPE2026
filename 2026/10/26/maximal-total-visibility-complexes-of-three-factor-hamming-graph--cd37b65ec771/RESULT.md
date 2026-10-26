# Maximal total-visibility complexes of three-factor Hamming graphs with binary coordinates

## Finding

Let \(G_{a,b}=K_2\square K_a\square K_b\) be the Cartesian product of complete graphs, with integers \(a,b\ge 2\). A **total mutual-visibility set** is a vertex set \(S\) such that every two vertices of the entire graph have a shortest path whose internal vertices avoid \(S\). Such a set is **maximal** if it has no strictly larger total mutual-visibility superset. The **lower total mutual-visibility number** \(\mu_{\mathrm t}^{-}(G)\) is the least cardinality of a maximal set.

**Theorem (binary-factor three-fold Hamming products).** Every \(G_{a,b}\) has \(\mu_{\mathrm t}^{-}(G_{a,b})=2\). Moreover, the number of maximal total mutual-visibility sets of cardinality two is exactly
\[
M_2(a,b)=ab+2b\,\mathbf 1_{\{a=2\}}+2a\,\mathbf 1_{\{b=2\}}+4\,\mathbf 1_{\{a=b=2\}}.
\]
These pairs are precisely the two endpoints of a complete two-vertex coordinate fiber, together with the four antipodal pairs when all three factors are binary. A two-vertex coordinate fiber is a pair obtained by fixing the other two coordinates and varying the coordinate whose factor is \(K_2\).

For the doubly binary subfamily \(J_m=K_2\square K_2\square K_m\), \(m\ge2\), the following stronger, complete classification holds. Every total mutual-visibility set is either (i) a subset supported on one pair of diagonally opposite binary cells, with each third-coordinate symbol used at most once, or (ii) a pair of adjacent binary cells at the same third-coordinate symbol. A set in (i) is maximal exactly when every symbol is used. Every set in (ii) is maximal.

Consequently, the polynomial enumerating **all** total mutual-visibility sets, including the empty set, and the polynomial enumerating only maximal ones are respectively
\[
T_m(z)=\sum_{S\,\mathrm{total}}z^{|S|}=2(1+2z)^m-1+4mz^2,
\qquad
F_m(z)=\sum_{S\,\mathrm{maximal\ total}}z^{|S|}=2^{m+1}z^m+4mz^2.
\]
For \(m=2\), the two terms of degree two in \(F_m\) are added. In particular \(J_m\) has \(2^{m+1}+4m\) maximal sets, its lower total mutual-visibility number is \(2\), and its upper total mutual-visibility number is \(m\).

There is also a topological interpretation. Let \(\Delta_m\) be the simplicial complex of all total mutual-visibility sets in \(J_m\). For every \(m\ge2\),
\[
\Delta_m\simeq S^{m-1}\vee S^{m-1}\vee\bigvee^{4m-1}S^1.
\]
Thus the complex is nonpure for \(m\ge3\). For \(m=2\) this expression means a wedge of nine circles; for \(m\ge3\), its first Betti number is \(4m-1\) and its Betti number in dimension \(m-1\) is two.

The earlier established upper value \(\mu_{\mathrm t}(G_{a,b})=a+b-2\) then shows a sharp unbounded difference \(\mu_{\mathrm t}(G_{a,b})-\mu_{\mathrm t}^{-}(G_{a,b})=a+b-4\) within these natural three-factor products. That upper-value theorem is cited as prior work, not claimed here.

## Assumptions and scope

All graphs are finite, simple, and have distinguished coordinate positions. The vertex set of \(G_{a,b}\) is \(\{0,1\}\times[a]\times[b]\), where \([q]=\{1,\ldots,q\}\); two vertices are adjacent precisely when they differ in one coordinate. Thus distance equals the number of disagreeing coordinates. Parameters \(a,b,m\) are integers satisfying \(a,b,m\ge2\), and vertex subsets are counted as distinct whenever their actual coordinate elements differ. The enumerating variable \(z\) is formal. A facet of \(\Delta_m\) means a set maximal by inclusion, **not** necessarily of maximum cardinality.

We use the established Hamming-graph visibility criterion of Bujtás, Klavžar, and Tian: a set is totally mutually visible if and only if it contains no pair at Hamming distance exactly two (Theorem 6 of [2]). This equivalence is not new. All classification, enumeration, minimum-size-pair, and homotopy assertions below are derived from that criterion.

## Proof

**1. Classify the inclusion-maximal two-element sets of \(G_{a,b}\).** By [2, Theorem 6], a two-element set \(\{u,v\}\) is feasible precisely when \(d(u,v)\) equals \(1\) or \(3\). A singleton cannot be maximal: add any neighbor of its vertex, obtaining a feasible pair at distance one.

First suppose \(d(u,v)=1\), so exactly one coordinate varies. If that coordinate has at least three available values, choose a third value in that same fiber; the added vertex is at distance one from both selected vertices, so the pair is not maximal. If the varying coordinate is binary, let \(w\) be any vertex outside the pair. Since the two binary values are exhausted, \(w\) agrees in that coordinate with exactly one endpoint. Let \(r\in\{1,2\}\) count its changes in the other two coordinates. Its distances to the endpoints are \(r\) and \(r+1\); one of these is exactly two. Thus no \(w\) may be adjoined, and the pair is maximal.

Next suppose \(d(u,v)=3\), so the endpoints differ in all three coordinates. If some coordinate has a third value different from both endpoint values, replace just that coordinate of \(u\) by this third value. The resulting vertex is at distances one and three from \(u\) and \(v\), respectively, so the pair extends. If all three factors are binary, any other vertex differs from \(u\) in \(r\in\{1,2\}\) coordinates and from \(v\) in \(3-r\); one distance equals two, preventing extension. Therefore only fully binary antipodal pairs are maximal in this case.

A binary coordinate \(i\) contributes exactly the product of the other two factor sizes as its number of coordinate-fiber pairs. The first coordinate always contributes \(ab\), the second contributes \(2b\) only for \(a=2\), and the third contributes \(2a\) only for \(b=2\). If all three are binary, the four antipodal pairs give a final contribution of four. These types are disjoint, proving the displayed formula for \(M_2(a,b)\) and \(\mu_{\mathrm t}^{-}(G_{a,b})=2\).

**2. Structural classification in \(J_m\).** View its vertices as \((c,t)\), with a binary cell \(c\in\{00,01,10,11\}\) and a symbol \(t\in[m]\). The four cells make a square: cells are *adjacent* if their binary strings differ in one coordinate, and *opposite* if they differ in two.

If a feasible set contains \((c,t)\) and \((c',t')\) in adjacent cells, then \(t=t'\), since otherwise the pair has Hamming distance two. Furthermore no third vertex can be added to this adjacent pair. Indeed, any other vertex at the same symbol lies in one of the other two cells, opposite to at least one endpoint, and is distance two from that endpoint. Any vertex at a different symbol lies in a cell adjacent to at least one of the two selected cells, hence is distance two from that selected vertex. So every adjacent pair sharing a symbol is a facet, and no larger feasible set contains an adjacent pair.

If no adjacent-cell pair occurs, every occupied cell lies in one of the two diagonals of the square. Within a fixed diagonal, two vertices in opposite cells at the same symbol would be distance two, while all other pairs in this diagonal are at distances one or three. Therefore a feasible set supported on the diagonal may assign to each symbol either no vertex or one of the two opposite cells, independently. Conversely every such assignment is feasible.

**3. Count all sets and facets.** Each diagonal yields \((1+2z)^m\): for each symbol, omit it (weight one) or use it in either cell (weight \(2z\)). The two diagonal families share only the empty set. The \(4m\) adjacent-cell pairs at equal symbols are not counted by either diagonal family, and their singletons were already counted. This proves
\[
T_m(z)=2(1+2z)^m-1+4mz^2.
\]
A diagonal set omitting any symbol can be enlarged at a cell of that diagonal. Conversely, if all \(m\) symbols are used, no additional diagonal vertex is possible. An outside-diagonal candidate has some symbol \(t\) and is at binary distance one from both diagonal cells. Since \(m\ge2\), there is a selected vertex with a different symbol, at total distance two from the candidate; hence the diagonal set is maximal. It has \(m\) vertices and there are \(2^m\) choices per diagonal. Together with the \(4m\) adjacent-pair facets, this establishes \(F_m\), the facet count, and the two extreme cardinalities. In the special case \(m=2\), all facets are of size two, but the two types remain disjoint.

**4. Topology.** The simplicial subcomplex supported on either diagonal is the join of \(m\) two-point discrete spaces: for each symbol, one can choose either opposite cell but never both. This is the boundary of the \(m\)-dimensional cross-polytope and hence a sphere \(S^{m-1}\). The two diagonal spheres have disjoint vertex sets. Their union is connected by precisely the \(4m\) extra adjacent-pair edges, none belonging to a simplex of dimension at least two. Both spheres are path connected for \(m\ge2\). The elementary graph-of-spaces homotopy calculation for two connected spaces linked by \(r\) edges gives their wedge together with \(r-1\) circles: choose one bridge to connect the spaces, and each remaining bridge adds one loop. Applying this with \(r=4m\) gives the homotopy equivalence. Since for \(m\ge3\) some facets have cardinality two and others have cardinality \(m\), nonpurity follows. This finishes the proof.

## Verification

The standalone program `verify.py` independently implements the **original all-pairs geodesic definition** (not just the distance-two criterion) for all \(4352\) vertex subsets across \(K_2\square K_2\square K_2\) and \(K_2\square K_2\square K_3\). These agree exactly with distance-two pair avoidance.

For \(m=2,\ldots,8\), it then builds the compatibility graph whose edges join pairs not at distance two, independently enumerates its maximal cliques and all cliques, and compares their actual labeled vertex sets and coefficient counts with the asserted facet families and both polynomials. This checks \(1156\) facets and \(19807\) feasible subsets (including empty sets). For each of \(25\) parameter choices \(2\le a,b\le6\), an independent exhaustive two-vertex maximality test checks the displayed formula, encompassing \(484\) maximal pairs. The exact program and recorded output accompany this document; invoke `python verify.py` to reproduce. Finite computation corroborates but does not replace the proof for arbitrary parameters.

## Relationship to prior work

Brešar and Yero [1] introduced and studied the lower total mutual-visibility number, proved general bounds and examples, and gave the two-factor formula \(\mu_{\mathrm t}^{-}(K_a\square K_b)=\min\{a,b\}\) for \(a,b\ge3\) (their Proposition 17). Their paper also motivates lower visibility in Cartesian products. Its named product results concern two-factor complete products and products of paths, not this three-factor facet and pair census.

Bujtás, Klavžar, and Tian [2] established the general Hamming-graph equivalence between total mutual-visibility and the absence of selected pairs at Hamming distance two (Theorem 6), and the **maximum** \(\mu_{\mathrm t}(K_2\square K_a\square K_b)=a+b-2\) (Theorem 9). The present work takes their criterion as a premise. Its new statement is a classification of inclusion-maximal sets, exact counts of all sets and facets for two binary factors, the minimum-size facet census with one binary factor, and a topological description. The known maximum and the distance-two criterion themselves are not claimed new. In particular, the difference between a membership characterization and an exact face enumerator requires the four-cell classification in the proof above.

A 2025 work on the *mutual*-visibility polynomial [3] addresses the weaker requirement that only selected vertices see one another; its abstract was examined, but its full text was not used to exclude possible overlap. The complete classification and its topological consequences should therefore be understood as a mathematically proved result with remaining bibliographic-priority uncertainty, not as independently certified novelty.

## Limitations

The complete face and facet polynomials and homotopy type are proved only for the three-factor family with two binary factors. For general \(K_2\square K_a\square K_b\), only the lower invariant and its two-vertex facet count are classified here; larger facets are not enumerated. No analogous claims are made for four or more factors, nor for noncomplete Cartesian factors. The cardinalities and Betti numbers use coordinate-distinguished vertices. The method depends on the published Hamming visibility equivalence, independently checked here only for small finite instances. No independently conducted audit or exhaustive all-literature priority certification has been performed.

## References

[1] B. Brešar and I. G. Yero, *Lower (total) mutual visibility in graphs*, arXiv:2307.02951, first public version 2023-07-06; subsequently *Applied Mathematics and Computation* 465 (2024), 128411. https://arxiv.org/abs/2307.02951

[2] C. Bujtás, S. Klavžar, and J. Tian, *Total mutual-visibility in Hamming graphs*, arXiv:2307.05168, first public version 2023-07-11; subsequently *Opuscula Mathematica* 45 (2025), 63–78. https://arxiv.org/abs/2307.05168

[3] Tonny K B and Shikhi M, *On the Visibility Polynomial of Graphs*, arXiv:2507.01851, first public version 2025-07-02 (abstract-level comparison only). https://arxiv.org/abs/2507.01851
