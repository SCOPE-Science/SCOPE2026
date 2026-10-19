# A sharp parity-adjacent run conditioning distance for stationary binary Markov chains

## Finding

Let \(0<a,b<1\), and start a binary Markov chain \(X_1,\ldots,X_n\) in its stationary distribution, with \(\Pr(X_{j+1}=1\mid X_j=0)=a\) and \(\Pr(X_{j+1}=0\mid X_j=1)=b\). Write \(K_n=\sum_j X_j\) for its occupancy count and \(R_n=1+\sum_{j=2}^n\mathbf1_{\{X_j\ne X_{j-1}\}}\) for its **total** number of maximal runs, counting both symbols.

For any integer sequence \(s=s_n\ge1\) such that \(s_n/n\to\rho\in(0,1/2)\), let \(P_n=\mathcal L(K_n\mid R_n=2s_n)\) and \(Q_n=\mathcal L(K_n\mid R_n=2s_n+1)\). The following explicit constant determines their sharp total-variation separation.

Set \(q=(1-b)/(1-a)\), and let \(x\) denote the unique point of \((\rho,1-\rho)\) satisfying

\[q\,x(1-x-\rho)=(x-\rho)(1-x).\]

Define

\[\sigma^2=\left(\frac{\rho}{x(x-\rho)}+\frac{\rho}{(1-x)(1-x-\rho)}\right)^{-1},\]
\[t=\frac{b(1-x-\rho)/(1-a)+a(x-\rho)/(1-b)}{2\rho}>0,\qquad
 g=\frac{a/(1-b)-b/(1-a)}{2\rho}.\]

Then

\[\boxed{\lim_{n\to\infty}\sqrt n\,d_{\mathrm{TV}}(P_n,Q_n)=\frac{|g|\sigma}{t\sqrt{2\pi}}.}\]

Here \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_k|P(k)-Q(k)|\). The limit is positive **exactly when** both \(a\ne b\) and \(a+b\ne1\). On either exceptional curve, \(P_n=Q_n\) at *every* finite admissible \(n,s\). Thus symmetric-but-dependent and independent-but-biased chains are separate mechanisms of exact parity-adjacent indistinguishability; otherwise the distance decays at the sharp \(n^{-1/2}\) rate.

## Assumptions and scope

The chain is homogeneous, strictly positive in each transition, and starts in the stationary law \(\pi_0=b/(a+b)\), \(\pi_1=a/(a+b)\). Fix \(\rho\in(0,1/2)\) while taking the limit. Each conditional event is nonempty for \(n\ge2s_n+1\), automatically true eventually. The number of *total* runs differs from the number of runs of ones; the conditioning in the statement is on the former. Parameters \(a,b,\rho\) remain fixed as \(n\to\infty\); no joint boundary-uniform claim is made.

## Proof

**1. Exact finite tilt.** Fix \(n\ge 2s+1\), \(s\ge1\), and \(s\le k\le n-s\). For \(R=2s\), a binary word starts and ends in opposite symbols, with \(s\) positive blocks and \(s\) zero blocks. The numbers of ways to distribute the \(k\) ones and \(n-k\) zeros among these blocks are respectively \(\binom{k-1}{s-1}\) and \(\binom{n-k-1}{s-1}\). Stationarity makes the two possible endpoint orientations have identical Markov probability at fixed composition. Consequently, writing \(J_r(k)=\Pr(K_n=k,R_n=r)\),

\[J_{2s}(k)=2\pi_0 a^s b^{s-1}(1-b)^{k-s}(1-a)^{n-k-s}\binom{k-1}{s-1}\binom{n-k-1}{s-1}.\]

For \(R=2s+1\), both endpoints have the same color. Splitting by the starting color, the all-zero-endpoint contribution has one additional zero block; the all-one-endpoint contribution has one additional one block. Using \(\pi_0 a=\pi_1 b\), and the ratios of consecutive binomial coefficients, one obtains exactly

