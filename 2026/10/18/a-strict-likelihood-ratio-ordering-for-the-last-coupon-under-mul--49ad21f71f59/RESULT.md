# A strict likelihood-ratio ordering for the last coupon under multiple quotas

## Finding
Let \(m\ge2\), \(h\ge1\) be integers. Let \(p_1,\ldots,p_m>0\) and \(p_0\ge0\) satisfy \(p_0+\sum_{i=1}^{m}p_i=1\). Draw independent symbols from \(\{0,1,\ldots,m\}\) with these probabilities, ignoring symbol \(0\) when counting collected coupons. Let \(N\) be the first draw number at which each positive symbol has occurred at least \(h\) times, and let \(L\in\{1,\ldots,m\}\) be the positive symbol drawn at time \(N\).

**Strict likelihood-ratio theorem.** For any two positive labels \(i,j\) with \(p_i<p_j\),
\[
\frac{\Pr(N=n+1,L=i)}{\Pr(N=n+1,L=j)}
>
\frac{\Pr(N=n,L=i)}{\Pr(N=n,L=j)},
\qquad n\ge mh.
\]
Equivalently, \(N\mid\{L=i\}\) is strictly larger than \(N\mid\{L=j\}\) in the likelihood-ratio order. At the first possible completion time \(n=mh\), the conditional final label is uniform across all \(m\) types; at every \(n>mh\), the final-label probabilities are strictly ordered by increasing rarity. Equal positive-symbol probabilities give identical conditional probabilities for the corresponding labels at all times.

Define \(F_{p,h}(z)=\sum_{r\ge h}p^r z^r/r!\). The exact joint law for all \(n\ge mh\) is
\[
\Pr(N=n,L=i)=
\frac{p_i^h (n-1)!}{(h-1)!}
[z^{n-h}]\,e^{p_0z}\prod_{\ell\ne i}F_{p_\ell,h}(z).
\]
For fixed positive probabilities and quota, the odds additionally satisfy
\[
\frac{\Pr(N=n,L=i)}{\Pr(N=n,L=j)}
\sim
\left(\frac{p_i}{p_j}\right)^h
\left(\frac{1-p_i}{1-p_j}\right)^{n-h}
\quad(n\to\infty),\quad p_i<p_j.
\]
The theorem covers the ordinary unequal-probability collector (\(h=1\)), all fixed repeated-collection quotas, and optional null draws.

## Assumptions and scope
Draws are independent and identically distributed; each of the \(m\) required types has strictly positive probability; every required type has the same positive integer quota \(h\). No restriction beyond \(p_0\ge0\) is made on the optional null type. All claims are finite-dimensional; the asymptotic formula is for fixed \(m,h,p_0,p_1,\ldots,p_m\), not a joint growing-type limit.

## Proof
**1. Joint coefficient identity.** For the collection to finish with label \(i\) at step \(n\), the last draw must be \(i\), exactly \(h-1\) of the first \(n-1\) symbols must equal \(i\), and each other required type must occur at least \(h\) times. Applying the multinomial theorem to the first \(n-1\) draws and multiplying by the last-draw probability \(p_i\) gives the stated coefficient expression exactly. It is positive for every \(n\ge mh\).

**2. A finite-order total-positivity lemma.** Call a nonnegative sequence log-concave if it has interval support and \(b_s^2\ge b_{s-1}b_{s+1}\). For such a sequence, the Toeplitz kernel \(K(k,r)=b_{k-r}\), taking absent coefficients as zero, has nonnegative minors of size two. Indeed, the adjacent quotient \(b_{s+1}/b_s\) decreases on the support, giving \(b_{k-r}b_{\ell-s}\ge b_{k-s}b_{\ell-r}\) whenever \(k<\ell\) and \(r<s\). Products of two such Toeplitz kernels remain nonnegative in their minors of size two by the Cauchy--Binet formula (with finite sums for each fixed index). Consequently, coefficient convolutions of nonnegative interval-supported log-concave sequences are again log-concave. This argument also covers a sequence supported at one point.

For each \(p>0\), the coefficient sequence of \(F_{p,h}\) is zero below \(h\) and equals \(p^r/r!\) at \(r\ge h\); it is log-concave. The sequence of coefficients of \(e^{p_0z}\) is log-concave too, including its single-point version when \(p_0=0\). Thus, fixing distinct labels \(i,j\), the coefficients \(b_s\) of
\[
B(z)=e^{p_0z}\prod_{\ell\notin\{i,j\}}F_{p_\ell,h}(z)
\]
form a nonnegative log-concave sequence. Its lowest positive index is \(s_0=(m-2)h\), with \(b_{s_0}>0\).

