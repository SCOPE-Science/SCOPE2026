# Exact 21-reset threshold for nonmonotone Brownian search termination times

## Finding

For a Brownian searcher on the half-line with independent Poisson resetting to its starting point, terminate the experiment on first absorption at the origin **or** on the reset event that exhausts a finite budget. The mean time to this *either-event termination* is strictly decreasing with reset rate if at most 20 resets are allowed before the fatal reset. If 21 or more resets are allowed, the mean instead has at least one strict local minimum followed by at least one strict local maximum. Thus the sharp integer at which a nonmonotone reset-rate profile first becomes possible is 21 allowed resets, independent of starting distance and diffusivity. No assertion of exactly two extrema at higher budgets is made.

## Assumptions and scope

Fix arbitrary \(a,D,r>0\). A particle starts at \(a\) and diffuses on \((0,\infty)\) with generator \(D\partial_{xx}\), being absorbed on reaching 0. Independently, Poisson resetting events occur at rate \(r\). Every nonterminal reset instantaneously returns the particle to \(a\). Fix an integer \(\mu\ge0\): the first \(\mu\) resets are permitted, while the next, \((\mu+1)\)-st, terminates the experiment if absorption has not already occurred. Write \(T_\mu(r)\) for the expectation of time to **either** terminating event. It is not the conditional mean time to successful absorption.

Let \(n=\mu+1\), \(z=a\sqrt{r/D}\), and \(q=1-e^{-z}\). Then \(0<q<1\) and

\[
 T_\mu(r)=\frac{a^2}{D}\frac{S_n(q)}{z^2},\qquad S_n(q)=\sum_{j=1}^{n}q^j.
\]

The theorem is

\[
\begin{aligned}
0\le\mu\le20 &: \quad T_\mu'(r)<0\quad\text{for every }r>0,\\
\mu\ge21 &: \quad T_\mu'(r)>0\quad\text{at }r=\frac{D(\log7)^2}{a^2},
\end{aligned}
\]

with the additional property that for \(\mu\ge21\), the derivative is negative at sufficiently small and sufficiently large positive rates. Consequently the latter profiles each possess a strict local minimum and a later strict local maximum.

## Proof

**1. Independent-cycle reduction.** Let \(\tau\) be the absorption time of Brownian motion without resetting. Its Laplace transform is \(\mathbb E[e^{-r\tau}]=e^{-a\sqrt{r/D}}=1-q\). With an independent exponential clock \(E_r\), the chance to reset before absorption is \(q=\mathbb P(E_r<\tau)\), and

\[
\mathbb E[\min(\tau,E_r)]=\frac{1-\mathbb E[e^{-r\tau}]}r=\frac qr.
\]

There are at most \(n\) independent attempts. Attempt \(j\) occurs with probability \(q^{j-1}\), giving

\[
T_\mu(r)=\frac qr\sum_{j=0}^{n-1}q^j
=\frac1r\sum_{j=1}^nq^j.
\]

This agrees with Eq. (5.37) of the motivating paper, but follows directly from the stopping rule.

**2. Reduce monotonicity to a weighted-index bound.** Set

\[
 E_n(q)=\frac{\sum_{j=1}^n j q^j}{\sum_{j=1}^n q^j},\qquad
 f(q)=\frac{(1-q)[-\log(1-q)]}{q},\qquad
 A_n(q)=f(q)E_n(q).
\]

Differentiating the dimensionless mean with respect to \(z\) shows

\[
 \operatorname{sgn}\frac{dT_\mu}{dr}
 =\operatorname{sgn}\left(A_n(q)-2\right),
\]

