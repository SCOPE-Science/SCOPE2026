# Pattern-sufficient conditional descent means in uniform random matchings

## Finding
Let \(N=2n\), and let \(\pi\) be the uniformly distributed fixed-point-free involution on \(\{1,\ldots,N\}\). Choose uniformly a set of \(k\) of its \(n\) pairs. Order their \(m=2k\) endpoints and encode their paired ranks by the involution \(\tau\) on \(\{1,\ldots,m\}\). For any permutation \(\sigma\), write \(D(\sigma)=\sum_{i=1}^{|\sigma|-1}\mathbf 1\{\sigma(i)>\sigma(i+1)\}\). **For every \(n\ge1\), \(1\le k\le n\), and every fixed-point-free involution \(\tau\) on \(m\) ranks,**
\[
\mathbb E[D(\pi)\mid\tau]=\frac N2+\frac mN\left(D(\tau)-\frac m2\right)=n+\frac kn(D(\tau)-k).
\]
In particular, for \(n\ge2\), let \(C\), \(H\), and \(A\) count unordered pairs of matching chords which cross, nest, and align, respectively, in the linear endpoint order. Then
\[
\operatorname{Cov}(D(\pi),C)=-\frac{n-1}{3},\quad
\operatorname{Cov}(D(\pi),H)=\frac{n-1}{3},\quad
\operatorname{Cov}(D(\pi),A)=0.
\]
The regression is *pattern-sufficient*: the entire induced marked matching influences this particular conditional mean only through its descent count. No independence statement follows from the zero covariance.

## Assumptions and scope
A matching is a partition of the labeled linearly ordered set \(\{1,\ldots,2n\}\) into unordered pairs, sampled uniformly from all \((2n-1)!!\) matchings. Its partner permutation is \(\pi\). The \(k\) marked pairs are sampled uniformly without replacement after drawing the matching. The induced matching \(\tau\) on ordered endpoint ranks is a complete observable of the marked submatching. A crossing has endpoint pattern \((1,3),(2,4)\); nesting has \((1,4),(2,3)\); alignment has \((1,2),(3,4)\). These are all three possibilities for two selected pairs. \(D\) counts strict descents at linear neighboring indices, not a cyclic descent and not \(D+1\).

## Proof
**Uniform residual law.** Condition on \(\tau\). The set \(S=\{s_1<\cdots<s_m\}\) of marked endpoints is uniform among \(m\)-subsets of \(\{1,\ldots,N\}\): the number of completions for any \(S\) and given \(\tau\) is \((N-m-1)!!\) (interpreted as \(1\) when \(m=N\)). On its complement, consisting of \(r=N-m\) endpoints, the unmarked matching is uniform, independently of \(S\).

**Exchangeable gaps.** Put \(G_0=s_1-1\), \(G_j=s_{j+1}-s_j-1\) for \(1\le j<m\), and \(G_m=N-s_m\). The gap vector ranges uniformly over all nonnegative \((m+1)\)-tuples summing to \(r\) and is exchangeable. Hence \(\mathbb P(G_j=0)=m/N\) and \(\mathbb P(G_j>0)=r/N\) for every gap index. For \(r>0\), set \(U=\mathbb E[G_0\mathbf1_{G_0>0}]\) and \(V=\mathbb E[G_1\mathbf1_{G_0>0}]\). Since all gaps total \(r\),
\[
U+mV=r\,\mathbb P(G_0>0)=r^2/N.
\]

**Both neighboring endpoints marked.** The only marked-marked neighbors are consecutive marked ranks \(j,j+1\) with \(G_j=0\). Such a pair forms a descent exactly when \(\tau(j)>\tau(j+1)\). Their total expected contribution is \(mD(\tau)/N\).

**Both neighboring endpoints unmarked.** For \(r\ge2\), the probability that a fixed neighboring pair in the full line consists of unmarked points is \(r(r-1)/(N(N-1))\). Conditional on those two points being consecutive in the unmarked ordered subset, the partner values form a descent with probability \(r/[2(r-1)]\): with probability \(1/(r-1)\) they match each other (forcing a descent), and otherwise partner order is symmetric. Summing over the \(N-1\) full-line neighboring pairs yields \(r^2/(2N)\). With \(r=0\), the contribution is zero, agreeing with that formula.

