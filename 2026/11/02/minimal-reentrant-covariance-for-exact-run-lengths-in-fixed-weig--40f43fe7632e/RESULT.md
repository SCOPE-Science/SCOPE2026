# Minimal reentrant covariance for exact run lengths in fixed-weight binary words

## Finding

**Theorem.** Fix two distinct positive integers \(r<s\). Let \(W\) be uniformly distributed over binary words with exactly \(a\) ones and \(b\) zeros, and let \(X_j\) count maximal contiguous runs of ones having length exactly \(j\), including runs touching either endpoint.

For fixed \(r,s\) and any sequence of integer pairs with \(b\to\infty\) and \(a/b\to x\in(0,\infty)\), put
\[
 g_j(x)=\frac{x^j}{(1+x)^{j+1}},\qquad Q_{r,s}(x)=2x^2+(1-r-s)x+rs.
\]
Then
\[
 \lim_{b\to\infty}\frac{\operatorname{Cov}(X_r,X_s)}{b}
 =-\frac{g_r(x)g_s(x)}{x(1+x)}Q_{r,s}(x).
\]
The normalized limiting covariance has a **strict negative–positive–negative sequence of phases** as \(x\) increases precisely when
\[
 \Delta_{r,s}:=(r+s-1)^2-8rs>0.
\]
In that case it is strictly positive exactly for
\[
 \frac{r+s-1-\sqrt{\Delta_{r,s}}}{4}<x<
 \frac{r+s-1+\sqrt{\Delta_{r,s}}}{4},
\]
and strictly negative outside the closed interval. When \(\Delta_{r,s}\le0\), it is never strictly positive. Of all distinct positive run lengths, \((r,s)=(1,9)\) is the unique pair of minimum total length \(r+s=10\) having such an open positive phase, with critical ratios \(3/2\) and \(3\).

The phenomenon also has an exact, not merely asymptotic, infinite family: for **every** integer \(t\ge10\), keeping \(b=t\) fixed across the three samples and taking \(a=t,2t,4t\), respectively, gives
\[
 \bigl(\operatorname{sgn}\operatorname{Cov}(X_1,X_9)\bigr)_{a=t,2t,4t}=(-,+,-).
\]

## Assumptions and scope

The word is sampled **uniformly conditional on both symbol totals**, not by drawing iid Bernoulli letters without conditioning. Every maximal run of ones is counted once, whether at an endpoint or in the interior. Different run lengths are fixed positive integers and their counts refer to the same word; the covariance is not a covariance of independent samples. The exact moment formula below holds whenever \(a\ge r+s\), \(b\ge2\), and \(r\ne s\). The limiting formula requires \(a,b\to\infty\) with \(a/b\to x\in(0,\infty)\). A vanishing *leading* limit at a critical ratio does not determine a finite-size covariance sign there.

Write \((v)_{\underline{k}}=v(v-1)\cdots(v-k+1)\) for the falling factorial and \((v)_{\underline0}=1\). Set \(n=a+b\) and \(m=b+1\). Define
\[
 p_j=\frac{b(a)_{\underline j}}{(n)_{\underline{j+1}}},\qquad
 p_{r,s}=\frac{b(b-1)(a)_{\underline{r+s}}}{(n)_{\underline{r+s+2}}}.
\]
For all the exact-formula parameters,
\[
 \operatorname{Cov}(X_r,X_s)=m(m-1)p_{r,s}-m^2p_rp_s.
\]

## Proof

**1. Uniform gaps and exact mixed moments.** Place the \(b\) zeros in order. The numbers of ones before the first zero, between successive zeros, and after the last zero form \(m=b+1\) ordered nonnegative gaps whose sum is \(a\). This correspondence between words and weak compositions is bijective. Every weak composition is therefore equally likely, with \(\binom{a+b}{b}\) possibilities. The chance that one specified gap equals \(j\) is
\[
 \frac{\binom{a-j+b-1}{b-1}}{\binom{a+b}{b}}=p_j.
\]
The chance that two specified, distinct gaps equal \(r\) and \(s\) is
\[
 \frac{\binom{a-r-s+b-2}{b-2}}{\binom{a+b}{b}}=p_{r,s}.
\]
These formulas hold in the stated domain. Writing \(X_j\) as a sum of \(m\) gap indicators, and using \(r\ne s\), gives \(\mathbb EX_j=mp_j\) and \(\mathbb E[X_rX_s]=m(m-1)p_{r,s}\), proving the exact covariance identity.

