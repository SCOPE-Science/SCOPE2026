# A shape-dependent sharp covariance threshold for symmetric Dirichlet samples

## Finding

Let \(n\ge2\), \(\alpha>0\), and let \(X=(X_1,\ldots,X_n)\sim\operatorname{Dirichlet}_n(\alpha,\ldots,\alpha)\). For \(0<t<1\), define the exceedance count
\[
K_t=\sum_{i=1}^n\mathbf1_{\{X_i>t\}}.
\]
For every \(\varphi\in C^2([0,1])\) with \(\varphi''(s)>0\) throughout \(0<s<1\), let \(F_\varphi=\sum_i\varphi(X_i)\). There exists exactly one threshold \(t_\varphi(n,\alpha)\in(0,1)\) such that
\[
\operatorname{Cov}(K_t,F_\varphi)<0\quad(0<t<t_\varphi),\qquad
\operatorname{Cov}(K_t,F_\varphi)=0\quad(t=t_\varphi),\qquad
\operatorname{Cov}(K_t,F_\varphi)>0\quad(t_\varphi<t<1).
\]

For the quadratic concentration statistic \(Q=\sum_iX_i^2\), write \(\beta=(n-1)\alpha\) and \(A=n\alpha\), and let \(B\) denote Euler's beta function. Then the *exact* covariance is
\[
\boxed{\operatorname{Cov}(K_t,Q)=
\frac{n\,t^{\alpha}(1-t)^\beta}{B(\alpha,\beta)(\beta+1)(A+1)}
\big((A+2)t-(\alpha+1)\big).}
\]
Consequently its unique interior zero is
\[
\boxed{t_Q(n,\alpha)=\frac{\alpha+1}{n\alpha+2}.}
\]
For \(n>2\), this threshold decreases strictly as \(\alpha\) increases, from the limit \(1/2\) as \(\alpha\downarrow0\) to the limit \(1/n\) as \(\alpha\to\infty\). For \(n=2\), the threshold is exactly \(1/2\) for all \(\alpha>0\). When \(\alpha=1\), the coordinates are uniform spacings and the formula reduces to the previously established uniform-simplex relation.

## Assumptions and scope

The distribution is a **symmetric** Dirichlet law with \(n\ge2\) coordinates and arbitrary real \(\alpha>0\). The strict single-crossing statement holds for every twice-continuously differentiable score satisfying strictly positive curvature on the open unit interval; adding an affine function to \(\varphi\) changes \(F_\varphi\) only by a constant, hence does not change its covariance. The inequalities are strict for every \(0<t<1\) other than the single zero. The endpoints \(t=0,1\) give degenerate exceedance counts and are excluded from uniqueness. The scalar \(Q\) is also called Simpson concentration, and for \(\alpha=1\) it is Greenwood's spacing statistic when \(n\) is the number of gaps, not the number of sampled interior points.

## Proof

**Conditional regression.** Put \(\mu=\mathbb E F_\varphi\), let \(S=X_1\sim\operatorname{Beta}(\alpha,\beta)\), and use Dirichlet neutrality: conditional on \(S=s\), the normalized remaining coordinates form an independent \(Y\sim\operatorname{Dirichlet}_{n-1}(\alpha,\ldots,\alpha)\). With the convention \(Y=(1)\) for \(n=2\),
\[
g(s):=\mathbb E[F_\varphi\mid S=s]
=\varphi(s)+(n-1)\mathbb E\varphi((1-s)Y_1).
\]
Thus \(g''(s)=\varphi''(s)+(n-1)\mathbb E[Y_1^2\varphi''((1-s)Y_1)]>0\) for \(0<s<1\). By exchangeability,
\[
\operatorname{Cov}(K_t,F_\varphi)
=n\int_t^1(g(s)-\mu)w_{\alpha,\beta}(s)\,ds,
\quad w_{\alpha,\beta}(s)=\frac{s^{\alpha-1}(1-s)^{\beta-1}}{B(\alpha,\beta)}.
\]

