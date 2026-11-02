# Exact optimal multi-leader placement for second-order coherence on an unweighted path

## Finding

**Theorem.** Fix integers \(n\ge2\) and \(2\le k\le n\). Let \(P_n\) be the unweighted undirected path with vertices \(1,\ldots,n\), and let \(S\) be any set of exactly \(k\) perfectly grounded (noise-free) leader vertices. Write \(F=V(P_n)\setminus S\), let \(L_{FF}\) denote the principal follower submatrix of the combinatorial graph Laplacian, and set
\[
J(S)=\operatorname{tr}(L_{FF}^{-2}),
\]
where \(J(S)=0\) if \(F\) is empty.

Write the leaders in increasing order as \(s_1<\cdots<s_k\), and define the nonnegative integer follower-gap lengths
\[
g_0=s_1-1,\quad g_i=s_{i+1}-s_i-1\ (1\le i<k),\quad g_k=n-s_k.
\]
These satisfy \(\sum_{i=0}^{k}g_i=n-k\). Define
\[
P(m)=\frac{m(m+1)(m^2+m+1)}6,\qquad
Q(m)=\frac{m(m+2)(2m^2+4m+9)}{180}
\]
for every nonnegative integer \(m\). Then the exact performance is
\[
\boxed{J(S)=P(g_0)+P(g_k)+\sum_{i=1}^{k-1}Q(g_i).}
\]

In particular, write the strictly increasing incremental cost sequences
\[
p_r=P(r)-P(r-1)=\frac{r(2r^2+1)}3,\qquad
q_r=Q(r)-Q(r-1)=\frac{(2r+1)(4r^2+4r+7)}{180},\quad r\ge1.
\]
**All global minimizers** are obtained by selecting the \(n-k\) cheapest individual increments from two copies of the \(p_r\) sequence and \(k-1\) copies of the \(q_r\) sequence, making any choices among equal-priced increments; the number selected from each sequence is its corresponding gap length. Conversely, every such selection is globally optimal. The prefix property of a selected sequence is automatic because its increments increase strictly. A min-heap constructs one optimal set in \(O(k+(n-k)\log(k+1))\) arithmetic comparisons after heap initialization.

For \(k\ge2\), every optimal leader set contains **both endpoints** if and only if
\[
\boxed{n\le3k-2.}
\]
When \(n>3k-2\), no optimal leader set contains both endpoints. Across any optimum the two endpoint follower tails differ in length by at most one, and all internal follower gaps differ in length by at most one. For \(n-k\le k-1\), the optimal cost is exactly \((n-k)/4\): all followers can be isolated between consecutive leaders.

There is also a sharp fixed-leader-count scaling law. For fixed \(k\ge2\), set \(\rho=15^{1/3}\) and \(D_k=2+(k-1)\rho\). As \(n\to\infty\), **every** optimum obeys
\[
\frac{g_0}{n},\frac{g_k}{n}\longrightarrow\frac1{D_k},\qquad
\frac{g_i}{n}\longrightarrow\frac{\rho}{D_k}\quad(1\le i<k),
\]
and
\[
\boxed{\lim_{n\to\infty}\frac{\min_{|S|=k}J(S)}{n^4}
=\frac{1}{6D_k^3}.}
\]
For two leaders, their asymptotic normalized locations are \(1/D_2\approx0.2239\) and \(1-1/D_2\approx0.7761\). This second-order spacing differs from the first-order path-leader objective.

## Assumptions and scope

All edges have unit conductance; the leader set has **exactly** \(k\) vertices and the leaders are perfectly grounded. Noise acts independently with unit intensity on follower acceleration. The combinatorial, not normalized, Laplacian is used. The trace in the theorem is of the square of the **grounded inverse**: it is not the trace of the square of the ungrounded Moore–Penrose pseudoinverse. The proof allows \(n=k\), with empty follower set, zero trace, and unique leader set.

In particular, for any damping \(\gamma>0\), the stable second-order network
\[
\ddot z+\gamma L_{FF}\dot z+L_{FF}z=\eta
\]
with independent unit-intensity white acceleration noise \(\eta\) has total stationary **position** variance \(J(S)/(2\gamma)\). For each positive grounded eigenvalue \(\lambda\), the corresponding scalar stationary variance is \(1/(2\gamma\lambda^2)\); hence all leader sets are ordered by the displayed trace, independently of \(\gamma\).