**2. The universal limiting sign kernel.** Put \(x_b=a/b\), so \(x_b\to x>0\). For each fixed integer \(k\), uniformly for \(x_b\) in a compact subset of \((0,\infty)\),
\[
 (a)_{\underline k}=a^k\left(1-\frac{k(k-1)}{2a}+O(b^{-2})\right),
 \quad (n)_{\underline k}=n^k\left(1-\frac{k(k-1)}{2n}+O(b^{-2})\right).
\]
Substitute these expansions into the exact moments, cancel the quadratic terms of the covariance, and divide by \(b\). The coefficient left after cancellation is
\[
 g_r(x_b)g_s(x_b)\left[-\frac{rs}{x_b}
 +\frac{rs+r+s+1}{1+x_b}-2\right]
 =-g_r(x_b)g_s(x_b)\frac{Q_{r,s}(x_b)}{x_b(1+x_b)}.
\]
Taking the limit proves the claimed formula without using a central limit theorem. Since the remaining factors are positive, the sign is the opposite of the quadratic \(Q_{r,s}\). Its discriminant is \(\Delta_{r,s}\). For positive \(r,s\), a strictly positive discriminant gives two positive roots (their sum is \((r+s-1)/2>0\), and product \(rs/2>0\)), hence the stated three phases. If the discriminant is nonpositive, the quadratic cannot be negative.

For \(r+s=u\le9\), the inequality \(rs\ge u-1\) (for positive integer \(r,s\)) gives
\[
 \Delta_{r,s}\le(u-1)^2-8(u-1)=(u-1)(u-9)\le0.
\]
At total length ten, the pair \((1,9)\) gives \(\Delta_{1,9}=9\), while \((2,8)\), \((3,7)\), \((4,6)\) have nonpositive discriminants. Thus \((1,9)\) uniquely minimizes the total run lengths among strict reentrant phases. Its roots are \(3/2\) and \(3\).

**3. All-orders exact three-phase witness.** For \(r=1,s=9\) with \(a\ge10,b\ge2\), elementary falling-factorial cancellations give
\[
 \frac{m-1}{m}\frac{p_{1,9}}{p_1p_9}=
 \frac{(b-1)(a-9)n(n-1)}{(b+1)a(n-10)(n-11)}.
\]
Consequently the covariance has the sign of the integer polynomial
\[
 F(a,b)=(b-1)(a-9)n(n-1)-(b+1)a(n-10)(n-11),
 \quad n=a+b.
\]
Direct expansions yield
\[
 \begin{aligned}
 F(t,t)&=-4t(t^2+3t+32),\\
 F(2t,t)&=t(t+13)(3t-19),\\
 F(4t,t)&=-5t(5t^2-54t+97).
 \end{aligned}
\]
For every integer \(t\ge10\), the first is negative, the second positive, and the third negative: \(5t^2-54t+97\ge57\) at \(t=10\) and increases thereafter. All denominators cancelled in obtaining the sign are strictly positive in this domain. This establishes the exact infinite family and finishes the proof.

## Verification

A standalone Python 3 checker, `checks/check_covariance.py`, enumerates binary words with \(2\le a\le7\), \(2\le b\le6\), calculates covariance from integer run counts and exact rational arithmetic, and compares all distinct run-length pairs with the factorial moment identity. It separately checks the three polynomial factorizations and their signs for every \(10\le t\le140\), and verifies asymptotic sign predictions on a broad parameter grid away from critical values. It reports 1292 passed assertions. These finite checks supplement rather than replace the all-orders algebraic proof.

## Relationship to prior work

Oh and Jang (2022) analyze the distributions and moments of exact-length success runs in a geometrically biased \(q\)-sequence. Their Theorems 3.1–3.3 concern one run length at a time in a different sampling scheme, whereas the present statement concerns *joint covariance across two distinct lengths conditional on symbol totals*. The classical literature on binary runs, including Makri, Philippou, and Psillakis (2007), provides combinatorial run-count enumeration and some conditional distributions; those components are not claimed as new. The contribution stated here is the covariance kernel's complete asymptotic sign criterion, the minimal strict reentrant length pair, and its exact infinite sequence of finite sign reversals. The literature search did not establish historical uniqueness; an earlier implicit derivation from broader joint run-count machinery remains possible.

## Limitations

The three-phase theorem concerns the normalized *limit* for each fixed pair of positive run lengths, and makes no assertion about finite signs at a critical limiting ratio. The exact sign witness uses only \((r,s)=(1,9)\) and three explicit fixed-count families; it is not a full finite sign classification at all \(a,b,r,s\). The argument does not extend unchanged to nonuniform word weights, arbitrary exchangeable distributions or run patterns that overlap other symbols. Prior generating-function formulations may encode this result implicitly. No independent external audit was performed.

## References

1. J. Oh and D.-G. Jang, *On Success runs of a fixed length defined on a \(q\)-sequence of binary trials*, first submitted 2022-10-10, arXiv:2210.04521, https://arxiv.org/abs/2210.04521.
2. F. S. Makri, A. N. Philippou, and Z. M. Psillakis, *Success run statistics defined on an urn model*, Advances in Applied Probability 39 (2007), 991–1019, https://doi.org/10.1239/aap/1198177236.
3. S. Eryilmaz, *Run Statistics Defined on the Multicolor URN Model*, Journal of Applied Probability 45 (2008), 1007–1023, https://doi.org/10.1239/jap/1231340230.
