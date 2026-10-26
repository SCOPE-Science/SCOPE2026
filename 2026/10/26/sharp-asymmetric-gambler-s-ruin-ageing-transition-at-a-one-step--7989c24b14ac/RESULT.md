# Sharp asymmetric gambler’s-ruin ageing transition at a one-step lower barrier

## Finding

Let \((S_n)_{n\ge0}\) be the biased simple random walk started at \(S_0=0\), with independent increments \(+1\) of probability \(p\in(0,1)\) and \(-1\) of probability \(q=1-p\). For each integer \(b\ge1\), let \(N_b\) be the first visit to \(\{-1,b\}\) and let \(T_b=\lceil N_b/2\rceil\). Its grouped survival function is \(s_t=\Pr(T_b>t)=\Pr(N_b>2t)\) for integers \(t\ge0\), and the hazard at an age with \(s_{t-1}>0\) is \(h_t=1-s_t/s_{t-1}\).

**Complete classification.** The hazard \((h_t)\) is nondecreasing (increasing failure rate, IFR) precisely in the following cases:

| Upper barrier \(b\) | Condition for IFR | Additional structure |
|---|---|---|
| \(1\) | Every \(p\in(0,1)\) | The lifetime is identically one. |
| \(2\) | Every \(p\in(0,1)\) | Constant hazard \(1-pq\). |
| \(3\) | \(p\ge1/2\) | Hazard increases after age one if \(p>1/2\), and is constant if \(p=1/2\). |
| \(4\) | \(p\ge(\sqrt5-1)/2\) | The hazards are strictly increasing above the boundary, constant at equality, and strictly decreasing below it. |
| \(b\ge5\) | Never | The hazard decreases strictly from age one to two. |

Thus the golden-ratio conjugate is a sharp drift threshold at upper boundary four, and the increasing-failure-rate property fails for every drift once the upper boundary is at least five.

## Assumptions and scope

The increments are independent, each taking only values \(\pm1\), and \(p\) is strictly between zero and one. Both endpoints are absorbing; the lower endpoint is exactly \(-1\) and the upper endpoint is the integer \(b\). The walk starts at zero. Absorption occurs on hitting, not only on checking every other step. Grouping the actual first-passage time through \(T_b=\lceil N_b/2\rceil\) removes observational half-period gaps without changing the physical exit rule.

The IFR requirement is \(h_{t+1}\ge h_t\) whenever both hazards are defined. Equivalently, the positive survival probabilities are log-concave: \(s_t^2\ge s_{t-1}s_{t+1}\). At finite-support endpoints the hazard is compared only on its defined support. This result does not characterize nonuniform boundaries, time-varying transition probabilities, other starting states, or other ways of grouping time.

## Proof

### Upper barriers one and two

At \(b=1\), the first step reaches an absorbing endpoint, so \(T_1=1\). At \(b=2\), the only surviving even-time state is zero. To survive another two increments from zero, the walk must make \(+1,-1\), of probability \(pq\). Therefore \(s_t=(pq)^t\), and the hazard is constantly \(1-pq\).

### Upper barrier three

At even times, conditional on nonabsorption, transient states are zero and two. Their two-step substochastic kernel, with states ordered \((0,2)\), is
\[
Q_3=\begin{pmatrix}pq&p^2\\q^2&pq\end{pmatrix}.
\]
The first row is \(p(q,p)\), and \((q,p)Q_3=2pq(q,p)\). Thus the exact survival sequence is
\[
s_0=1,\qquad s_t=p(2pq)^{t-1}\quad(t\ge1).
\]
Consequently \(h_1=1-p\), while \(h_t=1-2pq\) for every \(t\ge2\). The hazard is nondecreasing precisely when \(p\ge2pq\), equivalent to \(p\ge1/2\) because \(p>0\) and \(q=1-p\).

### Upper barrier four

