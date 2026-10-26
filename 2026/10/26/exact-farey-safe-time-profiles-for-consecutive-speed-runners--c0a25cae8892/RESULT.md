# Exact Farey safe-time profiles for consecutive-speed runners

## Finding
For each integer \(n\ge2\), let \(\|x\|=\min_{j\in\mathbb Z}|x-j|\) and define the **simultaneous safe-time profile**
\[
G_n(\delta)=\operatorname{Leb}\{t\in\mathbb R/\mathbb Z:\|kt\|>\delta\text{ for every }1\le k\le n\},\qquad \delta\ge0.
\]
Then, for all \(\delta\ge0\),
\[
\boxed{G_n(\delta)=\sum_{\substack{1\le q,r\le n\\\gcd(q,r)=1\\q+r>n}}\frac{\bigl(1-\delta(q+r)\bigr)_+}{qr},\qquad(y)_+=\max\{y,0\}.}
\]
The sum is over **ordered** denominator pairs. It is an exact finite formula, not an asymptotic estimate. Its positive-threshold nondifferentiability points are precisely
\[
\delta=\frac1s,\qquad n+1\le s\le2n-1,
\]
**except** that \(s=2n-2\) is omitted when \(n\) is even. Every remaining point is a genuine slope jump. In particular, \(G_n(\delta)=0\) for \(\delta\ge1/(n+1)\).

At the natural union-bound radius one obtains the exact identity
\[
\boxed{G_n\!\left(\frac1{2n}\right)=1-\frac1n\sum_{q=1}^{n}\frac{\varphi(q)}q\longrightarrow1-\frac6{\pi^2}\quad(n\to\infty),}
\]
where \(\varphi\) denotes Euler's totient function. The final segment of the profile is also exact: for \(1/(n+2)\le\delta\le1/(n+1)\),
\[
\boxed{G_n(\delta)=\frac{2\bigl(1-(n+1)\delta\bigr)}{n+1}\sum_{\substack{1\le j\le n\\\gcd(j,n+1)=1}}\frac1j.}
\]
For \(1/(n+2)<\delta<1/(n+1)\), the safe-time set has exactly \(\varphi(n+1)\) open connected components. At the critical radius, the non-strict simultaneous solutions \(\|kt\|\ge1/(n+1)\) are precisely the \(\varphi(n+1)\) reduced fractions with denominator \(n+1\); the *strict* safe-time set in the definition of \(G_n\) is empty there.

## Assumptions and scope
The speeds are exactly \(\{1,2,\ldots,n\}\); time is taken modulo one with normalized Lebesgue measure. The same nonnegative threshold applies to each speed. All claims hold for every integer \(n\ge2\), and every real \(\delta\ge0\). No claim is made for arbitrary speed sets, unequal thresholds, or optimality among all sets of \(n\) speeds.

## Proof
For \(1\le k\le n\), failure of the strict inequality \(\|kt\|>\delta\) occurs in arcs centered at \(a/k\), with radius \(\delta/k\). Reducing \(a/k\) to \(u/q\) with \(q\mid k\), the arc of radius \(\delta/k\) is contained in the arc of radius \(\delta/q\) associated with speed \(q\). Thus their union equals the union of arcs centered at all reduced fractions \(u/q\) with \(q\le n\), each having radius \(\delta/q\).

Order these fractions cyclically as the Farey sequence of order \(n\), identifying \(0/1\) and \(1/1\). For consecutive reduced fractions \(a/q<b/r\), Farey adjacency yields \(br-aq=1\), hence a center-to-center distance of exactly \(1/(qr)\); also \(q+r>n\) and \(\gcd(q,r)=1\). Conversely, every ordered pair \((q,r)\) satisfying \(1\le q,r\le n\), \(\gcd(q,r)=1\) and \(q+r>n\) occurs as denominators of exactly one consecutive cyclic Farey pair. This is the standard Farey-neighbor parametrization (the cyclic wrap is treated as the last fraction to \(1/1\)).

For the range \(0\le\delta\le1/(n+1)\), no non-neighbor arc can create an additional obstruction within a putative gap. Indeed, for any two distinct reduced centers \(a/q<b/r\) in linear order, the separation is at least \(1/(qr)\), while the absolute difference of their radii is \(\delta|q-r|/(qr)<1/(qr)\), since \(|q-r|\le n-1\). Hence both the left endpoints and right endpoints of their associated arcs occur in the same order as the centers. Within a Farey gap, the furthest-reaching arc from the left is therefore the immediately preceding-center arc and the furthest-reaching from the right is the immediately succeeding-center arc. This also holds for the wrap gap after unwrapping at \(1\). For larger \(\delta\), the displayed formula and the safe-time measure both vanish: at \(\delta=1/(n+1)\) all consecutive-center arcs already cover the circle, and enlarging them cannot uncover a point.

The uncovered part of the intervening arc therefore has length
\[
\left(\frac1{qr}-\frac\delta q-\frac\delta r\right)_+=\frac{(1-\delta(q+r))_+}{qr}.
\]
The complement of the reduced-center arcs is the union of these uncovered portions. Summing their lengths proves the boxed profile. The argument also applies after all arcs overlap, because every summand then vanishes. Since \(q+r\ge n+1\), this happens for \(\delta\ge1/(n+1)\).

