# Sharp discrete slope spectrum and grid formula for Dudley norms on finite graph metrics

## Finding
Let \(G=(V,E)\) be a finite connected simple graph with unit edge lengths, at least two vertices, and shortest-path diameter \(\Delta\). On the real space \(\mathbb R^V\) define
\[
 \|f\|_{BL}:=\max_{v\in V}|f(v)|+\max_{uv\in E}|f(u)-f(v)|.
\]
Every nonconstant extreme point of its closed unit ball has Lipschitz seminorm precisely \(2/(k+2)\), for some integer \(1\le k\le\Delta\), and all its values belong to the grid \(\{(-k+2j)/(k+2):0\le j\le k\}\). Conversely, for **each** integer \(1\le k\le\Delta\), at least one extreme point has this seminorm. The remaining extreme points with zero seminorm are exactly the two constant functions \(\pm1\).

Consequently, for any signed vector \(\mu\in\mathbb R^V\), the exact dual Dudley norm is
\[
 \|\mu\|_{BL}^*=\max\!\left\{\left|\sum_{v\in V}\mu_v\right|,\ \max_{1\le k\le\Delta}\frac1{k+2}\max_{z\in\mathcal Z_k(G)}\sum_{v\in V}\mu_v z_v\right\},
\]
where \(\mathcal Z_k(G)\) consists of functions \(z:V\to\{-k,-k+2,\ldots,k\}\) with \(|z_u-z_v|\le2\) on every edge. The inner maximum needs no absolute value because \(\mathcal Z_k(G)\) is symmetric.

For the path on \(n\ge2\) vertices, this formula has an exact dynamic program using \(O(n^3)\) arithmetic operations and \(O(n)\) memory. Fix \(k=1,\ldots,n-1\); write \(S_k=\{-k,-k+2,\ldots,k\}\) and initialize \(D_1(s)=\mu_1s\). Then recursively, for \(i=2,\ldots,n\),
\[
D_i(s)=\mu_i s+\max_{t\in S_k,\ |t-s|\le2}D_{i-1}(t).
\]
The inner grid maximum is \(\max_{s\in S_k}D_n(s)\); maximizing its quotient by \(k+2\) and the constant-function term gives the norm.

## Assumptions and scope
All scalars are real. Every graph is finite, undirected, simple, connected, nontrivial, and has unit-length edges. The Lipschitz seminorm is taken for the shortest-path metric, equivalently the largest edge difference. The norm here is the **sum** \(\|f\|_\infty+\operatorname{Lip}(f)\), rather than the alternative maximum of those two quantities. The mass vector may be signed and need not have zero total mass. A statement about all extreme points is made only for the restrictions above.

## Proof
**1. Lift the ball.** Set \(b=\operatorname{Lip}(f)\) and consider the polytope
\[
 Q=\{(f,b):0\le b\le1,\ |f_v|\le1-b\ (v\in V),\ |f_u-f_v|\le b\ (uv\in E)\}.
\]
Its projection onto \(f\) is exactly the \(BL\) unit ball. If a nonconstant \(f\) is extreme in that ball, it lies on its boundary, so \(\|f\|_\infty+\operatorname{Lip}(f)=1\) and \(0<b<1\). Its lift is unique: any feasible \(b'\) must satisfy \(\operatorname{Lip}(f)\le b'\le1-\|f\|_\infty\), and these endpoints coincide. If its lift were a proper convex combination of two points of \(Q\), the projected vectors would give a proper convex decomposition of \(f\), unless both equalled \(f\), in which case uniqueness of the lift still excludes a nontrivial decomposition. Thus its lift is a vertex of \(Q\).

**2. Tight components and anchors.** Fix a vertex \((f,b)\in Q\) with \(0<b<1\). Let \(H\) be the spanning subgraph consisting of edges where \(|f_u-f_v|=b\). Call a vertex an anchor if \(|f_v|=1-b\), and label its sign by the sign of \(f_v\). Every connected component of \(H\) contains an anchor: otherwise translating all values in that component by a common sufficiently small positive or negative amount leaves the active constraints unchanged and the inactive constraints strict, contradicting extremality.

At least one component of \(H\) has anchors of both signs. Otherwise every tight component has anchors of just one sign. In each component choose an anchor \(r\), whose sign is \(\sigma\), and write for every component vertex \(v\),
\[
 f_v=\sigma(1-b)+m_vb,
\]
where \(m_v\in\mathbb Z\) is the signed number of upward tight edges along any tight path from \(r\) to \(v\). This integer is path independent because the actual endpoint values agree and \(b>0\). If all anchors in the component have sign \(\sigma\), their integers are zero. Therefore the entire active system remains satisfied by setting \(b'=b+\varepsilon\), replacing each \(f_v\) by \(\sigma(1-b')+m_vb'\), and choosing either sign of sufficiently small \(\varepsilon\). All inactive inequalities remain strict by finiteness. This again contradicts being a vertex. Hence there is a tight-edge path from a positive anchor to a negative anchor within one component.

