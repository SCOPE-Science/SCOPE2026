# Vanishing-response opinion biases: subgeometric consensus and exact logarithmic accuracy laws

## Finding
Consider synchronous scalar opinion updates on any finite strongly connected weighted influence digraph. For continuous, strictly receptive disagreement responses with **vanishing ratio to disagreement** at zero, every initially nonunanimous trajectory reaches consensus, yet its opinion diameter \(D_t\) obeys
\[
0<D_{t+1}\le D_t,\qquad \lim_{t\to\infty}\frac{D_{t+1}}{D_t}=1,\qquad \lim_{t\to\infty}D_t^{1/t}=1.
\]
Thus even strong connectivity does not supply an exponential rate when the local response vanishes faster than the disagreement. This holds for heterogeneous responses on all directed edges, not just identical agents or reciprocal networks.

For two reciprocal agents with the flat odd bias \(\beta_\alpha(s)=\operatorname{sgn}(s)\exp(-|s|^{-\alpha})\), \(\alpha\ge1\), the positive gap \(d_t\) satisfies the **sharp three-term law**
\[
d_t^{-\alpha}=\log t+\left(1+\frac1\alpha\right)\log\log t+\log(2\alpha)+o(1).
\]
The number \(T_\alpha(\varepsilon)\) of updates needed to reduce the gap to \(\varepsilon\) satisfies
\[
T_\alpha(\varepsilon)\sim\frac{\varepsilon^{\alpha+1}}{2\alpha}\exp(\varepsilon^{-\alpha})\qquad(\varepsilon\downarrow0).
\]
In particular, the explicitly simulated flat bias in Alvim–Gaspar da Silva–Knight–Valencia (2024) has \(d_t^{-1}=\log t+2\log\log t+\log2+o(1)\). By contrast, for any nonzero odd bias analytic near zero with leading term \(\beta(s)=a s^m+O(s^{m+2})\), the two-agent gap has geometric asymptotics when \(m=1\) and a polynomial law \(d_t\sim[2a(m-1)t]^{-1/(m-1)}\) when the first nonzero order is \(m\ge3\). These conclusions together give a regularity-dependent quantitative boundary for consensus speed in the same opinion-update mechanism.

## Assumptions and scope
There are \(n\ge2\) agents with opinions \(x_i(t)\in[0,1]\). For each receiving agent \(i\), weights \(w_{ij}\ge0\) satisfy \(\sum_{j=1}^n w_{ij}=1\). The directed edge \(j\to i\) exists whenever \(i\ne j\) and \(w_{ij}>0\); the graph is strongly connected. Self-influence is permitted, but not required. For each ordered pair with positive weight, \(\beta_{ij}:[-1,1]\to[-1,1]\) is continuous, \(\beta_{ij}(0)=0\), and there is a *single* constant \(0<\theta<1/2\) such that for every \(s\ne0\),
\[
0<\frac{\beta_{ij}(s)}s\le\theta,
\qquad \lim_{s\to0}\frac{\beta_{ij}(s)}s=0.
\]
No oddness or differentiability is required in the graph-wide assertion. The update is
\[
x_i(t+1)=x_i(t)+\sum_j w_{ij}\beta_{ij}(x_j(t)-x_i(t)).
\]
The source model includes an outer truncation to \([0,1]\), but it is inactive under these hypotheses. Write \(D_t=\max_i x_i(t)-\min_i x_i(t)\) and assume \(D_0>0\). The two-agent assertions specialize to \(w_{12}=w_{21}=1\), identical odd responses in both directions and initial gap \(d_0\in(0,1]\). Their original mean opinion is conserved. In the contrasting analytic comparison, the flatness limit is *replaced* by the assumption that the common odd response is nonzero and real analytic near zero; the same strict receptiveness and uniform bound remain in force globally.

## Proof
**1. Convex hull, persistence and consensus.** Set \(q_{ij}(s)=\beta_{ij}(s)/s\) for \(s\ne0\), and \(q_{ij}(0)=0\). Then \(q_{ij}\in[0,\theta]\) and the update is a convex combination of the old opinions: the coefficients of \(x_j\), \(j\ne i\), are \(w_{ij}q_{ij}(x_j-x_i)\), while the coefficient of \(x_i\) is \(1-\sum_{j\ne i}w_{ij}q_{ij}(x_j-x_i)\ge1-\theta>0\). Consequently the minimum is nondecreasing, the maximum nonincreasing and the entire trajectory remains in the initial convex hull.

