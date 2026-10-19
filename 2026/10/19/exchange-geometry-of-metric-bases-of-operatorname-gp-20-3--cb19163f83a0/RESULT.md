# Exchange geometry of metric bases of \(\operatorname{GP}(20,3)\)

## Finding

Let \(G=\operatorname{GP}(20,3)\), with vertex set \(\{u_i,v_i:i\in\mathbb Z_{20}\}\) and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\), all indices modulo \(20\). A *metric basis* is a minimum-cardinality vertex set whose vectors of shortest-path distances distinguish all forty vertices of \(G\). Let \(\mathcal B(G)\) have one vertex for each metric basis, adjacent when the two bases differ by replacing exactly one selected vertex by one unselected vertex.

The graph \(G\) has metric dimension \(5\) (the value was known). Its complete metric-basis exchange graph has
\[
|V(\mathcal B(G))|=41{,}040,\qquad |E(\mathcal B(G))|=670{,}930.
\]
It is connected, with radius \(6\) and diameter \(7\). Exactly \(40{,}180\) bases have eccentricity \(6\), and exactly \(860\) have eccentricity \(7\); no other eccentricities occur. Its minimum and maximum degrees are \(7\) and \(69\).

For a basis with \(r\) outer vertices, the number of such bases is
\[
\begin{array}{c|rrrrr}
r&1&2&3&4&5\\ \hline
\#\text{bases}&1720&13400&20520&5300&100.
\end{array}
\]
No basis is supported entirely in the inner rim. Under the natural order-\(40\) dihedral automorphism subgroup that rotates or reverses both rims simultaneously, the \(41{,}040\) bases form \(1{,}032\) orbits: twelve of size \(20\) and \(1{,}020\) of size \(40\). The eccentricity-\(7\) bases form twenty-two of these orbits, one of size \(20\) and twenty-one of size \(40\). Their outer-rim counts are \(360\) for \(r=2\), \(420\) for \(r=3\), and \(80\) for \(r=4\).

## Assumptions and scope

All graphs are finite, simple, undirected, and vertex-labelled as defined. Distances are shortest-path distances in \(G\), not distances in the exchange graph unless explicitly indicated. A metric basis is a five-element unordered subset of the forty labelled vertices; global graph automorphisms are **not** identified when counting its states. An exchange replaces one vertex of the selected five-set by one outside it, without allowing an intermediate four-set. The reported graph distances refer only to such legal exchanges and are not distances in the ambient Johnson graph.

## Proof

The following is an exhaustive, finite proof with explicit, reproducible source, rather than an inference from sampled instances. Both programs supplied below reconstruct \(G\) and its distances independently.

First, every shortest-path distance is obtained by breadth-first search on the explicitly listed sixty edges of \(G\). For each unordered vertex pair \(\{x,y\}\), a candidate landmark \(w\) distinguishes the pair exactly when \(d(w,x)\ne d(w,y)\). A set is resolving if and only if at least one selected landmark distinguishes **each** of the \(\binom{40}{2}=780\) pairs. Hence exhaustive testing of all \(\binom{40}{4}=91{,}390\) four-sets, none of which resolves, proves the lower bound \(\dim(G)\ge5\). Every resolving five-set is minimal because no four-set resolves.

The verifier iterates over all \(\binom{40}{5}=658{,}008\) five-sets, testing separation of all vertex pairs (or, independently, checking uniqueness of the forty distance codes). Precisely \(41{,}040\) pass. Classification by the number of selected outer-rim vertices gives the five counts above. This enumeration is exhaustive: every unordered five-set occurs in exactly one increasing five-index tuple, and the resolving condition is necessary and sufficient.

Next, represent each five-set by its forty-bit characteristic mask. For each passing mask, enumerate its \(5\cdot35=175\) possible single-vertex replacements, retaining exactly those masks also in the passing collection. Every legal edge appears twice in the resulting degree sum. The sum is \(1{,}341{,}860\), giving \(670{,}930\) undirected edges. The degrees range from \(7\) to \(69\); the verifier explicitly checks adjacency symmetry.

