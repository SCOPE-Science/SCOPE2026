# Budgeted discounted hitting domination on balanced complete bipartite graphs

## Finding

Let \(n\ge2\) be an integer and \(0<\lambda<1\). On the balanced complete bipartite graph \(K_{n,n}\), define the discounted hitting support of a nonempty source set \(S\) by
\[
h_v^S=\mathbb E_v[\lambda^{T_S}],\qquad
T_S=\inf\{t\ge0:X_t\in S\},
\]
where \((X_t)\) is the simple non-lazy random walk. Define its uniform support and the budget optimum as
\[
\Phi_\lambda(S)=\min_{v\in V(K_{n,n})}h_v^S,
\qquad
H_{n,k}(\lambda)=\max_{|S|=k}\Phi_\lambda(S).
\]

For even \(k=2j\), let
\[
B_{n,k}(\lambda)=\frac{\lambda j}{n(1-\lambda)+\lambda j}.
\]
For odd \(k=2j+1\), let
\[
N_{n,k}(\lambda)=
\frac{\lambda n j+\lambda^2(n-j)(j+1)}
{n^2-\lambda^2(n-j-1)(n-j)},
\qquad
U_{n,k}(\lambda)=
\frac{\lambda^2 k}{n(1-\lambda^2)+\lambda^2 k}.
\]
Then, for all \(1\le k\le2n\), the exact maximum uniform support is
\[
\boxed{
H_{n,k}(\lambda)=
\begin{cases}
B_{n,k}(\lambda),&k<n,\ k\text{ even},\\
\max\{N_{n,k}(\lambda),U_{n,k}(\lambda)\},&k<n,\ k\text{ odd},\\
\lambda,&n\le k<2n,\\
1,&k=2n.
\end{cases}}
\]

Every source set achieving this budget optimum is characterized by how many sources it selects from each shore. For even \(k<n\), the only optimal profile is \((k/2,k/2)\). For odd \(k<n\), only the near-balanced profile \(((k+1)/2,(k-1)/2)\) or the one-shore profile \((k,0)\), and their reversals, can be optimal. The larger of \(N_{n,k}\) and \(U_{n,k}\) determines the choice. For \(n\le k<2n\), the optimal sets are precisely those containing one entire shore. The only optimal set for \(k=2n\) is the full vertex set.

For odd \(3\le k<n\), these two regimes exchange dominance at a unique value
\[
\boxed{
\lambda_{n,k}=
\frac{\sqrt{(k+1)^2+8n(2n+1-k)}-(k+1)}
{2(2n+1-k)}.}
\]
The near-balanced profiles are the only maximizers for \(\lambda<\lambda_{n,k}\), the one-shore profiles are the only maximizers for \(\lambda>\lambda_{n,k}\), and both are maximizers at equality. For \(k=1\), the two profiles agree.

The exact numbers of labeled source sets maximizing the uniform support are \(\binom n{k/2}^2\) for even \(k<n\), and, for odd \(k=2j+1<n\), either \(2\binom nj\binom n{j+1}\), or \(2\binom nk\), or their sum, according as the near-balanced score is larger, smaller, or equal to the one-shore score. The \(k=1\) count is \(2n\). For \(n\le k<2n\), the count is \(2\binom n{k-n}\), and for \(k=2n\) it is \(1\).

Finally, for every \(0<\tau\le1\), the discounted hitting domination number defined by the uniform threshold is
\[
\boxed{
\delta_{\lambda,\tau}(K_{n,n})
=\min\{1\le k\le2n:H_{n,k}(\lambda)\ge\tau\}.}
\]
In particular, \(\delta_{\lambda,\tau}(K_{n,n})=2n\) whenever \(\tau>\lambda\); otherwise the optimum is the least qualifying budget among \(1,\ldots,n\).

## Assumptions and scope

All graphs are finite, simple, undirected, and have no loops. The graph has precisely two shores of size \(n\), with every edge crossing the shores present. The random walk moves to one of the \(n\) neighbors uniformly and has no holding probability. Source vertices are pinned at support \(1\), and the attenuation parameter satisfies \(0<\lambda<1\). The source budget is an integer \(1\le k\le2n\). No statement about \(\lambda=1\), irregular bipartite graphs, or arbitrary weighted transitions is implied.

The number of budget-optimal source sets counts distinct vertex subsets, not automorphism orbits. The counts do **not** claim to enumerate every source set meeting a lower threshold below the optimum; the final explicit threshold example is checked separately.

