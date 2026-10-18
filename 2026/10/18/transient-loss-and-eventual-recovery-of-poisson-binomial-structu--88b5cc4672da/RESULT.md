# Transient loss and eventual recovery of Poisson–binomial structure for discrete record counts

## Finding
Let \(X_1,X_2,\ldots\) be independent, identically distributed observations on the ordered alphabet \(\{1,\ldots,d\}\), with \(d\ge2\) and strictly positive atom probabilities \(p_1,\ldots,p_d\). Define the number of strict **new** upper records after the initial observation by
\[
R_n=\sum_{t=2}^{n}\mathbf1\{X_t>\max(X_1,\ldots,X_{t-1})\},\qquad n\ge1.
\]
Put \(q_i=p_i/(p_i+\cdots+p_d)\) for \(1\le i<d\). The limiting record count has the known independent-Bernoulli representation
\[
R_\infty\ \overset{\mathrm d}=\ \sum_{i=1}^{d-1}\operatorname{Bernoulli}(q_i),
\]
with independent summands, and the same natural coupling satisfies
\[
d_{\mathrm{TV}}(\mathcal L(R_n),\mathcal L(R_\infty))\le (1-p_d)^n.
\]
Consequently, **if the \(q_i\) are pairwise distinct, there is a finite \(n_0\) such that \(R_n\) is Poisson–binomial for every integer \(n\ge n_0\)**. In contrast, finite horizons can destroy the Poisson–binomial property even under identical independent observations:

1. With five ordered atoms of probabilities \((1,1,1,1,8)/12\), the three-observation record count has generating polynomial
\[
G_3(z)=\frac{197}{288}+\frac{247}{864}z+\frac{13}{432}z^2,
\quad \left(\frac{247}{864}\right)^2-4\frac{197}{288}\frac{13}{432}=-\frac{455}{746496}<0.
\]
2. With four ordered atoms of probabilities \((1,1,1,5)/8\), the four-observation record count has generating polynomial
\[
G_4(z)=\frac{649}{1024}+\frac{1309}{4096}z+\frac{93}{2048}z^2+\frac5{4096}z^3,
\]
whose cubic discriminant is \(-61127/274877906944<0\).

Both counterexamples occur on an open neighbourhood of the displayed interior probability vectors because the discriminants are strictly negative. The first counterexample occurs at the earliest possible sample length for failure: for \(n\le2\), \(R_n\) is always Bernoulli (or constant). No claim of minimum alphabet size is made. Each displayed law has distinct \(q_i\), hence finite-horizon nonrepresentability is transient and eventual representability is exact.

## Assumptions and scope
The alphabet is finite and linearly ordered; probabilities are strictly positive; record-breaking is strict, so ties do **not** count. The initial sample is regarded as the first record value, but it contributes zero to \(R_n\). A Poisson–binomial variable means a sum of finitely many **independent** Bernoulli variables, including parameters zero or one. The existence threshold \(n_0\) is qualitative, depending on the probability vector; there is no universal value asserted. Neither independent record indicators at finite horizons nor convergence in parameter-uniform total variation is claimed.

## Proof
**Infinite-record law and quantitative coupling.** For each letter \(i\), its first arrival can be represented by an independent exponential clock \(T_i\) with rate \(p_i\), because Poissonising the common iid categorical stream splits it into independent processes. The order of clock arrivals equals the order of first occurrences of the letters. For \(i<d\), letter \(i\) ever becomes an upper-record *value* exactly when \(T_i<\min_{j>i}T_j\). The probability of this event is \(q_i\). In an exponential race the time of the first arrival is independent of the remaining relative clock order; inducting down the suffixes \(\{i,\ldots,d\}\) shows that these \(d-1\) events are mutually independent. Letter \(d\) is always a record value, and removing the initial record subtracts one from the total number of record values. This proves the claimed independent-Bernoulli law; it is consistent with the established discrete record-value independence cited below.

Once the highest category \(d\) has appeared, no further new strict record is possible. Thus \(R_n=R_\infty\) whenever at least one of the first \(n\) observations equals \(d\). The exception probability is \((1-p_d)^n\), proving the coupling bound.

**Exact finite failures.** For any categorical law and \(n=3\), let \(F_i=\sum_{j\le i}p_j\). Then
\[
\Pr(R_3=0)=\sum_i p_iF_i^2,\qquad
\Pr(R_3=2)=\sum_{i<j<k}p_ip_jp_k,
\]
with the middle probability given by subtraction from one. The first identity conditions on the first sample; the second is exactly the event \(X_1<X_2<X_3\). Substitution of \((1,1,1,1,8)/12\) yields the displayed coefficients and negative quadratic discriminant. Any Poisson–binomial law with support contained in \(\{0,1,2\}\) factors into at most two nontrivial Bernoulli factors, so its quadratic generating polynomial must have real nonpositive roots. A negative discriminant contradicts this.