For shortest paths, consider the transformations \(u_i\mapsto u_{\varepsilon i+s}\), \(v_i\mapsto v_{\varepsilon i+s}\), for \(\varepsilon\in\{-1,1\}\) and \(s\in\mathbb Z_{20}\). Each preserves the three types of undirected edges and therefore preserves metric bases and exchanges. Thus exchange eccentricity is constant on every orbit of this size-\(40\) automorphism subgroup. The verifier forms all orbits directly, yielding twelve orbits of size \(20\) and \(1{,}020\) of size \(40\), and performs a complete breadth-first search from **each** of the resulting \(1{,}032\) representatives. Every search reaches all \(41{,}040\) vertices. Exactly \(1{,}010\) representative orbits have eccentricity \(6\), and twenty-two have eccentricity \(7\). Weighting by orbit sizes gives \(40{,}180\) and \(860\). Taking the minimum and maximum establishes the claimed radius and diameter; this procedure does not assume that the dihedral group is the full automorphism group.

## Verification

The supplied files `check_direct.cpp` and `check_masks.py` use only the C++17 and Python 3 standard libraries. With assertions enabled, run:

```sh
g++ -std=c++17 -O3 check_direct.cpp -o check_direct
./check_direct
python3 check_masks.py
```

The first program checks all four- and five-element subsets by uniqueness of integer-packed distance codes; it constructs every exchange edge, derives and verifies the natural dihedral action, and performs all \(1{,}032\) representative BFS computations. It asserts the complete counts and prints `VERIFY_OK`. The second program independently uses \(780\)-bit pair-separation masks instead of distance-code uniqueness, recomputes all bases and edges, verifies undirected adjacency and connectivity, and checks centers and diameter witnesses by two unrestricted BFS runs. It also prints `VERIFY_OK`. The corresponding exact outputs are included as `direct_output.txt` and `masks_output.txt`.

An explicit radius-\(6\) basis, in zero-based vertex indices \(u_i=i\), \(v_i=20+i\), is \(\{0,1,2,7,28\}\). A basis of eccentricity \(7\) is \(\{0,1,8,11,30\}\), and the second verifier exhibits \(\{4,13,16,25,27\}\) at exchange distance \(7\) from it. These are checkable examples, not substitutes for the exhaustive upper bounds.

## Relationship to prior work

Imran, Baig, Shafiq and Tomescu (2014) study the metric dimension of \(\operatorname{GP}(n,3)\) and provide bounds by congruence class. Shao, Sheikholeslami, Wu and Liu (2018, Theorem 8(ii)) establish the already-known dimension \(5\) at \(n=20\), but do not enumerate the metric bases or their one-vertex exchange graph. Gao, Xiao and Zhang (2025) study the large-parameter dimension problem, assuming sufficiently large \(n\) (for example \(n\ge36\)); this does not determine the finite exchange metric at \(n=20\). Comparisons against published exact basis-exchange results for other graphs do not imply this classification, because those results concern different underlying graphs or different resolution notions.

## Limitations

This is an exact theorem for one naturally exceptional forty-vertex generalized Petersen graph, not an infinite-family result. Its proof is exhaustive finite computation, supported by two distinct implementations; there is no claim that the empirical output alone proves anything beyond the completely enumerated domain. The checks do not establish publication priority against every possible inaccessible or unindexed table or unpublished computation. No independent external scientific audit is claimed.

## References

1. M. Imran, A. Q. Baig, M. K. Shafiq, I. Tomescu, *On Metric Dimension of Generalized Petersen Graphs P(n, 3)*, Ars Combinatoria **117** (2014), 113–130; publisher online record dated 2014-10-31. https://combinatorialpress.com/ars-articles/volume-117-ars-articles/on-metric-dimension-of-generalized-petersen-graphs-pn-3/
2. Z. Shao, S. M. Sheikholeslami, P. Wu, J.-B. Liu, *The Metric Dimension of Some Generalized Petersen Graphs*, Discrete Dynamics in Nature and Society (2018), Article 4531958, Theorem 8(ii). https://doi.org/10.1155/2018/4531958
3. R. Gao, Y. Xiao, Z. Zhang, *On the Metric Dimension of Generalized Petersen Graphs P(n,3)*, arXiv:2508.12224 (2025). https://arxiv.org/abs/2508.12224
