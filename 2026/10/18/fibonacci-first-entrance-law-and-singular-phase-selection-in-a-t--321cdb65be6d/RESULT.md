# Fibonacci first-entrance law and singular phase selection in a tent map with memory

## Finding

For the critical half-memory tent system of Góra, Boyarsky, Li, and Proppe, let
\[
G(x,y)=\left(y,\tau\!\left(\frac{x+y}{2}\right)\right),\qquad
\tau(t)=\begin{cases}2t,&0\le t\le 1/2,\\2-2t,&1/2\le t\le1.\end{cases}
\]
Its upper triangle \(P=\{(x,y)\in[0,1]^2:x+y\ge1\}\) is pointwise periodic under \(G^3\). For a random initial point with uniform area distribution on the square, let \(T=\min\{n\ge0:G^n(x,y)\in P\}\). If \(F_0=0,F_1=1,F_{n+2}=F_{n+1}+F_n\), then, for all integers \(n\ge1\),
\[
\mathbb P(T\ge n)=\frac1{2F_nF_{n+1}},\qquad
\mathbb P(T=n)=\frac1{2F_nF_{n+2}},\qquad
\mathbb P(T=0)=\frac12.
\]
Thus the *entire* transient-time distribution, not just eventual periodicity, is determined by Fibonacci numbers.

There is also a universal landing-phase law. Let \(h\) be any probability density on the square continuous at the origin with \(h(0,0)>0\), write \(\varphi=(1+\sqrt5)/2\), and let \((X_T,Y_T)=G^T(X_0,Y_0)\). Conditional on \(T=n\),
\[
(X_T,Y_T)\ \Longrightarrow\ (U/\varphi,U),
\]
where \(U\) is supported on \([\varphi^{-1},1]\) with density
\[
\frac{2u}{1-\varphi^{-2}}\,\mathbf 1_{[\varphi^{-1},1]}(u).
\]
This is a singular entrance law on the line \(y=\varphi x\), independent of \(h\). Moreover,
\[
\mathbb P_h(T\ge n)\sim\frac{5h(0,0)}{2\varphi}\varphi^{-2n},\qquad
\mathbb P_h(T=n)\sim\frac{5h(0,0)}{2\varphi^2}\varphi^{-2n}.
\]
Consequently \(\mathbb E_h[e^{sT}]<\infty\) if and only if \(s<2\log\varphi\). The assertions include every integer \(n\) where stated, and the limit law is weak convergence for bounded continuous test functions.

## Assumptions and scope

The state space is \([0,1]^2\); the branch switch is at \(x+y=1\), with the equality assigned to \(P\). Only the fixed parameter \(\alpha=1/2\) is considered. The initial distribution for the exact formulas is normalized two-dimensional Lebesgue measure; the asymptotic and weak-limit statements permit any nonnegative, integrable density \(h\) with total integral one, continuity at \((0,0)\), and \(h(0,0)>0\). Probabilities below refer to randomness of the *initial state*, not to random iteration. The origin has infinite entrance time but zero probability under every such density.

## Proof

**1. The periodic region and first-passage reduction.** If \(x+y\ge1\), then \(G(x,y)=(y,2-x-y)\), and direct substitution gives \(G^2(x,y)=(2-x-y,x)\) and \(G^3(x,y)=(x,y)\). All three states belong to \(P\). If \(x+y<1\), then \(G(x,y)=A(x,y)\) with \(A(x,y)=(y,x+y)\). While the orbit remains outside \(P\), both coordinates are nonnegative and the coordinate sum strictly increases except along the boundary \(y=0\). In particular, no earlier branch switch is possible when the final linear-branch sum is still below one.

**2. Exact Fibonacci survivor triangles.** Matrix induction gives, for every integer \(k\ge1\),
\[
A^k=\begin{pmatrix}F_{k-1}&F_k\\F_k&F_{k+1}\end{pmatrix},\qquad
(A^k(x,y))_1+(A^k(x,y))_2=F_{k+1}x+F_{k+2}y.
\]
Because successive sums increase on the nonnegative cone, for every \(n\ge1\),
\[
\{T\ge n\}=\{(x,y)\in[0,1]^2:F_nx+F_{n+1}y<1\}.
\]
Its two intercepts are \(1/F_n\) and \(1/F_{n+1}\), both at most one. Thus its area is exactly \((2F_nF_{n+1})^{-1}\). The first-hit region is the difference of two nested survivor triangles. Using \(F_{n+2}-F_n=F_{n+1}\), its area is
\[
\frac1{2F_nF_{n+1}}-\frac1{2F_{n+1}F_{n+2}}=\frac1{2F_nF_{n+2}}.
\]
Half of the initial square is already in \(P\), giving \(\mathbb P(T=0)=1/2\). The nested triangles shrink to the origin, establishing finite entrance almost everywhere.

