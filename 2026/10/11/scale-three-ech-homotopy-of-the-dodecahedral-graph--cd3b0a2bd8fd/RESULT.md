# Scale-three Čech homotopy of the dodecahedral graph

## Finding
For the dodecahedral graph \(D=GP(10,2)\), let \(\mathcal N(D,r)\) denote the nerve of all closed balls of radius \(r/2\), with centers at the graph vertices and balls taken in the unit-edge geometric realization equipped with its intrinsic shortest-path metric. Then

\[
\boxed{\mathcal N(D,3)\simeq S^2\vee\bigvee^{12}S^3.}
\]

The only nonzero reduced integral homology groups are \(\widetilde H_2\cong\mathbb Z\) and \(\widetilde H_3\cong\mathbb Z^{12}\). The complex is pure of dimension five but is not shellable.

## Assumptions and scope
The graph has vertices \(0,\ldots,19\). Write outer vertices \(i\) and inner vertices \(10+i\) for \(0\le i<10\), with indices modulo ten. Include precisely the three types of edges \(\{i,i+1\}\), \(\{i,10+i\}\), and \(\{10+i,10+(i+2)\}\). These give 20 vertices and 30 edges and specify the ordinary dodecahedral graph, independently of any spatial embedding. All graph edges have length one. Balls are *closed* subsets of the geometric realization, not only balls in the discrete vertex set.

For a vertex \(v\), define \(N[v]=\{v\}\cup\{w:vw\in E(D)\}\). Every edge \(uv\) yields the six-vertex set \(F_{uv}=N[u]\cup N[v]\). For graph Čech complexes at odd integer scale three, the edge-midpoint intersection description of Adams–Shukla–Singh, Lemma 2.2, gives the exact equality of abstract complexes
\[
\mathcal N(D,3)=\left\langle F_{uv}:uv\in E(D)\right\rangle.
\]
Here angle brackets mean the simplicial complex containing every subset of the specified generating sets; equality is combinatorial, not merely homotopy equivalence.

## Proof
**Exact facets and face counts.** The three edge families above generate exactly 30 distinct six-vertex maximal facets. Enumerating all nonempty subsets of these facets, with duplicates removed, gives the face vector in dimensions zero through five
\[
(20,150,380,410,180,30),
\]
thus 1,170 nonempty faces and 4,160 codimension-one Hasse incidences. The facet size proves purity of dimension five.

**A complete acyclic matching.** Encode each face by a 20-bit integer mask. Consider the fixed ordered vertex list

`[17,15,11,18,7,6,19,3,14,0,9,5,16,8,13,2,1,12,4,10]`.

At each successive listed vertex \(v\), scan currently unmatched nonempty faces in increasing order of (cardinality, integer mask), and match a face \(\sigma\) not containing \(v\) to \(\sigma\cup\{v\}\) whenever both are currently unmatched faces. Immediately remove the pair from consideration. This produces 578 distinct face pairs. Exactly fourteen faces remain unmatched: one vertex, one two-simplex, and twelve three-simplices.

Orient each incidence in the full Hasse diagram from its lower face to its upper face if it is a matched pair, and from upper face to lower face otherwise. A topological sort visits all 1,170 faces, establishing that this entire directed graph is acyclic, not merely that the matching pairs are disjoint. By Forman's discrete Morse theorem the resulting complex is homotopy equivalent to a CW complex with exactly these fourteen cells.

**The integral attaching degrees vanish.** Orient simplices by increasing vertex labels. The only potentially nonzero Morse cellular boundary goes from the twelve critical three-cells to the sole critical two-cell. For a matched pair \(\sigma^2\subset\tau^3\), eliminate its unit incidence in the signed integral boundary of \(\tau\): recursively replace \(\sigma\) by the negative signed sum of its other triangular faces, divided by its incidence sign \(\pm1\). A triangle paired as the upper element of a one-to-two pair contributes zero to the reduced two-chain group; the sole critical triangle projects to itself. Acyclicity guarantees that this recursive elimination terminates. Applying this exact integer reduction to all oriented boundaries of the twelve critical three-simplices yields **twelve zero coefficients** at the critical two-simplex, with no rational or floating-point arithmetic.

The Morse CW complex has a single zero-cell and no one-cells. Its two-skeleton is therefore \(S^2\). The attaching map of each of the twelve three-cells belongs to \(\pi_2(S^2)\cong\mathbb Z\), and its degree is exactly the computed integral cellular coefficient. Each degree is zero, so each attaching map is null-homotopic. The CW complex, and hence the original nerve, is homotopy equivalent to \(S^2\vee\bigvee^{12}S^3\), as claimed. Purity together with nonzero reduced homology strictly below dimension five obstructs shellability.

## Verification
The complete standard-library program `verify.py` reconstructs the graph, all 30 facets, all 1,170 nonempty faces, all 578 matched pairs, all 4,160 Hasse incidences, and the acyclic directed Hasse graph. It recomputes the twelve integral Morse boundary coefficients using the explicit orientation rule and recursive elimination, requiring each to vanish. Independently, exact simplicial boundary calculations over \(\mathbb F_2\) and \(\mathbb F_3\) both return the ranks \((19,131,248,150,30)\) in degrees one through five, hence reduced Betti numbers \((0,0,1,12,0,0)\). The alternating face sum is \(-10=1+1-12\). Run `python3 verify.py`; the expected final marker is `VERIFY_OK`. These finite checks are exhaustive for this explicitly defined twenty-vertex complex; the mathematical deduction from the matching to the homotopy type uses the stated Morse and attaching-map arguments.

## Relationship to prior work
Adams, Shukla and Singh introduce the intrinsic graph Čech nerve, give its integer-scale facet description (Lemma 2.2), and prove the graph-recovery regime below half the shortest-cycle length (Lemma 2.3); their higher-scale homotopy results concern hypercube graphs rather than the dodecahedral graph. The dodecahedron has girth five, so scale three lies outside that recovery theorem's guaranteed range. Previte's 2014 D-neighborhood thesis tabulates single-vertex distance-neighborhood complexes, including dodecahedral entries, but these correspond to even graph Čech scales for initial distance sets and do not determine the edge-union nerve at scale three. Matsushita's closed-neighborhood complex is likewise generated by one closed vertex neighborhood, rather than unions over graph edges. Earlier dodecahedral independence, matching, and graph-Rips computations concern distinct simplicial complexes, and neither equality of graphs nor similarity of numerical parameters transfers their homotopy conclusions to this nerve. A targeted search of available published sources found no equivalent exact scale-three result; this search is not a proof that no unindexed equivalent exists.

## Limitations
The theorem concerns the specific 20-vertex graph and exact intrinsic scale three. It makes no assertion about other graphs, other scales, persistence morphisms, or uniqueness of the homotopy type among graph families. Its proof relies on complete, finite, machine-replayable enumeration and exact integer Morse reductions; the verifier does not replace the stated standard topological theorems. Unindexed or differently phrased earlier results may exist.

## References
1. Henry Adams, Samir Shukla, Anurag Singh, *Čech complexes of hypercube graphs*, arXiv:2212.05871 (first public 12 December 2022), Lemmas 2.2–2.3, Sections 4–6. https://arxiv.org/abs/2212.05871
2. Corrine Previte, *The D-neighborhood complex of a graph*, doctoral dissertation, Colorado State University (2014), especially Chapter 3 and Table 3.1. https://doi.org/10.25675/3.018305
3. Takahiro Matsushita, *Closed neighborhood complexes of graphs*, arXiv:2511.12608 (2025), especially Theorems 1.2–1.4. https://arxiv.org/abs/2511.12608
