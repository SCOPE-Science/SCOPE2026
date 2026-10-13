# A unique macroscopic-cycle covariance crossover under the Ewens law

## Finding
Let \(\sigma_n\) be an Ewens random permutation of \(\{1,\ldots,n\}\) with parameter \(\theta>0\), let \(K_n\) be its total number of cycles, and let \(R_{n,m}\) count its cycles of length strictly greater than \(m\). For every \(n\ge2\), the covariance \(\operatorname{Cov}_\theta(K_n,R_{n,m})\), as \(m\) runs through \(0,\ldots,n-1\), crosses from positive to negative exactly once (with at most one zero). This finite-sample sign classification holds for all \(\theta>0\).

For each fixed \(\theta>0\) there is a unique fraction \(t_\theta\in(0,1)\) determined by
\[
Q_\theta(t_\theta)=0,\qquad
Q_\theta(t)=\theta\int_t^1\frac{(1-x)^{\theta-1}[1+\theta\log(1-x)]}{x}\,dx.
\]
The limiting covariance is \(Q_\theta(t)\) at cutoff \(m=\lfloor tn\rfloor\), for every \(0<t<1\); it is positive below \(t_\theta\) and negative above. If \(m_n(\theta)\) is the smallest nonnegative integer cutoff with nonpositive finite-sample covariance, then
\[
\lim_{n\to\infty}\frac{m_n(\theta)}n=t_\theta.
\]
The critical fraction satisfies
\[
\lim_{\theta\downarrow0}t_\theta=\frac12,\qquad
\lim_{\theta\to\infty}\theta t_\theta=c_\infty=0.4348182043849\ldots,
\]
where \(c_\infty\in(0,1)\) uniquely solves \(E_1(c_\infty)=e^{-c_\infty}\), with \(E_1(c)=\int_c^\infty e^{-u}/u\,du\). At \(\theta=1\), the critical fraction is \(t_1=0.2531929331984\ldots\), characterized by \(-\log t_1-\pi^2/6+\operatorname{Li}_2(t_1)=0\).

## Assumptions and scope
All permutations are on \(n\) labeled points. The Ewens probability of a permutation \(\sigma\) is \(\theta^{K(\sigma)}/\theta^{\overline n}\), where \(\theta^{\overline n}=\prod_{i=0}^{n-1}(\theta+i)\). Let \(C_{n,j}\) denote the number of \(j\)-cycles and set \(K_n=\sum_{j=1}^n C_{n,j}\) and \(R_{n,m}=\sum_{j=m+1}^n C_{n,j}\). The finite sign assertion concerns integer \(n\ge2\), every real \(\theta>0\), and \(0\le m\le n-1\); at \(m=n\), \(R_{n,n}=0\) deterministically. The asymptotic assertion holds at fixed \(\theta>0\) and fixed \(t\in(0,1)\), and the endpoint parameter limits refer to the already-defined continuum critical fraction.

Define \(h_0(\theta)=0\) and \(h_r(\theta)=\theta\sum_{i=0}^{r-1}(\theta+i)^{-1}\) for positive integers \(r\). Define \(\mu_{n,j}(\theta)=\mathbb E_\theta C_{n,j}\).

## Proof
**Exact marking identity.** Counting permutations after designating one \(j\)-cycle leaves an independent Ewens permutation on \(n-j\) remaining labels. Thus
\[
\mu_{n,j}(\theta)=\frac\theta j\frac{n!}{(n-j)!}\frac{\theta^{\overline{n-j}}}{\theta^{\overline n}},\qquad
\mathbb E_\theta[K_nC_{n,j}]=\mu_{n,j}(\theta)[1+h_{n-j}(\theta)].
\]
Since \(\mathbb E_\theta K_n=h_n(\theta)\), the finite covariance is exactly
\[
A_{n,m}(\theta):=\operatorname{Cov}_\theta(K_n,R_{n,m})
=\sum_{j=m+1}^n\mu_{n,j}(\theta)\,\delta_{n,j}(\theta),\qquad
\delta_{n,j}(\theta)=1-\theta\sum_{i=n-j}^{n-1}\frac1{\theta+i}.
\tag{1}
\]
This identity, by itself, follows from standard Ewens cycle counting; the claims here concern its global sign and scaling regimes.

