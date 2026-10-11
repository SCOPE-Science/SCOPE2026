# Gaussian crossover of random grid collapse under coprime expanding maps

## Finding

Let \(a,b\ge 2\) be coprime integers. On the circle \(\mathbb T=\mathbb R/\mathbb Z\), independently select the expanding map \(x\mapsto ax\pmod1\) with probability \(p_n\) and the map \(x\mapsto bx\pmod1\) otherwise. Start from the uniform probability measure \(\nu_n\) on the \(N_n=(ab)^n\) equally spaced points. Write \(\nu_{n,t,\omega}\) for the pushforward after \(t\) choices. Lebesgue probability measure \(m\) is invariant under both maps. Let \(\mathcal D(\nu,m)\) be the centered circle Cramér distance defined below, and let \(K_t\) be the number of selections of the \(a\)-map by time \(t\).

For **every** \(n\ge1\), \(t\ge0\), and selection sequence, the exact distance is
\[
\mathcal D(\nu_{n,t,\omega},m)
=\frac{a^{-(n-K_t)_+}b^{-(n-t+K_t)_+}}{\sqrt{12}},\qquad u_+=\max\{u,0\}.
\]
In particular, its first time at the maximal point-mass discrepancy, \(\tau_n=\inf\{t:\mathcal D(\nu_{n,t,\omega},m)=1/\sqrt{12}\}\), is the first time **both** kinds of map have been selected at least \(n\) times. For fixed \(p_n=p\in(0,1)\), its exact finite-time distribution is
\[
\mathbb P_p(\tau_n\le t)
=\sum_{k=n}^{t-n}\binom tk p^k(1-p)^{t-k}
\quad(t\ge 2n),
\]
with probability zero for \(t<2n\).

The critical-bias regime has a universal **Gaussian-to-folded-Gaussian crossover**. For any fixed real \(\beta\), set \(p_n=\tfrac12+\beta/\sqrt n\), restricting to the sufficiently large \(n\) for which \(0<p_n<1\). If \(Z\) is standard normal, then
\[
\frac{\tau_n-2n}{\sqrt n}\ \Longrightarrow\ \left|4\beta+\sqrt2 Z\right|.
\]
For each fixed real \(s\), put \(t_n(s)=\lfloor 2n+s\sqrt n\rfloor\). The entire logarithmic discrepancy profile converges:
\[
\frac1{\sqrt n}\log\big(\sqrt{12}\,\mathcal D(\nu_{n,t_n(s),\omega},m)\big)
\ \Longrightarrow\ 
-(\log a)\left(-\frac{s}{2}-2\beta-\frac{Z}{\sqrt2}\right)_+
-(\log b)\left(-\frac{s}{2}+2\beta+\frac{Z}{\sqrt2}\right)_+.
\]
For \(s\ge0\) the unscaled distance simultaneously converges in law to \(B_{s,\beta}/\sqrt{12}\), where \(B_{s,\beta}\) is Bernoulli with success probability
\[
\mathbb P(B_{s,\beta}=1)=
\Phi\left(\frac{s-4\beta}{\sqrt2}\right)
-\Phi\left(\frac{-s-4\beta}{\sqrt2}\right).
\]
For \(s<0\), it converges in probability to zero. The collapse-time limit is independent of the two coprime slopes, while the logarithmic distance profile retains their logarithms.

Away from the critical switching probability, if \(p_n=p\) is fixed and \(p\ne\tfrac12\), the collapse-time fluctuations instead are ordinary Gaussian:
\[
\frac{\tau_n-n/q}{\sqrt n}\Longrightarrow
\mathcal N\left(0,\frac{1-q}{q^2}\right),
\qquad q=\min\{p,1-p\}.
\]
Thus the balanced switching probability is the exact change point between the usual rare-map renewal law and a folded-normal crossover.

## Assumptions and scope

