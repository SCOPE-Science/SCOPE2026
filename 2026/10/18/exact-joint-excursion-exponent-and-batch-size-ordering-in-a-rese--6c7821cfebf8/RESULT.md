# Exact joint-excursion exponent and batch-size ordering in a resetting Brownian gas

## Finding

Consider the uniform batch-reset Brownian gas introduced in [1]. Fix integers \(N\ge2\), \(1\le m\le N\), \(1\le k\le N\) and constants \(D,r>0\). Each of \(N\) labelled particles diffuses on the line with variance \(2Dt\) over a free interval; at each event of an independent rate-\(r\) Poisson process, a uniformly chosen size-\(m\) subset is reset to the origin. In its stationary state select any \(k\) distinct labels and set

\[
q_j=1-\frac{\binom{N-j}{m}}{\binom Nm},\qquad 1\le j\le k,
\]

where a binomial coefficient with upper argument smaller than its lower argument is zero. The probability of a simultaneous large excursion obeys the **exact logarithmic tail law**

\[
\boxed{\displaystyle
\lim_{z\to\infty}-\frac1z\log\mathbb P\bigl(|X_1|\ge z,\ldots,|X_k|\ge z\bigr)
=\kappa_k:=\sqrt{\frac{rkq_k}{D}}.}
\]

For \(k\ge2\), the exponent relative to the observed one-particle exponent \(\kappa_1=\sqrt{rm/(ND)}\) is strictly **decreasing** with integer batch size \(m\):

\[
\boxed{\sqrt{k}\le\frac{\kappa_k}{\kappa_1}=\sqrt{\frac{kq_k}{q_1}}\le k,}
\]

with upper equality only for \(m=1\) and lower equality only for \(m=N\). Hence the normalized many-particle rare-excursion rate orders all batch sizes even in regimes where the stationary *two-point covariance amplitude* is nonmonotone [1].

A structural ingredient is another sharp statement, for the stationary ages \(A_1,\ldots,A_k\) since each tagged particle's last reset:

\[
\boxed{\mathbb E\exp\!\left(\theta\sum_{i=1}^k A_i\right)<\infty
\quad\Longleftrightarrow\quad \theta<\frac{rq_k}{k},\qquad \theta\in\mathbb R.}
\]

This is the exact moment boundary used in the same joint-excursion theorem, not a separate unrelated claim.

## Assumptions and scope

All limiting statements are for fixed finite \(N,m,k,D,r\), with only the spatial threshold \(z\) tending to infinity. Brownian motions of different labels are independent of each other and of the marked Poisson reset process. Each event independently resamples a uniform size-\(m\) subset without replacement. The stationary state is constructed from resets in the infinite past, which is valid because every label has positive reset intensity \(rq_1=rm/N\). There are no direct particle interactions, walls, drifts or confining potentials. The diffusion convention is generator \(D\partial_x^2\). Absolute excursions are simultaneous observations at a single stationary time; they are not first-passage events.

## Proof

**1. Stationary conditional Gaussian representation.** Construct a marked Poisson point process of total intensity \(r\) on past time, with independent uniform marks \(S\subset\{1,\ldots,N\}\) of cardinality \(m\). For each labelled particle \(i\), let \(A_i\) be the time elapsed since the most recent marked event with \(i\in S\). The probability that any fixed \(j\) labels are avoided by one mark is \(\binom{N-j}{m}/\binom Nm\), so \(q_j\) above is the mark-hit probability. Every \(A_i\) is finite almost surely. Conditional on the entire marked reset history, the free Brownian increments after the individual most recent resets are independent; consequently

\[
(X_1,\ldots,X_k)\mid(A_1,\ldots,A_k)
\ \overset{\mathrm d}=\ \bigl(\sqrt{2DA_1}\,Z_1,\ldots,\sqrt{2DA_k}\,Z_k\bigr),
\]

where the \(Z_i\) are independent standard normal random variables independent of the ages.

**2. The joint-age survival identity.** For \(J\subseteq\{1,\ldots,k\}\) of cardinality \(j\) and arbitrary \(t_i\ge0\), let

\[
\phi_J(t)=\mathbb E_S\left[\max\bigl(\{t_i:i\in S\cap J\}\cup\{0\}\bigr)\right].
\]

A marked event at backward age \(u\) violates at least one condition \(A_i>t_i\), \(i\in J\), exactly when it intersects some \(i\in J\) with \(u\le t_i\). The Poisson void formula therefore gives **exactly**

