# Sharp uniform branch discrepancy across a symmetric expanding Lorenz family

## Finding
For every real parameter \(1<\beta\le\sqrt{2}\), consider the discontinuous expanding map \(F_\beta:[0,1]\to[0,1]\) defined by
\[
F_\beta(u)=\begin{cases}\beta u+1-\beta/2,&0\le u<1/2,\\\beta(u-1/2),&1/2\le u\le1.\end{cases}
\]
Write \(\epsilon(u)=+1\) for \(u\ge1/2\), and \(\epsilon(u)=-1\) otherwise. Then for **every** \(u\in[0,1]\), every \(k\ge0\), and every integer \(n\ge0\),
\[
\left|\sum_{j=k}^{k+n-1}\epsilon(F_\beta^j(u))\right|\le2.
\]
The constant \(2\) is the best possible uniform bound, attained already at \(n=2\). For odd \(n\), the sum is necessarily \(\pm1\); for even \(n\), it belongs to \(\{-2,0,2\}\). Thus every length-\(n\) orbit segment has a number of right-branch visits differing from \(n/2\) by at most \(1\), independent of its starting position, the segment offset and the parameter in this range.

For every \(F_\beta\)-invariant Borel probability measure \(\mu\), \(\mu([1/2,1])=1/2\). Every periodic orbit has even least period and exactly equally many visits to either branch. Stronger finite-time information appears in the state-position enclosures in the proof.

## Assumptions and scope
The parameter \(\beta\) is real and satisfies \(1<\beta\le\sqrt2\). The value at the discontinuity \(1/2\) uses the right branch. The domain is the compact interval \([0,1]\), including both endpoints. We count the right branch as \(+1\) and the left branch as \(-1\), without averaging. No ergodicity, typicality or genericity is assumed. The assertion is uniform in every initial point and every finite time window.

At \(\beta=4/3\), the affine change \(u=3x-1\) conjugates the restriction to \([1/3,2/3]\) of the expanding two-branch map in Ghahremani–Kelmendi–Ouaknine, Example 4.1, to \(F_{4/3}\); it preserves the left/right cut. Our invariant-measure and periodic-orbit statements concern the compact normalized map, not an assertion about points outside the source example's invariant interval.

## Proof
Put
\[
L=1-\beta/2,\quad R=\beta/2,\quad s=\beta(\beta-1)/2,\quad d=1-s.
\]
The assumed range gives \(0<s<1/2\), \(1/2<d<1\), and
\[
\beta(d-1/2)\ge L,\qquad L+\beta s\le R.
\]
Indeed, both inequalities reduce to \((\beta-1)(1-\beta^2/2)\ge0\). The branch images preserve \([0,1]\).

For a trajectory beginning at \(u\), set \(B_n=\sum_{j=0}^{n-1}\epsilon(F_\beta^j(u))\) and \(u_n=F_\beta^n(u)\). We prove inductively that its \((n,B_n,u_n)\) belongs to precisely one of the following *permitted* states:

* for even \(n\), \(B_n=0\) with \(u_n\in[0,1]\), or \(B_n=-2\) with \(u_n\in[d,1]\), or \(B_n=2\) with \(u_n\in[0,s]\);
* for odd \(n\), \(B_n=-1\) with \(u_n\in[L,1]\), or \(B_n=1\) with \(u_n\in[0,R]\).

At \(n=0\), \(B_0=0\) and the first even state applies. The full list of transitions follows by splitting the current position at the branch boundary:

1. From even \(B=0\), left points map into \([L,1]\), yielding odd \(B=-1\); right points map into \([0,R]\), yielding odd \(B=1\).
2. From even \(B=-2\), \(u\in[d,1]\subset(1/2,1]\). Thus only the right branch applies and maps into \([\beta(d-1/2),R]\subset[L,1]\), yielding odd \(B=-1\).
3. From even \(B=2\), \(u\in[0,s]\subset[0,1/2)\). Only the left branch applies and maps into \([L,L+\beta s]\subset[0,R]\), yielding odd \(B=1\).
4. From odd \(B=-1\), the left part \([L,1/2)\) maps into \([L(\beta+1),1)=[d,1)\), yielding even \(B=-2\); the right part \([1/2,1]\) maps into \([0,R]\subset[0,1]\), yielding even \(B=0\).
5. From odd \(B=1\), the left part \([0,1/2)\) maps into \([L,1)\subset[0,1]\), yielding even \(B=0\); the right part \([1/2,R]\) maps into \([0,s]\), yielding even \(B=2\).

The identity \(L(\beta+1)=d\) follows from the definitions. These five cases exhaust every allowed state and branch, so induction proves the state-position enclosures for arbitrarily long trajectories. In particular, \(|B_n|\le2\) for all \(n\). Starting at \(u=0\), the first two branches are both left because \(F_\beta(0)=L<1/2\), so \(B_2=-2\); starting at \(u=1\), both are right because \(F_\beta(1)=R>1/2\), so \(B_2=2\). This proves sharpness. Any window beginning at time \(k\) is a prefix from \(F_\beta^k(u)\in[0,1]\), proving the window statement.

Finally, if \(\mu\) is invariant, then \(\int B_n\,d\mu=n(2\mu([1/2,1])-1)\), while \(|\int B_n\,d\mu|\le2\). Division by \(n\to\infty\) gives \(\mu([1/2,1])=1/2\). Apply this conclusion to the uniform measure on any finite periodic orbit to show that its right-visit count equals half its period, hence the least period is even. No invariant-measure existence theorem is needed for these implications.

## Verification
A standalone `CHECK.py` replays the five permitted transitions with exact rational interval arithmetic for representative parameters and checks exact rational orbits; it reports success when the specified inclusions hold. The continuum conclusion comes from the two displayed algebraic inequalities plus the finite-case induction, **not** from testing finitely many parameters. All boundary conventions and the sharpness witnesses are explicit.

## Relationship to prior work
Ghahremani, Kelmendi and Ouaknine (2023), Section 4 and Example 4.1, use the parameter \(4/3\) map to construct a non-dense infinite orbit. The present theorem describes every finite branch-count window on its invariant core and extends the discrepancy estimate to an entire real parameter interval. Cui and Ding (2009), Main Theorem and Remark 1(3), invoke Parry's periodic-renormalization classification for symmetric expanding Lorenz maps and identify this parameter family as part of a known phase-locking regime. Thus **qualitative phase locking and the relevant parameter range are not new**. The contribution claimed here is the explicit universal sharp constant, the finite-state spatial enclosures that certify it for every initial point, and the resulting exact finite-time counting statement, not the general existence of periodic renormalization or the qualitative mean frequency.

## Limitations
The theorem does not determine whether the bound remains true outside \((1,\sqrt2]\), nor does it classify all invariant probability measures, their densities, symbolic languages, or individual orbit closures. The stationarity and cycle consequences could be derivable by specializing earlier renormalization work; priority risk for those qualitative consequences is acknowledged, and they are not independently claimed as new. The interval certificate establishes the quantitative theorem directly; no independent external mathematical audit has been performed.

## References
1. F. Ghahremani, E. Kelmendi, J. Ouaknine, *Reachability in Injective Piecewise Affine Maps*, arXiv:2301.09752v1 (first public 2023-01-23), Section 4, Example 4.1. Full-text version inspected: arXiv:2301.09752v2, https://arxiv.org/html/2301.09752v2.
2. H.-F. Cui, Y.-M. Ding, *Renormalization and conjugacy of piecewise linear Lorenz maps*, arXiv:0906.3131v3 (2009), Main Theorem and Remark 1(3), https://arxiv.org/html/0906.3131v3.
