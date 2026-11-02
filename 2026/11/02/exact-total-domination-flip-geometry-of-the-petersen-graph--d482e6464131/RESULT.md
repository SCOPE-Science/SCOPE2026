# Exact total-domination flip geometry of the Petersen graph

## Finding
Let \(P=\operatorname{KG}(5,2)\), and let \(\mathcal D^t_k(P)\) be the graph of total dominating sets of cardinality at most \(k\), with one-vertex addition/deletion adjacency. The first connected cap is \(k=7\). At that cap, the reconfiguration graph has exactly \(332\) vertices, \(980\) edges, radius \(8\), and diameter \(10\). The eccentricities are \(8\) at exactly \(100\) configurations, \(9\) at exactly \(220\), and \(10\) at exactly \(12\).

There is an exact combinatorial isomorphism between \(\mathcal D^t_7(P)\) and the one-edge-toggle graph of **labelled triangle-free simple graphs on five vertices with at least three edges**. Under this isomorphism, the \(12\) peripheral states correspond precisely to the labelled five-cycles; the only six unordered diametral pairs are the complementary pairs of five-cycles. For any two states \(U,V\), their graph distance is either \(|U\triangle V|\) or \(|U\triangle V|+2\). Exactly \(735\) of the \(54{,}946\) unordered pairs require the extra two moves. In particular, every five-cycle configuration has Hamming-geodesic routes to every other configuration.

The exact counts of unordered pairs at distances \(1,\ldots,10\), respectively, are
\[
(980,3210,7070,11585,13170,10970,5810,1875,270,6).
\]
The known number of labelled triangle-free graphs on five vertices, and consequently the raw number \(332\) of eligible configurations, are **not presented as independent novelty**. The mathematical contribution proposed here is their sharp reconfiguration threshold and complete metric geometry.

## Assumptions and scope
Let \(X=\{0,1,2,3,4\}\). The Petersen graph has the ten two-element subsets of \(X\) as vertices, adjacent when disjoint. A set \(D\) of its vertices is *total dominating* when each vertex, including those belonging to \(D\), has at least one neighbor in \(D\). The cap \(k\) means \(|D|\le k\); a move adds or removes **one** Petersen vertex, never a simultaneous exchange.

Interpret \(D\) as an edge set of the complete graph \(K_5\). Write \(F=K_5-D\) for the labelled complementary graph on \(X\). The complement is a set complement **inside** \(E(K_5)\), not a vertex complement. Since \(K_5\) has ten edges, \(|D|\le7\) is equivalent to \(|E(F)|\ge3\). Complementation preserves single-edge differences and Hamming distance. All graphs are labelled, and unordered pairs of distinct reconfiguration states are counted only once.

## Proof
**1. Exact state equivalence.** A Petersen vertex \(e=\{u,v\}\) has a selected Petersen neighbor exactly when some edge of \(D\) avoids both \(u\) and \(v\). Failure of total domination at \(e\) therefore means that \(\{u,v\}\) is a two-vertex cover of the graph \((X,D)\). Since the complement of a vertex cover is independent, \(D\) is total dominating exactly when \((X,D)\) has independence number at most two. This is equivalent to the complementary graph \(F\) containing no triangle. Consequently, the stated complement correspondence is a bijection that preserves all and only the allowed moves.

**2. The ten labelled symmetry types.** Up to permutation of \(X\), triangle-free graphs with three through six edges have the following types. Entries give the number of labelled graphs, degree in the edge-toggle graph with the three-edge floor, and eccentricity in that graph. Disjoint unions are denoted \(\sqcup\); a broom is the five-vertex tree with degree sequence \((3,2,1,1,1)\).

| Edges in \(F\) | Type of \(F\) | Labelled states | Degree | Eccentricity |
| ---: | --- | ---: | ---: | ---: |
| 3 | \(K_{1,3}\sqcup K_1\) | 20 | 4 | 8 |
| 3 | \(P_3\sqcup K_2\) | 30 | 6 | 9 |
| 3 | \(P_4\sqcup K_1\) | 60 | 5 | 8 |
| 4 | \(K_{1,4}\) | 5 | 4 | 8 |
| 4 | \(C_4\sqcup K_1\) | 15 | 8 | 8 |
| 4 | broom | 60 | 6 | 9 |
| 4 | \(P_5\) | 60 | 7 | 9 |
| 5 | \(C_5\) | 12 | 5 | 10 |
| 5 | \(K_{2,3}\) with one edge deleted | 60 | 6 | 9 |
| 6 | \(K_{2,3}\) | 10 | 6 | 9 |

This table is exhaustive: it is obtained by checking the ten triangle masks among all \(2^{10}=1024\) edge bitmasks, then applying all \(5!=120\) label permutations. The orbit enumeration is reproduced, including every orbit's full breadth-first-search distance shells, in `verify_triangle_orbits.py`. In particular, the level counts are \((110,140,72,10)\), the degree counts are \(4:25,\ 5:72,\ 6:160,\ 7:60,\ 8:15\), and the counts of edges between consecutive levels are \((560,360,60)\). This proves the claimed vertex and edge totals.