**3. Quantization and the diameter bound.** Along that tight path, each signed increment is \(\pm b\). The endpoint difference equals \(2(1-b)\), so \(2(1-b)=kb\) for some strictly positive integer \(k\). Hence \(b=2/(k+2)\). The shortest-path distance between the two anchors is at most \(\Delta\), and the Lipschitz inequality \(2(1-b)\le b\,d(u,v)\) implies \(k\le\Delta\). In every tight component a chosen anchor has value \(\pm(1-b)\); every other vertex differs from it by an integer multiple of \(b\). Thus every \(f_v\) lies in the claimed parity grid. The only zero-seminorm extreme points are the constant functions \(\pm1\), since the constants form a line segment and interior constants are not extreme in the whole ball.

**4. Every slope occurs.** For any \(1\le k\le\Delta\), choose \(u,w\in V\) with \(d(u,w)=k\), set \(a=k/(k+2)\) and \(b=2/(k+2)\), and define
\[
 f(x)=\max\{-a,\ a-b\,d(u,x)\}.
\]
Then \(\|f\|_\infty=a\), \(\operatorname{Lip}(f)=b\), and \((f,b)\in Q\). The tight geodesic from \(u\) to \(w\), together with anchors \(f(u)=a=1-b\) and \(f(w)=-a=-(1-b)\), fixes \(b\) under any two-sided feasible perturbation: the endpoint difference gives \((k+2)\,\delta b=0\). All vertices at distance at least \(k\) from \(u\) are negative anchors, so their variations vanish. Every vertex at distance less than \(k\) is connected to \(u\) by a geodesic of tight edges, so its variation also vanishes. Therefore \((f,b)\) is a vertex of \(Q\). It follows that \(f\) is a vertex of the projected ball: if \(f\) were a proper convex combination of two ball points, lift them using their individual Lipschitz seminorms; convexity and \(\|f\|_\infty+\operatorname{Lip}(f)=1\) force the lifts to average to \((f,b)\), contradicting its extremality.

**5. Dual formula and recursion.** A linear functional on the finite-dimensional polytope attains its maximum at an extreme point. Each nonconstant extreme point yields a scaled grid labeling from Steps 2–3. Conversely each grid labeling gives a feasible \(BL\) unit-ball function, since its supremum is at most \(k/(k+2)\) and its edge Lipschitz seminorm at most \(2/(k+2)\). Taking the maximum over all such labelings and the two constant extreme points therefore gives equality. On a path, each constraint couples only adjacent labels. The displayed dynamic program is the usual exact last-state maximization, proven by induction on the prefix length. For fixed \(k\), it takes \(O(n(k+1))\) comparisons and multiplications and \(O(k)\) memory (each state has at most three predecessors); summation over \(k\le n-1\) gives \(O(n^3)\) arithmetic operations and \(O(n)\) memory.

## Verification
The accompanying `CHECKER.py` uses only the Python standard library. Run `python3 CHECKER.py`. It enumerates lifted-polytope vertices using exact rational Gaussian elimination on seven small connected graphs, then verifies every resulting boundary vertex against the slope/grid classification. It independently compares the dual optimum over those vertices to the grid formula for 18 rational signed mass profiles per graph, and checks path dynamic programming against exhaustive grid labeling for 60 further rational signed profiles. The successful run reported 106 boundary vertices on seven graphs and 60 path comparisons. These are finite regression tests; the unrestricted theorem follows from the preceding proof rather than from enumeration.

## Relationship to prior work
Hille and Theewis (2023), arXiv:2305.08500v1, provide a general framework of norming and dense sets of extreme points for bounded-Lipschitz function spaces, including a finite-space discussion. Their framework motivates the sharper graph-specific arithmetic question. Hille and Theewis (2022), arXiv:2206.12234, give general finite-metric linear programming and polyhedral computations for Fortet–Mourier/Dudley distances. The present claim does **not** assert that general graph norms were previously uncomputable or that this path algorithm improves on every general-purpose LP implementation. It identifies instead the exact finite discrete slope spectrum of every unit-edge graph, realizes each possible slope, and supplies an explicit parity-grid norm formula and path recursion. Bredies, Chirinos Rodriguez and Naldi (2023), arXiv:2304.14039v1, analyze extreme points of a different Lipschitz seminorm ball. Jabłoński and Marciniak-Czochra (2013), arXiv:1304.3501v1, study an alternative flat/Fortet–Mourier normalization using a maximum constraint rather than the present sum norm.

## Limitations
The grid spectrum uses integer unit-edge graph distances and need not hold for arbitrary weighted metrics. General graph grid maximization may remain exponentially large; only paths have the stated polynomial dynamic program. The finite checker is not an infinite proof. An earlier equivalent graph-specialized theorem under alternative terminology remains possible, so independent mathematical and bibliographic assessment is appropriate.

## References
1. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500v1 (first public 2023-05-15).
2. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet-Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234 (2022).
3. K. Bredies, M. Chirinos Rodriguez, and E. Naldi, *On extreme points and representer theorems for the Lipschitz unit ball on finite metric spaces*, arXiv:2304.14039v1 (2023).
4. J. Jabłoński and M. Marciniak-Czochra, *Efficient algorithms computing distances between Radon measures on R*, arXiv:1304.3501v1 (2013).