**Finite sign rigidity.** All \(\mu_{n,j}\) are positive. The sequence \(j\mapsto\delta_{n,j}\) is strictly decreasing, with \(\delta_{n,1}=1-\theta/(\theta+n-1)>0\) and \(\delta_{n,n}=1-h_n(\theta)<0\). Also \(A_{n,0}=\operatorname{Var}_\theta(K_n)>0\): the usual Ewens insertion construction represents \(K_n\) as a sum of independent Bernoulli variables with probabilities \(\theta/(\theta+i)\), and the second variable is nondegenerate for \(n\ge2\). At the opposite endpoint, \(A_{n,n-1}=\mu_{n,n}(1-h_n)<0\).

From (1), \(A_{n,m}-A_{n,m-1}=-\mu_{n,m}\delta_{n,m}\). Consequently the covariance sequence decreases while positive \(\delta\)'s are removed, may have one stationary increment if a \(\delta\) vanishes, and thereafter increases. Once the remaining summands all have negative \(\delta\), the covariance is negative. Together with the opposite endpoint signs, this proves precisely one transition from positive to negative among integer cutoffs; at most one cutoff has zero covariance. It also defines \(m_n(\theta)=\min\{m\in\{0,\ldots,n-1\}:A_{n,m}(\theta)\le0\}\).

**Macroscopic limit.** Put \(j/n=x\) and \(r=n-j\). By the gamma-function representation
\[
\mu_{n,j}(\theta)=\frac\theta j\frac{\Gamma(n+1)\Gamma(r+\theta)}{\Gamma(r+1)\Gamma(n+\theta)},
\]
and standard gamma-ratio estimates, for fixed \(x\in(0,1)\), \(n\mu_{n,\lfloor xn\rfloor}\to\theta(1-x)^{\theta-1}/x\). Furthermore \(\delta_{n,\lfloor xn\rfloor}\to1+\theta\log(1-x)\). On compact subintervals of \((0,1)\), equation (1) is an ordinary Riemann sum.

To justify its upper endpoint, fix \(t>0\), and write \(r=n-j\). Gamma-ratio bounds give \(\mu_{n,n-r}\le C_{\theta,t}n^{-\theta}(r+1)^{\theta-1}\); harmonic bounds give \(|\delta_{n,n-r}|\le C_\theta[1+\log(n/(r+1))]\). Hence the sum over \(0\le r\le\varepsilon n\) has absolute value at most \(C_{\theta,t}\varepsilon^\theta(1+|\log\varepsilon|)+o(1)\). Letting \(\varepsilon\downarrow0\) yields
\[
\lim_{n\to\infty}A_{n,\lfloor tn\rfloor}(\theta)=Q_\theta(t).
\tag{2}
\]

