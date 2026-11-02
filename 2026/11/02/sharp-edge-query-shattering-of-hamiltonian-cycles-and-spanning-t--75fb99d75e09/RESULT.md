# Sharp edge-query shattering of Hamiltonian cycles and spanning two-factors

## Finding

Let \(n\ge 3\), let \(E_n=\binom{[n]}2\), and identify each spanning simple graph with its Boolean edge-incidence function on \(E_n\). Let \(\mathcal C_n\) consist of all Hamiltonian cycles on \([n]\), and let \(\mathcal F_n\) consist of all spanning simple two-regular graphs (two-factors) on \([n]\). Every query tests the presence of one edge in the unknown graph.

For every integer \(n\ge5\), both concept classes have exactly
\[
\operatorname{VCdim}(\mathcal C_n)=\operatorname{VCdim}(\mathcal F_n)=n-2.
\]
In particular, a single spanning path on \(n-1\) vertices, with its \(n-2\) edges used as queries, is shattered already by the Hamiltonian cycles.

For \(3\le n\le7\), the exact static/adaptive dimension pairs for both classes are, in order of increasing \(n\),
\[
(0,0),\quad(1,1),\quad(3,3),\quad(4,5),\quad(5,6).
\]
Thus six vertices is the first order at which either class has strictly greater Littlestone than VC dimension; both classes have a gap of exactly one at orders six and seven.

The complete finite shattered-support polynomials, with the coefficient of \(z^j\) equal to the number of labeled \(j\)-edge query supports shattered, are:

| \(n\) | Hamiltonian cycles \(\mathcal C_n\): coefficients from constant term | Two-factors \(\mathcal F_n\): coefficients from constant term |
|---|---|---|
| 3 | 1 | 1 |
| 4 | 1, 6 | 1, 6 |
| 5 | 1, 10, 45, 60 | 1, 10, 45, 60 |
| 6 | 1, 15, 105, 375, 360 | 1, 15, 105, 395, 360 |
| 7 | 1, 21, 210, 1155, 3465, 2520 | 1, 21, 210, 1190, 3780, 2520 |

## Assumptions and scope

Graphs are undirected, simple, loopless, labeled and spanning. A two-factor has degree exactly two at every vertex, hence is a vertex-disjoint union of cycles each having length at least three. A Hamiltonian cycle is a connected two-factor. Empty query supports count as shattered. The Littlestone dimension is the greatest depth of a complete binary membership-query tree for which every root-to-leaf response sequence has a compatible concept. It is a shattering depth, not a worst-case identification-query count.

The VC formula is proved for all \(n\ge5\). The exact Littlestone dimensions and complete support profiles are only claimed at \(3\le n\le7\); no larger-order adaptive formula or optimality of the seven-vertex cutoff for any other property is claimed.

## Proof

**Universal VC upper bound.** Every two-factor has exactly \(n\) edges, so a query support of more than \(n\) edges cannot be shattered. Suppose a shattered support \(S\) has \(n\) edges. Realizing all positive answers forces \(S\) to be the entire edge set of a two-factor; omitting just one queried edge while requiring all other edges forces that edge back by the degree-two constraints, which is impossible. Suppose instead \(|S|=n-1\). Its all-positive realization is a two-factor \(F\) with one edge \(e\) removed, so \(S\) consists of cycles and one path on at least three vertices. Let \(u\) be one endpoint of this path, let \(w\) be its neighbor, and let \(v\) be the opposite endpoint. Requiring all edges of \(S\setminus\{uw\}\), while forbidding \(uw\), leaves degree deficits two at \(u\), one at \(w\), one at \(v\), and zero everywhere else. Any degree-two completion must join \(u\) to both \(w\) and \(v\), hence must include the forbidden edge \(uw\). Therefore no support of \(n-1\) edges is shattered. Supersets of unshattered supports cannot be shattered; the upper bound is \(n-2\). This applies simultaneously to Hamiltonian cycles and all two-factors.

**Universal VC lower bound.** Choose a path \(v_1v_2\cdots v_{n-1}\) and a further vertex \(z\), and query the \(n-2\) path edges. For any set \(T\) of edges required to be present, the graph consisting of \(T\) is a disjoint union of \(k\) ordered path blocks \(B_1,\ldots,B_k\), plus the isolated vertex \(z\). We exhibit a Hamiltonian cycle that traverses each block internally and uses none of the path edges omitted from \(T\).

If \(k=1\), insert \(z\) between the two endpoints of the single path block. If \(k=2\), at least one block has two or more vertices because \(n-1\ge4\); traverse the blocks in their original order and reverse a non-singleton block if necessary to make the joining edge different from the omitted path edge at their boundary. If \(k=3\), at least one block has two or more vertices. When \(B_1\) is non-singleton, traverse \(B_2,B_1,B_3,z\), orienting \(B_1\) forward; when \(B_2\) is non-singleton, traverse \(B_1,B_2,B_3,z\), orienting \(B_2\) backward; when \(B_3\) is non-singleton, traverse \(B_2,B_3,B_1,z\), orienting \(B_3\) backward. The sole possibly adjacent original blocks then join through endpoints different from the forbidden path boundary. If \(k\ge4\), traverse blocks with even indices, followed by blocks with odd indices, followed by \(z\). In this order no consecutive blocks have consecutive original indices: within each parity the index jumps by two, and the last even index differs from the first odd index by at least three. Every inter-block edge is therefore distinct from the omitted path edges. In every case each block is traversed as a path and \(z\) closes the list into a single simple spanning cycle. Hence every Boolean assignment on the queried path edges occurs within \(\mathcal C_n\), proving the lower bound for both classes.

