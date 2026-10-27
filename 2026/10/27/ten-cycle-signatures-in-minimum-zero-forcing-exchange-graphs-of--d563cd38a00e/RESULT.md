# Ten-cycle signatures in minimum zero-forcing exchange graphs of two-factor complements

## Finding
Let \(H\) be a finite, simple, spanning \(2\)-regular graph with every connected component an undirected cycle of length at least \(9\). Put \(N=|V(H)|\), let \(c_{10}\) be the number of ten-cycle components, and let \(G=\overline H\) be the graph complement. An ordinary zero-forcing set initially colors its members blue; a blue vertex with exactly one white neighbor may force it blue. The reconfiguration graph \(X(H)\) has one vertex for each **minimum-cardinality** zero-forcing set of \(G\), with an edge when the symmetric difference of two sets has size two.

For every such \(H\),
\[
Z(G)=N-3,\quad |V(X(H))|=N(N-4),\quad |E(X(H))|=N\left(\binom N2-11\right),\quad \operatorname{diam}X(H)=3.
\]
The exchange graph is connected. Its degree multiplicities, including zero multiplicities, are
\[
\begin{array}{c|c}
\text{degree}&\text{multiplicity}\\\hline
N&2N+10c_{10}\\
N+1&2N-20c_{10}\\
N+2&N(N-9)+10c_{10}\\
2N-6&N
\end{array}
\]
These four numerical degree values are distinct because \(N\ge9\). Hence \(c_{10}\) can be recovered from the degree spectrum alone as \((m_N-2N)/10\), where \(m_N\) is the number of degree-\(N\) vertices. For example, \(H=C_{20}\) and \(H=C_{10}\sqcup C_{10}\) give the same reconfiguration order \(320\), edges \(3580\), and diameter \(3\), but different degree distributions.

## Assumptions and scope
Every cycle length is at least \(9\), and all graphs are simple and undirected. Distances used below are distances within a component of \(H\); pairs in different components are treated as having infinite distance. Complementation exchanges the role of black and white only for identifying a configuration; the zero-forcing rule is applied to \(G\), not to \(H\). The result concerns the full token-jumping exchange graph of minimum sets, not fixed-size nonminimum forcing configurations.

## Proof
**1. Exact successful triples.** In \(G\), every vertex has degree \(N-3\). If fewer than \(N-3\) vertices are initially blue, then each blue vertex has at least two white neighbors, so no first force is possible. Consider therefore three initially white vertices \(W\). For a blue vertex \(v\), the number of its neighbors in \(G\) still white equals \(3-|N_H(v)\cap W|\). It can force at the first step precisely when its two \(H\)-neighbors are both in \(W\). Such a pair is a length-two chord across some cycle vertex \(v\), with \(v\notin W\).

Conversely, after any first force exactly two vertices \(x,y\) remain white. Because every component is a cycle of length at least nine, the vertices \(x,y\) have distinct open neighborhoods in \(H\), and there is a vertex \(v\in N_H(x)\setminus(N_H(y)\cup\{y\})\). This vertex is blue, nonadjacent to \(x\) in \(G\), and adjacent to \(y\) in \(G\), so forces \(y\). The final remaining white vertex has a blue neighbor in \(G\) and is forced. Thus the successful initial sets of minimum size are **exactly** the complements of triples \(W\) containing the two neighbors of an outside vertex of \(H\). In particular \(Z(G)=N-3\).

**2. Counting all successful triples.** Let \(D\) be the graph on \(V(H)\) joining each pair at distance two along a component of \(H\). Since the component lengths are at least nine, \(D\) has \(N\) edges, is \(2\)-regular and triangle-free. Every triple containing a \(D\)-edge is counted once by each of its \(D\)-edges; since there are \(N\) two-edge paths of \(D\), inclusion/exclusion gives \(N(N-2)-N=N(N-3)\) triples containing a \(D\)-edge. Exactly \(N\) of these have the form \(\{v^-,v,v^+\}\), in which the midpoint \(v\) is itself white; these triples have only one \(D\)-edge, and no valid blue midpoint. Deleting precisely those \(N\) failed triples leaves \(N(N-4)\) successful triples.

**3. The pair multiplicity and total edges.** For two distinct vertices \(a,b\) let \(g(a,b)\) be the number of successful triples containing them. A local inspection of their common and separate distance-two partners, excluding any white midpoint, gives
\[
\begin{array}{c|ccccc}
\operatorname{dist}_H(a,b)&1&2&3&4&\ge5\text{ or distinct components}\\\hline
 g(a,b)&2&N-3&4&3&4.
\end{array}
\]
There are exactly \(N\) unordered pairs at each of distances \(1,2,3,4\), because each cycle length is at least nine; all other \(\binom N2-4N\) pairs have the last type. The successful triples containing each fixed pair induce a clique \(K_{g(a,b)}\) in the token-jumping graph. Every exchange edge shares a unique two-element intersection and therefore belongs to exactly one such clique. Consequently
\[
|E(X)|=N\left[\binom{2}{2}+\binom{N-3}{2}+\binom{4}{2}+\binom{3}{2}\right]
+\left[\binom N2-4N\right]\binom42
=N\left(\binom N2-11\right).
\]
For a successful triple \(W\), its exchange degree is
\(\deg_X(W)=\sum_{\{a,b\}\subset W}(g(a,b)-1)\).

