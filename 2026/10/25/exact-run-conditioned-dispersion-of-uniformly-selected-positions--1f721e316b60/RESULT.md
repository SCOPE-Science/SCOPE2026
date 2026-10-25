# Exact run-conditioned dispersion of uniformly selected positions

## Finding

Let \(N\ge2\) and \(2\le k\le N\) be integers. Choose a \(k\)-element subset \(\{A_1<\cdots<A_k\}\) of \(\{1,\ldots,N\}\) uniformly. Define \(R\) to be the number of maximal nonempty blocks of consecutive selected integers, and define the usual unbiased sample variance of their positions by
\[
V=\frac1{k-1}\sum_{i=1}^k(A_i-\bar A)^2
 =\frac1{k(k-1)}\sum_{1\le i<j\le k}(A_j-A_i)^2,
\qquad \bar A=\frac1k\sum_{i=1}^k A_i.
\]
For every attainable integer \(1\le r\le\min\{k,N-k+1\}\), the exact conditional expectation is
\[
\boxed{\mathbb E[V\mid R=r]=
\frac{k(k+1)}{12}+
\frac{(k+1)(N-k+2)(N+k+1)}{12(k-1)}\frac{r-1}{r+1}.}
\tag{1}
\]
In particular, if \(2\le k<N\), it is strictly increasing in the attainable run count, with difference
\[
\mathbb E[V\mid R=r+1]-\mathbb E[V\mid R=r]
=\frac{(k+1)(N-k+2)(N+k+1)}{6(k-1)(r+1)(r+2)}>0.
\tag{2}
\]
The resulting **unconditional** covariance is exactly
\[
\boxed{\operatorname{Cov}(R,V)=\frac{(N-k)(N+k+1)}{6N},}
\tag{3}
\]
strictly positive for \(k<N\) and zero for \(k=N\).

## Assumptions and scope

Sampling is without replacement from the finite, equally spaced population \(\{1,\ldots,N\}\); no independent Bernoulli sampling or Poisson approximation is used. The statistic \(R\) counts runs of **selected sites (ones)**, not all runs in the associated binary incidence word. All formulae are exact and have the stated inclusive finite-integer ranges. If \(k=N\), necessarily \(R=1\). Every conditioning event in (1) has positive probability, given explicitly by
\[
\Pr(R=r)=\frac{\binom{k-1}{r-1}\binom{N-k+1}{r}}{\binom Nk}.
\tag{4}
\]
Neither strict stochastic ordering of the full conditional variance distributions nor independence of the statistics is claimed.

## Proof

