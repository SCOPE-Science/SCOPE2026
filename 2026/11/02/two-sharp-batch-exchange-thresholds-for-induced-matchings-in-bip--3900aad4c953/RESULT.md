# Two sharp batch-exchange thresholds for induced matchings in bipartite subdivisions

## Finding
For integers \(m,n\ge 3\), let \(G_{m,n}\) be obtained from the complete bipartite graph \(K_{m,n}\) by subdividing every edge exactly once. The maximum induced-matching cardinality of \(G_{m,n}\) is \(k=m+n-2\), and it has exactly \(mn\) maximum induced matchings.

For \(0\le t\le k\), define \(\mathcal R_t(G_{m,n})\) to have those maximum induced matchings as vertices, with two **distinct** matchings adjacent when at most \(t\) edges of the first are deleted and replaced with the same number of edges to obtain the second (with both endpoints maximum induced matchings; no intermediate stages are required). Write \(a=\min\{m,n\}\), \(b=\max\{m,n\}\), and \(N=mn\). The entire threshold sequence is

\[
\mathcal R_t(G_{m,n})\cong
\begin{cases}
N K_1, & 0\le t<a,\\
a K_b, & a\le t<b,\\
K_m\mathbin{\square}K_n, & b\le t<k,\\
K_N, & t=k.
\end{cases}
\]

The middle interval is empty when \(m=n\). In particular, the **minimum simultaneous replacement budget for connectedness is exactly \(\max\{m,n\}\)**. The connected graph at this first threshold has diameter two, whereas at budget \(k\) it is complete. These sharp obstruction sizes grow without bound even within bipartite graphs of girth eight and average degree less than four.

## Assumptions and scope
The bipartite vertex classes of the unsubdivided graph are \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_n\}\). For each pair \((i,j)\), the subdividing vertex is \(s_{ij}\), and its two incident edges are \(a_i s_{ij}\) and \(b_j s_{ij}\). No further edges occur. An **induced matching** is a set of edges whose endpoints induce a disjoint union of isolated edges, with no additional edges among those endpoints.

An exchange of size \(q\) means replacing precisely \(q\) selected edges by \(q\) unselected edges in one simultaneous step; the permitted budget \(t\) means \(1\le q\le t\). It does not mean \(t\) successive single-edge exchanges. The result is for all labelled \(m,n\ge3\), not for graph subdivisions in general or for near-optimal matchings.

## Proof
**Step 1: bound and classify the optima.** Every selected edge touches exactly one original vertex, either \(a_i\) or \(b_j\); call these edges respectively \(A\)-type and \(B\)-type. Since a matching cannot use any original vertex twice, the number of \(A\)-type edges is at most \(m\), and that of \(B\)-type edges at most \(n\). If both types occur, then at least one original \(A\)-vertex and one original \(B\)-vertex are unused. Indeed, whenever \(b_j s_{ij}\) is selected, no edge touching \(a_i\) may be selected: the extra edge \(a_i s_{ij}\) would connect two endpoints of distinct matching edges. Symmetrically, a selected \(A\)-type edge \(a_i s_{ij}\) forbids selecting any edge touching \(b_j\). Consequently any mixed-type induced matching has at most \((m-1)+(n-1)=m+n-2\) edges. A one-type matching has at most \(\max\{m,n\}<m+n-2\) edges, using \(m,n\ge3\).

For any \((r,c)\in[m]\times[n]\), define
\[
M_{r,c}=\{a_i s_{ic}:i\ne r\}\ \cup\ \{b_j s_{rj}:j\ne c\}.
\]
These \(m+n-2\) edges are an induced matching: each selected \(A\)-type edge has its subdivision endpoint in column \(c\), whose opposite original endpoint \(b_c\) is unused; each selected \(B\)-type edge has its subdivision endpoint in row \(r\), whose opposite original endpoint \(a_r\) is unused. They have distinct subdivision and original endpoints, and there are no edges between subdivision vertices.

Conversely, a maximum induced matching must use \(m-1\) \(A\)-type and \(n-1\) \(B\)-type edges. Let \(a_r\) and \(b_c\) be the unique unused original vertices on the two sides. Every selected \(A\)-type edge must then end at some \(s_{i c}\), since its opposite original vertex must be unused among the \(B\)-vertices. Likewise each selected \(B\)-type edge must be \(b_j s_{rj}\). Therefore the matching is exactly \(M_{r,c}\), proving both the optimum size and the \(mn\)-element classification.