The result addresses \(k\ge2\), not the separately studied one-leader location problem. A weighted path, finite leader anchoring, unequal noise intensities, and optimization of first-order coherence are outside the stated theorem.

## Proof

**1. Exact Green kernels.** Deleting the \(k\) leader rows and columns splits \(L_{FF}\) into independent tridiagonal blocks, one per nonempty follower gap. For a tail with \(m\) followers and only one grounded end, numbering followers from the grounded end outward gives the inverse Green kernel
\[
G^{\mathrm{tail}}_{ij}=\min(i,j),\qquad1\le i,j\le m.
\]
For an interior gap of \(m\) followers grounded at both ends, the inverse kernel is
\[
G^{\mathrm{int}}_{ij}=\frac{\min(i,j)(m+1-\max(i,j))}{m+1}.
\]
These expressions follow by checking the tridiagonal discrete second difference and the respective Neumann-free/Dirichlet or two-Dirichlet boundary conditions. In both cases, the diagonal second moment is \(\operatorname{tr}(G^2)=\sum_{i,j}G_{ij}^2\). Summing the corresponding polynomial series gives, respectively,
\[
\sum_{i,j=1}^{m}\min(i,j)^2=P(m),\quad
\sum_{i,j=1}^{m}\left(\frac{\min(i,j)(m+1-\max(i,j))}{m+1}\right)^2=Q(m).
\]
The formulas hold at \(m=0\) by empty summation. Traces add over blocks, proving the exact gap-cost decomposition.

**2. Discrete marginal costs and all minimizers.** Subtracting consecutive polynomial values yields precisely \(p_r\) and \(q_r\). Their successive differences are
\[
p_{r+1}-p_r=2r^2+2r+1>0,\qquad
q_{r+1}-q_r=\frac{12r^2+24r+19}{90}>0
\]
for all \(r\ge1\). Selecting a gap length \(g\) from one of these sequences incurs the sum of its first \(g\) increments. If a proposed gap vector omits a strictly cheaper increment from one sequence while including a more expensive final increment from another, transferring one follower from the latter gap to the former strictly improves \(J\). Conversely, a vector choosing the globally least \(n-k\) increments cannot be improved because any other selection of that many increments costs at least as much, even without imposing the prefix restrictions. Strict increase within each sequence ensures that any globally cheapest choice can be made prefix-closed. Ties between sequences allow exactly the claimed alternative minimizers. The min-heap algorithm selects the next cheapest head of each sequence successively; each step is a legal prefix extension and uses \(O(\log(k+1))\) comparisons.

Equal-type marginal sequences have equal strictly increasing prices; hence two tails (or two interior gaps) can never have lengths differing by two or more in an optimum: the last increment in the longer would cost strictly more than the next increment in the shorter.

**3. Sharp endpoint cutoff.** The first three interior increment prices and the first tail price are
\[
q_1=\frac14,\qquad q_2=\frac{31}{36},\qquad
p_1=1,\qquad q_3=\frac{77}{36}.
\]
Thus the first \(2(k-1)\) selected increments necessarily come from the interior gaps—two per gap, whenever that many followers exist—before any tail increment can be chosen. If \(n-k\le2(k-1)\), every minimizing gap vector therefore has \(g_0=g_k=0\), and both endpoints are leaders. If \(n-k>2(k-1)\), the next cheapest available increment is a tail increment \(p_1\), strictly cheaper than every interior \(q_3\), so any optimum has a positive tail. This is exactly \(n\le3k-2\). For \(n-k\le k-1\), all selected increments have price \(q_1=1/4\), proving the isolated-follower minimum.

**4. Fixed-count limit.** Divide the gap vector by \(n\). Because \(P(m)=m^4/6+O(m^3)\) and \(Q(m)=m^4/90+O(m^3)\), uniformly for integer \(0\le m\le n\), the normalized objective converges uniformly on the compact simplex
\[
\mathcal S_k=\left\{(x_0,\ldots,x_k)\in[0,1]^{k+1}:\sum_i x_i=1\right\}
\]
to the strictly convex function
\[
\mathcal J(x)=\frac{x_0^4+x_k^4}{6}+\frac1{90}\sum_{i=1}^{k-1}x_i^4.
\]
Its unique minimizer has all coordinates strictly positive: if one were zero and another positive, transferring a sufficiently small mass to the zero coordinate strictly lowers this strictly convex homogeneous degree-four cost. The Lagrange multiplier equations imply both tail coordinates are a common value \(a\), all interior coordinates a common value \(b\), and \(b^3=15a^3\). Together with \(2a+(k-1)b=1\), this yields \(a=1/D_k\) and \(b=\rho/D_k\). Evaluating \(\mathcal J\) there gives \(1/(6D_k^3)\). Every sequence of discrete minimizers converges to this unique continuum minimizer by uniform convergence and compactness. This proves the profile and minimum-limit statements.

