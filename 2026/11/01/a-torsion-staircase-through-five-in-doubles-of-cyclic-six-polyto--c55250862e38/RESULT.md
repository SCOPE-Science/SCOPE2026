# A torsion staircase through five in doubles of cyclic six-polytopes

## Finding
For every integer \(7\le m\le16\), let \(K_m=\partial C(m,6)\) be the boundary complex of the six-dimensional cyclic polytope with ordered vertices \(0,1,\ldots,m-1\), and let \(Y_m=D(K_m)\) be its simplicial double. Define the double to have as vertices unordered pairs \(\{a,b\}\) of vertices of \(K_m\). A collection of \(k\) such pairs is a face precisely when its pairs are disjoint and their union is a face of \(K_m\). The complexes \(Y_m\) are two-dimensional. Their **complete reduced integral homology** in the specified range is:

| \(m\) | \(\widetilde H_1(Y_m;\mathbb Z)\) | \(\widetilde H_2(Y_m;\mathbb Z)\) |
|---:|:---|---:|
| 7 | \(\mathbb Z/3\) | \(\mathbb Z^{20}\) |
| 8 | \(\mathbb Z^{15}\) | \(\mathbb Z^{78}\) |
| 9 | \(0\) | \(\mathbb Z^{134}\) |
| 10 | \(\mathbb Z^{24}\oplus\mathbb Z/2\) | \(\mathbb Z^{263}\) |
| 11 | \(0\) | \(\mathbb Z^{384}\) |
| 12 | \(\mathbb Z^{35}\oplus\mathbb Z/3\) | \(\mathbb Z^{610}\) |
| 13 | \(0\) | \(\mathbb Z^{818}\) |
| 14 | \(\mathbb Z^{48}\oplus\mathbb Z/4\) | \(\mathbb Z^{1167}\) |
| 15 | \(0\) | \(\mathbb Z^{1484}\) |
| 16 | \(\mathbb Z^{63}\oplus\mathbb Z/5\) | \(\mathbb Z^{1982}\) |

All other reduced integral homology groups vanish in this range. In particular the first occurrence of an order-five class in this natural family is at \(m=16\) (with the range beginning at the smallest six-dimensional cyclic polytope, \(m=7\)). The successive even parameters \(m=10,12,14,16\) exhibit torsion of exact orders \(2,3,4,5\), respectively. This is a **finite classification**, not an infinite-family formula.

## Assumptions and scope
Here \(C(m,6)\) is a cyclic polytope with vertices \(v_0,\ldots,v_{m-1}\) in moment-curve order. The facets of its simplicial boundary complex are exactly the six-element subsets \(F\subseteq\{0,\ldots,m-1\}\) satisfying Gale's evenness criterion: for every pair \(a<b\) not in \(F\), the number of elements \(f\in F\) with \(a<f<b\) is even. Any face of the boundary lies in at least one such facet. The double uses **disjoint unordered edges** whose full union is a face; disjointness alone is insufficient. Since the boundary has six-vertex facets, its double has dimension at most two, and every listed complex has triangles. Homology is unreduced only in dimension zero; all reduced groups are specified above.

## Proof
**1. Exhaustive construction.** For each \(m\) in the stated range, enumerate all \(\binom m6\) six-element candidates and retain exactly those satisfying Gale evenness. For every retained facet, enumerate every two-, four-, and six-element subset and all their perfect pairings. Replace each pairing by the sorted tuple of its constituent unordered pairs, and take the set-union over facets. A face of the double necessarily has a union that lies in a facet, and every enumerated matching has this property. Hence this procedure generates **all and only** the simplices of \(Y_m\). The recorded number of original polytope facets is
\[ (7,16,30,50,77,112,156,210,275,352) \]
for \(m=7,\ldots,16\), respectively. Their double face vectors \((f_0,f_1,f_2)\) are, in order,
\[
(21,105,105),(28,204,240),(36,351,450),(45,555,750),
(55,825,1155),(66,1170,1680),(78,1599,2340),
(91,2121,3150),(105,2745,4125),(120,3480,5280).
\]

**2. Acyclic discrete-Morse reduction.** Label each double vertex by its lexicographic position among all pairs of the original \(m\) vertices. Start with all nonempty simplices unpaired. For each double vertex \(v\) in order, consider the still-unpaired simplices not containing \(v\), in increasing order of dimension and then lexicographically. Pair a simplex \(\sigma\) with \(\sigma\cup\{v\}\) whenever both remain unpaired. Construct the entire directed Hasse graph of the resulting matching: reverse each matched cover relation and direct every unmatched cover relation downward. The attached verifier checks all incidences and topologically sorts the graph, proving acyclicity rather than assuming it. The critical-cell counts in dimensions \((0,1,2)\) are
\[
(1,7,27),(1,23,86),(1,33,167),(1,47,286),
(1,63,447),(1,81,656),(1,101,919),(1,123,1242),
(1,147,1631),(1,173,2092).
\]
This is a finite and fully reproducible discrete-Morse CW reduction, preserving integral homology.

