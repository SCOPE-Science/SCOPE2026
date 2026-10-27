# Commuting idempotent bands and an all-arity product-rank law for monotone contractions

## Finding
For \(n\ge1\), let \(\mathcal C_n\) be the monoid of all maps \(f:[n]\to[n]\) satisfying \(0\le f(i+1)-f(i)\le1\) for \(1\le i<n\). Let \(\mathcal E_n\) be its set of idempotents. Each idempotent is uniquely an interval retraction
\[
 e_{[a,b]}(x)=\min\{b,\max\{a,x\}\},\qquad1\le a\le b\le n.
\]
Two such idempotents commute exactly when their image intervals intersect. If they do, their product is the retraction onto that intersection. Consequently the maximal commutative subbands of \(\mathcal E_n\) are precisely the \(n\) interval stars
\[
 \mathcal S_i=\{e_{[a,b]}:a\le i\le b\},\qquad
 |\mathcal S_i|=i(n-i+1),\quad 1\le i\le n.
\]

For integers \(m,n\ge1\), let \(c_{n,k}^{(m)}\), for \(1\le k\le n\), count ordered \(m\)-tuples of pairwise commuting members of \(\mathcal E_n\) whose common product has image cardinality \(k\). Put \(\Delta_m(r)=r^m-(r-1)^m\) for \(r\ge1\). Then
\[
 c_{n,k}^{(m)}=\sum_{u=1}^{n-k+1}\Delta_m(u)\Delta_m(n-k-u+2).
\]
Define the ordinary Eulerian polynomial \(A_m(t)\) by \(\sum_{r\ge1}\Delta_m(r)t^{r-1}=A_m(t)/(1-t)^m\). The complete product-rank generating function and total-count series are
\[
 \sum_{n\ge1}\sum_{k=1}^{n}c_{n,k}^{(m)}z^kt^n
 =\frac{zt\,A_m(t)^2}{(1-zt)(1-t)^{2m}},\qquad
 \sum_{n\ge1}\left(\sum_{k=1}^n c_{n,k}^{(m)}\right)t^n
 =\frac{tA_m(t)^2}{(1-t)^{2m+1}}.
\]
In particular, for fixed \(m\), the probability that \(m\) independently uniform idempotents pairwise commute converges to
\[
 \frac{2^m(m!)^2}{(2m)!}=\frac{2^m}{\binom{2m}{m}}.
\]
Conditioned on this event, the normalized image size of their common product converges in distribution to \(\operatorname{Beta}(1,2m)\), whose density is \(2m(1-x)^{2m-1}\) for \(0<x<1\).

## Assumptions and scope
The chain is the labeled set \([n]=\{1,\ldots,n\}\) with its usual total order and metric. All transformations have full domain. Multiplication is composition; statements involving products of commuting maps are independent of composition order. The parameter \(m\) is any fixed positive integer for the asymptotic statements and any positive integer for the exact identities. The idempotents are sampled uniformly *from the idempotents*, not uniformly from the whole contraction monoid. The maximum subbands are maximal by inclusion, not just maximum cardinality.

## Proof
**1. Normal form.** For any \(f\in\mathcal C_n\), consecutive image values differ by zero or one, so its image is an interval \([a,b]\). If \(f^2=f\), every point of the image is fixed. Order preservation then gives \(f(x)=a\) for \(x<a\), \(f(x)=x\) for \(a\le x\le b\), and \(f(x)=b\) for \(x>b\). Conversely each displayed retraction is monotone, nonexpansive, and idempotent. Hence \(|\mathcal E_n|=n(n+1)/2\).

**2. Exact commutation criterion.** If \(I=[a,b]\) and \(J=[c,d]\) overlap, elementary clipping identities give \(e_I\circ e_J=e_J\circ e_I=e_{I\cap J}\). If, instead, \(b<c\), then \(e_I\circ e_J\) is the constant map with value \(b\), whereas \(e_J\circ e_I\) is constant with value \(c\). The other separated ordering is symmetric. Thus commutation is equivalent to nonempty intersection.

**3. Maximal commutative subbands.** Pairwise-intersecting closed intervals in a chain have nonempty common intersection: the maximum of their left endpoints does not exceed the minimum of their right endpoints. Hence any commutative subband \(\mathcal B\subseteq\mathcal E_n\) lies in \(\mathcal S_i\) for some common integer \(i\). Each \(\mathcal S_i\) is closed under products by step 2. Moreover \(e_{[i,i]}\in\mathcal S_i\) commutes with an idempotent exactly when its image interval contains \(i\); therefore no strictly larger commutative subband contains \(\mathcal S_i\). All maximal commutative subbands are the stars, and choosing \(a\in[1,i]\), \(b\in[i,n]\) proves their sizes.

**4. Rank-refined counting.** A pairwise commuting tuple has intervals with a nonempty intersection \([u,v]\). Its common product is precisely \(e_{[u,v]}\), of rank \(k=v-u+1\). Writing the individual intervals \([a_j,b_j]\), this prescribed intersection is equivalent to \(1\le a_j\le u\), \(\max_j a_j=u\), \(v\le b_j\le n\), and \(\min_j b_j=v\). The number of left-endpoint tuples is \(u^m-(u-1)^m=\Delta_m(u)\); independently, the number of right-endpoint tuples is \((n-v+1)^m-(n-v)^m=\Delta_m(n-v+1)\). Summation over \(u=1,\ldots,n-k+1\), with \(v=u+k-1\), proves the formula without overcounting, since each tuple has exactly one intersection.

