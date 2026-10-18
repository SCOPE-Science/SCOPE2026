# The zero-forcing reconfiguration graph of a clique–path join is a barbell

## Finding
Let \(s\ge2\), \(n\ge4\), and let \(G_{s,n}=K_s\vee P_n\) be the join of a complete graph on \(U=\{u_1,\ldots,u_s\}\) and the path \(v_1v_2\cdots v_n\). Let \(\mathscr Z(G)\) be the graph whose vertices are the *minimum ordinary zero-forcing sets* of \(G\), adjacent when one selected vertex can be exchanged for one unselected vertex.

Then \(Z(G_{s,n})=s+1\), and **all** minimum sets are exactly
\[
\begin{aligned}
 A_L&=U\cup\{v_1\}, & A_R&=U\cup\{v_n\},\\
 B_{L,u}&=(U\setminus\{u\})\cup\{v_1,v_2\},
 & B_{R,u}&=(U\setminus\{u\})\cup\{v_{n-1},v_n\},
 \quad u\in U.
\end{aligned}
\]
In particular, \(\mathscr Z(G_{s,n})\) is **two cliques of order \(s+1\) joined by exactly one bridge**: the left clique consists of \(A_L\) and the \(s\) sets \(B_{L,u}\); the right clique consists of \(A_R\) and the \(s\) sets \(B_{R,u}\); the only edge between them is \(A_LA_R\). Thus the reconfiguration graph has \(2s+2\) vertices, \(s(s+1)+1\) edges, diameter \(3\), and a unique bridge, independently of \(n\ge4\).

## Assumptions and scope
Graphs are finite, undirected, and simple. The join adds every edge between the two disjoint vertex sets. A blue vertex with exactly one white neighbor can color that neighbor blue. A zero-forcing set is an initial blue set that eventually colors the whole graph by this rule; \(Z(G)\) is the minimum possible initial size. The *token-jumping* adjacency rule changes exactly one member of a minimum set, so its symmetric difference with the other minimum set has size two. The theorem assumes integers \(s\ge2\) and \(n\ge4\); it makes no claim for shorter paths or other joins.

## Proof
**Universal-clique obstruction.** Every universal vertex \(u\in U\) is adjacent to every other vertex. If two distinct universal vertices start white, every blue vertex is adjacent to both white vertices. No first forcing step is then possible. Thus any zero-forcing set initially contains at least \(s-1\) of the \(s\) universal vertices.

**Minimum cardinality.** No set of at most \(s\) vertices can force the graph. Such a set with \(s\) initially blue universal vertices has no blue path vertex, and each blue universal vertex has \(n\ge4\) white neighbors. A set with \(s-1\) blue universal vertices and at most one blue path vertex also has no first force: each blue universal has the remaining white universal and at least \(n-1\ge3\) white path neighbors; the possible blue path vertex sees the white universal and at least one white path neighbor. Cases with two or more white universal vertices were already excluded. Therefore \(Z(G_{s,n})\ge s+1\). Conversely \(A_L\) forces along the path from \(v_1\) to \(v_n\), since the universal clique is blue; hence \(Z(G_{s,n})=s+1\).

**Complete classification at cardinality \(s+1\).** Such a set contains either all \(s\) universal vertices and one path vertex, or exactly \(s-1\) universal vertices and two path vertices. In the first case, a single internal blue path vertex \(v_i\), \(1<i<n\), has two white path neighbors; each blue universal has \(n-1\ge3\) white path neighbors. Thus only the two endpoint sets \(A_L,A_R\) force.

In the second case, let \(u\) be the one white universal vertex and let \(v_i,v_j\) be the two initially blue path vertices. Each blue universal sees \(u\) and \(n-2\ge2\) white path vertices. Every blue path vertex sees \(u\), so it cannot force another path vertex before \(u\) turns blue. The first force must therefore color \(u\), performed by a blue path vertex with all its path neighbors blue. With only two blue path vertices, an internal path vertex has two path neighbors and cannot satisfy this; a path endpoint can satisfy it exactly when its sole path neighbor is the other blue path vertex. Hence the selected pair must be \(\{v_1,v_2\}\) or \(\{v_{n-1},v_n\}\). Each such endpoint forces \(u\) immediately, after which the initial adjacent pair propagates along the path. This proves precisely the displayed list and shows no other minimum sets exist.