\[\frac{J_{2s+1}(k)}{J_{2s}(k)}=T_{n,s}(k):=
\frac1{2s}\left(\frac{b(n-k-s)}{1-a}+\frac{a(k-s)}{1-b}\right).\tag{1}\]

Both distributions have the same support \(s\le k\le n-s\). Therefore \(Q_n(k)=P_n(k)T_{n,s}(k)/\mathbb E_{P_n}T_{n,s}(K_n)\), with no omitted normalization constant. In particular \(T_{n,s}(k)>0\) on the support.

**2. Exact total-variation identity.** Put \(\rho_n=s_n/n\), \(U_n=K_n/n\),

\[\tau_n(u)=\frac{b(1-u-\rho_n)/(1-a)+a(u-\rho_n)/(1-b)}{2\rho_n}\]

and \(\gamma_n=[a/(1-b)-b/(1-a)]/(2\rho_n)\). This is an affine function of \(u\), and \(T_{n,s}(K_n)=\tau_n(U_n)\). Thus the normalization cancels its intercept, giving the **identity**

\[d_{\mathrm{TV}}(P_n,Q_n)=\frac{|\gamma_n|}{2\,\mathbb E_{P_n}\tau_n(U_n)}\;\mathbb E_{P_n}|U_n-\mathbb E_{P_n}U_n|.\tag{2}\]

No normal approximation has been used so far.

**3. Conditional Gaussian concentration with absolute moments.** Equation (1), or directly the even joint law, shows

\[P_n(K_n=k)=\frac{w_n(k)}{\sum_{j=s_n}^{n-s_n}w_n(j)},\qquad
w_n(k)=\binom{k-1}{s_n-1}\binom{n-k-1}{s_n-1}q^k.\tag{3}\]

For \(u\in(\rho,1-\rho)\), the limiting log-weight per observation, up to an additive constant, is

\[f_\rho(u)=u\,H(\rho/u)+(1-u)H(\rho/(1-u))+u\log q,\]

where \(H(v)=-v\log v-(1-v)\log(1-v)\). Its derivatives are

\[f_\rho'(u)=\log\frac{q\,u(1-u-\rho)}{(u-\rho)(1-u)},\qquad
f_\rho''(u)=-\frac{\rho}{u(u-\rho)}-\frac{\rho}{(1-u)(1-u-\rho)}<0.\]

The derivative runs from \(+\infty\) to \(-\infty\) across the interval, proving the existence and uniqueness of the stated maximizer \(x\), and \(-f_\rho''(x)=\sigma^{-2}\).

Here is a direct local-limit justification, including the moment step. Let \(x_n\) maximize the same entropy function with \(\rho\) replaced by \(\rho_n\); then \(x_n\to x\). Stirling's formula applied uniformly on a compact neighborhood of \(x_n\) to (3) gives, for \(k=nx_n+z\sqrt n\) with bounded \(z\), the ratio of \(w_n(k)\) to its weight at the nearest integer to \(nx_n\) tending to \(\exp[-z^2/(2\sigma^2)]\). The exact adjacent ratio

\[\frac{w_n(k+1)}{w_n(k)}=q\frac{k}{k-s_n+1}\frac{n-k-s_n}{n-k-1}\tag{4}\]

