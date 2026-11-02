# A square-root imbalance transition for optimally biased bipartite cover times

## Finding

Let \(K_{a,b}\) be a complete bipartite graph, with a specified starting vertex in the part of size \(a\). At each discrete transition, independently, with probability \(\varepsilon\) a controller chooses any adjacent vertex, and with probability \(1-\varepsilon\) the next vertex is uniform among all neighbours. The controller observes the visited set and may use any history-dependent randomized policy. For any \(a,b\ge1\) and \(0\le\varepsilon\le1\), a policy that chooses an unvisited neighbour whenever permitted *stochastically minimizes* the whole cover time among all policies.

For \(m\ge1\), let
\[
X_m=\sum_{j=1}^{m-1}G_{m,j},\qquad
\Pr(G_{m,j}=k)=q_{m,j}(1-q_{m,j})^{k-1},\qquad
q_{m,j}=\varepsilon+(1-\varepsilon)\frac jm,
\]
for \(k=1,2,\ldots\), with all summands independent and \(X_1=0\). Independent copies \(X_a,X_b'\) yield the exact optimally controlled cover-time law
\[
T_{a,b}^{\star}\ \overset{d}=\ \max\{2X_a,\,2X_b'+1\}.
\]
In particular, for the distribution functions \(F_m(k)=\Pr(X_m\le k)\), with \(F_m(k)=0\) at negative integers,
\[
\Pr(T_{a,b}^{\star}\le2k)=F_a(k)F_b(k-1),\qquad
\Pr(T_{a,b}^{\star}\le2k-1)=F_a(k-1)F_b(k-1).
\]
The last visited vertex lies in the second part precisely when \(X_b'\ge X_a\).

Fix \(0<\varepsilon<1\) and set
\[
I_\varepsilon=\frac{\log(1/\varepsilon)}{1-\varepsilon},\qquad
V_\varepsilon=\frac{\varepsilon^{-1}-1+\log\varepsilon}{1-\varepsilon}>0.
\]
For any real \(\lambda\), put \(a_n=n+\lfloor\lambda\sqrt n\rfloor\) and \(b_n=n-\lfloor\lambda\sqrt n\rfloor\), for sufficiently large integers \(n\). With independent standard normals \(Z_1,Z_2\),
\[
\frac{T_{a_n,b_n}^{\star}-2nI_\varepsilon}{2\sqrt n}
\ \Rightarrow\
\max\{\lambda I_\varepsilon+\sqrt{V_\varepsilon}Z_1,
          -\lambda I_\varepsilon+\sqrt{V_\varepsilon}Z_2\}.
\]
The limiting distribution function at \(x\in\mathbb R\) is
\[
\Phi\!\left(\frac{x-\lambda I_\varepsilon}{\sqrt{V_\varepsilon}}\right)
\Phi\!\left(\frac{x+\lambda I_\varepsilon}{\sqrt{V_\varepsilon}}\right).
\]
The terminal class has the sharp Gaussian crossover
\[
\Pr(\text{last vertex lies in the part of size }b_n)
\ \longrightarrow\
\Phi\!\left(-\frac{\sqrt2\lambda I_\varepsilon}{\sqrt{V_\varepsilon}}\right).
\]
Moreover, if \(Z\) is standard normal,
\[
\mathbb ET_{a_n,b_n}^{\star}
=2nI_\varepsilon+
\sqrt n\,\mathbb E\left|2\lambda I_\varepsilon+\sqrt{2V_\varepsilon}Z\right|
+o(\sqrt n).
\]
At exact balance the correction is \(2\sqrt{nV_\varepsilon/\pi}+o(\sqrt n)\). More generally, for \(a_n,b_n\sim n\) and \(|a_n-b_n|/\sqrt n\to\infty\), the larger part is last with probability tending to one. Thus fixed positive control moves the terminal-part crossover to the square-root imbalance scale.

## Assumptions and scope

The graph is loopless and complete bipartite, with labelled vertex parts of sizes \(a,b\ge1\). The initially occupied vertex in the first part counts as visited at time zero; the cover time counts subsequent transitions. The controller is offered full neighbour control independently at each time with a fixed probability \(\varepsilon\), and each uncontrolled move is independently uniform. No control is allowed to alter the forced alternation between vertex parts. The exact law and stochastic optimality hold even at \(\varepsilon=0\) or \(\varepsilon=1\), but the asymptotic Gaussian statements require one fixed \(\varepsilon\in(0,1)\), independent of \(n\).

## Proof

**1. All-horizon optimality.** Every odd transition enters the second part and every even transition enters the first. Suppose a visit is made to a part of size \(m\), with \(j\) vertices still unseen. Conditional on the complete past, an arbitrary controller can make a new discovery with probability no greater than
\(q_{m,j}=\varepsilon+(1-\varepsilon)j/m\); the first-visit-greedy policy attains equality. This bound is independent of all identities and positions inside the *other* part. Couple the numbers of already visited vertices under greediness and any competing policy using a common independent uniform random variable on each part-visit. Whenever their visit counts are equal, the greedy new-discovery probability is at least the competitor's; once the greedy count is ahead, the competitor cannot overtake it in one transition. An induction over successive visits to each part therefore gives coordinatewise dominance of the greedy visited-count vector, and hence the greedy cover time is no larger in this coupling at every horizon. This proves stochastic, not only expectation, optimality, for every history-dependent competitor.

**2. Exact independent-stage law.** Along a single part's arrivals, when \(j\) vertices remain unseen, successive new-discovery indicators are independent Bernoulli trials with success probability \(q_{m,j}\), until the next discovery; their waiting time is geometric with this parameter. The part of size \(a\) starts with one observed vertex; the second part starts empty, and its very first arrival discovers a vertex surely. Independence of the random control coins and uniform choices at separate odd and even transitions, together with a fixed tie-breaking convention for greediness, makes the two parts' waiting-time sequences independent. Their completion times on the physical clock are \(2X_a\) and \(2X_b'+1\), proving the exact maximum representation and the distribution functions.

**3. Moment asymptotics and joint CLT.** For \(0<\varepsilon<1\), uniformly over \(m\), the success parameters are bounded below by \(\varepsilon\). Hence the independent geometric summands have uniformly bounded third absolute centered moments. Euler or elementary Riemann-sum bounds for the continuously differentiable functions
\[f(x)=\bigl[\varepsilon+(1-\varepsilon)x\bigr]^{-1},\qquad
  g(x)=\frac{1-\varepsilon-(1-\varepsilon)x}{\bigl[\varepsilon+(1-\varepsilon)x\bigr]^2}\]
give
\[
\mathbb EX_m=m\int_0^1 f(x)\,dx+O_\varepsilon(1)
   =mI_\varepsilon+O_\varepsilon(1),\quad
\operatorname{Var}(X_m)=m\int_0^1g(x)\,dx+O_\varepsilon(1)
   =mV_\varepsilon+O_\varepsilon(1).
\]
The displayed value of \(V_\varepsilon\) is positive because the integrand \(g\) is positive except at an endpoint. Lyapunov's triangular-array central limit theorem gives
\((X_m-mI_\varepsilon)/\sqrt m\Rightarrow N(0,V_\varepsilon)\).
The independent copies yield independent normal limits. For the chosen part sizes, their centering shifts tend to \(\pm\lambda I_\varepsilon\) on the \(\sqrt n\) scale. Continuity of maximum proves the cover-time distributional limit and its displayed CDF.

**4. Terminal class and expectation.** The second part finishes last exactly when \(2X_b'+1>2X_a\), equivalently \(X_b'\ge X_a\). The difference between the two centered independent stage sums converges to a normal of variance \(2V_\varepsilon\) and mean \(-2\lambda I_\varepsilon\); its atom at zero disappears under the continuous limit, proving the normal terminal-class probability. The normalized maximum has uniformly bounded second moments (by the preceding variance estimates and the \(O_\varepsilon(1)\) mean errors), hence is uniformly integrable and its expectation converges. The identity \(2\max(u,v)=u+v+|u-v|\) gives the explicit expected-time correction. Finally, when \(a_n,b_n\sim n\) but \(|a_n-b_n|/\sqrt n\to\infty\), the difference of stage means has magnitude asymptotic to \(I_\varepsilon|a_n-b_n|\), while the variance is \(O_\varepsilon(n)\). Chebyshev's inequality gives the asserted last-part concentration.

## Verification

A standalone standard-library rational-arithmetic checker, `checker.py`, exhausts \(1\le a,b\le5\), control probabilities \(\varepsilon\in\{0,1/3,1/2,2/3,1\}\), and horizons \(0\le t\le22\). For each case it compares the independent-geometric formula against exact finite-state dynamic programming over *all* immediate control choices, and checks finite-stage moments. It prints `PASS 6250 exact rational assertions`. These finite checks detect indexing or policy errors but do not certify the all-size optimality or asymptotic claims; those follow from the analytic arguments above. To reproduce, run `python3 checker.py` from the directory containing the two standalone files.

## Relationship to prior work

The underlying time-dependent controlled walk is the \(\varepsilon\)-biased random walk studied by Haslegrave, Sauerwald and Sylvester. Their paper develops general hitting/cover-time bounds and policy complexity, but the inspected statements do not give the finite complete-bipartite factorization or this terminal-class Gaussian crossover. The conference predecessor of Georgakopoulos, Haslegrave, Sauerwald and Sylvester treats choice walks and biased walks but likewise does not provide these laws. The two-choice walk, which offers *two* uniform neighbours, is a different transition model: its one-step success probability is \(1-(1-j/m)^2\), not \(\varepsilon+(1-\varepsilon)j/m\). Its results cannot substitute for the exact distribution here. The general stochastic coupon-assignment literature offers possible antecedents of the greedy-policy lemma; this work's chief distinction is the explicit alternating independent-stage law and fixed-positive-control crossover, neither of which follows merely from a general policy-optimality assertion.

## Limitations

No statement is made about varying \(\varepsilon\) with graph size, noncomplete bipartite graphs, more than two parts, or control signals with temporal dependence. The endpoint \(\varepsilon=0\) has a different fluctuation scale. Priority relative to older general stochastic-assignment and coupon-collection results requires further independent historical examination; in particular, Ross and Wu's 2013 assignment paper could not be inspected in full through lawful open access. No independent mathematical audit has been performed.

## References

1. J. Haslegrave, T. Sauerwald and J. Sylvester, *Time Dependent Biased Random Walks*, arXiv:2006.02475 (first posted 3 June 2020), https://arxiv.org/abs/2006.02475 and https://arxiv.org/html/2006.02475v2 .
2. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *The Power of Two Choices for Random Walks*, arXiv:1911.05170 (first posted 12 November 2019), https://arxiv.org/abs/1911.05170 .
3. A. Georgakopoulos, J. Haslegrave, T. Sauerwald and J. Sylvester, *Choice and Bias in Random Walks*, LIPIcs ITCS 2020, Article 76, https://doi.org/10.4230/LIPIcs.ITCS.2020.76 .
4. S. M. Ross and D. T. Wu, *A generalized coupon collecting model as a parsimonious optimal stochastic assignment model*, Annals of Operations Research 208 (2013), 133–146, https://doi.org/10.1007/s10479-012-1086-5 (abstract inspected; full text not available).
