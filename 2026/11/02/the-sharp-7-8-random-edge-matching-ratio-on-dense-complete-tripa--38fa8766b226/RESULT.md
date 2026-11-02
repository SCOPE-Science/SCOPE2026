# The sharp \(7/8\) random-edge matching ratio on dense complete tripartite graphs

## Finding

Let \(G_n=K_{a_n,b_n,c_n}\) be complete tripartite, with deterministic positive integer part sizes satisfying
\[
\frac{a_n}{n}\longrightarrow a,\qquad
\frac{b_n}{n}\longrightarrow b,\qquad
\frac{c_n}{n}\longrightarrow c,\qquad a\ge b\ge c>0.
\]
Repeatedly choose one uniformly random edge among those whose endpoints are still unmatched, add it to the matching, and delete its endpoints. Write \(M_n\) for the terminal number of matched edges, \(U_n\) for the number of remaining unmatched vertices, and \(N_{AB,n},N_{AC,n},N_{BC,n}\) for the numbers of selected edges of each part-pair type. Then jointly in probability,
\[
\begin{aligned}
\frac{N_{AB,n}}n&\longrightarrow b\left(1-\frac{c}{2a}\right),\\
\frac{N_{AC,n}}n&\longrightarrow c\left(1-\frac{b}{2a}\right),\\
\frac{N_{BC,n}}n&\longrightarrow \frac{bc}{2a},\\
\frac{U_n}{n}&\longrightarrow\frac{(a-b)(a-c)}a,\\
\frac{M_n}{n}&\longrightarrow b+c-\frac{bc}{2a}.
\end{aligned}
\]
All five convergences also hold for expectations. In particular, if \(\nu(G_n)\) denotes the maximum matching cardinality, then
\[
\frac{\mathbb E M_n}{\nu(G_n)}\longrightarrow
\mathcal R(a,b,c):=
\frac{b+c-bc/(2a)}{\min\{(a+b+c)/2,b+c\}}.
\]
Across all positive \(a\ge b\ge c\),
\[
\boxed{\mathcal R(a,b,c)\ge\frac78,}
\]
with equality **if and only if** \(a:b:c=2:1:1\). Thus \(K_{2n,n,n}\) has asymptotic random-greedy matching size \(7n/4\), while a maximum matching has size \(2n\). This is a sharp *asymptotic within-family* statement; no finite-order universal \(7/8\) bound is asserted.

## Assumptions and scope

The graph is simple and has precisely three independent vertex parts, with all interpart edges present and no intrapart edges. Each step selects uniformly from the **currently feasible edges**, not uniformly from the set of maximal matchings or by first selecting a vertex. The part sizes are deterministic integer arrays with strictly positive linear limits, with \(n\) an arbitrary common scale (not necessarily the total number of vertices). Sorting the limiting sizes is without loss of generality; their finite-order ranking need not be identical for every \(n\). All limits refer to \(n\to\infty\).

## Proof

