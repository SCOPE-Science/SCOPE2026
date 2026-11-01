# Cut-degree census and maximum-cut thresholds for period-two chip-firing

## Finding
Let \(G=(V,E)\) be any finite connected simple graph with \(n=|V|\ge2\) vertices and \(m=|E|\). In synchronous degree-threshold parallel chip-firing, a vertex fires one chip to each neighbor if it currently holds at least its degree. The total number of chips is conserved.

For an edge cut \(S=\delta(U)\), let \(c_v(S)\) be the number of edges of \(S\) incident to \(v\), and define \([r]_z=1+z+\cdots+z^{r-1}\) for integers \(r\ge1\), with \([0]_z=0\). Let \(\mathcal C(G)\) be the set of distinct edge cuts, counting the cuts of \(U\) and its complement once. Define \(P_G(z)\) so that the coefficient of \(z^s\) counts *distinct primitive two-cycle orbits* whose conserved chip total is \(s\).

Then the exact, finite energy-resolved census is
\[
\boxed{P_G(z)=\sum_{S\in\mathcal C(G)}z^{2m-|S|}\prod_{v\in V}[c_v(S)]_z.}
\]
Writing \(q=\operatorname{MaxCut}(G)\) for the maximum cut size and \(M(G)\) for the number of distinct maximum edge cuts, the smallest and largest conserved totals supporting a primitive two-cycle are precisely
\[
\boxed{s_{\min}=2m-q,\qquad s_{\max}=2m+q-n,}
\]
and each extreme energy supports exactly \(M(G)\) different primitive two-cycle orbits. Moreover,
\[
\boxed{P_G(z)=z^{4m-n}P_G(z^{-1}).}
\]
In particular, deciding whether a connected graph supports a primitive two-cycle with at most a given number of chips is NP-complete.

For every tree \(T\), \(P_T(1)\) is a degree-product edge-cover sum computable using \(O(n)\) arithmetic operations. For the labelled path \(P_n\), \(n\ge2\), the exact number of distinct primitive two-cycles is the Pell number
\[
\boxed{P_{P_n}(1)=\frac{(1+\sqrt2)^{n-1}-(1-\sqrt2)^{n-1}}{2\sqrt2}.}
\]
These are components of one cut-enumerator theorem, not separate experimental claims.

## Assumptions and scope
Each vertex \(v\) has nonnegative integer chip count \(x_v\) and degree \(d_v\). The synchronous update is
\[
F_G(x)_v=x_v-d_v\mathbf1_{\{x_v\ge d_v\}}+\sum_{u\sim v}\mathbf1_{\{x_u\ge d_u\}}.
\]
No sinks, loops, multiple edges, stochastic choices, or asynchronous updates are used. The graph is finite and connected with at least one edge. A primitive two-cycle is an unordered pair \(\{x,F_G(x)\}\) with \(F_G^2(x)=x\ne F_G(x)\). A cut is an edge *set*, not an oriented bipartition. The polynomial does **not** enumerate fixed points, transients, or cycles of other lengths.

## Proof
**Equal two-step firing counts.** Let \(f_v\in\{0,1\}\) indicate whether \(v\) fires at the first step, and let \(g_v\) indicate firing at the second. From the update equation,
\[
F_G^2(x)-x=-L_G(f+g),
\]
where \(L_G\) is the ordinary graph Laplacian. For a connected graph, the kernel of \(L_G\) over the real numbers consists of constant vectors. Thus if \(F_G^2(x)=x\), then \(f+g\) is identically \(0\), \(1\), or \(2\). If it is \(0\), nobody fires and \(x\) is fixed; if it is \(2\), everybody fires and \(x\) is fixed. Every primitive two-cycle therefore has \(g_v=1-f_v\) at every vertex.

**Exact interval for one firing pattern.** Let \(S\) be the cut between first-step firing and nonfiring vertices. At vertex \(v\), exactly \(c_v(S)\) neighbors have the opposite first-step firing status. If \(f_v=1\), the next chip count is \(x_v-c_v(S)\); for the next status to be nonfiring, the necessary and sufficient interval is
\[
d_v\le x_v\le d_v+c_v(S)-1.
\]
If \(f_v=0\), the next chip count is \(x_v+c_v(S)\); for the next status to be firing, the necessary and sufficient interval is
\[
d_v-c_v(S)\le x_v\le d_v-1.
\]
There are exactly \(c_v(S)\) independently selectable counts in either case, and zero choices when \(c_v(S)=0\). Conversely these intervals ensure that all firing statuses reverse; since each vertex then fires exactly once in two steps, the Laplacian equation ensures return to the initial configuration. Thus they characterize, without omissions, every primitive two-cycle state.

**Energy polynomial and orbit quotient.** For one specified firing bipartition, all lower interval endpoints together sum to
\[
\sum_{f_v=1}d_v+\sum_{f_v=0}(d_v-c_v(S))=2m-|S|,
\]
because every crossing edge contributes once to the latter subtraction. Every vertex contributes an independent offset from \(0\) to \(c_v(S)-1\), proving the displayed polynomial contribution. Each cut of a connected graph has exactly two complementary firing bipartitions, corresponding to the two states of each primitive orbit. Summing once per distinct cut therefore counts orbits rather than states and proves the formula.