is strictly decreasing in \(k\). Its logarithmic decrement is bounded above by \(-c/n\) on any fixed compact neighborhood of \(x\), uniformly for all large \(n\). This controls intermediate tails by Gaussian bounds. Outside that neighborhood, the strict unique maximizer and Stirling large-deviation bound give exponential decay \(\exp(-c'n)\), with at most \(n\) support points. These estimates justify normalized Riemann summation and uniform integrability of the centered squared fluctuation. Consequently, under \(P_n\),

\[\frac{K_n-nx_n}{\sqrt n}\;\Longrightarrow\;N(0,\sigma^2),\qquad
\frac{\mathbb E_{P_n}|K_n-\mathbb E_{P_n}K_n|}{\sqrt n}\longrightarrow\sigma\sqrt{2/\pi},\]

and \(\mathbb E_{P_n}K_n/n\to x\). The latter also implies \(\mathbb E_{P_n}\tau_n(U_n)\to t>0\). Inserting these limits in (2) yields the displayed sharp constant.

**4. Exact exceptional set.** The affine tilt (1) is independent of \(k\) if and only if

\[\frac{a}{1-b}=\frac{b}{1-a}\quad\Longleftrightarrow\quad (a-b)(1-a-b)=0.\]

For these and only these parameter pairs \(P_n=Q_n\) for all admissible \(n,s\) having at least two support points. Off these curves \(g\ne0\), while \(\sigma,t>0\); hence the limit is positive. This proves the classification.

## Verification

Run `python verify_markov_run_tv.py` using Python 3 and its standard library. Its exact-rational calculations enumerate all binary trajectories for lengths \(3\le n\le8\), six pairs of strictly interior rational transition probabilities, and every admissible composition/run-count pair, verifying (1). It also computes the exact finite conditional tilt by log-gamma normalization for samples of size \(4000\), comparing five parameter configurations against the sharp limiting constant; two configurations have exactly zero distance. The checker reports `PASS 281 independent finite/limit checks`. Finite experiments support but do not establish the general asymptotic theorem; that rests on the Stirling/strict-concavity proof above.

## Relationship to prior work

Exact finite joint and conditional distributions for Markov-dependent binary run tests are classical. Corzo and Vergara (2016), especially their equation (2.5), give a conditional run-count formula at fixed occupancy and transition parameters. The finite tilt (1) is a re-expression of information already recoverable from their formulas; it is included **only as the starting identity**, not claimed as a new finite distribution. Savelyev and Balakin (2004) analyze the joint distribution of ones and runs of ones, including Gaussian approximations; their available abstract indicates relevant broader coverage, but the complete paper was not available for determining whether this precise parity-adjacent conditioning constant appears implicitly. Xia and Zhang (2010, first arXiv posting) analyze approximations to the unconditioned Markov-binomial count.

The specific claim assessed here is the **sharp \(\sqrt n\)-scaled total-variation limit between occupancy laws conditioned on adjacent even and odd counts of total runs**, including its two distinct exact-zero parameter curves and explicit positive coefficient. A generic Gaussian approximation or an exact finite joint table does not by itself supply the absolute first-moment asymptotic at this separation scale; the conditional discrete saddle-point analysis in Step 3 is essential. This distinction does not establish global publication priority: an earlier implicit saddle-point expansion may still cover the result.

## Limitations

The asymptotic is for fixed interior \(a,b,\rho\), not for rare-transition, boundary-density, or parameter-varying triangular-array regimes. The finite tilt is not claimed novel, and the 2004 joint-runs paper was inaccessible in full. Asymptotic total-variation equivalence does not imply equal conditional distributions off the two exceptional curves. No external independent audit or publication-priority certification has been performed.

## References

1. J. A. Corzo and M. E. Vergara, *A data driven runs test to identify first order positive Markovian dependence*, Hacettepe Journal of Mathematics and Statistics **45** (2016), 521–540, doi:10.15672/HJMS.2015559562, especially equations (2.4)–(2.5). Full paper: https://dergipark.org.tr/en/download/article-file/644858.
2. L. Ya. Savelyev and S. V. Balakin, *The joint distribution of the number of ones and the number of 1-runs in binary Markov sequences*, Discrete Mathematics and Applications **14** (2004), 353–372, doi:10.1163/1569392041938802. Abstract available; full text not inspected.
3. A. Xia and M. Zhang, *On approximation of Markov binomial distributions*, Bernoulli **15** (2009), 1335–1350; arXiv:1001.2144 (first posted 2010-01-13), doi:10.3150/09-BEJ194. Full article inspected in its open arXiv version.
