# A unique cube-root thinning threshold for vacancy–peak-load dependence in two bins

## Finding
Let \(L\ge2\) be an integer. Independently for each of \(L\) potential objects, retain it with probability \(0\le\theta\le1\), and if retained assign it with equal probability to one of two labeled bins. Let \(X\) and \(Y\) be the occupancies; put \(V=\mathbf 1_{\{X=0\}}+\mathbf 1_{\{Y=0\}}\) and \(H=\max(X,Y)\). There is a unique \(\theta_L\in(0,1)\) such that

\[
\operatorname{Cov}(V,H)\begin{cases}<0,&0<\theta<\theta_L,\\=0,&\theta=\theta_L,\\>0,&\theta_L<\theta\le1.\end{cases}
\]

At \(\theta=0\) the covariance is zero because both statistics are deterministic. The transition has the sharp asymptotic law

\[
\lim_{L\to\infty} L^{1/3}\theta_L=\left(\frac8\pi\right)^{1/3}.
\]

For \(L=2\), \(\theta_2=3-\sqrt5\). The condition \(L\ge2\) is sharp: with one potential object the covariance is negative for every \(0<\theta<1\) and vanishes at the endpoints.

An exact finite formula determines the unique zero. For \(k\ge1\), define
\[
h(k)=\frac{\binom{2\lfloor k/2\rfloor}{\lfloor k/2\rfloor}}{4^{\lfloor k/2\rfloor}},\qquad B\sim\operatorname{Bin}(L-1,\theta).
\]
Then, for \(0<\theta\le1\),
\[
\boxed{\ \operatorname{Cov}(V,H)=(1-\theta/2)^L L\theta\left(\frac{\theta}{2-\theta}-\mathbb E[h(1+B)]\right).\ }
\]
Thus \(\theta_L\) is the unique solution in \((0,1)\) of
\[
\frac{\theta}{2-\theta}=\sum_{b=0}^{L-1}\binom{L-1}{b}\theta^b(1-\theta)^{L-1-b}h(b+1).
\]

## Assumptions and scope
All \(L\) trials are independent. Outcomes \(0,1,2\) (not retained, first bin, second bin) have probabilities \(1-\theta,\theta/2,\theta/2\). No conditioning on the number retained is imposed. The statements concern covariance of the number of vacant bins and the larger of the two occupancies, not a covariance between individual occupancy counts. The asymptotic limit concerns integer \(L\to\infty\), with \(\theta=\theta_L\) allowed to vary. The positivity at \(\theta=1\) uses \(L\ge2\).

## Proof
**Step 1: An exact occupancy identity.** By exchangeability and linearity, with \(p_0=\mathbb P(X=0)=(1-\theta/2)^L\),
\[
\operatorname{Cov}(V,H)=2p_0\bigl(\mathbb E[H\mid X=0]-\mathbb E H\bigr).
\]
Conditional on \(X=0\), each trial independently chooses bin two with conditional probability \((\theta/2)/(1-\theta/2)=\theta/(2-\theta)\), hence \(H=Y\) and \(\mathbb E[H\mid X=0]=L\theta/(2-\theta)\). Define \(D=X-Y\). The identity \(H=(X+Y+|D|)/2\), combined with \(\mathbb E(X+Y)=L\theta\), gives
\[
\operatorname{Cov}(V,H)=p_0\left(\frac{L\theta^2}{2-\theta}-\mathbb E|D|\right).\tag{1}
\]
No independence between \(V\) and \(D\) has been assumed.

**Step 2: Absolute walk moments.** Let \(K=X+Y\sim\operatorname{Bin}(L,\theta)\). Conditional on \(K=k\), the difference \(D\) has the law of a simple symmetric random walk \(S_k\) after \(k\) steps. Put \(g(k)=\mathbb E|S_k|\), \(g(0)=0\). The recurrence \(g(k+1)-g(k)=\mathbb P(S_k=0)\) gives, for integers \(r\ge0\),
\[
\frac{g(2r+1)}{2r+1}=\frac{\binom{2r}{r}}{4^r},\quad
\frac{g(2r)}{2r}=\frac{\binom{2r}{r}}{4^r}\ \ (r\ge1).
\]
Consequently \(g(k)/k=h(k)\) and
\[
h(1)=1,\qquad h(2)=1/2,\qquad h(k+1)\le h(k)\quad(k\ge1).
\]
The monotonicity is also immediate from \(\binom{2r+2}{r+1}/4^{r+1}=\binom{2r}{r}(2r+1)/(4^r(2r+2))\).

**Step 3: Size-biased binomial reduction.** For \(B\sim\operatorname{Bin}(L-1,\theta)\), the elementary identity \(k\mathbb P(K=k)=L\theta\mathbb P(B=k-1)\) yields
\[
\mathbb E|D|=\mathbb E g(K)=L\theta\,\mathbb E[h(1+B)].\tag{2}
\]
Substituting (2) into (1) proves the displayed exact covariance formula.