**Exactly one endpoint marked.** Fix the marked rank \(j\), whose partner has marked rank \(t=\tau(j)\ne j\). When \(G_{j-1}>0\), its immediate left neighbor is an unmarked point; the left-to-right comparison is a descent exactly when that neighbor's partner exceeds \(s_t\). When \(G_j>0\), the immediate right neighbor is unmarked; the comparison is a descent exactly when that neighbor's partner is below \(s_t\). For \(r\ge2\), the other endpoint of any given unmarked point is uniform among the *other \(r-1\) unmarked points*. Thus the sum of the two conditional descent probabilities, averaged over gaps, has numerator
\[
\mathbb E\!\left[\mathbf1_{G_{j-1}>0}\sum_{h=t}^{m}G_h+\mathbf1_{G_j>0}\sum_{h=0}^{t-1}G_h\right]
-\mathbb P(G_0>0).
\]
The subtraction excludes the current unmarked point, which lies above \(s_t\) in the left-neighbor comparison when \(t<j\), or below \(s_t\) in the right-neighbor comparison when \(t>j\). Exactly one of those two cases occurs. The two gap-index sums partition all gap indices; precisely one of the two indicator gaps lies in its accompanying sum (because \(t\ne j\)). Exchangeability therefore identifies the first expectation as \(U+mV=r^2/N\). Division by \(r-1\) gives the expected contribution \((r^2/N-r/N)/(r-1)=r/N\) from this marked endpoint. Summed over all \(m\) marked endpoints, mixed neighbors contribute \(mr/N\). For \(r=0\), none exist, again matching the formula.

**Combine.** By the exhaustive partition into the three neighbor types,
\[
\mathbb E[D(\pi)\mid\tau]
=\frac{mD(\tau)}N+\frac{r^2}{2N}+\frac{mr}N
=\frac N2+\frac mN\left(D(\tau)-\frac m2\right).
\]
In particular its unconditional expectation is \(n\), either by symmetry of \(\pi\) under rank reversal or by direct averaging of this formula.

**Chord-pair covariance.** Selecting two distinct matching pairs uniformly gives, with equal probability \(1/3\), one of the three rank patterns \(\tau_A=(2,1,4,3)\), \(\tau_C=(3,4,1,2)\), and \(\tau_H=(4,3,2,1)\), whose descent counts are respectively \(2,1,3\). Taking \(k=2\) in the regression formula yields conditional means \(n\), \(n-2/n\), and \(n+2/n\). The count of pairs of any one type is the sum over all \(\binom n2\) pair choices of its indicator; conditioning on the pattern of a uniformly marked pair therefore gives
\[
\operatorname{Cov}(D(\pi),X_T)=\binom n2\mathbb P(T)\bigl(\mathbb E[D(\pi)\mid T]-n\bigr).
\]
Substituting the three means proves the displayed covariance identities.

## Verification
The standalone `verify.py` enumerates every perfect matching and all subsets of marked edges for all \(1\le n\le5\), tests every realized rank pattern using exact rational arithmetic, and checks the three chord-pair covariance formulas directly for \(2\le n\le5\). This exhaustive *finite* verification is independent of, and does not replace, the all-parameter combinatorial proof above.

## Relationship to prior work
Kim's 2017 analysis of descents of uniform matchings supplies the unconditioned mean and descent-moment background. Kasraoui–Zeng study joint crossing/nesting/alignment statistics, without the conditional marked-pattern regression or its signed covariance with permutation descents in the inspected material. Work on limit theorems for uniform chord diagrams addresses crossing statistics and their asymptotics. These antecedents motivate the questions; their marginal formulas do not by themselves imply the all-\(k\) pattern-sufficient conditional expectation proved here.

## Limitations
The claim is for a uniform matching on linearly ordered labels and uniformly marked edges. It does not assert a full conditional distribution, independence, a central-limit theorem, or extensions to nonuniform weights. Historical priority is conditional on the checked, nonexhaustive literature; equivalent findings may be unindexed, differently formulated, or contained in uninspected work. The finite verification covers only \(n\le5\).

## References
1. Gene B. Kim, *Distribution of descents in matchings*, arXiv:1710.03896v1 (first posted 2017-10-11), especially its mean formula and Section 2.
2. Anisse Kasraoui and Jiang Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, arXiv:math/0601081v1 (first posted 2006-01-04).
3. Juanita Paguyo, *Convergence rates of limit theorems for random chord diagrams*, arXiv:2104.01134 (2021).
