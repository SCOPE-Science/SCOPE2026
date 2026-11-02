# A seven-player limited-liability transition for closest voluntary Shapley payment flows

## Finding

For the symmetric pair-synergy cooperative game
\[
v(S)=a|S|+b\binom{|S|}{2},\qquad a\geq0,\quad b>0,
\]
consider the Euclidean-closest, edge-budget-balanced, fully voluntary payment flow whose expected terminal allocation is the Shapley value, with the uniform random-order and one-step deferral protocol of Lim [1]. With \(n\) players, let \(q_k\) be the payment to each incumbent when a \((k+1)\)-st player enters, and \(p_k\) the corresponding entrant payment. The unique closest signed flow has \(q_k=bz_k\) and \(p_k=a+bk-kq_k\), where \((z_1,\ldots,z_{n-1})\) is given exactly, for every \(2\leq n\leq7\), by

| \(n\) | \((z_1,\ldots,z_{n-1})\) |
|:--:|:--|
| 2 | \((1/2)\) |
| 3 | \((1/2,1/2)\) |
| 4 | \((1/2,2/5,3/5)\) |
| 5 | \((1/2,30/71,45/142,54/71)\) |
| 6 | \((1/2,20/41,10/41,12/41,40/41)\) |
| 7 | \((1/2,1/2,210/929,168/929,280/929,1200/929)\) |

For every \(2\leq n\leq6\), these closest signed flows are already componentwise nonnegative for all \(a\geq0\). At \(n=7\), the last entrant receives
\[
p_6=a-\frac{1626}{929}b.
\]
All other entrant and incumbent payments are nonnegative. Hence seven is the first player count, among all \(n\leq7\), for which the unique closest voluntary Shapley implementation can require a *negative individual transfer*: this occurs precisely for \(0\leq a<1626b/929\).

The closest voluntary **componentwise nonnegative** flow at \(n=7\) is also explicit. Put \(L=1+a/(6b)\). If \(0\leq a\leq1626b/929\), then
\[
\boxed{(q_1,\ldots,q_6)=b\left(\frac12,\frac12,\frac{15(2-L)}{47},\frac{12(2-L)}{47},\frac{20(2-L)}{47},L\right).}
\]
For \(a\geq1626b/929\), the closest nonnegative flow is the unconstrained signed flow in the table. If \(D_{+}\) and \(D_{\mathrm{signed}}\) denote the squared-Euclidean Shapley-flow adjustment costs, with a factor \(1/2\), then throughout the lower-\(a\) region
\[
\boxed{D_{+}-D_{\mathrm{signed}}=
\frac{21b^2}{43663}\left(1200-929L\right)^2.}
\]
Above the threshold this cost difference is zero. In particular the correction remains finite at \(a=0\); the *existence* of a nonnegative voluntary Shapley implementation is not obstructed. The distinction is that its least-squares optimal design differs from the unrestricted signed optimum.

## Assumptions and scope

The agent set \(N\) is finite, with \(2\leq n=|N|\leq7\), and the characteristic function is exactly the pair-synergy function displayed above. A transition from a coalition of size \(k\) to one of size \(k+1\) creates \(a+bk\), divided among the entrant and the \(k\) incumbents; all outsiders receive zero. Payments are made on each edge of the coalition lattice. The terminal allocation is **expected** over uniformly random entry orders, not necessarily equal across individual realized orders. Full voluntariness is the requirement that every outsider weakly prefers immediate entry over a one-step deferral, assuming other outsiders accept when chosen, at every reachable coalition state.

The baseline Shapley flow pays the entering agent the full \(a+bk\) and pays every other agent zero. Distance to this flow is half the sum of squared payment differences over **all** directed coalition-expansion edges and all agents. Signed flows permit negative individual transfers; nonnegative flows require all payments on all edges to be nonnegative. No separate constraint is placed on allocations at intermediate coalitions. Both optimization problems retain the exact expected Shapley terminal allocation \(a+b(n-1)/2\) per agent.

## Proof

