# A phase law and an atomic limiting distribution for mixed Wythoff representations

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(\alpha=\varphi^{-1}\), and \(\beta=\varphi^{-2}=1-\alpha\). For each integer \(n\ge2\), put
\[
r(n)=\#\{(h,k)\in\mathbb Z_{>0}^2:\ n=\lfloor h\varphi\rfloor+\lfloor k\varphi^2\rfloor\},
\qquad \theta_n=\{n\alpha\}.
\]
Define the circle-continuous, piecewise-linear function
\[
\Lambda(t)=\begin{cases}
\beta-t,&0\le t\le\beta,\\
t-\beta,&\beta\le t\le 2\beta,\\
\beta,&2\beta\le t<1.
\end{cases}
\]
Here \(\{x\}=x-\lfloor x\rfloor\). The principal conclusions are:

**Uniform phase approximation.** There is an absolute constant \(C\) such that, for every integer \(n\ge2\),
\[
\bigl|r(n)-(n-1)\Lambda(\theta_n)\bigr|\le C\log(n+1).
\]

**Limiting distribution.** As \(X\to\infty\), the empirical probability measures of \(r(n)/n\), for \(2\le n\le\lfloor X\rfloor\), converge weakly to
\[
\boxed{\mu=2\,\mathbf 1_{(0,\beta)}(t)\,dt+(1-2\beta)\,\delta_\beta.}
\]
In particular, the continuous component has constant density \(2\) on \((0,\beta)\), while a positive atom of mass \(1-2\beta=\sqrt5-2\) lies at the maximal normalized value \(\beta\). Consequently,
\[
\liminf_{n\to\infty}\frac{r(n)}n=0,\qquad
\limsup_{n\to\infty}\frac{r(n)}n=\beta,\qquad
\lim_{X\to\infty}\frac1{\lfloor X\rfloor-1}\sum_{n=2}^{\lfloor X\rfloor}\frac{r(n)}n=\alpha\beta=\sqrt5-2.
\]

## Assumptions and scope

The representation uses **positive** indices \(h,k\), counts each ordered choice \((h,k)\) exactly once, and fixes the lower Wythoff summand first and the upper Wythoff summand second. There are no restrictions on equality between the indices. The theorem concerns **all** integers \(n\ge2\) and the full limiting sequence \(X\to\infty\), without subsequence or probabilistic assumptions. The implicit logarithmic-error constant is independent of \(n\). The probability measure is supported on \([0,\beta]\) and is not a pointwise limit of the oscillating sequence \(r(n)/n\).

## Proof

**1. Convert representations into an irrational rotation count.** The Beatty sets \(L=\{\lfloor h\varphi\rfloor:h\ge1\}\) and \(U=\{\lfloor k\varphi^2\rfloor:k\ge1\}\) partition the positive integers, because \(\varphi^{-1}+\varphi^{-2}=1\). For an integer \(m\ge1\), the indicator of \(L\) is
\[
s(m)=\lfloor(m+1)\alpha\rfloor-\lfloor m\alpha\rfloor
=\mathbf1_{[\beta,1)}(\{m\alpha\}).
\]
Indeed, the number of positive indices \(h\) with \(\lfloor h\varphi\rfloor\le m\) equals \(\lfloor(m+1)\alpha\rfloor\); taking consecutive differences yields the indicator. The indicator of \(U\) is \(1-s(m)\). Thus, exactly,
\[
r(n)=\sum_{m=1}^{n-1}s(m)\bigl(1-s(n-m)\bigr).
\]
Write \(\theta=\{n\alpha\}\) and \(x=\{m\alpha\}\). The summand equals one precisely when
\[
x\in[\beta,1),\qquad \{\theta-x\}<\beta.
\]
Since \(\theta\notin\{0,\beta,2\beta\}\) for integers \(n\ge2\), this condition selects one interval \(J_\theta\) on the circle, with its immaterial endpoint conventions determined by the displayed indicators. Its interior is, case by case,
\[
J_\theta=\begin{cases}
(\alpha+\theta,1),&0<\theta<\beta,\\
(\beta,\theta),&\beta<\theta<2\beta,\\
(\theta-\beta,\theta),&2\beta<\theta<1.
\end{cases}
\]
The respective lengths are \(\beta-\theta\), \(\theta-\beta\), and \(\beta\), which equal \(\Lambda(\theta)\). Therefore
\[
r(n)=\#\{1\le m\le n-1:\{m\alpha\}\in J_{\theta_n}\}.
\]
Endpoint inclusion can affect an interval count by at most two and hence never affects the claimed error or weak limit.

**2. Establish uniform logarithmic discrepancy.** The continued fraction of \(\alpha\) has all partial quotients equal to one. Its convergent denominators \(q_j\) are Fibonacci numbers, with numerators \(p_j\) satisfying \(|\alpha-p_j/q_j|<1/q_j^2\). Consider any block of \(q_j\) consecutive integers, beginning at an arbitrary \(M\ge1\). The corresponding points \(\{(M+t)\alpha\}\), with \(0\le t<q_j\), lie within circular distance \(1/q_j\) of the translated equally spaced grid \(\{M\alpha+tp_j/q_j\}\). As \(p_j\) and \(q_j\) are coprime, that grid has exactly one point in each of \(q_j\) equal cells. For **any** circular interval \(J\), counting membership differs from \(q_j|J|\) by at most an absolute constant: a grid-count discrepancy of at most two, plus only a bounded number of grid points near the two endpoints. This argument is uniform in the block origin and interval.

