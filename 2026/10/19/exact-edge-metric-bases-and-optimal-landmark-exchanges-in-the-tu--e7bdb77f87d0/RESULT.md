# Exact edge-metric bases and optimal landmark exchanges in the Tutte–Coxeter graph

## Finding

Let \(T\) be the 30-vertex Tutte–Coxeter graph, realized as the incidence graph of the 15 duads and 15 synthemes on a six-element set. For a graph vertex \(v\) and edge \(e=uw\), define the vertex-to-edge distance \(d(v,e)=\min\{d(v,u),d(v,w)\}\). An **edge-metric generator** \(S\subseteq V(T)\) requires that for every pair of distinct edges \(e,f\), some \(s\in S\) has \(d(s,e)\ne d(s,f)\); a smallest generator is an **edge-metric basis**.

The edge-metric dimension is exactly \(\operatorname{edim}(T)=5\). There are precisely \(4560\) edge-metric bases: \(2280\) consist of two duads and three synthemes, and \(2280\) consist of three duads and two synthemes. There are no edge-metric generators of sizes one through four.

Let \(J\) be the **optimal-basis token-jumping graph** whose vertices are these \(4560\) unordered five-element bases. Two bases are adjacent precisely when one vertex can be replaced with one other vertex, with the resulting five-element set again an edge-metric basis. Then \(J\) has \(37320\) undirected edges, is connected, and has radius \(6\) and diameter \(7\). Exactly \(720\) vertices of \(J\) have degree \(13\) and eccentricity \(7\), while the remaining \(3840\) have degree \(17\) and eccentricity \(6\). Exactly \(360\) unordered pairs of bases are distance seven apart.

## Assumptions and scope

The ground set is \(\{0,1,2,3,4,5\}\). A **duad** is an unordered pair of distinct ground elements. A **syntheme** is a partition of the ground set into three duads. Number the fifteen duads lexicographically from \(0\) to \(14\), followed by the fifteen synthemes sorted lexicographically, numbered \(15\) to \(29\). Join duad \(p\) to syntheme \(m\) if and only if \(p\in m\). This defines precisely \(30\) vertices and \(45\) edges. The graph's six-element underlying alphabet fixes labels but does not impose an extra restriction on allowed generators. Every generator is an unordered subset of graph vertices; all token jumps between arbitrary vertices are permitted when the destination remains a minimum generator. No intermediate nonminimal sets are allowed.

## Proof

The following is a finite exhaustive proof with two standalone, differently implemented verification procedures and exportable certificates. All loops have explicit finite bounds, and the state-generation and graph-distance computations are detailed so that the outputs can be rederived rather than trusted as numerical assertions.

**(1) Construct the graph and all edge-distance signatures.** List the fifteen \(2\)-subsets of the six-element ground set; generate the fifteen perfect matchings of its complete graph recursively by matching the smallest remaining element. Construct the forty-five incidence edges. Breadth-first search from each of thirty vertices returns \(d(v,w)\), and thus the forty-five component vector \((d(v,e):e\in E(T))\) for every \(v\).

**(2) Characterize generators by a complete finite cover.** There are \(\binom{45}{2}=990\) unordered pairs \(\{e,f\}\) of distinct edges. For each candidate landmark \(v\), let \(R_v\) be exactly those pairs for which \(d(v,e)\ne d(v,f)\). By the definition of an edge-metric generator, \(S\) is a generator if and only if \(\bigcup_{v\in S}R_v\) is the complete 990-element pair set. The supplied `verify_python.py` represents each \(R_v\) as an exact 990-bit integer and exhaustively enumerates all \(\binom{30}{k}\) unordered \(k\)-element subsets for \(1\le k\le5\). Counts are \(0,0,0,0,4560\), respectively. For the first four sizes these are exhaustive nonexistence certificates, not samples. It groups the 4560 five-element bases by number of duads and obtains \(2280\) in each of the two stated types, and zero in every other type. The complete lexicographically ordered list is `basis_states.txt`.

