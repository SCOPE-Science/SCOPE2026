# Universal finite-sample dependence of two rank-based two-sample statistics

## Finding
For integers \(a,b\geq1\), write \(N=a+b\geq3\) and \(h=ab/N^2\). Under the uniform fixed-composition binary-label null, let \(R\) be the Wald–Wolfowitz number of runs and let \(V\) be the normalized two-sample Cramér–von Mises quadratic empirical-bridge statistic, defined precisely below. Their exact moments satisfy
\[
\operatorname{Cov}(R,V)=-\frac{2Nh-1}{3N}=-\frac{2ab-N}{3N^2}<0,
\qquad
\operatorname{Var}(R)=\frac{2Nh(2Nh-1)}{N-1},
\]
\[
\mathbb{E}V=\frac{N+1}{6N},\qquad
\operatorname{Var}(V)=\frac{(N+1)(4(N+1)h-3)}{180N^2h}.
\]
In particular,
\[
\operatorname{Corr}(R,V)=-\sqrt{\frac{10(N-1)(2Nh-1)}{N(N+1)(4(N+1)h-3)}}.
\]
If \(a/N\to p\in(0,1)\), then \(\sqrt{N}\operatorname{Corr}(R,V)\to-\sqrt5\), independently of the limiting sample-size ratio. The equivalent bridge energy \(T=abV\) obeys the exact size-independent regression-slope identity
\[
\frac{\operatorname{Cov}(R,T)}{\operatorname{Var}(R)}=-\frac{N-1}{6}.
\]
Here the displayed ratio is the population least-squares slope of \(T\) on \(R\), not a claim that the conditional expectation of \(T\) given \(R\) is linear.

## Assumptions and scope
Choose uniformly a binary word \((X_1,\ldots,X_N)\in\{0,1\}^N\) containing exactly \(a\) ones and \(b\) zeros. Set \(Y_j=X_j-a/N\), \(S_k=\sum_{j=1}^kY_j\), and
\[
R=1+\sum_{i=1}^{N-1}{\bf1}\{X_i\neq X_{i+1}\},\quad
T=\sum_{k=1}^{N-1}S_k^2,\quad V=T/(ab).
\]
For continuous equal-distribution independent samples of sizes \(a\) and \(b\), the pooled labels in increasing observation order have exactly this null distribution. If \(F_a,G_b\) are the two empirical distribution functions at pooled ranks \(z_{(k)}\), then
\[
V=\frac{ab}{N^2}\sum_{k=1}^{N-1}(F_a(z_{(k)})-G_b(z_{(k)}))^2.
\]
Thus \(V\) uses the standard pooled empirical-distribution weighting convention, with no additional centering or tie corrections. When \(N=2\), both statistics are deterministic and their correlation is undefined; the theorem excludes that degenerate case.

## Proof
Put \(h=ab/N^2\). Fixed-composition exchangeability and \(\sum_jY_j=0\) imply \(\mathbb{E}Y_j=0\), \(\mathbb{E}Y_j^2=h\), \(\mathbb{E}Y_rY_s=-h/(N-1)\) for distinct indices, and \(\mathbb{E}Y_j^4=h(1-3h)\). The elementary zero-sum distance identity gives
\[
T=-\sum_{1\le r<s\le N}(s-r)Y_rY_s.
\]
Consequently \(\mathbb ET=Nh(N+1)/6\).

For \(D_i={\bf1}\{X_i\ne X_{i+1}\}\), exchangeability gives \(q=\mathbb ED_i=2Nh/(N-1)\). Conditioned on \(D_i=1\), the pair at positions \(i,i+1\) has one zero and one one in either order, and the remaining \(N-2\) coordinates form a uniform word with \(a-1\) ones. The conditional expectation \(\mathbb E[Y_rY_s\mid D_i=1]\) depends only on how many of \(r,s\) lie in \(\{i,i+1\}\). For overlaps of respectively \(0,1,2\), its values are
\[
\frac{2-(N+6)h}{(N-2)(N-3)},\qquad
-\frac{1-4h}{2(N-2)},\qquad -h.
\]
The first expression is used only for \(N\ge4\), when a disjoint pair exists. In each case \(\operatorname{Cov}(D_i,Y_rY_s)=q(\mathbb E[Y_rY_s\mid D_i=1]+h/(N-1))\). Counting each distance \(s-r\) for the three overlap classes, summed over all \(i\), gives the weights
\[
W_0=\frac{(N-3)(N-2)(N-1)(N+1)}6,\quad
W_1=(N-1)\left(\frac{N(2N-1)}3-2\right),\quad W_2=N-1.
\]
Substitution into \(\operatorname{Cov}(R,T)=-\sum_{i,r<s}(s-r)\operatorname{Cov}(D_i,Y_rY_s)\) and simplification yields
\[
\operatorname{Cov}(R,T)=-\frac{Nh(2Nh-1)}3.
\]
For \(N=3\), the same value follows by direct evaluation of the three possible locations of the minority label (and symmetry on interchanging labels). Also, \(\mathbb ED_iD_{i+1}=ab/[N(N-1)]\) and, for disjoint edges,
\[
\mathbb E D_iD_j=\frac{4a(a-1)b(b-1)}{N(N-1)(N-2)(N-3)}.
\]
Summing these overlapping and disjoint contributions gives \(\operatorname{Var}(R)=2Nh(2Nh-1)/(N-1)\), with small \(N\) handled directly.

