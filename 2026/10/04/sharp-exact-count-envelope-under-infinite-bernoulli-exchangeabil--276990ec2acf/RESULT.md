# Sharp exact-count envelope under infinite Bernoulli exchangeability

## Finding

Let \(n\ge2\) and let \(1\le k\le n-1\). Consider an infinitely exchangeable
Bernoulli sequence
\[
(X_i)_{i\ge1}
\]
with common marginal
\[
\Pr(X_i=1)=\mu,
\]
and write
\[
K_n=\sum_{i=1}^n X_i.
\]

Define the binomial point-probability curve
\[
f_{n,k}(p)=\binom nk p^k(1-p)^{n-k},
\]
and the two breakpoints
\[
a=\frac{k-1}{n-1},
\qquad
b=\frac{k}{n-1}.
\]

Then the exact attainable set of point probabilities is
\[
\boxed{
\Pr(K_n=k)\in[0,U_{n,k}(\mu)].
}
\]

The upper endpoint is the three-piece function
\[
U_{n,k}(\mu)=
\begin{cases}
\dfrac{\mu}{a}f_{n,k}(a),
&0\le\mu\le a,\quad k>1,\\[3mm]
f_{n,k}(\mu),
&a\le\mu\le b,\\[3mm]
\dfrac{1-\mu}{1-b}f_{n,k}(b),
&b\le\mu\le1,\quad k<n-1,
\end{cases}
\]
where an edge piece is omitted when its denominator would vanish.

Equivalently, for \(k>1\),
\[
\frac{f_{n,k}(a)}{a}
=
\binom nk
\left(\frac{k-1}{n-1}\right)^{k-1}
\left(\frac{n-k}{n-1}\right)^{n-k},
\]
and for \(k<n-1\),
\[
\frac{f_{n,k}(b)}{1-b}
=
\binom nk
\left(\frac{k}{n-1}\right)^k
\left(\frac{n-k-1}{n-1}\right)^{n-k-1}.
\]

The upper extremizer has a directing measure with at most two atoms:

- if \(0\le\mu<a\), it is supported on \(\{0,a\}\);
- if \(a\le\mu\le b\), it is the degenerate law at \(\mu\);
- if \(b<\mu\le1\), it is supported on \(\{b,1\}\).

The lower endpoint \(0\) is attained for every \(\mu\) by a directing law
supported on \(\{0,1\}\). Convex mixing of upper and lower extremizers fills
the whole interval.

Thus the iid Bernoulli law maximizes the probability of exactly \(k\)
successes only in the narrow marginal window
\[
\frac{k-1}{n-1}
\le
\mu
\le
\frac{k}{n-1}.
\]
Outside that window, latent Bernoulli heterogeneity can increase the exact
count probability beyond the iid value.

## Assumptions and scope

Infinite exchangeability is essential. It means that every finite prefix is
the restriction of a single infinite exchangeable sequence. Under this
assumption, de Finetti's theorem represents the sequence as a mixture of iid
Bernoulli sequences.

Only the one-dimensional marginal mean \(\mu\) is fixed. No correlation,
mixing variance, or parametric form of the directing distribution is assumed.

The theorem treats interior counts \(1\le k\le n-1\). The endpoint events
\(K_n=0\) and \(K_n=n\) have different one-sided envelope geometry and are not
part of the claim.

## Proof

By de Finetti's theorem there is a random variable \(P\in[0,1]\) such that,
conditionally on \(P\), the sequence is iid Bernoulli with success probability
\(P\). The marginal constraint is
\[
\mathbb E P=\mu,
\]
and
\[
\Pr(K_n=k)=\mathbb E f_{n,k}(P).
\tag{1}
\]

The problem is therefore a one-moment extremal problem for the beta-shaped
curve \(f_{n,k}\) on \([0,1]\). Its maximum at fixed mean is the least concave
majorant evaluated at that mean, while its minimum is the greatest convex
minorant.

We first determine the least concave majorant.

