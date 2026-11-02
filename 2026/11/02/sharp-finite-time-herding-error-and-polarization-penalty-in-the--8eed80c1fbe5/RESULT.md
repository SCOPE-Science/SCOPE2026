# Sharp finite-time herding error and polarization penalty in the complete-mixing random-actions model

## Finding

In a synchronous random-actions opinion system with uniform complete interaction (including self-actions), the exact mean-squared distance to eventual binary consensus is a two-exponential expression. The result also determines the finite-time covariance matrix and the *sharp* effect of initial opinion dispersion at a fixed population mean. Specifically, for every integer \(n\ge2\), learning weight \(0<\alpha\le1\), deterministic initial vector \(x(0)\in[0,1]^n\), and integer \(t\ge0\), let
\[
 p_0=\frac1n\sum_{i=1}^{n}x_i(0),\quad
 D_0=\sum_{i=1}^{n}(x_i(0)-p_0)^2,\quad
 r=1-\frac{\alpha^2}{n},\quad s=(1-\alpha)^2.
\]
Then \(0\le s<r<1\), the dynamics converges almost surely to a common binary opinion \(B\in\{0,1\}\) with \(\Pr(B=1)=p_0\), and
\[
\boxed{\mathbb E[(p_t-B)^2]=p_0(1-p_0)r^t+\frac{\alpha^2D_0}{n^2}\frac{r^t-s^t}{r-s}},\qquad p_t=\frac1n\sum_i x_i(t).
\]
The individual errors and all unconditional covariances are also exact:
\[
\mathbb E[(x_i(t)-B)^2]=\mathbb E[(p_t-B)^2]+s^t(x_i(0)-p_0)^2,
\]
\[
\operatorname{Cov}(x_i(t),x_j(t))=p_0(1-p_0)-\mathbb E[(p_t-B)^2]\quad(1\le i,j\le n).
\]
Consequently the finite-time opinion covariance matrix is a nonnegative multiple of the all-ones matrix, even when the initial opinions are heterogeneous.

For fixed \(n\), \(\alpha\), \(p_0\), and every integer \(t\ge1\), the mean-squared consensus error is **strictly increasing** in \(D_0\). This comparison is sharp across *all* initial opinion vectors with that mean. Writing \(m=\lfloor np_0\rfloor\) and \(\theta=np_0-m\), the precise feasible interval of dispersion is
\[
 0\le D_0\le D_{\max}=m+\theta^2-np_0^2.
\]
The lower endpoint is attained at the homogeneous initial opinion \(x_i(0)=p_0\). The upper endpoint is attained by \(m\) opinions equal to one, one opinion equal to \(\theta\) if \(\theta>0\), and all remaining opinions equal to zero. Both endpoints yield equality in the corresponding error bounds. If \(0<p_0<1\), the asymptotic geometric factor is exactly \(r\), and the diversity penalty persists in its leading multiplicative constant: 
\[
\lim_{t\to\infty}\frac{\mathbb E[(p_t-B)^2]}{p_0(1-p_0)r^t}=
1+\frac{\alpha^2D_0}{n^2(r-s)p_0(1-p_0)}.
\]
In particular, increasing initial polarization at fixed mean does not alter the eventual probability of consensus on one, but increases the expected squared error at *every positive finite time*.

## Assumptions and scope

There are \(n\ge2\) agents, and \(x_i(t)\in[0,1]\) is agent \(i\)'s action-one probability at discrete time \(t\). Given the entire belief vector at time \(t\), the simultaneous actions \(A_i(t)\in\{0,1\}\) are mutually independent with \(A_i(t)\sim\operatorname{Bernoulli}(x_i(t))\). The synchronous update is
\[
 x_i(t+1)=(1-\alpha)x_i(t)+\frac\alpha n\sum_{j=1}^{n}A_j(t),
 \qquad i=1,\ldots,n,
\]
with the same \(0<\alpha\le1\) for all agents. Every agent observes the *same* average of all \(n\) actions, including their own, so the trust matrix is \(J_n/n\), not the loopless complete-graph matrix. Initial opinions are deterministic. The initial vectors are not assumed exchangeable, interior, or equal. No claim is made about arbitrary trust matrices, delayed observations, asynchronous updates, or dependent actions.

## Proof

Put \(p_t=n^{-1}\sum_i x_i(t)\) and \(d_i=x_i(0)-p_0\). Subtracting the population mean from each simultaneous update gives the **pathwise identity**
\[
 x_i(t)-p_t=(1-\alpha)^t d_i.
\]
In particular, \(\sum_i d_i=0\) and \(\sum_i(x_i(t)-p_t)^2=s^tD_0\). Conditional on the opinions at time \(t\), independence of Bernoulli actions gives
\[
\mathbb E[p_{t+1}\mid\mathcal F_t]=p_t,
\quad
\operatorname{Var}(p_{t+1}\mid\mathcal F_t)=\frac{\alpha^2}{n^2}\sum_{i=1}^{n}x_i(t)(1-x_i(t)).
\]
By expanding the squares about \(p_t\),
\[
\sum_i x_i(t)(1-x_i(t))=np_t(1-p_t)-s^tD_0.
\]
Define \(h_t=\mathbb E[p_t(1-p_t)]\). Taking conditional expectations of \(p_{t+1}(1-p_{t+1})\) yields the exact linear inhomogeneous recurrence
\[
 h_{t+1}=\left(1-\frac{\alpha^2}{n}\right)h_t+\frac{\alpha^2D_0}{n^2}s^t,
\quad h_0=p_0(1-p_0).
\]
Since \(r-s=\alpha(2-\alpha-\alpha/n)>0\) for \(n\ge2\) and \(0<\alpha\le1\), solving the recurrence proves
\[
 h_t=p_0(1-p_0)r^t+\frac{\alpha^2D_0}{n^2}\frac{r^t-s^t}{r-s}.
\]
The mean \(p_t\) is a bounded martingale, so \(p_t\to B\) almost surely and in every finite \(L^q\). The displayed formula shows \(h_t\to0\). Consequently \(\mathbb E[B(1-B)]=0\), and since \(B\in[0,1]\) almost surely, \(B\in\{0,1\}\) almost surely. The pathwise deviation identity implies \(x_i(t)\to B\) for every agent. Since \(\mathbb E[B]=p_0\), its success probability is \(p_0\).

