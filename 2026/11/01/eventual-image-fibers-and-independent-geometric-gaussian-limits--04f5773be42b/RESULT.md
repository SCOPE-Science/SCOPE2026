# Eventual-image fibers and independent geometric–Gaussian limits in directed-path weak endomorphisms

## Finding
For every integer \(n\ge1\), consider the monoid \(W_n\) of all full maps \(f:[n]\to[n]\), where \([n]=\{1,\ldots,n\}\), satisfying \(f(i+1)-f(i)\in\{0,1\}\) for \(1\le i<n\). This is the weak-endomorphism monoid of the directed path, also denoted \(IO_n\) in the literature.

Every \(f\in W_n\) has a nonempty consecutive fixed-point set \(\operatorname{Fix}(f)=[a,b]\cap\mathbb Z\), and its eventual idempotent is exactly the interval clamp
\[
 f^n=e_{a,b},\qquad e_{a,b}(i)=\max\{a,\min\{i,b\}\}.
\]
Let \(R=b-a+1\) denote the rank of the eventual image and \(M=|\operatorname{im}f|\) the original image rank. **The complete joint fiber of the eventual-power map**, refined by \(M\), is
\[
 \#\{f\in W_n:\operatorname{Fix}(f)=[a,b],\ M=m\}
 =\binom{d_{n,a,b}}{m-(b-a+1)},\qquad
 d_{n,a,b}=\max(0,a-2)+\max(0,n-b-1),
\]
where out-of-range binomial coefficients vanish. The unconditional fiber has size \(2^{d_{n,a,b}}\).

For \(n\ge2\) the bivariate polynomial is
\[
 J_n(u,v):=\sum_{f\in W_n}u^{R(f)}v^{M(f)-1}
 =u^n v^{n-1}+2\sum_{r=1}^{n-1}u^r v^{r-1}(1+v)^{n-r-1}
 +\sum_{r=1}^{n-2}(n-r-1)u^r v^{r-1}(1+v)^{n-r-2}.
\]
For \(n=1\), the polynomial is \(J_1(u,v)=u\).

For \(1\le r<n\), summing the fibers gives
\[
 N_{n,r}:=\#\{f:R(f)=r\}=(n-r+3)2^{n-r-2},\quad N_{n,n}=1,
\]
and \(|W_n|=(n+1)2^{n-2}\) for \(n\ge2\). Hence
\[
 \Pr(R=r)=\frac{n-r+3}{n+1}2^{-r}\quad(1\le r<n),\qquad
 \Pr(R=n)=\frac4{(n+1)2^n},\qquad \mathbb E R=\frac{2n}{n+1}.
\]
Writing \(A=a\) for the first fixed point and sampling \(f\) uniformly from \(W_n\), we additionally have the joint limit
\[
 \left(R,\frac{A-1}{n-1},\frac{2(M-(n+1)/2)}{\sqrt n}\right)
 \ \Longrightarrow\ (G,U,Z),
\]
where \(G,U,Z\) are *mutually independent*, \(\Pr(G=r)=2^{-r}\) for every integer \(r\ge1\), \(U\) is uniform on \([0,1]\), and \(Z\) is standard normal.

## Assumptions and scope
The maps are full, order-preserving and weakly adjacency-preserving on the directed path; there is no orientation reversal. Function powers are composition. The eventual image is \(\bigcap_{j\ge1}\operatorname{im}(f^j)\), which here equals the fixed-point set. The finite counting identities hold for all positive integers \(n\), with the stated special case at \(n=1\). The probabilistic theorem concerns the limit \(n\to\infty\), uniform choice among **all** elements of \(W_n\). The original image-rank marginal and the total number of elements are established earlier facts, included for context and normalization, not asserted as independent novelties.

## Proof
**1. Fixed interval and stabilization.** Set \(\delta_i=f(i)-i\). Then \(\delta_{i+1}-\delta_i\in\{-1,0\}\), so \(\delta_i\) is nonincreasing. Also \(\delta_1\ge0\) and \(\delta_n\le0\), and every integer value between is attained, so the zero set is a nonempty integer interval \([a,b]\). For \(i<a\), \(f(i)>i\) and monotonicity gives \(f(i)\le f(a)=a\); hence forward iterates increase to \(a\). For \(i>b\), iterates decrease to \(b\). Each strict move advances by at least one, so at most \(n-1\) moves occur. Thus \(f^n=e_{a,b}\) pointwise. In particular, the eventual-power map from \(W_n\) to its idempotents is well defined and its fibers are indexed by nonempty intervals.

