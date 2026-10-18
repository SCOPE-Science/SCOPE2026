# Risk-fiber calibration and an exact recurrence obstruction in a collective-risk cooperation game

## Finding

Consider the three-variable cooperation–risk–cost flow of Wang, Hua, Liu, Zhang, Liu and Szolnoki (2026), Model 1, with a quorum of at least two but fewer than the group size. The theorem below describes **every invariant probability law supported compactly in the open state box**, including the invariant law of any interior periodic orbit, without assuming that such an orbit exists.

Let \(N\ge3\), \(2\le M\le N-1\) be integers and let \(B,\mu_1,\mu_2,\theta_1,\theta_2,\theta_3,\theta_4\) be positive, with \(0<\beta<\alpha\). Define
\[
F(s)=\binom{N-1}{M-1}s^{M-1}(1-s)^{N-M},\quad
\chi=\frac{\mu_1}{\mu_1+\mu_2},\quad
\eta=\frac{(\theta_1+\theta_2)\chi-\theta_1+\theta_4}{\theta_3+\theta_4}.
\]
Let \(H\) be the least concave majorant of \(F\) on \([0,1]\), given explicitly in the proof. For **every compactly supported invariant probability measure** \(\nu\) in \(\Omega=(0,1)\times(0,1)\times(\beta,\alpha)\),
\[
\boxed{\mathbb E_\nu[x\mid r]=\chi\quad\text{almost surely}},\qquad
\boxed{\mathbb E_\nu[r]=\eta},\qquad
\boxed{\mathbb E_\nu[c]=B\mathbb E_\nu[rF(x)]}.
\]
In particular, \(\operatorname{Cov}_\nu(x,h(r))=0\) for every bounded measurable \(h\), and such a measure **must** obey
\[
\boxed{0<\eta<1\quad\text{and}\quad\beta<B\eta H(\chi).}
\]
Consequently, if either requirement fails, the flow has **no nonempty compact forward-invariant subset contained in \(\Omega\)**. Every strictly interior trajectory then satisfies
\[
\liminf_{t\to\infty}\operatorname{dist}((x(t),r(t),c(t)),\partial\Omega)=0.
\]
This excludes interior equilibria, periodic orbits, and all other compact persistent interior invariant dynamics; it does **not** establish global convergence to a particular boundary equilibrium.

The bound \(\mathbb E[rF(x)]\le\eta H(\chi)\) is sharp as a **moment relaxation** under the two constraints \(\mathbb E[r]=\eta\) and \(\mathbb E[x\mid r]=\chi\); sharpness does not assert dynamical attainability.

For a completely rational illustration, take \(N=5\), \(M=3\), \(B=1\), \(\mu_1=1\), \(\mu_2=9\), \(\theta_1=\theta_2=\theta_3=1\), \(\theta_4=8\), \(\alpha=1/2\), \(\beta=2/25\). Then \(\chi=1/10\), \(\eta=4/5\), and
\[
H(\chi)=\frac4{45},\qquad B\eta H(\chi)=\frac{16}{225}<\frac2{25}=\beta.
\]
Therefore no compact interior invariant set exists at these parameters. The weaker upper bound using only the **two marginal means**, without risk-fiber calibration, is \(4/45>2/25\) and cannot yield this exclusion.

## Assumptions and scope

The deterministic, infinite-population mean-field system is
\[
\begin{aligned}
\dot x&=x(1-x)[BF(x)r-c],\\
\dot r&=r(1-r)[\mu_1-(\mu_1+\mu_2)x],\\
\dot c&=(\alpha-c)(c-\beta)[\theta_1-(\theta_1+\theta_2)x-\theta_4+(\theta_3+\theta_4)r].
\end{aligned}
\]
Here \(x\) denotes the fraction cooperating, \(r\) is collective failure risk, and \(c\) is the contribution cost. Positivity of the parameters makes the closed box forward invariant; strictly interior initial values remain interior at all finite times and solutions exist globally. Compact support in the **open** box is essential for bounded logarithmic test functions. The statement concerns Model 1, not its extended risk–cost-coupled Model 2.

## Proof