**1. Uniform-edge chain and finite-time fluid limit.** Attach independent exponential clocks of rate \(1/n\) to every currently feasible edge, discarding clocks incident to a chosen edge when it fires. By exponential competition, the embedded edge-selection chain is exactly uniform among feasible edges. If \((A_n(t),B_n(t),C_n(t))\) are the numbers of surviving vertices, define \(X_n=A_n/n\), \(Y_n=B_n/n\), \(Z_n=C_n/n\). Edges between the first two parts fire at total rate \(A_nB_n/n=nX_nY_n\); similarly for the other pairs. Consequently the drift is
\[
F(x,y,z)=\bigl(-x(y+z),-y(x+z),-z(x+y)\bigr).
\]
Each jump is of order \(1/n\), all rates are bounded by a constant times \(n\) on the fixed compact box containing the trajectories, and each coordinate's compensated martingale has predictable quadratic variation at most \(C_T/n\) over \([0,T]\). Doob's inequality followed by Gronwall's inequality yields, for every fixed \(T<\infty\),
\[
\sup_{t\le T}\|(X_n,Y_n,Z_n)(t)-(x,y,z)(t)\|\xrightarrow{\mathbb P}0,
\]
where \((x,y,z)\) is the unique nonnegative solution of \((x',y',z')=F(x,y,z)\) with \((x(0),y(0),z(0))=(a,b,c)\).

**2. Exact solution of the three-population flow.** Let \(u(t)\) solve
\[
u'(t)=(1-au(t))(1-bu(t))(1-cu(t)),\qquad u(0)=0.
\]
Then the exact fluid solution is
\[
\begin{aligned}
x(t)&=a(1-bu(t))(1-cu(t)),\\
y(t)&=b(1-au(t))(1-cu(t)),\\
z(t)&=c(1-au(t))(1-bu(t)).
\end{aligned}
\]
For example, differentiating the first expression and using the scalar equation gives \(x'=-x(y+z)\); the other identities follow by symmetry. Because \(a\ge b\ge c>0\), the scalar solution is increasing, remains in \([0,1/a)\), and tends to \(1/a\) as \(t\to\infty\), including when some limiting part sizes coincide. Therefore
\[
(x(t),y(t),z(t))\longrightarrow\left(\frac{(a-b)(a-c)}a,0,0\right).
\]

**3. Justification at the random terminal time.** Finite-horizon fluid convergence alone does not imply terminal convergence. First suppose \(a>b\). For any sufficiently large deterministic \(T\), \(x(T)>y(T)+z(T)\). With probability tending to one, the same strict inequality holds for the remaining finite graph at \(T\). No subsequent matching can change the fact that the largest part outnumbers the other two together: choosing an edge between the smaller parts increases this excess by two, and choosing an edge incident to the largest part leaves it unchanged. At termination, only largest-part vertices remain. The number of edges selected after \(T\) is bounded by the total number of vertices in the two smaller parts at \(T\). Hence the final largest-part count differs from \(A_n(T)\) by at most \(B_n(T)+C_n(T)\). Divide by \(n\), let \(n\to\infty\), then let \(T\to\infty\). This establishes the terminal formula when \(a>b\).

If \(a=b\), all three deterministic fluid populations tend to zero, so for large \(T\) the total number of unmatched vertices remaining at \(T\), divided by \(n\), is arbitrarily small with high probability. The terminal count can only decrease from this value. This establishes the same formula, now zero, in the tied case. Sorting errors of order \(o(n)\) at finite \(n\) do not affect either argument.

**4. Exact limiting counts for each edge type.** Let \(N_{AB,n}(t)\) count chosen edges of type \(AB\) up to artificial time \(t\). Its predictable intensity is \(nX_n(t)Y_n(t)\), so the preceding quadratic-variation argument gives
\[
\frac{N_{AB,n}(T)}n\xrightarrow{\mathbb P}\int_0^T x(t)y(t)\,dt
\]
for each fixed \(T\); the other pair types are analogous. After \(T\), the number of additional choices is at most the entire population remaining at \(T\) divided by two. If \(a>b\), the stronger bound by the two small parts holds; if \(a=b\), the entire population at large \(T\) is small. In both cases the tail contribution vanishes in the successive \(n\), then \(T\), limit.

Using \(u\) as the integration variable and the exact formulas above,
\[
\begin{aligned}
\int_0^\infty xy\,dt&=ab\int_0^{1/a}(1-cu)\,du=b\left(1-\frac{c}{2a}\right),\\
\int_0^\infty xz\,dt&=ac\int_0^{1/a}(1-bu)\,du=c\left(1-\frac{b}{2a}\right),\\
\int_0^\infty yz\,dt&=bc\int_0^{1/a}(1-au)\,du=\frac{bc}{2a}.
\end{aligned}
\]
Summing gives the claimed limiting matching size. The unmatched count follows equally from the terminal fluid value or from total initial vertices minus twice the matching size. Every normalized count is deterministically bounded, so convergence in probability also implies convergence of expectations.

**5. Matching optimum and sharp efficiency.** On a complete multipartite graph with part sizes \(A,B,C\), any matching has at most \(\lfloor(A+B+C)/2\rfloor\) edges and at most \(B+C\) edges when \(A\) is the largest part. Both bounds are attainable in the relevant case: if \(A\ge B+C\), match all vertices outside the largest part across the cut; otherwise repeatedly match two currently largest nonempty parts, leaving at most one vertex. Therefore
\[
\frac{\nu(G_n)}n\longrightarrow\min\left\{\frac{a+b+c}{2},b+c\right\}.
\]
Set \(x=b/a\), \(y=c/a\), and \(s=x+y\), so \(0<y\le x\le1\). If \(s\le1\),
\[
\mathcal R=1-\frac{xy}{2s}\ge1-\frac{s}{8}\ge\frac78,
\]
using \(xy\le s^2/4\). Equality forces \(s=1\) and \(x=y=1/2\). If \(s\ge1\),
\[
1-\mathcal R=\frac{(1-x)(1-y)}{1+s}
\le\frac{(1-s/2)^2}{1+s}\le\frac18.
\]
The final expression is strictly decreasing for \(1\le s<2\), and equals \(1/8\) at \(s=1\); again equality forces \(x=y=1/2\). Thus \(7/8\) is the unique sharp limiting ratio, attained when \(a:b:c=2:1:1\).

## Verification

Run the included Python standard-library checker with `python3 checker.py`. It independently enumerates the full exact edge-type-count distribution using both a size-state recursion and labeled-vertex edge enumeration on small graphs, verifies the fluid and type-rate polynomial identities by exact rational coefficient arithmetic, checks the sharp ratio on a dense rational grid, and performs bounded randomized diagnostics on larger graphs. The script reports 3311 passed exact/algebraic assertions; randomized diagnostics are supplementary. The asymptotic convergence and global continuous optimization follow from the preceding proof, not from finite enumerations, samples or a numerical fit.

## Relationship to prior work

Hertz, Bonte, Devillez and Mélot [1] explicitly define the same *random-feasible-edge algorithm* in their introduction but focus on a different invariant, the uniform average over all maximal matchings. Since the greedy algorithm does not choose maximal matchings uniformly, their asymptotic formulas do not imply the distribution-specific counts here. Arnosti [2] analyzes randomized greedy matching on bipartite graphs, including the random-edge rule, averaging over random edge sets, not the present deterministic dense graph with three positive parts. Dyer and Frieze [3] introduce the fixed-graph random-edge process and prove worst-case/sparse-family performance results; their abstract and indexed descriptions do not state the tripartite fluid solution or the sharp class ratio. Pippenger [4] studies edge adsorption on graph classes with strong local restrictions, rather than dense complete tripartite graphs.

The formulas here use known stochastic-approximation techniques but concern a previously unidentified exact fluid first integral and sharp three-part class bound in the literature examined. A complete historical priority guarantee is not asserted. Full text of [3] could not be obtained during this inspection; its precise scope remains a residual literature risk.

## Limitations

The limits require three *strictly positive* proportional part sizes and uniform feasible-edge selection. The result does not claim a sharp bound for all finite complete tripartite graphs, unequal edge weights, vertex-first greedy algorithms, arbitrary complete multipartite graphs with four or more parts, or a central limit theorem. The exact-rational finite checker is corroborating evidence only; it is not an infinite proof and does not independently validate literature priority.

## References

[1] A. Hertz, S. Bonte, G. Devillez and H. Mélot, *The average size of maximal matchings in graphs*, arXiv:2204.10236, first posted 2022-04-21. https://arxiv.org/abs/2204.10236

[2] N. Arnosti, *Greedy Matching in Bipartite Random Graphs*, *Stochastic Systems* 12 (2022), 133–150; online publication 2021-11-02; author's April 2021 manuscript: https://nickarnosti.com/ResearchPapers/Arnosti_GreedyMatching.pdf

[3] M. Dyer and A. Frieze, *Randomized greedy matching*, *Random Structures & Algorithms* 2 (1991), 29–45. https://doi.org/10.1002/rsa.3240020104

[4] N. Pippenger, *Random Sequential Adsorption on Graphs*, *SIAM Journal on Discrete Mathematics* 2 (1989), 393–401. https://doi.org/10.1137/0402034