**3. Exact distance certificate and its completeness.** Fix the lexicographic order of the ten edges \(01,02,03,04,12,13,14,23,24,34\), indexed by \(0,\ldots,9\). Encode a labelled graph by its edge bitmask \(b\in\{0,\ldots,1023\}\). For each of the ten triples \(abc\), let \(T_{abc}\) be the bitmask of its three edges. Define the finite state set
\[
\mathcal F=\bigl\{b:\ \operatorname{popcount}(b)\ge3,\ (b\mathbin{\&}T_{abc})\ne T_{abc}\text{ for all }abc\bigr\}.
\]
For \(s\in\mathcal F\), define \(R_0(s)=\{s\}\) and
\[
R_{j+1}(s)=R_j(s)\cup\bigl\{b\oplus2^i:\ b\in R_j(s),\ 0\le i<10,\ b\oplus2^i\in\mathcal F\bigr\}.
\]
By induction on \(j\), \(R_j(s)\) is **exactly** the set of states reachable from \(s\) within \(j\) moves. Hence the least \(j\) such that \(t\in R_j(s)\) is the actual shortest-path distance. The finite loops in the two included complete Python programs evaluate this recurrence, one starting from all \(332\) original Petersen total-dominating sets and the other from one representative of each of the ten \(S_5\)-orbits. The first constructs the original open-neighborhood condition directly; the second constructs only triangle-free graphs. Both independently obtain the full distance histogram stated above. The second also prints complete distance shells for each orbit. Thus no sampled or bounded-depth extrapolation is used.

These exhaustive exact evaluations yield connectivity, eccentricities \(8:100,9:220,10:12\), and therefore radius \(8\) and diameter \(10\). They also compare each computed distance with the exact Hamming lower bound \(\operatorname{popcount}(s\oplus t)\). Of the \(54{,}946\) unordered pairs, \(54{,}211\) meet that lower bound and exactly \(735\) require two additional steps; no pair has a larger deficit. All ten orbit distance shells establish that only the \(C_5\)-orbit is peripheral. There are exactly six pairs at distance ten, and each pair consists of the two complementary five-cycles on \(X\). For the \(C_5\)-orbit the Hamming defect is always zero, giving the stated geodesic property.

**4. Sharp threshold.** The complement transformation identifies inclusion-minimal total dominating sets with maximal triangle-free graphs on five labelled vertices. These consist of ten \(K_{2,3}\)'s (selected size four), twelve \(C_5\)'s (selected size five), and five \(K_{1,4}\)'s (selected size six). Thus the minimum total domination number is \(4\) and the maximum size of an inclusion-minimal total dominating set is \(6\). Exact component enumeration gives: at cap four, ten isolated states; at cap five, ten components isomorphic to \(K_{1,6}\) and twelve isolates; at cap six, one component of order \(217\) and five isolates; at cap seven, a connected graph of order \(332\). Any total dominating set larger than six has a smaller total dominating subset, so every state introduced above cap seven can reach an existing state by deletions. Hence the first cap for which all subsequent reconfiguration graphs are connected is exactly seven.

## Verification
Run `python3 verify_petersen_direct.py` and `python3 verify_triangle_orbits.py` with Python 3.10 or later; no third-party dependencies or data files are required. The first script tests all \(1024\) subsets of Petersen vertices against direct open neighborhoods, builds each cap-four-through-seven reconfiguration graph, and performs complete breadth-first search from all \(332\) cap-seven states. The second script independently tests triangle masks, constructs all \(120\) permutations of the five labels, and uses ten orbit-representative breadth-first searches with orbit-size weighting. They agree on every cardinality, component structure, distance shell consequence, eccentricity, Hamming defect, and diametral-pair classification. Both scripts were executed successfully on their actual embedded versions before acceptance.

## Relationship to prior work
Haas and Seyffarth introduced addition/deletion reconfiguration of **ordinary** dominating sets in their 2012 manuscript. Alikhani, Fatehi, and Mynhardt introduced the **total**-dominating analogue in their 2017 manuscript (journal publication 2019), proving general threshold bounds and studying paths, cycles, and realizability. Those general results do not give this Petersen-specific threshold or any of the above distances; in particular, the general bounds \(\Gamma_t\le d_0\le\min\{n-1,\Gamma_t+\gamma_t\}\) only restrict the present case to a wider interval. The published labelled triangle-free graph count for five vertices is \(388\), so the filtered state count \(388-(1+10+45)=332\) is already an immediate enumeration corollary. The proposed new content is the exact connected-threshold, orbit-wise metric geometry, six diametral pairs, and quantified geodesic defect.

## Limitations
This is a complete **finite** theorem for the Petersen graph and the specified one-vertex add/delete operation, not an asymptotic claim for all Kneser or generalized Petersen graphs. The finite bitmask search is exhaustive and proves the numeric conclusions only because every one of the \(1024\) possible configurations is checked and every reachable move is generated. Independent mathematical priority cannot be proved by database searches; an unindexed equivalent historical metric computation remains possible. No independent scholarly audit is asserted.

## References
1. R. Haas and K. Seyffarth, *The \(k\)-Dominating Graph*, arXiv:1209.5138, first publicly posted 2012-09-24, https://arxiv.org/abs/1209.5138.
2. S. Alikhani, D. Fatehi, and C. M. Mynhardt, *On \(k\)-Total Dominating Graphs*, arXiv:1711.04363, first posted 2017-11-12; *Australasian Journal of Combinatorics* 73(2) (2019), 313–333, https://ajc.maths.uq.edu.au/pdf/73/ajc_v73_p313.pdf.
3. OEIS A213434, *Number of labelled triangle-free simple graphs on \(n\) vertices*, https://oeis.org/A213434 (known five-vertex value \(388\)).
4. E. W. Weisstein, *Total Dominating Set*, MathWorld, https://mathworld.wolfram.com/TotalDominatingSet.html (definition and Petersen example).