**(3) Exhaust the exchange graph.** For each basis \(S\), each of its five elements \(s\), and every \(t\in V(T)\setminus S\), test whether \((S\setminus\{s\})\cup\{t\}\) appears in the complete basis list. This is equivalent to the asserted symmetric-difference-two rule and generates every possible token jump once in each direction. The procedure produces \(74640\) directed incidences or \(37320\) undirected exchange edges. `exchange_edges.txt` lists every undirected edge once, using zero-based line numbers in `basis_states.txt`. Counting its vertex degrees gives exactly \(720\) degree-13 and \(3840\) degree-17 vertices; their degree sum \(720\cdot13+3840\cdot17=74640\) checks the edge count.

**(4) Verify all distances.** Run an ordinary shortest-path breadth-first search from each of the \(4560\) exchange vertices. Each visit reaches all \(4560\) states, proving connectivity; the maxima of distances from each source are \(6\) for \(3840\) bases and \(7\) for \(720\) bases. Their minimum and maximum prove radius six and diameter seven. Recording all \(i<j\) with distance exactly seven gives \(360\) pairs, listed in `distance_7_pairs.txt`.

**(5) Independent recomputation.** `verify_cpp.cpp` reconstructs the incidence graph from a separate perfect-matching enumeration, encodes each edge-distance vector with base-five positional signatures, and tests collision-freeness of edge signatures rather than using the pair-coverage masks. It independently enumerates all candidate landmark sets through size five, forms the exchange graph, and performs every-source breadth-first search. Its outputs agree on generator counts, exchange edges, degrees, connectivity, radii and eccentricities. It also supplies two diameter-witness basis bitmasks. Each verification algorithm relies only on the stated incidence definition, not on `basis_states.txt` or the other implementation for its numerical results.

## Verification

Run `python3 verify_python.py` in the folder containing the files; it reconstructs the graph and regenerates `basis_states.txt`, `exchange_edges.txt`, and `distance_7_pairs.txt`. Compile `verify_cpp.cpp` with `c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp`, then run `./verify_cpp`. Their recorded expected summaries are in `verify_python_output.txt` and `verify_cpp_output.txt`. The deterministic output lists are complete, not representatives. For the Python verifier, the ordering of duads and synthemes and the sorting of bases determine the printed IDs. The programs need the Python standard library or a C++17 compiler, respectively. The all-source searches cover every basis and hence cannot miss peripheral configurations.

## Relationship to prior work

Kelenc, Tratnik and Yero introduced the edge-metric dimension and elementary theory of edge-distinguishing landmarks in the paper posted as arXiv:1602.00291v1 on January 31, 2016 [1]. Their object is exactly the vertex-to-edge distance used here; their general statements, as inspected, do not establish the Tutte–Coxeter minimum and basis-exchange census. The classical duad–syntheme incidence description of this graph is documented by the American Mathematical Society [2] and Brouwer [3]. These structural descriptions fix the graph but do not imply the present optimization or reconfiguration counts.

Ordinary vertex metric dimension is a different problem: it distinguishes vertex pairs, rather than the \(990\) pairs of graph edges. Even its exact value does not imply \(\operatorname{edim}(T)=5\) or the size and diameter of the optimal edge-basis exchange graph. Published work on edge-metric bases of crown and half graphs likewise concerns different incidence and adjacency structures. A mathematical-record search for Tutte–Coxeter edge metric dimension, its aliases (the Tutte eight-cage, the duad–syntheme incidence graph and the \(W(2)\) generalized-quadrangle Levi graph), and optimal-basis exchange statistics did not identify a result determining these quantities. This negative search is not proof of global priority.

## Limitations

This is a finite exact statement for the particular 30-vertex graph; no formula for arbitrary generalized quadrangles or cages is claimed. Computation here provides an exhaustive finite proof through inspectable programs and deterministic certificates, but does not constitute an independent external audit. Source searches may miss unpublished, unindexed, or differently named classifications. The available primary inspection does not establish that no previous researcher computed these same quantities. The numbers refer to unordered vertex landmark sets and unrestricted one-landmark token jumps, not token sliding or fault-tolerant edge resolution.

## References

[1] A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1 (2016-01-31), https://arxiv.org/pdf/1602.00291.

[2] American Mathematical Society, *Tutte–Coxeter Graph*, Visual Insight (2015-08-15), https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/.

[3] A. E. Brouwer, *The generalized quadrangle of order 2*, https://aeb.win.tue.nl/graphs/GQ22.html.
