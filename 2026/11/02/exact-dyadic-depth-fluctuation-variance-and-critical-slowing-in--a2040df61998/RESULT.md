# Exact dyadic-depth fluctuation variance and critical slowing in the Pelikan random map

## Finding
For the stationary absolutely continuous Pelikan random interval map, the time integral of dyadic depth has an explicit central-limit variance. Let \(d=2p-1\). For \(1/2<p\le1\), if \(K_t\) is the dyadic depth and \(\mu_p=p/d\), then
\[
\frac{1}{\sqrt T}\sum_{t=0}^{T-1}(K_t-\mu_p)\ \Longrightarrow\ \mathcal N(0,\sigma_p^2),\qquad
\sigma_p^2=\frac{2+5d^2+24d^3-7d^4}{4d^4}.
\]
The limit \(\lim_{T\to\infty}T^{-1}\operatorname{Var}(\sum_{t<T}K_t)=\sigma_p^2\) also holds. The one-time level variance and integrated autocorrelation factor are
\[
\operatorname{Var}(K_0)=\frac{1+7d^2}{4d^2},\qquad
\frac{\sigma_p^2}{\operatorname{Var}(K_0)}=\frac{2+5d^2+24d^3-7d^4}{d^2(1+7d^2)}.
\]
In particular \(\sigma_p^2\sim1/(2d^4)\) and the normalized correlation factor is asymptotic to \(2/d^2\) as \(p\downarrow1/2\). This separates instantaneous depth fluctuations from the more severe critical slowing of their running sum.

## Assumptions and scope
Independently for each integer time \(t\ge0\), set \(X_{t+1}=2X_t\bmod1\) with probability \(p\), or \(X_{t+1}=X_t/2\) with probability \(q=1-p\). Here \(1/2<p\le1\). Start from the stationary **absolutely continuous** probability on the interval and exclude the endpoint zero; the stationary point mass at zero is not the measure in this claim. Define \(K_t=k\ge0\) precisely when \(2^{-k-1}<X_t\le2^{-k}\). Exceptional dyadic boundaries have zero probability under this stationary density; they do not affect the assertion. Put \(d=p-q=2p-1\), \(\mu_p=p/d\), and \(S_T=\sum_{t=0}^{T-1}(K_t-\mu_p)\) for integers \(T\ge1\). The central limit concerns the annealed stationary law, incorporating both initial position and independent map choices. The endpoint \(p=1\) is included; \(p=1/2\) is not.

## Proof
**Dyadic Markov reduction.** Conditional on the present dyadic band, the absolutely continuous stationary law has uniform coordinate density in that band; the independent doubling/halving branches preserve this conditional uniformity even after conditioning on the full band history. On levels \(k\ge1\), doubling decreases depth by one and halving increases it by one. On level zero, halving goes to level one, while doubling sends a uniform point of \((1/2,1]\) to a uniform point of \((0,1]\), whose new depth \(J\) obeys \(\Pr(J=j)=2^{-j-1}\). Thus the Markov transition operator is
\[
(Ph)(k)=p h(k-1)+q h(k+1)\quad(k\ge1),\qquad
(Ph)(0)=q h(1)+p\sum_{j\ge0}2^{-j-1}h(j).
\]
In particular, conditional uniformity and the stationary mass formula establish the reduction without confusing the dyadic chain with the position process.

**Stationary moments.** Writing \(\Pi(z)=\sum_{k\ge0}\pi_k z^k\) and \(\pi_0=\Pr(K=0)\), the stationarity equation is
\[
\Pi(z)=p\frac{\Pi(z)-\pi_0}{z}+qz\Pi(z)+\frac{p\pi_0}{2-z}.
\]
Requiring \(\Pi(1)=1\), and cancelling the known factor \(z-1\), gives
\[
\pi_0=\frac d{2p},\qquad \Pi(z)=\frac d{(2-z)(p-qz)}.
\]
The resulting nonnegative coefficients sum to one. Differentiating at \(z=1\) gives
\[
\mu_p=\mathbb E K=\frac p d,\quad
\operatorname{Var}(K)=\frac{1+7d^2}{4d^2},
\]
and yields the cubic moment needed below. Both PGF poles are outside the closed unit disk for \(p>q\), so all polynomial moments exist.