**3. Strict likelihood-ratio preservation.** Set \(a_p(r)=p^r/r!\) for \(r\ge h\) and zero otherwise, and let
\[
C_k(p)=\sum_{r\ge h} b_{k-r}a_p(r).
\]
For \(p_j>p_i\), the ratio \(a_{p_j}(r)/a_{p_i}(r)=(p_j/p_i)^r\) strictly increases over their common positive support. The Toeplitz inequality from Step 2 implies that \(C_k(p_j)/C_k(p_i)\) is nondecreasing in \(k\): expanding the cross-product difference for two indices \(k<\ell\) into pairs \(r<s\) expresses it as a sum of products of two nonnegative two-by-two determinants.

The inequality is strict for every \(s_0+h\le k<\ell\). In the cross-product expansion, select the ranks \(r=k-s_0\) and \(s=\ell-s_0\); both are at least \(h\) and \(r<s\). Their Toeplitz minor has the strictly positive contribution \(b_{s_0}^2\), because \(b_{k-s}=0\) lies below the first supported index. The rank-sequence minor is also strictly positive because \(p_j>p_i\). Therefore \(C_\ell(p_j)/C_\ell(p_i)>C_k(p_j)/C_k(p_i)\).

By Step 1, the ratio of interest equals \((p_i/p_j)^h C_{n-h}(p_j)/C_{n-h}(p_i)\); hence it strictly increases with \(n\ge mh\). Dividing each joint probability by its label marginal only introduces a fixed positive factor, proving the conditional likelihood-ratio statement.

**4. Endpoints and tail.** At \(n=mh\), every required type appears exactly \(h\) times and the null type never appears; the multinomial weight is invariant under which label was completed on the last step. Thus \(\Pr(L=i\mid N=mh)=1/m\). For fixed \(i\), the probability that the first \(n-1\) draws contain exactly \(h-1\) copies of \(i\) and at least \(h\) of each other type is asymptotic to the corresponding event without the latter restrictions: conditioned on no additional \(i\), all remaining required types have positive conditional probabilities and miss their quotas with exponentially small probability. Multiplication by \(p_i\) yields
\[
\Pr(N=n,L=i)\sim
\frac{p_i^h}{(h-1)!}
\frac{(n-1)!}{(n-h)!}(1-p_i)^{n-h},
\]
and taking ratios completes the proof.

## Verification
The accompanying `verify_coupon.py` uses exact rational arithmetic. It checks all joint probabilities by independent complete enumeration of draw strings on bounded instances, validates the lowest-time uniformity, and tests every successive strict odds inequality for several unequal parameter vectors, with and without null draws and at quotas one, two, and three. This is independent finite verification, not a substitute for the arbitrary-size proof in Steps 1--4.

## Relationship to prior work
The classical multiple-quota coupon-collector setting and generating functions for its *unlabeled* completion time are in Myers and Wilf (2003), Section 3, building on Newman and Shepp (1960). Anceaume, Busnel and Sericola (2014), Section 2, derive the *unlabeled* completion-time distribution for arbitrary coupon weights with an optional null coupon. The present finding addresses a different joint object—the completion time paired with the *identity* of the completing type—and determines its strict likelihood-ratio geometry simultaneously across arbitrary weights, repeated quotas, and null draws. The proof does not assert that completion-time distributions or generating functions themselves are new.

## Limitations
The model has independent fixed-probability draws, finite \(m\), equal quotas across types, and at most one unconstrained null class. The result does not cover quotas varying by label or adaptive sampling. The claim is a mathematical consequence under these assumptions; uniqueness in all literature is not formally certified, and a related reverse-hazard or total-positivity formulation may exist. No independent audit has been performed.

## References
1. A. N. Myers and H. S. Wilf, *Some New Aspects of the Coupon-Collector's Problem*, arXiv:math/0304229v1 (first public 2003-04-16), Sections 3--4. https://arxiv.org/html/math/0304229v1
2. E. Anceaume, Y. Busnel and B. Sericola, *New Results on a Generalized Coupon Collector Problem Using Markov Chains*, arXiv:1402.5245v1 (first public 2014-02-21), Section 2. https://ar5iv.labs.arxiv.org/html/1402.5245
3. D. J. Newman and L. Shepp, *The Double Dixie Cup Problem*, American Mathematical Monthly 67 (1960), 58--61 (cited background, not used for the proof).
