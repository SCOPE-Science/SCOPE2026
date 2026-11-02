# Two-grade coupon completion: a universal Gumbel window and a sharp last-bottleneck crossover

## Finding

Let \(n\) range over even integers tending to infinity, and let \(m=m_n\) be any sequence of positive integers with \(m_n\to\infty\). In independent draws from \(n\) equally likely coupon types, split the types into two specified groups of size \(n/2\). Let \(K_{n,-}\) be the first draw index when every type of the first group has appeared at least \(m\) times. Define \(K_{n,+}\) similarly for the second group, but require \(m+1\) copies of every type. Set \(T_n=\max(K_{n,-},K_{n,+})\).

For every integer \(j\geq1\), write
\[
Q_j(u)=e^{-u}\sum_{k=0}^{j-1}\frac{u^k}{k!},\qquad u\geq0.
\]
There is a unique \(u_n>0\) solving
\[
\frac n2\bigl(Q_m(u_n)+Q_{m+1}(u_n)\bigr)=1.
\]
Eventually \(u_n>m\). Define \(b_n=u_n/(u_n-m)\). Without a growth-rate restriction on \(m_n\) beyond divergence,
\[
\boxed{\ \Pr\left\{\frac{T_n-nu_n}{nb_n}\leq x\right\}\longrightarrow
\exp(-e^{-x})\quad(x\in\mathbb R).\ }
\]

There is also a complete competition law for the class that finishes last. If \(m_n/\log n\to\alpha\in[0,\infty]\), define \(r_0=\infty\), \(r_\infty=1\), and, for \(0<\alpha<\infty\), let \(r_\alpha>1\) be the unique solution of
\[
r_\alpha-1-\log r_\alpha=1/\alpha.
\]
Then
\[
\boxed{\ \Pr(K_{n,+}>K_{n,-})\longrightarrow\frac{r_\alpha}{1+r_\alpha}.\ }
\]
Thus the group requiring one additional copy accounts for asymptotically all last completions when \(m_n\ll\log n\), exactly half when \(m_n\gg\log n\), and an explicit strictly intermediate proportion when \(m_n\) and \(\log n\) are comparable.

More precisely, putting \(a_\alpha=1/(1+r_\alpha)\), interpreted as zero when \(r_\alpha=\infty\), for all fixed real \(x,y\),
\[
\begin{aligned}
&\Pr\left\{\frac{K_{n,-}-nu_n}{nb_n}\leq x,\;
\frac{K_{n,+}-nu_n}{nb_n}\leq y\right\}\\
&\hspace{10mm}\longrightarrow
\exp\bigl(-a_\alpha e^{-x}-(1-a_\alpha)e^{-y}\bigr).
\end{aligned}
\]
For \(\alpha=0\), this is a joint distribution-function limit with the first coordinate escaping to \(-\infty\); it is not asserted to be a tight weak limit on \(\mathbb R^2\).

## Assumptions and scope

All draws are independent and uniformly distributed over \(n\) labeled types. The two groups are fixed in advance, disjoint, and each has exactly \(n/2\) members. Required multiplicities are \(m_n\) and \(m_n+1\), respectively, and \(m_n\to\infty\). No independence is imposed on the two completion indices in discrete draw time. The analysis uses a Poissonized coupling where the corresponding continuous-time completion indices become independent. The primary result is a distributional limit and a last-completer probability; it does not claim a convergence rate, expected stopping-time expansion, or an unequal group-size formula.

## Proof

**1. Independent Gamma maxima after Poissonization.** Run a global rate-one Poisson draw clock in physical time, assigning to each event an independent uniformly random type. Rescale time as \(t=nu\). Poisson thinning makes the rescaled arrival processes of all \(n\) coupon types independent rate-one Poisson processes. The first time one type has \(j\) arrivals has a \(\operatorname{Gamma}(j,1)\) law with upper tail \(Q_j\). Thus the rescaled group completion times \(M_{n,-},M_{n,+}\) are independent and satisfy
\[
\Pr(M_{n,-}\le u)=(1-Q_m(u))^{n/2},\qquad
\Pr(M_{n,+}\le u)=(1-Q_{m+1}(u))^{n/2}.
\]
Their maximum has CDF equal to the product. If \(N(t)\) is the global rate-one Poisson counting process, the exact discrete completion indices under this coupling are \(K_{n,\pm}=N(nM_{n,\pm})\). Completion events cannot tie in physical or draw time.

