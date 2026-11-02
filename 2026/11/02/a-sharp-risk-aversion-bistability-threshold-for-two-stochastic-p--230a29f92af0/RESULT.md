# A sharp risk-aversion bistability threshold for two stochastic parallel roads

## Finding

Two parallel roads can have strictly increasing travel times in **every realized traffic scenario**, yet homogeneous nonatomic travelers minimizing mean travel time plus a nonnegative multiple of travel-time variance can possess **three distinct Wardrop equilibria**, two of them strict, locally attracting pure-road allocations. The mechanism is an anticorrelation between the intercept and congestion slope of the random road: its travel-time variance decreases as its flow increases.

The following sharp parameter theorem makes this phenomenon nonaccidental. Suppose a unit mass chooses between a deterministic road A, with latency \(L_A(x)=c+dx\), and a two-scenario road B, with equiprobable latencies \(L_B^{(0)}(y)=u+sy\) and \(L_B^{(1)}(y)=u+H+ty\). Assume
\[
 u\ge0,\quad c>0,\quad d>0,\quad s>t>0,\quad H>s-t>0.
\]
Here \(x=1-y\) is the flow on A, and \(y\in[0,1]\) is the flow on B. The intercept \(c\) may be chosen freely, holding the other primitives fixed. Put \(v=(s+t)/2\) and \(\Delta=s-t\). For mean-variance coefficient \(\gamma\ge0\), there is a choice of \(c>0\) for which both all-A and all-B are **strict** Wardrop equilibria if and only if
\[
 \boxed{\displaystyle \gamma>\gamma_c:=\frac{4(v+d)}{\Delta(2H-\Delta)}.}
\]
More precisely, for fixed \(c\) the two pure equilibria are simultaneously strict exactly when
\[
 \boxed{\displaystyle u+\frac H2+v+\frac{\gamma(H-\Delta)^2}{4}
 <c< u+\frac H2-d+\frac{\gamma H^2}{4}.}
\]
Whenever these inequalities hold, there is exactly one additional mixed Wardrop equilibrium. The two pure equilibria are locally attracting, and the mixed equilibrium is repelling, under the projected route-choice adjustment \(\dot y=-[Q_B(y)-Q_A(1-y)]\) in the interior of the interval.

An exact fully classified example is
\[
 L_A(x)=\frac{27}{5}+x,\qquad
 L_B^{(0)}(y)=3y,\qquad L_B^{(1)}(y)=4+y,
\]
with the two B scenarios equally likely. If \(E_\gamma\) denotes its set of Wardrop B-flows, then the entire phase diagram is:

| Risk coefficient | All equilibrium B-flows |
|---|---|
| \(0\le\gamma<11/10\) | \(1\) |
| \(\gamma=11/10\) | \(0,1\) |
| \(11/10<\gamma<7/5\) | \(0,y_-(\gamma),1\) |
| \(\gamma=7/5\) | \(0,6/7,1\) |
| \(7/5<\gamma<45/32\) | \(0,y_-(\gamma),y_+(\gamma)\) |
| \(\gamma=45/32\) | \(0,14/15\) (the interior equilibrium is double) |
| \(\gamma>45/32\) | \(0\) |

Here
\[
 y_\pm(\gamma)=\frac{4\gamma-3\pm\sqrt{9-32\gamma/5}}{2\gamma}
\]
are used only on the intervals where the displayed roots are real and feasible. In the three-equilibrium regions, the lower mixed root is repelling; the upper mixed root, when present, is attracting. At \(\gamma=6/5\), the two strict pure equilibria have different total *expected* travel times, \(32/5\) (all A) and \(4\) (all B), despite both being individually stable under mean-variance choices.

## Assumptions and scope

The population is a continuum of infinitesimal, identical, nonatomic travelers with total demand one and a single origin-destination pair. Each road is a direct parallel link. The deterministic latency on A depends only on its own flow. On B, conditional on a common Bernoulli scenario, latency is one of the two specified affine functions of its own aggregate flow. Both realized B latencies are strictly increasing and, since \(H>\Delta\), the high-intercept scenario remains the slower one throughout \([0,1]\). Agents know the two conditional distributions at a proposed aggregate flow and minimize \(Q=\mathbb E[L]+\gamma\operatorname{Var}(L)\), with \(\gamma\ge0\). A single infinitesimal user does not change aggregate flow or the scenario distribution. Travel times are nonnegative for all feasible flows. The adjustment stability conclusions concern only the explicitly stated projected scalar adjustment and do not assert stability for every learning rule.

