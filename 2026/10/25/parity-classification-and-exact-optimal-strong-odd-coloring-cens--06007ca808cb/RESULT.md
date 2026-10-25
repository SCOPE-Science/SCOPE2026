# Parity classification and exact optimal strong odd coloring census for fully subdivided complete bipartite graphs

## Finding
Let \(H_{p,q}=S(K_{p,q})\) arise by replacing every edge of \(K_{p,q}\) by a two-edge path, with \(p,q\ge1\). Its exact strong odd chromatic number is
\[
\chi_{\mathrm{so}}(H_{p,q})=\begin{cases}4,&p\equiv q\equiv0\pmod2,\\3,&\text{otherwise}.\end{cases}
\]
For the named palette \(\{0,1,2\}\), the number of strong odd colorings is
\[
N_{p,q}(3)=\begin{cases}
6,&p,q\text{ odd},\\
3\cdot2^{p-1},&p\text{ even},\ q\text{ odd},\\
3\cdot2^{q-1},&p\text{ odd},\ q\text{ even},\\
0,&p,q\text{ even}.
\end{cases}
\]
In addition, for every even integer \(q\ge2\), the number of optimally strong odd colorings of \(H_{2,q}\) using **four named colors** is exactly
\[
\boxed{N_{2,q}(4)=12\cdot4^q+6\cdot3^q-18\cdot2^q-6.}
\]
These latter graphs are unions of \(q\) internally disjoint length-four paths sharing two endpoints; the enumerator counts all assignments to their individually distinguished vertices, with no quotient by graph or color automorphisms.

## Assumptions and scope
All graphs are finite and simple. A coloring is *strong odd* when adjacent vertices have different colors and, for every vertex and every color present among its neighbors, the number of neighbors with that color is odd. Both parts of the underlying complete bipartite graph are nonempty. A named \(k\)-coloring is a map to the exact labeled palette \(\{0,\ldots,k-1\}\) and need not be surjective by definition; in the cases counted on an optimal palette surjectivity follows from optimality. We do not count arbitrary \(k\)-colorings for \(k>\chi_{\mathrm{so}}\).

Write original vertices as \(a_i\) and \(b_j\), and the unique subdivision vertex of \(a_ib_j\) as \(x_{ij}\). The neighbors of \(x_{ij}\) are exactly \(a_i,b_j\); hence a strong odd coloring forces their colors to differ. At an original vertex, the neighbors are its corresponding subdivision vertices.

## Proof
**1. Lower bound and the three-color rigidity.** Every subdivision vertex has two neighbors of different colors. As the subdivision vertex itself must have a third color, \(\chi_{\mathrm{so}}(H_{p,q})\ge3\). With exactly three colors, the original vertices use disjoint sets of colors on their two sides, since every \(a_i\) and \(b_j\) must differ. Once their colors have been specified, the color of each \(x_{ij}\) is the *unique* remaining color.

Fix a side-A original vertex colored \(\alpha\). For each color \(\beta\) appearing on side B, all \(x_{ij}\) whose B endpoint has color \(\beta\) receive the unique third color \(\gamma\) different from \(\alpha,\beta\). As there are only three colors, the map \(\beta\mapsto\gamma\) is injective. Therefore its neighborhood satisfies the strong odd condition if and only if **each nonempty color class on side B has odd size**. The symmetric statement holds for side A. These conditions are also sufficient for every original vertex, while every subdivision vertex has differently colored original neighbors and hence automatically satisfies the strong odd condition.

Each side requires at least one color, and the total number of different original colors is at most three. Thus the original color-class partitions are either \((1,1)\), \((2,1)\), or \((1,2)\). Splitting a side into two odd positive classes requires that side's cardinality to be even; a one-class side must have odd cardinality. Hence: if both sizes are odd, only \((1,1)\) occurs and exactly \(3\cdot2=6\) named colorings exist. If \(p\) is even and \(q\) odd, only \((2,1)\) occurs: choose the B singleton color in three ways and assign the other two named colors to side A with odd multiplicities in \(2^{p-1}\) ways. The reverse case is symmetric. If both sizes are even, no three-coloring exists. This proves the displayed three-color count and its zero/nonzero cases.

**2. Four-color construction for the even-even case.** Color every original A vertex by \(0\) and every original B vertex by \(1\). For each \((i,j)\), color \(x_{ij}\) by \(2\) when exactly one of \(i,j\) equals its part's distinguished index \(0\), and by \(3\) otherwise. In every row, color \(2\) occurs either once or \(q-1\) times; color \(3\) occurs the complementary odd number, because \(q\) is even. Likewise every column has counts \(1\) and \(p-1\), both odd. Properness and the degree-two condition are immediate. Thus four colors suffice, and the lower bound from step 1 makes the bound sharp. For the remaining parity cases, step 1 gave an explicit three-color construction.

**3. Exact optimal four-color count when the first part has size two.** Fix the colors \(a_0=\alpha\), \(a_1=\beta\) from the four named colors \(C=\{0,1,2,3\}\). For each page \(j\), write \((b_j,x_{0j},x_{1j})=(v,s,t)\). The independent page choices satisfy
\[
v\notin\{\alpha,\beta\},\quad s\notin\{\alpha,v\},\quad t\notin\{\beta,v\},\quad s\ne t.
\]
The final inequality is exactly the neighborhood condition at the degree-two vertex \(b_j\). There are six allowed triples per page whether \(\alpha=\beta\) or not; every triple also automatically satisfies the subdivision vertices' conditions. Pages are otherwise independent apart from the neighborhood parity constraints at the two hubs.

