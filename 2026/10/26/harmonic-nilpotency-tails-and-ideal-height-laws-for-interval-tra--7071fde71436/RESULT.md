# Harmonic nilpotency tails and ideal-height laws for interval-translation inverse monoids

## Finding
For every integer \(N\ge1\), choose uniformly from the nonzero nilpotents of the consecutive-diagonal rook monoid \(M_{N+1}\), and denote the least zero power by \(\nu_N\). For every integer \(j\ge1\),
\[
\Pr(\nu_N>j)=\frac{3}{N(N+1)(N+2)}\sum_{d=1}^{\lfloor N/j\rfloor}(N-jd+1)(N-jd+2).
\]
For each fixed \(j\ge1\), this tends to \(1/j\); moreover \(\mathbb E\nu_N=\log N+O(1)\).

There is an exact continuous counterpart. Let \(\overline M_n\) be the real-coordinate interval-translation inverse monoid, \(n\ge2\), with normalized three-dimensional Lebesgue volume on its nonzero parameter body (the isolated zero has probability zero). Almost every element is nilpotent. More precisely, the continuous ratio \(R=h/|d|\) of segment height to absolute translation magnitude satisfies \(\Pr(R>r)=1/(1+r)\) for every real \(r\ge0\), a Pareto-II law with density \(1/(1+r)^2\). Hence its least zero power \(\nu\) obeys, for every integer \(j\ge1\),
\[
\Pr(\nu>j)=\frac1j,\qquad
\Pr(\nu=j)=\frac1{j(j-1)}\quad(j\ge2).
\]
In particular each sampled element has finite nilpotency index almost surely, but \(\mathbb E\nu=+\infty\). All nonnegative moments of order \(\alpha<1\) are finite and those of order \(\alpha\ge1\) are infinite.

The tail can also be resolved along the natural chain of principal ideals. Let \(I_H\subset\overline M_n\) consist of zero and elements whose segment height \(h\) is at most \(H\), where \(0<H\le n-1\). Put \(u=H/(n-1)\). Under normalized Lebesgue volume on the positive-volume body of \(I_H\), for every integer \(j\ge2\),
\[
\Pr(\nu>j\mid I_H)=\frac{3}{1-(1-u)^3}
\begin{cases}
\displaystyle\frac{u^2}{j-1}-\frac{(2j-1)u^3}{3(j-1)^2},&0<u\le\frac{j-1}{j},\\[4pt]
\displaystyle\frac{1/j-(1-u)^3}{3},&\frac{j-1}{j}\le u\le1.
\end{cases}
\]
At the shared boundary both expressions agree. For every fixed \(u\in(0,1]\), this tail is asymptotic to \(c(u)/j\), where
\[
c(u)=\frac{3u^2-2u^3}{1-(1-u)^3}>0.
\]
Thus restriction to any nonzero-height principal ideal still leaves an infinite mean least zero power. The above formulas determine one integrated nilpotency-index distribution, not separate claims about unrelated structures.

