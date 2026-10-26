# A centered parabolic covariance law for fixed points and inversions under Ewens sampling

## Finding
Let \(\pi\) follow the Ewens distribution on permutations of \([n]\) with real parameter \(\theta>0\). For every integer \(n\ge3\) and each position \(i\in[n]\), set \(B_i=\mathbf1\{\pi(i)=i\}\) and let \(I\) denote the total number of inversions in the one-line permutation. Define
\[
R_{n,\theta}^{2}=\frac{(1-\theta)(n-1)\big[(n-3)(2n-1)+3(n-1)\theta\big]}{12(\theta+n-3)(\theta+n-1)}.
\]
Then the exact finite-size formula is
\[
\boxed{\operatorname{Cov}(B_i,I)=\frac{2\theta}{(\theta+n-1)(\theta+n-2)}\left[R_{n,\theta}^{2}-\left(i-\frac{n+1}{2}\right)^2\right].}
\]
When \(\theta>1\) all covariances are strictly negative. For \(\theta=1\),
\[
\operatorname{Cov}(B_i,I)=-\frac{(2i-n-1)^2}{2n(n-1)},
\]
which is zero exactly at the central position of odd-length permutations. When \(0<\theta<1\), the covariance is positive, zero, or negative according as \(\left|i-(n+1)/2\right|\) is smaller than, equal to, or greater than \(R_{n,\theta}>0\). Thus all odd sizes have a positively correlated central fixed point, whereas both endpoints remain negatively correlated. Even sizes can have an empty positive window, depending on \(\theta\).

For fixed \(0<\theta<1\), the positive window has asymptotic half-width
\[
\frac{R_{n,\theta}}{\sqrt n}\longrightarrow\sqrt{\frac{1-\theta}{6}}.
\]
More precisely, for any sequence of valid indices \(i_n\) such that \(\big(i_n-(n+1)/2\big)/\sqrt n\to z\in\mathbb R\),
\[
\boxed{n\operatorname{Cov}(B_{i_n},I)\longrightarrow 2\theta\left[\frac{1-\theta}{6}-z^2\right].}
\]

## Assumptions and scope
The Ewens measure assigns to each \(\pi\in S_n\) probability \(\theta^{c(\pi)}/\prod_{j=0}^{n-1}(\theta+j)\), where \(c(\pi)\) counts disjoint cycles. An inversion is a pair of positions \(a<b\) with \(\pi(a)>\pi(b)\). The claimed identities hold for all real \(\theta>0\), all integers \(n\ge3\), and all positions \(1\le i\le n\); there is no asymptotic hypothesis for the exact formula. Empty intervals of integer indices are allowed.

## Proof
**1. Deletion and the conditional law.** For every specified \(i\), Ewens cycle weights factor when \(i\) is a singleton cycle, giving
\[
\Pr(B_i=1)=\frac{\theta}{\theta+n-1}.
\]
Conditionally on \(B_i=1\), deleting the singleton \(i\) and order-preservingly relabeling the other \(n-1\) values gives an Ewens-\(\theta\) permutation of size \(n-1\). For such a permutation on \(m\) labels the one-coordinate marginal is \(\Pr(\pi(j)=j)=\theta/(\theta+m-1)\) and \(\Pr(\pi(j)=k)=1/(\theta+m-1)\) for distinct \(j,k\); these follow by deleting a specified one-cycle and by conjugation invariance plus normalization.

**2. Exact conditional inversion mean.** Inversions involving two labels other than \(i\) are preserved on deleting \(i\). Under \(B_i=1\), the missing inversions are precisely \((j,i)\) for \(j<i\) with \(\pi(j)>i\), and \((i,j)\) for \(j>i\) with \(\pi(j)<i\). By the preceding marginal each of the \(i-1\) earlier labels has probability \((n-i)/(\theta+n-2)\) to exceed \(i\), and each of the \(n-i\) later labels has probability \((i-1)/(\theta+n-2)\) to lie below \(i\). Hence, with \(M_m(\theta)=\mathbb E_\theta I_m\),
\[
\mathbb E[I\mid B_i=1]=M_{n-1}(\theta)+\frac{2(i-1)(n-i)}{\theta+n-2}.
\]

