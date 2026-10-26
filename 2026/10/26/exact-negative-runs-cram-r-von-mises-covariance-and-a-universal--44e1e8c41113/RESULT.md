# Exact negative runs–Cramér–von Mises covariance and a universal correlation constant

## Finding

Fix integers \(a,b\ge1\), put \(N=a+b\), and uniformly shuffle \(a\) ones and \(b\) zeros into \(X_1,\ldots,X_N\). Let \(A_t=\sum_{i=1}^{t}X_i\) and \(D_t=NA_t-at\). Define the Wald–Wolfowitz runs statistic and the null-normalized two-sample Cramér–von Mises statistic by
\[
R=1+\sum_{j=1}^{N-1}\mathbf 1\{X_j\ne X_{j+1}\},\qquad
T=\frac{1}{abN^2}\sum_{t=1}^{N-1}D_t^2.
\]
Under the continuous equal-distribution two-sample null, the pooled sample-label sequence is exactly this uniform binary shuffle, and \(T\) is the Anderson two-sample statistic \((ab/N)\int(F_a-G_b)^2\,dH_N\), where \(H_N=(aF_a+bG_b)/N\).

For **every** \(a,b\ge1\),
\[
\boxed{\operatorname{Cov}(R,T)=\frac{N-2ab}{3N^2}.}
\]
This covariance is **strictly negative whenever \(N\ge3\)**. For \(N=2\), the run count is constant and the covariance vanishes. The equivalent unnormalized identity for \(Q=abN^2T\) is
\[
\operatorname{Cov}(R,Q)=\frac{ab(N-2ab)}{3}.
\]
In addition, along any sequence \(N\to\infty\) with \(a/N\to p\in(0,1)\), the correlation has the **sample-allocation-independent** first-order law
\[
\boxed{\sqrt N\,\operatorname{Corr}(R,T)\longrightarrow-\sqrt5.}
\]
Thus the two statistics are negatively correlated at every nontrivial finite size, even though their correlation decays universally at rate \(N^{-1/2}\).

## Assumptions and scope

All randomization is conditional on fixed class sizes \(a,b\), with every binary sequence of those counts equally likely. Under the distribution-free interpretation, both samples are independent, identically distributed under the null, and the common law is continuous (no pooled ties). The statistic \(T\) is the *ordinary two-sample empirical-CDF Cramér–von Mises* statistic, not a centered, differently weighted, or integrated-empirical-process modification. The exact covariance holds for all positive integer sizes, including heavily imbalanced allocations. The correlation limit assumes both limiting class proportions are strictly between zero and one; the theorem asserts no particular correlation limit for sparse allocations.

## Proof

Set \(Q=\sum_{t=1}^{N-1}D_t^2\), \(c=ab\), and \(I_j=\mathbf1\{X_j\ne X_{j+1}\}\). Simple sampling without replacement yields
\[
\mathbb E[D_t]=0,\qquad
\mathbb E[D_t^2]=\frac{ct(N-t)}{N-1},\qquad
\mathbb EQ=\frac{cN(N+1)}6,
\]
and exchangeability gives \(\Pr(I_j=1)=2c/[N(N-1)]\), the same for every \(j\). Consequently,
\[
\operatorname{Cov}(R,Q)=\frac{2c}{N(N-1)}\sum_{j=1}^{N-1}\delta_j,
\qquad
\delta_j=\mathbb E[Q\mid I_j=1]-\mathbb EQ.
\tag{1}
\]
For \(N\ge4\), condition on \(I_j=1\). The two symbols at positions \(j,j+1\) are one zero and one one in equiprobable order. They are independent of a uniform ordering of the remaining \(a-1\) ones and \(b-1\) zeros. If \(H_h\) denotes the number of ones in the first \(h\) positions of the latter ordering, then
\[
\mathbb EH_h=\frac{h(a-1)}{N-2},\qquad
\operatorname{Var}(H_h)=\frac{h(N-2-h)(a-1)(b-1)}{(N-2)^2(N-3)}.
\]
The conditional distribution of \(A_t\) is that of \(H_t\) for \(t<j\), of \(H_{j-1}+B\) for \(t=j\), and of \(H_{t-2}+1\) for \(t>j\), with an independent fair Bernoulli \(B\). Therefore, for each \(t\), its conditional quadratic moment follows from
\[
\mathbb E[D_t^2\mid I_j=1]=N^2(\operatorname{Var}(H_h)+v_B)
+\bigl(N[\mathbb EH_h+\mu_B]-at\bigr)^2,
\]
where the triple \((h,\mu_B,v_B)\) is \((t,0,0)\), \((j-1,1/2,1/4)\), or \((t-2,1,0)\) in the three cases. Subtract the unconditional moment and sum over \(t=1,\ldots,N-1\). Elementary sums of first and second powers yield the **exact conditional-influence profile**
\[
\delta_j=\frac{N}{6(N-2)(N-3)}\Bigl[
(36c-6N(N+1))j(N-j)+N^4+3N^3-4N^2+6N
-c(8N^2-4N+12)\Bigr].
\tag{2}
\]
Using \(\sum_{j=1}^{N-1}j(N-j)=N(N-1)(N+1)/6\) simplifies the aggregate profile to
\[
\sum_{j=1}^{N-1}\delta_j=\frac{N(N-1)(N-2c)}6.
\tag{3}
\]
Substitution in (1) proves \(\operatorname{Cov}(R,Q)=c(N-2c)/3\), and division by \(cN^2\) proves the formula for \(T\). For \(N=3\), the words of either class composition yield \(\operatorname{Cov}(R,Q)=-2/3\); \(N=2\) has constant \(R\). For \(N\ge3\), \(c=ab\ge N-1\), hence \(N-2c\le2-N<0\), proving strict negativity.