**4. All degree classes.** Each successful triple contains either one or two edges of \(D\), since \(D\) is triangle-free. Precisely \(N\) successful triples contain two such edges: the three consecutive vertices of a length-two path of \(D\), namely \(\{v^{-2},v,v^{+2}\}\). The pair distances inside are \(2,2,4\); their exchange degree equals \(2(N-4)+(3-1)=2N-6\).

Every other successful triple has one unique \(D\)-edge \(\{v^-,v^+\}\), and one remaining vertex \(x\notin\{v^{-3},v^-,v,v^+,v^{+3}\}\). Thus each of the \(N\) choices of \(v\) admits \(N-5\) such vertices \(x\). The pair \(\{v^-,v^+\}\) contributes \(N-4\) to degree. If the cycle of \(v\) has length different from ten, the two choices \(x=v^{\pm2}\) give degree \(N\), the two choices \(x=v^{\pm5}\) give degree \(N+1\), and the remaining \(N-9\) give degree \(N+2\). On a ten-cycle, the two expressions \(v^{+5}\) and \(v^{-5}\) coincide, and that unique antipodal choice has distance four from both endpoints of the core: it contributes degree \(N\), rather than two distinct degree-\(N+1\) triples. In a ten-cycle the per-center counts therefore become three, zero, and \(N-8\), respectively. Summing over all centers gives the four displayed degree multiplicities. This also establishes that all possible exchange edges and vertices have been classified.

**5. Connectivity and sharp diameter.** Each successful triple \(W\) contains an admissible \(D\)-edge \(A\) with its midpoint outside \(W\). Choose such a core \(A\) and analogously \(B\subseteq W'\). If \(A=B\), then \(W,W'\) are equal or adjacent. If the cores share one endpoint, the triple \(A\cup B\) contains both cores with their midpoints outside (the girth assumption excludes a conflicting midpoint). Thus both \(W\) and \(W'\) are adjacent to that intermediate triple, unless one is already equal to it.

If \(A\) and \(B\) are disjoint, choose \(a\in A\) not equal to the midpoint of \(B\), and \(b\in B\) not equal to the midpoint of \(A\). Then \(A\cup\{b\}\) is a successful triple containing \(A\), while \(B\cup\{a\}\) is a successful triple containing \(B\). These two intermediate triples share \(\{a,b\}\), so the path
\(W\to A\cup\{b\}\to B\cup\{a\}\to W'\)
uses at most three exchanges. In any component cycle, the two successful triples \(\{v,v^{+2},v^{+4}\}\) and \(\{v^+,v^{+3},v^{+5}\}\) are disjoint. Since a single exchange changes one member of a triple, moving between these disjoint triples requires at least three exchanges. Hence the graph is connected and its diameter is exactly three.

## Verification
The included `verify.py` constructs the complement graph explicitly and simulates zero forcing without using the distance-two characterization. It compares these genuine forced triples with the proposed structural condition, enumerates all optimum exchange edges, validates the complete degree multiplicities and connectivity, and exhaustively computes all-pair exchange distances through order \(20\). Tested component length lists include `[9]`, `[10]`, `[11]`, `[12]`, `[13]`, `[18]`, `[19]`, `[20]`, `[9,9]`, `[9,10]`, `[9,11]`, `[10,10]`, `[9,9,9]` and `[9,10,11]`. It prints `VERIFY_OK` after all assertions. Infinite-parameter assertions rest on the preceding proof, not finite extrapolation.

## Relationship to prior work
Eroh, Kang and Yi establish the known zero-forcing number of complements of cycles. An existing exact calculation for a *single* cycle complement additionally counts its minimum forcing sets; neither numerical result is claimed as new here. Geneson, Haas and Hogben introduce zero-forcing reconfiguration graphs. The present theorem treats complements of **arbitrary disjoint long-cycle unions**, and determines their optimum exchange graph's complete degree spectrum, a ten-cycle component detector, and sharp diameter. The count \(N(N-4)\) restricted to a single cycle is already covered by the earlier exact single-cycle calculation; the general component-dependent degree signature is the new object.

## Limitations
The cycle-girth hypothesis is essential to the stated pair-distance table; no extension to shorter components is claimed. The theorem concerns minimum ordinary zero forcing and token-jumping exchanges, not skew or positive-semidefinite variants. Earlier equivalent reconfiguration statements in unindexed literature may exist; the available comparisons do not certify exhaustive bibliographic novelty. No independent audit has been performed.

## References
1. L. Eroh, C. Kang, E. Yi, *On Zero Forcing Number of Graphs and Their Complements*, arXiv:1402.1962 (initial public version, 2014-02-09); especially their results on cycle complements.
2. J. Geneson, R. Haas, L. Hogben, *Reconfiguration graphs of zero forcing sets*, arXiv:2009.00220 (2020); definitions and general theory of minimum-set token-jumping graphs.
3. Earlier exact determination of the zero-forcing polynomial for a single cycle complement (2022 comparison record); its scalar and single-cycle enumeration results are treated as prior, not new contributions.