**2. A uniform Gamma-tail estimate.** Let \(u>m\), \(v=u-m\), \(\eta=v/u\), and \(f_{m+1}(u)=e^{-u}u^m/m!\). The logarithmic derivative of this Gamma density at \(u\) is \(-\eta\). For \(t\ge0\), elementary logarithm inequalities yield
\[
-\eta t-\frac{mt^2}{2u^2}
\leq\log\frac{f_{m+1}(u+t)}{f_{m+1}(u)}
\leq-\eta t.
\]
Integrating over \(t\ge0\), and using \(e^{-z}\ge1-z\), gives the explicit Mills comparison
\[
\frac{f_{m+1}(u)}\eta\left(1-\frac{m}{(u-m)^2}\right)
\leq Q_{m+1}(u)\leq\frac{f_{m+1}(u)}\eta.
\tag{1}
\]
The analogous bound for \(Q_m\) uses the density \(f_m(u)=e^{-u}u^{m-1}/(m-1)!\) and the slope \(1-(m-1)/u\).

At the defining center \(u=u_n\), monotonicity implies \(1/n\le Q_{m+1}(u_n)\le2/n\). The Gamma central limit theorem shows that, for every fixed \(A\), \(Q_{m+1}(m+A\sqrt m)\) is bounded away from zero. Hence
\[
\frac{u_n-m}{\sqrt m}\to\infty.
\tag{2}
\]
In particular, \(m/(u_n-m)^2\to0\), and (1) yields
\[
\frac{Q_{m+1}(u_n)}{Q_m(u_n)}
=\frac{u_n}{m}(1+o(1)).
\tag{3}
\]
For the last equality note \(f_m(u_n)/f_{m+1}(u_n)=m/u_n\) and the two Mills slopes have ratio tending to one.

**3. Uniform local exponential tails.** Set \(b=b_n=u_n/(u_n-m)\), so \(b\eta=1\). For every fixed real \(x\), (2) implies that \(u_n+xb_n>m\) eventually and that its Mills slope is \(\eta(1+o(1))\). Taylor expansion of the logarithm of each Gamma density on the displacement \(xb_n\) gives
\[
\log\frac{f_j(u_n+xb_n)}{f_j(u_n)}=-x+o(1),
\qquad j\in\{m,m+1\},
\]
since its quadratic remainder is \(O(m/(u_n-m)^2)\) and the two initial logarithmic slopes differ by only \(1/u_n\). Applying (1) at both arguments proves
\[
\frac{Q_j(u_n+xb_n)}{Q_j(u_n)}\to e^{-x}
\qquad(j=m,m+1).
\tag{4}
\]
As \((n/2)(Q_m(u_n)+Q_{m+1}(u_n))=1\), the sum of expected missing quotas at \(u_n+xb_n\) tends to \(e^{-x}\). Each failure probability is at most \(2/n\) at the center and remains \(O(1/n)\) under fixed scaled shifts. Taking logarithms of the two independent group CDFs proves the standard Gumbel CDF in Poissonized time. If the ratio in (3) has limit \(r\in[1,\infty]\), (4) also proves the two-coordinate distribution-function limit with intensities \(1/(1+r)\) and \(r/(1+r)\).

**4. Controlling the Poisson clock for arbitrary growing multiplicity.** Put \(I(\rho)=\rho-1-\log\rho\), \(\rho\ge1\). Stirling's formula and (1) show
\[
Q_{m+1}(u_n)=\frac{1+o(1)}{\eta\sqrt{2\pi m}}\,
\exp\bigl(-mI(u_n/m)\bigr),
\]
where \(\eta=(u_n-m)/u_n\) and \(\eta\sqrt m\to\infty\) by (2). From \(Q_{m+1}(u_n)\ge1/n\),
\[
mI(u_n/m)\le\log n+O(1).
\tag{5}
\]
For \(\rho\ge1\), differentiation proves
\[
\frac{(\rho-1)^2}{\rho}\le2(\rho-1-\log\rho).
\]
Consequently,
\[
\frac{u_n}{b_n^2}
=u_n\left(1-\frac m{u_n}\right)^2
\le2mI(u_n/m)\le2\log n+O(1).
\tag{6}
\]
The Poisson martingale maximal inequality gives, for every \(\varepsilon>0\),
\[
\Pr\left(\sup_{0\le t\le2nu_n}|N(t)-t|>\varepsilon nb_n\right)
\le\frac{8u_n}{\varepsilon^2nb_n^2}\longrightarrow0.
\]
Because \(u_n/b_n=u_n-m\to\infty\) and the Poissonized maximum is \(u_n+O_{\Pr}(b_n)\), both group completion times lie below \(2u_n\) with probability tending to one. Therefore the exact coupling \(K_{n,\pm}=N(nM_{n,\pm})\) transfers the limiting CDFs to discrete draw time. It also preserves exactly which group finishes last, without approximation of its indicator.

