# Sharp bounded-error amplification of gradient reconstruction on every bicyclic graph

## Finding
Let \(G\) be any finite connected **simple** graph with exactly \(m\ge5\) edges and cycle-space dimension \(|E(G)|-|V(G)|+1=2\). Orient the edges arbitrarily and let \(B\) be the unweighted vertex–edge incidence matrix. The Euclidean edge-gradient projector is \(P_G=B^{\mathsf T}(BB^{\mathsf T})^\dagger B\). Its sharp amplification under coordinatewise bounded edge-data errors is \(\Lambda(G)=\|P_G\|_{\ell^\infty(E)\to\ell^\infty(E)}\).

The exact maximum over **all** such graphs with \(m\) edges is
\[
\boxed{\displaystyle
\max_G\Lambda(G)=M_m=\begin{cases}
\frac32,&m=5,\\[2pt]
\frac53,&m=6,\\[2pt]
\frac{3(m-1)}{m+3},&m\ge7\text{ odd},\\[2pt]
\frac{3m(m-2)}{m^2+2m-4},&m\ge8\text{ even}.
\end{cases}}
\]
Every maximum is attained, and its **unique graph isomorphism type** is the union of three internally vertex-disjoint paths between two branch vertices, with path lengths \((1,2,2)\) when \(m=5\), \((2,2,2)\) when \(m=6\), and
\[
\boxed{\left(1,\left\lfloor\frac{m-1}{2}\right\rfloor,\left\lceil\frac{m-1}{2}\right\rceil\right)}
\quad(m\ge7).
\]
In particular, \(M_m\) is strictly increasing, \(M_m>2\) if and only if \(m\ge10\), and
\[
\lim_{m\to\infty}M_m=3,\qquad M_m=3-\frac{12}{m}+O(m^{-2}).
\]
Each \(\ell^\infty\) matrix norm is attained exactly on sign-valued edge inputs, so the bounds apply to actual finite perturbations, not only infinitesimal ones.

## Assumptions and scope
All graphs are finite, connected, undirected, simple and have no edge weights; isolated vertices are excluded by connectedness. The edge-gradient projector is the Euclidean \(\ell^2\)-orthogonal projection onto the range of \(B^{\mathsf T}\), but the measured operator norm is the edgewise \(\ell^\infty\)-to-\(\ell^\infty\) norm. The result maximizes over graph isomorphism types at a fixed number of edges; neither arbitrary weights nor larger cycle rank are covered. Orientation affects coordinate signs but not the norm. The dagger is the Moore–Penrose pseudoinverse. The minimum possible edge count is five.

A **three-path theta graph** consists of two endpoints joined by exactly three internally vertex-disjoint simple paths. A two-cycle cactus core consists of two edge-disjoint cycles, which may meet at one vertex or be joined by bridges. Trees may be attached to either kind of core without changing its cycle rank.

## Proof
**1. Exact theta-graph row formula.** Direct all three theta paths from their shared initial vertex to the shared terminal vertex, with lengths \(a,b,c\ge1\), at most one equal to one (simplicity). Its Euclidean circulation subspace consists of flows having a constant value \(z_i\) on each path with \(z_1+z_2+z_3=0\). Put \(S=1/a+1/b+1/c\). Orthogonal projection \(Q=I-P_G\) onto the circulations has matrix entries, for edges on paths \(i,j\),
\[
Q_{e_i,e_j}=\frac{\mathbf1_{i=j}}{\ell_i}-\frac1{\ell_i\ell_j S},\qquad(\ell_1,\ell_2,\ell_3)=(a,b,c).
\]
Indeed minimizing squared distance over pathwise constant flows yields \(z_i=\bar y_i-(\sum_j\bar y_j)/(\ell_iS)\), where \(\bar y_i\) is the arithmetic mean along path \(i\). Within one path the entries of \(Q\) are positive, and between distinct paths they are negative. Consequently an edge in a path of length \(\ell\), with other path lengths \(u,v\), has absolute row sum in \(P_G\) exactly
\[
R(\ell;u,v)=2-\frac2\ell+\frac{\ell+2}{\ell^2(1/\ell+1/u+1/v)}
=2-\frac2\ell+\left(1+\frac2\ell\right)\frac1{1+\ell(1/u+1/v)}.
\]
The diagonal entry of \(P_G\) is positive, the other entries on its path are negative, and cross-path entries are positive. Thus the formula holds including \(\ell=1\). The theta norm is \(\max\{R(a;b,c),R(b;a,c),R(c;a,b)\}\).