Each hub has \(q\) neighbors. Since \(q\) is even and only three colors can occur there (the hub's own color being excluded), a strong odd hub neighborhood must contain **exactly two colors with odd positive multiplicities**, and its third allowable color must be absent. This exclusion condition is essential; merely requiring a parity vector of weight two without excluding the third color would count invalid positive-even occurrences.

For each hub choose its absent color \(z_0\in C\setminus\{\alpha\}\) and \(z_1\in C\setminus\{\beta\}\), respectively. Define \(c_0\) as the numerically smaller of the two remaining allowed colors at hub zero, and \(c_1\) analogously. Let \(P_{\alpha,\beta}(z_0,z_1)\) be the page triples above with \(s\ne z_0\) and \(t\ne z_1\). For signs \(\epsilon,\eta\in\{+1,-1\}\), write
\[
\Lambda(z_0,z_1;\epsilon,\eta)=\sum_{(v,s,t)\in P_{\alpha,\beta}(z_0,z_1)}\epsilon^{[s=c_0]}\eta^{[t=c_1]}.
\]
Here brackets are indicator functions. Since \(q\) is even and the absent colors cannot appear, both retained colors at a given hub occur oddly precisely when the selected color \(c_i\) occurs oddly. The two independent oddness conditions give the exact character formula
\[
F_{\alpha,\beta}(q)=\frac14\sum_{z_0,z_1}\sum_{\epsilon,\eta\in\{\pm1\}}\epsilon\eta\,\Lambda(z_0,z_1;\epsilon,\eta)^q.
\]
The absent color of each valid coloring is unique, so there is no multiplicity from summing the nine absent-color choices.

Direct enumeration of the six possible page triples and nine absent-color pairs produces the following complete signed multiplicities for the values of \(\Lambda\). The entries give \(w(\lambda)=\sum\epsilon\eta\) over all combinations with that value; unspecified entries are zero.

| Hub colors | \(w(-2)\) | \(w(-1)\) | \(w(0)\) | \(w(1)\) | \(w(2)\) | \(w(3)\) | \(w(4)\) |
|---|---:|---:|---:|---:|---:|---:|---:|
| Equal | 3 | -2 | -6 | -4 | 3 | 6 | 0 |
| Distinct | -12 | 0 | 4 | 0 | 4 | 0 | 4 |

For every positive even \(q\), substituting the table into the character formula gives
\[
F_{\alpha,\alpha}(q)=\frac32(3^q+2^q-1),\qquad
F_{\alpha,\beta}(q)=4^q-2^{q+1}\quad(\alpha\ne\beta).
\]
There are exactly four ordered equal-color hub pairs and twelve ordered distinct-color hub pairs. Hence
\[
N_{2,q}(4)=4F_{\alpha,\alpha}(q)+12F_{\alpha,\beta}(q)
=12\cdot4^q+6\cdot3^q-18\cdot2^q-6,
\]
as asserted. The computation is an all-parameter finite-state/character argument, not an extrapolation from sample values.

## Verification
The standalone file `verify_so_incidence.py` checks the strong odd definition by enumerating all maps from the three named colors on ten small parameter pairs. It exhaustively enumerates all four-colorings of \(H_{2,2}\) and \(H_{2,4}\), finding \(168\) and \(3264\) and checking the monochromatic-original subcounts \(24\) and \(96\). `verify_theta_so.py` independently counts length-\(q\) page sequences by dynamic programming: it tracks both used-color support and parity masks to reject positive even multiplicities. For \(q=2,4,6,8\) the counts are respectively \(168,3264,52368,821184\), agreeing with the character sums and closed expression. The proof above covers all positive \(p,q\) and every even \(q\ge2\), beyond finite tested ranges.

## Relationship to prior work
Kwon and Park introduced the strong odd coloring parameter and established general bounds in *Strong odd coloring of sparse graphs* (arXiv:2401.11653; initially public 2024-01-22). Caro, Petruševski, Škrekovski and Tuza developed trees, planar cases and graph products in *On strong odd colorings of graphs* (arXiv:2410.02336; 2024-10-03). In particular their statement about \(K_{p,q}\) itself being strongly odd at most four-colorable concerns the **unsubdivided** graph and does not count the colorings here. A later study of the complete-graph subdivision \(S(K_n)\) (arXiv:2509.20763, Section 3.4) addresses another incidence graph: its original endpoints are adjacent in the unsubdivided complete graph, unlike the two original parts here. Their results do not imply the displayed parity law or the exponential exact census. A 2026 complexity study (arXiv:2610.01441) treats decision/parameterized complexity rather than an identified exact enumeration of this family. Graph-square coloring for theta graphs is also a different, stricter local condition. Published semantically related result records on crown-graph strong odd coloring and forced coloring of \(K_{p,q}\) concern different objects or coloring notions.

## Limitations
The closed four-color census is proved only when one underlying part has two vertices and the other has even size; a closed census for arbitrary even-even \(p,q\) is not established. No claim is made about \(k\)-colorings for higher palettes, or independent validation. Although inspected sources and indexed comparisons did not identify an equivalent result, incompletely indexed specialized graph-coloring literature could affect priority. In particular, independent research on multitheta graphs and subdivision parity colorings is a residual overlap risk.

## References
1. H. Kwon and B. Park, *Strong odd coloring of sparse graphs*, arXiv:2401.11653 (first public 2024-01-22), https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *On strong odd colorings of graphs*, arXiv:2410.02336 (first public 2024-10-03), https://arxiv.org/html/2410.02336v1.
3. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, *The odd independence number of graphs, I*, arXiv:2509.20763 (first public 2025-09-25), https://arxiv.org/abs/2509.20763.
4. D. Pradhan, V. Sharma and S. Verma, *On the Classical and Parameterized Complexity of Strong Odd Coloring*, arXiv:2610.01441 (first public 2026-10-01), https://arxiv.org/abs/2610.01441.
