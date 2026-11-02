# Every terminal receives positive optimal reactivity on a Brownian metric star

## Finding

Let a diffusing particle start at the central vertex of a compact metric star with \(m\ge3\) arms of arbitrary lengths \(\ell_i>0\). The diffusion generator along each arm is \(D\partial_{xx}\), with continuous values and the Kirchhoff condition at the central vertex. The outer end of arm \(i\) is partially absorbing with Robin reactivity \(\kappa_i\ge0\), where \(\sum_i\kappa_i=K>0\). **The mean absorption time has exactly one globally optimal allocation, and all \(m\) optimal reactivities are strictly positive.** This holds at every finite budget and every set of positive lengths, even for extreme asymmetry.

With \(r_i=\kappa_i/D\), \(R=K/D\), write
\[
A(r)=\sum_{i=1}^m\frac{\ell_i(1+r_i\ell_i/2)}{1+r_i\ell_i},\qquad
B(r)=\sum_{i=1}^m\frac{r_i}{1+r_i\ell_i}.
\]
The central-start mean absorption time is exactly \(A(r)/(D B(r))\). Put \(V=A(r)/B(r)\). Its unique optimum is characterized by positive numbers \(V,\lambda\) satisfying
\[
r_i=\frac1{\ell_i}\left(\sqrt{\frac{\ell_i^2/2+V}{\lambda}}-1\right)>0,
\quad \sum_i r_i=R,\quad A(r)=V B(r),\quad 0<\lambda<V.
\]
These relations form an exact finite-dimensional characterization, not a claimed elementary closed form for general arm lengths.

## Assumptions and scope

The compact star has \(m\ge3\) finite arms, each parametrized by distance \(x\in[0,\ell_i]\) from the center. The diffusion coefficient \(D>0\) is the same on all arms. At the center, the backward mean-time function is continuous and \(\sum_i u_i'(0)=0\). At the terminal of arm \(i\), its Robin condition is \(u_i'(\ell_i)=-r_i u_i(\ell_i)\) where \(r_i=\kappa_i/D\). At least one reactivity is positive because \(\sum_i\kappa_i=K>0\), so killing is certain with finite mean on the compact connected star. The initial position is exactly the central junction; the result does not assert the same optimizer for arbitrary starting measures.

## Proof

**Step 1: solve the backward problem.** Write \(U=u_i(0)\) for the common expected lifetime at the central vertex. Along each arm, \(D u_i''(x)=-1\), hence \(u_i(x)=U+c_i x-x^2/(2D)\). The terminal Robin condition gives
\[
c_i=\frac{\ell_i(1+r_i\ell_i/2)/D-r_i U}{1+r_i\ell_i}.
\]
Kirchhoff flux balance \(\sum_i c_i=0\) then yields
\[
U=\frac{\displaystyle\sum_i\ell_i(1+r_i\ell_i/2)/(1+r_i\ell_i)}{D\displaystyle\sum_i r_i/(1+r_i\ell_i)}=\frac{A(r)}{D B(r)}.
\]
All terms in \(B\) are nonnegative and at least one is positive. Thus this is finite and uniquely solves the Poisson equation.

**Step 2: existence and strict uniqueness.** The budget simplex \(\mathcal S=\{r_i\ge0:\sum_i r_i=R\}\) is compact, and \(B(r)>0\) there. Let \(V_*:=\min_{r\in\mathcal S} A(r)/B(r)>0\). Define the auxiliary objective \(H_V(r)=A(r)-VB(r)\). Every summand is
\[
h_i(r_i)=\frac{\ell_i(1+r_i\ell_i/2)-Vr_i}{1+r_i\ell_i}.
\]
For every \(V>0\),
\[
h_i'(r_i)=-\frac{\ell_i^2/2+V}{(1+r_i\ell_i)^2},\qquad
h_i''(r_i)=\frac{2\ell_i(\ell_i^2/2+V)}{(1+r_i\ell_i)^3}>0.
\]
Thus \(H_{V_*}\) is strictly convex on \(\mathcal S\). Since \(H_{V_*}(r)=B(r)[A(r)/B(r)-V_*]\ge0\), and equality is attained precisely at any optimal allocation, strict convexity forces exactly one optimizer \(r_*\).

