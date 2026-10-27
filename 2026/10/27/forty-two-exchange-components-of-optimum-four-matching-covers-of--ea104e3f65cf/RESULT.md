# Forty-two exchange components of optimum four-matching covers of the flower snark \(J_5\)

## Finding
Let \(F=J_5\) be the 20-vertex, 30-edge flower snark defined below. A *four-cover* is an unordered set of four distinct perfect matchings whose union contains every edge of \(F\). Let \(\mathcal R(F)\) have these covers as vertices, with two covers adjacent if they share exactly three perfect matchings. Thus each move replaces one perfect matching and must maintain four-cover feasibility.

There are exactly \(200\) four-covers. Their exchange graph has \(220\) edges and exactly \(42\) components, in four isomorphism classes:

| Copies | Vertices per component | Edges per component | Vertex-degree multiset within a component |
|---:|---:|---:|---|
| \(10\) | \(1\) | \(0\) | \(0^1\) |
| \(20\) | \(5\) | \(5\) | \(1^2,2^1,3^2\) |
| \(10\) | \(7\) | \(9\) | \(1^1,2^2,3^3,4^1\) |
| \(2\) | \(10\) | \(15\) | \(2^5,4^5\) |

All copies within each row are isomorphic as simple graphs; the complete vertex and adjacency descriptions appear in `certificate.json` and are checked by `verify_recursive.py`, including an explicit finite graph-isomorphism backtrack. The four component types are distinguished by their orders. In particular **ten optimal covers are isolated** under every feasible single-matching replacement. The global degree distribution of \(\mathcal R(F)\) is \(0^{10},1^{50},2^{50},3^{70},4^{20}\).

Every four-cover doubles precisely the edges of a single perfect matching of \(F\). Among the \(32\) perfect matchings, exactly two are the doubled-edge matching for \(10\) four-covers each, ten for \(7\) covers each, ten for \(6\) covers each, and ten for \(5\) covers each. The existence of such a doubled-edge matching is previously known in all cubic four-covers; the displayed extension multiplicities are part of the finite census.

## Assumptions and scope
Use indices \(i\in\{0,1,2,3,4\}\), with arithmetic modulo \(5\). The vertices of \(F\) are \(a_i,b_i,c_i,d_i\). Its edges are \(a_ib_i,a_ic_i,a_id_i,b_ib_{i+1}\), together with the ten-cycle
\[
c_0c_1c_2c_3c_4d_0d_1d_2d_3d_4c_0.
\]
All edges on that cyclic word join consecutive symbols, including the final return edge. This precisely specifies a simple cubic graph; edge order and vertex naming are fixed in the included source codes. A perfect matching meets each graph vertex once; hence it has \(10\) edges. A cover is a **set**, not a labeled or repeated four-tuple. No intermediate noncover is allowed in the exchange graph. The theorem concerns this single graph, not every flower snark.

## Proof
**Exhaustive finite matching lemma.** `verify_recursive.py` constructs exactly the stated 30 edges. At each recursive step it takes the least-indexed unmatched vertex and branches over each incident edge to an unmatched neighbor. Every perfect matching must use exactly one of these edges. Branches are disjoint and the reduction removes exactly the selected pair of vertices; induction on the number of unmatched vertices proves that every and only perfect matching appears exactly once. The program verifies that the resulting set contains \(32\) distinct matchings.

**Exhaustive four-cover lemma.** Every possible unordered four-cover is among the \(\binom{32}{4}=35{,}960\) four-subsets of those perfect matchings. The verifier computes the bitwise union of the four edge-incidence masks and retains it precisely when all \(30\) edges occur. It finds exactly \(200\) covers. It also explicitly checks that no three of the \(32\) perfect matchings cover the edge set; hence the minimum perfect-matching covering number is \(4\). That latter number agrees with the pre-existing theorem of Fouquet and Vanherpe.

**Exchange and component lemma.** For each retained four-subset, the verifier indexes its four three-subsets. Two retained four-subsets are adjacent exactly when they share one of those indexed triples. Every such pair is added once to a simple undirected adjacency relation; this gives \(220\) edges. Exhaustive graph traversal yields \(42\) connected components. Exact isomorphism testing uses a bijective backtrack restricted to vertices of equal degree and checks every adjacency/nonadjacency against the partially defined bijection. It verifies isomorphism among the components within each row in the table, with multiplicities \(10,20,10,2\). The class orders \(1,5,7,10\) are distinct, proving that these are four and only four isomorphism classes. The component vertex and edge counts independently sum to \(200\) and \(220\).