## Assumptions and scope
The integer monoid \(M_{N+1}\) consists of an isolated zero and admissible integer triples \((k,d,m)\) satisfying
\[
1-\min(0,d)\le k\le m\le N+1-\max(0,d).
\]
Its nonzero elements represent single uninterrupted blocks on a diagonal of a rook matrix; the triples with \(d\ne0\) are exactly the nonzero nilpotents. Multiplication of nonzero triples is
\[
(k,d,m)(k',d',m')=
\begin{cases}
(\max(k,k'-d),\ d+d',\ \min(m,m'-d)),&\max(k,k'-d)\le\min(m,m'-d),\\
0,&\text{otherwise}.
\end{cases}
\]
The real monoid \(\overline M_n\) uses the same inequalities and multiplication with real parameters. Normalized volume is specifically ordinary Euclidean Lebesgue measure in the coordinates \((k,d,m)\), divided by the body's total volume; no claim of Haar invariance or invariance under arbitrary semigroup automorphisms is made. The zero and the \(d=0\) idempotent sheet have zero volume. The normalized affine isomorphisms between real parameter bodies preserve this probability law. The principal ideals \(I_H\) are the height cuts established in the foundational work. The ideal at \(H=0\) has zero three-dimensional measure and is excluded from the conditional-volume assertion.

## Proof
Write \(h=m-k\ge0\) and \(a=|d|\). Iterating the multiplication rule yields that a nonzero triple with \(a>0\) has a nonzero \(j\)-th power if and only if \(h\ge(j-1)a\). Equivalently, its least zero power is \(2+\lfloor h/a\rfloor\), including all integer equality boundaries. This power criterion also follows directly by induction: each further factor shortens the allowed interval by exactly \(a\), until the lower endpoint exceeds the upper.

For the finite formula set \(n=N+1\). For either sign of an integer shift \(d\ge1\), a segment of height \(h\), where \(0\le h\le N-d\), has exactly \(N-d-h+1\) admissible placements. Consequently the total number of nonzero nilpotents is
\[
2\sum_{d=1}^N\sum_{h=0}^{N-d}(N-d-h+1)=\frac{N(N+1)(N+2)}3.
\]
The event \(\nu_N>j\) requires \(h\ge(j-1)d\), so necessarily \(d\le N/j\). For such a shift, the sum of the placement counts over admissible heights is \((N-jd+1)(N-jd+2)/2\). Including both signs proves the finite tail formula.

To take the limit, put \(S_{N,j}=\sum_{d=1}^{\lfloor N/j\rfloor}(N-jd+1)(N-jd+2)\). The summand is nonnegative and decreasing on the relevant interval. Its integral from \(0\) to \(N/j\) is
\[
\frac1j\left(\frac{N^3}{3}+\frac{3N^2}{2}+2N\right).
\]
The difference between this integral and the right-endpoint sum is between zero and \((N+1)(N+2)\). Thus \(\Pr(\nu_N>j)=1/j+O(1/N)\) uniformly for \(1\le j\le N\). Since \(2\le\nu_N\le N+1\), the tail-sum identity gives \(\mathbb E\nu_N=1+\sum_{j=1}^N\Pr(\nu_N>j)=\log N+O(1)\).

For the real model set \(L=n-1\). On each sign of \(d\), the changes of variables from \((k,d,m)\) to \((k,a,h)\) have absolute Jacobian one, with \(0\le a\le L\), \(0\le h\le L-a\), and a placement interval for \(k\) of length \(L-a-h\). Total parameter volume is therefore
\[
V=2\int_0^L\int_0^{L-a}(L-a-h)\,dh\,da=\frac{L^3}{3}.
\]
More generally, for every real \(r\ge0\), imposing \(h\ge ra\) leaves volume \(L^3/[3(1+r)]\), by the same integration with upper shift bound \(L/(1+r)\). Therefore \(\Pr(R>r)=1/(1+r)\); differentiating its distribution function on \(r>0\) yields the claimed density. In particular, for an integer \(j\ge1\), the power condition \(h\ge(j-1)a\) leaves volume
\[
V_j=2\int_0^{L/j}\int_{(j-1)a}^{L-a}(L-a-h)\,dh\,da=\frac{L^3}{3j}.
\]
Dividing proves the harmonic tail. Subtracting adjacent tails gives the probability mass formula, and the tail-sum criterion gives infinite first moment and the stated moment threshold.

Finally restrict to \(0\le h\le H=uL\). Rescale \(L=1\). Integrating over shift magnitude first, the slice density at height \(h\) for the unrestricted ideal is \((1-h)^2\), so its total volume is
\[
V(H)=\int_0^u(1-h)^2\,dh=\frac{1-(1-u)^3}{3}.
\]
For \(j\ge2\), the extra requirement \(h\ge(j-1)a\) makes the shift range \(0\le a\le\min\{h/(j-1),1-h\}\). Integrating \(2(1-h-a)\) over this interval and then over \(0\le h\le u\), splitting at \(h=(j-1)/j\), gives respectively
\[
\frac{u^2}{j-1}-\frac{(2j-1)u^3}{3(j-1)^2}
\quad\text{and}\quad
\frac{1/j-(1-u)^3}{3}.
\]
Dividing by \(V(H)\) proves the ideal formulas. For fixed \(0<u<1\), the first branch holds for all sufficiently large \(j\), and expansion gives the positive constant \(c(u)\). For \(u=1\), the unrestricted exact tail gives the same conclusion with \(c(1)=1\).

## Verification
The self-contained program `verify.py` constructs admissible integer triples, multiplies them repeatedly to determine least zero powers independently of the asserted closed formula, and checks all finite tail coefficients for \(1\le N\le18\). It also checks the two ideal-volume antiderivatives using exact rational arithmetic on numerous parameter grids, together with the unrestricted harmonic law. Run `python3 verify.py` using Python's standard library. The observed result for the saved program was `VERIFY_OK: 13367 exact structural, finite enumeration, and rational-integration checks`. Finite testing and rational identities are supplementary; the proof above establishes the quantified infinite claims.

## Relationship to prior work
Fikioris and Fikioris introduced the finite consecutive-diagonal rook monoids, their power formulas, nilpotency indices, and total counts in *A subsemigroup of the rook monoid* (arXiv:2111.01863, first posted November 2, 2021). Their real-parameter extension *An extension to “A subsemigroup of the rook monoid”* (arXiv:2302.09496, first posted February 19, 2023) establishes the real inverse monoid, the pointwise least-zero-power formula, the affine monoid isomorphisms and the principal ideal height classification. These foundations are explicitly used here. Neither inspected exposition asserts the exact normalized-volume law, the ideal-height conditional tails, or the finite rank-free nilpotency-index tail census given above. The elementary pointwise formula alone is not asserted to be new. There remains a possibility that the same distribution has been derived elsewhere under interval-translation or partial-injection terminology.

## Limitations
The uniform measure is attached to the indicated finite counting measure or real three-dimensional coordinate volume, not to all conceivable random models of the monoid. The isolated zero and the measure-zero idempotents have no effect on real-volume statistics; \(H=0\) is not included in the conditional-volume theorem. There is no claim that normalized Lebesgue volume is multiplicatively invariant or canonical among all probability measures. The discrete asymptotic is for uniformly chosen nonzero nilpotents, not for all elements conditioned on their degree. Source priority is assessed against the literature actually inspected; independent validation has not occurred.

## References
1. G. Fikioris and G. Fikioris, *A subsemigroup of the rook monoid*, arXiv:2111.01863 (initial public version November 2, 2021), subsequently Semigroup Forum 105 (2022), 191–216.
2. G. Fikioris and G. Fikioris, *An extension to “A subsemigroup of the rook monoid”*, arXiv:2302.09496 (initial public version February 19, 2023), subsequently Semigroup Forum 107 (2023), 637–650; DOI:10.1007/s00233-023-10393-8.