The two transient even-time states remain zero and two, now with kernel
\[
Q_4=\begin{pmatrix}pq&p^2\\q^2&2pq\end{pmatrix}.
\]
For \(t\ge0\), write \(s_t=(1,0)Q_4^t(1,1)^\top\). The two characteristic roots are
\[
\lambda_+=\frac{3+\sqrt5}{2}pq,\qquad
\lambda_-=\frac{3-\sqrt5}{2}pq,
\]
which are strictly positive and distinct. Since \(s_0=1\) and \(s_1=p\), diagonalization gives
\[
s_t=A\lambda_+^t+B\lambda_-^t,\quad
A=\frac{p-\lambda_-}{\lambda_+-\lambda_-},\quad
B=\frac{\lambda_+-p}{\lambda_+-\lambda_-}.
\]
Here \(A>0\) for all \(0<p<1\), since \(\lambda_-<pq<p\). Direct multiplication yields the exact identity
\[
s_t^2-s_{t-1}s_{t+1}=-AB(\lambda_+-\lambda_-)^2
(\lambda_+\lambda_-)^{t-1},\qquad t\ge1.
\]
Every factor except \(-B\) is positive. Thus the survival sequence is log-concave for all ages exactly when \(B\le0\), i.e. \(\lambda_+\le p\). Cancelling \(p>0\) gives \(q\le2/(3+\sqrt5)=(3-\sqrt5)/2\), equivalent to
\[
p\ge\frac{\sqrt5-1}{2}.
\]
The sign is strict for all ages off this threshold. At equality \(B=0\), so \(s_t=\lambda_+^t\) and the hazard is constant.

### Every upper barrier at least five

For \(b\ge5\), an upper-barrier hit is impossible in the first four steps, and a lower-barrier hit occurs as soon as a negative step is taken from zero. The sole surviving one-step choice is \(+1\), hence \(s_1=p\). Of the length-four walks staying nonnegative, the probabilities sum to
\[
s_2=p^4+3p^3q+2p^2q^2=p^2(2-p).
\]
The first two hazards are
\[
h_1=1-p,\qquad h_2=1-p(2-p).
\]
Their difference is \(h_2-h_1=-pq<0\). Thus IFR fails already at ages one and two, for every \(p\in(0,1)\). Together with the previous cases, this completes the classification.

## Verification

The standalone script `verify_asymmetric_ifr.py` propagates the exact-rational killed-walk state vector. It tests six rational drift probabilities, upper boundaries \(1,2,3,4,5,6,9\), all declared formulas up to nine grouped epochs, the Cayley–Hamilton recurrence for \(b=4\), and the first two survival probabilities for every tested \(b\ge5\). It returned

`VERIFY_OK: 6 rational biases; b in {1,2,3,4,5,6,9}; grouped survival recurrences, b=4 determinants, and b>=5 initial IFR obstructions.`

The verifier only checks finite examples and does not prove the universal conclusion; the exact finite-state and algebraic arguments above do.

## Relationship to prior work

Ye Liang, “Parity-Skeleton First-Passage Dynamics and Optimal Intervention in Two-Sided Discrete Monitoring Systems” (arXiv:2609.13000v1, submitted 11 July 2026), proves IFR for a centered walk with *symmetric* absorbing boundaries. Its discussion explicitly identifies asymmetric barriers and preservation of IFR as a further research direction. The present result isolates the shortest lower-barrier geometry and gives the full classification in the upper barrier and drift, including failure of IFR and the golden-ratio transition.

Evans, Peköz and Righter (arXiv:2301.08328), and Geng and Markowsky (DOI 10.1080/15326349.2025.2515964), study stochastic order of exit times for *symmetric* gambler’s-ruin intervals as the bias changes; the results stated in their publicly accessible descriptions are not an asymmetric interval's full hazard classification. The former preprint's introductory statement and methods were inspected; the latter's published full text was not accessible through the searched publisher page. General finite-chain spectral formulas are methodological background but do not alone give the drift cutoffs above.

## Limitations

The precise result applies only to the lower boundary \(-1\), upper boundary \(b\), initial state zero, iid nearest-neighbor steps, and grouping \(\lceil N_b/2\rceil\). It neither classifies arbitrary asymmetric boundary pairs nor asserts universal IFRA/NBU classifications. An unlocated equivalent in broader ageing/reliability literature remains possible, despite the statement-level comparisons with the closest identified sources. No independent validation is claimed.

## References

1. Y. Liang, “Parity-Skeleton First-Passage Dynamics and Optimal Intervention in Two-Sided Discrete Monitoring Systems,” arXiv:2609.13000v1, first public posting 2026-07-11. https://arxiv.org/abs/2609.13000.
2. S. Evans, E. A. Peköz, and R. Righter, “Increasing Gambler’s Ruin duration and Brownian Motion exit times,” arXiv:2301.08328v1, 2023-01-19. https://arxiv.org/abs/2301.08328.
3. X. Geng and G. Markowsky, “Stochastic domination of exit times for random walks and Brownian motion with drift,” *Stochastic Models* 42 (2026), 51–59; published online 2025-06-14. DOI: 10.1080/15326349.2025.2515964.
