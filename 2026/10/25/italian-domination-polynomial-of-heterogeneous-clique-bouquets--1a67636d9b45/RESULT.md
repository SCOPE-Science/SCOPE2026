# Italian domination polynomial of heterogeneous clique bouquets
## Finding
For integers \(r\ge2\) and \(m_1,\dots,m_r\ge2\), let \(W=K_1\vee(K_{m_1}\sqcup\cdots\sqcup K_{m_r})\), a graph with a single central vertex joined to each of \(r\) mutually anticomplete clique blades. Every Italian dominating function on \(W\) receives labels \(0,1,2\) and every zero vertex sees total neighbor-label weight at least \(2\). Write \(D_I(W;x)\) for the ordinary generating polynomial of all such functions, by total label weight.

Define \(A_m(x)=(1+x+x^2)^m\). Then
\[
\boxed{D_I(W;x)=x^2\prod_{i=1}^r A_{m_i}(x)+x\prod_{i=1}^r(A_{m_i}(x)-1)+\prod_{i=1}^r(A_{m_i}(x)-1-m_i x).}
\]
The coefficient of \(x^k\) is the exact number of Italian dominating functions of weight \(k\), for every integer \(k\). In particular, setting \(x=1\) gives
\[
\#\{\text{Italian dominating functions}\}=3^{\sum_i m_i}+\prod_i(3^{m_i}-1)+\prod_i(3^{m_i}-1-m_i).
\]
The constant and linear coefficients vanish and the quadratic coefficient equals one. Thus the minimum weight is \(2\), attained uniquely by assigning \(2\) to the center and \(0\) elsewhere. For uniform blades of size \(m\), the formula becomes
\[
D_I(K_1\vee rK_m;x)=x^2 A_m(x)^r+x(A_m(x)-1)^r+(A_m(x)-1-mx)^r.
\]
This includes all friendship graphs at \(m=2\).

## Assumptions and scope
The graphs are finite, undirected, simple, connected and have \(r\ge2\) nonempty clique blades, each of size at least \(2\). Denote the central vertex by \(c\) and the disjoint blades by \(B_i\) with \(|B_i|=m_i\). The graph has all edges within each blade and all edges between \(c\) and a blade vertex, and no edges between distinct blades.

For any function \(f:V(W)\to\{0,1,2\}\), write its weight \(w(f)=\sum_{v\in V(W)}f(v)\). It is Italian dominating if each vertex \(v\) with \(f(v)=0\) satisfies \(\sum_{u\in N(v)}f(u)\ge2\). This is also the Roman \(\{2\}\)-domination condition; the phrase Italian domination polynomial denotes the generating function over **all** feasible functions, not merely minimum-weight ones.

## Proof
Partition the admissible functions into three disjoint classes according to the central label \(f(c)\).

If \(f(c)=2\), every zero blade vertex is adjacent to the center of weight \(2\), so every assignment on the blades is feasible. The center is positive and needs no condition. An individual blade of order \(m_i\) contributes \((1+x+x^2)^{m_i}=A_{m_i}(x)\); multiplying over blades and including the center weight gives \(x^2\prod_i A_{m_i}(x)\).

If \(f(c)=1\), a zero vertex of blade \(B_i\) sees the center's \(1\) plus the weights of every other vertex of the same blade. Thus its defense condition is equivalent to having at least one positive vertex in that blade. If there are no zeros in the blade, this condition also holds automatically. Consequently *precisely* the all-zero assignment to that blade is forbidden; the blade polynomial is \(A_{m_i}(x)-1\). Conversely, if every blade has a positive vertex, all its zero vertices are defended, and the central vertex is positive. This gives \(x\prod_i(A_{m_i}(x)-1)\).

If \(f(c)=0\), a zero vertex in blade \(B_i\) sees exactly the labels of the other members of \(B_i\), so it is defended precisely if the entire blade has weight at least \(2\). For \(m_i\ge2\), any blade assignment of weight at most \(1\) contains a zero, so it fails; any assignment of blade weight at least \(2\) succeeds, since removing a zero vertex does not change the blade's total weight. The forbidden blade assignments consist of the single all-zero pattern and exactly \(m_i\) weight-one patterns. Hence the blade polynomial is \(A_{m_i}(x)-1-m_i x\). Since every blade has weight at least \(2\) and \(r\ge2\), the zero central vertex automatically sees total weight at least \(2\). All blade choices are independent and contribute \(\prod_i(A_{m_i}(x)-1-m_i x)\).

