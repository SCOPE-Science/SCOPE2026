# A two- and three-sphere wedge from the bidirected pentagon multipath complex

## Finding

Let \(B\) be the **bidirected five-cycle** on \(\mathbb Z/5\mathbb Z\): for every \(i\), both directed arcs \(i\to i+1\) and \(i+1\to i\) are present (indices modulo five). Let \(X(B)\) be the simplicial complex whose vertices are these ten arcs and whose nonempty faces are the subsets of arcs forming vertex-disjoint unions of directed simple paths. Then there is an **integral homotopy equivalence**

\[
X(B)\simeq S^2\vee S^3\vee S^3.
\]

In particular, this non-shellable complex is a wedge of spheres. This provides an exact five-vertex instance of the general wedge-of-spheres question for bidirected polygon multipath complexes.

## Assumptions and scope

All graphs and simplicial complexes are finite. A directed simple path has distinct vertices; the single-vertex component is allowed. The graph \(B\) has five vertices and exactly ten distinct arcs, not merely one chosen orientation of each undirected edge. An arc subset is a face precisely if the resulting spanning digraph has indegree and outdegree at most one at each vertex and contains no directed cycle. The assertion concerns this single explicitly specified complex, not polygons with other numbers of vertices. The homotopy equivalence is over the integers, not merely a rational or mod-two homology comparison.

For the certificate, label the forward arcs \(a_i:i\to i+1\) by integers \(i=0,1,2,3,4\) and the reverse arcs \(b_i:i+1\to i\) by integers \(5+i\). The ten-bit integer \(m\) denotes the subset containing exactly the arcs whose bits in \(m\) are one. All checks and bitmask data use this convention.

## Proof

**1. Complete face list.** A valid nonempty arc set has indegree and outdegree at most one and has no directed cycles. Since the underlying undirected graph is a five-cycle, the only possible directed cycles consist either of a two-arc backtrack along one undirected edge or of the coherently directed entire five-cycle. The first is detected by selecting both opposite arcs along an edge; the second, once the degree bounds and exclusion of backtracks hold, is detected by choosing five arcs. Thus the elementary predicate in `verify_bp4.py` enumerates **all** nonempty faces by checking each of the \(2^{10}-1\) nonempty subsets, not a sample. The face vector in dimensions zero through three is exactly \((10,30,30,10)\). No higher-dimensional face exists.

**2. A complete acyclic Morse matching.** The file `matching_certificate.json` explicitly lists thirty-eight distinct covering pairs of the face poset, the ten-arc pivot order used to construct them, and the four critical faces. The pairs are between faces of consecutive dimensions and partition all noncritical faces. To check acyclicity, orient every Hasse covering relation downward except the thirty-eight matched relations, which are oriented upward. The directed graph has eighty vertices and 190 directed arrows. The standalone checker constructs this entire directed graph, checks the certificate and performs an exhaustive topological sort, visiting all eighty vertices. Hence there is no closed gradient path. The critical faces are bitmasks \(128\) in dimension zero, \(104\) in dimension two, and \(30,864\) in dimension three. By the acyclic-matching theorem of discrete Morse theory, \(X(B)\) is homotopy equivalent to a CW complex \(Y\) with **one zero-cell, no one-cells, one two-cell and two three-cells**. Its two-skeleton is therefore \(S^2\).

**3. The two top cycles and their independence.** Any four-arc multipath on a five-cycle is a coherently directed path obtained by omitting one edge of the undirected cycle. Consequently, its ten three-simplices are exactly the five four-element subsets of \(\{a_0,\ldots,a_4\}\) and the five four-element subsets of \(\{b_0,\ldots,b_4\}\). The alternating oriented sums of these two groups are the simplicial boundaries of the corresponding formal four-simplices and hence are integral three-cycles. Their supports are disjoint, so the two cycles are linearly independent in the third chain group and yield independent classes in \(H_3(X(B);\mathbb Z)\), since no four-simplices exist. The verifier checks the asserted complete top-face list and computes both signed boundaries exactly over \(\mathbb Z\).

**4. Attaching degrees and homotopy.** The Morse CW complex \(Y\) has precisely two three-cells, so the rank of its integral third homology is at most two. By Step 3 this rank is at least two. Thus its cellular boundary \(\partial_3:\mathbb Z^2\to\mathbb Z\) is the zero map. The two attaching maps are maps \(S^2\to Y^{(2)}=S^2\), and the entries of \(\partial_3\) are their integral degrees. Since \(\pi_2(S^2)\cong\mathbb Z\) is classified by degree, both attaching maps are nullhomotopic. Attaching two three-cells trivially to \(S^2\) gives \(Y\simeq S^2\vee S^3\vee S^3\), as claimed.

## Verification

The package contains the independent, standard-library-only checker `verify_bp4.py`, the explicit list of matched face pairs in `matching_certificate.json`, and the actual recorded output in `verification_output.txt`. Extract these three files into one directory and run `python3 verify_bp4.py`. The verifier independently compares a local forbidden-cycle predicate against a graph-component-based path predicate on all 1,023 nonempty subsets; reconstructs the eighty valid faces; checks all thirty-eight given matching pairs; verifies the eighty-node, 190-arrow directed Hasse graph is acyclic; enumerates all ten three-simplices; and checks the two top cycles have zero **signed integral** boundary. Successful output begins `VERIFY_OK`.

The finite check is exhaustive for **this particular complex**. The all-size polygon question is not inferred from it.

## Relationship to prior work

Caputi, Collari and Smith (2026, arXiv:2601.05670, Definition 1.2, Theorem 2.10 and Section 3) define the bidirected polygon family, determine its homology, prove non-shellability and explicitly leave its wedge-of-spheres homotopy classification open. Their homology theorem predicts \(\widetilde H_2\cong\mathbb Z\) and \(\widetilde H_3\cong\mathbb Z^2\) in the five-vertex case, but homology alone does not establish the attaching maps or the asserted homotopy type. The construction above supplies an acyclic matching and verifies the attaching degrees independently of that prediction.

Caputi, Collari, Di Trani and Smith (2022, arXiv:2208.04656, Section 4.2) prove wedge decompositions for oriented polygons, expressly requiring no bidirectional edges; those results do not directly cover the five-cycle with both directions on every edge. These related general results are acknowledged, not presented as new.

## Limitations

The theorem treats only the five-vertex bidirected polygon. It neither proves the 2026 conjecture for all bidirected polygons nor rules out nontrivial higher-dimensional attaching maps in larger cases. It does not establish an equivariant homotopy equivalence or a canonical sphere splitting. The finite certificate proves combinatorial acyclicity but is not a machine-independent substitute for understanding the standard discrete-Morse and CW attaching-map results invoked in the proof. Full novelty is subject to ongoing bibliographic uncertainty, and no independent scientific audit is claimed.

## References

1. L. Caputi, C. Collari and J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670, first public version 2026-01-09, especially Definition 1.2, Theorem 2.10 and Section 3. https://arxiv.org/abs/2601.05670
2. L. Caputi, C. Collari, S. Di Trani and J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656, first public version 2022-08-09, especially Section 4.2; subsequently published in *Mathematika* 70 (2024). https://arxiv.org/abs/2208.04656
3. R. Forman, *Morse theory for cell complexes*, *Advances in Mathematics* 134 (1998), 90–145; discrete-Morse CW reduction and acyclic partial matchings.