The slope of each summand changes at \(\delta=1/(q+r)\), with strictly positive jump \((q+r)/(qr)\). Hence breakpoints correspond exactly to attainable sums \(s=q+r\) with \(q,r\) coprime and \(q,r\le n\). Every odd \(s\in[n+1,2n-1]\) occurs via consecutive integers \(((s-1)/2,(s+1)/2)\). If \(s=2m\) and \(m\) is even, \((m-1,m+1)\) is an admissible coprime pair. If \(m\) is odd and \(s\le2n-4\), then \((m-2,m+2)\) is admissible: both entries are odd, and their gcd divides four. Finally, if \(n\) is even and \(s=2n-2\), the only possible pairs are \((n-2,n)\), \((n-1,n-1)\), and \((n,n-2)\), all noncoprime. If \(n\) is odd, the even-\(m\) construction works instead. This proves the exact breakpoint set, including all small boundaries.

All Farey gaps satisfy \(q+r\le2n\). At \(\delta=1/(2n)\), no positive-part truncation changes a summand, so
\[
G_n\!\left(\frac1{2n}\right)=\sum_{(q,r)}\frac1{qr}-\frac1{2n}\sum_{(q,r)}\left(\frac1q+\frac1r\right).
\]
The first sum is the total Farey gap length, namely one. Each reduced fraction of denominator \(q\) is endpoint of one gap on each side, so the second sum is \(2\sum_{q\le n}\varphi(q)/q\), with \(\varphi(1)=1\). This proves the exact benchmark identity. The classical Möbius-inversion estimate \(\sum_{q\le n}\varphi(q)/q=(6/\pi^2)n+O(\log n)\) proves the displayed limit.

For \(1/(n+2)\le\delta\le1/(n+1)\), all terms except those with \(q+r=n+1\) vanish (at the lower endpoint terms with \(q+r=n+2\) vanish exactly). Such ordered pairs are indexed by reduced residues \(j\bmod(n+1)\), and
\[
\sum_{\substack{1\le j\le n\\\gcd(j,n+1)=1}}\frac1{j(n+1-j)}
=\frac2{n+1}\sum_{\substack{1\le j\le n\\\gcd(j,n+1)=1}}\frac1j.
\]
This gives the final segment. For strictly interior thresholds in that segment each of the \(\varphi(n+1)\) contributing Farey gaps contains exactly one disjoint open safe interval. At \(\delta=1/(n+1)\), the only non-strict solutions are the touching points of those gaps. Between Farey neighbours \(a/q<b/r\) with \(q+r=n+1\), the touching point is their mediant \((a+b)/(q+r)\), reduced because \(br-aq=1\). As these Farey gaps vary, the mediants are exactly all \(\varphi(n+1)\) reduced fractions of denominator \(n+1\); no strict solution remains.

## Verification
Run `python3 verify.py` with the Python standard library. The verifier computes unsafe interval unions using *every unreduced speed* and exact rational arithmetic, independently of the denominator-pair formula. It matches the full profile at 480 rational parameter configurations for \(2\le n\le21\), checks all predicted slope-change index sets, tests the benchmark totient identity, and verifies the final-segment harmonic identity. Its expected final line is `CERTIFICATE_OK sizes=20 exact_profile_points=480 kink_classifications=20`. These finite tests do not prove the infinite-domain result; the argument above does.

## Relationship to prior work
Hu and Jing (arXiv:2610.23790v1, first public 2026-10-16) introduce the uncovered-time measure at threshold \(1/(2n)\) and establish a uniform positive lower bound for *arbitrary* speed sets. Their paper does not give an exact all-threshold profile for consecutive speeds or classify its changes of slope. Jensen (arXiv:2605.27941v1) develops mixed threshold regions and a two-speed integral, not this \(n\)-speed, all-threshold formula. Zhang (arXiv:2608.13599v1) treats components after removing one baseline speed at a single critical threshold, not the intact baseline profile at every threshold. Marklof (2024) studies fixed-width rational-window void statistics and limits for Farey fractions; the present safe intervals have denominator-dependent radii and the stated finite-\(n\) parity breakpoint distinction is not supplied by that work. The proof relies on the classical Farey-neighbor theorem; the resulting full profile is an elementary exact consequence of that structure. These comparisons do not establish exhaustive novelty across earlier Farey literature.

## Limitations
This is a classification for the consecutive-speed configuration only; it neither improves the universal Lonely Runner Conjecture threshold nor addresses general unequal speed sets. The main argument uses classical Farey facts. Earlier or implicit equivalent formulations in metric Diophantine approximation cannot be completely excluded. The accompanying computational checks are finite. Independent mathematical validation has not been performed.

## References
1. Xiyu Hu and Yifan Jing, *Near optimal gap in the Lonely Runner Conjecture*, arXiv:2610.23790v1 (submitted 2026-10-16), https://arxiv.org/abs/2610.23790 .
2. Alathea Jensen, *Mixed thresholds in the Lonely Runner Conjecture*, arXiv:2605.27941v1 (submitted 2026-05-27), https://arxiv.org/abs/2605.27941 .
3. Yuhan Zhang, *Single-speed modifications of the tight Lonely Runner instance: an effective bound and the complete classification for r = 2*, arXiv:2608.13599v1 (submitted 2026-08-01), https://arxiv.org/abs/2608.13599 .
4. Jens Marklof, *Smallest denominators*, Bulletin of the London Mathematical Society 56 (2024), 1920–1938, https://doi.org/10.1112/blms.13034 .
5. Classical Farey-neighbor theorem and the classical Möbius-inversion estimate for the summatory totient ratio, as used explicitly in the proof.
