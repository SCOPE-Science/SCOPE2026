# Maximal-depth nilpotents of oriented partial-injection monoids and Farey denominators

## Finding
Let \(X_n=\{0,1,\ldots,n-1\}\) with its usual circular order. For an injective partial transformation \(\alpha:D\to X_n\), call it **orientation-preserving** if the images of the points of \(D\), read in increasing order, form a cyclically increasing sequence; call it **orientation-reversing** if they form a cyclically decreasing sequence. Write \(\mathcal{POPI}_n\) for the preserving partial-injection monoid and \(\mathcal{PORI}_n\) for their preserving-or-reversing union. Composition is ordinary partial composition; zero is the empty map.

**Theorem.** For every integer \(n\ge4\), writing \(\nu_n^+(n)\) and \(\nu_n^{\pm}(n)\) for the number of elements whose least positive zero power is exactly \(n\),
\[
\nu_n^+(n)=n\sum_{k=1}^{n-1}\varphi(k),\qquad
\nu_n^{\pm}(n)=n\left(2+\sum_{k=1}^{n-1}\varphi(k)\right).
\]
All the elements counted have rank \(n-1\); the orientation-reversing-but-not-preserving contribution is exactly \(2n\). They are naturally indexed, modulo rotation of the underlying \(n\)-cycle, by Farey gaps of order \(n-1\) for the preserving part and by two alternating parity words for the reversing part. In particular,
\[
\nu_n^+(n)=\frac{3n^3}{\pi^2}+O(n^2\log n),\qquad
\nu_n^{\pm}(n)=\frac{3n^3}{\pi^2}+O(n^2\log n).
\]
The standard term \(\sum_{k=1}^{m}\varphi(k)\) counts Farey gaps; its occurrence alone is not claimed as a new enumerative sequence.

## Assumptions and scope
All transformations are injective **partial** maps. A nilpotent has no cycles in its directed functional graph. Its nilpotency index is the smallest positive \(h\) for which \(\alpha^h\) is empty. For the formulas with disjoint preserving and reversing parts, \(n\ge4\) is essential: an injective map of domain size two is simultaneously preserving and reversing. The maximum possible index is \(n\) and occurs on a single chain of \(n\) distinct vertices, with successive arrows \(x_i\mapsto x_{i+1}\) for \(0\le i\le n-2\).

## Proof
**1. Reduction to circular time orders.** A partial injection decomposes into disjoint directed chains and cycles. Nilpotency excludes cycles. With \(n\) vertices its index is at most \(n\); equality forces precisely one chain \((x_0,x_1,\ldots,x_{n-1})\). Put \(m=n-1\), and label vertex \(x_i\) by its time index \(i\). The physical clockwise arrangement determines one circular permutation of \(\{0,\ldots,m\}\); write \(g\) for its clockwise-successor permutation. It is an \((m+1)\)-cycle. The arrow map on labels sends \(i\) to \(i+1\) on \(\{0,\ldots,m-1\}\). Exactly \(n\) distinct placements on the labeled physical circle realize each circular time order.

**2. Preserving successor equation.** For \(S\subseteq\{0,\ldots,m\}\), denote by \(g_S\) the clockwise successor after removing the labels outside \(S\). The map \(i\mapsto i+1\) from \(P=\{0,\ldots,m-1\}\) to \(Q=\{1,\ldots,m\}\) preserves cyclic order exactly when
\[
 g_Q(i+1)=g_P(i)+1\quad (0\le i<m).
\]
Let \(b=g(0)\) and \(d=g^{-1}(0)\), both nonzero. The only exceptional successor comparisons occur immediately before the omitted label \(m\) in \(P\) and the omitted label \(0\) in \(Q\). Away from them the equation reads \(g(i+1)=g(i)+1\). Starting at \(g(0)=b\), tracing to those two exceptions gives \(b+d>m\) and forces the following complete successor map:
\[
 g(i)=\begin{cases}
 i+b,&0\le i\le m-b,\\
 i+b-d,&m-b<i<d,\\
 i-d,&d\le i\le m.
 \end{cases}
\]
The displayed intervals can be empty. Conversely, for any \(1\le b,d\le m\) with \(b+d>m\), the map displayed is a permutation and directly satisfies the cyclic-order successor equation. Thus the only remaining condition on \((b,d)\) is that \(g\) be one cycle.

**3. The coprimality criterion.** Let \(L=b+d\). The displayed permutation \(g\) is exactly the first-return permutation of the modular rotation \(u\mapsto u+b\pmod L\) on the consecutive subset \(\{0,\ldots,m\}\). Indeed, one rotation step either remains in the subset, giving the first or third branch, or lands above \(m\), in which case the next step returns and gives the middle branch. This rotation has \(\gcd(b,d)\) cycles; each meets the consecutive subset because its size \(m+1\) exceeds \(\gcd(b,d)\). Therefore the first-return map is an \((m+1)\)-cycle if and only if \(\gcd(b,d)=1\).

