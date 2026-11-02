# Marked Zipf coupon extremes: independent Gumbel completion time and exponential terminal rank

## Finding
For each fixed \(\alpha>0\), let \(E_{k,n}\), \(1\le k\le n\), be independent exponential random variables with rates \(k^{-\alpha}\). Write \(M_n=\max_k E_{k,n}\), \(J_n=\operatorname*{argmax}_k E_{k,n}\), \(L_n=\log n\) and \(b_n=L_n-\log L_n-\log\alpha\). Then
\[
\left(M_n/n^\alpha-b_n,\;\alpha L_n(1-J_n/n)\right)\ \Longrightarrow\ (G,V),
\]
where \(G\) is standard Gumbel with \(\Pr(G\le x)=\exp(-e^{-x})\), \(V\) has the unit-rate exponential law, and \(G\) and \(V\) are independent.

More structurally, the point process
\[
\Xi_n=\sum_{k=1}^n\delta_{\left(\alpha L_n(1-k/n),\ E_{k,n}/n^\alpha-b_n\right)}
\]
converges vaguely to a Poisson point process on \([0,\infty)\times\mathbb R\) with intensity \(e^{-u-z}\,du\,dz\). This determines the asymptotic ranks of the last \(r\) clocks for every fixed \(r\): their endpoint-distance marks converge to independent unit exponential variables, independently of their limiting extreme heights.

For iid coupons of types \(1,\ldots,n\) with Zipf probabilities \(p_{n,k}=k^{-\alpha}/H_{n,\alpha}\), \(H_{n,\alpha}=\sum_{j=1}^n j^{-\alpha}\), let \(T_n\) be the number of draws needed to see every type and let \(K_n\) be the last type seen for the first time. The same joint convergence holds with first coordinate \(T_n/(n^\alpha H_{n,\alpha})-b_n\) and second \(\alpha L_n(1-K_n/n)\). Last fixed-rank coupon labels obey the same independent exponential mark law.

## Assumptions and scope
The exponent \(\alpha>0\) is fixed as \(n\to\infty\). The independent clocks have rates \(k^{-\alpha}\), not rates proportional to \(k^{\alpha}\). A unique maximum holds with probability one. Point-process convergence is vague on compact subsets of \([0,\infty)\times\mathbb R\); the limiting process has finitely many points above any fixed height, and infinitely many as the height tends to negative infinity. Fixed top-order statistics are taken in descending height order.

## Proof
Put \(Y_{k,n}=E_{k,n}/n^\alpha\) and \(\lambda_{k,n}=(n/k)^\alpha\), so that \(Y_{k,n}\) is exponential with rate \(\lambda_{k,n}\). Define \(u_{k,n}=\alpha L_n(1-k/n)\). For bounded \(u_{k,n}\), uniformly on compact \(u,z\) sets,
\[
\lambda_{k,n}=1+u_{k,n}/L_n+O(L_n^{-2}),\quad
\lambda_{k,n}\exp[-\lambda_{k,n}(b_n+z)]
=\frac{\alpha L_n}{n}e^{-u_{k,n}-z}(1+o(1)).
\]
The \(u\)-grid spacing equals \(\alpha L_n/n\). Hence, for every nonnegative continuous compactly supported test function \(f\),
\[
\sum_{k=1}^n \mathbb E[1-e^{-f(u_{k,n},Y_{k,n}-b_n)}]
\ \longrightarrow\ \int_0^\infty\!\int_{\mathbb R}(1-e^{-f(u,z)})e^{-u-z}\,dz\,du.
\]
Each summand is uniformly \(O(L_n/n)\) where \(f\) is supported, so the sum of their squares tends to zero. Multiplication of independent Laplace factors proves convergence to the stated Poisson point process.