For the variance of \(T\), use the three distinct-index moments
\[
M_{22}=\mathbb E(Y_1^2Y_2^2)=\frac{(N+3)h^2-h}{N-1},\quad
M_{211}=\mathbb E(Y_1^2Y_2Y_3)=\frac{2h-(N+6)h^2}{(N-1)(N-2)},
\]
\[
M_{1111}=\mathbb E(Y_1Y_2Y_3Y_4)=-\frac{3M_{211}}{N-3}.
\]
They follow respectively from the deterministic sum \(\sum Y_i^2=Nh\), the zero sum \(\sum Y_i=0\), and multiplying that zero sum by three distinct \(Y_i\). Writing \(w_{rs}=s-r\), direct polynomial summation gives the sum of squared weights, the sum of products over pairs of edges sharing one endpoint, and the sum over disjoint edge pairs:
\[
U_2=\frac{N^2(N^2-1)}{12},\quad
U_1=\frac{N(N-2)(N-1)(N+1)(7N+4)}{120},\quad
U_0=\frac{N(N-3)(N-2)(N-1)(N+1)(5N+4)}{360}.
\]
Therefore
\[
\mathbb ET^2=U_2M_{22}+2U_1M_{211}+2U_0M_{1111},\qquad
\operatorname{Var}(T)=\frac{N^2h(N+1)(4(N+1)h-3)}{180}.
\]
This calculation holds directly for \(N\ge4\); \(N=3\) follows from the three-word calculation. Divide the covariance by \(ab=N^2h\) and the variance by \((ab)^2\) to obtain the expressions for \(V\). The correlation formula follows by division by the two positive standard deviations. Finally, if \(h\to p(1-p)>0\), its squared value multiplied by \(N\) converges to \(5\), giving the stated negative limit. The regression slope follows by taking the ratio of \(\operatorname{Cov}(R,T)\) and \(\operatorname{Var}(R)\).

## Verification
Run `python3 verify.py` using Python 3 and the standard library. It enumerates every fixed-composition word for all \(2\le N\le11\), computes rational moments independently of the proof, and checks all six mean, variance, covariance, and regression identities. Weight and conditional-moment identities can also be checked by their displayed finite sums. The finite check supports, but does not replace, the symbolic all-size argument above.

## Relationship to prior work
The Wald–Wolfowitz runs statistic is classical; Bhattacharya (arXiv:1508.07530, first public 2015-08-30) treats its graph-based form and broader asymptotic testing framework. Ramdas, García Trillos, and Cuturi (arXiv:1509.02237, first public 2015-09-08) relate empirical-distribution two-sample criteria and their asymptotics. These works supply context and marginal-statistic results, not this finite mixed covariance or universal correlation coefficient. Nearby published analyses of pairwise transition-indicator covariances under fixed composition likewise do not imply the nonlocal bridge-energy cross-moment without an additional calculation. The present exact claim concerns the joint permutation-null law, not separate marginal distributions.

## Limitations
These are finite-sample null identities for continuous two-sample rankings with no ties; they do not give joint tail probabilities, combination-test optimality, power under alternatives, or the conditional law of \(V\) given \(R\). The correlation limit assumes both sample fractions remain bounded away from zero. The literature comparison does not certify worldwide historical priority; an earlier joint nonparametric-test analysis might contain an equivalent formula. No independent audit has been performed.

## References
1. B. B. Bhattacharya, *A General Asymptotic Framework for Distribution-Free Graph-Based Two-Sample Tests*, arXiv:1508.07530 (first public 2015-08-30), https://arxiv.org/abs/1508.07530.
2. A. Ramdas, N. García Trillos, and M. Cuturi, *On Wasserstein Two Sample Testing and Related Families of Nonparametric Tests*, arXiv:1509.02237 (first public 2015-09-08), https://arxiv.org/abs/1509.02237.
3. A. Wald and J. Wolfowitz, *On a Test Whether Two Samples Are from the Same Population*, Annals of Mathematical Statistics 11 (1940), 147–162 (historical primary source for the runs test; not used as a claim of joint-law coverage).