**5. Rational series.** For fixed \(k\), step 4 is the convolution of the series \(F_m(t)=\sum_{r\ge1}\Delta_m(r)t^{r-1}=A_m(t)/(1-t)^m\) with itself, shifted by \(t^k\). Thus the coefficient of \(z^k\) is \(t^k F_m(t)^2\). Summing the geometric series over \(k\ge1\) gives the bivariate formula. Substituting \(z=1\) gives the total series. The standard Eulerian identity follows also by taking first differences of \(\sum_{r\ge1}r^mt^{r-1}\), and \(A_m(1)=m!\).

**6. Asymptotic law.** The total-count series has its sole singularity on the closed unit disk at \(t=1\), a pole of order \(2m+1\) with leading numerator \((m!)^2\). Equivalently, the binomial expansion gives
\[
 C_n^{(m)}:=\sum_k c_{n,k}^{(m)}
 =\frac{(m!)^2}{(2m)!}n^{2m}+O_m(n^{2m-1}).
\]
There are \(N_n=n(n+1)/2\) idempotents, so \(C_n^{(m)}/N_n^m\to2^m(m!)^2/(2m)!\). Writing \(h=n-k\), the exact coefficient formula \(c_{n,k}^{(m)}=[t^h]A_m(t)^2/(1-t)^{2m}\) is a polynomial in the nonnegative integer \(h\) of degree \(2m-1\): expand the numerator of degree at most \(2m-2\) and use the binomial coefficient formula for the denominator. Its leading coefficient is \(A_m(1)^2/(2m-1)!=(m!)^2/(2m-1)!\). Thus, uniformly as \(n\to\infty\) and \(1\le k\le n\),
\[
 c_{n,k}^{(m)}=
 \frac{(m!)^2}{(2m-1)!}(n-k)^{2m-1}
 +O_m(n^{2m-2}+1).
\]
The bound \(c_{n,k}^{(m)}\le C_m(n-k+1)^{2m-1}\) holds for all \(1\le k\le n\), by summing the elementary bound \(\Delta_m(r)\le mr^{m-1}\). Consequently the normalized ranks converge weakly to the distribution with density \(2m(1-x)^{2m-1}\); the displayed bound controls the endpoint contribution. In particular the conditional expected rank divided by \(n\) tends to \(1/(2m+1)\), since the normalized ranks lie in \([0,1]\).

## Verification
A standalone standard-library checker independently enumerates every monotone 1-Lipschitz map by its initial value and its successive increments, rather than assuming the interval normal form. It finds idempotents by composing maps, verifies the interval description and pairwise commutation criterion, checks that the predicted stars are maximal, and then independently enumerates ordered idempotent tuples, their commutation and their product image ranks. It matches the exact formula in 30 configurations: all \(1\le n\le9\) for \(m=1,2\), all \(1\le n\le7\) for \(m=3\), and all \(1\le n\le5\) for \(m=4\). The run examines 102,917 ordered candidate tuples and reports `ALL_CONTRACTION_IDEMPOTENT_TUPLE_CHECKS_PASSED 30 102917`. Execute `python3 verify.py` with Python 3 and no third-party dependencies. These finite checks are evidence, not a substitute for the all-parameter proof above.

## Relationship to prior work
Zubairu, Umar and Aliyu (arXiv:2205.00438v1, first public 2022-05-01) study the full order-preserving contraction semigroup and its idempotent and regular subsemigroups; the count \(n(n+1)/2\) of idempotents is previously established. Umar and Zubairu (2021) establish structural properties of contraction transformation semigroups. Their investigated statements do not contain an all-arity commuting-idempotent intersection-rank distribution or the maximal commutative stars proved here. Zubairu (2023) studies an idempotent-generated semigroup of *partial order-decreasing* contractions, a different domain; its full text was not accessible for comparison. The univariate numerical sequence for the ordered pair count when \(m=2\), namely \(1,7,26,70,155,301,\ldots\), occurs in OEIS A293311 and A061926 under other combinatorial interpretations; no numerical priority is claimed for that sequence. The contribution concerns the specific transformation-semigroup interpretation, the commutation and maximal-subband classifications, all tuple lengths and common-product ranks, and the limiting distribution.

## Limitations
This result is confined to full order-preserving nonexpansive maps of finite chains, and concerns uniform sampling among *idempotents*. It does not count arbitrary commuting elements or settle the analogous problem for partial, nonmonotone, or order-reversing contractions. The asymptotic rank law fixes tuple length \(m\) as \(n\to\infty\); no joint growing-\(m\) limit is asserted. The existence of published equivalent statements under interval-graph or retraction terminology remains a priority risk, particularly where pertinent full texts were inaccessible. An independent mathematical audit has not been performed.

## References
1. M. M. Zubairu, A. Umar and M. J. Aliyu, *On the combinatorial and rank properties of certain subsemigroups of full contractions of a finite chain*, arXiv:2205.00438v1 (2022-05-01), https://arxiv.org/abs/2205.00438.
2. A. Umar and M. M. Zubairu, *On certain semigroups of contraction mappings of a finite chain*, Algebra and Discrete Mathematics 32 (2021), 299–320, https://doi.org/10.12958/adm1816.
3. M. M. Zubairu, *On the subsemigroup generated by idempotents of the semigroup of order preserving and decreasing contraction mappings of a finite chain*, Journal of the Nigerian Mathematical Society 42 (2023), 140–152, https://ojs.ictp.it/jnms/index.php/jnms/article/view/934.
4. OEIS A293311 and A061926, numerical tables for the univariate pair-count sequence, https://oeis.org/A293311 and https://oeis.org/A061926.