To justify extraction of global top points, not merely points on compact mark intervals, use convexity: for every \(1\le k\le n\),
\[
\lambda_{k,n}=(1-(1-k/n))^{-\alpha}\ge1+\alpha(1-k/n)=1+u_{k,n}/L_n.
\]
At each fixed \(x\) and all sufficiently large \(n\), \(t_n=b_n+x>0\) and \(t_n/L_n\to1\). Thus
\[
\sum_{u_{k,n}>R}\Pr(Y_{k,n}>t_n)
\le e^{-t_n}\sum_{u_{k,n}>R}e^{-t_n u_{k,n}/L_n}
\le C_xe^{-R/2}
\]
for all \(R\ge0\) and sufficiently large \(n\); the last estimate follows by bounding the geometric sum on the equally spaced grid, using \(e^{-t_n}=\alpha L_n e^{-x}/n\). Also \(\sum_k\Pr(Y_{k,n}>b_n+x)\to e^{-x}\) and the largest individual exceedance probability tends to zero. Consequently the maximum has the Gumbel law and the top fixed-number points are tight in spatial mark, allowing the continuous-mapping theorem applied to the point process. The limiting intensity factors as \(e^{-u}\,du\) times \(e^{-z}\,dz\); the mark theorem for a Poisson process therefore makes the spatial marks iid \(\operatorname{Exp}(1)\), independent of ordered heights.

For the coupon model, superpose independent Poisson arrival processes of rates \(p_{n,k}\); their first-arrival times equal \(H_{n,\alpha}E_{k,n}\) in law. The merged arrivals form a unit-rate Poisson process with iid Zipf type labels independent of its exponential interarrival gaps. Consequently the discrete last-new-type index has exactly the same law as \(J_n\), jointly with the Poissonized completion time. With \(A_n=n^\alpha H_{n,\alpha}\), the number \(T_n\) of merged arrivals before completion obeys \(\mathbb ET_n\le A_n(1+\log n)\) by comparison to \(n\) identical exponential clocks of rate \(1/A_n\). Conditional on \(T_n\), the Poissonized completion time is a sum of \(T_n\) independent unit exponential gaps, giving
\[
\mathbb E\left[\left(\frac{T_n-\sum_{j=1}^{T_n}W_j}{A_n}\right)^2\right]
=\frac{\mathbb ET_n}{A_n^2}
\le\frac{1+\log n}{A_n}\ \longrightarrow0,
\]
since \(A_n\ge n\). This joint coupling changes neither final coupon labels nor their ranks and transfers all claimed laws to discrete draws.

## Verification
Execute \(\texttt{python verification.py}\) using Python 3 standard libraries. It checks the finite independent-clock tail masses and maximum distribution across multiple exponents, sample sizes and heights, and tests the predicted winner-index distribution by seeded simulation. Numerical checks are finite corroboration, not the proof of Poisson convergence or the infinite limit.

## Relationship to prior work
Barak-Pelleg, Berend and Kolesnik study the maximum and winner index of independent exponentials with **increasing rates** \(1,2,\ldots,n\), as well as long coupon waiting stages; their asymptotic maximal clock has a different regime from the present **decreasing rates** \(k^{-\alpha}\). Neal's general unequal-probability coupon-collector theorem already establishes broad **marginal** completion-time limits, including Gumbel laws; no novelty is claimed for Gumbel convergence alone. Ilienko establishes unmarked point-process convergence for equiprobable coupons, rather than the Zipf endpoint-rank marks here. The present contribution is the explicit **joint** endpoint label localization and time limit, with an indexed marked Poisson process and independence of extreme order-label marks. General point-process tools underlie the proof; priority of an equivalent specialization elsewhere is not ruled out.

## Limitations
Only fixed \(\alpha>0\) and fixed numbers of final coupon types are treated. No explicit convergence rate, result uniform as \(\alpha\to0\), or statement for non-power-law perturbations is proved. The marginal time Gumbel limit is not presented as new. Independent validation and exhaustive literature priority checking remain outstanding.

## References
1. D. Barak-Pelleg, D. Berend and G. Kolesnik, *Maximum of Exponential Random Variables, Hurwitz's Zeta Function, and the Partition Function*, arXiv:2005.03392 (public v1 May 7, 2020), doi:10.4064/sm200630-11-12.
2. P. Neal, *The Generalised Coupon Collector Problem*, Journal of Applied Probability 45 (2008), 621–629, doi:10.1239/jap/1222441818.
3. A. Ilienko, *Convergence of point processes associated with coupon collector's and Dixie cup problems*, Electronic Communications in Probability 24 (2019), paper 51, arXiv:1904.12954.
4. C. D. Long, *Extremality and Limit Laws for the Siblings of the Coupon Collector*, arXiv:2606.29635 (2026), related nonuniform coupon setting.