The same random choice is applied simultaneously to every grid point at each step (a *quenched* random composition), not an independently chosen map for every point. The two slopes are fixed coprime integers at least two. The grid has precisely \((ab)^n\) points; no interpolation or rounding takes place because multiplication by either integer maps this grid into itself. We compare the *pushed-forward uniform initial-grid measure* with Lebesgue measure, not an empirical measure along one point's orbit. The random variable \(K_t\) has the binomial distribution with parameters \(t,p_n\).

For probability measures \(\mu,\nu\) on the circle with cumulative functions \(F_\mu,F_\nu\) on \([0,1)\), write \(H=F_\mu-F_\nu\). The centered circle Cramér distance is
\[
\mathcal D(\mu,\nu)^2=\int_0^1\left(H(x)-\int_0^1H(u)\,du\right)^2dx.
\]
The centering makes it independent of the choice of angular origin. All limits are as \(n\to\infty\) with the displayed slopes, \(s\), \(\beta\), and, where applicable, \(p\) fixed. These are distributions over the random map sequence, not deterministic almost-sure asymptotics.

## Proof

**1. Exact image and discrepancy.** For an arbitrary deterministic word containing \(k\) occurrences of the first map and \(t-k\) of the second, commutativity gives the multiplier \(A=a^kb^{t-k}\). The image of the uniform cyclic grid \(N^{-1}\mathbb Z/\mathbb Z\) under multiplication by \(A\) is its unique subgroup of size \(M=N/\gcd(N,A)\), and all image points have equal numbers of preimages. Since \(\gcd(a,b)=1\) and \(N=(ab)^n\),
\[
M=a^{(n-k)_+}b^{(n-t+k)_+}.
\]
For the uniform probability measure on the \(M\)-point subgroup, the difference between its cumulative distribution and the uniform distribution, on \(j/M<x<(j+1)/M\), is \((j+1)/M-x\). Its average over the full circle equals \(1/(2M)\). Centering gives a sawtooth of variance \(M\int_0^{1/M}(u-1/(2M))^2du=1/(12M^2)\). Substituting the formula for \(M\) proves the first identity, including \(M=1\). Since \(a,b>1\), the maximal distance occurs exactly when \(M=1\), equivalently \(k\ge n\) and \(t-k\ge n\). Taking binomial probabilities proves the finite-time expression.

**2. Critical window.** Fix \(s,\beta\). With \(t_n=\lfloor2n+s\sqrt n\rfloor\) and \(p_n=1/2+\beta/\sqrt n\), the triangular-array central limit theorem for Bernoulli variables gives
\[
\frac{K_{t_n}-n}{\sqrt n}\Longrightarrow
\frac{s}{2}+2\beta+\frac{Z}{\sqrt2},
\qquad
\frac{t_n-K_{t_n}-n}{\sqrt n}\Longrightarrow
\frac{s}{2}-2\beta-\frac{Z}{\sqrt2}
\]
**jointly**, since the second count equals \(t_n-K_{t_n}\). Indeed \(t_np_n=n+(s/2+2\beta)\sqrt n+O(1)\), and \(t_np_n(1-p_n)/n\to1/2\). Applying the continuous mapping theorem to the exact expression in Step 1 proves the logarithmic-distance law.

The collapse event is the intersection of the two inequalities \(K_{t_n}\ge n\) and \(t_n-K_{t_n}\ge n\). Since the limiting Gaussian has no mass on either boundary, the event probability tends to the probability that \(\left|4\beta+\sqrt2Z\right|\le s\), which is zero for \(s<0\) and the displayed normal-CDF difference for \(s\ge0\). The distance itself equals \(1/\sqrt{12}\) on collapse. Off collapse, except on an event of vanishing probability near the Gaussian boundaries, at least one missing-map count is a positive multiple of \(\sqrt n\); then the distance is bounded by an exponentially decaying function of \(\sqrt n\). This proves the two-point weak limit for the unscaled distance.

