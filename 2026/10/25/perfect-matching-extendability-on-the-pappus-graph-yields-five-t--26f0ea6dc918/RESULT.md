# Perfect-matching extendability on the Pappus graph yields five three-spheres and one four-sphere

## Finding
Let \(P\) be the eighteen-vertex cubic Pappus graph, and let \(\mathcal P(P)\) be the simplicial complex of edge sets extendible to a perfect matching of \(P\). Then
\[
\mathcal P(P)\simeq\bigvee^{5}S^3\vee S^4.
\]
Thus \(\widetilde H_3(\mathcal P(P);\mathbb Z)\cong\mathbb Z^5\), \(\widetilde H_4(\mathcal P(P);\mathbb Z)\cong\mathbb Z\), and all other reduced integral homology groups vanish. This is a complete integral homotopy classification, not a field-homology inference.

## Assumptions and scope
Fix graph vertices \(0,\ldots,17\). Begin with the eighteen cycle edges \(\{i,i+1\pmod {18}\}\); add chords \(\{i,i+s_i\pmod {18}\}\), where the LCF shift sequence is `[5,7,-7,7,-7,-5]` repeated three times. Duplicate unordered edges are ignored. The resulting simple cubic graph has twenty-seven edges, indexed \(0,\ldots,26\) in lexicographic order. A perfect matching meets every graph vertex exactly once, so it contains nine graph edges. The complex vertices are the twenty-seven graph edges; its nonempty faces are precisely the nonempty subsets of the graph's perfect matchings. The empty face is used for enumeration only, not as a nonempty cell. Homotopy is ordinary geometric-realization homotopy.

This is the *perfect-matching extendability* complex, not the ordinary matching complex of all disjoint edge sets. No weighted matching, arbitrary hypergraph, or family-wide claim is made.

## Proof
**Complete finite face description.** Starting with all graph vertices unmatched, recursively choose the least unmatched vertex and match it to each available neighbor. This enumerates every perfect matching exactly once. There are forty-two. Enumerating all their bitmask subsets and removing duplicates gives the nonempty face vector, by increasing cardinality,
\[
(27,297,1575,3780,4752,3456,1512,378,42),
\]
which totals \(15{,}819\) faces and makes the complex pure of dimension eight. The accompanying `verify_pappus_pm.py` constructs the graph and repeats this full enumeration without external datasets.

**Acyclic matching certificate.** Orient the nonempty-face poset's incidence arrows downward except along specified paired inclusions, which point upward. Reserve the singleton complex vertex with graph-edge index \(25\) as critical. At every subsequent stage, toggle the index \(p\) in the fixed order

`[25,4,11,10,26,23,7,1,15,2,14,21,24,5,12,3,9,6,8,17,20,13,0,18,19,16,22]`.

At each stage pair every remaining face \(\sigma\) without \(p\) to \(\sigma\cup\{p\}\), provided both are present and neither has been paired. There are exactly \(7{,}905\) pairs. The nine unmatched faces consist of one zero-cell, one two-cell, six three-cells, and one four-cell. Explicitly forming all \(78{,}921\) covering incidences and topologically sorting the directed Hasse graph visits all \(15{,}819\) nonempty faces. Therefore the matching is acyclic and produces a CW model with only these nine critical cells by discrete Morse theory.

**Signed integral attaching degrees.** Orient every simplex by ascending graph-edge index. For every oriented matched pair \((u,v)\), with \(u\) a codimension-one face of \(v\), eliminate the unit incidence \([v:u]=\pm1\) from the simplicial differential. The resulting finite gradient recursion projects critical-cell boundaries to lower critical cells; acyclicity guarantees termination and no denominators arise. Ordering critical cells by their face-bitmask values, the differential from six critical three-cells to the single two-cell is
\[
\partial_3=\begin{pmatrix}0&-1&-1&1&0&0\end{pmatrix},
\]
while the boundary from the one four-cell to the six three-cells is identically zero:
\[
\partial_4=\begin{pmatrix}0&0&0&0&0&0\end{pmatrix}^{\mathsf T}.
\]
The standalone verifier reconstructs these matrices from oriented simplicial incidences, rather than accepting the displayed entries as data. The nonzero unit in \(\partial_3\) permits a cellular cancellation of the two-cell with one three-cell. There are no critical one-cells; the resulting three-skeleton has one zero-cell and five three-cells, hence is \(\bigvee^5S^3\). Its Hurewicz map \(\pi_3\to H_3\) is an isomorphism, since the space is two-connected. Because \(\partial_4=0\), the attaching map of the remaining four-cell has zero Hurewicz class in \(\mathbb Z^5\) and hence is nullhomotopic. Attaching the four-cell therefore wedges on \(S^4\). This proves the announced integral homotopy equivalence.