**Adjacency.** Two distinct left-side sets \(B_{L,u},B_{L,w}\) differ only in which universal vertex is omitted, and hence are adjacent. Each \(B_{L,u}\) differs from \(A_L\) by exchanging \(u\) for \(v_2\). Thus the \(s+1\) left-side sets form a complete graph. The right-side proof is identical. The two endpoint sets \(A_L,A_R\) are adjacent by exchanging \(v_1\) for \(v_n\). No \(B_{L,u}\) can be adjacent to a right-side set: for \(n\ge4\), its two path vertices \(v_1,v_2\) are disjoint from \(v_{n-1},v_n\), and comparison with \(A_R\) also changes at least two selected vertices. Likewise, \(A_L\) is not adjacent to any \(B_{R,u}\). Hence \(A_LA_R\) is the unique cross-edge. Since \(s\ge2\), each clique has at least three vertices; all its edges lie on triangles, whereas the cross-edge is a bridge. The vertex and edge counts and diameter now follow. \(\square\)

## Verification
The standalone C++17 file `check.cpp` constructs \(K_s\vee P_n\) directly, independently applies the color-change rule to every initial set of cardinality at most \(s+1\), compares all minimum sets against the classification, and checks the complete two-clique-plus-bridge adjacency structure. It covers every \(1\le s\le6\), \(4\le n\le12\), including the known one-universal-vertex boundary as a sanity check. It tested 261,879 initial sets across 54 graph instances, found 486 minimum sets, and examined 1,062 resulting reconfiguration edges. The recorded output is in `verification_output.txt`. These computations corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work
Geneson, Haas and Hogben (arXiv:2009.00220v1, 2020) introduced the token-jumping zero-forcing graph and classified certain complete, path, cycle, disconnected, and forest cases. Their directly inspected Sections 2–4 do not give the clique–path-join family or the present barbell realization.

The published *Zero forcing polynomial of fan graphs* treats \(K_1\vee P_n\) and identifies the four minimum forcing sets when \(n\ge3\); this is the \(s=1\) boundary of the construction, whose reconfiguration graph is a four-vertex path. It does not cover \(s\ge2\), where two arbitrarily large complete subgraphs joined by a unique bridge arise. The distinct published *Zero forcing polynomial of bridge barbells* concerns zero-forcing sets **of a barbell as the base graph**, not the zero-forcing **reconfiguration graph** of \(K_s\vee P_n\). The two objects should not be conflated.

Boyer et al. (arXiv:1801.08910v1, 2018) introduced zero-forcing set enumeration, and Menon and Singh (arXiv:2405.01423v1, 2024, especially §3.2) gave coefficientwise bounds under adding a universal vertex. Neither result describes these minimum-set swaps or implies their unique-bridge structure. The contribution is the all-parameter inverse-reconfiguration realization and complete minimum-set structure, not a claim of a new forcing rule or of the known \(s=1\) case.

## Limitations
Only ordinary zero forcing with token-jumping swaps on \(K_s\vee P_n\) for \(s\ge2,n\ge4\) is covered. There is no statement about token sliding, positive-semidefinite or skew forcing, or arbitrary clique joins with other graphs. The theorem provides a realization of equal-sided barbell reconfiguration graphs; it does not classify all possible base graphs realizing them. Unindexed equivalent or stronger statements in the literature cannot be excluded by the searches performed.

## References
1. J. Geneson, R. Haas, L. Hogben, “Reconfiguration graphs of zero forcing sets,” arXiv:2009.00220v1 (1 September 2020), subsequently *Discrete Applied Mathematics* 329 (2023), 126–139. https://arxiv.org/abs/2009.00220
2. K. Boyer et al., “The zero forcing polynomial of a graph,” arXiv:1801.08910v1 (26 January 2018), subsequently *Discrete Applied Mathematics* 258 (2019), 35–48. https://arxiv.org/abs/1801.08910
3. K. Menon, A. Singh, “Exploring the Influence of Graph Operations on Zero Forcing Sets,” arXiv:2405.01423v1 (2 May 2024). https://arxiv.org/html/2405.01423v1
4. “Zero forcing polynomial of fan graphs,” publicly available scientific result, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-fan-graphs--f3b2c94da283/RESULT.md
5. “Zero forcing polynomial of bridge barbells,” publicly available scientific result, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-zero-forcing-polynomial-of-bridge-barbells--5431b532d7f2/RESULT.md