A Zeckendorf expansion decomposes the consecutive integers from \(1\) to \(n-1\) into at most \(O(\log(n+1))\) consecutive blocks whose lengths are these Fibonacci denominators (with singletons handled directly). Summing the preceding block estimates, uniformly over the interval \(J\), gives
\[
\sup_J\left|\#\{1\le m\le n-1:\{m\alpha\}\in J\}-(n-1)|J|\right|=O(\log(n+1)).
\]
Applying this to \(J=J_{\theta_n}\) proves the uniform phase approximation. In particular, a nonfixed, \(n\)-dependent interval causes no problem because the discrepancy estimate is uniform over intervals.

**3. Compute the limiting law.** Irrational rotation implies that \(\theta_n=\{n\alpha\}\) is uniformly distributed on \([0,1)\). Dividing the phase approximation by \(n\) shows that \(r(n)/n-\Lambda(\theta_n)\to0\) uniformly along all sufficiently large indices. The function \(\Lambda\) is continuous on the circle; therefore its pushforward of Lebesgue measure is the limiting empirical law.

The first two branches of \(\Lambda\) each traverse the full interval \((0,\beta)\) with absolute slope one. They contribute a density of one each. The third branch is constant \(\beta\) on an interval of length \(1-2\beta\), producing exactly that mass at \(\beta\). This yields \(\mu\) as stated. Its total mass is \(2\beta+(1-2\beta)=1\). Its first moment is
\[
2\int_0^\beta t\,dt+(1-2\beta)\beta
=\beta-\beta^2=\alpha\beta=\sqrt5-2.
\]
Finally, density of the rotation orbit and the range \(\Lambda([0,1))=[0,\beta]\) yield the displayed liminf and limsup, completing the proof.

## Verification

The companion `verify.py` uses exact integer square roots to calculate Wythoff-membership indicators. It directly computes the full indicator convolution through \(n=8192\), independently enumerates literal lower-plus-upper pairs through \(n=2048\), and compares the two counts exactly. It additionally checks the initial OEIS A259598 terms, numerically examines the phase error for the complete range, and compares the finite mean with the predicted first moment. Its executable result is `VERIFY_OK` with phase errors between approximately \(-1.851\) and \(1.716\) over the checked range. These finite tests are not the basis of the infinite proof, which is given above.

## Relationship to prior work

Ashburn's *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words* (first public release 2026-10-04; arXiv:2610.04842v1; primary MSC 11B85), Theorem 1, determines precisely when the same representation count is \(0\), \(1\), or \(2\); it does not present the macroscopic phase approximation or the empirical distribution with an atom. Shallit's *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond* (arXiv:2006.04177; published 2022), Section 11.2, explicitly supplies a general rank-19 automata-based **exact linear representation** of mixed Wythoff counts. That algorithmic coverage is a substantial predecessor; the present assertion is **not** that counts lacked an exact computational representation, but that the elementary uniform phase approximation and explicit limiting law are not stated in the examined treatment. OEIS A259598 records the sequence, its generating-function convolution and exceptional low multiplicities, but not this limiting law.

Earlier work of Kawsumarng, Khemaratchatakumthorn, Noppakaew and Pongsriiam establishes the representation-support criterion. The Phunphayap–Pongsriiam–Shallit and Pongsriiam papers examine broader Beatty sumsets and additive bases. Their accessible descriptions concern support/coverage rather than the asserted normalized mixed representation-count distribution. The full texts of some of those works were not available in this comparison; this is an originality limitation, not evidence of absence.

## Limitations

The phase error is proved to be \(O(\log n)\), not claimed optimal. The limiting law is a weak empirical limit over integers, not a distribution arising from independent random choices, nor an exact finite-\(n\) formula. No assertion of mathematical priority or uniqueness is inferred from unsuccessful searches; previous exact automata enumeration is expressly acknowledged.

## References

1. A. Ashburn, *Proofs of some OEIS conjectures on Wythoff sums, Fibonacci and Lucas words*, arXiv:2610.04842v1 (2026-10-04), especially Theorem 1 and Section 3. https://arxiv.org/html/2610.04842v1
2. J. Shallit, *Sumsets of Wythoff Sequences, Fibonacci Representation, and Beyond*, arXiv:2006.04177 (2020), especially Section 11.2. https://arxiv.org/abs/2006.04177
3. OEIS A259598, *Number of representations as a lower plus upper Wythoff number*. https://oeis.org/A259598
4. S. Kawsumarng, T. Khemaratchatakumthorn, P. Noppakaew and P. Pongsriiam, *Sumsets associated with Wythoff sequences and Fibonacci numbers*, *Periodica Mathematica Hungarica* 82 (2021), 98–113. https://doi.org/10.1007/s10998-020-00343-0
5. P. N. Phunphayap, P. Pongsriiam and J. Shallit, *Sumsets associated with Beatty sequences*, *Discrete Mathematics* 345 (2022), 112810. https://doi.org/10.1016/j.disc.2022.112810
6. P. Pongsriiam, *Combinatorial structure and sumsets associated with Beatty sequences generated by powers of the golden ratio*, *Electronic Research Archive* 30 (2022), 2385–2405. https://doi.org/10.3934/era.2022121