**Step 3: no inactive terminal.** Let \(\lambda>0\) be the common marginal benefit \((\ell_i^2/2+V_*)/(1+r_i\ell_i)^2\) on active coordinates. For any inactive coordinate \(j\), the one-sided first-order condition implies \(\lambda\ge \ell_j^2/2+V_*>V_*\). We now show that even \(\lambda\ge V_*\) is impossible. Indeed, for every active coordinate, this inequality implies
\[
(1+r_i\ell_i)^2\le1+\frac{\ell_i^2}{2V_*},
\qquad r_i\le \frac{\ell_i}{4V_*}.
\]
Inactive coordinates automatically satisfy the same bound, so \(R=\sum_i r_i\le\sum_i\ell_i/(4V_*)\). On the other hand, \(A(r_*)\ge\frac12\sum_i\ell_i\) and \(B(r_*)\le\sum_i r_i=R\), whence \(V_*=A(r_*)/B(r_*)\ge\sum_i\ell_i/(2R)\). Combined these inequalities would imply \(R\le R/2\), a contradiction. Therefore \(\lambda<V_*\), all optimal reactivities are strictly positive, and the stationarity equation solves uniquely for each coordinate as stated. Conversely, any positive solution of the displayed budget, consistency, and stationarity relations is the unique minimizer by strict convexity of \(H_V\) and the identity \(H_V=0\).

## Verification

The accompanying `checker.py` independently differentiates the convex auxiliary objective symbolically, tests 210 randomly parameterized stars with three through eight unequal arms against constrained numerical minimization, checks 2,520 additional feasible allocations, and verifies the lifetime lower bound. Numerical results are diagnostics only: the theorem is established by the Poisson-equation calculation and the strict-convexity/contradiction proof above.

## Relationship to prior work

Kostrykin, Potthoff, and Schrader establish Brownian motions and their generators on metric graphs (arXiv:1102.4937v1, 2011); this supplies the underlying graph-boundary framework, not a terminal-reactivity budget theorem. Singer, Schuss, Osipov, and Holcman (2008) analyze partially reflected diffusion and the Robin reaction law, but not graph-star allocation. Nicolaou and Mulder (2023) optimize flux uptake under a fixed surface-reactivity budget for exterior diffusion around convex bodies, not the central-start mean lifetime of a branched metric graph. Existing two-terminal interval allocation formulas concern a topologically different two-arm case; they do not imply a universal strict-positive optimum on an arbitrary multi-arm junction. The new contribution is the complete strict-interiority and uniqueness theorem for every heterogeneous finite star, with an exact system characterizing the optimum.

## Limitations

This claim applies to finite compact stars with \(m\ge3\), common constant diffusivity, central Kirchhoff coupling, Robin absorption only at leaves, a central point launch, and a finite strictly positive sum of reactivities. It does not establish the optimal allocation for general networks with cycles, arbitrary launches, multiple interacting particles, or spatially varying diffusion. Historical priority is based on accessible indexed and full-text sources; unindexed equivalent optimizations cannot be excluded. Independent validation has not been performed.

## References

1. V. Kostrykin, J. Potthoff, R. Schrader, *Brownian Motions on Metric Graphs*, arXiv:1102.4937v1 (2011), https://arxiv.org/abs/1102.4937.
2. A. Singer, Z. Schuss, A. Osipov, D. Holcman, *Partially Reflected Diffusion*, SIAM Journal on Applied Mathematics **68** (2008), 844–868, https://doi.org/10.1137/060663258.
3. K. Nicolaou, B. M. Mulder, *A probabilistic algorithm for optimising the steady-state diffusional flux into a partially absorbing body*, Scientific Reports **13** (2023), 22815, https://doi.org/10.1038/s41598-023-49566-4.