**Extreme energies and reflection.** A cut of size \(s\), with all cross-degrees positive, contributes only in the interval
\[
2m-s\ \le\ |x|\ \le\ 2m+s-n,
\]
with coefficient one at either endpoint. Every maximum cut has all cross-degrees positive: otherwise flipping an incident-edge-isolated vertex to the opposite shore would increase the cut. Therefore minimizing the first endpoint and maximizing the second gives exactly the two claimed energy thresholds. Only maximum cuts contribute at either global extremum; each supplies one orbit, so the extreme coefficient is \(M(G)\). Each factor \([r]_z\) is palindromic of degree \(r-1\). As \(\sum_vc_v(S)=2s\), all nonzero cut contributions have the same reflection center \(2m-n/2\), giving the polynomial identity.

**Complexity implication.** The decision problem of a primitive two-cycle at energy at most \(B\) is in NP: a witness is a chip configuration with entries in the proven ranges \(0\le x_v\le2d_v-1\), and two updates suffice to check it. The threshold formula makes the answer yes precisely when \(\operatorname{MaxCut}(G)\ge2m-B\). The ordinary MAX-CUT decision problem remains NP-complete on connected simple graphs: disconnected instances may be joined by bridges, increasing the optimum by exactly the number of bridges. This yields the claimed many-one reduction.

**Trees and paths.** For a tree every subset \(S\subseteq E\) is a cut, hence
\[
P_T(1)=\sum_{S\subseteq E(T)}\prod_{v\in V(T)}c_v(S).
\]
Root the tree. For a vertex \(v\), let \(W_v(t)\), \(t\in\{0,1\}\), be the sum of these products over choices of edges in the subtree when its parent edge is selected exactly when \(t=1\). For each child \(u\), put \(a_u=W_u(0)\) and \(b_u=W_u(1)\). Then
\[
Q_v=\sum_{u}b_u\prod_{w\ne u}(a_w+b_w),\qquad R_v=\prod_u(a_u+b_u),
\]
and \(W_v(0)=Q_v\), \(W_v(1)=Q_v+R_v\). For a leaf the pair is \((0,1)\). Compute each product and its first-degree coefficient by repeated multiplication of \((R,Q)\) pairs, using a constant number of arithmetic operations per child. At the root, \(P_T(1)=W_{\mathrm{root}}(0)\). This proves an \(O(n)\)-arithmetic-operation evaluation for every tree.

For a path, write one binary indicator for each edge of a selected subset. Both terminal edge indicators must be one for a nonzero contribution. For adjacent edge indicators \(a,b\in\{0,1\}\), the internal vertex supplies weight \(a+b\). Thus, with row and column order \(0,1\), the transfer matrix is
\[
H=\begin{pmatrix}0&1\\1&2\end{pmatrix},\qquad P_{P_n}(1)=(H^{n-2})_{1,1}.
\]
The characteristic polynomial of \(H\) is \(\lambda^2-2\lambda-1\), and the initial values for paths with two and three vertices are \(1,2\). This gives the Pell recurrence and its displayed closed form.

## Verification
The included standard-library-only Python program `verify_cut_cycles.py` independently computes the cut polynomial and the two-step dynamics on every vertex-level configuration in the finite box \(0\le x_v<2d_v\). It verifies every connected unlabeled simple graph through five vertices, additional paths, stars, cycles, complete bipartite graphs and seeded connected graphs up to ten vertices. Its recorded execution checked 72 graph cases and 1,821,396 complete configurations, confirmed extreme coefficients and energy reflection, compared the tree recurrence in 21 cases, and checked Pell values through paths on fifteen vertices. The program prints `CUT_CYCLE_ALL_CHECKS_PASSED`. The infinite-family theorem is established by the preceding proof; finite checking is corroboration, not extrapolation.

## Relationship to prior work
Bitar and Goles (1992) proved that parallel chip-firing on trees has eventual period one or two, without the unrestricted energy-resolved count stated here. Jiang (2010, Proposition 2.5) established the equal firing-count criterion for general connected graphs; its content is the first step of our proof, not the counting theorem. Jiang, Scully and Zhang (2012/2015) characterized possible periodic firing patterns and studied tree-like subgraphs, whereas the result here enumerates *states and primitive orbits*, identifies their conservation-law support with MAX-CUT, and gives a new arbitrary-tree degree-product evaluation. Later work on the middle activity stair determines period behavior within a specific energy range but does not supply this graph-wide orbit polynomial. Previously calculated counts for particular graph families do not imply the unrestricted cut identity.

## Limitations
The assertion concerns exactly primitive two-cycles. Other periods can occur on graphs with cycles; this theorem does not classify all attractors or transient times. The arithmetic-operation bound for trees does not assert linear bit complexity for arbitrarily large integers. Searches and accessible full-text comparisons found no equivalent cut-degree generating theorem, but the complete original 1992 paper was unavailable for inspection and an unindexed historical equivalent cannot be excluded. Independent external audit has not been performed.

## References
1. T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943 (first submitted 2010-03-04), especially Proposition 2.5 and Section 2.
2. T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786 (first submitted 2012-11-29); SIAM Journal on Discrete Mathematics 29 (2015), 615–630, DOI 10.1137/130933770.
3. J. Bitar and E. Goles, *Parallel chip firing games on graphs*, Theoretical Computer Science 92 (1992), 291–300, DOI 10.1016/0304-3975(92)90316-8.
4. D. Wang and N. Lannan, *All parallel chip-firing games with \(2|E|-|V|<|\sigma|<2|E|\) have period \(2\)*, arXiv:2608.04153 (2026); later period-only context.
5. R. M. Karp, *Reducibility Among Combinatorial Problems*, in Complexity of Computer Computations (1972), 85–103; classical MAX-CUT hardness background.
