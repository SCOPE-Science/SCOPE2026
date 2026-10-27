# Edge-metric bases and exchange diameter of the flower snark \(J_7\)

## Finding
Let \(J_7\) be the seven-petal Isaacs flower snark with the explicitly specified vertex and edge sets below. Its edge metric dimension is exactly
\[
\operatorname{edim}(J_7)=4.
\]
There are exactly \(1932\) four-vertex edge metric bases. Form the **minimum-basis exchange graph** \(\mathcal B_e(J_7)\) with these \(1932\) sets as vertices, and join two sets if and only if they share three vertices. Then \(\mathcal B_e(J_7)\) has exactly \(17920\) edges and is connected. Every exchange-graph vertex has eccentricity exactly \(5\), so
\[
\operatorname{rad}(\mathcal B_e(J_7))=
\operatorname{diam}(\mathcal B_e(J_7))=5.
\]
This is an exact finite theorem about the first nontrivial flower snark beyond \(J_5\), not a claim about all flower snarks.

## Assumptions and scope
All graphs are finite, undirected and simple. Index residues \(i\) range from \(0\) through \(6\). Define the \(28\) vertices
\[
V(J_7)=\{a_i,b_i,c_i,d_i:0\le i\le6\}.
\]
The edge set contains the \(21\) spokes \(a_ib_i,a_ic_i,a_id_i\); the seven inner-cycle edges \(b_ib_{i+1}\) for \(i\) interpreted modulo \(7\); the twelve untwisted outer edges \(c_ic_{i+1},d_id_{i+1}\) for \(0\le i\le5\); and the two twisted closure edges \(c_6d_0,d_6c_0\). Thus the graph is cubic with \(28\) vertices and \(42\) edges. The outer edges form a single \(14\)-cycle. This is the standard flower-snark construction, with the outer-cycle twist specified to avoid ambiguity.

For a vertex \(s\) and edge \(e=uv\), put
\[
d(s,e)=\min\{d(s,u),d(s,v)\}.
\]
A vertex set \(S\) **edge-resolves** if each two distinct edges have different ordered distance vectors \((d(s,e):s\in S)\) under any fixed ordering of \(S\). Its minimum size is \(\operatorname{edim}(J_7)\). In the exchange graph an elementary move removes one member of a four-element basis and inserts any previously unselected vertex; the removed and inserted vertices are not required to be adjacent in \(J_7\).

## Proof
The proof is exhaustive **over the complete finite domain** and rests on the following elementary equivalences, rather than on sample experiments.

1. For every vertex \(s\), compute its distance to all \(42\) edges using shortest-path distances in the explicitly constructed graph. Let \(U\) be the \(\binom{42}{2}=861\) unordered pairs of distinct edges. Define \(M(s)\subseteq U\) by \(\{e,f\}\in M(s)\) if and only if \(d(s,e)\ne d(s,f)\). By the definition of edge-resolution, \(S\) edge-resolves exactly when \(\bigcup_{s\in S}M(s)=U\). This equivalence checks every edge pair, not just incident pairs.

2. The standalone checker `verify_distances.py` constructs these \(861\)-bit separation sets with breadth-first shortest paths, and evaluates **all** \(\binom{28}{3}=3276\) distinct three-vertex subsets and **all** \(\binom{28}{4}=20475\) distinct four-vertex subsets. Zero triples cover \(U\); precisely \(1932\) quadruples cover \(U\). As edge-resolution is upwards-closed, no one- or two-vertex set can resolve either. The quadruple \(\{a_0,b_0,c_1,c_4\}\) is a direct witness. This establishes the dimension and count.

3. Let \(\mathcal F\) be the complete set of \(1932\) resolving quadruples from step 2. Two members of \(\mathcal F\) differ by a single replacement if and only if their intersection has cardinality \(3\). The checker creates all these adjacencies. Their degree sum is \(35840\), hence the number of undirected exchange edges is \(17920\).

4. For **each** of the \(1932\) possible source bases, breadth-first search over the full exchange graph reaches all \(1932\) vertices, and its maximum distance from that source is exactly \(5\). Reachability establishes connectedness. The universal maximum-distance statement establishes that all \(1932\) eccentricities equal \(5\), so both graph radius and diameter are \(5\).

These four steps use exact integer arithmetic and complete finite ranges. Independent companion code `verify_signatures.cpp` rebuilds the same graph with a different numbering, obtains vertex distances by Floyd–Warshall rather than shortest-path breadth-first search, recognizes bases by uniqueness of the \(42\) edge-distance tuples rather than separation-bit unions, and creates exchange edges by pairwise four-set intersections rather than generating replacements. It independently reproduces the four enumerative statements and every source eccentricity. The two recorded outputs agree exactly.

## Verification
With a Python 3 interpreter, run `python3 verify_distances.py`. With a C++17 compiler, run `c++ -std=c++17 -O2 verify_signatures.cpp -o verify_signatures` and then `./verify_signatures`. The expected plain-text outputs are included as `verify_distances.out` and `verify_signatures.out` and are identical. Both terminate with `VERIFIED` after assertions covering the \(3276\) triples, \(20475\) quadruples, exchange edge count, connectedness and eccentricity census. No external libraries, hidden tables or previously computed graph files are needed. The proof uses the displayed exhaustive finite algorithm; log messages alone are not its justification.

## Relationship to prior work
Kelenc, Tratnik and Yero introduced vertex-to-edge distance and edge metric dimension in their public 2016 manuscript [1], including a general set-cover formulation. Neither the basic definition nor the set-cover reduction is claimed as new here.

Milivojević Danas [2] studied the same Isaacs flower-snark family in full text, obtaining mixed metric dimension \(4\) for odd orders at least seven and bounding the edge metric dimension between \(3\) and \(4\). The paper explicitly leaves the exact edge metric dimension of the flower snarks as a future question. An upper bound of \(4\) and lower bound of \(3\) do not imply either choice at \(J_7\), much less the count or geometry of all its optimum landmark sets. The present finite census decides this first previously unresolved parameter instance and describes its complete minimum-basis exchange graph.

The exchange construction is a fixed-cardinality, unrestricted one-vertex **replacement** model. It is not the general exchange-property axiom for all inclusion-minimal resolving sets, not an edge-to-edge token slide, and not vertex-metric or mixed-metric resolution. Other graphs' metric-basis or edge-basis enumerators do not imply the present counts.

## Limitations
This theorem is specific to \(J_7\). The evidence is complete on that finite graph, but it does not show \(\operatorname{edim}(J_n)=4\) for every odd \(n\ge9\), nor does it determine exchange geometry at other sizes. It establishes no mixing-time assertion. Literature priority is not independently certified; an unindexed table or a non-obviously equivalent description of the same finite invariant remains a possible originality risk. The mathematical computation is fully self-contained and replayable, but no independent external scientific audit has been performed.

## References
[1] A. Kelenc, N. Tratnik, and I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1, first public release 2016-01-31, https://arxiv.org/html/1602.00291v1 .

[2] M. Milivojević Danas, *The mixed metric dimension of flower snarks and wheels*, *Open Mathematics* 19 (2021), 629–640, DOI:10.1515/math-2021-0065, https://scidar.kg.ac.rs/bitstream/123456789/13501/1/10.1515-math-2021-0065.pdf .
