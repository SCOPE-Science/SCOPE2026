# A sharp global convergence boundary for asymmetric lottery-contest best responses

## Finding

In the two-player linear-cost lottery contest with costs \(1\) and \(c\), respectively, normalize the prize to one. Let the players alternate exact best responses, with the cost-one player updating first in each round. Assume \(4/25<c\leq1\) and initial positive effort \(0<y_0<1\) of the cost-\(c\) player; the other player's initial effort can be arbitrary because it is replaced on the first move.

Write \(c_*=3-2\sqrt2\). **Every resulting trajectory converges to the unique positive Nash equilibrium if and only if \(c\geq c_*\).** When \(4/25<c<c_*\), the smooth two-move return map has **exactly one** positive primitive period-two orbit, so alternating best responses admit a strictly positive four-move cycle. When \(c\geq c_*\), no nontrivial period-two orbit exists and *every* initial effort \(y_0\in(0,1)\) converges to the Nash value \(y_*=1/(1+c)^2\). At equality \(c=c_*\), convergence is asserted without an exponential-rate claim.

This is a global convergence and exact period-two classification **within the specified smooth positive-effort regime**. It is not a classification of behavior at initial zero or large effort, where the model's zero-opponent rule may enter.

## Assumptions and scope

Each player chooses a nonnegative effort. For positive total effort, payoffs are
\[
 u_1(x,y)=\frac{x}{x+y}-x,\qquad
 u_2(x,y)=\frac{y}{x+y}-cy.
\]
For positive opponent effort, exact best responses are
\[
 B_1(y)=\max\{0,\sqrt y-y\},\qquad
 B_2(x)=\max\{0,\sqrt{x/c}-x\}.
\]
Only the smooth branches are used below: \(y\in(0,1)\) and \(x\in(0,1/4]\). A round first sets \(x=B_1(y)\), then sets \(y^+=B_2(x)\). Its return map is
\[
 F_c(y)=\sqrt{\frac{\sqrt y-y}{c}}-(\sqrt y-y),\quad 0<y<1.
\]
For \(4/25<c\leq1\), \(B_2\) is increasing on \([0,1/4]\), and
\[
 0<F_c(y)\leq F_c(1/4)=\frac{1}{2\sqrt c}-\frac14<1.
\]
Thus every positive orbit remains in \((0,1)\), and the displayed map extends continuously to \([0,1]\) by setting \(F_c(0)=F_c(1)=0\). The endpoint extension is only a mathematical device, not a claim that a player's best response is attained against exactly zero opposing effort.

## Proof

**1. Fixed points and local threshold.** At a positive fixed point, set \(x=B_1(y)\) and \(y=B_2(x)\). The best-response identities imply
\[
 (x+y)^2=y,\qquad c(x+y)^2=x.
\]
Therefore \(x=cy\), and the unique positive fixed point is
\[
 (x_*,y_*)=\left(\frac{c}{(1+c)^2},\frac1{(1+c)^2}\right).
\]
Differentiation gives
\[
 F_c'(y_*)=-\frac{(1-c)^2}{4c}.
\]
Its magnitude exceeds one precisely when \(c<c_*=3-2\sqrt2\) in \((0,1]\).

**2. Every primitive two-cycle obeys one quadratic constraint.** Suppose \(F_c(u)=v\), \(F_c(v)=u\), and \(0<u<v<1\). Write \(a=B_1(u)\), \(b=B_1(v)\), \(S=a+b+u+v\), \(\delta=v-u>0\), and \(\alpha=a-b\). From
\[
 (a+u)^2=u,\quad (b+v)^2=v,\quad
 c(a+v)^2=a,\quad c(b+u)^2=b,
\]
subtracting in pairs yields
\[
 (\alpha-\delta)S=-\delta,\qquad
 c(\alpha+\delta)S=\alpha.
\]
Eliminating \(\alpha\), using \(S>0\), gives
\[
 P_c(S):=2cS^2-(1+c)S+1=0. \tag{1}
\]
Moreover Cauchy--Schwarz applied separately to the two pairs of squares above shows
\[
 u+v\geq S^2/2,\qquad a+b\geq cS^2/2.
\]
Both equalities cannot hold for a primitive orbit (together they force \(u=v\)). Hence
\[
 S<\frac2{1+c}. \tag{2}
\]
The discriminant of \(P_c\) is \(\Delta(c)=c^2-6c+1\). For \(c>c_*\), it is negative; for \(c=c_*\), the double root equals \(2/(1+c)\) and violates (2). Thus **no positive primitive two-cycle exists at or above \(c_*\)**.

**3. Global convergence at and above the boundary.** The continuous extension \(F_c:[0,1]\to[0,1]\) has no primitive period-two points: the only points with \(F_c^2(y)=y\) besides positive interior candidates are the fixed endpoint \(y=0\); \(y=1\) maps to zero. Coppel's interval-iteration theorem states that a continuous self-map of a compact real interval with no primitive period-two orbit has convergent iterates from every starting point. Applying this theorem shows \(F_c^n(y_0)\) converges to a fixed point. The only fixed points of the extension are \(0\) and \(y_*\). But as \(y\downarrow0\),
\[
 F_c(y)\sim c^{-1/2}y^{1/4},
\]
so \(F_c(y)>y\) throughout some punctured neighborhood of zero. A strictly positive orbit cannot converge to zero, because it would eventually be strictly increasing. Its limit is therefore \(y_*\); continuity of \(B_1\) yields \(x\to x_*\). The equality case \(c=c_*\) is included in the absence-of-two-cycles argument.

