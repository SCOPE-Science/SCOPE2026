# Integral two-torsion and Moore-space summands in the first tetrahedral Johnson neighborhood complexes

## Finding

For an integer \(n\ge 4\), let \(J(n,3)\) be the simple graph whose vertices are the three-element subsets of \([n]\) and in which two distinct vertices are adjacent precisely when they have exactly two elements in common. Let \(\mathcal N(J(n,3))\) denote its **ordinary open-neighborhood complex**: a nonempty set of graph vertices is a simplex if and only if all its vertices are adjacent to a common graph vertex, which is not included merely by being the witness.

The first two genuinely tetrahedral cases admit the **integral homotopy classifications**

\[
\mathcal N(J(6,3))\simeq M(\mathbb Z/2,2)\vee\bigvee^{141}S^3,
\qquad
\mathcal N(J(7,3))\simeq M(\mathbb Z/2,2)\vee\bigvee^{771}S^3.
\]

Here \(M(\mathbb Z/2,2)\) is the based mapping cone of a map of degree two from \(S^2\) to \(S^2\). In particular, the only positive-degree integral homology groups in the two cases are

\[
\widetilde H_2\cong\mathbb Z/2,
\qquad
\widetilde H_3\cong\begin{cases}\mathbb Z^{141}&n=6,\\\mathbb Z^{771}&n=7.\end{cases}
\]

For comparison, \(\mathcal N(J(4,3))\simeq S^2\) and \(\mathcal N(J(5,3))\simeq\bigvee^{11}S^3\). Hence the earliest integral torsion in the natural rank-three Johnson sequence with \(n\ge4\) occurs at \(n=6\), and the same two-torsion persists at \(n=7\). No assertion is made for \(n\ge8\).

## Assumptions and scope

All spaces are finite abstract simplicial complexes with their usual geometric realizations; all homotopy equivalences are nonequivariant, and all homology assertions use integral coefficients. Every three-subset is a graph vertex, with vertices ordered lexicographically. Each graph vertex has exactly \(3(n-3)\) open neighbors. Its open-neighborhood simplex has that many vertices, hence dimension \(3(n-3)-1\). The complex is obtained from the union of all these simplices, with repeated faces identified.

The term *open* is essential: the scale-one graph-metric Vietoris–Rips complex of the Johnson graph is its **clique complex**, which differs sharply from this common-neighbor complex. The conclusion concerns exactly \(n=4,5,6,7\), not arbitrary Johnson ranks or all parameter values.

## Proof

**1. Complete, finite simplicial model.** List the vertices \(v_0,\ldots,v_{\binom n3-1}\) as lexicographically ordered three-subsets. For each center \(v_i\), form the set \(N_i=\{j:|v_i\cap v_j|=2\}\). For every nonempty subset of each \(N_i\), form its bitmask in the common vertex ordering, and remove duplicate masks. This enumerates **every** simplex, in both directions: the defining common-neighbor condition is exactly membership in one of those power sets. The resulting face vectors, indexed by dimensions starting at zero, are

\[
\begin{aligned}
 n=6:&\quad (20,180,960,2340,2520,1680,720,180,20),\\
 n=7:&\quad (35,525,4340,15960,27510,32340,27720,17325,7700,2310,420,35).
\end{aligned}
\]

There are respectively \(8620\) and \(136220\) nonempty faces.

**2. Exact acyclic discrete-Morse matchings.** For \(n=6\), visit the graph vertices in index order
\(4,1,2,3,0,5,6,\ldots,19\). For \(n=7\), visit in standard index order \(0,1,\ldots,34\). At vertex index \(i\), pair and remove every still-unpaired face \(\sigma\) that does not contain \(i\) with \(\sigma\cup\{i\}\), provided both faces are still present. Within one vertex step, these eligible pairs are disjoint, so their traversal order is immaterial. This is a matching of consecutive dimensions in the actual face poset.

For each pair, orient its Hasse edge upwards (smaller face to larger face) and every other cover downwards. The standalone verifier constructs the **entire** resulting directed Hasse graph and applies an exhaustive topological sort. It visits all \(8620\) or \(136220\) faces, proving there are no directed cycles; it explicitly processes respectively \(41940\) and \(839580\) cover relations. Forman's elementary acyclic-matching theorem therefore supplies homotopy-equivalent CW complexes whose critical-cell data are exactly

\[
\begin{array}{c|r|r|r|r}
 n&\text{pairs}&\text{critical vertices}&\text{critical 2-cells}&\text{critical 3-cells}\\\hline
 6&4238&1&1&142\\
 7&67723&1&1&772
\end{array}
\]

There are no critical cells in other dimensions, so the CW complexes have trivial one-skeleta and are simply connected. Both are obtained by attaching their three-cells to a single two-sphere.