**Exact finite adaptive bounds.** For each \(3\le n\le7\), exhaustive generation lists precisely the edge masks having degree two at every vertex. Connected masks give the Hamiltonian subfamily. The generator verifies hypothesis counts \((1,3,12,70,465)\) for all two-factors and \((1,3,12,60,360)\) for Hamiltonian cycles. Every query support is tested through its complete set of Boolean restrictions; pruning a nonshattered support is valid because no larger support containing it can be shattered. This yields the displayed exact support counts.

For any nonempty hypothesis version space \(V\), put \(V_q^b=\{H\in V:\mathbf1[q\in H]=b\}\). A complete depth-\(d\) online tree exists exactly when \(d=0\), or \(|V|\ge2^d\) and some query \(q\) satisfies the same criterion at depth \(d-1\) in both \(V_q^0\) and \(V_q^1\). This finite recurrence considers every possible initial edge query and is exact by induction on depth. Complete lower-bound trees with one distinct compatible graph at each terminal leaf are included in the certificates.

The upper bounds at \(n=3,4,5\) follow from the total hypothesis counts \(1,3,12\). At \(n=6\), every first-query positive branch contains 28 two-factors, or 24 Hamiltonian cycles, fewer than the 32 concepts required for a depth-five continuation; hence a depth-six tree is impossible. At \(n=7\), every possible first edge is conjugate by relabeling. For the fixed first edge \(\{0,1\}\), the positive branch contains 155 two-factors and 120 Hamiltonian cycles. The exhaustive depth predicate on this positive branch rejects a depth-six continuation in both classes (176 states for two-factors, 86 states for Hamiltonian cycles, with caches initialized solely for this check). Thus no depth-seven tree exists. The displayed depth-five and depth-six lower trees prove sharpness.

## Verification

Run `python3 verify_2factors.py` for the two-factor census and finite depth proof, `python3 verify_hamilton.py` for Hamiltonian cycles and `python3 independent_2factors.py` for the separate cycle-permutation generator, independent fiber-refinement VC census, independent upper-branch check and complete tree-witness replay. The two included JSON certificates contain every query node, every compatible terminal graph and the full finite hypothesis lists for reconstruction.

All finite computations use integer edge masks, integer bit operations and exact enumeration; no floating point tolerance, random sampling or extrapolation is involved. The all-size VC theorem relies on the preceding mathematical argument, not the finite computations. The independent implementation generates two-factors as permutation cycle decompositions; the primary implementation generates them as degree-two subsets of the complete-graph edge set.

## Relationship to prior work

The finite graph-family edge-query concept class here is distinct from the graph-neighborhood systems studied by Adler, Benediktsson and Macpherson in their 2020 preprint on Johnson and Hamming graphs. Their results bound shattering by graph adjacency neighborhoods; a concept in the present work is an entire two-factor or Hamiltonian cycle, and its query domain is the set of potential edges of the complete graph. Kostochka, Raspaud, Toft, West and Zirlin study existence of regular factors in prescribed host graphs, not static or adaptive shattering over all spanning two-factors of a complete graph. Coudert and collaborators study algorithms for graph-neighborhood VC dimension, again a different query system. No implication from these particular theorems yields the present all-order formula or the finite adaptive onset. A search of related literature and published mathematical records found no directly covering statement; this is not a proof of historical priority.

## Limitations

Only the VC dimension is classified for every \(n\). The exact online dimensions beyond seven vertices remain unproved here. The complete support-count polynomials are only supplied through seven vertices. The exact finite computations depend on deterministic exhaustive code and tree certificates. Historical-priority searches can miss equivalent formulations, including descriptions in terms of incidence families of Hamiltonian subgraphs, cycle systems or edge-prediction mistake trees.

## References

1. A. V. Kostochka, A. Raspaud, B. Toft, D. B. West and D. Zirlin, *Cut-edges and regular factors in regular graphs of odd degree*, first public preprint 14 June 2018, arXiv:1806.05347, https://arxiv.org/abs/1806.05347.
2. I. Adler, B. G. Benediktsson and D. Macpherson, *Vapnik–Chervonenkis dimension and density on Johnson and Hamming graphs*, first public preprint 31 July 2020, arXiv:2007.16042, https://arxiv.org/abs/2007.16042.
3. D. Coudert, M. Csikós, G. Ducoffe and L. Viennot, *Practical Computation of Graph VC-Dimension*, SEA 2024, DOI:10.4230/LIPIcs.SEA.2024.8, https://doi.org/10.4230/LIPIcs.SEA.2024.8.