The discrepancy is nondecreasing along any fixed sequence, because its subgroup order \(M\) only decreases as counts increase. Hence \(\{\tau_n\le t\}\) is exactly the collapse event at time \(t\). The just-proved distribution-function convergence at every \(s\) yields the claimed law for \((\tau_n-2n)/\sqrt n\).

**3. Fixed unequal probabilities.** Let \(q=\min\{p,1-p\}<1/2\) be the probability of the rarer multiplier. The time \(T_n\) to obtain \(n\) uses of that map is the sum of \(n\) independent geometric waiting times, each with mean \(1/q\) and variance \((1-q)/q^2\). The ordinary central limit theorem gives
\[
\frac{T_n-n/q}{\sqrt n}\Longrightarrow
\mathcal N\left(0,\frac{1-q}{q^2}\right).
\]
At time \(T_n\), the number of uses of the other map is \(T_n-n\); by the strong law this divided by \(n\) tends to \((1-q)/q>1\). Thus \(\mathbb P(\tau_n=T_n)\to1\). The two normalized hitting times consequently have the same limit, completing the proof.

## Verification

The standalone `verify.py` uses only the Python standard library. It enumerates all choice words of length at most six on grids of \(6^n\) points for \(n=1,2,3\), computes the image measure exactly with rational weights, and integrates the piecewise-affine centered Cramér distance using rational arithmetic. It compares those independently computed squares with \(1/(12M^2)\). It also enumerates Bernoulli words and matches the exact binomial-collapse probabilities. Finally, it evaluates the finite binomial sums in selected Gaussian crossover windows and compares them with the stated normal CDF. The rational enumerations are exhaustive only for these finite test sizes; neither they nor the Gaussian diagnostics replace the analytic proof for arbitrary parameters and limiting \(n\).

## Relationship to prior work

Guihéneuf and Monge's 2022 study of spatial discretizations of expanding circle maps introduces and analyzes this centered Cramér discrepancy, proving fixed-time, generic-map estimates. Their discussion explicitly identifies the resonant deterministic map \(x\mapsto2x\pmod1\) on grids with powers of two as an exception to generic behavior. Their companion numerical paper studies short-, medium-, and long-term effects and orbit mergers for smooth expanding maps. These contributions are credited; the present theorem instead computes the quenched discrepancy exactly for random compositions of two coprime integer maps and determines its transition law across the critical switching bias. The usual binomial and geometric central limit theorems are used as existing tools rather than claimed as new. No conclusion is drawn for nonlinear maps with rounding errors or for independently chosen maps at each grid point.

## Limitations

Only this exact arithmetic family, grid sizes \((ab)^n\), and the specified quenched map-selection mechanism are treated. There is no generic-random or noisy-rounding theorem. The principal normal crossover describes collapse to a single grid point, not mixing toward Lebesgue at long times. The calculations establish no novelty for the classical binomial central limit theorem itself. Publication priority relative to results on stochastic finite-grid synchronization stated in different terminology remains a residual uncertainty; the cited sources and searched comparisons are not a guarantee of exhaustive literature coverage.

## References

1. P.-A. Guihéneuf and M. Monge, *Discrepancy and discretizations of circle expanding maps I: theory*, arXiv:2206.07991v1 (first posted 16 June 2022); published as *Cramér distance and discretisations of circle expanding maps I: theory*, Nonlinearity **36** (2023), 4810–4843, DOI 10.1088/1361-6544/ace817.
2. P.-A. Guihéneuf and M. Monge, *Discrepancy and discretizations of circle expanding maps II: simulations*, arXiv:2206.08000v1 (first posted 16 June 2022); published as *Cramér distance and discretizations of circle expanding maps II: simulations*, Dynamical Systems (2023).
3. Standard binomial triangular-array and geometric waiting-time central limit theorems, used in their classical forms; no external numerical or computer-assisted theorem is assumed.