**3. The *integral* attaching degrees.** Work with oriented simplices in increasing vertex order, so that the coefficient of the face missing vertex \(j\) is \((-1)^j\). For every matched lower two-simplex \(a\) and upper three-simplex \(b\), the incidence coefficient of \(a\) in \(\partial b\) is \(\pm1\). These pivots can be eliminated exactly, in a directed acyclic dependency order determined by their other two-faces. This is the standard integer cellular cancellation for a discrete-Morse matching; it produces the boundary \(\partial^M_3\) of the Morse CW model, and no division other than by a unit is needed. Cancellations in other adjacent dimensions do not change the remaining degree-three to degree-two boundary entries.

The verifier recomputes all orientation signs and all integer pivot eliminations from scratch. In the \(n=6\) case, the one-by-142 Morse boundary has \(31\) entries \(+2\), \(23\) entries \(-2\), and \(88\) zeros. In the \(n=7\) case, the one-by-772 row has \(125\) entries \(+2\), \(131\) entries \(-2\), one entry \(-4\), and \(515\) zeros. In both cases its entrywise greatest common divisor is exactly two.

The attaching maps of the three-cells lie in \(\pi_2(S^2)\cong\mathbb Z\), so their integral cellular degrees determine their homotopy classes. Unimodular changes of basis on the wedge of attaching two-spheres reduce the row to \((2,0,\ldots,0)\), yielding the mapping cone of the degree-two map together with the stated free three-sphere summands. This proves the two homotopy equivalences and the torsion assertion, not merely a mod-two Betti calculation.

**4. Preceding cases.** When \(n=4\), the Johnson graph is the complete graph on four vertices and its open-neighborhood complex is the boundary of a tetrahedron, namely \(S^2\). When \(n=5\), the same lexicographic toggle matching leaves one critical vertex, exactly eleven critical three-cells, and no other critical cells; the verifier also exhaustively checks acyclicity at this size. Hence the neighborhood complex is a wedge of eleven three-spheres. These exhaust all smaller defined ranks in the stated sequence.

## Verification

Run `python3 verify_johnson.py` with Python 3 and no third-party dependencies. The complete verifier reconstructs all graph adjacencies, all neighborhood-generated faces, every matched pair, all Hasse cover relations, and the topological-order acyclicity test; it then performs exact integer boundary cancellation and asserts the critical-cell counts and boundary gcd. It independently checks the preceding \(n=5\) critical-cell pattern and its acyclicity. The successful run ends with `VERIFY_OK n=6,7 integral Morse homotopy certificates; n=5 boundary check`.

Every finite case claimed is exhaustively enumerated. The listed exact computations are a finite proof because the theorem has no unbounded parameter quantifier. None of the homotopy conclusions follows by an invalid extrapolation from mod-two ranks. The smallest case is also identified symbolically as the boundary of a simplex.

## Relationship to prior work

Kahle's foundational study supplies the ordinary common-neighbor definition and connects neighborhood-complex topology to graph coloring; its theorems on random graphs do not compute these deterministic three-subset Johnson complexes. Matsushita develops general fundamental-group and higher-neighborhood constructions, rather than the integral three-dimensional attaching maps studied here.

A published scale-one Johnson-graph clique-complex collapse concerns all pairwise-adjacent collections, not the collections with a **common adjacent witness** studied here: the latter have maximal faces of dimensions eight and eleven in the displayed cases, far larger than the Johnson clique sizes. A published finite calculation of triangular-graph neighborhood homology concerns \(J(n,2)\) and mod-two dimensions, not the integral homotopy of \(J(n,3)\). Thus neither result implies this degree-two Moore-space summand or its two exact accompanying sphere counts. Searches under Johnson, tetrahedral Johnson, hypersimplex, neighborhood, graph-Hom, and integral torsion terminology did not locate an implication-equivalent calculation; that noncoverage is not a proof of global uniqueness.

## Limitations

There is no determination of \(\mathcal N(J(n,3))\) for \(n\ge8\), no general result for arbitrary Johnson ranks, no equivariant homotopy classification, and no information about induced persistence maps. The two finite certificates rely on complete enumeration and exact discrete-Morse arithmetic, provided in the standalone program. They require independent checking for scientific assurance; no independent audit or external formal certification is claimed. An equivalent result indexed under graph-Hom complexes or association schemes may exist outside the inspected literature.

## References

1. M. Kahle, *The neighborhood complex of a random graph*, arXiv:math/0512077, first posted 2005-12-04; J. Combin. Theory Ser. A 114 (2007), 380–387.
2. T. Matsushita, *Fundamental groups of neighborhood complexes*, arXiv:1210.2803, first posted 2012-10-10; J. Math. Sci. Univ. Tokyo 24 (2017), 321–353.
3. P. Shuldiner and R. W. Oldford, *The Clique Structure of Johnson Graphs*, arXiv:2208.12710 (2022); background for the structural distinction between Johnson cliques and neighborhoods.
