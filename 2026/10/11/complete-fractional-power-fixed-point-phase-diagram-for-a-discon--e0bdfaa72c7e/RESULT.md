# Complete fractional-power fixed-point phase diagram for a discontinuous interval family

## Finding
For the two-branch interval map in the next section, write
\[
L(b,d)=\frac{b^d(1-b)^{1-d}}{d^d(1-d)^{1-d}},\qquad
R(b,d)=\frac{(1-b)^d b^{1-d}}{d^d(1-d)^{1-d}}.
\]
For every \(a,b,c\in(0,1)\) and \(d\in(0,1)\), its number \(N\) of distinct real fixed points in \([0,1]\) is exactly \(N=N_L+N_R\), where
\[
N_L=\begin{cases}
2,&b>d\ \text{and}\ 1-a>L(b,d),\\
1,&b>d\ \text{and}\ 1-a=L(b,d),\\
0,&\text{otherwise},
\end{cases}
\qquad
N_R=\begin{cases}
2,&b<1-d\ \text{and}\ c>R(b,d),\\
1,&b<1-d\ \text{and}\ c=R(b,d),\\
0,&\text{otherwise}.
\end{cases}
\]
Each equality case gives exactly one interior, multiplier-one saddle-node fixed point, at
\[
x_L^*=\frac{b-d}{1-d}\quad\text{or}\quad x_R^*=\frac{b}{1-d},
\]
respectively. In each strict two-root case the lower left fixed point is attracting and the upper left is repelling; the lower right is repelling and the upper right attracting. The maximum number of fixed points is four, attained exactly when
\[
0<d<\frac12,\qquad d<b<1-d,\qquad
1-a>L(b,d),\qquad c>R(b,d).
\]
Every count \(0,1,2,3,4\) occurs for admissible parameters; the maximal bound four is attained, for example, at \((a,b,c,d)=(1/20,1/2,19/20,1/4)\).

## Assumptions and scope
The map, introduced as Equation (15) in Lawnik--Moysis--Volos (2023), is the discontinuous increasing-branch map
\[
f_{a,b,c,d}(x)=\begin{cases}
1-(1-a)\left(\dfrac{b-x}{b}\right)^d,&0\le x\le b,\\
c\left(\dfrac{x-b}{1-b}\right)^d,&b<x\le1.
\end{cases}
\]
The domain is precisely \([0,1]\); \(0<a,b,c<1\) and \(0<d<1\). The switching point \(x=b\) belongs to the left branch, whose value there is one, while the right-hand limit is zero. Neither \(x=0\), \(x=b\), nor \(x=1\) is fixed. Stability refers only to the local one-dimensional dynamics near an interior fixed point, not global basins or chaoticity. The parent paper proves the separate fixed-point-free statement for \(d\ge1\); the present claim classifies the complementary fractional-power regime.

## Proof
**Left branch.** Set \(A=1-a\in(0,1)\) and \(u=(b-x)/b\in[0,1]\). The fixed-point equation becomes \(H_L(u)=0\) for
\[
H_L(u)=1-b+bu-Au^d.
\]
For \(0<d<1\), \(H_L\) is strictly convex on \((0,1)\), with \(H_L(0)=1-b>0\) and \(H_L(1)=a>0\), so it has at most two interior zeros. If \(b\le d\), the tangent-line inequality \(u^d\le1-d+du\) gives
\[
H_L(u)>1-b+bu-(1-d+du)=(d-b)(1-u)\ge0
\]
for interior \(u\); positivity at both endpoints was already established. Hence there are no left roots.