Let \(b(r)=\max_{i,j:w_{ij}>0}\max_{|s|\le r}|\beta_{ij}(s)|\). At a maximizing old coordinate, its new value is no smaller than its old value minus \(b(D_t)\); analogously a minimizing coordinate rises by at most \(b(D_t)\). Hence
\[
D_t-2b(D_t)\le D_{t+1}\le D_t,\qquad b(D_t)\le\theta D_t,
\]
which proves \(D_{t+1}\ge(1-2\theta)D_t>0\) and excludes finite-time consensus.

To prove asymptotic consensus, fix any state with nonzero diameter \(D\) and original maximum \(M\). An agent strictly below \(M\) stays strictly below \(M\) after one update, because its own coefficient is strictly positive and no input exceeds \(M\). Any agent with an incoming positive-weight edge from one strictly below \(M\) also becomes strictly below \(M\) at the next step, by the strict positivity of \(\beta_{ij}(s)/s\) whenever \(s\ne0\). Strong connectivity propagates the set of agents below \(M\) through all vertices in at most \(n-1\) steps. Therefore \(\max_i x_i(n-1)<M\); the symmetric argument raises the minimum above its old value. The minimum and maximum of the trajectory tend to limits \(L\le U\). If \(L<U\), choose a convergent subsequence of states \(x(t_k)\to z\), with diameter \(U-L>0\). Continuity of the update and the existence of those extremal limits imply that the first \(n-1\) iterates from \(z\) maintain maximum \(U\) and minimum \(L\). This contradicts strict extreme contraction just proved. Thus \(L=U\), and every coordinate converges to the same opinion.

Since the graph has finitely many edges and each response is flat, \(b(r)/r\to0\) as \(r\downarrow0\). The diameter inequality, together with \(D_t\downarrow0\), yields \(D_{t+1}/D_t\to1\). Finally, telescoping \(\log D_t=\log D_0+\sum_{j<t}\log(D_{j+1}/D_j)\) and taking Cesàro means gives \(t^{-1}\log D_t\to0\), hence \(D_t^{1/t}\to1\). In fact \(D_t/c^t\to\infty\) for every \(0<c<1\).

