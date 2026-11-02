# Exact coalescence-time law and a non-Gumbel logarithmic limit on the star

## Finding

Let \(\tau_n\) be the time until only one particle remains when independent rate-one continuous-time simple random walks start at every vertex of the star with \(n\geq1\) leaves and merge on collision. For every \(s\geq0\),
\[
\mathbb E e^{-s\tau_n}
=\frac{n+1}{n+1+s}
\prod_{r=2}^{n}
\frac{(r-1)((n+1)r+ns)}{n(r+s)^2-r(n-r+1)}.
\tag{1}
\]
The empty product equals one. In particular, with \(H_n=\sum_{j=1}^n1/j\),
\[
\mathbb E\tau_n=H_n+1-\frac{H_n+2}{n+1}.
\tag{2}
\]
The centered variables \(\tau_n-\log n\) converge in distribution to a nondegenerate, non-Gumbel random variable \(W\) whose Laplace transform, for \(s\geq0\), is
\[
\mathbb E e^{-sW}=\Gamma(1+s)
\prod_{r=2}^{\infty}\frac{(r+s)(r+s-1)}{(r+s)^2-r}.
\tag{3}
\]
This product converges locally uniformly for \(s\geq0\). Its first three cumulants are
\[
\mathbb EW=\gamma+1,\qquad
\operatorname{Var}(W)=\frac{\pi^2}{2}-1,\qquad
\kappa_3(W)=14+14\zeta(3)-2\pi^2.
\tag{4}
\]
Consequently its standardized skewness is approximately \(1.42079\), unequal to the \(1.13955\) skewness of any positively scaled Gumbel variable; a negatively scaled Gumbel has negative skewness.

## Assumptions and scope

Fix \(n\in\{1,2,\ldots\}\). The underlying graph is \(K_{1,n}\), with distinguished hub and \(n\) labeled leaves. At time zero every one of its \(n+1\) vertices contains one particle. Each remaining particle independently waits an exponential time of rate one and then jumps to a uniformly selected adjacent vertex. On landing at an occupied vertex, the moving particle coalesces with its occupant and one particle remains at that vertex; the surviving particle has a fresh independent rate-one clock. The random variable \(\tau_n\) is the first time there is exactly one surviving particle. There is no killing, immigration, noise reset, or particle creation. Rates are per occupied vertex, **not** unit rates per edge. All logarithms are natural.

## Proof

**1. A one-level excursion decomposition.** Suppose there are exactly \(r\) particles, \(2\le r\le n+1\), with the hub occupied. Then the occupied leaves number \(r-1\). Total jump rate is \(r\). A jump decreases particle count if a leaf jumps into the hub, probability \((r-1)/r\), or if the hub jumps to an occupied leaf, probability \((r-1)/(nr)\). Therefore the success probability at an event is
\[
p_{n,r}=\frac{(r-1)(n+1)}{nr},\qquad
q_{n,r}=1-p_{n,r}=\frac{n-r+1}{nr}.
\tag{5}
\]
The only unsuccessful move with hub occupied is from hub to an empty leaf. This vacates the hub. All \(r\) particles now sit on leaves, so their next jump, after an independent \(\mathrm{Exp}(r)\) wait, necessarily returns a leaf particle to the hub without changing the particle count. Thus a failed attempt uses two independent \(\mathrm{Exp}(r)\) waits, and a successful attempt uses one.

For each \(r\), let \(J_{n,r}\) count failures before success, geometrically distributed with \(\Pr(J_{n,r}=j)=p_{n,r}q_{n,r}^{j}\), \(j\ge0\). With mutually independent \(E_{r,j}\sim\mathrm{Exp}(r)\), the duration of the successful stage, starting with occupied hub, is distributed as
\[
S_{n,r}=\sum_{j=1}^{2J_{n,r}+1}E_{r,j}.
\tag{6}
\]
Conditional on success, it was the hub-to-occupied-leaf transition with probability
\[
\frac{(r-1)/(nr)}{p_{n,r}}=\frac1{n+1},
\]
and a leaf-to-hub transition otherwise. This success type is independent of the stage duration, by independent exponential holding times and categorical jump choices. In the first case the hub is vacant after coalescence. It takes one additional \(\mathrm{Exp}(r-1)\) waiting time to reoccupy it before the next occupied-hub stage.