**Symmetry and reduction.** The feasible set (local budget balance, one-step entry inequalities, and a fixed expected terminal allocation) is convex, and the squared-distance objective is strictly convex. Permuting players preserves feasibility and the objective. Therefore the unique optimizer is player-symmetric, including when componentwise payment nonnegativity is imposed. A symmetric payment flow is described by one incumbent payment \(q_k\) at each level \(k\geq1\) and \(p_k=a+bk-kq_k\) for the entrant; \(p_0=a\). Conversely every such sequence is edge-budget-balanced, and by player symmetry its efficient expected terminal allocation is exactly the Shapley value.

Conditional on entering at position \(k+1\), an agent's remaining path payoff is
\[
a+b\,r_k(z),\qquad r_k(z):=k-kz_k+\sum_{\ell=k+1}^{n-1}z_\ell,
\]
where \(q_k=bz_k\), \(z_0=0\). Deferral leaves each later entry position equally likely. Thus the complete full-voluntariness system is
\[
g_k(z):=r_k(z)-\frac{\sum_{\ell=k+1}^{n-1}r_\ell(z)}{n-k-1}\geq0,
\qquad 0\leq k\leq n-2.
\tag{1}
\]
The universal-acceptance Bellman principle and the equivalence of this inequality to dynamic optimality are proved for general flows in [1, Section 3 and Proposition 5]. The objective is
\[
D(z)=\frac{b^2}{2}\sum_{k=1}^{n-1}w_k z_k^2,
\qquad w_k=\binom nk(n-k)k(k+1)>0.
\tag{2}
\]
For limited liability the additional exact constraints are
\[
0\leq z_k\leq1+\frac{a}{bk},\qquad 1\leq k\leq n-1.
\tag{3}
\]

**Exact unrestricted optimality certificates.** Define the constant vector \(c\) and the \((n-1)\)-square rational matrix \(A\) by \(c_k=g_k(0)\) and \(A_{k,j}=g_k(e_j)-c_k\), with zero-based \(k\in\{0,\ldots,n-2\}\) and one-based \(j\in\{1,\ldots,n-1\}\); \(e_j\) is the \(j\)-th unit vector. Therefore \(g(z)=Az+c\). Let \(W=\operatorname{diag}(w_1,\ldots,w_{n-1})\). For each row in the table, the exact feasible vector \(z\) satisfies the stationarity equation
\[
Wz=A_I^{\mathsf T}\lambda,
\]
where \(I\) is the set of binding inequalities \(g_k=0\) and \(\lambda\geq0\) is listed next. The entries of \(\lambda\) correspond to consecutive elements of \(I\):

| \(n\) | binding \(k\) | \(\lambda\) |
|:--:|:--|:--|
| 2 | \(0\) | \((1)\) |
| 3 | \(0,1\) | \((9/2,3/4)\) |
| 4 | \(0,1\) | \((66/5,28/5)\) |
| 5 | \(0,1\) | \((2330/71,2985/142)\) |
| 6 | \(0,1\) | \((3015/41,2388/41)\) |
| 7 | \(0,1,2\) | \((270963/1858,476175/3716,16044/929)\) |

For every row, all unlisted participation inequalities have nonnegative slack. These finite exact rational identities are reconstructed from (1)–(2), without an optimization library, by the accompanying `check.py`. Stationarity with nonnegative multipliers is sufficient for the global minimum of the convex quadratic over \(Az+c\geq0\): by expansion of the objective around \(z\), the linear term on any feasible displacement is nonnegative, and the quadratic remainder is strictly positive for every nonzero displacement. Thus all vectors in the table are uniquely globally optimal. For \(n\leq6\), \(0\leq z_k\leq1\) for every \(k\), so (3) holds for every \(a\geq0\). At \(n=7\), every component is positive, but \(z_6=1200/929>1\), with all preceding \(z_k<1\). This proves the first limited-liability boundary and the exact negative last-entrant payment.

