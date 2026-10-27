# Exact four-broadcast scheduling and a concentration regime in a two-follower opinion network

## Finding

A stubborn leader with fixed opinion \(1\) broadcasts to two initially neutral followers whose ordinary interaction is reciprocal averaging. If the positive broadcast weights differ, the optimal placement of a fixed number of silent updates is sharply dependent on the broadcast budget. For three broadcasts, every optimal schedule splits the available silence as evenly as the integer constraint allows. For four broadcasts, every optimal schedule balances the first and last silent gaps, but need not balance the middle gap: a quartic with exactly one positive root on each parity class reduces the entire integer optimization to at most four candidates. A parameter inequality gives a rigorous regime where the unique optimum puts *all* silence in the middle gap.

More precisely, write \(\lambda=1-2p\), \(a=1-(b_1+b_2)/2\), and \(c=(b_2-b_1)/2\). For four broadcasts and total silence \(G\), the unique schedule \((0,G,0)\) maximizes the eventual follower consensus whenever
\[
\lambda^G(1+\lambda)>1+\frac{c^2}{a^2}\lambda.
\]
For example, at \(p=1/100\), \(b_1=4/5\), \(b_2=1/5\), and \(G=10\), the unique optimum is \((0,10,0)\), while the evenly distributed schedule \((3,4,3)\) gives strictly lower eventual consensus. Their exact consensus-error difference (balanced minus optimal) is
\[
\frac{25553392256660104683}{24414062500000000000000}>0.
\]
The setting is a natural two-follower specialization of time-limited leader influence in averaging networks; it is not a claim that all larger networks or other objectives behave similarly.

## Assumptions and scope

Let \(0<p<1/2\), \(0<b_1,b_2<1\), and \(b_1\ne b_2\). The follower opinion column \(z=(z_1,z_2)^T\) begins at \((0,0)^T\). Ordinary silent updates are \(z\mapsto Wz\) and broadcasts are \(z\mapsto b+DWz\), where
\[
W=\begin{pmatrix}1-p&p\\p&1-p\end{pmatrix},\qquad
b=\begin{pmatrix}b_1\\b_2\end{pmatrix},\qquad
D=\operatorname{diag}(1-b_1,1-b_2).
\]
The leader never changes opinion \(1\). Exactly \(k\in\{3,4\}\) broadcasts occur, with the first broadcast immediately and nonnegative integer numbers \(g_1,\ldots,g_{k-1}\) of silent updates between consecutive broadcasts. The fixed silent-update budget satisfies \(\sum_i g_i=G\ge0\). All followers continue ordinary averaging indefinitely after the final broadcast. The objective is to maximize their common limiting opinion \(L\), equivalently minimize their consensus error \(E=1-L\).

All results are exact for every permitted real parameter and integer budget. The stated concentrated-schedule condition is sufficient; it is not claimed necessary for integer optimality.

## Proof

Put \(u=\mathbf 1-z\). A silent update is \(u\mapsto Wu\), while a broadcast is \(u\mapsto DWu\), since \(b+D\mathbf 1=\mathbf1\). The stochastic matrix \(W\) has eigenvectors \((1,1)^T\) and \((1,-1)^T\) with eigenvalues \(1\) and \(\lambda=1-2p\in(0,1)\). After the broadcasts, ordinary updates converge to projection on \((1,1)^T\); thus \(E=(u_1+u_2)/2\) directly after the last broadcast.

In normalized consensus/disagreement coordinates, \(W\) is \(\operatorname{diag}(1,\lambda)\) and \(D\) is \(\begin{pmatrix}a&c\\c&a\end{pmatrix}\), with \(a>0\), \(c\ne0\). The initial error vector has coordinates \((1,0)\). For three broadcasts, writing \(x=\lambda^{g_1+1}\), \(y=\lambda^{g_2+1}\), multiplication of the three broadcast matrices gives
\[
E_3=a^3+ac^2(x+y+xy).
\]
Because \(xy=\lambda^{G+2}\) is fixed, minimizing \(E_3\) amounts to minimizing \(x+y\). Strict convexity of \(t\mapsto\lambda^t\) for \(0<\lambda<1\), or the elementary exchange comparison between gaps differing by two, shows that the minimizers are exactly the integer pairs with \(|g_1-g_2|\le1\).

For four broadcasts, let \(x=\lambda^{g_1+1}\), \(y=\lambda^{g_2+1}\), \(z=\lambda^{g_3+1}\), and \(K=xyz=\lambda^{G+3}\). Direct multiplication yields the exact identity
\[
E_4=a^4+a^2c^2\bigl[K+y+(1+y)(x+z)\bigr]+c^4xz.
\]
For any fixed middle gap \(m=g_2\), the products \(xz=K/y\) and \(y\) are fixed. Since \(a^2c^2(1+y)>0\), minimizing \(E_4\) is equivalent to minimizing \(x+z\). Therefore all global minimizers have \(|g_1-g_3|\le1\), with \(g_1=\lfloor(G-m)/2\rfloor\) and \(g_3=\lceil(G-m)/2\rceil\), up to exchanging the ends.