**Quadratic Poisson equation.** Set
\[
h(k)=\frac{k(k-1)}{2d},\qquad g(k)=k-\mu_p.
\]
For \(k\ge1\), direct substitution into the two nearest-neighbor transitions gives \((I-P)h(k)=g(k)\). At \(k=0\), the geometric reinjection satisfies \(\mathbb E[J(J-1)]=2\); hence \(Ph(0)=p/d=\mu_p\) and again \((I-P)h(0)=g(0)\). Thus the Poisson equation is exact on the whole countable state space, including the exceptional reinjection boundary.

**Martingale and variance.** The level chain is irreducible and aperiodic, with a geometric Foster drift: for some \(1<r<\min\{p/q,2\}\) when \(q>0\), the function \(r^k\) contracts in conditional expectation outside level zero, whose restart distribution has an exponential moment. At \(p=1\), every positive depth steps deterministically down to zero and level zero restarts geometrically; it is likewise geometrically ergodic. Consequently the stationary chain is ergodic with sufficient moments for the martingale central limit theorem. Define
\[
M_T=\sum_{t=0}^{T-1}\bigl(h(K_{t+1})-(Ph)(K_t)\bigr).
\]
The Poisson identity gives \(S_T=M_T+h(K_0)-h(K_T)\). Because \(h(K_t)\) has finite second moment in stationarity, the boundary is negligible under scaling by \(\sqrt T\). The martingale increments have a finite second moment and conditional variances whose time averages converge almost surely to their expectation by ergodicity; the Lindeberg condition follows by dominated truncation of the stationary increment square. The martingale CLT applies.

By stationarity and \((I-P)h=g\), its variance per step is
\[
\sigma_p^2=\mathbb E\bigl[(h(K_1)-Ph(K_0))^2\bigr]
=2\mathbb E[g(K)h(K)]-\mathbb E[g(K)^2].
\]
Differentiating the displayed PGF three times and simplifying gives
\[
\mathbb E[g(K)h(K)]=\frac{1+3d^2+12d^3}{4d^4},
\]
which yields the claimed \(\sigma_p^2\). The variance limit follows from the martingale variance identity, Cauchy--Schwarz and the uniformly bounded stationary second moment of the boundary term. For \(0<d\le1\), the numerator satisfies \(2+5d^2+24d^3-7d^4>0\), so the limiting Gaussian is nondegenerate. Dividing by the displayed one-time variance gives the exact integrated correlation factor and critical asymptotics.

## Verification
Run `python verify_depth.py` with Python 3, SymPy and NumPy. The embedded standalone checker verifies symbolically the stationarity generating-function equation, the Poisson equation at interior and reinjection levels, derivatives through the cubic moment, and the exact variance and critical-exponent identities. Independently it sums a large but finite number of autocovariances in truncated transition matrices for four sample parameter values. Those numerical truncations illustrate the formulas and **are not** exhaustive verification of infinite chains. The infinite theorem follows from the analytic proof above. The limiting variance is \(6\) at \(p=1\), \(23.25\) at \(p=3/4\), and \(372\) at \(p=3/5\).

## Relationship to prior work
Yan et al. (arXiv:2308.09269, 2023) study the Pelikan random map, its invariant densities and coordinate statistics. Monthus (2025) derives an exact dyadic Markov-chain representation and related stationary and propagator quantities; the present derivation uses that natural representation but targets a different, time-additive level observable and its exact Green--Kubo variance. A later analysis by Brevitt and Klages (2026) focuses on quasi-stationary survival and first-return phenomena, not the stationary additive-depth CLT. General Markov-chain Poisson equations and martingale CLTs are standard tools and not claimed as new. Prior propagator formulas could in principle yield the new variance after additional nontrivial computation; priority in unindexed work remains a risk.

## Limitations
The theorem is for the absolutely continuous stationary initialization only, not the absorbing atom at zero, and does not claim a stationary CLT at the critical value \(p=1/2\). It does not determine higher-order cumulants or functional limit theorems. Full older literature coverage and a separate independent mathematical audit remain outstanding. Numerical matrix truncations are illustrations, not proofs of infinite-dimensional identities.

## References
1. J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck and R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269v1 (first publicly posted 2023-08-18).
2. C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, Journal of Statistical Mechanics (2025), DOI:10.1088/1742-5468/adaa6c.
3. S. Brevitt and R. Klages, *Quasi-stationary and quasi-ergodic distributions in the Pelikan random map*, arXiv:2607.19084v1 (2026).