To determine the correlation, summing local transition covariances, or using the classical runs formula, gives
\[
\operatorname{Var}(R)=\frac{2ab(2ab-N)}{N^2(N-1)}.
\tag{4}
\]
If \(a/N\to p\in(0,1)\), the exact covariance tends to \(-2p(1-p)/3\), while (4) implies \(\operatorname{Var}(R)/N\to4p^2(1-p)^2\). The finite-population empirical-process functional central limit theorem gives
\[
\left(\frac{NA_{\lfloor Nt\rfloor}-a\lfloor Nt\rfloor}{\sqrt{abN}}\right)_{0\le t\le1}\ \Longrightarrow\ (B(t))_{0\le t\le1},
\]
where \(B\) is a standard Brownian bridge. Thus \(T\Longrightarrow\int_0^1 B(t)^2dt\). Moreover hypergeometric Hoeffding bounds give uniformly bounded eighth moments of the displayed scaled bridge, and hence uniformly bounded fourth moments of \(T\), when \(a/N\) stays away from zero and one. In particular \(T^2\) is uniformly integrable. Since \(\operatorname{Cov}(B(s),B(t))=\min(s,t)-st\), Gaussian fourth moments give
\[
\operatorname{Var}\left(\int_0^1B(t)^2dt\right)=2\int_0^1\!\int_0^1[\min(s,t)-st]^2\,ds\,dt=\frac1{45}.
\]
Consequently \(\operatorname{Var}(T)\to1/45\), and combining the three exact or limiting moment formulas yields
\[
\sqrt N\operatorname{Corr}(R,T)
\longrightarrow\frac{-2p(1-p)/3}{2p(1-p)/\sqrt{45}}=-\sqrt5.
\]

## Verification

Run the standalone Python 3 script `verify.py` from the artifact directory. It uses only standard-library exact rational arithmetic, exhaustively enumerates every fixed-composition word for \(2\le N\le12\), independently calculates both first moments and their covariance, and checks the claimed all-size expression. A separate conditional-hypergeometric computation verifies (2), (3), and the covariance identity for every class composition through \(N=55\), without permutation enumeration at the larger sizes. A final numerical consistency check probes the limiting constant at large balanced and imbalanced compositions, **using the proved limiting variance**, rather than purporting to certify a limit numerically. The script reports 57,127 successful finite checks/consistency cases. These computations are reproducibility cross-checks, not proofs of infinite statements.

## Relationship to prior work

The Wald–Wolfowitz and Mood works establish the classical distribution-free runs framework. The full Smeeton–Cox treatment explains uniform fixed-count shuffling and the marginal run count; it does not analyze the empirical squared-bridge statistic. Anderson's two-sample Cramér–von Mises criterion is the source of the statistic studied here. The complete, accessible Xiao–Gordon–Yakovlev article gives its exact **marginal** null distribution and the same CDF normalization, but does not give a joint runs moment. A published local-transition-covariance analysis of fixed-composition runs supplies (4) and pairwise transition dependence, but does not address \(Q\), the empirical bridge, or the universal cross-statistic correlation. Separate marginal laws and local run-indicator covariances do not determine the mixed moment in this result. Targeted source, equivalence, and published-record comparisons located no implication deriving the exact covariance and asymptotic constant; absence from retrieved sources does not establish historical uniqueness.

## Limitations

This is an exact second-order mixed-moment theorem, **not** the full joint distribution of the statistics, a claim of independence, or a universal tail-dependence characterization. The asymptotic correlation concerns only nonvanishing class proportions. The complete texts of some historical original articles (including Anderson 1962 and the 1940 works) were not available in inspected sources; an earlier equivalent calculation under different notation remains a specific priority risk. The conditional-influence derivation is exact, and the limiting argument relies on the standard finite-population bridge theorem and explicit uniform-integrability control.

## References

1. A. Wald and J. Wolfowitz, “On a Test Whether Two Samples are from the Same Population,” *Annals of Mathematical Statistics* 11 (1940), 147–162, DOI: 10.1214/aoms/1177731909.
2. T. W. Anderson, “On the Distribution of the Two-Sample Cramér–von Mises Criterion,” *Annals of Mathematical Statistics* 33 (1962), 1148–1159, DOI: 10.1214/aoms/1177704477.
3. N. Smeeton and N. J. Cox, “Do-it-yourself shuffling and the number of runs under randomness,” *Stata Journal* 3 (2003), 270–277, DOI: 10.1177/1536867X0300300304.
4. Y. Xiao, A. Gordon, and A. Yakovlev, “A C++ Program for the Cramér–von Mises Two-Sample Test,” *Journal of Statistical Software* 17(8) (first public 18 December 2006), 1–15, DOI: 10.18637/jss.v017.i08.
5. “Exact dependence phases of fixed-composition run transitions,” public research record: `2026/10/4/SCOPE-exact-dependence-phases-of-fixed-composition-run-transitions--c6b28ad6d93d`; compared only for claim overlap, not treated as an archived source.