**Step 2: calculate exact exchange sizes.** Distinct maximum matchings \(M_{r,c}\) and \(M_{s,d}\) have \(k\) edges apiece. The minimum number of simultaneously replaced edges is \(q=k-|M_{r,c}\cap M_{s,d}|\). Directly from the displayed classification,
\[
q\big((r,c),(s,d)\big)=
\begin{cases}
0,&(r,c)=(s,d),\\
m,&r=s,\ c\ne d,\\
n,&r\ne s,\ c=d,\\
k,&r\ne s,\ c\ne d.
\end{cases}
\]
For example, fixing \(r\) and changing \(c\) leaves precisely the \(n-2\) common \(B\)-type edges whose columns avoid both \(c\) and \(d\), giving replacement cost \(k-(n-2)=m\). Fixing \(c\) gives cost \(n\) by symmetry. Changing both coordinates gives no common edge at all.

**Step 3: read off the graphs.** Below \(\min\{m,n\}\), no distinct states are adjacent. If \(m<n\), at budgets \(m\le t<n\), the only exchanges change \(c\) while keeping \(r\), giving \(m\) copies of \(K_n\); the case \(n<m\) is symmetric. At budgets \(\max\{m,n\}\le t<k\), any two states differing in exactly one coordinate are adjacent and no others are, which is exactly the Cartesian rook graph \(K_m\square K_n\). Its connectedness and diameter two follow by changing the two coordinates in succession; opposite-coordinate pairs are nonadjacent since their cost is \(k>t\). At \(t=k\), every distinct pair is adjacent. Each transition is exact, proving the claimed sharp thresholds and graph isomorphisms.

Finally, \(G_{m,n}\) is bipartite, its smallest cycle arises by subdividing a four-cycle of \(K_{m,n}\), hence has length eight, and its \(mn+m+n\) vertices and \(2mn\) edges give average degree \(4mn/(mn+m+n)<4\).

## Verification
Two standalone standard-library Python checkers are included. Run `python3 verify.py` and `python3 verify_alt.py` in the extracted directory.

`verify.py` independently constructs the subdivided graph, enumerates all size-\(k\) subsets of its edges, tests induced matching directly by endpoint adjacency, compares with the stated \(mn\) optimum configurations, and reconstructs all exchange components for every budget \(1\le t\le k\). It checks \((m,n)=(3,3),(3,4),(4,3),(3,5),(4,4)\).

`verify_alt.py` builds the **edge-compatibility graph** independently, enumerates its maximal cliques by Bron--Kerbosch recursion, extracts all maximum cliques, and checks the complete replacement-distance multiplicities for the same five parameter pairs. The checks corroborate the symbolic argument, which alone establishes the statements for infinitely many \((m,n)\).

## Relationship to prior work
The maximum-induced-matching problem is classical. Dabrowski, Demange and Lozin (2013, freely available author manuscript) investigate algorithmic complexity of maximum induced matching, including structured bipartite graphs and hypercubes; their Theorems 1--4 give tractability, hardness and a hypercube cardinality but not a sharp batch-exchange classification on the once-subdivided bicliques. The manuscript's introduction and principal results were inspected, including the search for subdivision and reconfiguration terminology.

A maximum induced matching of \(G\) is an independent set of the square of its line graph \(L(G)^2\), so the batch-exchange operation is a generalized token jump on optimum independent sets of \(L(G)^2\). Křišťan and Svoboda (2024) establish general reconfiguration rules for independent sets, vertex covers and dominating sets. Their full accessible introduction, definitions and reachability results do not compute the optimum-state exchange threshold or graph isomorphism for \(L(G_{m,n})^2\); their distance-restricted token movement is also distinct from our distance-unrestricted edge replacements. Neither the classical optimization result nor the universal reconfiguration rules imply the stated three structural transitions.

## Limitations
Only maximum cardinality induced matchings are considered; allowing nonmaximum intermediate matchings or imposing adjacency on individual moved edges changes the question. The family requires \(m,n\ge3\). Small-case computation is confirmatory, not a proof for arbitrary parameters. No assertion of publication priority or independent expert validation is made. An equivalent specific classification could exist in uncatalogued or inaccessible literature.

## References
1. K. K. Dabrowski, M. Demange and V. V. Lozin, *New results on maximum induced matchings in bipartite graphs and beyond*, Theoretical Computer Science **478** (2013), 33--40. DOI: `10.1016/j.tcs.2013.01.027`; accessible full author manuscript: https://www.konraddabrowski.co.uk/nrim-v7.pdf (preprint dated December 28, 2012; verified journal-public date March 25, 2013).
2. J. M. Křišťan and J. Svoboda, *Reconfiguration Using Generalized Token Jumping*, arXiv:2411.12582 (first public November 19, 2024), https://arxiv.org/abs/2411.12582.
