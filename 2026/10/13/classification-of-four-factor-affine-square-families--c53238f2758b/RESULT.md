# Classification of four-factor affine square families
## Finding
Let \(a_1(t),a_2(t),a_3(t),a_4(t)\) be distinct affine functions in \(\mathbb Z[t]\), each with positive leading coefficient, and suppose their values are pairwise distinct and at least \(2\) for all sufficiently large integers \(t\). If
\[
\prod_{i=1}^{4} a_i(t)!
\]
is a perfect square for every sufficiently large integer \(t\), then after relabeling so that
\[
a_1(t)>a_2(t)>a_3(t)>a_4(t)
\]
for all sufficiently large \(t\), there are coprime integers \(r>s\ge1\) and an affine function \(H(t)\in\mathbb Z[t]\) with positive leading coefficient such that
\[
(a_1,a_2,a_3,a_4)
=
(r^2H,r^2H-1,s^2H,s^2H-1).
\]
Conversely every quadruple of this form has square factorial product, with the identity
\[
(r^2H)!(r^2H-1)!(s^2H)!(s^2H-1)!
=
\bigl(rsH\,(r^2H-1)!(s^2H-1)!\bigr)^2.
\]
Thus the paired-consecutive construction is exhaustive among four-factor affine square families; the two larger arguments are obtained from the two smaller ones by a rational-square scale.

## Assumptions and scope
An affine function means \(\alpha t+\beta\) with \(\alpha,\beta\in\mathbb Z\) and \(\alpha>0\). The conclusion is eventual: only sufficiently large integer values of \(t\) are relevant, exactly as in the affine-family formulation of Yudin's Appendix A. Distinctness refers to the four affine functions and, equivalently here, to their values for all sufficiently large \(t\).

The theorem is specifically a classification at four factors and exponent two. It does not classify affine families with five or more factorials, or analogous families for higher perfect powers.

## Proof
Because any two distinct affine functions have an eventually fixed order, relabel so that
\[
a_1>a_2>a_3>a_4
\]
eventually. Write \(\lambda_i\) for the positive leading coefficient of \(a_i\).

First, \(\lambda_1=\lambda_2\). If \(\lambda_1>\lambda_2\), choose a fixed \(\theta<1\) larger than both \(1/2\) and \(\lambda_2/\lambda_1\). By the prime number theorem, for all sufficiently large \(t\) there is a prime \(p\) with
\[
\theta a_1(t)<p\le a_1(t).
\]
Then \(p>a_2(t)\), while \(p>a_1(t)/2\), so \(p\) occurs exactly once in \(a_1(t)!\) and not at all in the other three factorials. This contradicts the square condition. Hence \(\lambda_1=\lambda_2\), and therefore
\[
a_1(t)-a_2(t)=d
\]
for a fixed positive integer \(d\).

Remove the square \((a_2(t)!)^2\). The square condition becomes
\[
\Bigl(\prod_{j=1}^{d}(a_2(t)+j)\Bigr)a_3(t)!a_4(t)!=\square.
\]
The same prime-separation argument forces \(\lambda_3=\lambda_4\). Indeed, if \(\lambda_3>\lambda_4\), the prime number theorem gives, for all large \(t\), arbitrarily many primes in the interval
\[
\bigl(\max\{a_4(t),a_3(t)/2\},a_3(t)\bigr].
\]
Only the fixed \(d\) factors \(a_2(t)+1,\ldots,a_2(t)+d\) can interfere. For large \(t\), each such linear-size integer is divisible by at most one prime from this interval, so at most \(d\) primes are excluded. Choose one of the remaining primes \(p\). Then \(v_p(a_3(t)!)=1\), \(p>a_4(t)\), and \(p\) divides none of the displayed \(d\) factors, again giving odd total valuation. Thus \(\lambda_3=\lambda_4\), so
\[
a_3(t)-a_4(t)=e
\]
for a fixed positive integer \(e\).

After removing the second square \((a_4(t)!)^2\), define
\[
F(t)=\prod_{j=1}^{d}(a_2(t)+j)\prod_{j=1}^{e}(a_4(t)+j).
\]
Then \(F(n)\) is a perfect square for every sufficiently large integer \(n\).

We use the following elementary polynomial lemma: if a real polynomial \(F\) is positive for all large real \(x\) and \(F(n)\) is a square integer for every sufficiently large integer \(n\), then \(F\) is the square of a polynomial in \(\mathbb Q[x]\). To prove it, put \(y_n=\sqrt{F(n)}\in\mathbb Z\), and let \(m=\deg F\). For \(k=\lfloor m/2\rfloor+1\), the \(k\)-th derivative of \(\sqrt{F(x)}\) is \(O(x^{m/2-k})=o(1)\). The integral formula for finite differences therefore gives \(\Delta^k y_n=o(1)\). Since \(\Delta^k y_n\) is an integer, it is eventually zero. Hence \(y_n\) agrees eventually with a polynomial \(Q(n)\in\mathbb Q[n]\) of degree at most \(k-1\). The identity \(F(n)=Q(n)^2\) for infinitely many integers then gives \(F=Q^2\).