Assume \(k>1\). For \(p>0\),
\[
\frac{f_{n,k}(p)}{p}
=
\binom nk p^{k-1}(1-p)^{n-k}.
\]
Its logarithmic derivative is
\[
\frac{k-1}{p}-\frac{n-k}{1-p},
\]
which vanishes exactly at
\[
p=a=\frac{k-1}{n-1}.
\]
Hence
\[
\frac{f_{n,k}(p)}p
\le
\frac{f_{n,k}(a)}a
\]
for every \(p\in(0,1)\), so the line through \((0,0)\) and
\((a,f_{n,k}(a))\) majorizes the curve. The maximizing-ratio condition also
gives the tangency identity
\[
f'_{n,k}(a)=\frac{f_{n,k}(a)}a.
\tag{2}
\]

Similarly, when \(k<n-1\),
\[
\frac{f_{n,k}(p)}{1-p}
=
\binom nk p^k(1-p)^{n-k-1}
\]
is maximized at
\[
p=b=\frac{k}{n-1}.
\]
Therefore the line joining \((b,f_{n,k}(b))\) to \((1,0)\) majorizes the
curve, with tangency identity
\[
f'_{n,k}(b)
=
-\frac{f_{n,k}(b)}{1-b}.
\tag{3}
\]

It remains to check that \(f_{n,k}\) itself is concave between the two
tangency points. On the open unit interval,
\[
f''_{n,k}(p)
=
\binom nk p^{k-2}(1-p)^{n-k-2}Q(p),
\]
where
\[
Q(p)
=
n(n-1)p^2-2k(n-1)p+k(k-1).
\]
The polynomial \(Q\) is convex, and
\[
Q(a)=\frac{(k-1)(k-n)}{n-1}\le0,
\qquad
Q(b)=\frac{k(k-n+1)}{n-1}\le0.
\]
A convex function lies below the chord joining its endpoint values, so
\[
Q(p)\le0
\qquad(a\le p\le b).
\]
Thus \(f_{n,k}\) is concave on \([a,b]\). Equations (2) and (3) show that
the left line, central curve, and right line join with matching slopes.
Consequently \(U_{n,k}\) is concave and majorizes \(f_{n,k}\).

It is the least concave majorant. Let \(H\) be any concave majorant of
\(f_{n,k}\). On \([0,a]\), concavity and
\[
H(0)\ge0,\qquad H(a)\ge f_{n,k}(a)
\]
give
\[
H(p)\ge\frac{p}{a}f_{n,k}(a).
\]
On \([a,b]\), one has \(H\ge f_{n,k}\) by definition. On \([b,1]\),
concavity and the endpoint inequalities similarly give
\[
H(p)\ge\frac{1-p}{1-b}f_{n,k}(b).
\]
Hence \(H\ge U_{n,k}\).

The cases \(k=1\) and \(k=n-1\) are the corresponding one-sided versions:
the missing tangent point is an endpoint, and the same derivative argument
gives the remaining tangent line.

Jensen's inequality applied to the least concave majorant now yields
\[
\mathbb E f_{n,k}(P)
\le
\mathbb E U_{n,k}(P)
\le
U_{n,k}(\mathbb E P)
=
U_{n,k}(\mu).
\]

The bound is attained. In the left regime, choose
\[
\Pr(P=a)=\frac{\mu}{a},
\qquad
\Pr(P=0)=1-\frac{\mu}{a}.
\]
In the central regime, choose \(P=\mu\) almost surely. In the right regime,
choose
\[
\Pr(P=b)=\frac{1-\mu}{1-b},
\qquad
\Pr(P=1)=1-\frac{1-\mu}{1-b}.
\]
Each measure has mean \(\mu\), and substituting into (1) gives the
corresponding piece of \(U_{n,k}\).

For the lower endpoint, note that \(f_{n,k}\ge0\) and
\[
f_{n,k}(0)=f_{n,k}(1)=0.
\]
The zero function is therefore a convex minorant. It is the greatest one:
if \(G\le f_{n,k}\) is convex, then
\[
G(0)\le0,\qquad G(1)\le0,
\]
so convexity gives
\[
G(p)\le(1-p)G(0)+pG(1)\le0.
\]
Thus the greatest convex minorant is identically zero. It is attained by
\[
\Pr(P=1)=\mu,
\qquad
\Pr(P=0)=1-\mu.
\]