**Exact constrained optimum at seven agents.** For \(0\leq a\leq1626b/929\), equivalently \(1\leq L\leq1200/929\), substitute the claimed six-vector into \(g=Az+c\). The first three inequalities bind. The other three slacks, in increasing order \(k=3,4,5\), are exactly
\[
\frac{8(30L-13)}{141},\qquad
\frac{285L-53}{94},\qquad
\frac{13(33L-19)}{47},
\]
all strictly positive on this interval. Every bound (3) is satisfied, and the last upper bound binds as \(z_6=L\). Exact Lagrange multipliers for consent levels \(k=0,1,2\) are
\[
\lambda_0=\frac{3(8703-3200L)}{94},\quad
\lambda_1=\frac{175(303-128L)}{188},\quad
\lambda_2=\frac{84(113-80L)}{47},
\]
while the multiplier of \(L-z_6\geq0\) is
\[
\mu=\frac{42(1200-929L)}{47}.
\]
All four are nonnegative on the entire interval. The exact stationarity identity is
\[
Wz=A_{\{0,1,2\}}^{\mathsf T}\lambda-\mu e_6.
\]
These identities, along with strict convexity and feasibility of all constraints, prove global optimality and uniqueness of the constrained flow. For \(a\geq1626b/929\), the unrestricted optimum is itself feasible and therefore solves the restricted problem. Substitution in (2) and simplification give
\[
D_{\mathrm{signed}}=\frac{1742853}{3716}b^2,
\qquad D_{+}-D_{\mathrm{signed}}
=\frac{21b^2(1200-929L)^2}{43663}.
\]
The positive gap below the threshold and zero gap at or above it are exact. This completes the stated classification for \(2\leq n\leq7\).

## Verification

The standard-library, exact-rational `check.py` reconstructs (1) and (2) directly from the payoff definition. It tests all six unrestricted primal/dual KKT certificates, the seven-agent constrained certificate at five rational parameters (including both endpoints), all asserted nonnegativity limits, and the exact difference in adjustment cost. It also evaluates terminal transfers over \(15,120\) permutation paths and independently checks \(1,623\) direct statewise Bellman consent inequalities. Its actual execution returned:

`VERIFY_OK cases=14 exact_inequalities=111 enumerated_paths=15120 direct_consent_states=1623`

The displayed rational identities and convex-optimality argument provide the proof; this finite program is a reproducibility aid, not an appeal to empirical evidence for an unbounded claim. The mathematical statement is deliberately finite in \(n\), but continuous in both real game parameters.

## Relationship to prior work

Lim [1, Section 4.1, Proposition 5] introduced the payment-flow projection and proved the **general symmetric-cardinality quadratic-program reduction** used here, including the case-by-case formulas at two and three agents. These facts are not presented as new. The contribution here is to solve the naturally motivated pair-synergy model *explicitly through its first binding nonnegativity constraint*: the rational optimal incumbent-payment tables, the sharp seven-agent first-sign boundary, the nonnegative optimum as a function of the singleton-to-pair value ratio, and the exact least-squares penalty of limited liability. These quantitative facts are not stated by that general reduction or its two-/three-player examples. General population-monotonic allocation-scheme results, including Sprumont [2], provide conceptual background for nonnegative payment constructions but do not fix the unique Shapley-distance minimizing flow or its active-set threshold. In particular, the simple feasible constant sharing rule \(q_k=b/2\) already proves **existence** of a nonnegative voluntary implementation at every \(n\); the present result is not an existence theorem.

## Limitations

The first-boundary assertion checks exactly \(2\leq n\leq7\) and makes no claim about a general closed form for arbitrary larger \(n\). It depends on the *specific* half-squared Euclidean edge norm, the uniform random-entry protocol, and symmetric pair-synergy payoffs; other adjustment norms, stochastic entry distributions, or general convex TU games need not have these thresholds. Equal residual sharing with an endogenously selected terminal allocation is a distinct problem. Equivalent parameter-specific solutions may appear in unpublished notes or unindexed numerical optimization research. This work has a self-review only; no independent audit has been performed.

## References

[1] Tongseok Lim, *Stable Allocations, Unstable Payment Paths: The Shapley Value and Voluntary Coalition Formation*, arXiv:2609.20421v1 (first public 2026-09-17), https://arxiv.org/abs/2609.20421. Relevant main text: Sections 2–5 and Appendix A.6.

[2] Yves Sprumont, *Population Monotonic Allocation Schemes for Cooperative Games with Transferable Utility*, Games and Economic Behavior **2** (1990), 378–394. DOI: 10.1016/0899-8256(90)90006-G.
