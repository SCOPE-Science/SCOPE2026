# A Gaussian critical-window crossover for the mean coordinate of the Pelikan random map

## Finding

For a random mixture of the doubling map and contraction by two, the physical coordinate has an exact finite-time binomial representation. At the critical-window bias \(p_n=1/2+\alpha/\sqrt n\), it has a universal, explicit Gaussian crossover on the scale \(n^{-1/2}\):
\[
\lim_{n\to\infty}\sqrt n\,\mathbb E_{p_n}X_n
=F(\alpha):=\sqrt{\frac2\pi}e^{-2\alpha^2}+4\alpha\Phi(2\alpha).
\]
Here \(\Phi\) is the standard normal distribution function. This establishes the full finite-observation-time interpolation between the contracting and chaotic sides of the intermittent threshold, rather than an asymptotic at one fixed probability.

An exact identity behind the limit is, for each \(0<p<1\), integer \(n\ge0\), and a sum \(S_m\) of \(m=n+1\) independent signs with positive-sign probability \(p\),
\[
\mathbb E_p X_n=\frac1{2pm}\sum_{\substack{1\le k\le m\\k\equiv m\ (\mathrm{mod}\ 2)}}
 k\binom{m}{(m+k)/2}p^{(m+k)/2}(1-p)^{(m-k)/2}
 \sum_{j=0}^{k-1}\left(\frac{1-p}{2p}\right)^j.
\]
This finite sum is well defined even at \(p=1/3\) and avoids a singular substitution at the threshold. In particular \(F(0)=\sqrt{2/\pi}\), while \(F'(\alpha)=4\Phi(2\alpha)>0\) and \(F''(\alpha)=8\varphi(2\alpha)>0\), where \(\varphi\) is the standard normal density.

## Assumptions and scope

For each \(p\in(0,1)\), let \(X_0\) be uniform on \([0,1)\). At each iteration choose independently the map \(x\mapsto2x\bmod1\) with probability \(p\) or \(x\mapsto x/2\) with probability \(q=1-p\). Expectations average over the initial point and all map choices. In the scaling assertion \(\alpha\in\mathbb R\) is fixed, \(n\to\infty\), and \(p=p_n\) changes with \(n\); for sufficiently large \(n\), it lies in \((0,1)\). This is not a claim about any quenched orbit, a stationary distribution at the critical parameter, or arbitrary initial densities.

## Proof

**1. Closed dyadic-shell dynamics.** Partition \((0,1)\) into \(I_j=[2^{-j-1},2^{-j})\), \(j\ge0\). The uniform initial distribution and both branch maps preserve the class of distributions uniform within each shell. Let \(\pi_t(j)=\Pr(X_t\in I_j)\). From the two branches, for \(j\ge0\) and with \(\pi_t(-1)=0\),
\[
\pi_{t+1}(j)=p\pi_t(j+1)+q\mathbf1_{\{j\ge1\}}\pi_t(j-1)
 +p\,2^{-j-1}\pi_t(0).
\]
Indeed, on the top shell the doubling branch becomes uniform on the whole unit interval, explaining the reset term. Initially \(\pi_0(j)=2^{-j-1}\). Conditional on shell \(j\), the coordinate mean is \(3\cdot2^{-j}/4\).

**2. Exact generating function.** For formal variables \(z,u\), put \(G(z,u)=\sum_{t,j\ge0}\pi_t(j)z^t u^j\) and \(P(z)=\sum_{t\ge0}\pi_t(0)z^t\). Summing the shell recurrence yields
\[
G(z,u)=\frac{(2-u)^{-1}+pzP(z)[(2-u)^{-1}-u^{-1}]}
{1-z(p/u+qu)}.
\]
Let \(r(z)\) be the unique formal power series satisfying \(r=z(p+qr^2)\), with \(r(0)=0\). The denominator vanishes at \(u=r\), and absence of negative powers of \(u\) forces cancellation in the numerator. Thus \(P(z)=r/[2pz(1-r)]\). Evaluating at \(u=1/2\) gives the coordinate-mean generating series
\[
M_p(z):=\sum_{t\ge0}\mathbb E_p X_t z^t
=\frac{r(z)}{z(1-r(z))(2p-qr(z))}.
\]
The identity is formal at the origin and holds without assumptions on long-time stationarity.

**3. First-passage coefficient identity.** Write \(c=q/(2p)\). Algebraically,
\[
M_p(z)=\frac1{2pz}\sum_{k\ge1}A_k r(z)^k,
\qquad A_k=\sum_{j=0}^{k-1}c^j.
\]
The power series \(r(z)^k\) is the first-passage generating series for a biased nearest-neighbor walk starting at height \(k\), with downward probability \(p\). By the ballot or cyclic-lemma identity, for each \(m\ge k\) of the same parity,
\[
[z^m]r(z)^k=\frac{k}{m}\Pr(S_m=k),
\quad \Pr(S_m=k)=\binom m{(m+k)/2}p^{(m+k)/2}q^{(m-k)/2}.
\]
All other coefficients vanish. Extracting \([z^n]M_p(z)\) proves the stated exact finite-binomial representation.

**4. Joint critical-window limit.** Fix real \(\alpha\), set \(p_n=1/2+\alpha/\sqrt n\), \(q_n=1-p_n\), \(c_n=q_n/(2p_n)\), and \(m=n+1\). For all sufficiently large \(n\), \(0<c_n\le3/4\). Accordingly,
\[
\mathbb E_{p_n}X_n=\frac1{2p_nm(1-c_n)}\left(
\mathbb E[S_m^+]-\mathbb E[S_m^+c_n^{S_m^+}]\right).
\]
Here \(S_m^+=\max(S_m,0)\); its zero value makes the formula valid for negative walk endpoints. Since \(0\le s(3/4)^s\le C\) uniformly for integers \(s\ge0\), the second expectation is uniformly bounded. The triangular-array central limit theorem and bounded second moments give, by uniform integrability,
\[
\frac{S_m}{\sqrt n}\Rightarrow Z+2\alpha,
\qquad \frac1{\sqrt n}\mathbb E[S_m^+]\longrightarrow
\mathbb E[(Z+2\alpha)^+],
\]
with standard normal \(Z\). Since \(2p_n(1-c_n)\to1/2\) and \(m/n\to1\), it follows that
\[
\sqrt n\,\mathbb E_{p_n}X_n\longrightarrow
2\mathbb E[(Z+2\alpha)^+]
=2\varphi(2\alpha)+4\alpha\Phi(2\alpha)=F(\alpha).
\]
The derivative and edge laws follow from elementary differentiation and the Gaussian tail formula. No limit interchange between fixed \(p\) and time is used.

## Verification

The accompanying standalone standard-library script `checker.py` calculates the finite-time coordinate mean in two independent exact-rational ways: integration of every affine branch of the random map and evaluation of the ballot formula. All 27 comparisons (nine times at each of three distinct branch probabilities) agree exactly. It also reports reference numerical evaluations of \(F\) at three biases. The infinite-time crossover and its sharp prefactor are established by the analytic central-limit argument, not by finite checks. Reproduce with `python checker.py`.

## Relationship to prior work

Yan, Majumdar, Ruffo, Sato, Beck and Klages [1] introduce and analyze the simple random expanding/contracting map, including invariant densities, correlations and its intermittent threshold. Monthus [2] gives an explicit full transient shell propagator, the exact expression of mean position as a shell observable (her Eqs. 157–159), and the leading fixed-critical-parameter shell occupation asymptotics (her Eq. 66); these established ingredients and the elementary ballot theorem are not claimed as new. Homburg and collaborators [3] give a broader theory of critical intermittency for a different family of interval maps. The present claim is specifically the **joint limit in which the map-selection probability moves across the threshold at distance of order \(n^{-1/2}\)**, and the resultant closed Gaussian crossover function for the physical coordinate. The fixed-parameter formulas and estimates in [1,2] do not themselves state this joint-limit theorem.

## Limitations

The exact finite-time binomial identity follows from the special dyadic affine geometry and does not automatically generalize to other random maps. The crossover concerns annealed first moments from a uniform start. It does not prove a process-level invariance principle, quenched convergence, or a full distributional limit. Literature concerning explicit transients of this exact map makes the publication-priority comparison particularly close; independent priority and mathematical review are not yet established. The analytic arguments above supply mathematical evidence, not independent certification.

## References

[1] J. Yan, M. Majumdar, S. Ruffo, Y. Sato, C. Beck, R. Klages, *Transition to anomalous dynamics in a simple random map*, arXiv:2308.09269 (first posted 2023-08-18), https://arxiv.org/abs/2308.09269.

[2] C. Monthus, *Explicit dynamical properties of the Pelikan random map in the chaotic region and at the intermittent critical point towards the non-chaotic region*, arXiv:2409.19999 (first posted 2024-09-30), https://arxiv.org/abs/2409.19999.

[3] A. J. Homburg, C. Kalle, M. Ruziboev, E. Verbitskiy, B. Zeegers, *Critical Intermittency in Random Interval Maps*, Comm. Math. Phys. 394 (2022), https://doi.org/10.1007/s00220-022-04396-9.
