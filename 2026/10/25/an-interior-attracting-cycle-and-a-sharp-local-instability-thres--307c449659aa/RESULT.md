# An interior attracting cycle and a sharp local instability threshold in asymmetric lottery contests

## Finding

Consider a two-player proportional-prize lottery contest with linear effort costs \(1\) and \(c\), and deterministic alternating exact best replies. There is an **open cost-asymmetry interval strictly above the previously identified reset-cycle bound** in which the unique Nash equilibrium is repelling and there is a positive prime-two orbit of the two-move return map. In particular:

1. For every \(4/25<c<3-2\sqrt{2}\), the two-move return map has a nonconstant prime-two orbit entirely in its positive, smoothly defined region. Thus the original unilateral best-response sequence has a nontrivial four-move cycle and never needs a reply to zero rival effort.
2. For \(4/25<c<1\), the unique positive Nash equilibrium is locally attracting when \(c>3-2\sqrt{2}\) and locally repelling when \(c<3-2\sqrt{2}\). The borderline \(c=3-2\sqrt{2}\) is nonhyperbolic; no stability conclusion at equality is asserted.
3. At the exact rational cost ratio \(c=1/6\), at least one positive four-move cycle is **locally attracting**. Its existence, strict interiority and attraction have a standalone exact-rational interval certificate.

These are properties of actual one-at-a-time best-response updates, not of a continuous-time approximation. The result does not assert global convergence or a complete classification of periodic attractors.

## Assumptions and scope

For \(x,y\ge0\) with \(x+y>0\), the two payoffs are
\[
u_1(x,y)=\frac{x}{x+y}-x,\qquad u_2(x,y)=\frac{y}{x+y}-cy,
\]
where the prize has value one and \(0<c<1\). Player 1 has unit marginal cost, player 2 has marginal cost \(c\). Players alternate, with player 1 revising first after a recorded revision of player 2. When the opponent's effort is positive, a player's unique exact best reply is
\[
B_1(y)=\max\{0,\sqrt y-y\},\qquad
B_2(x)=\max\{0,\sqrt{x/c}-x\}.
\]
The original literature uses a small positive action to resolve the undefined best response when the opponent produces zero. No such convention enters any constructed orbit: every individual effort on it is strictly positive.

For \(4/25<c<1\) and \(0<y<1\), define \(b(y)=\sqrt y-y\) and
\[
F_c(y)=\sqrt{b(y)/c}-b(y).
\]
This records player 2's effort after one update by each player: \(y_{k+1}=F_c(y_k)\); one iterate of \(F_c\) represents two unilateral moves. Endpoint values used below are limits, not best replies at zero opponent effort.

## Proof

**Invariant positive interval.** For \(0<y<1\), \(0<b(y)\le1/4\). Since \(c<1\), the function \(z\mapsto\sqrt{z/c}-z\) is strictly increasing on \((0,1/4]\), as its derivative is at least \(1/\sqrt c-1>0\). It is positive there, and
\[
0<F_c(y)\le\frac1{2\sqrt c}-\frac14<1
\quad\Longleftrightarrow\quad c>\frac4{25}.
\]
Thus \(F_c\) maps \((0,1)\) strictly into itself for the claimed cost ratios. Every successive effort is then positive; in particular neither player takes a best response to zero effort.

**Fixed point and sharp local threshold.** Any positive fixed point of \(F_c\) gives mutual best responses \(x=b(y)\) and \(y=B_2(x)\). Write \(s=x+y\). The two first-order conditions of the strictly concave unilateral payoffs give \(y=s^2\) and \(x=cs^2\). Therefore \(s=1/(1+c)\), and the only interior fixed point is
\[
y_*=\frac1{(1+c)^2},\qquad x_*=\frac{c}{(1+c)^2}.
\]
Conversely this pair is indeed interior and solves both best-response equations. Direct differentiation yields
\[
B_1'(y_*)=\frac{c-1}{2},\qquad
B_2'(x_*)=\frac{1-c}{2c},\qquad
F_c'(y_*)=-\frac{(1-c)^2}{4c}.
\]
For \(0<c<1\), the modulus of this multiplier exceeds one exactly when \(c<3-2\sqrt2\), equals one at that threshold, and is below one above it. The standard differentiable one-dimensional local stability criterion proves the asserted hyperbolic classifications.