Apply the lemma to the displayed \(F\). Each of the first \(d\) linear factors has a simple root, and so does each of the last \(e\) factors. Since \(F\) is a polynomial square, the two root multisets must coincide. Consequently \(d=e\). If \(d=e\ge2\), the two root sets are finite arithmetic progressions of the same length with spacings \(1/\lambda_2\) and \(1/\lambda_4\). Equality of the sets forces \(\lambda_2=\lambda_4\) and then equality of their endpoints forces \(a_2=a_4\), contradicting distinctness. Therefore
\[
d=e=1.
\]
So the four arguments are
\[
a_1=a_2+1,
\qquad
a_3=a_4+1,
\]
and the residual polynomial is
\[
F(t)=a_1(t)a_3(t).
\]
Because this product is a polynomial square and both factors are linear, they have the same root and are associates over \(\mathbb Q\). Thus
\[
a_1=q^2a_3
\]
for some rational \(q>1\). Write \(q=r/s\) in lowest terms. Since both \(a_1\) and \(a_3\) have integer coefficients, the identity \(s^2a_1=r^2a_3\) and \(\gcd(r,s)=1\) force every coefficient of \(a_3\) to be divisible by \(s^2\). Hence \(a_3=s^2H\) for an affine \(H\in\mathbb Z[t]\), and then \(a_1=r^2H\). This gives the asserted form, and the displayed factorial identity proves the converse.

## Verification
The argument is symbolic and has no finite search component. The two external inputs are standard: the prime number theorem in fixed proportional intervals and the elementary fact that finite differences of an integer sequence are integers. The polynomial-square lemma is proved in full above rather than treated as a computational heuristic.

As a direct consistency check, substituting \(a_1=r^2H\), \(a_2=r^2H-1\), \(a_3=s^2H\), and \(a_4=s^2H-1\) reduces the product exactly to
\[
r^2s^2H^2\bigl((r^2H-1)!(s^2H-1)!\bigr)^2.
\]
No assertion is made from bounded numerical experimentation.

## Relationship to prior work
Erdős and Graham observed in 1976 that if \(n=m^2u\) with \(m>1\), then \(n!(n-1)!u!(u-1)!\) is a square; their four-factor discussion also gives other non-affine examples. Yudin uses the same paired-consecutive identity in the form \(n=v^2u\) and, in Appendix A, proves that for every exponent there are bounded-size distinct-factorial families whose arguments are fixed affine functions of a parameter. Neither inspected source gives a necessity theorem for four affine arguments.

Bérczes, Dujella, Hajdu, Saradha and Tijdeman study products of factorials that are perfect powers as the number of factorials varies, including exact statements at the exponent threshold and bounded-factor constructions. Their paper does not formulate an affine-parametric classification, and targeted full-text searches found no use of the terms affine, polynomial, or arithmetic progression in this role. Dujella, Najman, Saradha and Shorey study the three-factor square equation and exhibit quadratic and Pell-type infinite families, not a four-affine classification.

The result here therefore sharpens the recent affine construction in a different direction: at the first four-factor square level it proves exhaustiveness, and it also shows that the integer-square scaling in the displayed recent construction is only the \(s=1\) subfamily of the full rational-square scaling \(r^2/s^2\).

## Limitations
The classification depends on requiring the square identity for every sufficiently large integer parameter. It does not classify isolated solutions or families supported on a thin subsequence of parameters. The proof uses the prime number theorem to separate unequal slopes; it does not supply an effective threshold in terms of the affine coefficients. Search and source inspection cannot exclude an equivalent unindexed formulation, particularly in older factorial-product literature, although the directly relevant four-factor pages of Erdős--Graham and the modern affine construction were materially inspected.

## References
1. F. Yudin, *Square products of factorials and a conjecture of Erdős and Graham*, arXiv:2610.01899v1, 1 October 2026. Primary MSC 11D85.
2. P. Erdős, R. L. Graham, *On products of factorials*, Bulletin of the Institute of Mathematics Academia Sinica 4 (1976), 337--355.
3. A. Bérczes, A. Dujella, L. Hajdu, N. Saradha, R. Tijdeman, *Products of factorials which are powers*, Annales Mathematicae et Informaticae 50 (2019), 1--13.
4. A. Dujella, F. Najman, N. Saradha, T. N. Shorey, *Products of three factorials*, Publicationes Mathematicae Debrecen 85 (2014), 123--130, DOI 10.5486/PMD.2014.5835.
