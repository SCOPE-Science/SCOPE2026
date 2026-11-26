# Exact edge-metric bases and optimal landmark exchanges in the Tutte–Coxeter graph

## Finding

Let \(T\) be the 30-vertex Tutte–Coxeter graph, realized as the incidence graph of the 15 duads and 15 synthemes on a six-element set. For a vertex \(v\) and an edge \(e=uw\), let \(d(v,e)=\min\{d(v,u),d(v,w)\}\). An edge-metric generator is a set \(S\) such that the vectors \((d(s,e))_{s\in S}\) are distinct for the 45 edges. An edge-metric basis is a smallest such set.

The edge-metric dimension is \(5\). There are exactly \(4560\) bases: \(2280\) with two duads and three synthemes, and \(2280\) with three duads and two synthemes. There are no edge-metric generators of sizes one through four.

Join two bases when one is obtained from the other by replacing exactly one landmark. This exchange graph has \(37320\) undirected edges, is connected, has radius \(6\) and diameter \(7\), and has \(360\) unordered pairs at distance seven. Its full joint vertex census is:

| Degree | Eccentricity | Bases |
|---:|---:|---:|
| 13 | 6 | 720 |
| 13 | 7 | 0 |
| 17 | 6 | 3120 |
| 17 | 7 | 720 |

In particular every degree-13 basis has eccentricity six, whereas eccentricity seven occurs only at degree 17. The marginal histograms do not determine this pairing and are unchanged by the correction.

## Assumptions and scope

The ground set is \(\{0,1,2,3,4,5\}\). A duad is an unordered two-element subset. A syntheme is a partition into three duads. Number the duads lexicographically from \(0\) to \(14\), then the synthemes from \(15\) to \(29\), lexicographically by sorted lists of their duads. The incidence edges are exactly the pairs in which the duad is a member of the syntheme. All graph vertices are eligible as landmarks. The bases are unordered sets; a replacement can jump to any graph vertex not already present if the result is again a basis. No nonminimum intermediate set is allowed.

## Proof

This is a bounded exhaustive proof. The construction, enumeration and shortest-path stages are as follows.

1. Enumerate the two-element subsets and the perfect matchings of the ground set. To list the matchings, pair the smallest remaining element with each possible partner and recurse on the remaining elements. Form the incidence adjacency lists by testing membership. Breadth-first search from all 30 vertices gives the vertex distance table, and the minimum of the two endpoint distances gives the exact edge-distance table.
2. Index the \(\binom{45}{2}=990\) unordered edge pairs. For each vertex \(v\), set the bits corresponding to pairs on which the two distances from \(v\) differ. A subset resolves the edges if and only if its bitwise union is the entire 990-bit mask. `verify_python.py` tests every subset of sizes one through five, obtaining \(0,0,0,0,4560\) and the two composition counts. The empty set also cannot resolve any edge pair. `basis_states.txt` is the complete ordered list of passing five-subsets. The separate `verify_cpp.cpp` implementation tests uniqueness of base-five edge signatures instead of mask coverage and obtains the same minimum and count.
3. The exchange relation is precisely intersection of size four for distinct bases. `verify_python.py` and `verify_cpp.cpp` build adjacency by testing each replacement. Equivalently, place every five-set into its five four-subset buckets and take every unordered pair in each bucket. A pair of distinct five-sets occurs at most once because it cannot have two distinct common four-subsets. This constructs all \(37320\) exchange edges. `verify_joint.py` uses the bucket computation and compares the entire result with `exchange_edges.txt`.
4. For each of the \(4560\) sources, start a breadth-first search at distance zero and assign a previously unvisited neighbor distance one more than the vertex being expanded. Every source reaches the entire exchange graph. For each source separately, take the maximum assigned distance and increment a bin indexed by the pair (source degree, maximum distance). `verify_joint.py` gives the displayed joint histogram. The minimum and maximum eccentricities prove radius six and diameter seven. The same pass records each distance-seven pair with increasing labels, giving exactly the 360 pairs in `distance_7_pairs.txt`. The two original verifier outputs report only the separate degree and eccentricity histograms; those outputs alone do not verify a joint assignment.

## Verification

In a directory with the certificates, run `python3 verify_joint.py`, or pass the certificate directory as its single argument. It requires only the Python standard library and checks the full edge list, all-source distances, the joint histogram and the full distance-seven list. Its expected output is in `verify_joint_output.txt`. To check that the certificate begins with exactly the optimum landmark sets, regenerate the lists with `python3 verify_python.py`; `c++ -O2 -std=c++17 verify_cpp.cpp -o verify_cpp` followed by `./verify_cpp` verifies the minimum and the marginal census using a separate signature test. Their existing summaries remain valid. The joint check is exhaustive, not a sampled inference from the marginals.

## Relationship to prior work

Kelenc, Tratnik and Yero [1] define precisely the vertex-to-edge distinguishing invariant used here. The AMS description [2] and Brouwer [3] give the incidence geometry of the same graph (also called the Tutte eight-cage or the incidence graph of the generalized quadrangle of order two). They identify the input graph and invariant but do not supply the edge-basis or exchange-graph census in the inspected passages. Ordinary metric bases distinguish pairs of vertices, not pairs of edges; their counts on this graph do not imply the result. The closest inspected Coxeter-graph exchange census is for the 28-vertex Coxeter graph and ordinary metric bases, a different graph and invariant. The comparison is bounded and does not establish publication priority.

## Limitations

This is a finite exact result for this incidence graph and this token-jumping rule, not a formula for arbitrary cages, generalized quadrangles, vertex-resolving bases or token sliding. The proof relies on reproducible exact enumeration, not on formal proof-assistant certification. Earlier computations under different names or outside the inspected literature may exist.

## References

1. A. Kelenc, N. Tratnik, I. G. Yero, *Uniquely identifying the edges of a graph: the edge metric dimension*, arXiv:1602.00291v1 (2016-01-31), https://arxiv.org/pdf/1602.00291.
2. American Mathematical Society, *Tutte–Coxeter Graph*, Visual Insight (2015-08-15), https://blogs.ams.org/visualinsight/2015/08/15/tutte-coxeter-graph/.
3. A. E. Brouwer, *The generalized quadrangle of order 2*, https://aeb.win.tue.nl/graphs/GQ22.html.
