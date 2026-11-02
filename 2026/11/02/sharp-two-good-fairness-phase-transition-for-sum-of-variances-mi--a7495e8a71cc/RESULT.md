# Sharp two-good fairness phase transition for sum-of-variances-minimizing lotteries

## Finding
For two agents and two indivisible goods, normalize each agent's total value to one. Suppose the agents have values \(v_1(A)=a\), \(v_1(B)=1-a\), \(v_2(A)=b\), and \(v_2(B)=1-b\), where \(0<a<b<1/2\). Among all complete-allocation lotteries satisfying ex-ante proportionality, minimize the sum \(\Phi=\operatorname{Var}(U_1)+\operatorname{Var}(U_2)\) of agents' own-bundle utility variances.

Write \(C\) for the allocation giving \(A\) to agent 1 and \(B\) to agent 2, \(D\) for the reverse one-good-each allocation, \(E\) for both goods to agent 1, and \(F\) for both goods to agent 2. Set \(S=(C+D)/2\) and \(R=tD+(1-t)F\), where \(t=1/[2(1-b)]\). Here formal convex combinations denote lotteries.

**Exact classification.** Every optimum is one of \(S\) and \(R\). Define \(x=1-2a\), \(y=1-2b\), and
\[
 g_x(y)=y\left(1+\frac{(1+x)^2}{(1+y)^2}\right)-x^2-y^2.
\]
If \(g_x(y)>0\), the unique optimum is \(S\); if \(g_x(y)<0\), the unique optimum is \(R\); if \(g_x(y)=0\), precisely \(S\) and \(R\) are optimal, and their nontrivial mixtures are not. For each fixed \(0<x<1\), there is a unique \(y_*(x)\in(0,x)\) satisfying \(g_x(y_*)=0\). Thus the exact transition is \(b_*(a)=[1-y_*(1-2a)]/2\), with the fair optimum \(S\) for \(a<b<b_*(a)\) and the ex-post-unfair optimum \(R\) for \(b_*(a)<b<1/2\).

Both allocations in the support of \(S\) are EF1 (indeed EFX). The lottery \(R\) allocates both goods to agent 2 with positive probability and is therefore not ex-post EF1 or ex-post MMS. At \((a,b)=(1/10,2/5)\), \(S\) costs \(17/100\), while \(R=(5/6)D+(1/6)F\) costs \(13/80\), providing a rational witness of strict failure.

## Assumptions and scope
Agents' additive values are strictly positive, normalize to one separately, and satisfy \(0<a<b<1/2\). All four deterministic allocations of the two distinct goods are allowed, allocations are complete, and lotteries are probability distributions over these four allocations. Ex-ante proportionality means \(\mathbb E U_i\ge1/2\) for both agents. Utility variance is computed with respect to the random allocation, not across agents or goods. No independence restriction is imposed on good assignment. Claims do not extend to boundary parameters \(a=b\), \(a=0\), \(b=1/2\), more goods, or additional constraints.

## Proof
The four own-utility vectors \((U_1,U_2)\) are \(z_C=(a,1-b)\), \(z_D=(1-a,b)\), \(z_E=(1,0)\), and \(z_F=(0,1)\). Write the lottery probabilities \((c,d,e,f)\), nonnegative and summing to one. Ex-ante proportionality imposes \(ac+(1-a)d+e\ge1/2\) and \((1-b)c+bd+f\ge1/2\).

We first enumerate the vertices of this three-dimensional polytope. An extreme point needs three active inequalities in addition to the probability-sum equality. If at least two probability coordinates vanish, it lies on one of the six two-allocation edges. Direct substitution shows that the only feasible edge intersections are \(S=(1/2,1/2,0,0)\), \(Q=(0,0,1/2,1/2)\), and the endpoints \(H_1=(0,t_1,0,1-t_1)\), \(H_2=(0,t_2,0,1-t_2)\) of the feasible portion of edge \(DF\), where \(t_1=1/[2(1-a)]\) and \(t_2=1/[2(1-b)]\). More explicitly, the edges \(CD\) and \(EF\) meet the constraints only at \(S,Q\), the edge \(DF\) has feasible interval \([t_1,t_2]\) in its \(D\)-weight, and the other three edges have no feasible point. A one-outcome lottery is infeasible. If at most one probability coordinate vanishes at a vertex, both ex-ante inequalities must be active. Adding their equalities gives \(c+d+e+f=1\), and subtracting the first equality from \(1/2\) gives the equivalent equation \((a-b)(c-d)=0\); thus \(c=d\) and \(e=f=1/2-c\), a line segment from \(Q\) to \(S\) with no new vertices. Hence the complete vertex set is \(\{S,Q,H_1,H_2\}\).