**Step 4: Existence, uniqueness and boundaries.** As \(\theta\) grows, \(B\sim\operatorname{Bin}(L-1,\theta)\) increases under its standard common-uniform coupling. Since \(h\) is nonincreasing, \(A_L(\theta)=\mathbb E[h(1+B)]\) is nonincreasing. It is strictly decreasing on \((0,1)\) for \(L\ge2\): in the common-uniform coupling between any two distinct parameters, an event with positive probability moves \(B\) from zero to one, and \(h(1)>h(2)\). On the other hand, \(\theta/(2-\theta)\) increases strictly. At \(\theta=0\), its value is zero while \(A_L(0)=1\); at \(\theta=1\), it equals one while \(A_L(1)=h(L)<1\). Continuity proves exactly one crossing with the stated signs. For \(L=2\), substitution gives \(\theta_2=3-\sqrt5\). For \(L=1\), \(A_1\equiv1\), and \(\operatorname{Cov}(V,H)=-\theta(1-\theta)\).

**Step 5: Sharp asymptotic constant.** Set \(\theta=cL^{-1/3}\) for fixed \(c>0\). The summands of \(D\) are independent with values \(-1,0,1\), mean zero and variance \(\theta\). Their total variance is \(L\theta=cL^{2/3}\to\infty\). The Lindeberg central limit theorem and bounded second moments of the normalized sums imply
\[
\frac{\mathbb E|D|}{\sqrt{L\theta}}\longrightarrow\mathbb E|N(0,1)|=\sqrt{\frac2\pi}.
\]
Also,
\[
\frac{L\theta^2/(2-\theta)}{\sqrt{L\theta}}=\frac{\sqrt L\,\theta^{3/2}}{2-\theta}\longrightarrow\frac{c^{3/2}}2.
\]
By (1), the covariance at \(\theta=cL^{-1/3}\) has, for all sufficiently large \(L\), the sign of \(c^{3/2}/2-\sqrt{2/\pi}\), provided the latter is nonzero. The unique-crossing property sandwiches \(L^{1/3}\theta_L\) between arbitrary fixed constants below and above the unique solution \(c_*=(8/\pi)^{1/3}\), proving the limit.

## Verification
The included standalone `verify.py` performs independent exact enumeration of all \(3^L\) outcome strings for \(2\le L\le7\) at six rational choices of \(\theta\), and compares covariances to the closed expression using exact fractions. It independently checks the central-binomial monotonicity through \(L=69\), boundary signs, and numerical roots and bracketing at sizes through \(L=1000\). All 273 programmed checks passed when executed from the embedded package contents. These finite checks corroborate but do not prove the universal assertions; Steps 1–5 provide the proof.

## Relationship to prior work
The classical multinomial maximum-load literature, including Yusas (1972/1973) and Freeman (1979), treats distributional calculations for the largest cell count. Proschan and Sethuraman (1975) analyze multivariate count inequalities. Bogachev, Gnedin and Yakubovich (2006, Sections 1–2) develop occupancy models and Poissonization, including dependence terms for occupied-cell counts. These ingredients motivate studying the **joint** behavior of vacancy and maximum occupancy when arrivals are Bernoulli-thinned. The claim here is specifically a unique finite-retention covariance transition for two bins and its cube-root asymptotics. No novelty is claimed for basic multinomial conditioning, the standard random-walk absolute moments, or central limit theory.

## Limitations
The finding does not establish a transition for three or more bins, unequal assignment probabilities, non-Bernoulli retention, or correlations in place of covariance. The size-\(L\) polynomial gives an implicit rather than elementary closed-form root for general \(L\). Priority is assessed from accessible literature and mathematical records; older articles on multinomial maxima and association could contain an implicit equivalent identity, and their full texts were not all accessible. There has been no independent scientific audit.

## References
- L. V. Bogachev, A. V. Gnedin, and Yu. V. Yakubovich, *On the variance of the number of occupied boxes*, arXiv:math/0609498 (first public version 18 September 2006), https://arxiv.org/abs/math/0609498.
- I. S. Yusas, *On the Distribution of the Maximum Frequency of a Multinomial Distribution*, *Theory of Probability & Its Applications* 17 (1972/1973), 712–717, DOI:10.1137/1117087.
- F. Proschan and J. Sethuraman, *Simple Multivariate Inequalities Using Association*, *Theory of Probability & Its Applications* 20 (1975), 193–195, DOI:10.1137/1120023.
- P. R. Freeman, *Exact Distribution of the Largest Multinomial Frequency*, *Applied Statistics* 28 (1979), 333–336, DOI:10.2307/2347220.