When \(b>d\), the number
\[
u_L=\frac{d(1-b)}{b(1-d)}\]
lies strictly between zero and one. Simultaneous equations \(H_L(u_L)=H_L'(u_L)=0\) have the unique coefficient \(A=L(b,d)\). At this coefficient strict convexity and tangency force a unique zero at \(u_L\), corresponding to \(x_L^*=(b-d)/(1-d)\). Decreasing \(A\) strictly raises \(H_L(u)\) at every interior point, eliminating all roots; increasing \(A\) makes \(H_L(u_L)<0\), giving one root on either side of \(u_L\) by the endpoint signs and strict convexity. These changes occur inside the admissible interval because \(L(b,d)<1\) when \(b>d\), by strict weighted arithmetic-geometric mean inequality.

**Right branch.** Set \(v=(x-b)/(1-b)\in(0,1]\). The fixed-point equation is \(H_R(v)=0\), where
\[
H_R(v)=cv^d-b-(1-b)v.
\]
It is strictly concave, with \(H_R(0)=-b<0\) and \(H_R(1)=c-1<0\). For \(b\ge1-d\), the same tangent inequality gives \(H_R(v)<(1-d-b)(1-v)\le0\) for interior \(v\), hence no roots. For \(b<1-d\), set \(v_R=db/((1-b)(1-d))\in(0,1)\). The equations \(H_R(v_R)=H_R'(v_R)=0\) hold precisely at \(c=R(b,d)\); strict concavity gives one tangency root there, zero below, and two above, again all interior. The location is \(x_R^*=b/(1-d)\). The strict inequalities \(L(b,d),R(b,d)<1\) in their respective existence ranges follow from the weighted arithmetic-geometric mean inequality, so all stated phases are realizable in the open parameter box.

**Types and maximality.** Both branch maps have strictly positive derivatives. For \(d<1\), the left branch has positive second derivative and the right branch negative second derivative. At a strict left two-root configuration, the derivative crosses one from below to above as the fixed point moves right, so the smaller left fixed point has multiplier in \((0,1)\) and the larger exceeds one. On the right, the derivative crosses one from above to below, reversing these roles. At tangency the multiplier is exactly one, second derivative is nonzero, and variation of \(a\), respectively \(c\), changes the fixed-point equation with nonzero derivative; these are generic one-parameter saddle-nodes. The left tangency is attracting from below and repelling from above; the right tangency attracts from above and repels from below. Two roots on both branches require simultaneously \(b>d\) and \(b<1-d\), possible exactly for \(d<1/2\). Thus the displayed four-root criterion is necessary and sufficient. With \(d=1/4\), \(b=1/2\), the two thresholds coincide at \((16/27)^{1/4}\in(0,1)\). Independently choosing \(1-a\) and \(c\) below, at, or above that threshold realizes every total count from zero through four.

## Verification
At \((a,b,c,d)=(1/20,1/2,19/20,1/4)\), both threshold inequalities are strict because \((19/20)^4>16/27\). Substituting \(t=u^{1/4}\) on the left and \(t=v^{1/4}\) on the right makes each fixed-point equation the same polynomial equation
\[
10t^4-19t+10=0,\qquad 0<t<1.
\]
The polynomial is positive at \(t=0,1\), equals \(-139/128\) at \(t=3/4\), and has strictly increasing derivative on \(t>0\); therefore it has exactly two roots in \((0,1)\), one for each side of the negative interior value. The roots correspond to two distinct left points and two distinct right points. The separate script `verify.py` checks the rational sign certificate and threshold inequalities with exact fractions, and compares the source's illustrated fixed-point-free parameter example. It does not prove the universal theorem; that follows from the convexity and concavity arguments above.

## Relationship to prior work
Lawnik, Moysis, and Volos (2023), Equation (15), introduce exactly this family. Their Lemma 1 proves absence of fixed points for \(d\ge1\). Remark 4 expressly discusses \(d<1\), notes that existence then depends on parameters, and supplies selected numerical examples without an analytical threshold. The present complete fractionally powered phase diagram, two explicit saddle-node hypersurfaces, sharp count bound, and local stability ordering concern the complementary regime. Their general observation that fixed points are intersections with the identity line is used, but does not itself give the closed all-parameter classification. Berezowski--Lawnik (2021) investigate hidden attractors arising from Newton recursions and discretization, a different map. The later Lawnik--Moysis--Baptista--Volos (2024) paper describes a different transformation method and logistic/tent-derived constructions in its publicly readable abstract; its full text was not available for substantive comparison, so any claim of exhaustive publication priority is qualified. The present result requires no assumption that nonexistence of a fixed point implies chaos.

## Limitations
The theorem classifies fixed points and their local one-sided/linear behavior, not periodic points of period greater than one, global basins, Lyapunov exponents, entropy, or cryptographic suitability. The endpoint parameter cases \(a,b,c\in\{0,1\}\) and \(d\in\{0,1\}\) are excluded. The comparison with the full text of the 2024 follow-up could not be completed; this leaves a residual literature-priority risk despite the different construction described in its abstract. The fixed-point count is an exact analytical conclusion, not an experimentally inferred census.

## References
1. M. Lawnik, L. Moysis, C. Volos, *A Family of 1D Chaotic Maps without Equilibria*, Symmetry **15** (2023), 1311. DOI: 10.3390/sym15071311. Equation (15), Lemma 1, Remark 4. First public release: 27 June 2023.
2. M. Lawnik, L. Moysis, M. S. Baptista, C. Volos, *Discrete one-dimensional piecewise chaotic systems without fixed points*, Nonlinear Dynamics **112** (2024), 6679–6693. DOI: 10.1007/s11071-024-09349-6. Abstract and bibliographic material inspected; full text unavailable.
3. M. Berezowski, M. Lawnik, *Hidden Attractors in Discrete Dynamical Systems*, Entropy **23** (2021), 616. DOI: 10.3390/e23050616. Distinct recurrence families.