## Proof

Let the shores be \(L\) and \(R\), and suppose \(S\) contains \(x\) vertices of \(L\) and \(y\) vertices of \(R\). When \(x<n\) and \(y<n\), all non-sources in \(L\) have a common support \(u\), and all non-sources in \(R\) have a common support \(v\). The first-step equations are
\[
u=\lambda\left(\frac yn+\left(1-\frac yn\right)v\right),
\qquad
v=\lambda\left(\frac xn+\left(1-\frac xn\right)u\right).
\]
Solving them gives
\[
u=\frac{\lambda n y+\lambda^2x(n-y)}
{n^2-\lambda^2(n-x)(n-y)},
\qquad
v=\frac{\lambda n x+\lambda^2y(n-x)}
{n^2-\lambda^2(n-x)(n-y)}.
\]
The denominator is positive since \(0<\lambda<1\). A source has support \(1\), so the bottleneck is \(\min\{u,v\}\). Moreover,
\[
u-v=\frac{\lambda n(y-x)(1-\lambda)}
{n^2-\lambda^2(n-x)(n-y)}.
\]
Thus, by interchanging shores if necessary, assume \(x\ge y\); then \(u\le v\), and \(u\) is the objective.

For \(k=x+y<n\), write
\[
t=\frac kn,\qquad d=\frac{x-y}{n},\qquad
c=2(1-\lambda)+\lambda t,
\qquad
D_0=1-\lambda^2\left(1-\frac t2\right)^2.
\]
Here \(0\le d\le t<1\), \(D_0>0\), and \(c-\lambda d>0\). The balanced continuous benchmark is
\[
B=\frac{\lambda t}{c}.
\]
Direct algebra gives the exact identity
\[
B-u(d)=
\frac{\lambda(1-\lambda)}{2c}
\frac{d(c-\lambda d)}{D_0+\lambda^2d^2/4}.
\]
Therefore \(u(d)<B\) for every \(d>0\), and \(d=0\) is the unique optimum whenever the budget is even.