**Step 1: exact risk-fiber identity.** Put \(m=\mu_1+\mu_2\), so \(\dot r=m r(1-r)(\chi-x)\). Let \(\nu\) be any invariant probability with compact support in \(\Omega\). For any continuous test \(h\) on the compact risk projection, choose a continuously differentiable function \(\Phi\) in its neighborhood with \(\Phi'(r)=h(r)/[r(1-r)]\). Its flow-generator derivative is \(m h(r)(\chi-x)\). Invariance therefore gives
\[
0=\int\!m h(r)(\chi-x)\,d\nu.
\]
Continuous tests determine conditional expectation; hence \(\mathbb E[x\mid r]=\chi\) almost surely. Taking \(h\equiv1\) yields \(\mathbb E x=\chi\), while choosing \(h(r)=r\) gives \(\mathbb E[xr]=\chi\mathbb E r\), and the same reasoning works for every bounded measurable \(h\).

**Step 2: risk and cost averages.** Because the support is bounded away from the cost endpoints, apply invariance to
\[
\Psi(c)=\log\frac{c-\beta}{\alpha-c}.
\]
The exact derivative along the flow is
\[
\dot\Psi=(\alpha-\beta)[\theta_1-\theta_4-(\theta_1+\theta_2)x+(\theta_3+\theta_4)r].
\]
Averaging and substituting \(\mathbb E x=\chi\) proves \(\mathbb E r=\eta\). Since the risk coordinate lies strictly between zero and one, \(0<\eta<1\).

The log odds \(\log[x/(1-x)]\) has derivative \(BF(x)r-c\). Invariance gives \(\mathbb E c=B\mathbb E[rF(x)]\). Compact support implies \(\mathbb E c>\beta\).

**Step 3: sharp pivotal envelope.** Write \(p=M-1\ge1\), \(q=N-M\ge1\), and \(d=p+q-1=N-2\). Set \(u_-=(p-1)/d\), \(u_+=p/d\), and \(K=\binom{p+q}{p}\). Then
\[
H(s)=\begin{cases}
(s/u_-)F(u_-),&0\le s<u_-,\quad p>1,\\
F(s),&u_-\le s\le u_+,\\
((1-s)/(1-u_+))F(u_+),&u_+<s\le1,\quad q>1.
\end{cases}
\]
If \(p=1\), the left segment is absent; if \(q=1\), the right segment is absent. The ratio \(F(s)/s=K s^{p-1}(1-s)^q\) reaches its maximum at \(u_-\) (when \(p>1\)); similarly \(F(s)/(1-s)\) reaches its maximum at \(u_+\) (when \(q>1\)). Therefore the two outer tangent chords dominate \(F\). For the middle segment,
\[
F''(s)=K s^{p-2}(1-s)^{q-2}
[(p+q)(p+q-1)s^2-2p(p+q-1)s+p(p-1)].
\]
The bracket is convex and nonpositive at both \(u_-\) and \(u_+\), so it is nonpositive between them. The three pieces join with matching one-sided slopes; consequently \(H\) is concave and dominates \(F\). Conversely every concave majorant must dominate the outer chords (by its endpoint and tangent-point values) and the central \(F\), proving that \(H\) is the **least** concave majorant. The same endpoint argument covers \(p=1\) or \(q=1\).

**Step 4: conditional Jensen and exclusion.** Conditional on \(r\), the risk-fiber law and Jensen's inequality give
\[
\mathbb E[F(x)\mid r]\le\mathbb E[H(x)\mid r]
\le H(\mathbb E[x\mid r])=H(\chi).
\]
Since \(r>0\), multiply by \(r\) and integrate:
\[
\beta<\mathbb E c=B\mathbb E[rF(x)]\le B\eta H(\chi).
\]
This proves the necessary conditions. If a nonempty compact forward-invariant set existed inside \(\Omega\), the time averages of a trajectory in it would possess a weakly convergent subsequence, whose limit is an invariant probability supported in that compact set (the Krylov–Bogolyubov argument); that contradicts the necessary conditions. Finally, if an interior orbit had positive eventual distance from the boundary, its forward orbit closure after a sufficiently late time would be just such a compact forward-invariant subset. Thus the stated \(\liminf\) vanishes.

**Step 5: moment sharpness, not dynamical sharpness.** For any \(0<\eta<1\), let \(r\) be constant \(\eta\) as an abstract random variable and choose an \(x\)-law with mean \(\chi\) attaining the concave envelope \(H(\chi)\). The relevant law has at most two atoms, at \(\{0,u_-\}\) left of the central interval, at \(\{u_+,1\}\) right of it, or is concentrated at \(\chi\) in the center. Then \(\mathbb E[x\mid r]=\chi\), \(\mathbb E r=\eta\), and \(\mathbb E[rF(x)]=\eta H(\chi)\). Interior-supported laws approximate this value while preserving the two moments by shrinking both coordinates toward their means. These abstract laws need not be invariant for the differential equations.

For the example, \(F(s)=6s^2(1-s)^2\), \(u_-=1/3\), and \(F(u_-)/u_-=8/9\), so \(H(1/10)=4/45\). A mean-only coupling attaining \(\mathbb E[rF(x)]=4/45\) puts masses \(3/10\), \(1/2\), \(1/5\) on \((x,r)=(1/3,1),(0,1),(0,0)\), respectively. Its \(\mathbb E x=1/10\) and \(\mathbb E r=4/5\), but \(\mathbb E[xr]=1/10\ne(1/10)(4/5)\); hence it is forbidden by the risk-fiber law. The genuine conditional ceiling is \(16/225\).

## Verification

`check.py` contains a standard-library exact-rational checker. It verifies the three logarithmic generator identities at rational interior states, the two tangent points and concavity certificates for every \(1\le p,q\le14\), the piecewise upper envelope on rational meshes, and both exact example bounds and moment constructions. Execute `python check.py` from the extracted finding directory; expected output is `VERIFY_OK`. These finite checks support algebraic reproducibility, not the invariant-measure existence theorem, whose proof is analytic.

## Relationship to prior work

Wang et al., *PLOS Computational Biology* 22 (2026), e1013512, introduced exactly these three feedback equations and analyzed boundary/interior equilibrium locations and stability. The inspected full journal article and its publicly described supplemental content concern equilibria, multistability, and an extended Model 2. They do not state the risk-fiber invariant-measure calibration or the parameter-only absence of **all** compact interior recurrent sets. A separately hosted full supplemental PDF could not be materially inspected and remains a specified originality risk.

The previously published published-finding corpus finding *Sharp exact-count envelope under infinite Bernoulli exchangeability* already proves the same **one-variable concave majorant formula** for a binomial point probability. That envelope is used as **prior mathematics**, not presented as new. Its theorem has no evolving risk or cost coordinates and does not imply the risk-conditioned law or the dynamical recurrence obstruction. The published-finding corpus finding *Mutual mean-independence and exact zero covariance in the classical Lotka–Volterra flow* proves an analogous conditional-generator method for a different two-species ODE. It does not determine conditional cooperation in this game or its payoff ceiling. No claim is made that conditional-generator methods themselves are new.

## Limitations

The theorem is a **necessary obstruction**, not a sufficient criterion for persistent interior recurrence when the inequalities hold. The moment envelope is sharp among admissible probability laws, but may be dynamically unattainable. Approaching the state-box boundary along a sequence of times does not imply convergence, extinction, or a unique final attractor. Boundary cycles and boundary equilibria are not excluded. The model assumes deterministic well-mixed infinite-population replicator dynamics, a binomial quorum, and the specific linear feedback structure of Model 1; no empirical inference is claimed. Novelty searches are nonexhaustive, and complete source-supplement comparison is the remaining literature limitation.

## References

1. L. Wang, S. Hua, Y. Liu, L. Zhang, L. Liu and A. Szolnoki, “Coevolutionary dynamics of cooperation, risk, and cost in collective risk games,” *PLOS Computational Biology* **22** (2026), e1013512, first published 2026-02-20, DOI 10.1371/journal.pcbi.1013512. Full HTML: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013512.
2. “Sharp exact-count envelope under infinite Bernoulli exchangeability,” published published-finding corpus record `2026/10/4/SCOPE-sharp-exact-count-envelope-under-infinite-bernoulli-exchangeabil--276990ec2acf`, available at https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-sharp-exact-count-envelope-under-infinite-bernoulli-exchangeabil--276990ec2acf.
3. “Mutual mean-independence and exact zero covariance in the classical Lotka–Volterra flow,” published published-finding corpus record `2026/10/11/SCOPE-mutual-mean-independence-and-exact-zero-covariance-in-the-classi--5a8ff27e72a6`, at https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-mutual-mean-independence-and-exact-zero-covariance-in-the-classi--5a8ff27e72a6.