Write the internal unselected-gap lengths as \(G_h=A_{h+1}-A_h-1\), for \(1\le h\le k-1\), and put \(G_0=A_1-1\), \(G_k=N-A_k\). These are nonnegative integers with \(\sum_{h=0}^{k}G_h=N-k\), and the subset corresponds bijectively to its gap composition. Since \(R=1+\#\{h:1\le h\le k-1,\,G_h>0\}\), conditioning on \(R=r\) makes the set \(J\) of positive internal-gap indices a uniformly chosen \((r-1)\)-subset of \(\{1,\ldots,k-1\}\).

Put \(q=r-1\), \(m=N-k\), \(b=r+1\), and \(M=m-q\). On the chosen \(q\) internal indices write \(G_h=1+Y_h\), while all other internal gaps are zero. Together with the two outer gaps \(G_0,G_k\), the \(q\) residual internal values \(Y_h\) constitute a uniformly random weak composition of \(M\) into \(b\) labeled bins, independent of \(J\). There are \(\binom{k-1}{q}\binom{M+b-1}{b-1}=\binom{k-1}{r-1}\binom{N-k+1}{r}\) such configurations, proving (4).

For two distinct bins of this weak composition, elementary stars-and-bars factorial-moment identities give
\[
\mathbb E Y=\frac Mb,\qquad
\mathbb E[Y(Y-1)]=\frac{2M(M-1)}{b(b+1)},\qquad
\mathbb E[Y_iY_j]=\frac{M(M-1)}{b(b+1)}.
\tag{5}
\]
These identities also hold when \(M=0\). For \(k\ge3\), exchangeability of \(J\) yields, for distinct internal indices \(h,\ell\),
\[
\begin{aligned}
\mu:=\mathbb E[G_h\mid R=r]
 &=\frac{q}{k-1}\left(1+\frac Mb\right),\\
\alpha:=\mathbb E[G_h^2\mid R=r]
 &=\frac{q}{k-1}\left(1+\frac{3M}{b}
      +\frac{2M(M-1)}{b(b+1)}\right),\\
\beta:=\mathbb E[G_hG_\ell\mid R=r]
 &=\frac{q(q-1)}{(k-1)(k-2)}\left(1+\frac{2M}{b}
      +\frac{M(M-1)}{b(b+1)}\right).
\end{aligned}
\tag{6}
\]
For \(d=j-i\), the distance between selected sites is \(A_j-A_i=d+\sum_{h=i}^{j-1}G_h\). Expanding its square and using (6),
\[
\mathbb E[(A_j-A_i)^2\mid R=r]
=d^2(1+2\mu+\beta)+d(\alpha-\beta).
\tag{7}
\]
There are \(k-d\) pairs with index separation \(d\). Since
\[
\sum_{d=1}^{k-1}(k-d)d=\frac{k(k^2-1)}6,
\qquad
\sum_{d=1}^{k-1}(k-d)d^2=\frac{k^2(k^2-1)}{12},
\tag{8}
\]
substituting (7) into the pairwise representation of \(V\), then (6) with \(M=N-k-r+1\) and \(b=r+1\), cancels to exactly (1). When \(k=2\), the same identity follows directly: \(R=1\) means an adjacent selected pair, so \(V=1/2\); at \(R=2\), a pair at distance \(d\ge2\) has multiplicity \(N-d\) and \(V=d^2/2\). Evaluating \(\sum_{d=2}^{N-1}(N-d)d^2\big/\big(2\sum_{d=2}^{N-1}(N-d)\big)\) gives (1) at \(r=2\), whenever that event exists. Formula (2) is the direct difference between consecutive evaluations of (1).

For an independent derivation of (3), let \(I_e\) indicate that the two endpoints of a lattice edge \(e=\{i,i+1\}\) are sampled; then \(R=k-\sum_e I_e\). For pairs \(f=\{a,b\}\), \(a<b\), let \(J_f\) indicate that both endpoints are sampled and put \(w_f=(b-a)^2\). Then \(V=\sum_f w_fJ_f/[k(k-1)]\). For \(N\ge4\), group edge–pair incidences by \(h=|e\cup f|\in\{2,3,4\}\). Their total weights are
\[
\begin{aligned}
W&:=\sum_{a<b}(b-a)^2=\frac{N^2(N^2-1)}{12},\\
S_2&=N-1,\\
S_3&=4W-2\sum_{j=1}^{N-1}j^2-2(N-1)
 =\frac{(N-1)(N-2)(N^2+N+3)}3,\\
S_4&=(N-1)W-S_2-S_3.
\end{aligned}
\tag{9}
\]
Here the formula for \(S_3\) counts the adjacent lattice edges incident to precisely one endpoint of \(f\). With \((t)_{\underline h}=t(t-1)\cdots(t-h+1)\), and interpreting \((k)_{\underline h}=0\) for \(h>k\), exact inclusion sampling gives
\[
\operatorname{Cov}(R,V)=-\frac1{k(k-1)}
\sum_{h=2}^4 S_h\left(\frac{(k)_{\underline h}}{(N)_{\underline h}}
  -\left(\frac{(k)_{\underline2}}{(N)_{\underline2}}\right)^2\right).
\tag{10}
\]
Substitution of (9) simplifies to (3). The small cases \(N=2\) (only \(k=2\)) and \(N=3\) follow by direct enumeration: the only nonconstant case is \((N,k)=(3,2)\), where the covariance equals \(1/3\), consistent with (3). This completes the finite-sample proof.

## Verification

The standalone standard-library script `VERIFY.py` checks (1) and (4) by exhaustive enumeration of every subset with \(2\le N\le13\) and \(2\le k\le N\). It separately checks the full covariance (3), the weak-composition moments against (1) across all attainable parameters with \(N\le80\), and the distinct union-size overlap computation (10) for \(N\le120\). It checks strict adjacent conditional-mean differences wherever two runs counts are attainable. On replay, it enumerates 16,278 samples, checks 239 conditional groups, 45,020 gap-moment identities, 7,137 overlap covariances, and 41,860 strict differences, all using exact rational arithmetic. The general results are proved above, independently of these finite checks.

## Relationship to prior work

Classical fixed-composition runs tests study the total number of runs or sequences of run lengths. The historical analysis of Barton and David, *Multiple Runs* (1957), supplies a directly related archival point of departure; the accessible publisher record identifies the topic, but the original full text could not be examined. Smeeton and Cox's *Do-it-yourself Shuffling and the Number of Runs under Randomness* (2003), inspected in full, studies shuffling-based run-count distributions and their use for detecting clustering, but does not report the joint run-conditioned quadratic position dispersion (1) or covariance (3). The exact local covariance field of binary transition indicators in the previously published work *Exact dependence phases of fixed-composition run transitions* is a distinct second-order object: it concerns neighboring indicator pairs, and does not determine the conditional quadratic dispersion of the locations of all selected sites. The present result uses a run-conditioned weak-composition decomposition that is more specific than either the standard marginal runs law or the unconditional finite-population variance formula.

## Limitations

This is a theorem about the conditional **mean** of a quadratic statistic, not its conditional distribution, variance or a claim of independence. It addresses one-dimensional equally spaced populations and uniform fixed-size subsets; arbitrary unequal site weights and independent Bernoulli thinning are not covered. The identity by itself does not provide optimality or power guarantees for a combined statistical test. Older scanned runs literature, particularly Barton and David (1957) and Mood (1940), may contain equivalent formulations or stronger results; a complete historical-priority claim is not made. Publication/source dates in the references are not dates for the finding proved here.

## References

1. D. E. Barton and F. N. David, “Multiple Runs,” *Biometrika* **44** (1957), 168–178, DOI: 10.1093/biomet/44.1-2.168. Publisher records show 01 June 1957 as the public date of this archival reference.
2. N. Smeeton and N. J. Cox, “Do-it-yourself Shuffling and the Number of Runs under Randomness,” *The Stata Journal* **3** (2003), 270–277, DOI: 10.1177/1536867X0300300304.
3. A. M. Mood, “The Distribution Theory of Runs,” *Annals of Mathematical Statistics* **11** (1940), 367–392, DOI: 10.1214/aoms/1177731825 (only December 1940 verified, no assumed day).
4. “Exact dependence phases of fixed-composition run transitions,” previously published mathematical research, 2026; relevant accessible full scientific statement, distinct local-indicator problem.