\[
\mathbb P(A_i>t_i\ \text{for all }i\in J)=e^{-r\phi_J(t)}.
\]

The function \(\phi_J\) is convex (an expectation of maxima of coordinate-affine functions), invariant under permutations of the \(j\) labels, and positively homogeneous. Averaging \(t\) over its \(j!\) permutations and applying convexity shows

\[
\phi_J(t)\ge \phi_J(\bar t,\ldots,\bar t)
=q_j\bar t=\frac{q_j}{j}\sum_{i\in J}t_i.
\]

In fact \(q_j-q_{j-1}\) is the probability a mark hits the \(j\)-th new label but avoids the first \(j-1\); explicitly,

\[
q_j-q_{j-1}=\frac{m}{N}\,
\frac{(N-m)_{\underline{j-1}}}{(N-1)_{\underline{j-1}}},\qquad q_0=0.
\]

The falling-factorial quotient decreases with \(j\), so \(q_j/j\) is nonincreasing. In particular, \(rq_j/j\ge c:=rq_k/k\) for \(1\le j\le k\).

**3. Sharp exponential-moment boundary for age sums.** Write \(S_k=\sum_{i=1}^k A_i\). For any \(0<\theta<c\), expand the identity \(e^{\theta A_i}=1+\theta\int_0^{A_i}e^{\theta t}\,dt\) in the product over labels, apply Tonelli's theorem, and then apply the preceding upper-orthant estimate. The term indexed by a subset \(J\) of cardinality \(j\) is at most \(\theta^j/(c-\theta)^j\). Thus

\[
\mathbb E e^{\theta S_k}
\le\sum_{j=0}^k\binom kj\left(\frac{\theta}{c-\theta}\right)^j
=\left(\frac{c}{c-\theta}\right)^k<\infty.
\]

The same conclusion is immediate for \(\theta\le0\). Conversely, for every \(s\ge0\), demanding that all tagged ages exceed \(s/k\) means no mark intersects any tagged label during the latest \(s/k\) units of time, an event of probability \(e^{-rq_k s/k}=e^{-cs}\). Hence

\[
\mathbb P(S_k>s)\ge e^{-cs}.
\]

The positive-variable tail integral \(\mathbb E e^{\theta S_k}=1+\theta\int_0^\infty e^{\theta s}\mathbb P(S_k>s)\,ds\) diverges for all \(\theta\ge c\), including equality. This proves the exact moment domain.

**4. Upper excursion exponent.** Gaussian Chernoff bounds, followed by conditional independence and the harmonic-mean inequality, yield for \(z>0\)

\[
\begin{aligned}
\mathbb P(|X_i|\ge z,\ 1\le i\le k)
&\le 2^k\mathbb E\exp\left(-\frac{z^2}{4D}\sum_i\frac1{A_i}\right)\\
&\le 2^k\mathbb E\exp\left(-\frac{k^2z^2}{4DS_k}\right).
\end{aligned}
\]

For every \(0<\theta<c\), the arithmetic-geometric mean inequality supplies

\[
\frac{k^2z^2}{4DS_k}+\theta S_k\ge k z\sqrt{\theta/D}.
\]

The finite exponential moment from Step 3 therefore gives

\[
\mathbb P(|X_i|\ge z\ \forall i)
\le 2^k\mathbb E e^{\theta S_k}\,e^{-kz\sqrt{\theta/D}}.
\]

First take \(z\to\infty\), then \(\theta\uparrow c\). This proves that the logarithmic decay rate is **at least** \(k\sqrt{c/D}=\sqrt{rkq_k/D}\).

**5. Matching lower excursion exponent.** For any \(a>0\) and \(z>0\), the event \(A_i\ge az\) for all tagged labels has exact probability \(e^{-rq_kaz}\). On that event each conditional Gaussian tail is at least the one with age \(az\), giving

\[
\mathbb P(|X_i|\ge z\ \forall i)
\ge e^{-rq_kaz}\left[\operatorname{erfc}\left(\sqrt{\frac{z}{4Da}}\right)\right]^k.
\]

Since \(\log\operatorname{erfc}(\sqrt{z/(4Da)})=-z/(4Da)+O(\log z)\), the logarithmic rate is **at most** \(rq_ka+k/(4Da)\). Minimizing over \(a>0\), at \(a=\sqrt{k/(4Drq_k)}\), gives \(\sqrt{rkq_k/D}\), matching Step 4.

**6. Strict ordering of batch sizes.** Telescoping the no-hit probabilities gives