**3. Substitution of the known mean.** The exact unconditional Ewens inversion mean (Pinsky--Schickentanz, Theorem 1(b), cited below) is
\[
M_m(\theta)=\frac{(\theta-1)m(m-1)(2m-1)/6+m^2(m-1)^2/4}{(\theta+m-1)(\theta+m-2)},\qquad m\ge2.
\]
For completeness, it is equivalently characterized by \(M_1(\theta)=0\) and the recurrence
\[
M_m(\theta)=\frac{\theta+m-3}{\theta+m-1}M_{m-1}(\theta)+\frac{(m-1)^2}{\theta+m-1},\qquad m\ge2,
\]
where the recurrence at \(m=2\) takes its evident finite interpretation \(M_1=0\). Direct algebra verifies the displayed closed form and recurrence for \(m\ge3\), and the \(m=2\) case directly. In particular, no new claim is made for this known scalar mean.

Combining Steps 1--2 gives
\[
\operatorname{Cov}(B_i,I)=\frac{\theta}{\theta+n-1}\left(M_{n-1}(\theta)-M_n(\theta)+\frac{2(i-1)(n-i)}{\theta+n-2}\right).
\]
Substituting the preceding rational mean and using
\[
(i-1)(n-i)=\frac{(n-1)^2}{4}-\left(i-\frac{n+1}{2}\right)^2
\]
reduces the constant term to the specified \(R_{n,\theta}^2\) and yields the boxed identity. Every denominator is positive for \(n\ge3\) and \(\theta>0\).

**4. Phase classification and limit.** The bracket \((n-3)(2n-1)+3(n-1)\theta\) is strictly positive. Therefore \(R_{n,\theta}^2\) has the sign of \(1-\theta\), and the positivity/zero/negativity statements follow from the squared centered-position form. When \(\theta=1\), the squared radius is zero, yielding the displayed negative square. Both endpoints have squared distance \((n-1)^2/4\), larger than \(R_{n,\theta}^2\) for \(0<\theta<1\): indeed from Step 2, at either endpoint the conditional inversion mean is \(M_{n-1}\), and the recurrence shows \(M_n>M_{n-1}\) (also directly, adding a new label creates inversions with positive probability). Finally, for fixed \(\theta>0\) expansion of the rational radius gives \(R_{n,\theta}^2/n\to(1-\theta)/6\); inserting the assumed index scaling into the exact covariance gives the limit.

## Verification
The accompanying standalone `verify.py` enumerates every permutation for \(3\le n\le8\) using exact rational Ewens weights at five positive concentrations. It checks the scalar mean, individual fixed-point probabilities, conditional regression covariance, and centered parabola independently, then checks the rational identities and sign regimes through \(n=150\) and the radius limit numerically at larger finite sizes. The exact theorem and limiting assertions rely on the preceding proof, not on finite enumeration. Execute `python verify.py` with Python 3 standard library.

## Relationship to prior work
The 2018 preprint by Özdemir (later published 2023, primary MSC 60C05) studies random walks driven by Ewens permutations and provides a qualifying probabilistic foundation rather than an inversion-covariance result. Pinsky--Schickentanz (2025, Theorem 1(b)) established the unconditional inversion mean quoted in Step 3, and its Proposition 10 conditions on the **total number** of fixed points, not the event that a **specified position** is fixed. Pinsky (2025) likewise studies the fixed-point **count** under uniform sampling. These laws do not state the position-indexed covariance parabola or its \(\sqrt n\)-width sign reversal. Other related exact work describes cycle-count/inversion dependence or fixed-point/descent dependence but does not yield this statement unchanged. The claim is not that existing results lack the algebraic ingredients; it is the finite-size position-resolved dependence classification and mesoscopic transition.

## Limitations
This work does not determine the full joint law of fixed points and inversions, claim independence at vanishing covariance, or establish a limit theorem for the inversion statistic. The scalar mean is explicitly credited. Although the most directly relevant available primary texts were inspected, historical-priority uncertainty remains for other possible equivalent formulations.

## References
1. A. Y. Özdemir, *Random walks generated by the Ewens distribution on the symmetric group*, first arXiv submission 2018-11-05, arXiv:1811.02039v1; *Algebraic Combinatorics* **6** (2023), 907–927, doi:10.5802/alco.290. (Primary MSC 60C05.)
2. R. G. Pinsky and D. T. Schickentanz, *Inversions in Random Permutations Under the Ewens Sampling Distribution With and Without a Prescribed Number of Fixed Points*, arXiv:2510.20654v2 (2025), Theorem 1 and Proposition 10.
3. R. G. Pinsky, *The inversion statistic in derangements and in other permutations with a prescribed number of fixed points*, arXiv:2505.02058v1 (2025), Theorems 1–2.