Coprime denominator pairs satisfying \(1\le b,d\le m<b+d\) are exactly the pairs of denominators of adjacent fractions in the Farey sequence of order \(m\). One direction follows from the Farey-neighbor determinant-one relation and its no-mediant criterion; the converse follows from the unique positive modular solution to that determinant equation for coprime \((b,d)\). The number of Farey gaps is the classical quantity \(\sum_{k=1}^m\varphi(k)\). Consequently the number of preserving circular time orders is this sum, and the labeled placements number \(n\sum_{k=1}^{n-1}\varphi(k)\). The recurrence for \(g\) is also precisely the classical Sós-permutation recurrence, up to inversion of its order-of-positions convention; its enumeration is explicitly credited to the earlier literature.

**4. Reversing circular time orders.** A cyclic-order-reversing bijection between the two finite subsets \(P\) and \(Q\) extends by interpolation on complementary arcs to an orientation-reversing homeomorphism \(h\) of the circle, carrying each physical point \(x_i\) to \(x_{i+1}\), for \(0\le i<m\). Such a homeomorphism has exactly two fixed points. It exchanges the two complementary open arcs, and its second iterate restricts to an increasing homeomorphism of each arc. Since the \(x_i\) are distinct for \(0\le i\le m\), its even-indexed orbit points are strictly ordered in one arc and its odd-indexed points are strictly ordered in the other, with the two orders opposite. Up to choosing the physical clockwise direction, only two time-order words are possible:
\[
(0,2,4,\ldots,\text{largest even},\text{largest odd},\ldots,3,1)
\quad\text{or}\quad
(0,1,3,\ldots,\text{largest odd},\text{largest even},\ldots,4,2).
\]
Here indices stop at \(m\). Both words directly satisfy the anti-cyclic image condition for the path map, and each has \(n\) distinct labeled circular placements. Therefore exactly \(2n\) reversing maximal-depth nilpotents exist.

For \(n\ge4\), the domain of each path map has at least three points; a cyclically increasing image triple cannot simultaneously be cyclically decreasing. Thus the preserving and reversing sets are disjoint in this stratum. Adding yields the second displayed formula. Finally the classical summatory-totient asymptotic \(\sum_{k\le m}\varphi(k)=3m^2/\pi^2+O(m\log m)\) gives the stated asymptotics.

## Verification
The included standalone `checker.py` computes each maximal-index nilpotent independently by enumerating all \(n!\) directed paths for \(2\le n\le8\), then testing the original cyclic/anti-cyclic image definitions. Its preserving counts are \(2,6,16,30,60,84,144\) for \(n=2,\ldots,8\), while its reversing counts are \(2,6,8,10,12,14,16\). For \(n=4,\ldots,8\), their union has sizes \(24,40,72,98,160\), agreeing with the theorem. Separately the checker constructs every successor permutation from every permissible \((b,d)\) up through \(m=30\), confirms its exact cycle count equals \(\gcd(b,d)\), and compares the resulting coprime-pair count with the summatory totient. Execute `python checker.py` using Python 3 standard library. Finite tests are corroborative and do not replace the preceding proof.

## Relationship to prior work
Li and Fernandes (2022) establish the standard families of preserving and oriented partial permutation monoids and study **endomorphisms of those monoids**; the inspected full paper does not enumerate their maximal-index nilpotent elements. Bockting-Conrad, Kashina, Petersen and Tenner (2020) survey and develop Sós permutations and their established Farey correspondence and recurrence, in particular the already-known \(\sum\varphi\) count. The preserving branch is therefore a semigroup interpretation of a known combinatorial class, not a new Sós enumeration. The contribution assessed here is the maximal nilpotency-index interpretation **together with** the exact reversing contribution and union formula in the naturally enlarged oriented inverse monoid.

## Limitations
No enumeration is asserted for nilpotents of smaller index or smaller rank. This result does not determine the full nilpotent polynomial or any Green-theoretic classification. Direct comparisons with all early orientation-preserving transformation literature could not be completed; an equivalent consequence of an earlier general semigroup theorem remains a priority risk. The asymptotic error uses a standard number-theoretic estimate, not a new estimate. Independent scientific audit has not been performed.

## References
1. D. B. Li and V. H. Fernandes, *Endomorphisms of semigroups of oriented transformations*, arXiv:2207.12823v1, first public 2022-07-26, full text https://arxiv.org/html/2207.12823v1. Primary MSC 20M10, 20M20.
2. S. Bockting-Conrad, Y. Kashina, T. K. Petersen, and B. E. Tenner, *Sós Permutations*, arXiv:2007.01132v1, first public 2020-07-02, full text https://arxiv.org/html/2007.01132v1; in particular the Farey correspondence and three-branch recurrence, attributed therein to Surányi and Sós.
3. Classical Farey-neighbor and summatory-Euler-totient results, as discussed in reference 2; these ingredients are credited background.