\[
\frac{q_k}{q_1}=\sum_{j=0}^{k-1}
\frac{(N-m)_{\underline j}}{(N-1)_{\underline j}},
\qquad q_1=\frac mN,
\]

with a zero numerator when the falling factorial reaches a zero factor. For \(k\ge2\), the \(j=1\) summand is strictly decreasing for each successive integer \(m\in\{1,\ldots,N\}\), and every other summand is nonincreasing. Hence \(q_k/q_1\), and thus \(\kappa_k/\kappa_1\), decreases strictly with \(m\). At \(m=1\), \(q_k=k/N\) and the ratio is \(k\); at \(m=N\), \(q_k=q_1=1\) and it is \(\sqrt{k}\). This proves all claims.

## Verification

The standalone script `verify.py` computes \(q_j\) by two independent combinatorial formulas and checks strict batch-size ordering over \(1014\) finite parameter triples. For two tagged labels it independently integrates the stationary law using three thinned shock processes: shocks resetting both labels have rate \(a=rm(m-1)/(N(N-1))\), and shocks resetting exactly one specified label each have rate \(b=rm(N-m)/(N(N-1))\). Writing independent \(U_1,U_2\sim\operatorname{Exp}(b)\) and \(C\sim\operatorname{Exp}(a)\), the tagged ages are \(\min(U_1,C)\) and \(\min(U_2,C)\), with the appropriate infinite-clock convention when a rate is zero. This gives a one-dimensional quadrature for the joint excursion probability, wholly independent of Steps 3–5. Six sample choices and three thresholds per choice agree with the stated large-threshold exponents. A direct integration of the two-age survival law also yields, writing \(\lambda_1=rq_1\), \(\lambda_2=rq_2\),

\[
\mathbb E e^{\theta(A_1+A_2)}
=\frac{\lambda_1\lambda_2+\theta(\lambda_2-2\lambda_1)}
{(\lambda_1-\theta)(\lambda_2-2\theta)},\qquad \theta<\lambda_2/2,
\]

consistent with the general sharp boundary. These numerical and algebraic checks do not replace the unrestricted analytic argument.

## Relationship to prior work

De Mauro, Majumdar and Schehr [1] introduced uniform batch resetting and established an exact recursive hierarchy of positional marginals and second-order stationary and temporal correlation formulas, including nonmonotonicity of a covariance measure across batch sizes. Their formulas make the present question natural but do not state the joint large-threshold exponent, the sharp moment domain for the tagged reset ages, or the strict ordering of normalized multi-particle rare-excursion rates. The full original manuscript and its supplemental treatment of the one-, two- and \(N\)-point equations, large-distance pair-density behavior and spectral form factor were compared. Its broad Fourier recursion is acknowledged: the present theorem is an asymptotic extraction requiring an additional age-domain convexity argument, not a claim that the earlier joint law was unavailable.

De Mauro, Biroli, Majumdar and Schehr [2] derive complete positional mixtures under *fully simultaneous* reset events, including the \(m=N\) endpoint of this theorem, but do not analyze partially synchronous uniform \(m\)-batch events. Vilk, Assaf and Meerson [3] treat independent resets and reset-to-origin of the farthest particle, not the intermediate uniformly sampled batches. The independent \(m=1\) and fully simultaneous \(m=N\) endpoint rates are consistent with those prior settings and are not claimed as new individually. The distinguishing result here is the exact general \(1<m<N\) law and its all-batch monotonic comparison.

## Limitations

The result determines the exact **exponential logarithmic rate**, not the pre-exponential constant, polynomial correction, or a uniform bound as \(k\) or \(N\) grows. No claim is made about hitting times, pair-density tails along different rays, or arbitrary non-Poissonian reset-time laws. The overlapping reset-age representation and Poisson-void formula are standard tools; novelty is limited to their stated sharp combination for this batch-reset observable. Although extensive targeted comparisons found no explicit covering theorem, it remains possible that a general multivariate shock/Gaussian-mixture large-deviation result subsumes the finding implicitly.

## References

1. G. de Mauro, S. N. Majumdar and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077, first submitted 27 January 2026; in particular main results and Supplemental Sections S1–S3 and S9. https://arxiv.org/abs/2601.20077
2. G. de Mauro, M. Biroli, S. N. Majumdar and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658, first submitted 8 September 2025. https://arxiv.org/abs/2509.06658
3. O. Vilk, M. Assaf and B. Meerson, *Fluctuations and first-passage properties of systems of Brownian particles with reset*, arXiv:2205.10273, first submitted 20 May 2022. https://arxiv.org/abs/2205.10273
