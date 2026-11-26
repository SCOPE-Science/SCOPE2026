# Pell ties and the local Gaussian rank law for isotone mutual-inverse pairs

## Finding

Let \(\mathcal O_n\) be the monoid of weakly increasing self-maps of the labeled chain \([n]=\{1,\ldots,n\}\). Draw an **ordered** pair \((f,g)\) uniformly from those satisfying \(fgf=f\) and \(gfg=g\), and let \(R_n\) be its common image rank. The finite rank enumeration is known: the unnormalized weight at rank \(r\) is \(w_{n,r}=\binom{n+r-1}{2r-1}^2\), \(1\le r\le n\) [1, Eq. (3); 2]. The findings here concern the modes and the asymptotic behavior of these weights.

* **Exact modes and ties.** Let \(\tau_n=(\sqrt{1+5n^2}-1)/5\). When \(\tau_n\notin\mathbb Z\) the unique maximizing rank is \(\lfloor\tau_n\rfloor+1\). Otherwise the two maxima are \(r=\tau_n\) and \(r+1\). In the latter case the weights strictly increase up to the plateau and strictly decrease after it; in the former they strictly increase toward and strictly decrease away from the mode (empty ranges allowed). The tied sizes and ranks are exactly
  \[
  (5r+1)+n\sqrt5=(161+72\sqrt5)^j,\qquad j=1,2,\ldots.
  \]
  The first tie is at \(n=72\), between ranks 32 and 33.
* **Local and global Gaussian laws.** The standardized variable \((R_n-n/\sqrt5)/\sqrt{n/(5\sqrt5)}\) converges in distribution to \(N(0,1)\). For every sequence \(a_n=o(n^{2/3})\), with \(a_n\ge0\), uniformly for integer \(1\le r\le n\) with \(|r-n/\sqrt5|\le a_n\),
  \[
  \Pr(R_n=r)=\sqrt{\frac{5\sqrt5}{2\pi n}}\exp\!\left(-\frac{5\sqrt5(r-n/\sqrt5)^2}{2n}\right)(1+o(1)).
  \]
* **Normalization and rarity.** With \(\varphi=(1+\sqrt5)/2\), the normalizing sum for the rank law is
  \[
  Z_n:=\sum_{r=1}^n w_{n,r}\sim\frac{\varphi^{4n}}{2\sqrt{2\pi}\,5^{1/4}\sqrt n}.
  \]
  For two independent uniform maps, the probability of both inverse identities is therefore asymptotic to \(\frac{\sqrt{2\pi}}{5^{1/4}}\sqrt n\, (\varphi^4/16)^n\).

## Assumptions and scope

These are full isotone maps, not order-decreasing or partial maps, and the inverses are semigroup inverses, not necessarily two-sided functional inverses. The law of \(R_n\) is for a uniform valid pair (inverse-graph edges, with order), not a uniform map, a uniform idempotent, or the number of partners of a map at a fixed rank. The rarity statement uses the uniform product measure before conditioning.

## Proof

**Known weights.** Each rank-\(r\) map is specified by its interval kernel and its increasing image, so there are \(\binom{n-1}{r-1}\binom nr\) such maps. The rank inequalities from the two sandwich equations give equal ranks. Thus the rank-\(r\) pair count equals the first moment of the inverse degree in [1, Eq. (3)] times the number of rank-\(r\) maps, yielding \(w_{n,r}\) for \(r\ge2\). For \(r=1\) all ordered pairs of constant maps qualify, giving \(n^2=w_{n,1}\). The full range is also stated directly in [2]. An equivalent explanation from the crossed-transversal relation [3, §2] is that each kernel comes with a marked point in each fiber (a member of the opposite image); these choices are independent for the two kernels. For one half the generating function is \((\sum_{a\ge1}az^a)^r=z^r(1-z)^{-2r}\), whose \(z^n\)-coefficient is the classical idempotent count [4]. Squaring gives the known pair weights.

**Modes.** If \(E_{n,r}=\sqrt{w_{n,r}}\), then for \(r<n\)
\[
\frac{E_{n,r+1}}{E_{n,r}}=\frac{n^2-r^2}{2r(2r+1)}.
\]
It exceeds, equals, or is less than one according as \(n^2\) exceeds, equals, or is less than \(5r^2+2r\), a strictly increasing expression for \(r\ge1\). This gives the claimed modes (\(0<\tau_n<n\); at \(n=1\) there is only one rank). Equality is equivalent to \((5r+1)^2-5n^2=1\). The least positive Pell unit of norm one for this integer equation is \(9+4\sqrt5\): the cases \(1\le n\le3\) do not give a square \(5n^2+1\), and \(n=4\) gives \(9^2\). Thus all positive solutions are powers of this unit. Their constant coefficients modulo 5 are \((-1)^m\) for power \(m\), so the restriction \(5r+1\equiv1\pmod5\) requires even powers. Squaring the unit gives the family stated above; all these solutions have \(1\le r<n\) by \(n^2=5r^2+2r\).