For \(n=4\), track the current maximum and number of strict new records by the exact recursion
\[
 a_{t+1}(j,k)=\sum_{i\le j} p_j\,a_t(i,k-\mathbf1\{j>i\})
 +a_t(j,k)\sum_{h<j}p_h,
\]
with \(a_1(i,0)=p_i\), zero outside the indicated ranges. The first term accounts for drawing a new value equal to the new maximum; its \(i=j\) contribution is the tie, while the second term covers strictly smaller draws. Here \(G_t(z)=\sum_{j,k}a_t(j,k)z^k\). Applying the recursion to \((1,1,1,5)/8\) gives the stated cubic. With coefficients \(a,b,c,d\) from highest degree to constant, the cubic discriminant is
\[
18abcd-4b^3d+b^2c^2-4ac^3-27a^2d^2=-\frac{61127}{274877906944}.
\]
Every Poisson–binomial polynomial has only real nonpositive zeros; a negative cubic discriminant gives one real and two nonreal zeros. Again the representation is impossible.

**Eventual restoration.** Coefficientwise, \(G_n(z)=\mathbb E[z^{R_n}]\) converges to
\[
G_\infty(z)=\prod_{i=1}^{d-1}(1-q_i+q_iz).
\]
For pairwise distinct \(q_i\), this has \(d-1\) distinct negative real zeros. A sufficiently small real coefficient perturbation of a real polynomial with simple real zeros retains one simple real zero in a disjoint interval around each of them (for instance by endpoint sign changes plus degree counting). Since the highest coefficient of \(G_n\) converges to a strictly positive number, for all sufficiently large \(n\) it has exactly degree \(d-1\) and all roots simple, negative, and real. Normalization \(G_n(1)=1\) then factors it as \(\prod_{i=1}^{d-1}(1-\theta_{i,n}+\theta_{i,n}z)\) with \(0<\theta_{i,n}<1\), proving its Poisson–binomial representation. The two explicit probability vectors satisfy distinctness of the corresponding \(q_i\).

## Verification
The accompanying `verify.py` uses only exact rational arithmetic. It independently enumerates all \(5^3\) and \(4^4\) observation words, checks the two coefficient vectors and both negative discriminants, and independently reconstructs the limiting record count from all size-biased first-appearance permutations. It also verifies 48 instances of the finite-state recurrence, normalization, and the total-variation bound on several positive probability vectors. Its output is a finite consistency check, not a proof of the universal statements above.

## Relationship to prior work
Lafuente, Gouet, López, and Sanz (2022), in their paper on near-record values, state and use the classical fact that indicators of **eventual discrete record values** are independent Bernoulli variables (their Lemma 1(a)). That established fact supports the limiting representation here; it does not classify the fixed-time distribution of the **number of strict new records**. Li (2022) concerns records relative to a moving window of fixed width, rather than all-time upper records observed up to a fixed horizon. Tang and Tang (2019) describe the classical connection between real-rooted probability-generating polynomials and Poisson–binomial laws. Serinaldi and Kilsby (2018) discuss independent record-event representations for iid settings, commonly under continuous/no-tie assumptions; this does not settle the discrete-tie finite-horizon examples. The proposed contribution is the paired exact finite-horizon obstructions and their rigorous reconciliation with eventual Poisson–binomial recovery for generic finite alphabets. The infinite-horizon independence theorem, real-rootedness characterization, and elementary root-continuity principle are not claimed as new.

## Limitations
No universal bound on the eventual restoration time is obtained. The examples do not establish the least alphabet size permitting failure at each horizon, nor characterize all distributions for which finite-horizon real-rootedness holds. Published literature may contain equivalent examples under alternative terminology. No independent audit has been performed.

## References
1. M. Lafuente, R. Gouet, F. J. López, and G. Sanz, *Near-Record Values in Discrete Random Sequences*, Mathematics 10 (2022), 2442. DOI: 10.3390/math10142442; first public version confirmed 2022-07-13; MSC 60G70 (primary).
2. A. Li, *On the recent-\(k\)-record of discrete random variables*, arXiv:2208.06791 (2022), https://arxiv.org/abs/2208.06791.
3. W. Tang and F. Tang, *The Poisson Binomial Distribution—Old & New*, arXiv:1908.10024 (2019), https://arxiv.org/abs/1908.10024.
4. F. Serinaldi and C. G. Kilsby, *Unsurprising Surprises: The Frequency of Record-breaking and Overthreshold Hydrological Extremes Under Spatial and Temporal Dependence*, Water Resources Research 54 (2018), DOI: 10.1029/2018WR023055.