**2. Optimize over theta graphs at fixed edge count.** Fix \(m=\ell+u+v\). For fixed \(\ell\), the row formula decreases strictly with \(1/u+1/v\), which is minimized when \(u,v\) are as balanced as possible. If \(\ell\ge2\), the real-variable arithmetic–geometric mean bound \(1/u+1/v\ge4/(m-\ell)\) implies
\[
R(\ell;u,v)\le\frac{5\ell+3m-8}{3\ell+m}.
\]
For \(m>6\) this expression is strictly decreasing in \(\ell\); hence every row in a path of length at least two obeys
\[
R(\ell;u,v)\le B_m=\frac{3m+2}{m+6}.
\]
If a path has length one, its row sum is \(3/S=3uv/(uv+u+v)\), and, for fixed \(u+v=m-1\), strict maximization of \(uv\) uniquely balances \(u,v\) up to interchange. This gives \(C_m=3(m-1)/(m+3)\) when \(m\) is odd and \(C_m=3m(m-2)/(m^2+2m-4)\) when \(m\) is even. For odd \(m\ge7\),
\[
C_m-B_m=\frac{4(m-6)}{(m+3)(m+6)}>0;
\]
for even \(m\ge8\),
\[
C_m-B_m=\frac{4(m^2-7m+2)}{(m+6)(m^2+2m-4)}>0.
\]
Thus **every** row not in a length-one path is strictly suboptimal, and every length-one row is maximized uniquely by the balanced remaining pair. Direct calculation in the only theta length partitions at \(m=5,6\) gives \((1,2,2)\mapsto3/2\), \((1,2,3)\mapsto18/11\), and \((2,2,2)\mapsto5/3\). This proves the theta classification.

**3. Classify all connected rank-two graphs.** Delete bridges and all hanging trees. Since the remaining cycle space has dimension two, either two independent simple cycles are edge-disjoint (cactus type, potentially connected by a bridge path), or two simple cycles share a path and their union is a three-path theta core. No other cycle-bearing block is possible at cycle rank two: an additional independent intersection pattern would contribute another independent cycle. The circulation projection vanishes on bridges, so \(P_G\) acts as the identity on bridge-edge coordinates and has no coupling between bridge edges and cycle-core edges. Therefore attached trees do not change the core projector norm whenever that norm exceeds one.

In the two-cycle cactus case the two cycle-indicator vectors have disjoint edge supports and are orthogonal. On a cycle of length \(r\), \(Q\) has signed entries of magnitude \(1/r\) and \(P=I-Q\) has absolute row sum \(2-2/r\). Hence any such graph with \(m\) edges has norm at most \(2-2/(m-3)\), because the other simple cycle uses at least three edges. This is strictly less than \(M_m\) for every \(m\ge6\): for \(m=6,7,8\) check \(4/3<5/3\), \(3/2<9/5\), \(8/5<36/19\); for \(m\ge9\), the cactus bound is strictly below two whereas \(M_m\ge2\).

For a theta core with fewer than \(m\) edges, the preceding fixed-size maximum is strictly smaller than \(M_m\), since the formulas show strict growth of \(M_m\): adding an edge to one of the two balanced longer paths increases its shortcut row, and the exceptional transition \(M_5<M_6<M_7\) is direct. Therefore bridges exclude equality. This proves both the global bound and uniqueness of the extremizing graph.

