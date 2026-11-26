# Sharp finite-time herding error and polarization penalty under complete mixing

## Finding

In the synchronous random-actions model with complete interaction including self-actions and fresh conditional action draws, let \(n\ge2\), \(0<\alpha\le1\), and \(x(0)\in[0,1]^n\) be deterministic. Set
\[
p_t=n^{-1}\sum_i x_i(t),\qquad D_0=\sum_i(x_i(0)-p_0)^2,\qquad
r=1-\alpha^2/n,\quad s=(1-\alpha)^2.
\]
Then \(0\le s<r<1\) and all opinions converge almost surely to a common bit \(B\) with \(\Pr(B=1)=p_0\). For every integer \(t\ge0\), the exact mean-squared error to that bit is
\[
E_t:=\mathbb E[(p_t-B)^2]=p_0(1-p_0)r^t+\frac{\alpha^2D_0}{n^2}\frac{r^t-s^t}{r-s}.
\]
The individual errors and unconditional covariances are
\[
\mathbb E[(x_i(t)-B)^2]=E_t+s^t(x_i(0)-p_0)^2,\qquad
\operatorname{Cov}(x_i(t),x_j(t))=p_0(1-p_0)-E_t.
\]
The covariance matrix is a nonnegative multiple of the all-ones matrix (thus of rank at most one).

At fixed \(n,\alpha,p_0\), the error \(E_t\) is strictly increasing in the feasible dispersion \(D_0\) for every \(t\ge1\). Write \(m=\lfloor np_0\rfloor\) and \(\theta=np_0-m\). Its full feasible interval is \([0,m+\theta^2-np_0^2]\). A homogeneous profile attains the lower endpoint. A profile with \(m\) ones, one entry \(\theta\) if \(\theta>0\), and all remaining entries zero attains the upper endpoint. For \(0<p_0<1\), the leading rate is exactly \(r\), with
\[
\lim_{t\to\infty}\frac{E_t}{p_0(1-p_0)r^t}
=1+\frac{\alpha^2D_0}{n^2(r-s)p_0(1-p_0)}.
\]
At \(t=0\) the formula uses \(s^0=1\), including when \(\alpha=1\). The means \(p_0=0,1\) give constant paths, with no nontrivial dispersion comparison.

## Assumptions and scope

Let \(\mathcal F_t=\sigma(x(0), A(0),\ldots,A(t-1))\) be the entire history just before the time-\(t\) action draw. **Conditional on \(\mathcal F_t\)**, the actions \(A_i(t)\in\{0,1\}\) are mutually independent Bernoulli variables with success probabilities \(x_i(t)\). In particular the product-Bernoulli law at each step does not depend on earlier actions except through the current state; prescribing only the law conditional on the current state without this transition assumption is not sufficient. The synchronous update is
\[
x_i(t+1)=(1-\alpha)x_i(t)+\frac\alpha n\sum_{j=1}^n A_j(t).
\]
The interaction matrix is \(J_n/n\), not the loopless complete-graph matrix. The result does not apply as stated to arbitrary interactions, other update protocols, dependent actions conditional on the history, or random initial beliefs.

## Proof

Subtract the population mean from each update to get \(x_i(t)-p_t=(1-\alpha)^t(x_i(0)-p_0)\) pathwise. The deviations sum to zero, and their squares sum to \(s^t D_0\). By the conditional product law,
\[
\mathbb E[p_{t+1}\mid\mathcal F_t]=p_t,\qquad
\operatorname{Var}(p_{t+1}\mid\mathcal F_t)=\frac{\alpha^2}{n^2}\sum_i x_i(t)(1-x_i(t))
=\frac{\alpha^2}{n^2}(np_t(1-p_t)-s^tD_0).
\]
Consequently \(h_t=\mathbb E[p_t(1-p_t)]\) satisfies \(h_{t+1}=rh_t+(\alpha^2/n^2)D_0s^t\) with \(h_0=p_0(1-p_0)\). Here \(r-s=\alpha(2-\alpha-\alpha/n)>0\). Summing the geometric convolution solves the recurrence and gives the displayed formula for \(E_t\) with \(h_t\) in its place.

Bounded martingale convergence gives \(p_t\to B\) almost surely and in every finite \(L^u\), \(u\ge1\). The explicit formula implies \(h_t\to0\), so \(\mathbb E[B(1-B)]=0\) and \(B\in\{0,1\}\) almost surely. The deviations vanish, giving convergence of every opinion, and \(\mathbb E[B]=p_0\). Because the mean is the conditional expectation \(p_t=\mathbb E[B\mid\mathcal F_t]\), its squared error conditional on the history is \(p_t(1-p_t)\). Thus \(E_t=h_t\). Expanding the squared error of \(x_i(t)\) about \(p_t\), the cross term vanishes by conditional centering. The deterministic deviations also give \(\operatorname{Cov}(x_i(t),x_j(t))=\operatorname{Var}(p_t)=p_0(1-p_0)-h_t\).

The coefficient of \(D_0\) in \(E_t\) is positive for every positive \(t\). Its minimum feasible value is zero by nonnegativity, attained at equal opinions. To maximize \(D_0=\sum_i x_i(0)^2-np_0^2\), if two coordinates are strictly interior, vary them at fixed sum until one reaches an endpoint of \([0,1]\); by convexity one endpoint of the variation interval does not decrease the objective. Iteration leaves at most one interior coordinate, giving exactly the stated maximal profile. Interpolating between the homogeneous profile and a maximizing profile with weight \(\lambda\in[0,1]\) on the latter gives dispersion \(\lambda^2D_{\max}\), filling the interval. Finally \((s/r)^t\to0\) proves the leading factor for interior \(p_0\).

## Verification and limits

The unchanged companion `verify.py` propagates finite rational laws under the product-Bernoulli transition. The frozen package records 80 exact configurations, 380 time slices and 117 dispersion-grid profiles. Its terminal-error check uses the conditional law of \(B\) established by the proof. These checks are corroborative only, not an unbounded-time convergence proof or an exhaustive test of real profiles. For example, at \(n=2,\alpha=1/2,p_0=1/2,t=1\), the profiles \((1/2,1/2)\) and \((0,1)\) give errors \(7/32\) and \(1/4\), respectively: the first mean has variance \(1/32\), whereas the second is deterministic at this step.

## Relationship to prior work

Leshem and Scaglione introduce the model and analyze convergence and martingale variance in general networks [1]. Abrahamsson, Danev and Larsson study related extensions and convergence [2, 3]; [3] establishes almost-sure convergence and convergence in moments under broader network hypotheses and discusses the conditioning needed in the variance argument. Binary herding, the weighted-mean martingale, and conditional variance are not claimed as new. The exact finite-horizon error here comes from closing and solving the two-mode moment recurrence using pathwise deterministic disagreement in complete mixing, and yields the sharp effect of fixed-mean dispersion. Its rate concerns ensemble mean-square error to the limiting bit, not a late-path slope or error to a deterministic truth.

## References

1. A. Leshem and A. Scaglione, *The Impact of Random Actions on Opinion Dynamics*, [arXiv:1704.01660](https://arxiv.org/abs/1704.01660).
2. O. Abrahamsson, D. Danev and E. G. Larsson, *On the Impact of Random Actions on Opinion Dynamics*, [arXiv:2012.15154](https://arxiv.org/abs/2012.15154).
3. O. Abrahamsson, D. Danev and E. G. Larsson, *Strong Convergence of a Random Actions Model in Opinion Dynamics*, [arXiv:2401.16574](https://arxiv.org/abs/2401.16574).