**Both endpoint regressions exceed the mean.** Subtract an affine function and write \(f(s)=\varphi(s)-\varphi(0)-s\varphi'(0)\). Then \(f(0)=0\) and \(f(s)/s\) is strictly increasing on \((0,1]\). For a symmetric \(m\)-coordinate Dirichlet vector \(Z\), the size-biased pick from its coordinates has distribution \(W_m\sim\operatorname{Beta}(\alpha+1,(m-1)\alpha)\), with \(W_1=1\). Therefore
\[
\mathbb E\sum_{i=1}^m f(Z_i)
=\mathbb E\frac{f(W_m)}{W_m}.
\]
Since \(W_{n-1}\) strictly stochastically dominates \(W_n\), including when \(n=2\) and \(W_1=1\), this expectation is strictly larger for \(m=n-1\) than for \(m=n\). Consequently \(g(0)>\mu\). Also \(\sum_i f(X_i)<f(1)\) almost surely, by strict convexity, \(f(0)=0\), and positivity of the interior Dirichlet coordinates. Hence \(g(1)>\mu\).

**Exactly one crossing.** The strictly convex continuous function \(h=g-\mu\) is positive at both endpoints, while \(\mathbb E h(S)=0\). Therefore its negative set is one nonempty interval \((u,v)\subset(0,1)\); \(h>0\) on \((0,u)\cup(v,1)\). Define \(H(t)=\int_t^1h(s)w_{\alpha,\beta}(s)\,ds\), so \(H(0)=H(1)=0\) and \(H'(t)=-h(t)w_{\alpha,\beta}(t)\). It follows that \(H<0\) on \((0,u]\), \(H>0\) on \([v,1)\), and \(H\) is strictly increasing on \((u,v)\). It therefore has one and only one interior zero, with the asserted sign pattern.

**Quadratic computation.** For \(\varphi(s)=s^2\), Dirichlet moments yield
\[
\mu=\frac{\alpha+1}{A+1},\qquad
c=\frac{\alpha+1}{\beta+1},\qquad
g(s)=s^2+c(1-s)^2.
\]
Set
\[
R(t)=\frac{t^\alpha(1-t)^\beta}{B(\alpha,\beta)(\beta+1)(A+1)}\big((A+2)t-(\alpha+1)\big).
\]
Direct differentiation using \(A=\alpha+\beta\) gives \(R'(t)=-(g(t)-\mu)w_{\alpha,\beta}(t)\), and \(R(1)=0\). Thus \(H(t)=R(t)\), proving the covariance identity after multiplication by \(n\). The remaining threshold and shape-parameter monotonicity claims are immediate; explicitly, for \(n>2\), \(\partial_\alpha t_Q=(2-n)/(n\alpha+2)^2<0\).

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It carries out 4,156 exact rational checks using independent beta-tail polynomial integrations for positive integer shape parameters, and checks several higher polynomial convex scores. The quadratic formula was additionally checked algebraically by differentiating its displayed beta-tail antiderivative. These finite computations corroborate but do **not** replace the proof for arbitrary real \(\alpha>0\), arbitrary sample size, or arbitrary admissible \(\varphi\).

## Relationship to prior work

Royen's 2010 study of Dirichlet square sums and Greenwood's statistic derives exact *marginal distributions* for \(Q\), for general Dirichlet parameters, but its results do not present the joint threshold-exceedance covariance. A prior uniform-simplex calculation (identifier `8cec2684-e10a-4f25-bc74-47e4588a92c0`) established the corresponding convex-score sign change only for \(\alpha=1\) and the Greenwood threshold \(2/(n+2)\). That case is **covered prior work**, not asserted anew. The result here extends the one-switch statement to **every** symmetric Dirichlet concentration \(\alpha>0\), with a new exact shape-dependent transition and its sharp parameter limits. General Dirichlet moment identities and beta calculus are established ingredients, not claimed innovations.

## Limitations

The universal single-crossing proof assumes equal Dirichlet parameters and strict score convexity. It does not establish the same conclusion for asymmetric Dirichlet vectors, nonconvex scores, or arbitrary dependent compositions. The result is a covariance classification, not a stochastic-order theorem, a distributional independence claim, or a claim about testing power. Although the cited and searched sources did not establish the full shape-dependent assertion, an implicit formulation in older general beta/Dirichlet covariance theory cannot be categorically excluded without an independent historical review.

## References

1. T. Royen, *The distribution of the square sum of Dirichlet random variables and a table with quantiles of Greenwood's statistic*, arXiv:1008.4059, first publicly posted 2010-08-24. https://arxiv.org/abs/1008.4059
2. E. Hashorva, *Extremes of aggregated Dirichlet risks*, arXiv:1404.3304 (first posted 2014-04-12); Journal of Multivariate Analysis 133 (2015), 334–345, DOI 10.1016/j.jmva.2014.09.018. This work concerns tail asymptotics of Dirichlet power sums, not the present finite-sample covariance. https://arxiv.org/abs/1404.3304
3. Prior finite uniform-simplex covariance finding, identifier `8cec2684-e10a-4f25-bc74-47e4588a92c0`: *A universal one-switch covariance law for large spacings and convex spacing tests* (prior claim, \(\alpha=1\) only).
