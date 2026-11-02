# The five-vertex edge-monotonicity obstruction in random greedy adsorption

## Finding
Let \(X(G)\) be the number of vertices accepted by random-order greedy maximal-independent-set sampling on a finite simple graph \(G\): inspect a uniformly random permutation of its vertices, accepting a vertex if no previously accepted vertex is adjacent to it.

**Theorem (exact signed edge effect and first obstruction).** For integers \(k\ge2\), \(m\ge2\), form \(G_{k,m}=K_{1,k}\sqcup K_m\). Let \(h\) be the star centre and \(b\) any fixed vertex of the clique, and set \(H_{k,m}=G_{k,m}+hb\). Coupling the greedy processes by the *same* vertex-ordering yields
\[
X(H_{k,m})=X(G_{k,m})+(k-1)\mathbf1_{E_{k,m}},
\qquad \Pr(E_{k,m})=\frac1{(k+1)(k+m+1)}.
\]
In particular, \(X(H_{k,m})\ge X(G_{k,m})\) pointwise in this coupling, and
\[
\mathbb E X(H_{k,m})-\mathbb E X(G_{k,m})
=\frac{k-1}{(k+1)(k+m+1)}>0.
\]
The full law has support \(\{2,k+1\}\), with
\[
\Pr(X(H_{k,m})=2)=\frac{k+m}{(k+1)(k+m+1)},
\qquad \Pr(X(H_{k,m})=k+1)=1-\frac{k+m}{(k+1)(k+m+1)}.
\]
By contrast, if the clique is replaced by one isolated vertex (\(m=1\)), adding the same edge gives
\[
\mathbb E X(H_{k,1})-\mathbb E X(G_{k,1})
=-\frac{2}{(k+1)(k+2)}<0.
\]
Thus a second clique vertex produces a strict sign reversal, rather than merely weakening a negative edge effect.

Among **all** finite simple graphs, the minimum order of a graph \(G\) admitting a missing edge \(e\) with \(\mathbb E X(G+e)>\mathbb E X(G)\) is five. On five labelled vertices there are exactly \(240\) improving pairs \((G,e)\), comprising exactly **three** isomorphism types of graphs with a distinguished added edge, of labelled orbit sizes \(60,120,60\). Every improving pair at that order has the same increase \(1/15\), so \(1/15\) is also the exact maximum positive single-edge increase on five vertices.

The three marked representatives, with vertices \(0,1,2,3,4\), are:

| Existing edges of \(G\) | Added edge \(e\) | \(\mathbb E X(G)\) | \(\mathbb E X(G+e)\) |
|---|---|---|---|
| \(\{03,04,12\}\) | \(01\) | \(8/3\) | \(41/15\) |
| \(\{02,04,12,13\}\) | \(03\) | \(37/15\) | \(38/15\) |
| \(\{02,03,04,12,13\}\) | \(14\) | \(38/15\) | \(13/5\) |

Here \(ij\) abbreviates the unordered edge between distinct vertices \(i\) and \(j\). The first source graph is a disjoint three-vertex path and an edge; the second is a five-vertex path; the third is a four-cycle with a pendant leaf. In particular, edge-addition improvement occurs even with a **connected source graph**.

## Assumptions and scope
Graphs are finite, simple, undirected, and labelled when counted. Each vertex is inspected exactly once in a uniformly random permutation. Equivalently, the vertices receive independent continuous uniform arrival times. The random variable counts accepted vertices, not the independence number or a deterministic optimum. The star has one centre and \(k\) leaves, and the clique has \(m\) vertices; for the positive coupling \(k,m\ge2\). The five-vertex classification considers every graph and every nonedge, with an added edge treated as distinguished when classifying isomorphism types.

## Proof
Assign independent priorities \(U_v\sim\operatorname{Unif}[0,1]\) to all vertices. In \(G_{k,m}\), exactly one vertex of the clique is accepted, and the star accepts its centre if the centre is earlier than all leaves (then the star accepts one vertex), or else all \(k\) leaves (then it accepts \(k\) vertices). Consequently
\[
\Pr(X(G_{k,m})=2)=\frac1{k+1},
\qquad\Pr(X(G_{k,m})=k+1)=\frac{k}{k+1}.
\]
Consider the graph \(H_{k,m}\) using precisely these same priorities. There is only one additional edge, from the centre \(h\) to the distinguished clique vertex \(b\). If a star leaf precedes \(h\), then \(h\) is blocked in both graphs, all star leaves are accepted, and one clique vertex is accepted in both. If \(h\) precedes every star leaf, the only possibility for a difference is that \(b\) is the first clique vertex and \(b\) precedes \(h\). In this event, \(b\) is accepted, \(h\) is rejected only in \(H_{k,m}\), and all \(k\) leaves are accepted, increasing the total by \(k-1\). If instead \(h\) precedes \(b\), the added edge only rejects \(b\), when it would otherwise be selected; because \(m\ge2\), one of the other clique vertices is subsequently accepted, so the total stays unchanged. If another clique vertex precedes \(b\), then \(b\) is rejected in both graphs, with no effect on the star. These cases are exhaustive.