By the strong Markov property and leaf exchangeability, all these stages and success-type marks may be chosen independent. Let \(B_{n,r}\sim\mathrm{Bernoulli}(1/(n+1))\) and \(E'_{n,r}\sim\mathrm{Exp}(r)\) be independent of all stages. Relabeling the post-collision particle count, the complete coalescence time has the exact distributional decomposition
\[
\tau_n\overset d=\sum_{r=2}^{n+1}S_{n,r}
+\sum_{r=2}^{n} B_{n,r}E'_{n,r}.
\tag{7}
\]
In particular the \(r=n+1\) stage has \(q_{n,n+1}=0\), so it is simply \(\mathrm{Exp}(n+1)\).

**2. Finite transforms and mean.** Summing a geometric series in equation (6) gives, for \(s\ge0\),
\[
\mathbb E e^{-sS_{n,r}}
=\frac{p_{n,r}\,r(r+s)}{(r+s)^2-q_{n,r}r^2},
\qquad
\mathbb E e^{-sB_{n,r}E'_{n,r}}
=\frac{(n+1)r+ns}{(n+1)(r+s)}.
\tag{8}
\]
Their product over all occupied-particle levels simplifies algebraically to (1). Furthermore
\[
\mathbb ES_{n,r}
=\frac{1+q_{n,r}}{r(1-q_{n,r})}
=\frac{r+1}{r(r-1)}-\frac{2}{(n+1)(r-1)}.
\tag{9}
\]
Adding the empty-hub delays, whose means sum to \((H_n-1)/(n+1)\), gives (2).

**3. An infinite independent-stage limit.** For every integer \(r\ge2\) define independent \(S_r\) through (6), except that its failure probability is \(q_r=1/r\), the pointwise limit of \(q_{n,r}\). Thus
\[
\mathbb ES_r=\frac{r+1}{r(r-1)},\qquad
\operatorname{Var}(S_r)=\frac{r^2+4r-1}{r^2(r-1)^2}.
\tag{10}
\]
Couple \(J_{n,r}\) and \(J_r\) by common uniform trials, so \(J_{n,r}\le J_r\), and share the exponential waits. The expected aggregate excess duration of all limiting stages over finite stages is
\[
\sum_{r=2}^{n+1}\frac{2}{r}
\left(\frac{q_r}{1-q_r}-\frac{q_{n,r}}{1-q_{n,r}}\right)
=\frac{2H_n}{n+1}.
\]
The expected aggregate contribution of the empty-hub delays is \((H_n-1)/(n+1)\). Therefore the coupling yields
\[
\mathbb E\left|\tau_n-\sum_{r=2}^{n+1}S_r\right|
\le\frac{3H_n-1}{n+1}\longrightarrow0.
\tag{11}
\]
The series \(\sum_{r\ge2}(S_r-\mathbb ES_r)\) converges almost surely and in \(L^2\), because its terms are independent, centered, and have summable variances. Since \(\sum_{r=2}^{n+1}\mathbb ES_r=H_n+1-1/(n+1)\) and \(H_n-\log n\to\gamma\), equation (11) proves
\[
\tau_n-\log n\Rightarrow
W:=\gamma+1+\sum_{r=2}^{\infty}(S_r-\mathbb ES_r).
\tag{12}
\]

**4. Laplace product and non-Gumbel law.** Setting \(q_r=1/r\) in (8) and factoring gives
\[
\mathbb E e^{-sS_r}
=\frac{r-1}{r-1+s}
\frac{(r+s)(r+s-1)}{(r+s)^2-r}.
\tag{13}
\]
The first factors telescope through the gamma-function ratio, while the logarithm of each second factor is \(O_s(r^{-2})\), uniformly for \(s\) in compact nonnegative sets. The centered finite products have uniformly bounded higher exponential moments for each fixed nonnegative \(s\), so (12) permits taking expectations and yields (3).

The variance in (10) decomposes as
\[
\frac{r^2+4r-1}{r^2(r-1)^2}
=-\frac2{r-1}+\frac4{(r-1)^2}
+\frac2r-\frac1{r^2},
\]
whose sum is \(\pi^2/2-1\). For the third cumulant, differentiate the logarithm of the moment generating function in (13) at zero to obtain
\[
\kappa_3(S_r)=2\left((r-\sqrt r)^{-3}
+(r+\sqrt r)^{-3}-r^{-3}\right)
=\frac{12}{r-1}-\frac{12}{(r-1)^2}
+\frac{16}{(r-1)^3}-\frac{12}r-\frac2{r^3}.
\]
Summing gives \(14+14\zeta(3)-2\pi^2\). The characteristic function and exponential moments exist near the origin by the independent-series construction. Standardized third cumulants are invariant under positive affine changes and change sign under negative scaling. The strictly positive, approximately \(1.42079\) value here differs from the classical Gumbel magnitude \(12\sqrt6\zeta(3)/\pi^3\approx1.13955\). This excludes every affine Gumbel law and completes the proof.

## Verification

Run `python3 coalescence_check.py` using Python 3 and its standard library. The checker independently constructs the full finite-state generator on every nonempty occupied-vertex subset of \(K_{1,n}\) and solves the exact rational Laplace and moment equations, rather than relying on the geometric-stage decomposition. It reproduces (1), (2) for \(1\le n\le6\), the exact second moments for \(1\le n\le5\), and supplementary numerical convergence and positivity checks. The replay completed with **467 assertions passed**. Finite checks do not establish the limiting theorem; steps 3–4 above do.

## Relationship to prior work

Durrett's *Voter Models, Coalescing RWs*, Chapter 7, Example 7.6.1, explicitly identifies the same rate-one star coalescence model and proves the order-\(\log n\) **lower bound**; it does not provide the finite Laplace transform (1), the exact mean (2), or the centered limit (3). Cristali, Jiang, Junge, Kassem, Sivakoff and York (2019) derive geometric-stage sums for annihilating particles on stars. Their annihilation rule (colliding particles both disappear) and discrete-time sampling are different from pairwise coalescence here; their proposition does not imply (1)–(4). Fernley and Ortgiese (2019) study voter/coalescent observables on subcritical random graph models and do not give this deterministic-star centered law. Broader coalescing-walk and voter duality theory motivates the question, but no equivalently covering full statement was found in the inspected sources. Historical priority beyond the inspected sources remains a risk.

## Limitations

The theorem applies only to one particle initially at every vertex of a star, per-particle rate-one simple random walks, and binary collisions that merge into one particle. The explicit formula and limit are not asserted for per-edge-rate walks, annihilation, two-type particles, incomplete initial occupancy, or arbitrary graph sequences. No independent mathematical audit or exhaustive historical-priority certification has been performed.

## References

- R. Durrett, *Voter Models, Coalescing RWs*, Chapter 7, Example 7.6.1, https://sites.math.duke.edu/~rtd/DoG/Chapter7.pdf (accessed for the star model and its logarithmic lower bound).
- I. Cristali, Y. Jiang, M. Junge, R. Kassem, D. Sivakoff and G. York, *Two-type annihilating systems on the complete and star graph*, arXiv:1908.03218, first posted 2019-08-08, https://arxiv.org/abs/1908.03218 (model/annihilation comparison).
- J. Fernley and M. Ortgiese, *Voter models on subcritical inhomogeneous random graphs*, arXiv:1911.13187, first posted 2019-11-29, https://arxiv.org/abs/1911.13187 (graph voter/coalescent context).
- J. Hermon and collaborators, *Mean Field Behavior during the Big Bang Regime for Coalescing Random Walks*, https://arxiv.org/abs/2105.11585 (general coalescence framework, distinct clock scaling and observables).
