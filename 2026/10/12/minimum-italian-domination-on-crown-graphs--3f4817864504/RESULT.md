# Minimum Italian domination on crown graphs
## Finding
Let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph for \(n\ge2\), with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_i\) is the deleted matching edge. Then
\[
\gamma_I(\operatorname{Cr}_n)=
\begin{cases}
3,&n=3,\\
4,&n=2\text{ or }n\ge4.
\end{cases}
\]
Moreover, if \(m_I(G)\) denotes the number of minimum-weight Italian dominating functions on \(G\), then
\[
m_I(\operatorname{Cr}_n)=
\begin{cases}
9,&n=2,\\
2,&n=3,\\
12,&n=4,\\
\binom{n+1}{2},&n\ge5.
\end{cases}
\]
For \(n\ge5\), every minimum function is of exactly one of two types: choose one deleted matching pair and assign \(2\) to both endpoints, or choose two deleted matching pairs and assign \(1\) to all four endpoints. For \(n=4\), these ten functions remain and there are two additional functions assigning \(1\) to all vertices of exactly one shore. For \(n=3\), the two minimum functions assign \(1\) to all vertices of exactly one shore. For \(n=2\), \(\operatorname{Cr}_2\) is two disjoint edges and each component independently has the three minimum patterns \((2,0)\), \((0,2)\), and \((1,1)\).

## Assumptions and scope
An Italian dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that every vertex \(v\) with \(f(v)=0\) satisfies
\[
\sum_{u\in N(v)} f(u)\ge2.
\]
Its weight is \(\sum_{v\in V(G)}f(v)\), and \(\gamma_I(G)\) is the minimum weight. The count \(m_I(G)\) counts functions, not supports and not equivalence classes under automorphisms. The theorem concerns crown graphs only.

## Proof
Write
\[
X=\sum_{i=1}^n f(a_i),\qquad Y=\sum_{i=1}^n f(b_i).
\]
Because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), and symmetrically for \(b_i\), the Italian condition is equivalent to the two indexed implications
\[
f(a_i)=0\Longrightarrow Y-f(b_i)\ge2,\qquad
f(b_i)=0\Longrightarrow X-f(a_i)\ge2.
\]

First suppose \(n\ge4\). A function of weight at most \(3\) cannot exist. If both shore totals are positive, one of \(X,Y\) is at most \(1\); the opposite shore necessarily contains a zero, whose available neighboring weight is then at most \(1\). If one shore total is zero, every vertex of the other shore must be positive, requiring weight at least \(n\ge4\). Hence \(\gamma_I(\operatorname{Cr}_n)\ge4\). Weight \(4\) is attained by assigning \(2\) to \(a_i,b_i\) for any fixed \(i\), so equality holds.

Now classify all weight-\(4\) functions for \(n\ge4\). The possible ordered shore totals are \((0,4),(1,3),(2,2),(3,1),(4,0)\). The cases \((1,3)\) and \((3,1)\) are impossible: the shore of total \(3\) has a zero when \(n\ge4\), and that zero sees at most total weight \(1\) across the cut. A zero shore is possible only when every vertex on the opposite shore is positive, so \((0,4)\) and \((4,0)\) occur exactly when \(n=4\), producing the two all-one shore functions.

It remains to classify \((X,Y)=(2,2)\). If \(f(a_i)=0\), then \(2-f(b_i)\ge2\), so \(f(b_i)=0\); the symmetric implication gives the converse. Thus the zero indices on the two shores coincide. A shore of total \(2\) is either one label \(2\), or two labels \(1\). Equal zero sets force the same type and the same support indices on both shores. Therefore there are \(n\) matched \(2,2\) functions and \(\binom n2\) four-one functions, for a total of
\[
n+\binom n2=\binom{n+1}{2}.
\]
This proves the \(n\ge5\) count and gives ten of the twelve functions at \(n=4\).

For \(n=3\), weight \(2\) is impossible by the same indexed inequalities, while assigning \(1\) to all vertices of either shore gives weight \(3\). If a weight-\(3\) function has both shore totals positive, one shore has total at most \(1\), and the other shore has a zero, contradicting the condition at that zero. Hence one shore total is zero; then every vertex on the other shore must be positive, forcing the all-one pattern. Thus there are exactly two minimum functions.

For \(n=2\), \(\operatorname{Cr}_2\) is the disjoint union of two copies of \(K_2\). Each \(K_2\) has minimum Italian weight \(2\) with exactly three functions, namely \((2,0)\), \((0,2)\), and \((1,1)\). Additivity across components gives minimum weight \(4\) and \(3^2=9\) minimum functions.

## Verification
A standalone exhaustive checker is included as `verify_crown_italian.py`. It enumerates every \(\{0,1,2\}\)-labeling for \(2\le n\le6\), tests the Italian condition directly from the crown adjacency relation, and verifies both the claimed minimum weight and the claimed number of minimum functions. The finite computation is only a stress test; the universal theorem is proved analytically above.

Replay output:
`ALL CHECKS PASSED; n_range=2..6; exhaustive_labelings=597861; minima=(2:4/9,3:3/2,4:4/12,5:4/15,6:4/21)`

## Relationship to prior work
Roman \(\{2\}\)-domination, now also called Italian domination, was introduced by Chellali, Haynes, Hedetniemi, and McRae. Shao and Zhao recently introduced the Italian domination polynomial and the systematic counting of weight-\(k\) Italian dominating functions; their 2026 paper treats paths, trees, and cycles, with star tables as tree examples. Its full text does not treat crown graphs or complete bipartite graphs.

The closest database results found for the present crown-graph statement concern restrained domination on crown graphs, ordinary Roman domination on complete multipartite graphs, and Roman \(\{2\}\)-enumeration on complete multipartite graphs. None implies the crown-graph result because \(\operatorname{Cr}_n\) is obtained by deleting a perfect matching and is not complete multipartite for \(n\ge3\). A 2019 paper by Klostermeyer and MacGillivray studies Italian domination for several graph classes and is a plausible older source; its publisher abstract and indexed text were inspected, but a complete full-text comparison was unavailable from the accessible material, so an unindexed equivalent crown-graph formula remains a residual literature risk.

## Limitations
The result determines only the minimum weight and the number and structure of minimum-weight functions; it does not give the full Italian domination polynomial of \(\operatorname{Cr}_n\). The originality assessment is literature-search based rather than a proof of global uniqueness, and the inaccessible full text noted above leaves a specific residual risk.

## References
1. P. Shao and C. Zhao, *Counting Weight-\(k\) Italian Dominating Sets on Trees and Cycles*, arXiv:2610.00108v1, 2026.
2. M. Chellali, T. W. Haynes, S. T. Hedetniemi, and A. A. McRae, *Roman \(\{2\}\)-Domination*, Discrete Applied Mathematics 204 (2016), 22–28, DOI: 10.1016/j.dam.2015.11.013.
3. W. F. Klostermeyer and G. MacGillivray, *Roman, Italian, and 2-Domination*, Journal of Combinatorial Mathematics and Combinatorial Computing 108 (2019), 125–146.
4. M. Chellali, N. Jafari Rad, S. M. Sheikholeslami, and L. Volkmann, *Survey on Roman \(\{2\}\)-Domination*, Mathematics 12 (2024), 2771, DOI: 10.3390/math12172771.