The gain event is therefore
\[
E_{k,m}=\bigl\{U_b<U_h<\min_{1\le i\le k}U_i,\;U_b<\min_{c\in K_m\setminus\{b\}}U_c\bigr\}.
\]
Integrating first over \(U_b=t\), then \(U_h=s\), gives
\[
\Pr(E_{k,m})
=\int_0^1(1-t)^{m-1}\left(\int_t^1(1-s)^k\,ds\right)dt
=\frac1{(k+1)(k+m+1)}.
\]
The coupling identity and its expectation follow. Since the base total has only values \(2\) and \(k+1\), and the gain event can occur only when its value is \(2\), the displayed full two-point law follows. This also proves stochastic dominance of the total number accepted, not merely an inequality between expectations.

For \(m=1\), the added graph is the larger star \(K_{1,k+1}\). A star with \(r\) leaves has mean \((1+r^2)/(r+1)\), while the disjoint isolated vertex contributes exactly one, so
\[
\frac{1+(k+1)^2}{k+2}-1-\frac{1+k^2}{k+1}
=-\frac2{(k+1)(k+2)}.
\]

It remains to justify the exhaustive smallest-order assertion. For any induced graph \(F\) on \(r\) vertices define \(M(F)=\mathbb E X(F)\). Conditioning on the first inspected vertex \(v\) gives the exact finite recursion
\[
M(\varnothing)=0,
\qquad M(F)=1+\frac1r\sum_{v\in V(F)}M(F-N_F[v]),
\]
where \(N_F[v]\) is its closed neighbourhood. The supplied standard-library program `verify.py` evaluates this rational recursion for **every** labelled simple graph on orders one through five, independently compares its answer with a direct sum over **every** permutation, then compares every missing-edge addition. It considers, respectively, \(1,2,8,64,1024\) labelled graphs, no random samples. For order at most four it finds no positive edge addition. At order five it finds exactly \(240\) positive pairs; each has gain \(1/15\). To classify these without label multiplicity, it computes the lexicographically least representation of each marked pair \((G,e)\) under all \(5!\) relabellings. The resulting canonical classes number three, with orbit sizes \(60,120,60\); their edge sets and rational values are the table above. This is a finite exhaustive proof with the complete auditable enumeration algorithm, not an inference from partial examples.

## Verification
Run `python verify.py` with Python 3 and its standard library, from the directory containing this document. The checker independently computes every graph expectation twice, using the exact first-vertex recursion and exhaustive permutations; checks all nonedges on all orders up to five; computes marked-pair canonical orbits; checks the three displayed representatives; and checks the all-parameter star–clique formula for \(2\le k,m\le6\). It additionally checks the pointwise event identity by every vertex permutation for \(2\le k,m\le3\). The executed output was:

`VERIFY_OK graphs=1099 direct_permutations=124469 improving_marked_pairs=240 isomorphism_types=3 family_parameter_pairs=25`

The infinite family is proved by the priority coupling and exact integral; its correctness does not depend on any finite computation. The five-vertex minimality and classification are finite, and the checker exhaustively visits the stated entire finite domain.

## Relationship to prior work
Random sequential adsorption on graphs is the same random-order greedy maximal-independent-set process. Pippenger (1989) studies this process, especially on regular graphs and structures with few short cycles. Krivelevich, Mészáros, Michaeli and Shikhelman (first posted July 16, 2019) study its local limits and establish, among other results, that the path minimizes mean greedy occupancy among fixed-order trees. Neither their full accessible presentation nor the inspected sources give the star–clique edge-coupling, the sign reversal at the second clique vertex, or the complete marked-five-vertex comparison. The path-minimality theorem compares trees with other trees and does not imply an inequality upon *adding an edge*, which may create a cycle or connect components.

Published exact laws for random-order greedy independent sets on threshold graphs and connected chain graphs concern distributions **within** those graph classes. The star–clique family contains graphs outside those classes, and the present theorem concerns comparisons of the same priorities across two different graphs. In the five-vertex list, the exact law of a particular terminal graph, such as \(K_{2,3}\), does not itself imply the classified edge-improvement statement. The independently inspected public records and targeted literature searches disclosed no equivalent edge-addition comparison. This does not establish definitive historical priority; differently named studies of adsorption responses to changing a single exclusion bond remain a risk.

## Limitations
The stochastic order and explicit two-point law are specific to the star–clique bridge and require \(m\ge2\). Arbitrary edge additions need not increase occupancy; the theorem makes no global monotonicity claim. The finite classification is complete only through five vertices and the listed marked-edge classes, with no classification of all larger improving pairs. The results concern uniform vertex priorities; arbitrary unequal rates are not covered. Historical novelty remains conditional on the inspected literature, and no independent validation is claimed.

## References
1. M. Krivelevich, T. Mészáros, P. Michaeli and C. Shikhelman, “Greedy maximal independent sets via local limits,” arXiv:1907.07216v1, first submitted July 16, 2019; subsequently *Random Structures & Algorithms* 64 (2024), 986–1015, DOI:10.1002/rsa.21200.
2. N. Pippenger, “Random Sequential Adsorption on Graphs,” *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401, DOI:10.1137/0402034.
3. “Exact random-greedy maximal-independent-set law on chain graphs,” publicly available result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-random-greedy-maximal-independent-set-law-on-chain-graphs--36fe61ce32de .
4. “Exact random-greedy independent-set law on threshold graphs,” publicly available result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-random-greedy-independent-set-law-on-threshold-graphs--13703984bf2d .
