# The logarithmic moment is the sharp universal threshold for sublinear age of information
## Finding

Let \((\tau_n)_{n\ge0}\) be a nonnegative integer-valued age-of-information process. Assume that there is a finite constant \(\kappa\) such that
\[
\tau_{n+1}\le \tau_n+\kappa
\]
almost surely for every \(n\), and that all \(\tau_n\) are stochastically dominated by one nonnegative random variable \(T\):
\[
\Pr(\tau_n\ge t)\le \Pr(T\ge t)
\]
for every \(n\) and every \(t\ge0\). If
\[
\mathbb E\log(1+T)<\infty,
\]
then
\[
\frac{\tau_n}{n}\longrightarrow0
\qquad\text{almost surely.}
\]

This logarithmic moment condition is sharp as a universal condition on the common dominating law. If
\[
\mathbb E\log(1+T)=\infty,
\]
then there exists a unit-growth age-of-information process \((\tau_n)\), with \(\tau_{n+1}\le\tau_n+1\) and with every \(\tau_n\) stochastically dominated by the same \(T\), such that
\[
\limsup_{n\to\infty}\frac{\tau_n}{n}\ge\frac12
\qquad\text{almost surely.}
\]

For harmonic stochastic-approximation steps, sublinear age also yields
\[
\sum_{m=n-\tau_n}^{n-1}\frac1{m+1}\longrightarrow0
\qquad\text{almost surely.}
\]
Thus the positive-power moment hypothesis used in the delay-growth lemma of Redder, Ramaswamy and Karl can be weakened, for that delay-control mechanism, to the finite logarithmic moment condition together with the bounded-growth property already built into their age-of-information model.

## Assumptions and scope

The theorem is distribution-free apart from two structural assumptions: a common stochastic dominator and bounded upward age increments. No independence between the variables \(\tau_n\) is needed for the sufficient direction. The converse is existential: for every dominating law with infinite logarithmic moment, it constructs one admissible age process for which sublinear growth fails.

The stochastic-approximation consequence concerns the harmonic delay window used in the cited distributed stochastic-approximation analysis. It does not claim finite-time rates, optimality for step-size schedules slower than harmonic, or convergence under removal of the other hypotheses in that analysis.

A finite logarithmic moment is strictly weaker than every positive power moment. For example, if \(Z\) is exponential with mean one and
\[
T=\lfloor \exp(Z^2)\rfloor-1,
\]
then
\[
\mathbb E\log(1+T)\le \mathbb E Z^2=2,
\]
whereas
\[
\mathbb E T^p=\infty
\]
for every \(p>0\).

## Proof

Set
\[
Y=\log(1+T).
\]
Fix \(a>1\) and let \(n_k=\lceil a^k\rceil\). For any \(\varepsilon>0\), stochastic domination gives
\[
\Pr(\tau_{n_k}\ge \varepsilon n_k)
\le
\Pr\!\left(
Y\ge \log(1+\varepsilon n_k)
\right).
\]
For all sufficiently large \(k\),
\[
\log(1+\varepsilon n_k)\ge \frac{\log a}{2}k.
\]
Because \(\mathbb E Y<\infty\), monotonicity of the tail and the tail-integral formula imply, for every \(c>0\),
\[
\sum_{k=1}^{\infty}\Pr(Y\ge ck)<\infty.
\]
The first Borel--Cantelli lemma therefore gives
\[
\frac{\tau_{n_k}}{n_k}\longrightarrow0
\qquad\text{almost surely.}
\]
Using a countable sequence of rational \(\varepsilon>0\) makes this one probability-one statement.

For \(n_k\le n<n_{k+1}\), bounded upward growth gives
\[
\tau_n
\le
\tau_{n_k}+\kappa(n-n_k)
\le
\tau_{n_k}+\kappa(n_{k+1}-n_k),
\]
hence
\[
\limsup_{n\to\infty}\frac{\tau_n}{n}
\le
\kappa(a-1)
\qquad\text{almost surely.}
\]
Apply this simultaneously to the countable sequence \(a_j=1+1/j\) and let \(j\to\infty\). This proves \(\tau_n/n\to0\) almost surely.

For sharpness, suppose \(\mathbb E\log(1+T)=\infty\) and define
\[
q_k=\Pr(T\ge 2^k-1).
\]
The tail-sum formula applied to \(\log_2(1+T)\) gives
\[
\sum_{k=1}^{\infty}q_k=\infty.
\]
Let \(B_k\) be independent Bernoulli random variables with \(\Pr(B_k=1)=q_k\). On the dyadic block
\[
2^k\le n<2^{k+1},
\]
define
\[
\tau_n=B_k(n-2^k).
\]
Within a block the age either stays zero or increases by one at each step; at a block boundary it may drop. Thus
\[
\tau_{n+1}\le\tau_n+1.
\]
Moreover the associated information timestamp \(n-\tau_n\) is nondecreasing: it advances normally on an inactive block and is constant on an active block.