For any lottery \(p\),
\[
 \Phi(p)=\sum_jp_j\|z_j\|_2^2-\left\|\sum_jp_jz_j\right\|_2^2,
\]
which is concave on the probability simplex. Therefore an optimum exists at a listed vertex. Direct calculation gives
\[
 \Phi(S)=\left(\frac12-a\right)^2+\left(\frac12-b\right)^2,\qquad
 \Phi(Q)=\frac12.
\]
Because \(0<a<b<1/2\), \(\Phi(S)<1/2\). Along \(DF\), \(\Phi(H(t))=t(1-t)[(1-a)^2+(1-b)^2]\). Since \(1/2<t_1<t_2<1\), this decreases strictly and \(\Phi(H_2)<\Phi(H_1)\). Thus a minimizing vertex is \(S\) or \(R=H_2\). The exact formula
\[
 \Phi(R)=\frac{1-2b}{4(1-b)^2}\big[(1-a)^2+(1-b)^2\big]
\]
then yields \(4[\Phi(R)-\Phi(S)]=g_x(y)\). These statements establish the claimed strict regimes.

No additional optimum can lie on a nontrivial face: for lotteries \(p,q\),
\[
 \Phi(\lambda p+(1-\lambda)q)=\lambda\Phi(p)+(1-\lambda)\Phi(q)
 +\lambda(1-\lambda)\|\mathbb E_p z-\mathbb E_q z\|_2^2.
\]
When two distinct optimal vertices tie, this identity rules out their mixture whenever their mean vectors differ. Here \(\mathbb E_Sz=(1/2,1/2)\) but \(\mathbb E_R z=((1-a)/[2(1-b)],1/2)\ne(1/2,1/2)\). A representation of an arbitrary feasible optimizer as a convex combination of vertices, and the same identity extended to finitely many vertices, excludes every other optimizer; in the strict regimes the optimal vertex is also unique.

Finally, for fixed \(0<x<1\),
\[
 g_x(0)=-x^2<0,\quad g_x(x)=2x(1-x)>0,\quad
 g_x''(y)=-2-\frac{2(1+x)^2(2-y)}{(1+y)^4}<0\quad(0\le y\le x).
\]
Strict concavity together with the endpoint signs implies precisely one crossing in \((0,x)\): after entering the positive half-line, a concave function cannot return to zero within the interval when its right endpoint remains positive. This proves the unique transition. The allocation \(F\), which occurs with probability \(1-t=(1-2b)/[2(1-b)]>0\) under \(R\), leaves agent 1 empty despite strictly positive values for both goods, so deleting either one good from agent 2's bundle leaves a strictly positive bundle: EF1 fails. Under \(S\) each bundle contains exactly one good, so deleting that good eliminates envy. The rational example follows by substitution.

## Verification
Execute the bundled standalone Python 3 standard-library program `verify.py`: `python3 verify.py`. It checks the analytically derived four-vertex list against an independent exact rational active-constraint enumerator for 330 admissible rational parameter pairs; verifies every resulting vertex comparison and the phase identity; and checks the rational strict-failure witness. Expected output: `VERIFY_OK exact_parameter_pairs=330 active_sets_per_pair=20 witness_t=5/6 fair_variance=17/100 risky_variance=13/80`. These finite tests are supplementary to, not a replacement for, the universal analytic argument.

## Relationship to prior work
Babaioff and Grofman, *On Best-of-Both-Worlds Fairness via Sum-of-Variances Minimization* (arXiv:2601.16579v1, publicly submitted January 23, 2026), study sum-of-variances minimization under ex-ante proportionality and show that an optimal lottery need not be ex-post EF1 even for two agents and two goods (their Section 5 and numerical example/Appendix B). In contrast to their explicitly evaluated single preference profile, the result here gives a necessary-and-sufficient phase criterion for every interior parameter pair where both agents prefer the same good, including a unique transition curve, optimizer uniqueness, and exact tie behavior. Their specific witness already establishes existence of failure and is not claimed as new. Related few-agent best-of-both-worlds existence algorithms address a different optimization question.

## Limitations
Only the specified two-parameter open chamber of valuations and ex-ante proportionality constraint are classified. No general claim about the global objective outside this chamber, more agents, more goods, ex-ante envy-freeness, or other fairness constraints is made. The novelty assessment is based on accessible literature and mathematical-record searches, not an independent publication-priority determination; unindexed equivalent formulations remain possible. All numerical experiments are finite corroborations; no machine proof of the full theorem is claimed.

## References
- Moshe Babaioff and Yuval Grofman, *On Best-of-Both-Worlds Fairness via Sum-of-Variances Minimization*, arXiv:2601.16579v1 (first public January 23, 2026), https://arxiv.org/abs/2601.16579 ; readable version https://arxiv.org/html/2601.16579v1 . See Sections 1, 2, 5 and Appendix B.
- *Near-Optimal Best-of-Both-Worlds Fairness for Few Agents*, arXiv:2602.14668 (2026), https://arxiv.org/abs/2602.14668 . Different constructive near-optimal fairness guarantee, rather than exact two-good sum-of-variances optimizer classification.