The martingale convergence property gives \(\mathbb E[B\mid\mathcal F_t]=p_t\). Therefore \(\mathbb E[(p_t-B)^2\mid\mathcal F_t]=p_t(1-p_t)\), so the previously computed \(h_t\) is exactly the future-consensus mean-squared error, not merely an uncertainty proxy. Expanding \(x_i(t)-B=(p_t-B)+(1-\alpha)^td_i\), then using \(\mathbb E[p_t-B]=0\), proves each individual error formula. Since all centered differences \(x_i(t)-p_t\) are deterministic, \(\operatorname{Cov}(x_i(t),x_j(t))=\operatorname{Var}(p_t)\); and \(\mathbb E[p_t]=p_0\) implies \(\operatorname{Var}(p_t)=p_0(1-p_0)-h_t\). This proves the rank-one covariance identity.

For any \(t\ge1\), \((r^t-s^t)/(r-s)>0\). Hence the error varies strictly and affinely with dispersion \(D_0\) at fixed \(p_0\). Jensen's inequality gives its minimum \(D_0=0\). For the maximum, note \(D_0=\sum_i x_i(0)^2-np_0^2\). With fixed sum \(\sum_i x_i(0)=np_0\), moving mass between two strictly interior coordinates until one hits zero or one does not decrease the sum of squares, since a convex quadratic achieves its maximum at an interval endpoint. Iteration leaves at most one strictly interior coordinate, giving \(D_{\max}=m+\theta^2-np_0^2\). Both extremal profiles are admissible. Every intermediate dispersion is also attainable by interpolating between the homogeneous and maximizing profiles: \(x_i^{(\lambda)}=p_0+\lambda(x_i^{\max}-p_0)\) for \(0\le\lambda\le1\) has dispersion \(\lambda^2D_{\max}\). Finally \(s<r\) makes the second exponential negligible relative to \(r^t\), yielding the stated asymptotic ratio when \(p_0(1-p_0)>0\). The boundary \(p_0\in\{0,1\}\) is deterministic and covered by the exact formula, but not by that ratio.

## Verification

A standard-library Python exact-rational verifier (`verify.py`) recursively enumerates the entire finite-time distribution of \(p_t\), using the conditional Poisson-binomial distribution of the independent actions and the deterministic disagreement identity. It compares the resulting moment against the closed form, checks individual squared errors and covariance identities, and separately checks strict dispersion comparisons and sharp boundary profiles. Its executed output was: `PASS 80 exact finite-state configurations, 380 time slices; 117 dispersion-boundary grid profiles; individual/covariance/strict comparisons PASS`. Run `python3 verify.py` from the package directory. This is a finite rational check and **not** the proof for arbitrary \(n\), arbitrary real \(\alpha\), or unbounded time; the preceding argument supplies those universal steps.

## Relationship to prior work

Leshem and Scaglione's 2017 public preprint establishes the random-actions synchronous update, conditional independence and martingale-based binary-herding conclusion for irreducible networks. It also studies rates numerically and gives a late-stage pathwise exponential heuristic. Those facts are credited; the present claim instead gives a uniform complete-interaction *finite-horizon exact \(L^2\) error*, the rank-one covariance law, and sharp dependence on arbitrary initial dispersion. Its factor \(1-\alpha^2/n\) measures ensemble mean-square error, not the same quantity as a pathwise late-stage exponential slope.

Abrahamsson, Danev and Larsson's 2020 public preprint analyzes random-actions consensus with stubborn and drifting agents and critically discusses the original convergence proof. Their January 2024 work establishes strong convergence and convergence in moments under broader hypotheses. The 2020 full public text and 2024 abstract were examined. The 2024 full text could not be accessed, so possible previously published finite-time identities in that source remain a priority risk; no novelty follows merely from a search not finding them. This proof of convergence in the present complete-mixing case is independent of the disputed general argument.

## Limitations

The rank-one structure relies on every agent receiving the same average of all actions. It does not describe general sparse or heterogeneous networks. The target variable \(B\) is the *limiting binary consensus*, not a deterministic social truth. All expectations are over random actions conditional on the fixed initial vector; a random initial-vector distribution would require an additional expectation. Finite tests are corroborative and not exhaustive. Research novelty and correctness have not been independently audited; the material-access residual risk for the related 2024 paper remains.

## References

1. A. Leshem and A. Scaglione, “The impact of random actions on opinion dynamics,” first public arXiv posting 2017-04-05, https://arxiv.org/abs/1704.01660 . Full online text and model/appendix were inspected.
2. O. Abrahamsson, D. Danev and E. G. Larsson, “On the Impact of Random Actions on Opinion Dynamics,” first public arXiv posting 2020-12-30, https://arxiv.org/abs/2012.15154 .
3. O. Abrahamsson, D. Danev and E. G. Larsson, “Strong Convergence of a Random Actions Model in Opinion Dynamics,” first public arXiv posting 2024-01-29, https://arxiv.org/abs/2401.16574 . Full text was not accessible; abstract was inspected.