Set \(\epsilon=(G-m)\bmod2\) and \(C_0=2\), \(C_1=\sqrt\lambda+1/\sqrt\lambda\). For balanced outer gaps, \(x+z=C_\epsilon\sqrt{K/y}\). The remaining one-variable error is
\[
F_\epsilon(y)=a^4+a^2c^2\left[K+y+C_\epsilon\sqrt K\left(\sqrt y+\frac1{\sqrt y}\right)\right]+c^4\frac K y.
\]
Differentiating and multiplying by the positive factor \(y^2/(a^2c^2)\) shows that \(\operatorname{sgn}F_\epsilon'(y)\) equals the sign of
\[
P_\epsilon(v)=v^4+\frac{C_\epsilon\sqrt K}{2}(v^3-v)-\frac{c^2}{a^2}K,\qquad v=\sqrt y>0.
\]
In descending powers, the nonzero coefficients have signs \(+,+,-,-\). Descartes' rule, together with \(P_\epsilon(0)<0\) and \(P_\epsilon(v)\to\infty\), proves that there is exactly one positive root \(v_\epsilon\), and the derivative switches from negative to positive across it. On each parity class of feasible \(m\), \(y=\lambda^{m+1}\) moves monotonically with \(m\); hence the optimum is attained by one of the at most two feasible parity-constrained integers bracketing \(2\log(v_\epsilon)/\log\lambda-1\), or by the nearest endpoint if the root lies outside the feasible range. There are at most four candidates over both parities, yielding an exact finite algorithm for all \(G\), independent of the magnitude of \(G\).

For the concentration criterion, allow equal real outer gaps temporarily, which gives the lower envelope \(F_0(y)\) for every balanced or unbalanced integer schedule because \(x+z\ge2\sqrt{xz}\). Feasible \(y\) satisfies \(\lambda^{G+1}\le y\le\lambda\). At its left endpoint \(y_0=\lambda^{G+1}\), a direct factorization gives
\[
P_0(\sqrt{y_0})=\lambda^{G+2}\left[\lambda^G(1+\lambda)-1-\frac{c^2}{a^2}\lambda\right].
\]
If the bracket is positive, the unique-positive-root property implies \(F_0'(y)>0\) throughout \([y_0,\lambda]\). It follows that every schedule has \(E_4\ge F_0(y)\ge F_0(y_0)\), with equality only when \(m=G\) and \(g_1=g_3=0\). This proves global uniqueness of the concentrated schedule. In the specified rational example, \(\lambda=49/50\), \(a=1/2\), \(|c|=3/10\), and the criterion holds strictly; the exact errors are
\[
E_4(0,10,0)=\frac{903373787686956792814241}{4882812500000000000000000},\qquad
E_4(3,4,3)=E_4(0,10,0)+\frac{25553392256660104683}{24414062500000000000000}.
\]

## Verification

The standalone script `verify.py` uses only Python's `fractions.Fraction` and standard library. It independently evolves the two-dimensional update matrices for each gap schedule and compares the exact result against the two derived closed formulas. It enumerates every composition of \(G\le10\) for nine rational parameter sets and for both three and four broadcasts (3,168 schedules), checking three-broadcast balancing and four-broadcast outer-gap reduction. It also verifies the strict rational inequality, the unique optimal concentrated schedule, and the exact error difference for \(G=10\). Running `python verify.py` returns `CHECK_OK`. The proof above, rather than finite enumeration, establishes the assertions for all allowed parameters and budgets.

## Relationship to prior work

Zhuang, Wang, Wang, Wang, and Yang (2022) formulated temporary external influence in a DeGroot-style model; its Section 4 considers a leader with uniform influence on an addressed subset, and its Section 5 compares selected timing patterns rather than deriving the finite-budget optimum with two heterogeneous exposure strengths. Their full-coverage timing-independence statement applies to equal influence weights, not the unequal weights assumed here. Shen, He, Wu, Zhu, and Shen (2023) introduced intermittent leaders into signed follower networks, including the broadcast matrix \(\begin{pmatrix}1&0\\b&(I-B)W\end{pmatrix}\), and identified a timing-independence condition for equal influence magnitudes. The present theorem explicitly works in the contrasting timing-dependent positive-weight regime and determines exact optimal placement for three or four broadcasts with a fixed total silent-update budget. Weimer, Miller, Hill, and Hodson (2019) studied simulation-based agent scheduling and update-order effects rather than this leader-pulse optimization. No priority beyond the inspected accessible sources is claimed.

## Limitations

The classification uses precisely two symmetric followers, positive unequal leader weights, synchronous updating, a fixed number of three or four broadcasts and a fixed total count of intervening silent updates. It optimizes post-intervention consensus, not transient social welfare, adoption thresholds, discounted reward or arbitrarily many broadcasts. The four-broadcast concentration inequality is sufficient, not a necessary-and-sufficient condition for every integer instance. Literature coverage is nonexhaustive; an equivalent unpublished or inaccessible result may exist.

## References

1. Zhuang, Z., Wang, K., Wang, Z., Wang, J., and Yang, Y. (2022). *Maximising the Influence of Temporary Participants in Opinion Formation*. arXiv:2205.12503v1 (first publicly posted 25 May 2022). https://arxiv.org/abs/2205.12503 .
2. Shen, Z., He, G., Wu, X., Zhu, Y., and Shen, M. (2023). *Opinion dynamics with intermittent-influence leaders on the signed social network*. Engineering Reports 5, e12649. DOI: 10.1002/eng2.12649 . Open full text: https://onlinelibrary.wiley.com/doi/full/10.1002/eng2.12649 .
3. Weimer, C., Miller, J. O., Hill, R., and Hodson, D. (2019). *Agent Scheduling in Opinion Dynamics: A Taxonomy and Comparison Using Generalized Models*. Journal of Artificial Societies and Social Simulation 22(4), 5. DOI: 10.18564/jasss.4065 . https://www.jasss.org/22/4/5.html .