These are all possible central labels; their contributions are disjoint and exhaust the valid functions, proving the displayed polynomial without approximation. At \(x=1\), substitute \(A_m(1)=3^m\) for the exact total. The first summand has unique minimum degree \(2\), the second minimum degree at least \(r+1\ge3\), and the third minimum degree at least \(2r\ge4\), so the weight-two function is unique. The uniform-blade specialization follows by identical factors.

## Verification
The included `verify.py` is standalone Python. It constructs adjacency for each clique bouquet and exhaustively enumerates all assignments in \(\{0,1,2\}^{V(W)}\), checks the literal neighborhood condition for every zero vertex, and counts valid functions by weight. It independently computes the proposed polynomial by integer-coefficient convolution. It compares every coefficient for \(112\) graph profiles with between \(2\) and \(4\) blades, each of order \(1\), \(2\), or \(3\), and total blade order at most \(10\); this includes graphs in the theorem's scope and extra boundary cases with one-vertex blades. The test enumerates \(3{,}402{,}756\) labeled assignments and returns `VERIFY_OK`. For the single-vertex blades in these additional tests, the program correctly permits their weight-one pattern when the center is zero; the stated theorem itself only uses blade orders at least \(2\).

For example, the graph with two blades of size \(2\) has coefficients \(0,0,1,8,31,45,45,30,15,5,1\), in increasing weight order, by both independent procedures. The computations are finite corroboration, not a proof for arbitrary \(r\) or \(m_i\).

## Relationship to prior work
Shao and Zhao (2026) define the all-weight Italian domination polynomial and study its coefficients and algorithms on paths, trees, and cycles. Their first publicly accessible preprint appeared on September 9, 2026; the paper does not provide an all-weight formula for clique bouquets, which contain arbitrarily many cycles. Fernández and Leoni (2025) analyze Roman \(\{2\}\)-domination via graph joins, unions and modular decomposition, giving algorithms for the *minimum* weight, not complete weight enumerators. A separately published result gives an all-function Roman \(\{2\}\)-domination polynomial for complete multipartite graphs; its graph hypothesis does not cover clique bouquets with at least two nonsingleton blades, since such bouquets contain within-blade edges and no between-blade edges. Another publicly available exact polynomial for generalized windmills enumerates dissociation *vertex sets*, a different object with a different feasibility predicate. These prior results do not imply the present all-weight formula.

## Limitations
This statement concerns standard (non-perfect, non-total, non-secure) Italian domination on a single-hub union of cliques, with every blade of order at least \(2\). It neither claims a new minimum-weight Italian domination number nor classifies arbitrary block graphs or generalized multi-hub windmills. Literature searches cannot rule out unindexed equivalent formulas. No independent mathematical audit has been performed.

## References
1. P. Shao and C. Zhao, “Counting Weight-k Italian Dominating Sets on Trees and Cycles,” arXiv:2610.00108v1 (first public September 9, 2026), https://arxiv.org/abs/2610.00108.
2. L. Fernández and V. Leoni, “Roman {2}-domination on Graphs with ‘few’ 4-paths,” arXiv:2511.17369v2 (2025), https://arxiv.org/abs/2511.17369.
3. M. Chellali, T. W. Haynes, S. T. Hedetniemi, and A. A. McRae, “Roman {2}-domination,” *Discrete Applied Mathematics* 204 (2016), 22–28, https://doi.org/10.1016/j.dam.2015.11.013.
4. “Weight enumerator of all Roman {2}-dominating functions on complete multipartite graphs,” publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-weight-enumerator-of-all-roman-2-dominating-functions-on-complet--4a62f97e627e.
5. “Dissociation polynomial and all maximal dissociation sets of generalized windmills,” publicly available mathematical research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-dissociation-polynomial-and-all-maximal-dissociation-sets-of-gen--2c55298c97bc.