If \(n\) belongs to block \(k\) and \(0<t\le n-2^k\), then
\[
\Pr(\tau_n\ge t)=q_k
=
\Pr(T\ge 2^k-1)
\le
\Pr(T\ge t),
\]
while for larger \(t\) the left side is zero. Hence every \(\tau_n\) is stochastically dominated by \(T\). Since the \(B_k\) are independent and \(\sum_k q_k=\infty\), the second Borel--Cantelli lemma gives infinitely many active blocks almost surely. At the last time of each such block,
\[
\frac{\tau_{2^{k+1}-1}}{2^{k+1}-1}
=
\frac{2^k-1}{2^{k+1}-1}
\longrightarrow\frac12.
\]
This proves the sharp converse.

Finally, if \(\tau_n/n\to0\), then eventually \(\tau_n<n/2\), and
\[
0\le
\sum_{m=n-\tau_n}^{n-1}\frac1{m+1}
\le
\frac1{n-\tau_n+1}
+
\log\!\left(\frac{n}{n-\tau_n}\right)
\longrightarrow0.
\]
This is exactly the vanishing harmonic delay-window property needed to make the delayed-drift discrepancy disappear in the cited stochastic-approximation proof.

## Verification

The sufficient proof uses only stochastic domination, the tail-sum criterion for integrability, the first Borel--Cantelli lemma, and bounded upward age growth. No independence is used there.

For the converse, stochastic domination was checked pointwise on every dyadic block. The constructed timestamp \(n-\tau_n\) is nondecreasing and the age increases by at most one per time step, so the construction satisfies the standard age-of-information process constraints used in the predecessor analysis. Independence is introduced only for the block indicators \(B_k\), permitting the second Borel--Cantelli lemma.

The strict separation from positive-power moments follows from the explicit exponential example in the scope section: for sufficiently large \(z\), \(\lfloor e^{z^2}\rfloor-1\) is bounded below by a positive constant times \(e^{z^2}\), so its \(p\)-th moment dominates an integral proportional to
\[
\int^\infty \exp(pz^2-z)\,dz,
\]
which diverges for every \(p>0\).

## Relationship to prior work

Redder, Ramaswamy and Karl assume a common dominating delay variable having a finite \(p\)-th moment for some \(p\in(0,1]\). Their delay lemma proves \(\tau_n/n\to0\) almost surely, and their subsequent harmonic-step argument uses the equivalent vanishing accumulated step size over the stale window. Their proof also records the bounded one-step growth of age-of-information processes. The result above replaces the positive-power condition in this delay-growth step by the exact universal logarithmic threshold.

The 2023 predecessor by Ramaswamy, Redder and Quevedo likewise assumes a common dominator with a finite positive moment and proves sublinear delays before deriving the vanishing delay window. The 2024 dissertation treatment inspected for this comparison retains the same finite-positive-moment route. None of these inspected statements gives the finite-logarithmic-moment threshold or its converse construction.

The earlier 2022 time-varying-network paper studies a different eventual-delivery communication assumption. Its accessible published statement does not imply the common-dominator logarithmic threshold proved here.

## Limitations

The converse establishes sharpness of the logarithmic moment as a universal sufficient condition under common stochastic domination and bounded age growth. It does not say that every particular age process with an infinite logarithmic-moment dominator must have linear spikes.

The stochastic-approximation implication is confined to the delay-control part of the harmonic-step proof. Other assumptions in the cited stability and convergence theorems remain in force. No claim is made about a sharp moment threshold for every possible step-size sequence or every asynchronous algorithm.

A broad probability result under different terminology could conceivably subsume the standalone age-process lemma; the focused literature comparisons reported here did not reveal such a stronger statement.

## References

1. A. Redder, A. Ramaswamy, H. Karl, *Distributed Stochastic Approximation Algorithms and Heavy-Tailed Age of Information*, arXiv:2609.27499v1, 2026.
2. A. Ramaswamy, A. Redder, D. E. Quevedo, *Stability and Convergence of Distributed Stochastic Approximations with large Unbounded Stochastic Information Delays*, arXiv:2305.07091v1, 2023.
3. A. Redder, *Distributed Asynchronous Stochastic Approximation Algorithms with unbounded Stochastic Information Delays – Theory and Applications*, dissertation, DOI 10.17619/UNIPB/1-1997, 2024.
4. A. Ramaswamy, A. Redder, D. E. Quevedo, *Optimization Over Time-Varying Networks and Unbounded Information Delays*, IEEE Transactions on Automatic Control 67(8), DOI 10.1109/TAC.2021.3108492, 2022.
