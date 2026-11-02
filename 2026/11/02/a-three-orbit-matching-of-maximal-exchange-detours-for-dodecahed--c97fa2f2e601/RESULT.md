# A three-orbit matching of maximal exchange detours for dodecahedral feedback sets

## Finding
Let \(D\) be the dodecahedral graph and let \(\mathcal F\) denote its family of minimum feedback vertex sets. Form the token-jump graph \(R\) whose vertices are members of \(\mathcal F\), with an edge between sets differing in precisely one removed and one inserted vertex. For distinct \(A,B\in\mathcal F\), define their **exchange excess** by
\[
\varepsilon(A,B)=d_R(A,B)-\bigl(6-|A\cap B|\bigr).
\]
The subtracted term is the unavoidable number of replacements even if all intermediate constraints are ignored.

**Theorem (finite exact classification).** Every exchange excess belongs to \(\{0,1,2\}\). Among all \(\binom{2520}{2}=3{,}173{,}940\) unordered pairs, the multiplicities of excess \(0,1,2\) are respectively
\[
3{,}124{,}960,\qquad48{,}800,\qquad180.
\]
The \(180\) pairs of excess \(2\) form a matching on exactly \(360\) of the \(2520\) configurations: no configuration belongs to two such pairs. Each exceptional pair has a **unique** common edge of \(D\), and each of the \(30\) edges is that common edge for exactly six exceptional pairs (four with intersection size two; two with intersection size three). Under the full automorphism group of the dodecahedron, the exceptional pairs split into exactly three orbits of size \(60\).

An exhaustive refinement is the following table, where \(s=|A\cap B|\), \(d=d_R(A,B)\), and the final column counts unordered pairs.

| \(s\) | \(d\) | Pair count |
|---:|---:|---:|
| 5 | 1 | 23,940 |
| 4 | 2 | 162,870 |
| 4 | 3 | 4,410 |
| 3 | 3 | 567,820 |
| 3 | 4 | 20,960 |
| 3 | 5 | 60 |
| 2 | 4 | 1,067,430 |
| 2 | 5 | 21,510 |
| 2 | 6 | 120 |
| 1 | 5 | 972,420 |
| 1 | 6 | 1,920 |
| 0 | 6 | 330,480 |

As supporting (not independently claimed-new) checks, \(R\) has \(2520\) vertices and \(23{,}940\) edges, and all its vertices have eccentricity \(6\).

## Assumptions and scope
All graphs are finite, simple, and undirected. Explicitly, \(D=GP(10,2)\) has vertices \(u_0,\ldots,u_9,v_0,\ldots,v_9\) and the \(30\) edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\), with indices modulo \(10\). Integer codes \(0,\ldots,9\) correspond to the \(u\)-vertices and \(10,\ldots,19\) to the \(v\)-vertices. A *feedback vertex set* is a set \(S\) for which \(D-S\) is a forest. Token-jump adjacency permits the exchanged vertices to be nonadjacent in \(D\); this is not the more restrictive token-sliding relation. All distances are in \(R\), not in \(D\).

In the stated numeric coding, representatives of the three orbits of excess-two pairs are, respectively,
\[
\begin{aligned}
(\{0,1,3,5,16,17\},\ &\{0,1,5,7,13,14\}),\\
(\{0,1,3,7,14,19\},\ &\{0,1,4,8,12,17\}),\\
(\{0,1,3,8,14,17\},\ &\{0,1,4,7,12,19\}).
\end{aligned}
\]

## Proof
**Optimal size.** For a set \(S\) of size \(k\), deleting its vertices removes at most \(3k\) of the \(30\) graph edges. If \(D-S\) is a forest on \(20-k\) vertices, it has at most \(19-k\) edges. Thus \(30-3k\le19-k\) and \(k\ge6\). The exhaustive construction below exhibits \(2520\) qualifying sets of size \(6\); hence this is the exact minimum.

**Exhaustive finite certificate.** `verify_direct.py` generates each of the \(\binom{20}{6}=38{,}760\) six-element subsets exactly once using lexicographically ordered combinations. A disjoint-set union test processes every surviving edge of \(D-S\) and rejects a set exactly when adding an edge joins already connected endpoints, which is equivalent to the presence of a cycle. Hence the list of \(2520\) accepted masks is complete. For each mask it then tries all \(6\times14\) possible deletions/insertions, retaining exactly those outcomes also in the accepted dictionary. This constructs every legal edge of \(R\), without inferred symmetry or sampling. Breadth-first search from **every** mask gives the shortest-path metric; comparing every unordered pair to its Johnson lower bound gives the complete table and the three excess counts.

