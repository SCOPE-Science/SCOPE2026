# Poisson gap normalization reverses covariance with the event count
## Finding
Let \(N=N(t)\) count the events of a homogeneous Poisson process of rate \(\lambda>0\) on \([0,t]\). Include both boundary gaps \(D_0,\ldots,D_N\), and set
\[
Q_t=\sum_{i=0}^{N}\left(\frac{D_i}{t}\right)^2,\qquad C_t^2=(N+1)Q_t-1.
\]
Thus \(C_t^2\) is the population squared coefficient of variation of the complete-window gaps. With \(\mu=\lambda t\), define
\[
A(\mu)=\frac{2[\mu-2+(\mu+2)e^{-\mu}]}{\mu^2}.
\]
Then
\[
\operatorname{Cov}(N,Q_t)=-A(\mu),\qquad \operatorname{Cov}(N,C_t^2)=A(\mu),
\]
and \(A(\mu)>0\) for every \(\mu>0\). Hence the normalization by the realized mean gap reverses the covariance sign with exactly the same magnitude. Also
\[
\operatorname{Cov}\!\left(N,\sum_{i=0}^{N}D_i^2\right)=-t^2A(\mu).
\]
The sparse and dense limits are \(A(\mu)=\mu/3+O(\mu^2)\) as \(\mu\downarrow0\) and \(A(\mu)=2/\mu-4/\mu^2+O(e^{-\mu}/\mu)\) as \(\mu\to\infty\).

## Assumptions and scope
The process is homogeneous Poisson on a fixed finite interval. Both boundary gaps are included, even when \(N=0\). The dispersion \(C_t^2\) uses the population-variance convention across the realized gaps. No statement is made for general renewal processes, omitted boundary gaps, or statistics based only on completed interarrival times.

## Proof
Condition on \(N=n\). The ordered event times are uniform order statistics, so the \(n+1\) normalized gaps have the \(\operatorname{Dirichlet}(1,\ldots,1)\) law. Each coordinate has second moment \(2/[(n+1)(n+2)]\), hence
\[
\mathbb E[Q_t\mid N=n]=\frac{2}{n+2},\qquad \mathbb E[C_t^2\mid N=n]=\frac{n}{n+2}.
\]
For \(N\sim\operatorname{Poisson}(\mu)\), direct index shifting gives \(\mathbb E[Nh(N)]=\mu\mathbb E[h(N+1)]\). Therefore
\[
\operatorname{Cov}(N,Q_t)=-2\mu\,\mathbb E\!\left[\frac{1}{(N+2)(N+3)}\right],
\]
while the covariance with \(C_t^2\) is the same quantity with positive sign. Finally,
\[
\mathbb E\!\left[\frac{1}{(N+2)(N+3)}\right]
=\int_0^1x(1-x)e^{\mu(x-1)}\,dx
=\frac{\mu-2+(\mu+2)e^{-\mu}}{\mu^3}.
\]
This gives the formulas. If \(g(\mu)=\mu-2+(\mu+2)e^{-\mu}\), then \(g(0)=0\) and \(g'(\mu)=1-(1+\mu)e^{-\mu}>0\), because \(e^\mu>1+\mu\). Thus \(A(\mu)>0\). The stated asymptotics follow by expansion.

## Verification
The standalone `verify.py` checks the conditional identities exactly for \(0\le n\le1000\), compares direct Poisson summation with both covariance formulas at ten intensities between \(0.01\) and \(50\), and checks the small-intensity expansion at three high-precision values. It returns `VERIFY_OK conditional=1001 poisson=10 small_mu=3`. These are consistency checks; the proof above establishes the all-parameter theorem.

## Relationship to prior work
Di and Perlman place Poisson processes, arrival times, gap-linearity, and Dirichlet geometry in one spacing framework. Mirakhmedov treats Greenwood's sum-of-squared-spacings statistic and its fixed-size asymptotic efficiency. The present result instead randomizes the spacing dimension through the Poisson count and computes the resulting mixed covariance. Fixed-dimension Greenwood results do not imply this quantity because conditioning on the count removes the randomness whose covariance is at issue.

The closest prior result in the checked collection for the same Poisson window concerns the longest boundary-inclusive gap, not quadratic gap energy. Other checked exact Greenwood results couple the statistic to fixed-dimension spacing functionals and likewise do not imply the random-count identity.

## Limitations
The claim is confined to the homogeneous Poisson benchmark and the boundary-inclusive convention. The complete Di–Perlman journal body was not available through the checked lawful source, although its public technical-report abstract was inspected. Older spacing literature using alternate normalizations remains a residual originality risk.

## References
1. Y. Di and M. Perlman, “Detecting Linear Sequences and Subsequences,” University of Washington Statistics Technical Report 520, publicly listed 2007-10-01; journal DOI 10.1016/j.jspi.2008.03.007.
2. S. M. Mirakhmedov, “On Greenwood goodness-of-fit test,” *Journal of Statistical Planning and Inference* 140 (2010), 3017–3025, DOI 10.1016/j.jspi.2010.04.002. Its article record states “Available online 13 April 2010” and lists MSC 62G10, 62G20, 60F10.
