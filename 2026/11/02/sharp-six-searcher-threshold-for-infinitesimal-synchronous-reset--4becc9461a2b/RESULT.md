# Sharp six-searcher threshold for infinitesimal synchronous resetting in lattice search

## Finding
Consider \(N\) independent, discrete-time, nearest-neighbor simple symmetric random walks started at site \(2\) on the nonnegative integer half-line, with an absorbing target at \(0\). Write \(\tau_N\) for the first target hit by any walker, and \(\tau_N(q)\) for the first target hit under simultaneous resetting: after each unsuccessful step, with probability \(q\in(0,1)\), all walkers are returned to site \(2\) without using an additional time step. Choices at successive times are independent of the walks.

**Theorem.** For \(N=1,2\), \(\mathbb E\tau_N=\infty\) but \(\mathbb E\tau_N(q)<\infty\) for every \(q>0\). For every \(3\le N\le6\), all sufficiently small \(q>0\) strictly reduce \(\mathbb E\tau_N(q)\) below \(\mathbb E\tau_N\). For every \(N\ge7\), all sufficiently small \(q>0\) strictly *increase* the mean. In particular, the sharp integer cutoff between infinitesimal improvement and deterioration is six searchers. No assertion is made about globally optimal or finite-size reset probabilities.

For \(N\ge5\), the signed first-order response exists and satisfies
\[
\left.\frac{d}{dq}\mathbb E\tau_N(q)\right|_{q=0+}=\mu_N^2-\mu_N-h_N,
\quad \mu_N=2\sum_{m\ge0}a_m^N,\quad h_N=\sum_{m\ge0}(4m+1)a_m^N,
\]
where \(a_m=\frac{2m+1}{m+1}\binom{2m}{m}4^{-m}\). The derivative is negative for \(N=5,6\) and positive for every \(N\ge7\). For \(N=3,4\), the right derivative is negative infinity.

## Assumptions and scope
All \(N\) walkers are independent between reset events and use fair steps \(+1\) or \(-1\) until the first target hit. The reset decision is common to all walkers and is made only following a globally unsuccessful step. At a reset, each walker returns simultaneously to the same deterministic starting site \(2\), with no additional time cost. Time is counted in attempted walk steps. The initial (unreset) search process is not conditioned on survival.

## Proof
**One-walker survival.** Reflection and the ballot identity for a symmetric walk started at distance two show, for each integer \(m\ge0\),
\[
\Pr(\tau_1>2m)=\Pr(\tau_1>2m+1)=a_m,
\qquad a_0=1,\qquad \frac{a_{m+1}}{a_m}=\frac{2m+3}{2m+4}.
\]
For example, at time \(2m\), survival is the sum of the nonnegative endpoints of a walk starting at \(2\), after subtracting their reflected paths through \(0\); the resulting two central binomial coefficients add to the displayed \(a_m\). Since only even times can hit \(0\), the adjacent survival probabilities coincide. Independence gives \(\Pr(\tau_N>2m)=\Pr(\tau_N>2m+1)=a_m^N\).

**Moments and renewal.** The tail-sum formulas \(\mathbb ET=\sum_{t\ge0}\Pr(T>t)\) and \(\mathbb E[T(T-1)]/2=\sum_{t\ge0}t\Pr(T>t)\) yield \(\mu_N\) and \(h_N\). Stirling's formula gives \(a_m\sim 2/\sqrt{\pi m}\), so \(\mu_N<\infty\) exactly for \(N>2\), and \(h_N<\infty\) exactly for \(N>4\). Set \(f_N(q)=\mathbb E(1-q)^{\tau_N}\). The probability of success in one reset-free attempt is \(f_N(q)/(1-q)\), because the reset decision is made only after failed steps, and its mean number of completed attempted walk steps is \((1-f_N(q))/q\). Independent renewals at unsuccessful resets imply the exact identity
\[
\mathbb E\tau_N(q)=\frac{(1-q)(1-f_N(q))}{q f_N(q)}.
\]
For \(N>4\), Taylor expansion \(f_N(q)=1-\mu_Nq+h_Nq^2+o(q^2)\) proves the derivative formula. For \(N=3,4\), the second factorial moment diverges; the nonnegative remainder in the expansion increases beyond every finite bound, so \((\mathbb E\tau_N(q)-\mu_N)/q\to-\infty\). For \(N=1,2\) the unreset mean diverges, whereas resetting yields a geometric number of finite-mean unsuccessful attempts and a positive chance of a two-step hit per attempt, so the reset mean is finite.

