# Exact optimal discrete-gradient census for the minimal eight-vertex dunce hat
## Finding
Let \(K\) be the simplicial complex on vertices \(1,\ldots,8\) with facets
\[
124,127,128,134,135,136,156,178,235,237,238,245,348,367,456,468,678.
\]
It is the eight-vertex dunce-hat triangulation distributed in Hachimori's simplicial-complex library. The exact census is:

* there are \(1{,}992{,}223\) acyclic triangle-edge matchings with exactly one critical triangle;
* in every one of those matchings, the eight edges left unmatched to triangles form a connected unicyclic spanning graph;
* the unique-cycle length \(\ell\) has distribution
\[
N_3=754{,}080,\quad N_4=706{,}489,\quad N_5=365{,}173,\quad
N_6=131{,}021,\quad N_7=31{,}621,\quad N_8=3{,}839;
\]
* consequently the number of full acyclic Hasse matchings with Morse vector \((1,1,1)\) is
\[
8\sum_{\ell=3}^8 \ell N_\ell
=8\cdot 7{,}952{,}246
=63{,}617{,}968.
\]

These are exactly the gradient vector fields with the minimum possible total number of critical simplices.

## Assumptions and scope
A discrete gradient vector field is represented by a matching on the Hasse diagram of \(K\). A simplex is critical when it is unmatched. The matching is acyclic when the Hasse diagram, with matched incidences reversed, has no directed cycle; equivalently there is no closed Forman \(V\)-path. The Morse vector records the numbers of critical vertices, edges, and triangles.

The claim is for this labelled eight-vertex triangulation only. It does not assert that every combinatorial type of minimal dunce-hat triangulation has the same census. Counts are counts of gradient vector fields/Hasse matchings, not of real-valued discrete Morse functions realizing them.

## Proof
There are \(24\) edges and \(17\) triangles. For a triangle-edge layer with one critical triangle, choose that critical triangle and match each of the other \(16\) triangles injectively to one of its three boundary edges. For a matched pair consisting of an edge \(e\) and triangle \(F\), add directed transitions from \(F\) to every other triangle containing \(e\). Reversing all these transitions gives the usual triangle-to-triangle \(V\)-path convention, so directed cycles are unchanged. Maintaining the exact transitive closure while the \(16\) choices are built rejects an assignment precisely when it creates a closed \(V\)-path. Thus the recursion enumerates every acyclic triangle-edge matching once and only once.

The exhaustive recursion gives \(1{,}992{,}223\) accepted triangle-edge layers. For each accepted layer, inspect the eight edges not used by triangle matches. Exhaustively, this residual graph contains all eight vertices and is connected. Since it has eight vertices and eight edges, it is unicyclic. Leaf peeling therefore recovers its unique cycle, producing the stated cycle-length distribution.

Fix one accepted triangle-edge layer whose residual graph has unique-cycle length \(\ell\). Any compatible vertex-edge layer with one critical vertex is exactly a rooted spanning tree of the residual graph: choose the critical vertex as root and match every other vertex to its parent edge. Conversely an acyclic vertex-edge matching with one critical vertex orients a spanning tree toward the root. A connected unicyclic graph with cycle length \(\ell\) has exactly \(\ell\) spanning trees, obtained by deleting one cycle edge. There are eight possible roots. Hence the layer has exactly \(8\ell\) extensions. Summing gives \(63{,}617{,}968\).

The same exact recursion, now requiring all \(17\) triangles to be matched injectively to edges, returns zero acyclic matchings. Therefore no discrete gradient on \(K\) has zero critical triangles. Since \(K\) is connected, the weak Morse inequality gives at least one critical vertex. Euler's relation \(c_0-c_1+c_2=1\) rules out a total of two critical cells, and a total of one would have to be \((1,0,0)\), which is impossible because it has no critical triangle. The census above supplies fields with three critical cells, namely \((1,1,1)\). Thus three is the minimum, and every minimum field is counted above.

## Verification
The standalone verifier `verify.py` reconstructs the complex from the facet list, checks the \((8,24,17)\) face vector and edge-incidence profile, exhaustively enumerates the one-critical-triangle layers with an incremental transitive-closure cycle test, verifies connected unicyclic residual graphs, computes the cycle histogram, separately enumerates the zero-critical-triangle case, and checks the rooted-tree extension formula. Its expected terminal line is:

`VERIFY_OK facets=17 edges=24 full12=0 acyclic16=1992223 cycle_hist=3:754080,4:706489,5:365173,6:131021,7:31621,8:3839 weighted=7952246 optimal_fields=63617968`

The finite enumeration is exhaustive for this fixed complex; no inference to other dunce-hat triangulations is made.

## Relationship to prior work
Lewiner, Lopes, and Tavares introduced optimal discrete gradient fields as those with the minimum number of critical cells and, in their Table 2, reported the dunce-hat model with face vector \((8,24,17)\) and minimum Morse vector \((1,1,1)\). That establishes the previously known optimum vector but does not give a count of optimal gradient fields or a residual-cycle distribution.

Benedetti and Lutz gave a geometric realization of a minimal eight-vertex dunce-hat triangulation and emphasized its noncollapsibility. Paixão and Spreer later classified minimal dunce-hat triangulations in the context of random collapsibility. Those results motivate the object and its role as a test case, but the inspected statements do not imply the exact census above.

## Limitations
The result is an exact finite computation plus the rooted-tree structural reduction for one specific labelled minimal triangulation. The exhaustive verifier is deterministic but is not a formal proof assistant certificate. The literature search found no prior statement of the two exact counts or the six-cell cycle histogram, but unindexed legacy software output remains a residual originality risk. The date field associated with this package uses the earliest day-level public timestamp verified for a minimal eight-vertex dunce-hat source; an older 2003 paper was inspected but its available metadata gave only month-level publication information, so no day was invented.

## References
1. T. Lewiner, H. Lopes, G. Tavares, “Towards optimality in discrete Morse theory,” *Experimental Mathematics* 12(3), 271–285 (2003), DOI `10.1080/10586458.2003.10504498`.
2. B. Benedetti, F. H. Lutz, “The dunce hat in a minimal non-extendably collapsible 3-ball,” arXiv:`0912.3723v1` (submitted 2009-12-18).
3. J. Paixão, J. Spreer, “Random collapsibility and 3-sphere recognition,” arXiv:`1509.07607v1` (submitted 2015-09-25).
4. M. Hachimori, Simplicial Complex Library, datum `dunce_hat.dat`, `https://infoshako.sk.tsukuba.ac.jp/~hachi/math/library/dunce_hat.dat`.