**Independent consistency checks.** Separate bitset Gaussian elimination of every full simplicial boundary over \(\mathbb F_2\), without relying on the Morse matching, gives boundary ranks \((0,26,271,1304,2471,2280,1176,336,42)\) in dimensions zero through eight. The resulting reduced mod-two Betti ranks are five in dimension three and one in dimension four, and zero otherwise. These field computations corroborate, but do not replace, the integral attaching calculation.

## Verification
From the two packaged evidence files, execute `python3 verify_pappus_pm.py` with a current Python 3 interpreter and no external packages. The script asserts the LCF graph, all forty-two perfect matchings and their subset faces; enumerates and checks all matched pairs and directed face incidences; checks acyclicity with an exhaustive topological sort; derives the exact signed integral Morse boundaries; calculates independently every full mod-two simplicial boundary rank; and counts matching-extension obstructions. It must print `VERIFY_OK`, followed by the counts and matrices copied in `verification_output.txt`.

Independent exhaustive enumeration of all graph matchings gives \(35{,}367\) nonempty ordinary matching faces. Precisely \(19{,}548\) of these do not lie in \(\mathcal P(P)\). Of the inclusion-minimal nonextendible matchings, 144 contain three edges and 351 contain four; every proper subset of such a matching is extendible. The distinction from the ordinary complex is explicit and not merely terminological.

## Relationship to prior work
Kozlov's 2005 work on finite combinatorial simple homotopy gives an archive-era methodological foundation for poset reductions, not this graph-specific classification. The Pappus–Desargues graph literature identifies the underlying cubic symmetric graph, while graph-reference literature verifies the LCF description. The published exact integral calculation for the **ordinary** Pappus matching complex finds \(\mathcal M(P)\simeq\bigvee^{40}S^5\), and the earlier published mod-two computation finds its degree-five Betti rank forty. Those statements concern all matchings, not just perfect-matching-extendible faces. In fact \(\mathcal P(P)\subsetneq\mathcal M(P)\), with \(15{,}819\) versus \(35{,}367\) nonempty faces; the published ordinary-complex analysis expressly excludes the perfect-matching subcomplex from its scope. The prior statements do not imply the mixed three-/four-dimensional result here.

Bayer, Jelić Milutinović and Vega treat perfect-matching complexes arising from finite planar honeycomb subgraphs, rather than the nonplanar toroidal Pappus Levi graph. Published work on polygonal-line tilings and on Möbius/circular ladder graphs likewise uses different graph families and does not cover this exact object. Searches also compared the Pappus configuration incidence, hexagonal-toroidal and alternative graph naming conventions; no mathematically equivalent published homotopy claim was identified.

## Limitations
The theorem classifies only the fixed eighteen-vertex Pappus graph's perfect-matching extendability complex. The calculation is exhaustive and fully reproducible but does not provide a closed family classification, a shelling, or a general toroidal-graph theorem. Exact integer Morse-boundary reduction is essential: the mod-two ranks alone would not rule out integral torsion or establish homotopy type. Searches and inspection of accessible close sources do not prove bibliographic uniqueness; an equivalent result may exist in differently titled or unindexed literature. No independent scientific audit is claimed.

## References
1. Dmitry N. Kozlov, *Simple homotopy types of Hom-complexes, neighborhood complexes, Lovász complexes, and atom crosscut complexes*, arXiv:math/0503613v1, first public 2005-03-28. https://arxiv.org/abs/math/0503613
2. Italo J. Dejter, *Pappus–Desargues digraph confrontation*, arXiv:0904.1096, first public 2009-04-07. https://arxiv.org/abs/0904.1096
3. Margaret Bayer, Marija Jelić Milutinović and Julianne Vega, *Perfect Matching Complexes of Honeycomb Graphs*, arXiv:2209.02803. https://arxiv.org/abs/2209.02803
4. Himanshu Chandrakar and Anurag Singh, *Perfect Matching Complexes of Polygonal Line Tilings*, arXiv:2407.05809. https://arxiv.org/abs/2407.05809
5. H. Agarwal and R. Basak, *Homotopy Types of Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601. https://arxiv.org/abs/2608.30601
6. *Integral homotopy type of the Pappus graph matching complex*, published exact ordinary-matching calculation. https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-integral-homotopy-type-of-the-pappus-graph-matching-complex--db6c6c11f317
7. *Mod-2 homology of the Pappus matching complex*, published ordinary-matching calculation. https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-mod-2-homology-of-the-pappus-matching-complex--a28326a5f491
8. *Pappus Graph*, Wolfram MathWorld. https://mathworld.wolfram.com/PappusGraph.html