**Signs for all integer searcher counts.** Write \(D_N=h_N+\mu_N-\mu_N^2\), the negative of the derivative. The exact-arithmetic checker described below certifies the following deliberately rounded **outward** intervals:
\[
3.783<D_5<4.087,\quad 0.082<D_6<0.084,\quad
-0.678<D_7<-0.675,\quad -0.903<D_8<-0.900,
\quad h_9<2.
\]
These are finite *rational enclosures of infinite sums*, not simulations: \(a_m\) is enclosed at each step by floor and ceiling fixed-point arithmetic on integers with scale \(10^{32}\), through \(m=9999\). Every omitted tail is bounded from above using the Wallis-type inequality
\[
\left(\binom{2m}{m}4^{-m}\right)^2\le \frac1{3m+1},
\]
which follows by induction from the identity \(4(m+1)^2(3m+1)-(2m+1)^2(3m+4)=m\). Hence for \(m\ge1\), \(a_m^2\le4/(3m)\), and sums are bounded by elementary decreasing-power integrals. The checker explicitly uses conservative rational tail estimates and asserts the strict enclosures. For every \(N\ge9\), \(0\le a_m\le1\) yields \(h_N\le h_9<2\), while \(\tau_N\ge2\) implies \(\mu_N^2-\mu_N\ge2\). Therefore \(D_N<0\) for all \(N\ge9\), completing the exhaustive sign classification.

## Verification
Run `python3 check_restart.py` with Python 3 and no external packages. The script computes integer lower/upper enclosures of the complete infinite series, checks the strict signs for \(5\le N\le8\), bounds \(h_9\), and checks 10,000 exact induction identities. Rational tail bounds are also written in the proof; the executable does not replace their mathematical justification. In particular, the very small but positive gap at \(N=6\) is certified rather than estimated from floating point.

## Relationship to prior work
Biroli, Majumdar and Schehr analyze continuous Brownian searchers with simultaneous or individual resetting and identify a noninteger Brownian critical searcher number; the present claim concerns discrete lattice walks, the smallest nontrivial starting distance, the exact infinitesimal criterion and a rigorously bounded lattice integer cutoff. Das and Giuggioli develop discrete-space-time resetting and associated first-passage laws, principally for one walker. Classical restart renewal identities are used rather than claimed as new. The finding does not infer the lattice result from a Brownian continuum limit, which does not control this fixed two-site initial condition.

## Limitations
Only the sign at vanishing reset probability is classified; a globally minimizing reset rate might behave differently. Resetting is simultaneous, instantaneous and geometrically triggered after each failure; independent per-walker resets, delayed reset costs, biased walks, different initial sites, finite lattices and higher dimensions are outside scope. Historical priority has not been independently certified.

## References
- M. Biroli, S. N. Majumdar and G. Schehr, *Critical Number of Walkers for Diffusive Search Processes with Resetting*, arXiv:2303.18012 (first public 2023-03-31), https://arxiv.org/abs/2303.18012.
- D. Das and L. Giuggioli, *Discrete space-time resetting model*, arXiv:2209.08330 (first public 2022-09-17), https://arxiv.org/abs/2209.08330.
- *Encounter times of random walkers with simultaneous resetting on networks*, arXiv:2604.20770 (first public 2026-04-22), https://arxiv.org/abs/2604.20770 (related but different encounter target).
