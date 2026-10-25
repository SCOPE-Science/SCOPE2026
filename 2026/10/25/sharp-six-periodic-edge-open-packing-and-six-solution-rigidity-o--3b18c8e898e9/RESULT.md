# Sharp six-periodic edge open packing and six-solution rigidity of Möbius ladders

## Finding
Let \(M_{2n}\) be the cubic Möbius ladder on \(\mathbb Z/(2n)\mathbb Z\), with edges \(\{i,i+1\}\) and \(\{i,i+n\}\). For every integer \(n\ge3\), its edge-open-packing number is
\[
\rho_e^{\mathrm o}(M_{2n})=\begin{cases}n,&n\equiv3\pmod6,\\n-1,&n\not\equiv3\pmod6.\end{cases}
\]
In the equality class \(n\equiv3\pmod6\), the labelled graph has **exactly six** optimal edge-open-packing subsets. Each is the union of all three incident edges at each vertex in a single periodic residue class of one of the two bipartition sides. These are exactly three cyclic phases for each bipartition choice; there are no other optimal subsets of cardinality \(n\).

## Assumptions and scope
Graphs are finite, simple and undirected. An *edge open packing* is a set \(P\) of edges such that no two distinct edges of \(P\) have a *third* edge joining one endpoint of the first to one endpoint of the second. Equivalently, the subgraph induced by the endpoints of \(P\) is a disjoint union of induced stars, and its edge set is precisely \(P\). The parameter \(\rho_e^{\mathrm o}(G)\) denotes the maximum possible \(|P|\). Every \(M_{2n}\) here has \(2n\) vertices, \(3n\) edges, and degree three. Vertex labels, additions and subtractions in edge formulas are taken modulo \(2n\).

## Proof
**Upper bound and rigidity of equality.** In any cubic graph, the induced components supported by an edge open packing \(P\) are stars. Choose for each edge of \(P\) its leaf endpoint (for a one-edge star choose either endpoint). These chosen leaves are all distinct, and each has exactly two incident edges leaving the endpoint support of \(P\). Those two exterior edges are distinct across leaves and distinct from \(P\). Hence the graph contains at least \(3|P|\) edges. In \(M_{2n}\), therefore, \(|P|\le n\).

If \(|P|=n\), every graph edge has been accounted for in the counting argument. Thus each star centre has no exterior edge, each star is a full induced \(K_{1,3}\), and the graph has no edges between vertices outside the selected endpoint support. Indeed, a shorter star would have a centre (or the unused endpoint of a \(K_2\)) with an extra exterior edge, contradicting equality of the count. Writing \(A\) for the star centres, \(B\) for their leaves and \(C\) for unused vertices, all graph edges join \(B\) to \(A\cup C\), and every vertex in \(B\) has exactly one neighbour in \(A\). Hence the graph is bipartite. In a connected cubic bipartite graph both sides have the same size. Since every vertex of \(A\) has exactly three distinct neighbours in \(B\), we have \(|B|=3|A|\).

In \(M_{2n}\), the cycle edges force any bipartition to alternate parities, and the antipodal edges preserve bipartiteness exactly when \(n\) is odd. Each parity class has \(n\) vertices, so equality requires simultaneously \(n\) odd and \(3\mid n\), that is \(n\equiv3\pmod6\). For every other residue, integrality yields \(\rho_e^{\mathrm o}(M_{2n})\le n-1\).

**Construction in every residue.** Let \(q=\lfloor n/6\rfloor\) and \(r=n-6q\). For a vertex \(c\), write \(S(c)\) for its three incident edges. Define the basic set of centres
\[
T=\{6i:0\le i<q\},\qquad B=\{n+3+6i:0\le i<q\}.
\]
The following table specifies an edge set \(P\) in every case. "Full" means taking every edge in \(S(c)\) for each displayed centre; additional edges are ordinary unordered graph edges.

| \(r\) | Full-star centres | Deletion/addition | \(|P|\) |
|---|---|---|---|
| 0 | \(T\cup B\) | Delete \(\{0,2n-1\}\) | \(6q-1\) |
| 1 | \(T\cup B\) | None | \(6q\) |
| 2 | \(T\cup B\) | Add \(\{6q-1,6q\}\) | \(6q+1\) |
| 3 | \(\{6i:0\le i\le2q\}\) | None | \(6q+3\) |
| 4 | \(T\cup B\cup\{6q\}\) | None | \(6q+3\) |
| 5 | \(T\cup B\) | Add \(\{6q-1,6q\}\), \(\{6q,6q+n\}\), \(\{6q+2,6q+3\}\), \(\{6q+2,6q+2+n\}\) | \(6q+4\) |

Here is a uniform direct verification of the table. For vertices at cyclic perimeter distance \(d\in\{0,\dots,n\}\), their graph distance in \(M_{2n}\) is \(\min\{d,1+n-d\}\): a shortest walk uses either no antipodal chord or exactly one. Thus two full stars around distinct centres have no edge between their endpoint supports when the centres are at graph distance at least four. Centres within \(T\), or within \(B\), differ by multiples of six not approaching the antipodal difference closer than six; cross differences are \(n+3+6(j-i)\), so their distance from the antipodal difference is at least three. Their cyclic distance from zero is at least \(r+3\). Consequently the basic centres have pairwise graph distance at least four for \(r\ne0\). For \(r=0\), precisely the last centre \(2n-3\) and first centre \(0\) have graph distance three, producing the unique intervening edge \(\{2n-2,2n-1\}\) between their star leaves. Deleting \(\{0,2n-1\}\) removes \(2n-1\) from the endpoint support and therefore eliminates this conflict.