**4. Sharp failure below the boundary.** Suppose \(4/25<c<c_*\). Let \(G(y)=F_c^2(y)-y\). As \(y\downarrow0\),
\[
 F_c^2(y)\sim c^{-5/8}y^{1/16},
\]
so \(G(y)>0\) for sufficiently small positive \(y\). At \(y_*\), \(G(y_*)=0\) and \(G'(y_*)=F_c'(y_*)^2-1>0\). Hence \(G\) is negative immediately to the left of \(y_*\) and positive immediately to its right. The intermediate value theorem supplies a root in \((0,y_*)\) distinct from any fixed point, and therefore a positive primitive two-cycle. Since \(F_c:(0,1)\to(0,1)\), this cycle never invokes the zero-opponent response. Starting on it precludes convergence to the equilibrium.

**5. Uniqueness of the primitive orbit.** For \(4/25<c<c_*\), the quadratic \(P_c\) has two real roots. Evaluate it at the strict bound in (2):
\[
 P_c\!\left(\frac2{1+c}\right)
 =-\frac{c^2-6c+1}{(1+c)^2}<0.
\]
Thus its larger root lies *above* \(2/(1+c)\), violating (2). Only the smaller root is possible:
\[
 S=S_-(c)=\frac{1+c-\sqrt{c^2-6c+1}}{4c}.
\]
For this fixed \(S\), the equations already obtained give \(\alpha=\delta(S-1)/S\). Adding the four best-response square identities yields
\[
 \delta^2=
 \frac{S^2\bigl(2S-(1+c)S^2\bigr)}
 {1+c(2S-1)^2}. \tag{3}
\]
The right-hand side is positive by (2), and \(\delta>0\) fixes its square root. Also
\[
 u+v=\frac12\left(S^2+\frac{\delta^2}{S^2}\right).
\]
Consequently \(u\) and \(v\), and then \(a\) and \(b\), are uniquely determined. The existence proved in step 4 completes the claim: there is **exactly one unordered primitive two-cycle** in this parameter band.

## Verification

The general proof is analytic: the absence of period-two points is an algebraic deduction, and the global-convergence step invokes the precisely stated interval theorem of Coppel. The included `verify.py` uses exact symbolic arithmetic to check the quadratic discriminant, the strict-bound evaluation, and an explicit positive cycle at \(c=1/6\). In that example the four best-response square identities are exact and the two-return multiplier is \(43/243\). Run `python verify.py` after installing `requirements.txt`. A finite symbolic check of this example is not a proof of the universal threshold theorem.

## Relationship to prior work

Ghosh and Goldberg (2023, Section 3 and Conclusion) construct nonconvergent alternating best-response examples when \(c\leq4/25\), report simulations suggesting convergence for \(c>4/25\), and explicitly leave the allowable heterogeneity for convergence as an open direction. An existing narrower analysis in the same model establishes an interior cycle below \(c_*\) and the local multiplier, but does not establish **global convergence for every positive initial effort at or above \(c_*\)** nor **uniqueness of all interior primitive two-cycles below it**. These are the advances here. Ewerhart's (2017) best-response potential concerns homogeneous contests and does not imply the heterogeneous boundary. Coppel (1955) supplies a general interval theorem; the special algebraic exclusion of all two-cycles in this contest is needed to invoke it.

## Limitations

The domain is \(4/25<c\leq1\) with \(0<y_0<1\), positive interior exact best replies and a fixed alternating update order. Initial configurations activating the model's zero-opponent convention, player-specific strategy constraints, more than two players, and changed contest-success functions are not covered. Above the threshold no uniform convergence rate is asserted; at the critical value the local multiplier is \(-1\). Below the threshold the proof does not classify higher-period or chaotic dynamics or claim global attraction to the unique two-cycle. Publication priority beyond the inspected literature remains subject to independent bibliographic confirmation.

## References

1. A. Ghosh and P. W. Goldberg, *Best-Response Dynamics in Lottery Contests*, arXiv:2305.10881v1 (first public version 18 May 2023), especially Section 3 and Section 7. https://arxiv.org/html/2305.10881
2. W. A. Coppel, *The solution of equations by iteration*, Proc. Cambridge Philos. Soc. **51** (1955), 41–43. DOI: 10.1017/S030500410002990X.
3. C. Ewerhart, *The lottery contest is a best-response potential game*, Economics Letters **155** (2017), 168–171. DOI: 10.1016/j.econlet.2017.03.030.
4. A. Ghosh, *Best-Response Dynamics in Tullock Contests with Convex Costs*, arXiv:2310.03528 (2023). Only abstract-level content was accessible for this follow-up; its full-text overlap remains a residual risk.
