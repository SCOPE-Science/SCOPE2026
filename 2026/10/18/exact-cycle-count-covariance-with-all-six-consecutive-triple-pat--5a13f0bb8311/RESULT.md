# Exact cycle-count covariance with all six consecutive triple patterns

## Finding
For every integer \(n\ge3\), let \(\Pi\) be uniformly distributed on the symmetric group \(S_n\). Let \(C\) denote the number of cycles, including one-cycles, in the disjoint-cycle decomposition of \(\Pi\). For each \(p\in S_3\), let \(N_p\) count indices \(1\le i\le n-2\) for which the triple \((\Pi(i),\Pi(i+1),\Pi(i+2))\) has relative order \(p\). In the fixed order \((123,132,213,231,312,321)\), the **complete mixed covariance row** is
\[
\left(\operatorname{Cov}(C,N_p)\right)_{p\in S_3}
=\frac{(3n-2,\;3n-8,\;3n-8,\;4-3n,\;4-3n,\;10-3n)}{6n(n-1)}.
\]
For every \(n\ge4\), the first three entries are strictly positive and the last three strictly negative. At \(n=3\), the last entry is instead positive. Of particular interest, the two oriented peak types \(132\) and \(231\) satisfy
\[
\operatorname{Cov}(C,N_{132}-N_{231})=\frac{n-2}{n(n-1)},\qquad
\operatorname{Cov}(C,N_{132}+N_{231})=-\frac{2}{3n(n-1)}.
\]
The corresponding two orientations of a valley, \(213\) and \(312\), obey exactly the same pair of identities. Thus the **orientation contrast has order \(n^{-1}\)** but the covariance for the total peak or valley count has order \(n^{-2}\) because of cancellation.

## Assumptions and scope
The sample is a uniform *one-line* permutation; the cycles counted by \(C\) are cycles of the bijection, not consecutive circular patterns. All inequalities and equalities hold for integers in their stated ranges, with no asymptotic hypothesis. A relative-order pattern is obtained by replacing a triple of distinct values by its ranks \(1,2,3\). The six consecutive-pattern counts sum deterministically to \(n-2\), consistent with the zero sum of the displayed covariance row.

## Proof
**1. Uniform completion of prescribed images.** Fix \(t\in\{1,\ldots,n-2\}\) and distinct images \(u,v,w\in\{1,\ldots,n\}\) for the three domain points \(t,t+1,t+2\). This directed partial injection decomposes into directed paths (isolated vertices allowed) and already closed directed cycles. Denote its number of closed cycles by \(Z(t;u,v,w)\). There are exactly \(m=n-3\) path components: adding each of the three prescribed edges either consumes one path or closes one cycle, and in either case reduces the number of path components by one. The remaining free bijection connects the path tails to path heads and is a uniform permutation of these \(m\) paths. Consequently, writing \(H_m=\sum_{j=1}^m j^{-1}\) and \(H_0=0\),
\[
\mathbb E[C\mid \Pi(t)=u,\Pi(t+1)=v,\Pi(t+2)=w]=Z(t;u,v,w)+H_{n-3}.
\]
This includes \(n=3\), for which no paths remain. The unconditional mean is \(\mathbb E C=H_n\). Each ordered distinct image triple has probability \(1/[n(n-1)(n-2)]\), and each pattern occurs at any specified position with probability \(1/6\).

**2. Exact closed-cycle contributions.** Put \(S_p=\sum_{t=1}^{n-2}\sum_{(u,v,w):\operatorname{pat}(u,v,w)=p}Z(t;u,v,w)\). Split \(S_p=F_p+B_p+T_p\) by closed-cycle lengths one, two, and three. In the order \((123,132,213,231,312,321)\), elementary summation gives the following complete tables:
\[
\begin{aligned}
(F_p)_p&=\tfrac{n-2}{2}(n(n-1),\;n^2-2n-1,\;n^2-2n-1,\;(n-3)(n-1),\;(n-3)(n-1),\;n^2-5n+8),\\
(B_p)_p&=(0,\;\tfrac{(n-2)(n-1)}2,\;\tfrac{(n-2)(n-1)}2,\;\tfrac{(n-3)(n-2)}2,\;\tfrac{(n-3)(n-2)}2,\;(n-2)^2),\\
(T_p)_p&=(0,0,0,n-2,n-2,0).
\end{aligned}
\]
For reproducibility, here are explicit ways to obtain the entries, not just an unproved table. For a rank pattern \(p=(r_0,r_1,r_2)\), the number of ordered image triples of type \(p\) making \(x=t+a\) a fixed point equals
\[
\binom{x-1}{r_a-1}\binom{n-x}{3-r_a},\qquad a\in\{0,1,2\},
\]
with binomial coefficients interpreted as zero outside their ordinary ranges. Summing this expression over \(a=0,1,2\) and \(t=1,\dots,n-2\), using \(\sum t\) and \(\sum t^2\), yields \(F_p\). For two-cycles there are three possible pairs of domain points: between \(t,t+1\) the counts by pattern are \(n-t-1\) for \(213\) and \(t-1\) for \(321\); between \(t,t+2\) they are \(n-t-2\) for \(231\), \(t-1\) for \(312\), and \(1\) for \(321\); between \(t+1,t+2\) they are \(t\) for \(132\) and \(n-t-2\) for \(321\). Sum each across \(t\). A prescribed three-cycle is exactly one of the image assignments \((t+1,t+2,t)\) and \((t+2,t,t+1)\), producing respectively patterns \(231\) and \(312\). This proves \(B_p,T_p\), including all boundary cases. A triple assignment containing multiple distinct closed cycles contributes to each of the appropriate tables: the decomposition is additive, so nothing is overcounted.