For \(r=4\), the extra centre \(6q\) is at graph distance at least four from the basic centres. For \(r=3\), distinct centres in the displayed progression are six apart on the perimeter, and antipodal differences are three away from every multiple of six, again giving separation at least four. For \(r=2\), each endpoint of the extra edge \(\{6q-1,6q\}\) is at graph distance at least three from the basic centres; hence its two endpoints have no edge to any full-star support. For \(r=5\), the two additional pairs of edges induce two disjoint \(K_{1,2}\) stars centred at \(6q\) and \(6q+2\). These two induced stars are nonadjacent to each other by direct examination of the four specified leaves, and each partial-star centre is at graph distance at least four from every basic centre. This covers the boundary cases \(q=0\) in residues three, four and five as well. Therefore all table sets are valid edge open packings. Their listed sizes match the upper bounds, proving the formula.

**Exactly six equality packings.** Suppose \(n=6q+3\). Equality requires \(A\) to lie entirely in one parity class and give each vertex of the opposite class precisely one neighbour in \(A\). For the choice of even-indexed centres, define \(x_j=1\) if \(2j\in A\) and zero otherwise, for \(j\in\mathbb Z/n\mathbb Z\). Put \(h=(n+1)/2\). The three even neighbours of the odd vertex \(2j+1\) yield
\[
x_j+x_{j+1}+x_{j+h}=1\qquad(j\in\mathbb Z/n\mathbb Z).
\]
Shifting this equation by \(h\), using \(2h\equiv1\pmod n\), and subtracting gives \(x_j=x_{j+h+1}\) for all \(j\). As \(\gcd(n,h+1)=3\), the sequence is three-periodic. Since \(h\equiv2\pmod3\), the original equation becomes \(x_0+x_1+x_2=1\), so exactly one of the three residue classes is selected. The converse is immediate. This gives exactly three centre sets in the even class; the odd class gives three more by rotation. The selected full-star edges uniquely determine their centres, so all six edge sets are distinct.

## Verification
The accompanying \(verify.py\) constructs every displayed edge family and checks its induced endpoint graph, with \(n=3,\ldots,999\) passing. Independently, direct subset enumeration proves the optimum for \(n=3,\ldots,6\), and an integer-programming formulation of the **original edge-pair conflict definition** confirms it for \(n=3,\ldots,36\). A separate exact-cover census gives exactly three feasible centre configurations on each parity class for \(n\in\{3,9,15,21,27,33\}\). The test output is in \(verify_output.txt\). These finite tests do not prove the unbounded formula: the proof above does.

Run: `python3 verify.py`. Dependencies: Python 3, NumPy and SciPy with its mixed-integer optimizer. \(n\) is the parameter in \(2n\) vertices, not the total graph order.

## Relationship to prior work
Edge open packing was introduced by Chelladurai, Kalimuthu and Soundararajan. Brešar and Samadi established the general \(|E(G)|/\delta(G)\) upper bound and characterized equality structurally; the cubic upper bound and bipartite necessity used above are therefore established context, not novel claims. Pandey and Santra gave general necessary-and-sufficient conditions for exact packing numbers and characterized values near the entire edge count, but no numerical Möbius-ladder formula or six-solution count. Brešar, Dravec, Hedžet and Samadi studied the same invariant on graph products and certain hypercubes; their product bounds do not directly give this twisted-cyclic graph family. Das and Santra's October 2026 work supplies algorithms for AT-free, chordal and convex bipartite classes without this uniform formula.

For comparison, a separately recorded exact result for the *untwisted* circular ladder \(C_n\square K_2\) attains \(n\) when \(6\mid n\); this graph is not \(M_{2n}\). The present result identifies the complementary shifted equality phase \(n\equiv3\pmod6\) under the Möbius twist, and proves the complete six-residue construction and equality census. A numerical algorithm or a general characterization without resolving the cyclic constraints is not a covering closed formula.

## Limitations
This result concerns only the graph \(M_{2n}\), \(n\ge3\), not arbitrary cubic graphs or twisted strips with changed rung connections. It counts optimum configurations only in the equality branch; no claim is made about the total number of near-optimal \(n-1\)-edge packings. It is a mathematical proof with self-review, not an independent audit. Unindexed equivalent results under injective edge colouring, efficient star packing, generalized Petersen/circulant graph, or cyclic exact-cover language remain possible bibliographic risks.

## References
1. G. K. Das and K. Santra, *Maximum Edge Open Packing on AT-Free, Chordal, and Convex Bipartite Graphs*, arXiv:2610.02275v1, first posted 2026-10-01, https://arxiv.org/html/2610.02275.
2. B. Brešar and B. Samadi, *Edge open packing: complexity, algorithmic aspects, and bounds*, arXiv:2403.00750v1, https://arxiv.org/html/2403.00750, especially Theorem 4.1.
3. A. Pandey and K. Santra, *Edge open packing: further characterizations*, arXiv:2508.01935v1, https://arxiv.org/html/2508.01935v1.
4. B. Brešar, T. Dravec, J. Hedžet and B. Samadi, *Induced matching vs edge open packing: trees and product graphs*, arXiv:2406.04020v2, https://arxiv.org/html/2406.04020v2.
5. G. Chelladurai, K. Kalimuthu and S. Soundararajan, *Edge open packing sets in graphs*, RAIRO Operations Research 56 (2022), 3765–3776, https://doi.org/10.1051/ro/2022171.