**3. General-density tails and exponential moments.** The survivor triangles have diameter \(O(F_n^{-1})\), so continuity at the origin implies \(h(x,y)=h(0,0)+o(1)\) uniformly on them. Their weighted masses, and the masses of the included first-hit bands, equal \(h(0,0)(1+o(1))\) times their respective areas. Binet's formula gives \(F_n=\varphi^n/\sqrt5\,(1+O(\varphi^{-2n}))\). Substitution yields the displayed constants. Since the first-hit probabilities are asymptotic to a positive multiple of \(\varphi^{-2n}\), comparison with a geometric series proves the exact exponential-moment threshold, including divergence at equality.

**4. Singular landing law.** On \(T=n\), put \(u=F_nx\) and \(v=F_{n+1}y\). The entry-event polygon, up to boundary points, is
\[
R_n=\left\{u,v\ge0:\ u+v<1,\quad
\frac{F_{n+1}}{F_n}u+\frac{F_{n+2}}{F_{n+1}}v\ge1\right\}.
\]
Under the coordinate change, conditional density is proportional to \(h(u/F_n,v/F_{n+1})\mathbf 1_{R_n}\). Fibonacci ratios converge to \(\varphi\); the sets \(R_n\) consequently converge, in area and almost everywhere, to
\[
R_\infty=\{u,v\ge0:\varphi^{-1}\le u+v\le1\}.
\]
The density factor tends uniformly to the positive constant \(h(0,0)\). Dominated convergence therefore gives normalized uniform area on \(R_\infty\). Also the actual landing state at time \(n\) is
\[
(X_n,Y_n)=\left(\frac{F_{n-1}}{F_n}u+\frac{F_n}{F_{n+1}}v,\ u+v\right),
\]
which tends uniformly on the unit simplex to \(((u+v)/\varphi,u+v)\). Finally, the length of the intersection of \(R_\infty\) with \(u+v=t\), expressed in \((t,u)\) coordinates of Jacobian one, is \(t\). Normalizing \(\int_{\varphi^{-1}}^1t\,dt=(1-\varphi^{-2})/2\) proves the stated limiting density. No finite-time distribution is asserted to be supported on the limiting line.

## Verification

The standalone `verify.py` uses Python standard-library exact fractions and independent rational polygon clipping. For each \(1\le n\le19\), it constructs the survivor triangle and first-hit polygon inside the square by half-plane intersections, computes both shoelace areas, and compares them to the two Fibonacci formulas exactly. It also propagates vertices through the linear recurrence to confirm the exit inequalities and reports the predicted limiting entrance-coordinate mean. Execute with `python3 verify.py`; the expected final line is `VERIFY_OK`. The interval-by-interval and infinite-time assertions are established above analytically; finite computations are corroborative only.

## Relationship to prior work

Góra, Boyarsky, Li, and Proppe proved in their April 2016 manuscript, Section 7.1, that this half-memory map is already 3-periodic on the upper triangle and that all other points except the origin eventually reach it. They gave the expanding linear recursion below that triangle. Those results are the foundational input and are **not** claimed as new. The present result instead specifies the complete Lebesgue first-entrance distribution and derives the universal singular conditional distribution of landing locations for arbitrary continuous positive source densities, together with its sharp moment threshold. The same authors' July 2016 sequel studies the parameter interval \(3/4<\alpha<1\) and does not furnish the stated half-memory first-entrance law. Related published first-exit calculations for other piecewise maps do not imply these Fibonacci constants or the ray-selection law for this map.

## Limitations

This concerns \(\alpha=1/2\) only and probabilities over initial states. It is not a distribution for a stationary invariant measure (the initial uniform measure need not be invariant), and the weak limit is not a total-variation convergence to a singular measure. Densities vanishing or singular at the origin can have different tail exponents. The proof does not assert a parameter-uniform law as \(\alpha\to1/2\), nor absolute priority over every unindexed general first-passage theorem.

## References

1. P. Góra, A. Boyarsky, Z. Li, H. Proppe, *Statistical and Deterministic Dynamics of Maps with Memory*, arXiv:1604.06991v1 (public 2016-04-24), especially Section 7.1. https://arxiv.org/abs/1604.06991
2. P. Góra, A. Boyarsky, Z. Li, *Singular SRB measures for a non 1--1 map of the unit square*, arXiv:1607.01658v1 (public 2016-07-06), Introduction and parameter-scope statement. https://arxiv.org/abs/1607.01658