**4. Threshold and asymptotics.** Substituting \(m=9\) yields \(M_9=2\); the strictly increasing formula gives \(M_m>2\) precisely for \(m\ge10\). The displayed rational functions give \(M_m=3-12/m+O(m^{-2})\) for either parity. The \(\ell^\infty\) norm of any real finite matrix equals its largest absolute row sum and is realized by choosing each input coordinate as the sign of a maximizing row, establishing exact finite attainment.

## Verification
The self-contained `checker.py` uses SymPy and NetworkX. It independently constructs the vertex–edge incidence matrix of theta graphs, derives its rational nullspace, computes the Euclidean cut projector \(I-C(C^{\mathsf T}C)^{-1}C^{\mathsf T}\), and verifies its exact absolute row sums against the formula. It checks all ordered theta lengths with total edge count from five through twenty-three, exact optimizer uniqueness through seventeen edges, all connected bicyclic graphs in the NetworkX graph atlas with at most seven vertices, and rational growth/threshold inequalities through sixty edges. All 6,953 exact assertions passed. These are supplementary computations; the four analytic proof steps establish the unrestricted theorem.

Reproduce from the two-file package by executing `python checker.py` with the packages `sympy` and `networkx` installed. No network calls, external data, or randomized testing are required.

## Relationship to prior work
Jiang, Lim, Yao, and Ye (arXiv:0811.1067, first posted 2008-11-07) define least-squares gradient reconstruction and its circulation residual on a comparison graph. Kassel and Wu (arXiv:1312.2946) identify the transfer-current matrix with an edge-space Green-function projection. Dilworth, Kutzarova, and Ostrovskii (arXiv:2305.12582) study orthogonal and minimal cycle-space projections and obtain exact norms for highly symmetric graph families, notably hypercubes; the inspected results do not optimize the cut-projection \(\ell^\infty\) norm over every rank-two graph of fixed edge count. The new statement is an extremal theorem over graph topologies, not merely the standard projector identity.

Two related published investigations compare different invariants: a theorem on cactus transportation-space Schauder-basis coordinate suppressions (`SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd`) uses an \(\ell^1\) quotient norm rather than the Euclidean cut projector, and `SCOPE-exact-algebraic-gnarledness-of-three-path-theta-graphs--cceb12dd2a0d` computes chain-extension gnarledness rather than error-amplification row norms. Neither mathematical assertion entails the present classification or sharp constants.

## Limitations
Weights are exactly one, the graph is simple and connected, and its cycle rank is exactly two. No assertion is made for arbitrary cycle rank, multigraphs, directed optimization, edge-dependent measurement variances, or the optimum among all linear projections onto gradient flows. The result concerns the **specific Euclidean orthogonal projector** measured in a different norm. Earlier work supplies the cut/cycle decomposition and transfer-current identity; their use does not alone imply the fixed-edge extremizer. Historical originality may be limited by an older unindexed calculation of rank-two electrical-projection row norms or by a different formulation of the same extremal graph theorem.

## References
1. X. Jiang, L.-H. Lim, Y. Yao, and Y. Ye, *Statistical Ranking and Combinatorial Hodge Theory*, arXiv:0811.1067 (first public 2008-11-07), https://arxiv.org/abs/0811.1067.
2. A. Kassel and W. Wu, *Transfer Current and Pattern Fields in Spanning Trees*, arXiv:1312.2946 (first public 2013-12-10), https://arxiv.org/abs/1312.2946.
3. S. J. Dilworth, D. Kutzarova, and M. I. Ostrovskii, *Cycle Spaces: Invariant Projections and Applications to Transportation Cost*, arXiv:2305.12582 (first public 2023-05-21), https://arxiv.org/abs/2305.12582.
4. *Sharp coordinate-projection norms for edge bases of cactus transportation spaces*, public mathematical record, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-coordinate-projection-norms-for-edge-bases-of-cactus-trans--b98930fbc1cd/RESULT.md.
5. *Exact algebraic gnarledness of three-path theta graphs*, public mathematical record, https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-algebraic-gnarledness-of-three-path-theta-graphs--cceb12dd2a0d/RESULT.md.