**2. The flat two-agent law.** For every \(\alpha\ge1\) and \(0<s\le1\), \(\exp(-s^{-\alpha})/s\le e^{-1}<1/2\). Thus \(\beta_\alpha\) meets the global hypotheses, for instance with \(\theta=2/5\). Oddness gives the exact scalar recurrence
\[
d_{t+1}=d_t-2e^{-d_t^{-\alpha}},\qquad d_t\downarrow0.
\]
Put \(y_t=d_t^{-\alpha}\) and \(b=1+1/\alpha\). Because \(u_t=2y_t^{1/\alpha}e^{-y_t}\to0\), the binomial expansion of \(y_{t+1}=y_t(1-u_t)^{-\alpha}\) yields
\[
y_{t+1}-y_t=2\alpha y_t^b e^{-y_t}(1+O(u_t)),\qquad y_{t+1}-y_t\to0.
\]
For \(H(y)=e^y y^{-b}\), the mean-value theorem and \(H'(y)=H(y)(1-b/y)\) give \(H(y_{t+1})-H(y_t)\to2\alpha\). Therefore \(H(y_t)/t\to2\alpha\) by Cesàro summation, or equivalently
\[
y_t-b\log y_t=\log t+\log(2\alpha)+o(1).
\]
First \(y_t/\log t\to1\); substituting \(\log y_t=\log\log t+o(1)\) proves the three-term formula. For fixed \(d_0>0\) and \(T_\alpha(\varepsilon)=\min\{t:d_t\le\varepsilon\}\), the threshold \(y=\varepsilon^{-\alpha}\) is crossed with overshoot \(y_{T}-\varepsilon^{-\alpha}\to0\), because the increments tend to zero. Hence \(H(y_T)\sim H(\varepsilon^{-\alpha})\); combining with \(H(y_t)\sim2\alpha t\) proves the hitting-time equivalence.

**3. Analytic comparison.** If an odd nonzero bias analytic near zero has first nonzero Taylor term \(a s^m\), then strict receptiveness gives \(a>0\) and \(m\) an odd positive integer. The same reciprocal two-agent gap satisfies \(d_{t+1}=d_t-2ad_t^m+O(d_t^{m+2})\). For \(m=1\), \(d_{t+1}/d_t\to1-2a\in(0,1)\), an exponential rate. For \(m\ge3\), the mean-value expansion gives \(d_{t+1}^{-(m-1)}-d_t^{-(m-1)}\to2a(m-1)\), so Cesàro summation proves \(d_t\sim[2a(m-1)t]^{-1/(m-1)}\). The two-agent assumptions already ensure \(d_t>0\) and \(d_t\to0\).

## Verification
Run `python3 verify.py` using the attached standalone script. It performs three transitions in a heterogeneous four-node directed cycle with exact rational arithmetic, verifies convex-hull and diameter inequalities, checks two flat-bias recurrences with the original normalization, and checks two exact-rational transitions for each of three analytic powers. All checks passed in the package preparation. The graph-wide and asymptotic conclusions follow from the proofs, **not** from finite simulation; the finite floating-point computations do not certify the asymptotic constants or eventual inequalities.

## Relationship to prior work
Alvim, Gaspar da Silva, Knight and Valencia (arXiv:2402.17615v1, 27 February 2024), Definition 3 and Theorem 3.1, establish receptive-resistance consensus on strongly connected influence graphs and explicitly simulate the \(\alpha=1\) flat bias with qualitatively slow convergence in their Figure 5. The present conclusion quantifies that **same displayed example** to three asymptotic orders and gives the exact tolerance-time scale; its graph-wide no-geometric-rate theorem also covers heterogeneous responses. Paz and coauthors (arXiv:2409.10809v1, Theorem 4.1 and Theorem 4.2) prove consensus for generalized bias factors without quantitative estimates of the present form. The earlier Alvim and coauthors confirmation-bias model (arXiv:2112.09542) treats polarization/convergence and equilibrium values but not the flat-response inverse-logarithmic law. Baković and coauthors (arXiv:2403.03913v1) analyze a different multidimensional simplex-normalization model; its equilibria and stability results do not imply a bound for this disagreement-response recurrence. The standard theory of scalar slowly varying and parabolic recurrences can supply ingredients of Step 2; claiming novelty for these analytic tools in isolation is not intended.

## Limitations
The general graph claim requires a finite fixed strongly connected graph, uniform strict receptiveness, and flatness at zero on **every positive-weight edge**. It asserts the diameter's one-step ratio, not a universal graph-specific equivalent: differing edge responses can give distinct slow decay profiles. In the two-agent formulas, biases are symmetric and odd, and all estimates concern the deterministic synchronous model. The stated tolerance law is asymptotic as \(\varepsilon\downarrow0\); finite tolerances can have substantial preasymptotic effects, particularly for large \(\alpha\). The present literature comparison does not exclude unindexed nonlinear-iteration results that may imply one of these consequences. Independent validation has not been performed.

## References
1. M. S. Alvim, A. Gaspar da Silva, S. Knight, F. Valencia, *A Multi-Agent Model for Opinion Evolution under Cognitive Biases*, arXiv:2402.17615v1 (2024-02-27), https://arxiv.org/html/2402.17615v1 (Definition 3, Theorem 3.1, Figure 5, proof and appendix).
2. J. Paz and coauthors, *Consensus in Models for Opinion Dynamics with Generalized-Bias*, arXiv:2409.10809v1 (2024-09-17), https://arxiv.org/html/2409.10809v1 (Theorems 4.1–4.3).
3. M. S. Alvim, B. Amorim, S. Knight, S. Quintero, F. Valencia, *A Formal Model for Polarization under Confirmation Bias in Social Networks*, arXiv:2112.09542 (first publicly posted 2021-12), https://arxiv.org/html/2112.09542 (Sections 4–5).
4. L. Baković, D. Ohlin, G. Como, E. Tegling, *Multipolar Opinion Evolution in Biased Networks*, arXiv:2403.03913v1 (2024-03-06), https://arxiv.org/html/2403.03913v1 (model, analysis and conclusions).