**Nontrivial interior period-two orbit throughout the window.** Fix \(4/25<c<3-2\sqrt2\). Although the endpoint best replies are not needed, \(F_c\) admits a continuous extension to \([0,1]\) with \(F_c(0)=F_c(1)=0\). Its asymptotics at the left endpoint are
\[
F_c(y)\sim c^{-1/2}y^{1/4},\qquad
F_c(F_c(y))\sim c^{-5/8}y^{1/16}\quad (y\downarrow0).
\]
Hence \(G_c(y):=F_c(F_c(y))-y\) is positive for all sufficiently small positive \(y\). At the unique interior fixed point, \(G_c(y_*)=0\), while
\[
G_c'(y_*)=\bigl(F_c'(y_*)\bigr)^2-1>0.
\]
Therefore \(G_c\) is negative immediately to the left of \(y_*\) and positive immediately to its right. As \(y\uparrow1\), \(F_c(y)\to0\) and \(F_c(F_c(y))\to0\), so \(G_c(y)\to-1\). The intermediate value theorem yields roots of \(G_c\) in both \((0,y_*)\) and \((y_*,1)\). Any such root \(z\ne y_*\) has \(F_c^2(z)=z\); since \(y_*\) is the sole positive fixed point of \(F_c\), it belongs to a genuine period-two orbit. Both orbit points lie in \((0,1)\) by the invariant-interval argument.

**Certified attracting example.** Set \(c=1/6\) and \(J=[26299/100000,26300/100000]\). The exact rational interval verifier accompanying this result proves
\[
\begin{aligned}
 3\cdot10^{-6}&<F_c^2(26299/100000)-26299/100000<4\cdot10^{-6},\\
-6\cdot10^{-6}&<F_c^2(26300/100000)-26300/100000<-5\cdot10^{-6},\\
 F_c(J)&\subset (97447/100000,97455/100000),\\
 17/100&<(F_c^2)'(J)<18/100.
\end{aligned}
\]
Here the last inequality holds for every point of \(J\), not merely at the endpoints. Each bound is obtained by rational interval arithmetic with conservative integer-square-root enclosure; thus floating-point rounding is not a premise. The first two bounds and continuity yield a fixed point \(z\in J\) of \(F_c^2\). Since \(F_c(J)\) is disjoint from \(J\), this point is not fixed by \(F_c\). The derivative bound proves that its prime-two orbit is locally attracting. Every unilateral effort on the orbit is positive.

## Verification

Run `python verify_lottery_cycle.py` with a standard Python installation. The script constructs exact rational intervals; for a nonnegative rational \(r\), its square-root enclosure is obtained by integer square root at scale \(10^{24}\), rounded outward. Assertions certify all four displayed interval inequalities, disjointness of the two cycle neighborhoods, and an attracting two-iterate derivative. No numerical ODE or Monte Carlo output is used as an infinite proof.

The period-two existence for every cost ratio in the open window and the local-stability boundary are analytical consequences of the preceding equations. The exact-rational computation is required only for the specific attracting witness \(c=1/6\), not for the general existence theorem.

## Relationship to prior work

Ghosh and Goldberg [1] define the lottery-contest best-response process, prove rapid convergence for homogeneous contestants, construct heterogeneous cycles that pass through a zero-output reply, and give \(4/25\) as an illustrative heterogeneity bound; their discussion reports numerical convergence above that bound and leaves near-homogeneous costs open. The present nonzero-effort cycles occupy the previously unestablished interval \((4/25,3-2\sqrt2)\); the attracting witness is inside that interval.

Ghosh [2] studies convex costs and exhibits a heterogeneous positive-effort cycle for a different strictly convex contest. It does not supply the linear-cost ratio threshold or the positive-effort cycle for \(c=1/6\). Elkind, Ghosh and Goldberg [3] establish convergence for continuous-time and suitably damped best-response procedures, not for undamped alternating exact replies. Ewerhart [4] studies the best-response potential property in the common-valuation homogeneous-cost lottery contest, which does not imply convergence in the present heterogeneous game. No general uniqueness or full phase classification is claimed.

## Limitations

The upper local-stability threshold concerns the Nash fixed point, not global convergence. The existence theorem does not assert that all positive starting states approach a cycle or that there is exactly one periodic orbit. The certified attracting witness is for \(c=1/6\); attraction for every parameter in the open interval is not established. The dynamics at the neutral threshold \(3-2\sqrt2\), below \(4/25\), and for other cost models is not classified. The result is for exact alternating best response, not simultaneous or continuous-time revisions. Independently checking equivalently transformed contest or Cournot models remains a bibliographic risk.

## References

[1] A. Ghosh and P. W. Goldberg, *Best-Response Dynamics in Lottery Contests*, arXiv:2305.10881, first submitted 2023-05-18, sections 2--4 and appendix; https://arxiv.org/html/2305.10881v1 .

[2] A. Ghosh, *Best-Response Dynamics in Tullock Contests with Convex Costs*, arXiv:2310.03528, 2023-10-05, section 1 and Appendix A; https://arxiv.org/abs/2310.03528 .

[3] E. Elkind, A. Ghosh and P. W. Goldberg, *Continuous-Time Best-Response and Related Dynamics in Tullock Contests with Convex Costs*, arXiv:2402.08541, first submitted 2024-02-13, sections 3--5; https://arxiv.org/abs/2402.08541 .

[4] C. Ewerhart, *The lottery contest is a best-response potential game*, Economics Letters 155 (2017), 168--171; https://doi.org/10.1016/j.econlet.2017.03.030 .