For each excess-two pair, the verifier checks that the intersection of the two selected sets contains exactly one of the \(30\) original graph edges. It checks the common-edge counts separately for each original edge and each of the two occurring intersection sizes. It also confirms that every endpoint has exactly one exceptional partner.

**Orbit assertion.** Three explicit permutations in `verify_direct.py` are directly checked to preserve the \(30\)-edge set. Their closure has \(120\) elements. The automorphism group of the dodecahedral graph has order \(120\) (alternatively, its usual three-connected planar embedding determines an automorphism by the image of one vertex and the order of its three incident neighbors, giving at most \(20\cdot6\) possibilities). The program applies the generated group to the three displayed representative pairs and verifies that their orbits are disjoint, each has \(60\) members, and their union equals the complete \(180\)-pair exceptional set. This proves the exact three-orbit classification.

**Independent exhaustive reconstruction.** `verify_independent.py` starts from an alternative planar labeling of all \(30\) dodecahedral edges and verifies an explicit isomorphism to the generalized Petersen presentation. Rather than union-find, it recognizes forests by iteratively peeling all vertices of residual degree at most one. Rather than generating swaps, it constructs token-jump adjacency by testing that two selected six-element masks have intersection size exactly five. All-pairs breadth-first search then independently recovers every entry in the intersection-distance table, and checks the unique-partner and common-edge properties. Both methods exhaust finite state spaces; there is no inference from bounded experiments to an infinite family.

## Verification
Run `python3 verify_direct.py` and `python3 verify_independent.py` from the same directory as this document. Both use only the Python standard library, require Python version \(3.10\) or later, have no input files, and terminate with explicit success messages only after all assertions pass. Their complete source is included in this package. The direct certificate checks the three orbit representatives, group closure, and per-edge counts; the independent certificate checks the full shortest-path census via a different graph labeling, forest predicate, and adjacency implementation. The independent certificate does not constitute an independent human audit.

## Relationship to prior work
Kelly and Liu (2016) study induced forests and feedback vertex sets in subcubic graphs, explicitly identifying the dodecahedron as an extremal example. Their results concern optimum-set size and structural bounds, not this exchange-excess classification. Beineke and Vandell established the classical decycling viewpoint. Bousquet, Hommelsheim, Kobayashi, Mühlenthaler and Suzuki (2023) study feedback-vertex-set exchange reachability in planar graphs, proving a general transformation bound; that is not a count of the pairs requiring one or two additional steps in this particular minimum-set graph. The known total of \(2520\) configurations, the unrestricted token-jump graph's \(23{,}940\) edges and its diameter \(6\) are treated as background, **not** claimed as novel. The proposed contribution here is the complete exchange-excess spectrum and especially the exceptional-pair matching, its per-edge localization, and its three symmetry orbits.

## Limitations
The theorem is about this single named graph; it does not claim a universal excess bound for cubic graphs. The proof is a transparent exhaustive finite certificate rather than a short conceptual characterization of all exchange distances. The complete text of the closest 2023 reconfiguration article could not be obtained in this investigation; an equivalent historically published exceptional-pair classification under another terminology cannot be excluded. Independent external verification has not been performed.

## References
1. T. Kelly and C.-H. Liu, *Size of the Largest Induced Forest in Subcubic Graphs of Girth at least Four and Five*, arXiv:1603.03855, first publicly submitted 2016-03-12, https://arxiv.org/abs/1603.03855 ; available full-text version: https://arxiv.org/html/1603.03855v2 .
2. T. Kelly and C.-H. Liu, *Minimum Size of Feedback Vertex Sets of Planar Graphs of Girth at least Five*, arXiv:1603.04559, first publicly submitted 2016-03-15, https://arxiv.org/abs/1603.04559 .
3. L. W. Beineke and R. C. Vandell, *Decycling graphs*, Journal of Graph Theory 25 (1997), 59–77; DOI: 10.1002/(SICI)1097-0118(199705)25:1<59::AID-JGT4>3.0.CO;2-H.
4. N. Bousquet, F. Hommelsheim, Y. Kobayashi, M. Mühlenthaler, and A. Suzuki, *Feedback vertex set reconfiguration in planar graphs*, Theoretical Computer Science 979 (2023), article 114188; DOI: 10.1016/j.tcs.2023.114188.