For odd budgets \(d=0\) is impossible. Define
\[
g(d)=\frac{d(c-\lambda d)}{D_0+\lambda^2d^2/4}.
\]
Its derivative has the sign of
\[
Q(d)=D_0(c-2\lambda d)-\frac{\lambda^2c}{4}d^2.
\]
Since \(Q'(d)=-2\lambda D_0-\lambda^2cd/2<0\), the function \(g\) is increasing and then possibly decreasing, with no interior local minimum. Hence \(u=B-\frac{\lambda(1-\lambda)}{2c}g\) has no interior local maximum. Among the admissible lattice values of \(d\) for odd \(k\), its maximum is at either the smallest value \(d=1/n\) or the largest value \(d=k/n\). These correspond respectively to profiles \((j+1,j)\) and \((k,0)\), where \(k=2j+1\). Substitution yields \(N_{n,k}\) and \(U_{n,k}\). When \(k=1\), they are the same profile.

For odd \(3\le k<n\), put
\[
F_{n,k}(\lambda)=2n-(k+1)\lambda-(2n+1-k)\lambda^2.
\]
The exact subtraction of the endpoint scores is
\[
U_{n,k}-N_{n,k}=
-\frac{\lambda n(k-1)(1-\lambda)F_{n,k}(\lambda)}
{4\bigl(n(1-\lambda^2)+\lambda^2k\bigr)
\bigl(n^2-\lambda^2(n-j-1)(n-j)\bigr)}.
\]
The denominator and all other displayed factors are strictly positive. The polynomial \(F_{n,k}\) is strictly decreasing on \([0,1]\), starts at \(2n>0\), and ends at \(-2<0\). Its unique root is the stated \(\lambda_{n,k}\), proving the strict phase change and tie classification.

If \(S\ne V(K_{n,n})\), every non-source satisfies \(h_v^S\le\lambda\), since its first step incurs a factor \(\lambda\) and all neighbor supports are at most \(1\). Choosing all vertices of one shore as sources gives \(h_v^S=\lambda\) at every non-source of the other shore. If both shores contain a non-source, every such vertex has a non-source neighbor whose support is less than \(1\); the first-step average is then strictly less than \(\lambda\). Consequently, for \(n\le k<2n\), the budget optimum is \(\lambda\) and its maximizers are exactly the sets containing one entire shore. For \(k=2n\), the score is \(1\). This finishes the budget diagram and the source-set classification.

The displayed source-set counts follow by choosing the prescribed numbers of vertices independently from the labeled shores. For any threshold \(\tau\), a budget admits a qualifying set exactly when its maximum uniform support is at least \(\tau\); taking the least such budget proves the discounted hitting domination formula.

As a concrete strict symmetry-breaking instance, on \(K_{4,4}\) take \(\lambda=9/10\) and \(\tau=761/1000\). A two-source set has best score \(9/13\). For three sources, a near-balanced \((2,1)\) placement has score \(423/557\), whereas a \((3,0)\) placement has score \(243/319\), and
\[
\frac9{13}<\frac{423}{557}<\frac{761}{1000}<\frac{243}{319}.
\]
Thus exactly the \(2\binom43=8\) sets consisting of three vertices from one shore are minimum qualifying source sets. The transition for budget three occurs at \((\sqrt{13}-1)/3\).

## Verification

The standalone checker `artifacts/verify.py` uses exact Python rational arithmetic and constructs each complete bipartite graph explicitly. It independently solves the full vertexwise pinned random-walk linear system (rather than substituting the two-shore formula), compares its minimum to the rational formulas, and exhaustively checks all subsets and all budgets.

Its exhaustive cases cover \(2\le n\le5\) at fidelities \(1/3,1/2,3/4,9/10,19/20,99/100\). The checker also enumerates the eight qualifying minimum source sets in the example.

Replay:

`ALL CHECKS PASSED; parameter_cases=168; exact_vertex_linear_systems=8136; source_subsets_checked=8136; n=2..5; lambdas=1/3,1/2,3/4,9/10,19/20,99/100; n4_threshold_example=8`

The finite verification is corroborative. The arbitrary-size and continuum-parameter theorem is established by the first-step identities and the one-variable extremum argument above.

## Relationship to prior work

Allagan, Pereyra, and Massey introduced discounted hitting domination and the min-cardinality uniform-support threshold problem in September 2026, building on already known penalized and group hitting probabilities. They establish general submodularity, an exact integer-programming formulation, distance-domination recovery intervals, and special-family results for complete graphs, stars, and spiders. Their recovery theorem already covers portions of threshold space where the new minimum agrees with ordinary distance domination; those special cases are not presented as independently new here.

The new theorem is an explicit complete budget–fidelity phase diagram and a classification of every budget-optimal source set on \(K_{n,n}\), including a parity-sensitive switch between balanced and entirely one-shore placements at a precise algebraic fidelity. Neither general mixed-integer solvability nor the distance recovery sandwich supplies this extremizer classification or its transition threshold.

Guo, Lin, Wang, Wong, and Lin studied group hitting probability queries in 2024. That work treats evaluation and ranking of target sets from a given starting node. The fixed-start target-ranking objective is distinct from maximizing the minimum first-hit support over **all** starting vertices with a fixed source budget.

## Limitations

The result is specific to balanced complete bipartite graphs with ordinary non-lazy random walks and homogeneous discount. Source sets maximizing the budget score need not exhaust all sets that qualify at a lower prescribed threshold. In particular, the optimizer counts do not automatically count all minimum threshold-feasible sets except in separately analyzed cases such as the displayed \(K_{4,4}\) example.

The September 2026 initiating paper was examined in its accessible HTML material, including the definition, distance bounds, submodularity results, and section headings. Later portions of that source were not fully retrievable through the consulted public interfaces. Its accessible stated special families exclude balanced bicliques, but the possibility of an unadvertised related intermediate observation in later sections is a residual originality risk. Earlier group hitting literature may also use terminology not indexed by the searches performed.

## References

1. J. D. Allagan, K. Pereyra, and W. A. Massey, “Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms,” arXiv:2609.31535v1, first public September 25, 2026. MSC 2020: \(05C69\), \(05C85\), \(60J20\), \(68Q17\), \(90C11\), \(91D30\). https://arxiv.org/abs/2609.31535
2. Q. Guo, D. Lin, S. Wang, R. C.-W. Wong, and W. Lin, “Efficient Algorithms for Group Hitting Probability Queries on Large Graphs,” IEEE Transactions on Knowledge and Data Engineering 36 (2024), 2995–3008, DOI 10.1109/TKDE.2023.3349164.