**Upper tails and normalization.** Write \(x=r/n\) and
\[
h(x)=(1+x)\log(1+x)-(1-x)\log(1-x)-2x\log(2x),
\quad B(x)=\frac{x}{\pi(1-x^2)}.
\]
Extend \(h\) continuously to \([0,1]\). From \(E_{n,r}=\frac{2r}{n+r}\binom{n+r}{2r}\), Stirling gives
\[
w_{n,r}=\frac{B(x)}{n}e^{2nh(x)}(1+O(n^{-1}))
\]
uniformly for \(x\) in compact subintervals of \((0,1)\). Globally \(E_{n,r}\le e^{nh(x)}\) by the binomial entropy bound (obtained by bounding the single binomial probability at success parameter \(2r/(n+r)\) by one, with the endpoint by continuity). Since \(h'(x)=\log[(1-x^2)/(4x^2)]\), there is a unique maximum at \(x_*=1/\sqrt5\), where \(h(x_*)=\log[(1+x_*)/(1-x_*)]=2\log\varphi\). Furthermore \((2h)''(x_*)=-5\sqrt5\). The contribution outside any fixed closed interior interval around \(x_*\) is exponentially smaller than \(e^{2nh(x_*)}/\sqrt n\). On a sufficiently small such interval, Taylor's theorem bounds each weight by \(C e^{2nh(x_*)}e^{-cn(x-x_*)^2}/n\) for constants \(C,c>0\). After multiplication by \(\sqrt n e^{-2nh(x_*)}\), the sum over \(|r-nx_*|>M\sqrt n\) inside the interval is bounded by a constant times a Gaussian tail tending to zero as \(M\to\infty\), by comparison with its integral. For bounded \(|r-nx_*|/\sqrt n\) the lattice Riemann sum consequently gives
\[
Z_n\sim \frac{B(x_*)e^{2nh(x_*)}}{\sqrt n}\int_{\mathbb R}e^{-5\sqrt5 u^2/2}\,du
=\frac{\varphi^{4n}}{2\sqrt{2\pi}\,5^{1/4}\sqrt n}.
\]

**Local law and rarity.** On the stated local window, the cubic error in the expansion of \(2nh(r/n)\) is \(O(a_n^3/n^2)=o(1)\); also \(B(r/n)/B(x_*)\to1\) uniformly. Dividing the resulting estimate for \(w_{n,r}\) by \(Z_n\) proves the relative local approximation. On fixed standardized intervals it sums to the normal interval probability via a Riemann sum; together with the tail bound this proves weak convergence. Finally stars-and-bars gives \(|\mathcal O_n|=\binom{2n-1}{n}\sim 4^n/(2\sqrt{\pi n})\). The exact probability \(Z_n/|\mathcal O_n|^2\) yields the stated rarity prefactor and rate.

## Reproducibility

The accompanying standard-library Python scripts `verify_direct.py` and `verify_asymptotic.py` are unchanged. The former enumerates pairs at small sizes to check the known weights by the sandwich identities; the latter checks finite modes across the first Pell size and compares exact sums to the limiting approximation. These computations are finite checks, not proofs of the Pell classification or the local law.

## Relation to earlier results and limitations

The rank weights themselves and their exact sum as an expression are not novelty claims. The first-moment identity in [1] gives those weights, and [2] states them directly; [2] also optimizes the maximum number of partners of an individual map, a different statistic from the most probable rank of a valid pair. Higgins [3] uses the crossed-transversal structure for inverse matchings. The classical idempotent array in [4] is the square root of the pair-weight array, not the weights of this sampling law. Gaussian limits for the logarithm of the inverse-partner degree of one map at a prescribed proportional rank [5] do not describe fluctuations of the rank of a uniformly selected valid pair. This result isolates the arithmetic mode ties and the sharp local and global asymptotics of the pair-rank weights. Absolute priority for equivalent treatments of the underlying binomial array is not asserted. No inverse-matching or arbitrary-poset result is claimed.

## References

1. [Exact inverse-degree moments and Dirichlet limits for isotone transformation monoids](https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-inverse-degree-moments-and-dirichlet-limits-for-isotone-tr--35b0c2d31193/RESULT.md), Eq. (3).
2. [Exact extremal inverse neighborhoods in order-preserving transformation monoids](https://github.com/Resultary/2026/blob/main/2026/11/2/SCOPE-exact-extremal-inverse-neighborhoods-in-order-preserving-transfo--56b350ea9bb8/RESULT.md), Finding.
3. P. M. Higgins, *Balanced weightings and permutation matchings applied to the monoid of order-preserving mappings*, arXiv:2610.01912v1, §2.
4. OEIS Foundation, [A078812](https://oeis.org/A078812), idempotent triangle.
5. [Gaussian logarithmic fluctuations of inverse-partner degrees at proportional rank](https://github.com/Resultary/2026/blob/main/2026/11/8/SCOPE-the-inverse-partner-degree-law-and-gaussian-logarithmic-fluctuat--f03924d534c3/RESULT.md), Finding.