**2. Exact fibers.** For fixed \([a,b]\), write \(\varepsilon_i=f(i+1)-f(i)\in\{0,1\}\). Fixing every \(i\in[a,b]\) forces \(\varepsilon_i=1\) for \(a\le i<b\); positivity just outside the fixed interval forces \(\varepsilon_{a-1}=0\) if \(a>1\) and \(\varepsilon_b=0\) if \(b<n\). All the other \(d_{n,a,b}\) increments, those with \(i\le a-2\) or \(i\ge b+1\), are free binary choices. The value \(f(a)=a\) determines the starting value uniquely and guarantees \(1\le f(i)\le n\) everywhere, because there are at most \(a-2\) upward steps before \(a\) and at most \(n-b-1\) after \(b\). Every choice has exactly \([a,b]\) as its fixed set: the zero boundary increments rule out additional zeros of \(\delta_i\). Since the image of an element of \(W_n\) is an interval and its size is one plus the total number of upward increments, we have \(M=R+\#\{\text{free increments equal to one}\}\). This establishes the binomial fiber formula without enumeration assumptions.

**3. Summing locations.** If \(r<n\), let \(t=n-r\). The two intervals touching one boundary each contribute \(2^{t-1}\) maps, while the \(t-1\) remaining intervals each contribute \(2^{t-2}\) (there are no such intervals when \(t=1\)). Their weighted binomial generating polynomials are respectively \(v^{r-1}(1+v)^{t-1}\) and \(v^{r-1}(1+v)^{t-2}\). The unique full fixed interval gives \(u^nv^{n-1}\). This proves \(J_n\) and \(N_{n,r}\), including \(t=1\). Summing the \(N_{n,r}\) yields the established normalization \((n+1)2^{n-2}\). Elementary finite-geometric sums give \(\mathbb E R=2n/(n+1)\). The marginal initial-image mean also satisfies \(\mathbb E M=n/2+1/(n+1)\), consistent with established image-rank enumeration.

**4. Independence of the three scales.** For each fixed integer \(r\ge1\), the rank mass above tends to \(2^{-r}\). Uniformly in \(n\ge2\) and admissible \(r\), the bound \(\Pr(R=r)\le(4/3)2^{-r}\) holds, so the ranks are tight. Conditional on \(R=r<n\), each interior location of \(a\) has the same weight, and the two boundary locations each have twice that weight; dividing by \(n-1\) yields the uniform limiting location distribution. Conditional on any fixed \(r\) and any location, \(M=r+B\), where \(B\) is binomial with success probability \(1/2\) and with \(n-r-1\) trials for a boundary location or \(n-r-2\) for an interior one. The centered, \(\sqrt n\)-scaled binomial converges to a standard normal under the normalization shown, uniformly over these two possible trial counts; fixed shifts are negligible. For a fixed \(r\), products of bounded continuous tests of location and normalized image rank therefore converge to the corresponding product of uniform and Gaussian expectations. Tightness in \(r\) permits passage from fixed \(r\) to the full joint distribution, proving mutual independence of \(G,U,Z\).

## Verification
A standard-library Python program `verify_weak_path_attractor.py` enumerates all binary-increment maps with admissible initial values for \(1\le n\le13\), computes \(f^n\) by direct pointwise iteration and independently checks stabilization, identifies \([a,b]\) directly from fixed points, counts actual initial-image ranks, then compares the full three-parameter count against the closed binomial coefficient. It also checks the exact rank marginal and total monoid cardinality in every tested case. All comparisons passed, including all 28,672 elements when \(n=13\). The finite program is a reproducibility check, not the proof for unbounded \(n\).

## Relationship to prior work
Fernandes and Paulista, arXiv:2112.13427v1 (public December 26, 2021), Proposition 1.5, establish equivalence with order-preserving maps with interval image. Their Theorem 1.6 determines the cardinality by **initial** image rank; Corollary 1.9 counts idempotents, one per interval. Fernandes, arXiv:2407.05084v1 (public July 6, 2024), studies the same monoid \(IO_n\), especially presentations and the order-decreasing submonoid. Neither inspected primary discussion supplies the **fibers of the eventual-power map indexed by fixed intervals**, the joint initial-versus-eventual rank polynomial, or the mutually independent geometric/location/Gaussian limit. These are the assessed contributions; previously established one-rank counts and monoid cardinalities are not claimed as new. Laradji's work on fixed points of order-preserving **partial** transformations addresses a larger, distinct monoid; complete full-text exclusion of a possible reduction was not available.

## Limitations
All conclusions concern the directed-path weak-endomorphism monoid, not the full order-preserving transformation monoid nor partial maps. The Gaussian/local-uniform asymptotics require uniform sampling and growing path length. The novelty comparison is limited to available primary material and search results; a broader transformation-semigroup iterate-enumeration theorem could implicitly subsume this result. An inaccessible full text on fixed points of partial transformations remains a specific unresolved literature-priority risk. No independent mathematical audit or global priority certification is asserted.

## References
1. V. H. Fernandes and T. Paulista, *On the Rank of Monoids of Endomorphisms of a Finite Directed Path*, arXiv:2112.13427v1 (first public December 26, 2021), https://arxiv.org/abs/2112.13427.
2. V. H. Fernandes, *On the monoid of order-preserving transformations of a finite chain whose ranges are intervals*, arXiv:2407.05084v1 (first public July 6, 2024), https://arxiv.org/abs/2407.05084.
3. A. Laradji, *Fixed points of order-preserving transformations*, Journal of Algebra and Its Applications, DOI:10.1142/S0219498822500827; partial-transformation context, full paper not inspected.