Adding the three tables gives
\[
(S_p)_p=\tfrac{n-2}{2}\bigl(n(n-1),\;(n-2)(n+1),\;(n-2)(n+1),\;(n-2)(n-1),\;(n-2)(n-1),\;n^2-3n+4\bigr).
\]

**3. Compute covariance.** Conditioning and then averaging yields
\[
\mathbb E[CN_p]=\frac{n-2}{6}H_{n-3}+\frac{S_p}{n(n-1)(n-2)}.
\]
Subtract \(\mathbb E C\,\mathbb E N_p=H_n(n-2)/6\). Since \(H_n-H_{n-3}=1/n+1/(n-1)+1/(n-2)\), we obtain
\[
\operatorname{Cov}(C,N_p)=\frac{S_p}{n(n-1)(n-2)}-\frac{n-2}{6}\left(\frac1n+\frac1{n-1}+\frac1{n-2}\right).
\]
Inserting the six evaluated polynomials and canceling gives exactly the covariance row in the finding. Subtraction/addition of the oriented peak and valley entries proves the contrast and cancellation statements. The sign assertions follow directly from the six numerators and the positive denominator for \(n\ge3\). This completes the proof.

## Verification
The standalone included `verify.py` uses only the Python standard library. It independently enumerates all \(409{,}110\) permutations of orders \(3\) through \(9\), computes cycle numbers by following permutation orbits and consecutive triple ranks directly, and checks the six exact rational covariances. Independently, it enumerates every injection of three consecutive domain points for these orders, counts prescribed closed cycles, and checks the three six-entry polynomial tables. Further exact-rational algebraic substitutions are tested for orders \(10\) through \(30\). Running `python verify.py` passed **294 exact rational assertions**; these computations validate instances and the table, while the displayed universal argument is the proof for all \(n\).

## Relationship to prior work
Fu and Li (arXiv:1809.07465, first public September 20, 2018) explicitly distinguish the two orientations of peaks and establish distributions of consecutive-pattern counts; the inspected full text does not mark permutations by their disjoint-cycle number. Gessel and Zhuang (arXiv:2001.00654, first public January 2, 2020) obtain generating functions involving cycle type jointly with the descent and peak numbers. Their cycle–peak framework can cover the covariance with the *sum* of orientations. The present finding is therefore deliberately formulated as the **six-pattern mixed covariance vector and its orientation contrast**; it does not claim the aggregate peak covariance as a new standalone fact. Cycle-type/peak enumeration based only on the descent set does not resolve patterns \(132\) and \(231\) separately, because both have the same ascent–descent signature. Jimmy He's arXiv:2005.09802 supplies additional probabilistic context for dependence between permutation statistics but not the stated mixed vector. A prior public mathematical record gives cycle-count covariance with each inversion indicator at a prescribed pair of positions, which is distinct from the nonlinear three-value pattern statistic.

## Limitations
The theorem applies to uniform permutations, consecutive windows of length three, and second mixed moments with the number of disjoint cycles. It does not establish higher moments, joint limiting laws, or a general result for all pattern lengths. Published general cycle-type/descent generating-function methods may yield some consequences implicitly; the precise historical originality of the oriented mixed vector remains subject to independent literature review. The exact results and the conditional-completion identity require no unverified computational hypothesis.

## References
1. A. M. Fu and F. Z. K. Li, *Joint Distributions of Permutation Statistics and the Parabolic Cylinder Functions*, arXiv:1809.07465 (first public 2018-09-20). https://arxiv.org/abs/1809.07465
2. I. M. Gessel and Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654 (first public 2020-01-02). https://arxiv.org/abs/2001.00654
3. J. He, *A central limit theorem for descents of a Mallows permutation and its inverse*, arXiv:2005.09802 (first public 2020-05-20). https://arxiv.org/abs/2005.09802