A Wardrop equilibrium is a flow allocation where every positively used road has perceived cost no greater than the cost of the other road. An allocation is a **strict pure equilibrium** if everyone uses one road and the unused road has strictly greater perceived cost. A mixed equilibrium uses both roads and must equalize their perceived costs.

## Proof

For B-flow \(y\), direct averaging of its two equiprobable scenarios gives
\[
 \mathbb E L_B=u+\frac H2+vy,\qquad
 \operatorname{Var}(L_B)=\frac{(H-\Delta y)^2}{4}.
\]
Subtracting the deterministic cost \(Q_A(1-y)=c+d(1-y)\), the route-cost difference is
\[
 F_\gamma(y):=Q_B(y)-Q_A(1-y)
 =u+\frac H2-c-d+(v+d)y+\frac\gamma4(H-\Delta y)^2.
\]
Thus \(F_\gamma\) is continuous, and for \(\gamma>0\), strictly convex with second derivative \(\gamma\Delta^2/2>0\). Wardrop conditions reduce exactly to
\[
 y=0:\ F_\gamma(0)\ge0;\qquad
 0<y<1:\ F_\gamma(y)=0;\qquad
 y=1:\ F_\gamma(1)\le0.
\]
Both pure endpoints are strict if and only if \(F_\gamma(0)>0>F_\gamma(1)\). Rearranging these two inequalities yields exactly the displayed open interval for \(c\). Its width is
\[
 \frac{\gamma\Delta(2H-\Delta)}4-(v+d).
\]
Since \(\Delta>0\) and \(2H-\Delta>0\), this interval is nonempty exactly when \(\gamma>\gamma_c\). Its lower endpoint is positive, so an admissible positive \(c\) always exists when it is nonempty. Conversely, no \(c\) works at or below the threshold. When both strict endpoint conditions hold, a root exists in \((0,1)\) by continuity. Its uniqueness follows from strict convexity and the negative value at the right endpoint: the quadratic sublevel interval can enter \([0,1]\) only once from the left. The root crosses from positive to negative and has \(F'_\gamma<0\). Under projected \(\dot y=-F_\gamma(y)\), the motion points toward the closer pure endpoint on either side of that root, establishing its repelling nature and the local attraction of both pure equilibria.

For the rational example, the expected latency and variance on B are \(2+2y\) and \((2-y)^2\); on A the latency is \(32/5-y\). Therefore
\[
 F_\gamma(y)=\gamma(y-2)^2+3y-\frac{22}{5},\quad
 F_\gamma(0)=4\gamma-\frac{22}{5},\quad
 F_\gamma(1)=\gamma-\frac75.
\]
Its discriminant in \(y\) is \(9-32\gamma/5\), and its roots for \(\gamma>0\) are the displayed \(y_\pm(\gamma)\). The endpoint signs change exactly at \(\gamma=11/10\) and \(\gamma=7/5\); the discriminant vanishes exactly at \(\gamma=45/32\). At the three boundary coefficients the polynomials factor exactly as
\[
 F_{11/10}(y)=\frac{y(11y-14)}{10},\qquad
 F_{7/5}(y)=\frac{(y-1)(7y-6)}5,\qquad
 F_{45/32}(y)=\frac{(15y-14)^2}{160}.
\]
For \(0\le\gamma<11/10\), both endpoints of this convex polynomial are negative, hence it is negative throughout the feasible interval; only \(y=1\) is a Wardrop equilibrium. For \(11/10<\gamma<7/5\), its endpoint signs are positive and negative, so precisely one interior root exists. At \(\gamma=7/5\), the second factorization shows the interior root \(6/7\) and endpoint root 1. For \(7/5<\gamma<45/32\), both endpoint values are positive, while the vertex \(2-3/(2\gamma)\) lies strictly in \((0,1)\) and has negative value because the discriminant is positive. Hence there are exactly two interior roots. The double-root and no-root cases beyond the discriminant threshold follow directly from the last factorization and the negative discriminant. The boundary coefficient \(11/10\) likewise follows from its factorization. These cases exhaust every \(\gamma\ge0\) and prove the table. The sign of \(F_\gamma\) between its roots gives the stated local adjustment stability. At \(\gamma=6/5\), both endpoint conditions are strict, and the sole interior root is \((9-\sqrt{33})/12\). Total expected travel time at the two pure equilibria is respectively \(L_A(1)=32/5\) and \(\mathbb E L_B(1)=4\), as claimed.

## Verification

The accompanying standalone `check.py` requires Python 3 and SymPy. From the directory containing this file and the script, run `python check.py`. It independently constructs the two Bernoulli outcomes, simplifies mean and variance symbolically, verifies the sharp interval identity, the example discriminant and boundary factorizations, the explicit roots and the endpoint signs, and uses exact rational root counting at boundary and interior sample points. Further independent exact-rational parameter tests verify the general interval criterion, yielding 1,127 passing assertions. These finite tests supplement, but do not replace, the quantified algebraic proof above.

## Relationship to prior work

Ordóñez and Stier-Moses (2010) studied risk-averse Wardrop routing with random deviations independent of flow and proved essential uniqueness under their model's assumptions. That exogenous-noise premise does not cover the flow-dependent and decreasing variance here. Nikolova and Stier-Moses (2014), in their mean-*standard-deviation* model, established equilibrium structure and discussed nonmonotonicity and unresolved uniqueness under strictly increasing variance conditions; the present result uses mean-*variance* and a variance **decreasing** with flow, and does not settle their distinct uniqueness question. Nikolova and Stier-Moses (arXiv:1411.0059, 2014) and Lianeas, Nikolova, and Stier-Moses (2016; arXiv:1510.02067 first posted 2015) develop general mean-variance risk-aversion inefficiency bounds and variational tools. The latter explicitly makes a nondecreasing-modified-cost assumption for its variational inequality section. Its broad risk bounds and graph constructions do not state the two-scenario affine-road coexistence threshold or the complete bifurcation in this example. The result therefore isolates an assumption boundary for uniqueness arguments: increasing realized latency in every state does not imply increasing mean-variance perceived cost.

These are statement-and-assumption comparisons, not a proof of historical priority. An independently previously published specialization could exist under alternative terminology such as nonmonotone user equilibrium or fold bifurcation.

## Limitations

This is an exactly soluble, idealized two-road nonatomic traffic game with one common two-point latency scenario, identical agents, no incident correlation across multiple links, no finite-agent strategic effects, and a mean-plus-variance preference functional. The result makes no claim about mean-plus-standard-deviation equilibrium uniqueness, empirical traffic calibration, global stability under arbitrary behavior-update rules, or general networks. The sharp general risk coefficient permits the intercept of road A to be chosen; for a fixed intercept the separate strict inequalities, rather than that coefficient alone, determine coexistence. Novelty has been checked against identified primary sources and available comparable findings but is not independently certified.

## References

1. Ordóñez, F., and Stier-Moses, N. E. (2010). *Wardrop Equilibria with Risk-Averse Users*. Transportation Science 44(1), 63–86. Published online 2010-01-22. https://doi.org/10.1287/trsc.1090.0292
2. Nikolova, E., and Stier-Moses, N. E. (2014). *A Mean-Risk Model for the Traffic Assignment Problem with Stochastic Travel Times*. Operations Research 62(2), 366–382. https://doi.org/10.1287/opre.2013.1246 ; lawful author manuscript: https://users.ece.utexas.edu/~nikolova/papers/stochWardropEqFinalOR.pdf
3. Nikolova, E., and Stier-Moses, N. E. (2014). *The Burden of Risk Aversion in Mean-Risk Selfish Routing*. arXiv:1411.0059, first posted 2014-11-01. https://arxiv.org/abs/1411.0059
4. Lianeas, T., Nikolova, E., and Stier-Moses, N. E. (2016). *Asymptotically Tight Bounds for Inefficiency in Risk-Averse Selfish Routing*. IJCAI 2016, 339–345. First arXiv version posted 2015-10-07, arXiv:1510.02067. https://arxiv.org/abs/1510.02067 ; https://ijcai.org/proceedings/2016/0055.pdf