**3. Exact signed Morse differential.** Orient each simplex by ascending vertex labels. The unique critical zero-cell makes the Morse boundary in degree one zero. To calculate the degree-two differential, project each edge \(e\) onto the free abelian group on critical edges. The projection of a critical edge is its own basis vector, and the projection of an edge matched to a vertex is zero. If \(e\) is paired to a triangle \(T\), let \([T:e]\in\{\pm1\}\) denote the usual oriented incidence. The projection is recursively
\[
P(e)=-[T:e]^{-1}\sum_{e'\subset T,\ e'\ne e}[T:e']P(e').
\]
By the verified acyclic matching, this recursion terminates. For each critical triangle \(t\), the Morse boundary is \(\sum_{e\subset t}[t:e]P(e)\). Thus all coefficients and signs are computed as integers, not inferred from modular ranks. Apply exact integer Hermite normal form followed by Smith normal form. In the order \(m=7,\ldots,16\), the resulting matrix ranks are
\[7,8,33,23,63,46,101,75,147,110.\]
All nonzero Smith invariant factors are \(1\) except for a **single factor** equal to \(3,2,3,4,5\) at \(m=7,10,12,14,16\), respectively. The remaining cases have only unit nonzero factors. Thus the invariant-factor theorem gives the displayed first homology, and the free kernel gives the displayed second homology. No dimensions outside \(0,1,2\) occur. This proves the entire table.

## Verification
Run `python3 verify.py` with the declared `requirements.txt`. The script independently reconstructs every double from Gale facets, checks that every simplex was generated and every matching pair is valid, counts every Hasse incidence, topologically verifies acyclicity, computes every signed integral Morse boundary, calculates Hermite and Smith normal forms using exact arithmetic, and checks each displayed group. It also computes an independent mod-two rank on the **original, unreduced simplicial boundary matrices** for every parameter. At the final case \(m=16\), there are \(352\) polytope facets, \(120\) double vertices, \(3480\) double edges, and \(5280\) double triangles; \(3307\) pairs leave \((1,173,2092)\) critical cells, and the Morse \(173\)-by-\(2092\) boundary has rank \(110\) with invariant factors \(1\) repeated \(109\) times and \(5\) once. Its rank modulo five is \(109\) and modulo two, three, seven and eleven is \(110\). These modular ranks are cross-checks; the exact integral Smith computation certifies torsion.

## Relationship to prior work
Lesh, Schreiner and Wahl (arXiv:2506.10436v1, first publicly posted 2025-06-12) introduce doubling for general simplicial complexes and prove connectivity bounds in terms of weak Cohen–Macaulay dimensions. Their construction is used here, but their theorem does **not** compute integral homology for doubles of six-dimensional cyclic-polytope boundaries or supply any of the displayed torsion groups. The case of doubling a full simplex is the classical matching complex of a complete graph; the present cyclic boundary conditions remove faces and change the complex. Jonsson's five-torsion theorem concerns the distinct ordinary matching complex of a complete graph on fourteen vertices. Consequently neither source implies the displayed classification. The identified gap is a natural low-dimensional instance of the recently introduced doubling construction.

## Limitations
The calculation proves only the ten indicated parameters and their reduced integral homology. The observed even-parameter pattern is not asserted beyond \(m=16\). The result does not classify homotopy types, higher homotopy groups, or automorphism representations. Algebraic chain calculations do not by themselves provide any purported external or independent validation. Equivalent unindexed computations remain possible; novelty is assessed relative to the sources and searches stated in the accompanying review.

## References
1. Kathryn Lesh, Bridget Schreiner, Nathalie Wahl, *The double of a simplicial complex*, arXiv:2506.10436v1 (2025-06-12), https://arxiv.org/abs/2506.10436 . Definition 2.1 and Theorem A.
2. Jakob Jonsson, *Five-Torsion in the Homology of the Matching Complex on 14 Vertices*, arXiv:1203.5650 (2012), https://arxiv.org/abs/1203.5650 . Distinct ordinary matching-complex torsion comparison.
3. Margaret M. Bayer and Tibor Bisztriczky, *On Gale and braxial polytopes*, arXiv:math/0610940 (2006), https://arxiv.org/abs/math/0610940 . Background on Gale's evenness criterion.