**Algorithmically separate verification.** `verify_local_csp.py` does not first enumerate perfect matchings. It assigns to each graph edge a nonempty subset of four named colors. Each graph vertex must see a partition of the four colors among its three incident edges, necessarily of block sizes \(2,1,1\). Exactly \(3\binom42 2=36\) labeled local assignments are possible. Backtracking over the 20 vertices enforces equality of the assigned color subset at both ends of every edge. At a fixed root, global color permutations allow the pair on its doubled edge to be normalized to colors \(1,2\) and the other two incident edges to colors \(4,8\) in fixed order. There are three possible doubled root edges. Each unordered four-cover has exactly two normalized colorings, corresponding to interchanging colors \(1\) and \(2\); all other color permutations have been fixed. This independently produces \(400\) normalized labeled solutions, therefore \(200\) unordered four-covers. From their common three-matchings, it reconstructs the same \(220\) edges and the same component order/edge/degree profiles.

**Doubled-edge lemma.** At a vertex of a cubic graph, the four matchings each choose exactly one incident edge. In a four-cover all three incident edges occur, so their covering multiplicities must be \((2,1,1)\). The doubly covered edges consequently form a perfect matching; the verifier identifies that matching among its \(32\) candidates for every cover and counts its extensions. The resulting distribution \(10^2,7^{10},6^{10},5^{10}\) accounts for \(200\) covers.

These are finite exhaustive proofs: the specified loops range over finite sets, their completeness is established above, and all asserted counts and graph identities are explicitly checked. The recorded outputs alone would not establish completeness without the algorithms.

## Verification
With Python 3 and its standard library, run `python3 verify_recursive.py` and `python3 verify_local_csp.py`. The machine-readable outputs are included in `recursive_output.json` and `local_csp_output.json`. Running `python3 verify_recursive.py --certificate` emits the exact complete enumeration in `certificate.json`: 30 graph edges, all 32 matching bitmasks, all 200 four-cover index sets, all 220 exchange edges, and all 42 component vertex sets. All arrays are zero-based; matching indices use the sorted order of masks produced by the first program.

A fresh execution of each verifier completed successfully. Both methods found \(200\) covers, \(220\) exchange edges, \(42\) components, and the same four component profiles. The first method checks graph isomorphism directly; the second independently confirms every component order/edge/degree profile. These tests establish the finite claim for the precisely defined graph only.

## Relationship to prior work
Fouquet and Vanherpe, *On the perfect matching index of bridgeless cubic graphs* (arXiv:0904.1296v1, 2009), explicitly construct the flower snark, prove its perfect-matching index is \(4\) (Theorem 3.8), and observe the doubly covered perfect matching in any cubic four-cover (Proposition 3.1). Those facts are credited, not claimed as new. Their inspected sections do not state a count of four-covers or their single-replacement exchange components.

Hägglund and Markström, *Shortest cycle covers and cycle double covers with large 2-regular subgraphs* (arXiv:1306.3088v1, 2013), show a general correspondence between cubic four-covers and certain five-cycle-double covers. This broader relationship does not give the explicit \(J_5\) reconfiguration classification. Esperet and Mazzuoccolo (arXiv:1301.6926v1, 2013) prove general hardness results for perfect-matching covering number, not the present finite exchange graph. Máčajová and Škoviera (arXiv:2008.01398v1, 2020) give a broad tetrahedral-flow formulation for four-cover existence, not this individual graph's exchange components.

Additional targeted published-record and terminology searches compared exact counts, cover/index aliases, equivalent labeled and unlabeled formulations, and general results that might subsume the numerical statements. No directly covering published claim was identified; this is a best-knowledge originality assessment, not a proof of historical uniqueness.

## Limitations
The finite classification does not establish an exchange theorem for all flower snarks, nor a complexity result for finding paths between minimum covers on arbitrary cubic graphs. A different published computational table or an implicit calculation inside less-accessible literature could contain equivalent data. The two verification programs are algorithmically different, but they and this written argument have not undergone independent external mathematical audit.

## References
1. J.-L. Fouquet and J.-M. Vanherpe, *On the perfect matching index of bridgeless cubic graphs*, arXiv:0904.1296v1 (first posted 2009-04-08), https://arxiv.org/abs/0904.1296 .
2. J. Hägglund and K. Markström, *Shortest cycle covers and cycle double covers with large 2-regular subgraphs*, arXiv:1306.3088v1 (first posted 2013-06-13), https://arxiv.org/abs/1306.3088 .
3. L. Esperet and G. Mazzuoccolo, *On cubic bridgeless graphs whose edge-set cannot be covered by four perfect matchings*, arXiv:1301.6926v1 (first posted 2013-01-29), https://arxiv.org/abs/1301.6926 .
4. E. Máčajová and M. Škoviera, *Cubic graphs that cannot be covered with four perfect matchings*, arXiv:2008.01398v1 (first posted 2020-08-04), https://arxiv.org/abs/2008.01398 .