**A unique continuum zero.** The integrand in \(Q_\theta(t)\) has the sign of \(1+\theta\log(1-x)\), which changes once at \(b_\theta=1-e^{-1/\theta}\). Thus \(Q_\theta(t)<0\) for \(t\ge b_\theta\), while \(Q_\theta'(t)<0\) for \(0<t<b_\theta\). Near zero, \(Q_\theta(t)\to+\infty\), because the integrand has a positive \(\theta/x\) singularity. This proves a unique root \(t_\theta\in(0,b_\theta)\) and its stated signs. Applying (2) at two fixed points on opposite sides of \(t_\theta\), with the finite sign classification, proves \(m_n(\theta)/n\to t_\theta\).

**Limits in the Ewens parameter.** The mean continuum count of cycles longer than fraction \(t\) is
\[
M_\theta(t)=\theta\int_t^1\frac{(1-x)^{\theta-1}}x\,dx
=(1-t)^\theta+\theta\int_0^{1-t}\frac{y^\theta}{1-y}\,dy.
\]
Direct differentiation gives \(Q_\theta(t)=\theta\partial_\theta M_\theta(t)\). For fixed \(t\in(0,1)\), the integration-by-parts representation and dominated convergence yield
\[
\lim_{\theta\downarrow0}\frac{Q_\theta(t)}\theta
=\log(1-t)-\log t.
\]
This limit has its only zero at \(t=1/2\), and testing either side proves \(t_\theta\to1/2\).

At large \(\theta\), substitute \(t=c/\theta\) and \(u=\theta x\) in the integral. On bounded \(u\)-intervals, \((1-u/\theta)^{\theta-1}\to e^{-u}\) and \(1+\theta\log(1-u/\theta)\to1-u\). The tail is dominated by an integrable exponential-polynomial envelope up to \(u=\theta/2\); the rest is exponentially small by direct integration of powers of \(1-u/\theta\) and their logarithms. Consequently
\[
\lim_{\theta\to\infty}\frac{Q_\theta(c/\theta)}\theta
=J(c):=\int_c^\infty e^{-u}\frac{1-u}{u}\,du=E_1(c)-e^{-c}.
\]
The function \(J\) is positive near zero, strictly decreases on \((0,1)\), and is strictly negative on \([1,\infty)\). Hence its unique root \(c_\infty\in(0,1)\) controls \(\theta t_\theta\to c_\infty\) by two-sided sign tests. For \(\theta=1\), termwise integration of \(Q_1\) gives \(Q_1(t)=-\log t-\pi^2/6+\operatorname{Li}_2(t)\), yielding the displayed numerical root.

## Verification
A standalone Python standard-library checker, `check_cycles.py`, enumerates every permutation for \(2\le n\le7\) under each of \(\theta\in\{1/2,1,2\}\). It computes exact rational covariances from the Ewens probability law and independently from equation (1) for every cutoff \(0\le m<n\); all 81 cases agree exactly. It separately checks the finite sign ordering. Approximate numerical solutions of the continuum equations give \(t_1\approx0.2531929331984\) and \(c_\infty\approx0.4348182043849\); the supplied proof, not the finite checks or numerical roots, establishes infinite and universal claims. Reproduce with `python3 check_cycles.py`.

## Relationship to prior work
Betz and Schäfer (arXiv:1605.08383, first public 2016-05-26, primary MSC 60C05) investigate the **conditional** uniform model that forbids long cycles and derive central limit theorems for the total number of cycles. Their model and main theorems do not assert the **unconditioned** mixed covariance with the long-cycle count, nor the Ewens-parameter threshold. Lugo (arXiv:0909.2909, Proposition 1) supplies broad uniform-permutation mixed factorial-moment formulas, which already imply finite-count identities at \(\theta=1\); no independent novelty is claimed for that finite uniform specialization. Nikeghbali and Zeindler (arXiv:1105.2315) and Maples, Nikeghbali, and Zeindler (arXiv:1203.4132) study weighted-permutation cycle statistics and total-cycle asymptotics, supplying conceptual context but not the unique macroscopic mixed-covariance threshold or its parameter-endpoint laws in the inspected statements. The new assertion is the joint finite-sample sign rigidity and continuum crossover classification for **all** \(\theta>0\), not a reinvention of Ewens sampling identities.

## Limitations
The continuum limit holds for each fixed positive parameter and macroscopic fraction; no rate uniform over all positive parameters is claimed. The integer transition may occur with one exact zero or jump across zero. Neither a formula for the finite transition integer nor a monotonicity theorem for \(\theta\mapsto t_\theta\) is asserted. Classical Ewens moment identities and Poisson–Dirichlet intensity formulas can imply the exact finite covariance and its continuum integral; their priority is not disputed. The novelty assessment concerns the global sign and endpoint classifications, and historical literature may contain implicit coverage not identified in the inspected works. Independent verification and exhaustive historical priority checks have not been performed.

## References
1. V. Betz and H. Schäfer, *The number of cycles in random permutations without long cycles is asymptotically Gaussian*, arXiv:1605.08383 (v1 publicly posted 2016-05-26), https://arxiv.org/abs/1605.08383.
2. M. Lugo, *The number of cycles of specified normalized length in permutations*, arXiv:0909.2909 (2009), https://arxiv.org/abs/0909.2909.
3. A. Nikeghbali and D. Zeindler, *The generalized weighted probability measure on the symmetric group and the asymptotic behavior of the cycles*, arXiv:1105.2315 (2011), https://arxiv.org/abs/1105.2315.
4. K. Maples, A. Nikeghbali, and D. Zeindler, *On the number of cycles in a random permutation*, arXiv:1203.4132 (2012), https://arxiv.org/abs/1203.4132.