**5. The three regimes for the last completer.** If \(m_n/\log n\to\alpha\in(0,\infty)\), the more precise logarithm of the Mills comparison yields
\[
\log n=mI(u_n/m)+\log(\eta\sqrt m)+O(1).
\]
Since \(\eta\sqrt m\to\infty\) and \(\log(\eta\sqrt m)=O(\log m)=o(\log n)\), the unique limit \(u_n/m\to r_\alpha>1\) solves \(I(r_\alpha)=1/\alpha\). If \(m_n/\log n\to0\), the same identity forces \(u_n/m\to\infty\); otherwise its first term would be \(o(\log n)\). If \(m_n/\log n\to\infty\), (5) gives \(I(u_n/m)\to0\), hence \(u_n/m\to1\).

Combining with (3) identifies the limiting quota-failure intensity split. Independent limiting group maxima with CDFs \(\exp(-ae^{-x})\) and \(\exp(-(1-a)e^{-y})\) have the higher-quota group last with probability \(1-a\): for example, they are independent standard Gumbels shifted by \(\log a\) and \(\log(1-a)\), whose comparison is logistic. The same conclusion at \(a=0\) holds by degeneration of the lower-quota group to \(-\infty\) on the scaled axis. This proves the stated probability \(r_\alpha/(1+r_\alpha)\). \(\square\)

## Verification

The supplied standalone Python script `verify.py` checks the exact adjacent-shape Gamma polynomial identity using rational arithmetic, numerically solves the center equation, integrates the independent maxima's exact finite-sample winner probability, and compares finite-sample distribution functions against the predicted Gumbel form. Its actual output is in `verification_output.txt`; it reports **454 passed finite assertions**, including six parameter regimes spanning small and large multiplicity. The infinite-sequence statements rest on the analytic proof above; numerical comparisons are not used as an infinite proof.

## Relationship to prior work

Castro and Marinho (2026, arXiv:2610.33199v1) establish a Gumbel cutoff for **one common** growing quota over all coupon types. Long (2026, arXiv:2604.25108v2) develops Gamma-tail extremal techniques and varying coupon **arrival probabilities**, but assumes the same quota for all types. May (2008) gives an exact finite generating function for **arbitrary per-type quotas and probabilities**; its exact representation is acknowledged as broader at finite size, but does not state a growing-quota competition phase diagram or the sharp last-group probability. Ilienko (2020) studies the joint completions of successive homogeneous coupon collections, with fixed collection indices in the stated limiting framework.

The distinction here is not the definition of heterogeneous quotas or the univariate Gumbel law alone, but the joint competition profile and the boundary \(m\asymp\log n\) at which a difference of just one required copy changes the identity of the last unfinished class. Standard single-quota marked-defect limits do not directly record all the types sitting exactly at the lower quota, which are necessary for the higher-quota group's completion event. No independent-priority determination is claimed.

## Limitations

Only two preassigned equally sized classes with consecutive integer quotas are treated. For \(m_n/\log n\) not converging, the universal completion-time Gumbel limit remains valid, but no universal single last-class probability is asserted. The \(\alpha=0\) joint statement is a distribution-function limit with one coordinate escaping to \(-\infty\), not ordinary weak convergence in \(\mathbb R^2\). Explicit finite-size error rates, general unbalanced classes, unequal arrival probabilities, and independent validation remain outside scope. The possibility of older generalized coupon-collection or extreme-value results implicitly encompassing this scaling remains a historical-priority risk.

## References

1. M. E. Castro and R. Marinho, *Cutoff profile for the coupon collector with many collections*, arXiv:2610.33199v1, first posted 23 October 2026. https://arxiv.org/html/2610.33199v1
2. C. D. Long, *Terminal Defects, Growing Multiplicity, and Variance Extremality in the Double Dixie Cup Problem*, arXiv:2604.25108v2, 2026. https://arxiv.org/html/2604.25108v2
3. R. May, *Coupon Collecting with Quotas*, Electronic Journal of Combinatorics **15** (2008), #N31. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1n31/pdf/
4. A. Ilienko, *Limit theorems in the extended coupon collector's problem*, arXiv:2002.00650, 2020. https://arxiv.org/abs/2002.00650