**5. Stationary position variance.** Along a grounded eigenmode, the stochastic state matrix is \(\begin{pmatrix}0&1\\-\lambda&-\gamma\lambda\end{pmatrix}\). The stationary covariance Lyapunov equation, with unit white forcing in the acceleration component, has off-diagonal covariance zero, velocity variance \(1/(2\gamma\lambda)\), and position variance \(1/(2\gamma\lambda^2)\). The grounded Laplacian has strictly positive eigenvalues whenever at least one leader is fixed. Summing mode variances yields \(J(S)/(2\gamma)\), as asserted.

## Verification

A standalone Python standard-library script, `verify.py`, accompanies this note together with captured output, `checks.txt`. It reconstructs \(L_{FF}\), computes exact-rational inverses, tests the Green-cost formula for every leader subset of path orders from \(2\) through \(11\), exhaustively checks the minimizing subsets, and checks the sharp endpoint cutoff. It also samples larger instances to verify discrete exchange conditions, telescoping marginal identities, and the fixed-count asymptotic predictions.

The recorded checks comprise 4,082 exact grounded inverses, 65 exhaustive optimization instances (including auxiliary one-leader regression tests), 55 endpoint-cutoff tests, 5,466,943 sampled exchange comparisons, 67,816 marginal identities, and five asymptotic profiles. These **finite tests are not a proof** for arbitrary \(n\); the Green-kernel and exchange arguments above supply the infinite-domain proof. Only the Python standard library is required to replay them: `python verify.py`.

## Relationship to prior work

Fitch and Leonard (2014) explicitly solve leader placement for certain graphs, including paths, under a **first-order** noisy-consensus variance objective involving the inverse grounded Laplacian. Patterson, McGlohon, and Dyagilev (2014, 2016) provide exact general polynomial-time methods for leader placement on weighted paths and rings under first-order coherence and convergence-rate objectives. These objectives do not imply an inverse-square marginal-price classification.

Mackin and Patterson (2019) identify inverse-square trace quantities for higher-order noisy consensus with finite absolute-information leader gains and give general submodular optimization methods. Their model and general optimization guarantees motivate the second-order criterion, but the examined derivations do not state all exact optimum locations, the sharp endpoint-density cutoff, or the cube-root-of-15 profile for perfectly grounded paths. A large-anchoring limit can connect the objectives, but such a limit by itself does not imply this exact optimal-location theorem.

The new result is the **complete all-minimizer integer classification for every \(2\le k\le n\)**, the exact endpoint-support threshold, and the fixed-count continuum profile for the grounded inverse-square objective. The previously studied single-leader problem is excluded. A literature search is not a mathematical proof of publication priority.

## Limitations

Only simple unweighted paths, identical noise intensities, perfectly grounded leaders, and the specific inverse-square trace objective are covered. The constant-factor interpretation as second-order stationary position variance uses the displayed proportional-Laplacian damping model and positive \(\gamma\). No result is claimed for arbitrary network topologies, weighted paths, finite leader gains, or higher-than-second-order dynamics. Independent validation has not been performed. Specialized historical priority or equivalent formulations outside the inspected literature may exist.

## References

1. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first posted July 7, 2014. https://arxiv.org/abs/1407.1569
2. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595, first posted December 20, 2014. https://arxiv.org/abs/1412.6595
3. S. Patterson, N. McGlohon and K. Dyagilev, *Optimal k-Leader Selection for Coherence and Convergence Rate in One-Dimensional Networks*, arXiv:1604.07094, first posted April 24, 2016. https://arxiv.org/abs/1604.07094
4. E. Mackin and S. Patterson, *Submodularity in Systems with Higher Order Consensus with Absolute Information*, arXiv:1905.09156, first posted May 22, 2019. https://arxiv.org/abs/1905.09156