because \(dr/dz>0\). Under the probability weights proportional to \(q^j\), \(E_n\) is the mean of the index \(j\). For fixed \(q\in(0,1)\), it increases strictly with \(n\) (adjoining the new largest index raises the mean), and \(E_n(q)\le(1-q)^{-1}\). For fixed \(n\), it increases in \(q\), since \(qE_n'(q)\) is the strictly positive index variance. Also \(E_n(q)<(n+1)/2\), as the weights are strictly decreasing with \(j\). Finally, \(f(q)=z/(e^z-1)\) is strictly decreasing in \(q\).

**3. Exact proof for every budget \(\mu\le20\).** Monotonicity in \(n\) makes it enough to show \(A_{21}(q)<2\) for all \(0<q<1\).

For \(0<q\le1/2\), the infinite-geometric bound gives

\[
 A_{21}(q)\le\frac{-\log(1-q)}q\le2\log2<2.
\]

For \(19/20\le q<1\), put \(t=1-q\). Since \(-t\log t\) is increasing for \(0<t\le1/20\), and \(\log20<3\),

\[
 A_{21}(q)<\frac{11}{q}\frac{\log20}{20}<\frac{33}{19}<2.
\]

On the compact middle interval \([1/2,19/20]\), an exact-rational finite-interval certificate closes the remaining gap. For \(0<q<1\) put \(s=q/(2-q)\) and

\[
 U(q)=2\left(\sum_{k=0}^{63}\frac{s^{2k+1}}{2k+1}
 +\frac{s^{129}}{129(1-s^2)}\right).
\]

The atanh expansion and a geometric bound for its remaining positive tail imply \(-\log(1-q)<U(q)\). For every subinterval \([u,v]\subset[1/2,19/20]\), decreasing \(f\) and increasing \(E_{21}\) yield the rigorous upper bound

\[
 A_{21}(q)< U(u)\frac{1-u}{u}E_{21}(v)
 \quad\text{for all }q\in[u,v].
\]

The included `verify.py` performs a deterministic dyadic subdivision of the full middle interval and verifies the strict inequality

\[
 U(u)\frac{1-u}{u}E_{21}(v)<2
\]

at each of 80 rational subintervals (159 tested nodes, maximum subdivision depth 10). All comparisons use exact Python `Fraction` arithmetic. These finite intervals cover the entire middle range, so the certificate is an infinite-domain proof, not sample-based evidence. Thus every \(n\le21\) has \(T_\mu'(r)<0\) for all positive rates.

**4. Sharpness at \(\mu=21\), and persistence for every higher budget.** Take \(q=6/7\), so \(z=\log7\). The seven-term positive atanh partial sum for \(s=3/4\) establishes \(\log7>97/50\) by exact rational arithmetic. Direct rational evaluation in `verify.py` establishes

\[
 \frac{97}{50}\frac{1/7}{6/7}E_{22}(6/7)>2.
\]

It follows that \(A_{22}(6/7)>2\). Since \(E_n(q)\ge E_{22}(q)\) for every \(n\ge22\), this strict inequality holds for all higher budgets. For each fixed finite \(n\), however, \(A_n(q)\to1\) as \(q\downarrow0\) and \(A_n(q)\to0\) as \(q\uparrow1\). The analytic derivative is therefore negative near both endpoints and positive at the displayed interior point. Continuity and analyticity force at least one strict local minimum followed by at least one strict local maximum. This completes the proof.

## Verification

Run `python3 verify.py` using the standard library. It checks the complete exact rational interval cover (80 leaves, 159 tested nodes, maximum depth 10) and the strict rational witness at \(q=6/7\). The proof also uses elementary calculus facts explicitly given above, not numerical root finding. Numerical exploration suggests two stationary points for the first nonmonotone case \(\mu=21\), near \(z=1.771\) and \(z=2.133\); this observation is **not** used as a proof or a claim of uniqueness.

## Relationship to prior work

Bressloff, *Truncated stochastically switching processes* (2023 preprint, 2024 journal), Section V.B, Eq. (5.37), explicitly supplies the same mean-termination formula and Fig. 4 qualitatively shows monotonicity at small reset budgets and nonmonotonicity at larger ones. The numerical examples reported there include \(\mu=10,50,100\), but give no sharp all-budget threshold. The present result proves that the first budget at which this qualitative change can occur is exactly \(\mu=21\), uniformly over diffusivity and distance. The physical stopping-time observable and forward formula are not claimed as new.

Biroli, Majumdar and Schehr (2023) obtain critical *numbers of independent Brownian walkers* with resetting, with unlimited resetting until target encounter. Their critical-walker phenomenon is distinct from a cap on reset events for one searcher, and does not determine this integer budget. Other restart-efficiency studies concern successful completion times rather than termination by resource exhaustion.

## Limitations

This theorem classifies the existence, not the exact number, of stationary points for budgets \(\mu\ge21\). It does not optimize the conditional duration of successful search or the success probability. For each fixed finite budget, \(T_\mu(r)\to0\) as \(r\to\infty\), because the process can terminate almost immediately by exhausting its reset allowance; the local minimum should not be mistaken for a global optimum of successful search efficiency. The result assumes the same resetting point and initial point, a Poisson reset clock, one-dimensional Brownian motion, and termination immediately upon exceeding the budget. Exact scientific priority relative to all unpublished or unindexed work is not established.

## References

1. P. C. Bressloff, *Truncated stochastically switching processes*, arXiv:2310.20502v1 (first public 2023-10-31), Phys. Rev. E 109, 024103 (2024), https://arxiv.org/abs/2310.20502 ; https://doi.org/10.1103/PhysRevE.109.024103.
2. M. Biroli, S. N. Majumdar, G. Schehr, *Critical number of walkers for diffusive search processes with resetting*, arXiv:2303.18012 (2023), Phys. Rev. E 107, 064141 (2023), https://arxiv.org/abs/2303.18012.
3. M. R. Evans and S. N. Majumdar, *Diffusion with optimal resetting*, J. Phys. A 44, 435001 (2011), https://doi.org/10.1088/1751-8113/44/43/435001.