Finally, convex mixtures of two directing measures with the same mean
\(\mu\) retain that mean, and the point probability in (1) interpolates
linearly. Therefore every value in
\[
[0,U_{n,k}(\mu)]
\]
is attainable.

## Verification

A standalone exact-rational checker accompanies the theorem. For many
\((n,k)\) pairs and rational values of \(p\), it verifies the left and right
majorant inequalities, the central concavity certificate, the tangent
identities, and the endpoint directing measures.

The checker also enumerates a large collection of two-atom rational directing
laws with prescribed rational mean and confirms that none exceeds the stated
upper envelope.

These finite checks replay the formulas but do not replace the proof of the
continuous one-moment optimization.

## Relationship to prior work

Misra, Singh, and Harner study stochastic comparisons between a binomial law
and a mixed binomial law. Their mixed-binomial probability formula is exactly
the integral
\[
\mathbb E f_{n,k}(P)
\]
appearing here. Under equal means, their Theorem 4.3 proves that a nondegenerate
mixed binomial is uniformly more variable, and hence larger in convex order,
than the ordinary binomial. That ordering result does not determine the sharp
maximum of a single point mass, which is neither a convex nor a concave
functional of the count. The inspected paper does not state the two tangent
breakpoints or the exact fixed-mean point-mass interval.

Zaigraev and Kaniovski solve a different finite-exchangeable problem: with
only the marginal success probability fixed, they give sharp bounds for the
monotone event of at least \(k\) successes. Their optimization ranges over
all finitely exchangeable Bernoulli vectors, whereas the present theorem
imposes infinite extendibility and optimizes the nonmonotone event of exactly
\(k\) successes.

The closest published result located in the semantic database gives exact
tail envelopes under infinite exchangeability by taking the least concave
majorant of a binomial tail. Its proof establishes the general one-moment
envelope architecture. The point-mass objective here has different geometry:
its least concave majorant has two explicit tangent breakpoints,
\[
\frac{k-1}{n-1}
\quad\text{and}\quad
\frac{k}{n-1},
\]
with an iid central segment and two heterogeneous outer extremizers. The tail
theorem does not state or imply these point-mass formulas without this separate
calculation.

For comparison, over all merely \(n\)-exchangeable Bernoulli vectors with
mean \(\mu\), the count \(K_n\) may be any distribution on
\(\{0,\ldots,n\}\) with mean \(n\mu\). Its exact point-mass upper bound is
\[
\min\!\left\{
1,\frac{n\mu}{k},
\frac{n(1-\mu)}{n-k}
\right\},
\]
which is generally wider than the infinitely extendible envelope above.

## Limitations

The theorem fixes only the marginal mean of the directing law. If its variance
or other moments are known, sharper bounds are possible.

The endpoint count probabilities \(k=0\) and \(k=n\) require separate
one-sided formulas and are intentionally excluded.

The result is specific to infinite exchangeability. Finite exchangeability
without extendibility has a larger feasible class.

The originality assessment used targeted searches in exchangeability,
binomial-mixture, reliability, and moment-envelope terminology together with
full-text inspection of the closest primary sources and a statement-level
comparison with the closest published result. An equivalent formula may still
exist in older mixture or moment-problem literature under different language.

## References

1. N. Misra, H. Singh, and E. J. Harner, “Stochastic comparisons of Poisson
   and binomial random variables with their mixtures,” *Statistics &
   Probability Letters* 65 (2003), 279–290, DOI
   10.1016/j.spl.2003.07.002.
2. A. Zaigraev and S. Kaniovski, “Exact bounds on the probability of at least
   \(k\) successes in \(n\) exchangeable Bernoulli trials as a function of
   correlation coefficients,” preprint dated 2010-03-28; later published in
   *Statistics & Probability Letters* 80 (2010), 1079–1084.
3. B. de Finetti, classical representation theorem for infinitely
   exchangeable Bernoulli sequences.
